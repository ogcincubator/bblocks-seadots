#!/usr/bin/env python3
"""
Extract OIM file-write variables from indicators.ttl.

Runs a single SPARQL SELECT against the SKOS-encoded register and prints,
for each NetLogo file-write code, the matching concept IRI, type, prefLabel,
definition, scheme, and any skos:broader / skos:narrower links.

Usage:
    python extract_indicators.py [--ttl path/to/indicators.ttl] [--format table|tsv|json] [--out file]

Defaults:
    --ttl     examples/indicators.ttl   (relative to this script)
    --format  table
    --out     stdout
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from rdflib import Graph

# --- Codes to look up --------------------------------------------------------
# Original NetLogo file-write variable names. Both legacy and corrected
# spellings are included so the query is robust to upstream renames.
CODES: list[str] = [
    "repetitions", "ticks", "current_herring_season", "current_management_season",
    "current_TAC_herring", "TAC_herring_share_sv", "even_dispersal_rate",
    "winter_dispersal_rate", "spawning_dispersal_rate", "winter_closure_type",
    "spawning_closure_type", "trawling_limit", "fishing_algorithm",
    "current_year", "current_month", "year_tick",
    "herring_price_fish_meal", "sprat_price", "fuel_price",
    "fuel_consumption_SV", "fuel_consumption_LV", "stop_herring_growth",
    "mean_biomass_herring", "mean_biomas_sprat", "mean_biomass_sprat",
    "landing_value_herring_SV", "landing_value_herring_LV",
    "landing_value_sprat_SV",
    "landing-value_sprat_LV", "landing_value_sprat_LV",
    "catch_herring_SV_All", "catch_herring_LV_All",
    "catch_sprat_SV_All", "catch_sprat_LV_All",
    "VA_SV_All", "VA_LV_All",
    "yearly_growth_herring", "winter_closure_length",
    "TAC_share_B_herring", "B_herring_tot", "K_herring_reg_inc",
    "TAC_herring_Sweden_impl", "herring_price_human_cons",
    "SV_herring_market", "TAC_herring_est_error", "SV_fishing_radius",
    "TAC_herring_inc_SV", "TAC_herring_type",
]

# --- SPARQL query ------------------------------------------------------------
# Matches each code via skos:notation; falls back to skos:altLabel for legacy
# spellings. OPTIONALs are wrapped in COALESCE+STR inside GROUP_CONCAT to work
# around rdflib's NotBoundError on unbound optionals in aggregates.
QUERY_TEMPLATE = """
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?code ?concept ?type ?prefLabel ?definition ?scheme
       (GROUP_CONCAT(DISTINCT COALESCE(STR(?broader),  ""); SEPARATOR=" | ") AS ?broaders)
       (GROUP_CONCAT(DISTINCT COALESCE(STR(?narrower), ""); SEPARATOR=" | ") AS ?narrowers)
WHERE {
  VALUES ?code { %(values)s }

  { ?concept skos:notation ?code }
  UNION
  { ?concept skos:altLabel ?altLab . FILTER (STR(?altLab) = ?code) }

  OPTIONAL { ?concept a ?type .
             FILTER (?type IN (<http://www.w3.org/ns/sosa/ObservableProperty>,
                               <http://www.w3.org/ns/ssn/Property>,
                               <https://w3id.org/indicators/marine/Indicator>)) }
  OPTIONAL { ?concept skos:prefLabel  ?prefLabel  . FILTER (LANG(?prefLabel)  IN ("en","")) }
  OPTIONAL { ?concept skos:definition ?definition . FILTER (LANG(?definition) IN ("en","")) }
  OPTIONAL { ?concept skos:inScheme   ?scheme }
  OPTIONAL { ?concept skos:broader    ?broader }
  OPTIONAL { ?concept skos:narrower   ?narrower }
}
GROUP BY ?code ?concept ?type ?prefLabel ?definition ?scheme
ORDER BY ?code
"""


def build_query(codes: list[str]) -> str:
    values = " ".join(f'"{c}"' for c in codes)
    return QUERY_TEMPLATE % {"values": values}


def run(ttl_path: Path, codes: list[str]) -> list[dict]:
    g = Graph()
    g.parse(ttl_path, format="turtle")
    rows = g.query(build_query(codes))

    out: list[dict] = []
    for r in rows:
        code, concept, typ, label, defn, scheme, broaders, narrowers = r
        out.append({
            "code":       str(code),
            "concept":    str(concept) if concept else "",
            "type":       str(typ)     if typ     else "",
            "prefLabel":  str(label)   if label   else "",
            "definition": str(defn)    if defn    else "",
            "scheme":     str(scheme)  if scheme  else "",
            "broaders":   [b for b in str(broaders).split(" | ") if b],
            "narrowers":  [n for n in str(narrowers).split(" | ") if n],
        })
    return out


# --- Output formatters -------------------------------------------------------
def _short(uri: str) -> str:
    return uri.rsplit("/", 1)[-1] if uri else ""


def format_table(rows: list[dict]) -> str:
    if not rows:
        return "(no rows)"
    head = ("code", "concept", "type", "scheme", "broader", "narrower")
    widths = {h: len(h) for h in head}
    table = []
    for r in rows:
        row = (
            r["code"],
            _short(r["concept"]),
            _short(r["type"]),
            _short(r["scheme"]),
            ", ".join(_short(b) for b in r["broaders"])  or "-",
            ", ".join(_short(n) for n in r["narrowers"]) or "-",
        )
        for k, v in zip(head, row):
            widths[k] = max(widths[k], len(v))
        table.append(row)

    fmt = "  ".join(f"{{:<{widths[h]}}}" for h in head)
    sep = "  ".join("-" * widths[h] for h in head)
    lines = [fmt.format(*head), sep]
    lines.extend(fmt.format(*r) for r in table)
    return "\n".join(lines)


def format_tsv(rows: list[dict]) -> str:
    head = ("code", "concept", "type", "prefLabel", "definition",
            "scheme", "broaders", "narrowers")
    out_lines = ["\t".join(head)]
    for r in rows:
        out_lines.append("\t".join([
            r["code"], r["concept"], r["type"],
            r["prefLabel"].replace("\t", " "),
            r["definition"].replace("\t", " "),
            r["scheme"],
            ";".join(r["broaders"]),
            ";".join(r["narrowers"]),
        ]))
    return "\n".join(out_lines)


def format_json(rows: list[dict]) -> str:
    return json.dumps(rows, indent=2, ensure_ascii=False)


FORMATTERS = {"table": format_table, "tsv": format_tsv, "json": format_json}


# --- CLI ---------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    script_dir = Path(__file__).resolve().parent
    default_ttl = script_dir / "examples" / "indicators.ttl"

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--ttl", type=Path, default=default_ttl,
                        help=f"Path to indicators.ttl (default: {default_ttl})")
    parser.add_argument("--format", choices=FORMATTERS.keys(), default="table",
                        help="Output format (default: table)")
    parser.add_argument("--out", type=Path,
                        help="Write to file instead of stdout")
    parser.add_argument("--codes", nargs="+",
                        help="Override the built-in code list with these codes")
    parser.add_argument("--quiet", action="store_true",
                        help="Suppress the coverage report on stderr")
    args = parser.parse_args(argv)

    if not args.ttl.is_file():
        parser.error(f"TTL not found: {args.ttl}")

    codes = args.codes if args.codes else CODES
    rows = run(args.ttl, codes)
    rendered = FORMATTERS[args.format](rows)

    if args.out:
        args.out.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)

    if not args.quiet:
        matched = {r["code"] for r in rows}
        missing = sorted(set(codes) - matched)
        print(f"\n{len(rows)} rows; {len(matched)}/{len(codes)} input codes matched.",
              file=sys.stderr)
        if missing:
            print("Missing codes:", file=sys.stderr)
            for m in missing:
                print(f"  - {m}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
