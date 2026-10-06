#!/usr/bin/env python3
"""HELCOM MPA layers (HELCOM MADS Biodiversity 54 / 190) -> EMODnet marineprotectedareas (rsc = HELCOM).

Input : GeoJSON FeatureCollection in CRS84 as served by the Seadots pygeoapi collections
        `helcom-live-mpas` (layer 54, "HELCOM MPAs") and/or
        `helcom-live-mpa-network-2026` (layer 190, "Baltic Sea MPA network 2026").
        The layer is detected per feature from its fields.
Output: GeoJSON FeatureCollection validating against
        ogc.hosted.seadots.emodnet-protected-area.rsc-mpa, plus a `seadotsTransformReport`
        member that routes layer-190 rows which are not HELCOM MPA ids to the EMODnet layer
        where they belong (natura2000areas / nationallydesignatedareas) instead of
        forcing them into this profile.

Rules
  * One feature per HELCOM MPA id: polygons sharing an id are merged into one MultiPolygon.
  * Layer 190 `Code` is classified by pattern:
      ^\\d{1,5}$                -> HELCOM MPA database id  -> this profile
      ^\\d{6,10}$               -> EEA / WDPA site id      -> emodnet:nationallydesignatedareas (natdaid)
      ^[A-Z]{2}[A-Z0-9]{7}$     -> Natura 2000 site code   -> emodnet:natura2000areas (sitecode)
      anything else            -> national code, unresolved
  * status / status_yr / link come from layer 54 (MPA_status, Year_est, Site_link). Layer-190
    rows get them by joining on the id (pass layer 54 with --mpa-register); without a match the
    status is unknown and the site is reported, not published.
Standard library only. Usage:
    to_emodnet_rsc_mpa.py source.geojson [--mpa-register layer54.geojson] > out.geojson
"""
import argparse, collections, json, math, re, sys

HELCOM_ID = re.compile(r"^\d{1,5}$")
EEA_ID = re.compile(r"^\d{6,10}$")
N2K = re.compile(r"^[A-Z]{2}[A-Z0-9]{7}$")
LINK = "http://mpas.helcom.fi/apex/f?p=103:12:::NO::P12_ID:{}"
FIELDS = ["rsc", "code", "name", "orig_name", "country", "designatio", "iucn_cat", "rep_m_area", "gis_m_area",
          "rep_area", "gis_area", "status", "status_yr", "mang_auth", "link", "shape_leng", "shape_area"]


def polygons(geom):
    return [geom["coordinates"]] if geom["type"] == "Polygon" else list(geom["coordinates"])


def planar_measures(polys):
    length = area = 0.0
    for poly in polys:
        for i, ring in enumerate(poly):
            a = 0.0
            for (x0, y0), (x1, y1) in zip(ring, ring[1:]):
                length += math.hypot(x1 - x0, y1 - y0)
                a += x0 * y1 - x1 * y0
            area += abs(a) / 2 if i == 0 else -abs(a) / 2
    return round(length, 8), round(area, 8)


def classify(code):
    c = str(code).strip()
    if HELCOM_ID.match(c):
        return "helcom-mpa-id", int(c)
    if EEA_ID.match(c):
        return "eea-site-id", int(c)
    if N2K.match(c):
        return "natura2000-sitecode", c
    return "national-code", c


def register_from(features):
    reg = {}
    for f in features:
        p = f["properties"]
        if "MPA_ID" in p and p["MPA_ID"] is not None:
            reg[int(p["MPA_ID"])] = p
    return reg


def transform(src, mpa_register=None):
    feats = src.get("features", [])
    reg = register_from(feats)
    if mpa_register:
        reg = {**register_from(mpa_register.get("features", [])), **reg}

    groups = collections.OrderedDict()                     # HELCOM MPA id -> {name, country, polys}
    report = {"routedToNatura2000": [], "routedToNationallyDesignatedAreas": [], "unresolvedCode": [],
              "noStatusInRegister": [], "mergedParts": {}}
    for f in feats:
        p = f["properties"]
        if "MPA_ID" in p:                                   # layer 54
            kind, key = "helcom-mpa-id", int(p["MPA_ID"])
        else:                                               # layer 190
            kind, key = classify(p.get("Code"))
        entry = {"code": p.get("Code", p.get("MPA_ID")), "name": p.get("Name"), "country": p.get("Country"),
                 "type": p.get("Type")}
        if kind == "natura2000-sitecode":
            report["routedToNatura2000"].append({**entry, "target": f"emodnet:natura2000areas?sitecode={key}"})
            continue
        if kind == "eea-site-id":
            report["routedToNationallyDesignatedAreas"].append({**entry, "target": f"emodnet:nationallydesignatedareas?natdaid={key}"})
            continue
        if kind == "national-code":
            report["unresolvedCode"].append(entry)
            continue
        g = groups.setdefault(key, {"name": p.get("Name"), "country": p.get("Country"), "polys": [], "n": 0})
        g["polys"].extend(polygons(f["geometry"]))
        g["n"] += 1

    out = []
    for code, g in groups.items():
        r = reg.get(code)
        if r is None or not r.get("MPA_status"):
            report["noStatusInRegister"].append({"code": code, "name": g["name"], "country": g["country"]})
            continue
        if g["n"] > 1:
            report["mergedParts"][str(code)] = g["n"]
        shape_leng, shape_area = planar_measures(g["polys"])
        props = dict.fromkeys(FIELDS)
        props.update({
            "rsc": "HELCOM", "code": code, "name": r.get("Name") or g["name"], "country": r.get("Country") or g["country"],
            "status": r["MPA_status"], "status_yr": r.get("Year_est"),
            "link": r.get("Site_link") or LINK.format(code),
            "shape_leng": shape_leng, "shape_area": shape_area,
        })
        out.append({"type": "Feature", "id": code, "geometry": {"type": "MultiPolygon", "coordinates": g["polys"]},
                    "properties": props})
    return {"type": "FeatureCollection", "features": out, "seadotsTransformReport": report}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", nargs="?")
    ap.add_argument("--mpa-register", help="layer 54 (HELCOM MPAs) GeoJSON, used to join status/year/link onto layer-190 rows")
    a = ap.parse_args()
    src = json.load(open(a.source, encoding="utf-8")) if a.source else json.load(sys.stdin)
    reg = json.load(open(a.mpa_register, encoding="utf-8")) if a.mpa_register else None
    json.dump(transform(src, reg), sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if "input_data" in globals():
    # bblocks-postprocess: `metadata.mpaRegister` in transforms.yaml names the layer-54 file, relative to
    # this building block's directory.
    import os
    _reg = transform_metadata.metadata.get("mpaRegister")
    _reg = (json.load(open(os.path.join(transform_metadata.context.bblock_files_path, _reg), encoding="utf-8"))
            if _reg else None)
    output_data = json.dumps(transform(json.loads(input_data), _reg), ensure_ascii=False, indent=2)
elif __name__ == "__main__":
    main()
