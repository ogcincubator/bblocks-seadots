# Context validation report — `area-of-interest`

Date: 2026-05-19 · `context.jsonld` covers every property used in `schema.yaml` and `examples/utsira_surroundings_aoi.json`.

## Resolved to authoritative vocabularies

| Term | Resolved to |
|---|---|
| `title`, `name`, `description`, `created`, `updated`, `language`, `license`, `format` | DC Terms |
| `keywords`, `themes`, `formats`, `source`, `url` | DCAT |
| `concepts`, `scheme`, `label`, `vocabularyTerm` | SKOS |
| `provenance` | PROV-O |
| `verifiedOn` | DC Terms `date` |
| `primarySource` | DC Terms `source` |
| `bbox` | GeoJSON vocab |
| `note` | SKOS `note` |

## Missing authoritative URIs (local `seadots:` namespace)

| Term | Status | Action |
|---|---|---|
| `areaOfInterest` | local-permanent | Container term; no external candidate |
| `role` | needs-vocabulary | DCAT-Prov `Role`, PROV `Role` — evaluate |
| `centroid` | needs-vocabulary | No standard; possible GeoSPARQL term |
| `area_km2` | needs-vocabulary | QUDT `QuantityKind:Area` + km² unit URI; mint specialised term |
| `crs` | needs-vocabulary | OGC CRS register URI (`http://www.opengis.net/def/crs/EPSG/0/4326`) instead of `EPSG:4326` string |
| `provenanceValues` (`values` enum) | local-permanent | Shared with all per-input bblocks; candidate for a seadots-provenance bblock |
| `retrievalApiCall` | needs-discussion | Composition of `prov:hadActivity` + `dcat:accessURL`; no single term |
| `nearestAuthoritativeSource` | local-permanent | Novel pattern documented in this bblock family |
