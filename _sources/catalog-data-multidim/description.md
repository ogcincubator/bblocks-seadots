# SeaDOTs Catalog Data Multidimensional

OGC API Records profile for catalog records that describe multidimensional gridded or array-oriented data products such as NetCDF, Zarr, or CF-convention datasets.

The profile composes `ogc.hosted.seadots.catalog-data` for shared catalog data semantics and the imported `ogc.hosted.iliad.api.features.stac_multidim_data` building block for multidimensional metadata. It intentionally avoids copying inherited properties, schemas, or JSON-LD context. Local schema constraints only require a profile link that advertises the imported multidimensional data profile.

## Composition

| Concern | Source |
| --- | --- |
| Shared STAC/CF/provenance data record | `bblocks://ogc.hosted.seadots.catalog-data` |
| Multidimensional STAC/DCAT record structure | `bblocks://ogc.hosted.iliad.api.features.stac_multidim_data` |
| SeaDOTs profile advertisement | Local `schema.yaml` profile-link constraint |
| JSON-LD terms | Imported catalog-data and ILIAD multidimensional contexts |

## Usage Notes

Use this block when a SeaDOTs catalog record points to a multidimensional data asset rather than a scalar observation, workflow, or execution record. The actual multidimensional metadata terms remain governed by the imported ILIAD profile so that this block stays a thin OGC Record profile.

## Generator

The `scripts/build_catalog_data_multidim_record.py` helper generates a STAC/OGC Record from a NetCDF file header without loading data arrays. It prefers Python metadata backends (`netCDF4`, `h5netcdf`) when installed, then falls back to CLI metadata inspection (`h5dump`, `ncdump -h`) with a timeout.

Example:

```bash
python3 _sources/catalog-data-multidim/scripts/build_catalog_data_multidim_record.py \
  --href https://example.org/data/example.nc \
  --license https://spdx.org/licenses/CC-BY-4.0.html \
  -o /tmp/catalog-data-multidim-record.json \
  /path/to/example.nc
```
