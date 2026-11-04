"""Regression checks for source preservation and the OSM-to-EMODnet mappings."""
import json
import runpy
from pathlib import Path


HERE = Path(__file__).resolve().parents[1]
source_path = HERE.parent / "windfarm-openstreetmap" / "examples" / "osm-polish-offshore-wind-2026-10-27.geojson"
expected_path = HERE / "examples" / "osm-polish-offshore-wind-harmonized.geojson"
source = json.loads(source_path.read_text(encoding="utf-8"))
namespace = runpy.run_path(
    str(HERE / "transforms" / "to_emodnet_windfarm.py"),
    init_globals={"input_data": json.dumps(source, ensure_ascii=False)},
)
actual = json.loads(namespace["output_data"])
expected = json.loads(expected_path.read_text(encoding="utf-8"))

assert actual == expected
assert set(actual) == set(source)
assert actual["type"] == source["type"]
assert actual["source"] == source["source"]
assert len(actual["features"]) == len(source["features"]) == 292

source_by_id = {feature["id"]: feature for feature in source["features"]}
target_by_id = {feature["id"]: feature for feature in actual["features"]}
assert source_by_id.keys() == target_by_id.keys()
for source_feature_id, source_feature in source_by_id.items():
    target_feature = target_by_id[source_feature_id]
    assert target_feature["geometry"] == source_feature["geometry"]
    for key, value in source_feature["properties"].items():
        assert target_feature["properties"][key] == value

relation = target_by_id["relation/21402440"]
assert relation["geometry"] is None
assert relation["properties"]["members"] == source_by_id["relation/21402440"]["properties"]["members"]
assert relation["properties"]["name"] == "Baltic Power"
assert relation["properties"]["power_mw"] == 1200.0
assert relation["properties"]["category_of_offshore_production_area"] == 1

ba_tyk_ii = target_by_id["way/1560132096"]["properties"]
assert ba_tyk_ii["name"] == "MFW Bałtyk II Offshore Wind Farm"
assert ba_tyk_ii["power_mw"] == 720.0
assert ba_tyk_ii["year"] == "2027"
assert ba_tyk_ii["n_turbines"] == 50
assert ba_tyk_ii["category_of_offshore_production_area"] == 1
assert ba_tyk_ii["iho_feature_role"].endswith("#OffshoreProductionArea")

for source_feature_id in (
    "way/1560132096",
    "way/1560193204",
    "way/1560193205",
    "way/1532855580",
    "relation/21402440",
):
    assert target_by_id[source_feature_id]["properties"]["category_of_offshore_production_area"] == 1

wind_turbine = next(
    feature for feature in actual["features"]
    if feature["properties"]["tags"].get("generator:method") == "wind_turbine"
)
assert wind_turbine["properties"]["iho_feature_role"].endswith("#WindTurbine")
assert "category_of_offshore_production_area" not in wind_turbine["properties"]
assert all(
    "category_of_offshore_production_area" not in feature["properties"]
    for feature in actual["features"]
    if feature["properties"]["osm_type"] == "node"
)

unlabeled_turbine = next(
    feature for feature in actual["features"]
    if feature["properties"]["osm_type"] == "node"
    and "generator:output:electricity" in feature["properties"]["tags"]
)
assert unlabeled_turbine["properties"]["power_mw"] in (14.0, 15.0)
assert "category_of_offshore_production_area" not in unlabeled_turbine["properties"]
print("OSM-to-EMODnet transform checks passed for all 292 source features")
