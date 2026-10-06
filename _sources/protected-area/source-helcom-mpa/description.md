# HELCOM MPA source profile with EMODnet transform

**Sources.** The Seadots pygeoapi instance serves two HELCOM ArcGIS layers unchanged:

| Collection | HELCOM MADS layer | Granularity | Codes |
|---|---|---|---|
| `helcom-live-mpas` | 54 *HELCOM MPAs* | one row per MPA | `MPA_ID`, the HELCOM MPA database id |
| `helcom-live-mpa-network-2026` | 190 *Baltic Sea MPA network 2026* | one row per polygon (3,537 rows on 30 Sep 2026) | `Code`, which mixes four schemes |

**Target:** `emodnet-protected-area.rsc-mpa` with `rsc = HELCOM`, the same shape as
EMODnet's `marineprotectedareas`.

## Field mapping (layer 54)

| EMODnet | Source | Rule |
|---|---|---|
| `rsc` | — | constant `HELCOM` |
| `code` | `MPA_ID` | integer |
| `name` | `Name` | copy |
| `country` | `Country` | copy (English names match EMODnet) |
| `status` | `MPA_status` | copy (same three values) |
| `status_yr` | `Year_est` | copy (`Date_est` is dropped; EMODnet keeps only the year) |
| `link` | `Site_link` | copy |
| `shape_leng`, `shape_area` | geometry | planar on CRS84 |
| `orig_name`, `designatio`, `iucn_cat`, `*_area`, `mang_auth` | — | `null`, as in EMODnet's HELCOM rows |

Layer 54 maps losslessly. On the example data, both sites equal the EMODnet records on
every attribute except the geometry-derived ones.

## Layer 190: classify, join, dissolve, route

EMODnet has not published the 2026 network, and its `code` is `xsd:long`. Layer 190 therefore
needs three extra steps before any row can enter the profile:

1. **Classify `Code`** by pattern:
   - `^\d{1,5}$` is a HELCOM MPA id, and the row enters this profile.
   - `^\d{6,10}$` is an EEA/WDPA site id. The row is routed to `emodnet:nationallydesignatedareas`
     (`natdaid`). Example: Fehmarnbelt `555638668` → EMODnet `DE02AWZ_4`.
   - `^[A-Z]{2}[A-Z0-9]{7}$` is a Natura 2000 code. The row is routed to `emodnet:natura2000areas`
     (`sitecode`). Example: Kuršių marios `LTSIU0012`.
   - Any other code is national and is reported as unresolved.

   Routed rows are **not duplicated** into the RSC view. The report carries the
   EMODnet key they resolve to, so the API can link to them instead.
2. **Join layer 54** on the HELCOM id to obtain `MPA_status`, `Year_est` and `Site_link`. Layer 190
   has no status field. An id with no layer-54 match (a newly added MPA) has no status, so it is
   reported and not published until HELCOM publishes it in the MPA database.
3. **Dissolve** rows that share an id into one MultiPolygon. The transform concatenates the parts
   and does not union them. This is correct for the disjoint parts in layer 190. If parts overlap,
   union them first (e.g. `ST_Union` in the GeoPackage), or `shape_area` counts the overlap twice.

The 2026 `Type` / `TypeSpecification` labels (e.g. *Kansallispuisto*, *Natur- og vildtreservater*)
have no field in the EMODnet RSC schema. They survive only on the source collection. Mapping them
to EEA designation types would be a separate crosswalk per country, similar to the Norwegian
`verneform` crosswalk.
