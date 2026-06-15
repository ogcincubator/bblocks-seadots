# SeaDOTs Catalog Data Tabular

OGC API Records profile for catalog records that describe tabular data products such as CSV, TSV, Parquet, GeoParquet, or spatial attribute tables.

The profile composes `ogc.hosted.seadots.catalog-data` for shared Records/DCAT/STAC/CF/PROV-O catalog semantics, then adds locally only the tabular structural metadata terms drawn from the STAC `table` extension (https://github.com/stac-extensions/table) and GeoParquet column metadata conventions (https://geoparquet.org/). It intentionally avoids copying inherited properties, schemas, or JSON-LD context. The local schema constraint requires a profile link that advertises this building block's own identifier.

There is no imported ILIAD tabular block to depend on: the ILIAD `geoparquet` folder contains only a GeoParquet column-metadata sample with no `bblock.json` or schema. Therefore, unlike `catalog-data-multidim`, this profile defines the structural column descriptor terms locally and lists no ILIAD dependency.

## Composition

| Concern | Source |
| --- | --- |
| Shared STAC/CF/provenance data record | `bblocks://ogc.hosted.seadots.catalog-data` |
| Tabular column descriptor structure | Local `schema.yaml` — STAC `table` extension terms |
| GeoParquet primary geometry column | Local `schema.yaml` — `table:primary_geometry` |
| Profile advertisement | Local `schema.yaml` profile-link constraint |
| JSON-LD terms | Inherited `catalog-data/context.jsonld` + local `table:` prefix terms |

## Added Properties

All tabular-specific properties live under `properties` of the OGC API Record Feature:

| Property | Type | Description |
| --- | --- | --- |
| `table:columns` | array of column objects | Ordered column list. Each column has `name` (required), `description`, `type`, and `unit` (CF/UDUNITS string). |
| `table:primary_geometry` | string | Name of the primary geometry column (GeoParquet). |
| `table:row_count` | integer | Total number of data rows in the asset. |

The `table:` prefix is mapped to `https://stac-extensions.github.io/table/v1.2.0/schema.json#` in the JSON-LD context. Unit strings follow CF/UDUNITS conventions and are mapped to `qudt:unit`.

## Source-property Coverage Gaps

No upstream tabular bblock schema exists for the ILIAD ecosystem; the GeoParquet encoding details (e.g. `encoding`, `geometry_types`, `crs` per-column keys from the GeoParquet metadata format) are not yet covered by this profile. Consumers who need per-column GeoParquet encoding metadata should extend this block or declare those terms in `additionalProperties`.

## Usage Notes

Use this block when a SeaDOTs catalog record points to a tabular data asset — CSV, TSV, Parquet, GeoParquet, or a spatial attribute table. Supply `table:columns` to document column names, types, and units so downstream consumers can interpret the file without opening it.

For multidimensional gridded or array-oriented assets (NetCDF, Zarr), use `ogc.hosted.seadots.catalog-data-multidim` instead.
