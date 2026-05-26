# Context validation report — `area-of-interest`

The block is intentionally minimal: a GeoJSON `Feature` with a polygon
`geometry` and `properties.title` / `properties.description`.

## Mapped terms

| Term | Mapping |
|---|---|
| `id` | `@id` |
| `type` | `@type` |
| `geometry` | GeoJSON vocabulary |
| `coordinates` | GeoJSON vocabulary, list container |
| `Feature` | GeoJSON vocabulary |
| `Polygon` | GeoJSON vocabulary |
| `properties` | GeoJSON vocabulary |
| `title` | `dcterms:title` |
| `description` | `dcterms:description` |
| `links`, `href`, `rel` | IANA / GeoJSON link terms |

No derived AOI fields are expected. `bbox`, `centroid`, `area_km2`, `crs`, and
provenance were removed to avoid duplicating information already available from
the geometry or better handled in a separate metadata record.
