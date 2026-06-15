#!/usr/bin/env python3
"""Convert the Swedish DT whitespace CSV example to semantic GeoParquet.

The converter reads a GeoParquet header JSON document that contains CSVW-style
`propertyUrl` annotations for every physical column. It preserves the physical
column names, expands compact semantic URLs through the inline JSON-LD context,
and writes the expanded semantic links into both file-level CSVW metadata and
per-field Arrow metadata.

If an MCP server command is supplied, the script asks that server to resolve the
header meanings first. The local JSON-LD context is used as the deterministic
fallback, or as the source of truth when no MCP command is supplied.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import struct
import subprocess
import sys
from pathlib import Path
from typing import Any

pa: Any = None
pq: Any = None


DEFAULT_BASE_DIR = Path(__file__).resolve().parent
DEFAULT_CSV = DEFAULT_BASE_DIR / "simulation_1.csv"
DEFAULT_HEADER = DEFAULT_BASE_DIR / "simulation_1.geoparquet-header.json"
DEFAULT_OUTPUT = DEFAULT_BASE_DIR / "simulation_1.geoparquet"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a Swedish DT simulation CSV to semantic GeoParquet."
    )
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--header", type=Path, default=DEFAULT_HEADER)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--mcp-command",
        help=(
            "Optional MCP server command. The command is started over stdio and "
            "called with --mcp-tool to resolve column propertyUrl values."
        ),
    )
    parser.add_argument(
        "--mcp-tool",
        default="resolve_headers",
        help="MCP tool name used to resolve header meanings. Default: resolve_headers.",
    )
    parser.add_argument(
        "--require-mcp",
        action="store_true",
        help="Fail instead of falling back to inline JSON-LD context if MCP fails.",
    )
    return parser.parse_args()


def require_pyarrow() -> None:
    global pa, pq
    try:
        import pyarrow as pyarrow
        import pyarrow.parquet as parquet
    except ImportError as exc:
        raise SystemExit(
            "This script requires pyarrow. Install it with: "
            "python3 -m pip install pyarrow"
        ) from exc
    pa = pyarrow
    pq = parquet


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def context_terms(context: Any) -> dict[str, Any]:
    if isinstance(context, list):
        terms: dict[str, Any] = {}
        for item in context:
            terms.update(context_terms(item))
        return terms
    if isinstance(context, dict):
        nested = context.get("@context")
        if nested is not None:
            merged = {k: v for k, v in context.items() if k != "@context"}
            merged.update(context_terms(nested))
            return merged
        return context
    return {}


def expand_curie_or_iri(value: str, context: Any) -> str:
    if re.match(r"^[a-z][a-z0-9+.-]*://", value):
        return value
    if value.startswith("_:"):
        return value

    terms = context_terms(context)
    if value in terms:
        mapped = terms[value]
        if isinstance(mapped, str):
            return expand_curie_or_iri(mapped, context)
        if isinstance(mapped, dict) and isinstance(mapped.get("@id"), str):
            return expand_curie_or_iri(mapped["@id"], context)

    prefix, sep, suffix = value.partition(":")
    if sep and prefix in terms and isinstance(terms[prefix], str):
        return terms[prefix] + suffix

    vocab = terms.get("@vocab")
    if isinstance(vocab, str):
        return vocab + value

    return value


def local_header_meanings(header: dict[str, Any]) -> dict[str, str]:
    context = header.get("@context", {})
    meanings = {}
    for column in header["parquetSchema"]:
        name = column["name"]
        property_url = column.get("propertyUrl")
        if property_url:
            meanings[name] = expand_curie_or_iri(property_url, context)
    return meanings


def read_mcp_message(stream: Any) -> dict[str, Any]:
    headers: dict[str, str] = {}
    while True:
        line = stream.readline()
        if not line:
            raise RuntimeError("MCP server closed stdout")
        line = line.decode("utf-8").strip()
        if not line:
            break
        key, _, value = line.partition(":")
        headers[key.lower()] = value.strip()

    length = int(headers.get("content-length", "0"))
    if length <= 0:
        raise RuntimeError("MCP response missing Content-Length")
    return json.loads(stream.read(length).decode("utf-8"))


def write_mcp_message(stream: Any, message: dict[str, Any]) -> None:
    payload = json.dumps(message, separators=(",", ":")).encode("utf-8")
    stream.write(f"Content-Length: {len(payload)}\r\n\r\n".encode("utf-8"))
    stream.write(payload)
    stream.flush()


def mcp_request(proc: subprocess.Popen[bytes], message: dict[str, Any]) -> dict[str, Any]:
    assert proc.stdin is not None
    assert proc.stdout is not None
    write_mcp_message(proc.stdin, message)
    while True:
        response = read_mcp_message(proc.stdout)
        if response.get("id") == message.get("id"):
            if "error" in response:
                raise RuntimeError(json.dumps(response["error"], indent=2))
            return response["result"]


def extract_mcp_mapping(result: dict[str, Any]) -> dict[str, str]:
    if "mapping" in result and isinstance(result["mapping"], dict):
        return {str(k): str(v) for k, v in result["mapping"].items()}

    content = result.get("content")
    if isinstance(content, list):
        for item in content:
            if isinstance(item, dict) and item.get("type") == "json":
                data = item.get("json")
                if isinstance(data, dict):
                    return extract_mcp_mapping(data)
            if isinstance(item, dict) and item.get("type") == "text":
                text = item.get("text", "")
                try:
                    data = json.loads(text)
                except json.JSONDecodeError:
                    continue
                if isinstance(data, dict):
                    return extract_mcp_mapping(data)

    if all(isinstance(k, str) and isinstance(v, str) for k, v in result.items()):
        return {str(k): str(v) for k, v in result.items()}

    raise RuntimeError("MCP resolver did not return a column-to-URI mapping")


def mcp_header_meanings(
    command: str,
    tool_name: str,
    header: dict[str, Any],
) -> dict[str, str]:
    proc = subprocess.Popen(
        command,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    try:
        mcp_request(
            proc,
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2025-03-26",
                    "capabilities": {},
                    "clientInfo": {
                        "name": "swedish-dt-csv-to-geoparquet",
                        "version": "1.0.0",
                    },
                },
            },
        )
        assert proc.stdin is not None
        write_mcp_message(
            proc.stdin,
            {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}},
        )
        result = mcp_request(
            proc,
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/call",
                "params": {
                    "name": tool_name,
                    "arguments": {
                        "columns": [
                            {
                                "name": column["name"],
                                "propertyUrl": column.get("propertyUrl"),
                                "type": column.get("type"),
                            }
                            for column in header["parquetSchema"]
                        ],
                        "context": header.get("@context", {}),
                    },
                },
            },
        )
        return extract_mcp_mapping(result)
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=2)
        except subprocess.TimeoutExpired:
            proc.kill()


def resolve_header_meanings(args: argparse.Namespace, header: dict[str, Any]) -> dict[str, str]:
    local = local_header_meanings(header)
    if not args.mcp_command:
        return local

    try:
        resolved = mcp_header_meanings(args.mcp_command, args.mcp_tool, header)
    except Exception as exc:
        if args.require_mcp:
            raise
        print(f"warning: MCP resolver failed, using inline context: {exc}", file=sys.stderr)
        return local

    missing = [column["name"] for column in header["parquetSchema"] if column["name"] not in resolved]
    if missing:
        if args.require_mcp:
            raise RuntimeError(f"MCP resolver missed columns: {', '.join(missing)}")
        print(
            "warning: MCP resolver missed columns, filling from inline context: "
            + ", ".join(missing),
            file=sys.stderr,
        )
        resolved = {**local, **resolved}

    return resolved


def arrow_type(parquet_type: str) -> pa.DataType:
    normalized = parquet_type.upper()
    if normalized.startswith("INT64"):
        return pa.int64()
    if normalized.startswith("DOUBLE"):
        return pa.float64()
    if normalized.startswith("BOOLEAN"):
        return pa.bool_()
    if normalized.startswith("BYTE_ARRAY/WKB"):
        return pa.binary()
    if normalized.startswith("BYTE_ARRAY/UTF8"):
        return pa.string()
    raise ValueError(f"Unsupported parquet type: {parquet_type}")


def parse_value(value: str, data_type: pa.DataType) -> Any:
    if value == "":
        return None
    if pa.types.is_string(data_type):
        return value
    if pa.types.is_boolean(data_type):
        return value.lower() == "true"
    if pa.types.is_integer(data_type):
        return int(value)
    if pa.types.is_floating(data_type):
        parsed = float(value)
        return None if math.isnan(parsed) else parsed
    return value


def read_rows(csv_path: Path) -> tuple[list[str], list[list[str]]]:
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle, delimiter=" ", quotechar='"', skipinitialspace=True)
        rows = [[cell for cell in row if cell != ""] for row in reader if row]
    if not rows:
        raise ValueError(f"CSV is empty: {csv_path}")
    return rows[0], rows[1:]


def polygon_wkb(coordinates: list[list[list[float]]]) -> bytes:
    rings = coordinates
    payload = bytearray()
    payload.extend(struct.pack("<BI", 1, 3))
    payload.extend(struct.pack("<I", len(rings)))
    for ring in rings:
        payload.extend(struct.pack("<I", len(ring)))
        for x, y in ring:
            payload.extend(struct.pack("<dd", float(x), float(y)))
    return bytes(payload)


def build_table(
    csv_path: Path,
    header: dict[str, Any],
    meanings: dict[str, str],
) -> pa.Table:
    csv_header, rows = read_rows(csv_path)
    columns = header["parquetSchema"]
    source_names = [column["name"] for column in columns if column["name"] != "geometry"]

    if csv_header != source_names:
        missing = sorted(set(source_names) - set(csv_header))
        extra = sorted(set(csv_header) - set(source_names))
        raise ValueError(
            "CSV header does not match header parquetSchema. "
            f"Missing: {missing or 'none'}; extra: {extra or 'none'}"
        )

    by_name = {column["name"]: column for column in columns}
    values: dict[str, list[Any]] = {column["name"]: [] for column in columns}

    geometry_column = header["geo"]["primary_column"]
    geometry_meta = header["geo"]["columns"][geometry_column]
    geometry = polygon_wkb(geometry_meta["exampleGeometryGeoJSON"]["coordinates"])

    csv_index = {name: index for index, name in enumerate(csv_header)}
    for row_number, row in enumerate(rows, start=2):
        if len(row) != len(csv_header):
            raise ValueError(
                f"Row {row_number} has {len(row)} values, expected {len(csv_header)}"
            )
        for column in columns:
            name = column["name"]
            data_type = arrow_type(column["type"])
            if name == geometry_column:
                values[name].append(geometry)
            else:
                values[name].append(parse_value(row[csv_index[name]], data_type))

    arrays = []
    fields = []
    for column in columns:
        name = column["name"]
        data_type = arrow_type(column["type"])
        nullable = bool(column.get("nullable", True))
        metadata = {
            b"csvw:propertyUrl": meanings[name].encode("utf-8"),
        }
        if "description" in column:
            metadata[b"description"] = column["description"].encode("utf-8")
        fields.append(pa.field(name, data_type, nullable=nullable, metadata=metadata))
        arrays.append(pa.array(values[name], type=data_type))

    return pa.Table.from_arrays(arrays, schema=pa.schema(fields))


def geo_metadata(header: dict[str, Any]) -> dict[str, Any]:
    return header["geo"]


def csvw_metadata(header: dict[str, Any], meanings: dict[str, str]) -> dict[str, Any]:
    columns = []
    for column in header["parquetSchema"]:
        entry = {
            "name": column["name"],
            "datatype": column["type"],
            "propertyUrl": meanings[column["name"]],
        }
        if "description" in column:
            entry["description"] = column["description"]
        columns.append(entry)
    return {
        "@context": header.get("@context", {}),
        "tableSchema": {
            "columns": columns,
        },
    }


def with_file_metadata(
    table: pa.Table,
    header: dict[str, Any],
    meanings: dict[str, str],
) -> pa.Table:
    metadata = dict(table.schema.metadata or {})
    metadata.update(
        {
            b"geo": json.dumps(geo_metadata(header), separators=(",", ":")).encode("utf-8"),
            b"csvw": json.dumps(csvw_metadata(header, meanings), indent=2).encode("utf-8"),
            b"seadots:geoparquet-header": json.dumps(header, indent=2).encode("utf-8"),
        }
    )
    return table.replace_schema_metadata(metadata)


def main() -> int:
    args = parse_args()
    require_pyarrow()
    header = load_json(args.header)
    meanings = resolve_header_meanings(args, header)
    table = build_table(args.csv, header, meanings)
    table = with_file_metadata(table, header, meanings)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    pq.write_table(table, args.output, compression="zstd")
    print(f"wrote {args.output}")
    print(f"rows: {table.num_rows}")
    print(f"columns: {table.num_columns}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
