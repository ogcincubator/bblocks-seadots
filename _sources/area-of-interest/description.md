# Marine Area of Interest

OGC API Records / OGC Feature profile for a polygon delimiting a marine area of interest.

The geometry is carried by the top-level `geometry` field (GeoJSON Polygon). The `data` block carries derived scalars (bbox, centroid, area_km2, CRS) so a consumer can read the AOI without re-parsing the geometry. Mandatory `data.provenance` documents whether the polygon was retrieved from an authoritative source or hand-drawn / illustrative.

## Dependency

Inherits the OIM feature shape from `ogc.hosted.iliad.api.features.oim`.

## Vocabulary

- `bbox`, `centroid`, `area_km2` carried as local terms (`seadots:` namespace) — see `validation-report.md` for terms still pending authoritative vocabulary URIs.
- `crs` is a string identifier (e.g. `EPSG:4326`); a future revision MAY upgrade to an OGC CRS register URI.
