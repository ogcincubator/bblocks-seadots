#!/usr/bin/env python3
"""Naturvernområder (Miljødirektoratet, vern layer 0) -> EMODnet nationallydesignatedareas.

Input : GeoJSON FeatureCollection in CRS84 as served by the Seadots pygeoapi
        collections `no-live-naturvern-omrade` (ESRI provider) or
        `no-snapshot-naturvern-omrade-marine` (GeoPackage), or by ArcGIS REST f=geojson.
Output: GeoJSON FeatureCollection whose features validate against
        ogc.hosted.seadots.emodnet-protected-area.nationally-designated-area.
        Excluded / incomplete sites are reported in the collection member
        `seadotsTransformReport` (not part of the EMODnet schema; strip it if a
        strict EMODnet collection document is needed).

Standard library only, so it runs inside the pygeoapi container and in the
building-blocks CI. Usage:
    to_emodnet_nda.py [source.geojson] [--retrieved YYYY-MM-DD]
                      [--metadata-url URL] [--emodnet-reference emodnet.geojson] > out.geojson
Reads stdin when no source file is given.
"""
import argparse, csv, datetime as dt, json, math, os, sys

if "__file__" in globals():
    BBLOCK_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
else:                                       # run by bblocks-postprocess: no __file__, cwd = repo root
    BBLOCK_DIR = transform_metadata.context.bblock_files_path
XWALK = os.path.join(BBLOCK_DIR, "crosswalk")
NAMESPACE = "http://www.miljodirektoratet.no/naturbase"
DEFAULT_METADATA = "https://kartkatalog.geonorge.no/metadata/5857ec0a-8d2c-4cd8-baa2-0dc54ae213b4"

FIELDS = ["natdaid", "countrycod", "country", "regioncode", "sitename", "legalfound", "localid", "namespace",
          "versionid", "metadata_v", "metadata_b", "metadata_s", "metadata_f", "metadata_1", "geomtype", "id",
          "coast_mar", "nationalid", "designated", "designatio", "iucncatego", "iucndesc", "iucnlink", "sitearea",
          "majorecosy", "marinearea", "spatialdat", "spatialres", "pslocalid", "psnamespac", "psversioni",
          "remark", "shape_leng", "shape_area"]


def load_csv(name, key):
    with open(os.path.join(XWALK, name), newline="", encoding="utf-8") as f:
        return {row[key]: row for row in csv.DictReader(f)}


def pick(p, *names):
    """First present value among alternative source field names (live ArcGIS vs GeoPackage snapshot)."""
    for n in names:
        if n in p and p[n] is not None:
            return p[n]
    return None


def year_of(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):                     # ArcGIS epoch milliseconds
        return dt.datetime.fromtimestamp(v / 1000, dt.timezone.utc).year
    return int(str(v)[:4])                              # ISO 8601 string from GeoPackage / pygeoapi


def rings(geom):
    if geom["type"] == "Polygon":
        return [geom["coordinates"]]
    if geom["type"] == "MultiPolygon":
        return geom["coordinates"]
    raise ValueError(f"unsupported geometry {geom['type']}")


def planar_measures(geom):
    """Perimeter (deg) and area (deg^2) on lon/lat coordinates, as EMODnet's shape_leng/shape_area."""
    length = area = 0.0
    for poly in rings(geom):
        for i, ring in enumerate(poly):
            a = 0.0
            for (x0, y0), (x1, y1) in zip(ring, ring[1:]):
                length += math.hypot(x1 - x0, y1 - y0)
                a += x0 * y1 - x1 * y0
            area += abs(a) / 2 if i == 0 else -abs(a) / 2   # outer ring minus holes
    return round(length, 8), round(area, 8)


def as_multipolygon(geom):
    return {"type": "MultiPolygon", "coordinates": rings(geom)}


def transform(src, retrieved, metadata_url, emodnet_ref=None):
    desig = load_csv("verneform-designation.csv", "verneform")
    iucn = load_csv("iucn.csv", "iucn")
    eco = load_csv("ecosystem.csv", "majorEcosystemType")
    ref = {}
    if emodnet_ref:
        for f in emodnet_ref.get("features", []):
            nid = f["properties"].get("nationalid")
            if nid:
                ref[nid] = f["properties"]

    out, report = [], {"excluded": [], "notYetReportedToEEA": [], "needsMarineAreaOverlay": [],
                       "inferredDesignation": [], "differsFromEMODnet": []}
    for feat in src.get("features", []):
        p = feat["properties"]
        nid = p.get("naturvernId")
        verneform = p.get("verneform")
        d = desig.get(verneform)
        if not d or not d["designatio"]:
            report["excluded"].append({"nationalid": nid, "reason": f"verneform {verneform!r} has no EEA designation type"})
            continue
        e = eco.get(p.get("majorEcosystemType"))
        if e is None or e["majorecosy"] == "Terrestrial":
            report["excluded"].append({"nationalid": nid, "reason": "not marine (EMODnet view is limited to marine sites)"})
            continue
        i = iucn.get(p.get("iucn") or "IkkeVurdert", iucn["IkkeVurdert"])
        cdda = p.get("cddaId")
        natdaid = int(cdda) if cdda not in (None, "") else None
        area_m2 = pick(p, "SHAPE.STArea()", "SHAPE_STArea", "Shape_Area")
        marine = e["marinearea"]
        shape_leng, shape_area = planar_measures(feat["geometry"])

        props = dict.fromkeys(FIELDS)
        props.update({
            "natdaid": natdaid, "countrycod": "NO", "country": "Norway", "regioncode": "NO",
            "sitename": p.get("navn"), "legalfound": year_of(pick(p, "vernedato")),
            "localid": nid, "namespace": NAMESPACE, "metadata_v": metadata_url, "metadata_b": retrieved,
            "geomtype": "polygon", "coast_mar": 1, "nationalid": nid, "designated": "Designated site",
            "designatio": d["designatio"], "iucncatego": i["iucncatego"], "iucndesc": i["iucndesc"],
            "sitearea": round(area_m2 / 10000, 2) if area_m2 is not None else None,
            "majorecosy": e["majorecosy"], "marinearea": float(marine) if marine != "" else None,
            "spatialdat": "public", "spatialres": "Scale larger 100K",
            "pslocalid": nid, "psnamespac": NAMESPACE, "shape_leng": shape_leng, "shape_area": shape_area,
        })

        # Step 4 enrichment: marine share of mixed sites needs a coastline overlay. When an EMODnet
        # reference record exists for the same site, reuse its value and say so in the report.
        r = ref.get(nid)
        if props["marinearea"] is None:
            if r and r.get("marinearea") is not None:
                props["marinearea"] = r["marinearea"]
            else:
                report["needsMarineAreaOverlay"].append(nid)
        if natdaid is None:
            report["notYetReportedToEEA"].append(nid)
        if d["confidence"] == "inferred":
            report["inferredDesignation"].append({"nationalid": nid, "verneform": verneform, "designatio": d["designatio"]})
        if r:
            diffs = {k: {"source": props[k], "emodnet": r.get(k)} for k in
                     ("natdaid", "sitename", "legalfound", "designatio", "iucncatego", "majorecosy", "sitearea")
                     if r.get(k) != props[k] and not (k == "sitearea" and r.get(k) is not None and props[k] is not None
                                                      and abs(r[k] - props[k]) < 0.05)}
            if diffs:
                report["differsFromEMODnet"].append({"nationalid": nid, "fields": diffs})

        out.append({"type": "Feature", "id": natdaid if natdaid is not None else f"NO-{nid}",
                    "geometry": as_multipolygon(feat["geometry"]), "properties": props})

    return {"type": "FeatureCollection", "features": out, "seadotsTransformReport": report}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", nargs="?")
    ap.add_argument("--retrieved", default=dt.date.today().isoformat())
    ap.add_argument("--metadata-url", default=DEFAULT_METADATA)
    ap.add_argument("--emodnet-reference", help="EMODnet nationallydesignatedareas GeoJSON for the same sites (optional)")
    a = ap.parse_args()
    src = json.load(open(a.source, encoding="utf-8")) if a.source else json.load(sys.stdin)
    ref = json.load(open(a.emodnet_reference, encoding="utf-8")) if a.emodnet_reference else None
    json.dump(transform(src, a.retrieved, a.metadata_url, ref), sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if "input_data" in globals():
    # bblocks-postprocess: options come from the `metadata` of the transform in transforms.yaml,
    # file paths in it are relative to this building block's directory.
    _m = transform_metadata.metadata
    _ref = _m.get("emodnetReference")
    _ref = json.load(open(os.path.join(BBLOCK_DIR, _ref), encoding="utf-8")) if _ref else None
    output_data = json.dumps(transform(json.loads(input_data), _m.get("retrieved", dt.date.today().isoformat()),
                                       _m.get("metadataUrl", DEFAULT_METADATA), _ref), ensure_ascii=False, indent=2)
elif __name__ == "__main__":
    main()
