# Harvest time series scenario Scen M3 — source GeoJSON

This source-side block is intentionally lossless for the supplied GeoJSON. It contains
19,920 Point features: 83 repeated feature identifiers over 240 source timestamps.

## Source-property coverage gaps

| name | reason it cannot be fully mapped | recommended fallback |
|---|---|---|
| `bwmus` | The file contains no variable definition, unit, vocabulary URI, owner, or model documentation. | Obtain the scenario model documentation and map to a NERC/CF term where applicable. |
| `time` | The source string has no timezone or calendar declaration. | Confirm timezone and calendar; then serialise as ISO 8601 date-time with offset. |

## Provenance

The attached filename and SHA-256 checksum are: `harvest_timeseries_scenario_Scen_M3[539974].geojson`,
`be2abe4e83f239888eb9540d7aa1b9bf5c85516546ffec18067147a3f454a554`.
No API endpoint, landing page, licence, or owner metadata accompanied the attachment.
