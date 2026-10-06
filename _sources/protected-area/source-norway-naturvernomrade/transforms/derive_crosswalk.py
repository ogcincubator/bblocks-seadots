#!/usr/bin/env python3
"""Step 3: confirm the verneform -> EEA designation crosswalk from data, not labels.

Joins the Norwegian source snapshot with the EMODnet snapshot on
naturvernId = nationalid and tabulates verneform x designatio (and iucn x iucncatego).
A verneform whose sites map to one designatio in (almost) all joined pairs is
confirmed; a split distribution points to a crosswalk error or, as for Møysalen,
to an error in the EEA reporting chain. Reads the GeoPackages' attribute tables
with the standard-library sqlite3 module (no GDAL / SpatiaLite needed).

Usage:
  derive_crosswalk.py seadots_geonorge_naturvernomrader_marine_4326.gpkg \
                      seadots_emodnet_norway_marine_protected_areas.gpkg \
                      [--source-table naturvern_omrade_marine] \
                      [--emodnet-table nationallydesignatedareas_NO_marine] [--csv out.csv]
"""
import argparse, collections, csv, sqlite3, sys


def rows(path, table, cols):
    con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    q = "SELECT " + ", ".join(f'"{c}"' for c in cols) + f' FROM "{table}"'
    try:
        return con.execute(q).fetchall()
    finally:
        con.close()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source_gpkg")
    ap.add_argument("emodnet_gpkg")
    ap.add_argument("--source-table", default="naturvern_omrade_marine")
    ap.add_argument("--emodnet-table", default="nationallydesignatedareas_NO_marine")
    ap.add_argument("--csv", help="write the confirmed crosswalk table here")
    a = ap.parse_args()

    src = {nid: (vf, iucn) for nid, vf, iucn in rows(a.source_gpkg, a.source_table, ["naturvernId", "verneform", "iucn"])}
    emo = {nid: (d, i) for nid, d, i in rows(a.emodnet_gpkg, a.emodnet_table, ["nationalid", "designatio", "iucncatego"]) if nid}

    desig = collections.defaultdict(collections.Counter)
    iucn = collections.defaultdict(collections.Counter)
    for nid, (vf, iu) in src.items():
        if nid in emo:
            desig[vf][emo[nid][0]] += 1
            iucn[iu][emo[nid][1]] += 1

    out = []
    print(f"joined sites: {sum(sum(c.values()) for c in desig.values())} "
          f"(source {len(src)}, EMODnet {len(emo)})")
    for vf, c in sorted(desig.items()):
        top, n = c.most_common(1)[0]
        share = n / sum(c.values())
        status = "confirmed" if share >= 0.98 else "SPLIT - review"
        print(f"{vf:48s} -> {top:5s} {n}/{sum(c.values())} {status}  {dict(c)}")
        out.append({"verneform": vf, "designatio": top, "pairs": sum(c.values()), "share": round(share, 3), "status": status})
    print()
    for iu, c in sorted(iucn.items()):
        print(f"{iu:12s} -> {dict(c)}")
    only_src = sorted(set(src) - set(emo))
    print(f"\nin source but not in EMODnet ({len(only_src)}): {', '.join(only_src[:20])}{' ...' if len(only_src) > 20 else ''}")
    if a.csv:
        with open(a.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(out[0]))
            w.writeheader(); w.writerows(out)


if __name__ == "__main__":
    sys.exit(main())
