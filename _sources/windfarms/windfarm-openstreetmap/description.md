# OpenStreetMap offshore wind source data

This block describes the unconverted JSON response of the OpenStreetMap API 0.6 map endpoint (`/api/0.6/map.json?bbox=…`) for the Polish Baltic offshore wind extent, retrieved on 2026-10-27. It is a source-data profile: it records the response exactly as the API returns it and does not filter, convert, or reinterpret any element.

## Structure

The response carries API metadata and a flat list of OSM elements:

- `version`, `generator`, `copyright`, `attribution`, `license` — API version, producing server software, and the copyright statement, attribution URL, and licence URL supplied by OSM.
- `bounds` — the requested bounding box (`minlat`, `minlon`, `maxlat`, `maxlon`) in WGS 84 decimal degrees.
- `elements` — nodes, ways, and relations in source order. Each element has `type`, `id`, `timestamp`, `version`, `changeset`, `user`, and `uid`, and optionally `tags`:
  - **nodes** carry `lat` and `lon`;
  - **ways** carry `nodes`, an ordered list of node identifiers (a closed way repeats its first node last);
  - **relations** carry `members`, an ordered list of `{type, ref, role}` references (the role may be empty).

Element identifiers are numeric and unique only within their element type, so a node and a way may share the same `id`. Geometry is implicit: ways and relations have no coordinates of their own, only references that resolve through the nodes in the same response. Tags are kept as an open key–value dictionary of uninterpreted source strings. In the JSON-LD context, each tag key maps to `https://www.openstreetmap.org/wiki/Key:<key>`, following the [osm2rdf](https://github.com/ad-freiburg/osm2rdf) convention. For example, `plant:source` becomes `osmkey:plant:source`. Keys without a colon resolve through `@vocab`. Keys with a colon resolve through a prefix term for their first segment (`plant`, `seamark`, `name`, …), as JSON-LD 1.1 requires. Where that segment is also a bare key (`name`, `source`, `note`, …), the bare key expands to the prefix IRI with a trailing colon (`osmkey:name:`). The ontology declares those IRIs equivalent to the plain key IRIs. A tag key with a colon whose first segment has no prefix term in the context is read as an absolute IRI, so add that segment to the context when a new snapshot introduces one.

## Example snapshot

The request extent is `16.74361,54.953732,17.78045,55.13824`. The response contains 1,530 elements: 1,499 nodes, 17 ways, and 14 relations, with 413 distinct tag keys. Most nodes are untagged way vertices. Tagged features include 283 `power=generator` nodes (turbines), substations, submarine cables, and wind farm areas (`industrial=windfarm`, `power=plant`). The bounding box also returns features that are unrelated to wind energy, such as administrative boundaries, wrecks, and reefs. Element edit timestamps range from 2012-04-04 to 2026-10-18.

The snapshot reflects the OSM database at retrieval time. It is not a stable or authoritative national inventory. Any harmonisation, such as building GeoJSON geometries or selecting wind-farm features, belongs in a separate downstream transformation that keeps this raw response alongside its output. See the [OSM element model](https://wiki.openstreetmap.org/wiki/Elements) and the [OSM API map call](https://wiki.openstreetmap.org/wiki/API_v0.6#Retrieving_map_data_by_bounding_box:_GET_/api/0.6/map).

## IHO semantics

IHO S-100 Data Dictionary item 42 is “Category of Offshore Production Area”, defined as the classification of an area at sea within which production facilities exist. Its listed value “Wind Farm” applies to wind-farm area features when source tags explicitly identify that category. The transform in the companion harmonised block asserts this IHO value only when the OSM tags identify a wind farm (`industrial=windfarm` or `seamark:landmark:production_area=wind_farm`). It does not assign the area category to individual turbine nodes or to ambiguous features. The IHO attribute is documented at the [IHO Geospatial Information Registry](https://registry.iho.int/fdd/view3.do?idx=42&type=3).

## Licence

OSM data is licensed under the [Open Database License 1.0](https://opendatacommons.org/licenses/odbl/1-0/). Keep the attribution "© OpenStreetMap contributors" ([copyright](https://www.openstreetmap.org/copyright)) when redistributing the example.
