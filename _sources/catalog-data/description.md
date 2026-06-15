# SeaDOTs Catalog Data

Generic Records/DCAT and STAC Item profile for SeaDOTs catalog records that describe data artefacts. It composes the EarthCODE common GeoDCAT/STAC profile, the STAC CF extension, and the STAC Item provenance profile, then adds only SeaDOTs terms that are shared by data records regardless of workflow role or data type.

This block is the shared base for catalog input records, catalog output records, and data-type-specific records such as multidimensional data. Input/output status is represented by `properties.role` (`input` or `output`) and provenance links such as `derived_from` or `via`, not by separate building blocks.

`ogc.osc.geodcat-stac-earthcode.products` was considered as a single import, but it constrains `type` to `Collection`. SeaDOTs catalog input and output records are STAC Items (`type: Feature`), so this block imports `ogc.osc.geodcat-stac-earthcode.common` instead and adds the Item/CF/provenance contracts explicitly.

## Composition

| Concern | Source |
| --- | --- |
| Records/DCAT and GeoDCAT-STAC common profile | `bblocks://ogc.osc.geodcat-stac-earthcode.common` |
| STAC Item plus PROV-O provenance | `bblocks://ogc.contrib.stac.item-prov` |
| CF metadata extension | `bblocks://ogc.contrib.stac.extensions.cf` |
| SeaDOTs shared data-record terms | Local `schema.yaml` |

## Roles

| Role | Meaning |
| --- | --- |
| `data` | Generic data artefact without a workflow-specific role. |
| `input` | Data artefact consumed by an execution or workflow. |
| `output` | Data artefact produced by an execution or workflow. |
