"""Add defensible EMODnet properties while preserving the complete OSM source."""
import json
import re


def as_mw(value):
    """Return numeric MW only when the tag explicitly supplies the MW unit."""
    if not isinstance(value, str):
        return None
    match = re.fullmatch(r"\s*([0-9]+(?:\.[0-9]+)?)\s*MW\s*", value, re.IGNORECASE)
    return float(match.group(1)) if match else None


def as_count(value):
    """Return an integer for an explicit whole-number count, otherwise None."""
    if not isinstance(value, str) or not re.fullmatch(r"\s*[0-9]+\s*", value):
        return None
    return int(value)


def transform(collection):
    if collection.get("type") != "FeatureCollection" or not isinstance(collection.get("features"), list):
        raise ValueError("Expected a GeoJSON FeatureCollection with a features array")
    result = dict(collection)
    features = []
    for source_feature in collection["features"]:
        feature = dict(source_feature)
        source_properties = source_feature.get("properties") or {}
        properties = dict(source_properties)
        tags = source_properties.get("tags") or {}

        # Preserve source fields and raw tags, then add only supported harmonized properties.
        name = tags.get("name") or tags.get("seamark:name")
        if name is not None:
            properties["name"] = name
        for tag_key in ("plant:output:electricity", "generator:output:electricity"):
            capacity = as_mw(tags.get(tag_key))
            if capacity is not None:
                properties["power_mw"] = capacity
                break
        for source_key, target_key in (
            ("status", "status"),
            ("plant:type", "type_inst"),
            ("start_date", "year"),
        ):
            if tags.get(source_key) is not None:
                properties[target_key] = tags[source_key]
        turbine_count = as_count(tags.get("turbines"))
        if turbine_count is not None:
            properties["n_turbines"] = turbine_count

        geometry = source_feature.get("geometry")
        geometry_type = geometry.get("type") if isinstance(geometry, dict) else None
        is_area_geometry = (
            geometry_type in {"Polygon", "MultiPolygon"}
            or (source_properties.get("osm_type") == "relation" and tags.get("type") == "multipolygon")
        )
        has_windfarm_evidence = (
            tags.get("industrial") == "windfarm"
            or tags.get("seamark:landmark:production_area") == "wind_farm"
            or (tags.get("plant:source") == "wind" and tags.get("plant:type") == "offshore")
        )
        is_windfarm_area = is_area_geometry and has_windfarm_evidence
        if is_windfarm_area:
            properties["category_of_offshore_production_area"] = 1
            properties["iho_feature_role"] = (
                "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#OffshoreProductionArea"
            )
        elif (
            source_properties.get("osm_type") == "node"
            and geometry_type == "Point"
            and tags.get("generator:method") == "wind_turbine"
        ):
            properties["iho_feature_role"] = (
                "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
            )

        feature["properties"] = properties
        features.append(feature)
    result["features"] = features
    return result


# The bblocks Python transform runner provides input_data and reads output_data.
if "input_data" in globals():
    output_data = json.dumps(transform(json.loads(input_data)), ensure_ascii=False, indent=2) + "\n"
