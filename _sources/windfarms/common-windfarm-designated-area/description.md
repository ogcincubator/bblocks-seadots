# Windfarm designated area

A wind farm as a designated area or project, as a GeoJSON Feature or a FeatureCollection of such features. Individual devices are out of scope; the turbines are modelled in [common-windfarm-turbine](../common-windfarm-turbine/) and link back to their wind farm. The only device-level value kept here is the count `n_turbines`.

The property set extends the EMODnet Human Activities windfarm attributes with the windpark parameters found in the other sources in this register:

| Group | Properties | Sources |
|---|---|---|
| EMODnet core | `name`, `country`, `n_turbines`, `power_mw`, `status`, `type_inst`, `year`, `updateyear`, `dist_coast`, `area_sqkm`, `notes` | EMODnet, OSM, NVE, PL |
| Status and time | `status_detail`, `status_as_of`, `year_semantics`, `year_is_assumed`, `operational_date`, `offshore` | OSM, NVE, PL |
| Organisations | `operator` (array), `owner`, `developer` | OSM, NVE, PL |
| Licensing and administration | `licence_status`, `licensing_case`, `admin_units`, `electricity_price_area`, `mean_annual_production_gwh` | NVE |
| Provenance | `source_type` (`osm` \| `emodnet` \| `national`), `source_dataset`, `source_reference`, `source_record_id`, `source_snapshot_date`, `last_updated` | all |
| Location provenance | `location_status`, `location_method`, `location_reference`, `same_as` | all |

`status` uses the EMODnet vocabulary (`Planned`, `Approved`, `Construction`, `Production`, `Dismantled`), and the source wording is kept in `status_detail`. `licence_status` is the licensing authority's wording and is kept separate from the operational status. Geometry is a Polygon or MultiPolygon for a designated area, a Point when the source only publishes a location (EMODnet), or `null` when no geometry is available. In the `null` case `location_status` is `unmatched` and `location_method` says why.

Every feature is one source record. Records of the same wind farm from different sources are not merged. Instead they are linked with `same_as`, so conflicting values stay visible. For example, OSM tags Baltic Power as an operating plant (`power=plant`), while EMODnet reports it as under construction with 1,140 MW against OSM's 1,200 MW.

Not carried over from the source blocks:
- `nve_turbine_details`, which is device-level and belongs in the turbine block;
- `shape_leng` and `shape_area`, which are GIS artefacts of the EMODnet service;
- the record-matching scores from the Polish block (`MatchCandidate`). The block-specific `location_emodnet_ids` becomes the general `same_as`.

## Example

The example FeatureCollection has 12 records:

- **OpenStreetMap** (2026-10-27 snapshot, [windfarm-openstreetmap](../windfarm-openstreetmap/)): Baltic Power, Baltica 2, Baltica 3, MFW Bałtyk II and MFW Bałtyk III. For each, the plant relation and its area ways are merged into one feature, with the primary element's tags winning. Geometry is the outer way, and `area_sqkm` is computed geodesically on WGS 84. Each area way was checked to contain all of its relation's turbines. No OSM area contains the Bałtyk III turbines, so that feature has `null` geometry. `n_turbines` comes from the `turbines` tag when present, otherwise from the count of `generator` members in the relation. OSM does not state the country, so `country` is null.
- **EMODnet** (WFS `emodnet:windfarms`, retrieved 2026-11-04): the five records for the same farms, matched by name.
- **NVE**: the Smøla onshore record from [emodnet-compliant-windfarm-no](../emodnet-compliant-windfarm-no/).
- **Polish national pipeline**: the illustrative record from [emodnet-compliant-windfarm-pl](../emodnet-compliant-windfarm-pl/).

## Semantics

`context.jsonld` maps `properties` with `@nest`, so the attributes attach directly to the feature. Terms come from the shared windfarm ontology ([common-windfarm-ontology](../common-windfarm-ontology/), `owf:`). Its `owf:WindfarmArea` class refers to the IHO S-100 windfarm definition. Properties that also exist in the Norwegian and Polish blocks are declared `owl:equivalentProperty` to those terms. `country` and `status` values resolve to the EMODnet concepts in that ontology, which link to the EU country authority table and INSPIRE ConditionOfFacilityValue. `same_as` maps to `schema:sameAs`.

OSM-derived records are © OpenStreetMap contributors under the [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/).
