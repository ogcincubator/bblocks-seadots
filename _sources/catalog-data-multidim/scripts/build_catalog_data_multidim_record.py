#!/usr/bin/env python3
"""Build a SeaDOTs catalog-data-multidim record from a NetCDF header.

The script intentionally reads only NetCDF metadata. It never indexes variable
data arrays; optional Python backends open the dataset for metadata inspection,
and the fallback backend shells out to `ncdump -h`.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import quote


NETCDF_MEDIA_TYPE = "application/x-netcdf"
CATALOG_DATA_PROFILE = "bblocks://ogc.hosted.seadots.catalog-data"
CATALOG_DATA_MULTIDIM_PROFILE = "bblocks://ogc.hosted.seadots.catalog-data-multidim"
ILIAD_MULTIDIM_PROFILE = "bblocks://ogc.hosted.iliad.api.features.stac_multidim_data"


@dataclass
class VariableHeader:
    name: str
    dtype: str | None = None
    dimensions: list[str] = field(default_factory=list)
    attrs: dict[str, Any] = field(default_factory=dict)


@dataclass
class NetcdfHeader:
    dimensions: dict[str, int | None] = field(default_factory=dict)
    variables: dict[str, VariableHeader] = field(default_factory=dict)
    attrs: dict[str, Any] = field(default_factory=dict)
    backend: str = "unknown"


def scalar(value: Any) -> Any:
    """Convert backend-specific scalar values to JSON-friendly Python values."""
    if hasattr(value, "tolist"):
        value = value.tolist()
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    if isinstance(value, (list, tuple)):
        return [scalar(v) for v in value]
    return value


def read_with_netcdf4(path: Path) -> NetcdfHeader:
    try:
        import netCDF4  # type: ignore
    except ImportError as exc:
        raise RuntimeError("netCDF4 is not installed") from exc

    header = NetcdfHeader(backend="netCDF4")
    with netCDF4.Dataset(path, "r") as dataset:
        header.attrs = {name: scalar(dataset.getncattr(name)) for name in dataset.ncattrs()}
        header.dimensions = {
            name: (None if dim.isunlimited() else len(dim))
            for name, dim in dataset.dimensions.items()
        }
        for name, var in dataset.variables.items():
            header.variables[name] = VariableHeader(
                name=name,
                dtype=str(var.dtype),
                dimensions=list(var.dimensions),
                attrs={attr: scalar(var.getncattr(attr)) for attr in var.ncattrs()},
            )
    return header


def read_with_h5netcdf(path: Path) -> NetcdfHeader:
    try:
        import h5netcdf  # type: ignore
    except ImportError as exc:
        raise RuntimeError("h5netcdf is not installed") from exc

    header = NetcdfHeader(backend="h5netcdf")
    with h5netcdf.File(path, "r", decode_vlen_strings=True) as dataset:
        header.attrs = {name: scalar(value) for name, value in dataset.attrs.items()}
        for name, dim in dataset.dimensions.items():
            size = getattr(dim, "size", None)
            if size is None:
                try:
                    size = len(dim)
                except TypeError:
                    size = None
            header.dimensions[name] = size
        for name, var in dataset.variables.items():
            header.variables[name] = VariableHeader(
                name=name,
                dtype=str(getattr(var, "dtype", "")) or None,
                dimensions=list(getattr(var, "dimensions", [])),
                attrs={attr: scalar(value) for attr, value in var.attrs.items()},
            )
    return header


def parse_ncdump_value(raw: str) -> Any:
    raw = raw.strip().rstrip(";")
    values: list[str] = []
    token = ""
    in_string = False
    escape = False
    for char in raw:
        if escape:
            token += char
            escape = False
            continue
        if char == "\\" and in_string:
            escape = True
            continue
        if char == '"':
            in_string = not in_string
            continue
        if char == "," and not in_string:
            values.append(token.strip())
            token = ""
            continue
        token += char
    if token.strip() or raw == "":
        values.append(token.strip())

    parsed = [parse_atom(value) for value in values]
    return parsed[0] if len(parsed) == 1 else parsed


def parse_atom(value: str) -> Any:
    if value in {"", "_"}:
        return value
    cleaned = re.sub(r"([0-9.])([fFdDsSlLbB])$", r"\1", value)
    try:
        if re.fullmatch(r"[-+]?\d+", cleaned):
            return int(cleaned)
        if re.fullmatch(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?", cleaned):
            return float(cleaned)
    except ValueError:
        pass
    return value


def read_with_ncdump(path: Path, timeout: int) -> NetcdfHeader:
    if shutil.which("ncdump") is None:
        raise RuntimeError("ncdump is not available")

    proc = subprocess.run(
        ["ncdump", "-h", str(path)],
        check=True,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    header = NetcdfHeader(backend="ncdump")
    section: str | None = None

    var_re = re.compile(r"^\s*(?P<dtype>[\w\*]+)\s+(?P<name>[\w.-]+)\((?P<dims>[^)]*)\)\s*;")
    scalar_var_re = re.compile(r"^\s*(?P<dtype>[\w\*]+)\s+(?P<name>[\w.-]+)\s*;")
    attr_re = re.compile(r"^\s*(?:(?P<var>[\w.-]+):)?(?P<attr>[\w.-]+)\s*=\s*(?P<value>.*)")

    for line in proc.stdout.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped == "dimensions:":
            section = "dimensions"
            continue
        if stripped == "variables:":
            section = "variables"
            continue
        if stripped.startswith("// global attributes:"):
            section = "global_attrs"
            continue
        if stripped == "data:":
            break

        if section == "dimensions" and "=" in stripped:
            name, value = stripped.rstrip(";").split("=", 1)
            value = value.strip()
            header.dimensions[name.strip()] = None if value.startswith("UNLIMITED") else parse_atom(value)
            continue

        if section == "variables":
            match = var_re.match(line) or scalar_var_re.match(line)
            if match:
                dims = match.groupdict().get("dims") or ""
                header.variables[match.group("name")] = VariableHeader(
                    name=match.group("name"),
                    dtype=match.group("dtype"),
                    dimensions=[dim.strip() for dim in dims.split(",") if dim.strip()],
                )
                continue
            match = attr_re.match(line.rstrip(";"))
            if match:
                var_name = match.group("var")
                attr = match.group("attr")
                value = parse_ncdump_value(match.group("value"))
                if var_name and var_name in header.variables:
                    header.variables[var_name].attrs[attr] = value
                elif var_name:
                    header.variables.setdefault(var_name, VariableHeader(name=var_name)).attrs[attr] = value
                else:
                    header.attrs[attr] = value
                continue

        if section == "global_attrs":
            match = attr_re.match(line.rstrip(";"))
            if match:
                header.attrs[match.group("attr")] = parse_ncdump_value(match.group("value"))

    return header


def h5dump_block_value(block: list[str]) -> Any:
    values: list[str] = []
    in_data = False
    data_depth = 0
    for line in block:
        stripped = line.strip()
        if stripped == "DATA {":
            in_data = True
            data_depth = 1
            continue
        if not in_data:
            continue
        data_depth += stripped.count("{") - stripped.count("}")
        if data_depth <= 0:
            break
        if "DATASET " in stripped:
            continue
        match = re.search(r"\(\d+\):\s*(.*)", stripped)
        if match:
            values.append(match.group(1).rstrip(","))
        elif values:
            values.append(stripped.rstrip(","))
    if not values:
        return None
    return parse_ncdump_value(", ".join(values))


def read_with_h5dump(path: Path, timeout: int) -> NetcdfHeader:
    if shutil.which("h5dump") is None:
        raise RuntimeError("h5dump is not available")

    proc = subprocess.run(
        ["h5dump", "-H", "-A", str(path)],
        check=True,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    header = NetcdfHeader(backend="h5dump")
    lines = proc.stdout.splitlines()
    brace_depth = 0
    current_dataset: str | None = None
    current_dataset_depth: int | None = None
    index = 0
    attr_start_re = re.compile(r'^\s*ATTRIBUTE\s+"(?P<name>[^"]+)"\s+\{')
    dataset_start_re = re.compile(r'^\s*DATASET\s+"(?P<name>[^"]+)"\s+\{')
    dataspace_re = re.compile(r"DATASPACE\s+SIMPLE\s+\{\s+\(\s*(?P<dims>[^)]*?)\s*\)")

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        dataset_match = dataset_start_re.match(line)
        if dataset_match:
            current_dataset = dataset_match.group("name")
            current_dataset_depth = brace_depth + line.count("{") - line.count("}")
            header.variables.setdefault(current_dataset, VariableHeader(name=current_dataset))

        attr_match = attr_start_re.match(line)
        if attr_match:
            attr_name = attr_match.group("name")
            block = [line]
            depth = line.count("{") - line.count("}")
            index += 1
            while index < len(lines) and depth > 0:
                block.append(lines[index])
                depth += lines[index].count("{") - lines[index].count("}")
                index += 1
            value = h5dump_block_value(block)
            if value is not None:
                if current_dataset:
                    header.variables.setdefault(current_dataset, VariableHeader(name=current_dataset)).attrs[attr_name] = value
                else:
                    header.attrs[attr_name] = value
            continue

        if current_dataset:
            dataspace_match = dataspace_re.search(stripped)
            if dataspace_match:
                dims = []
                for part in dataspace_match.group("dims").split(","):
                    part = part.strip()
                    if part:
                        dims.append(parse_atom(part))
                dim_names = [f"dim_{pos}" for pos, _ in enumerate(dims)]
                header.variables[current_dataset].dimensions = dim_names
                for name, size in zip(dim_names, dims, strict=False):
                    if isinstance(size, int):
                        header.dimensions.setdefault(name, size)

        brace_depth += line.count("{") - line.count("}")
        if current_dataset and current_dataset_depth is not None and brace_depth < current_dataset_depth:
            current_dataset = None
            current_dataset_depth = None
        index += 1

    return header


def read_header(path: Path, backend: str, timeout: int) -> NetcdfHeader:
    attempts = []
    backends = [backend] if backend != "auto" else ["netCDF4", "h5netcdf", "h5dump", "ncdump"]
    for candidate in backends:
        try:
            if candidate == "netCDF4":
                return read_with_netcdf4(path)
            if candidate == "h5netcdf":
                return read_with_h5netcdf(path)
            if candidate == "ncdump":
                return read_with_ncdump(path, timeout)
            if candidate == "h5dump":
                return read_with_h5dump(path, timeout)
            raise RuntimeError(f"Unknown backend: {candidate}")
        except Exception as exc:  # noqa: BLE001 - keep backend errors for CLI diagnostics.
            attempts.append(f"{candidate}: {exc}")
    raise RuntimeError("Could not read NetCDF header. Attempts: " + "; ".join(attempts))


def first_text(*values: Any) -> str | None:
    for value in values:
        if value is None:
            continue
        if isinstance(value, list):
            value = ", ".join(str(v) for v in value if v is not None)
        text = str(value).strip()
        if text:
            return text
    return None


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "netcdf-dataset"


def path_href(path: Path) -> str:
    try:
        return path.resolve().as_uri()
    except ValueError:
        return quote(str(path))


def variable_role(name: str, variable: VariableHeader) -> str:
    attrs = {key.lower(): str(value).lower() for key, value in variable.attrs.items()}
    standard_name = attrs.get("standard_name", "")
    axis = attrs.get("axis", "")
    units = attrs.get("units", "")
    coordinate_names = {"time", "lat", "latitude", "lon", "longitude", "x", "y", "z", "depth"}
    if name.lower() in coordinate_names or axis in {"t", "x", "y", "z"}:
        return "coordinate"
    if standard_name in {"time", "latitude", "longitude", "depth"}:
        return "coordinate"
    if " since " in units:
        return "coordinate"
    return "data"


def data_variables(header: NetcdfHeader, limit: int) -> list[VariableHeader]:
    variables = [
        variable
        for variable in header.variables.values()
        if variable_role(variable.name, variable) == "data"
    ]
    variables.sort(key=lambda var: (len(var.dimensions), var.name), reverse=True)
    return variables[:limit]


def cf_parameters(variables: list[VariableHeader]) -> list[dict[str, Any]]:
    params = []
    for variable in variables:
        attrs = variable.attrs
        param: dict[str, Any] = {
            "name": str(first_text(attrs.get("standard_name"), variable.name)),
            "schema": "http://vocab.nerc.ac.uk/standard_name/",
        }
        unit = first_text(attrs.get("units"))
        description = first_text(attrs.get("long_name"), attrs.get("description"), attrs.get("comment"))
        if unit:
            param["unit"] = unit
        if description:
            param["description"] = description
        params.append(param)
    return params


def variables_property(variables: list[VariableHeader]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for variable in variables:
        attrs = variable.attrs
        name = variable.name
        result[name] = {
            "title": first_text(attrs.get("long_name"), attrs.get("standard_name"), name),
            "description": first_text(attrs.get("description"), attrs.get("comment"), attrs.get("long_name"), name),
        }
        unit = first_text(attrs.get("units"))
        if unit:
            result[name]["unit"] = unit
    return result


def parse_float_attr(value: Any) -> float | None:
    if isinstance(value, list) and value:
        value = value[0]
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def bbox_from_attrs(header: NetcdfHeader) -> list[float] | None:
    aliases = {
        "west": ["geospatial_lon_min", "westernmost_longitude", "lon_min", "xmin"],
        "east": ["geospatial_lon_max", "easternmost_longitude", "lon_max", "xmax"],
        "south": ["geospatial_lat_min", "southernmost_latitude", "lat_min", "ymin"],
        "north": ["geospatial_lat_max", "northernmost_latitude", "lat_max", "ymax"],
    }
    values: dict[str, float] = {}
    lower_attrs = {key.lower(): value for key, value in header.attrs.items()}
    for target, names in aliases.items():
        for name in names:
            number = parse_float_attr(lower_attrs.get(name))
            if number is not None:
                values[target] = number
                break
    if set(values) == {"west", "east", "south", "north"}:
        return [values["west"], values["south"], values["east"], values["north"]]
    return None


def geometry_from_bbox(bbox: list[float] | None) -> dict[str, Any] | None:
    if not bbox:
        return None
    west, south, east, north = bbox
    return {
        "type": "Polygon",
        "coordinates": [[
            [west, south],
            [east, south],
            [east, north],
            [west, north],
            [west, south],
        ]],
    }


def normalize_datetime(value: Any) -> str | None:
    text = first_text(value)
    if not text:
        return None
    text = text.replace(" ", "T")
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        return text + "T00:00:00Z"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:Z|[+-]\d{2}:\d{2})?", text):
        return text if text.endswith("Z") or re.search(r"[+-]\d{2}:\d{2}$", text) else text + "Z"
    return None


def normalize_license(value: Any) -> str:
    text = first_text(value)
    if not text:
        return "proprietary"
    spdx_match = re.search(r"/licenses/([^/#?]+)", text)
    if spdx_match:
        return spdx_match.group(1).removesuffix(".html")
    if re.fullmatch(r"[\w\-\.\+]+", text):
        return text
    return "proprietary"


def temporal_extent(header: NetcdfHeader) -> tuple[str | None, str | None, str]:
    lower_attrs = {key.lower(): value for key, value in header.attrs.items()}
    start = normalize_datetime(first_text(lower_attrs.get("time_coverage_start"), lower_attrs.get("geospatial_time_min")))
    end = normalize_datetime(first_text(lower_attrs.get("time_coverage_end"), lower_attrs.get("geospatial_time_max")))
    midpoint = start or end or dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return start, end, midpoint


def build_record(path: Path, header: NetcdfHeader, args: argparse.Namespace) -> dict[str, Any]:
    slug = slugify(args.id or path.stem)
    title = first_text(args.title, header.attrs.get("title"), path.stem) or path.stem
    description = first_text(
        args.description,
        header.attrs.get("summary"),
        header.attrs.get("description"),
        header.attrs.get("comment"),
        f"Catalog record generated from the NetCDF header of {path.name}.",
    )
    selected_variables = data_variables(header, args.max_variables)
    params = cf_parameters(selected_variables)
    bbox = bbox_from_attrs(header)
    start_datetime, end_datetime, datetime_value = temporal_extent(header)

    properties: dict[str, Any] = {
        "title": title,
        "description": description,
        "datetime": datetime_value,
        "keywords": ["SeaDOTs", "multidimensional", "NetCDF", "CF"],
        "license": normalize_license(first_text(args.license, header.attrs.get("license"), header.attrs.get("licence"))),
        "role": args.role,
        "convention": first_text(header.attrs.get("Conventions"), header.attrs.get("conventions"), "CF"),
        "formats": [{"name": "NetCDF", "mediaType": NETCDF_MEDIA_TYPE}],
        "variables": variables_property(selected_variables),
    }
    if start_datetime:
        properties["start_datetime"] = start_datetime
    if end_datetime:
        properties["end_datetime"] = end_datetime
    if params:
        properties["cf:parameter"] = params

    record: dict[str, Any] = {
        "id": args.id or f"https://w3id.org/ogc/hosted/seadots/catalog/dataset/{slug}",
        "type": "Feature",
        "itemType": "record",
        "stac_version": "1.0.0",
        "stac_extensions": [
            "https://stac-extensions.github.io/datacube/v2.2.0/schema.json",
            "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
            "https://stac-extensions.github.io/prov/v1.0.0/schema.json",
        ],
        "geometry": geometry_from_bbox(bbox),
        "properties": properties,
        "assets": {
            args.asset_key: {
                "href": args.href or path_href(path),
                "type": NETCDF_MEDIA_TYPE,
                "title": args.asset_title,
                "roles": ["data"],
            }
        },
        "links": [
            {
                "rel": "describedby",
                "href": CATALOG_DATA_PROFILE,
                "type": "application/schema+json",
                "title": "SeaDOTs Catalog Data bblock",
            },
            {
                "rel": "describedby",
                "href": CATALOG_DATA_MULTIDIM_PROFILE,
                "type": "application/schema+json",
                "title": "SeaDOTs Catalog Data Multidimensional bblock",
            },
            {
                "rel": "profile",
                "href": ILIAD_MULTIDIM_PROFILE,
                "type": "application/schema+json",
                "title": "ILIAD STAC/DCAT multidimensional data profile",
            },
        ],
    }
    if bbox:
        record["bbox"] = bbox
    if args.collection:
        record["collection"] = args.collection
        record["links"].append({"rel": "collection", "href": args.collection, "type": "application/json"})
    if params:
        record["assets"][args.asset_key]["cf:parameter"] = params
    if args.include_header_summary:
        properties["netcdf:header"] = {
            "backend": header.backend,
            "dimensions": header.dimensions,
            "variableCount": len(header.variables),
            "selectedVariables": [var.name for var in selected_variables],
        }
    return record


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a catalog-data-multidim STAC/OGC Record from a NetCDF header."
    )
    parser.add_argument("netcdf", type=Path, help="Path to the NetCDF file.")
    parser.add_argument("-o", "--output", type=Path, help="Write JSON to this path instead of stdout.")
    parser.add_argument("--backend", choices=["auto", "netCDF4", "h5netcdf", "ncdump", "h5dump"], default="auto")
    parser.add_argument("--timeout", type=int, default=60, help="Timeout in seconds for CLI metadata backends.")
    parser.add_argument("--id", help="Record id. Defaults to a SeaDOTs w3id based on the file name.")
    parser.add_argument("--title", help="Record title. Defaults to NetCDF global title or file stem.")
    parser.add_argument("--description", help="Record description. Defaults to summary/description/comment metadata.")
    parser.add_argument("--href", help="Asset href. Defaults to a file:// URI for the input path.")
    parser.add_argument("--asset-key", default="netcdf", help="STAC asset key.")
    parser.add_argument("--asset-title", default="NetCDF data cube", help="STAC asset title.")
    parser.add_argument("--role", choices=["data", "input", "output"], default="data")
    parser.add_argument("--license", help="Record license. Defaults to global license/licence metadata.")
    parser.add_argument("--collection", help="Optional STAC collection id or URI.")
    parser.add_argument("--max-variables", type=int, default=12, help="Maximum data variables to expose.")
    parser.add_argument(
        "--include-header-summary",
        action="store_true",
        help="Include dimensions and selected variable names in properties.netcdf:header.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if not args.netcdf.exists():
        print(f"NetCDF file does not exist: {args.netcdf}", file=sys.stderr)
        return 2
    try:
        header = read_header(args.netcdf, args.backend, args.timeout)
        record = build_record(args.netcdf, header, args)
    except Exception as exc:  # noqa: BLE001 - CLI should report concise diagnostics.
        print(f"Could not generate record: {exc}", file=sys.stderr)
        return 1

    text = json.dumps(record, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
