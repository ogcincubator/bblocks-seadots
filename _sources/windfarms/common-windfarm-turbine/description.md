# Wind turbine

A single wind turbine, represented as a GeoJSON Feature with Point geometry. A set of turbines is a FeatureCollection of such features. The schema accepts either.

## Properties

| Property | Type | Meaning | OSM source tag |
|---|---|---|---|
| `ref` | string | Turbine label within its wind farm | `ref` |
| `windfarm_name` | string | Name of the wind farm | `name` of the `site` relation containing the turbine |
| `windfarm` | URI | Identifier of the wind farm | URL of that relation |
| `manufacturer` | string | Turbine manufacturer | `manufacturer` |
| `model` | string | Model designation | `model` |
| `rated_power_mw` | number (MW) | Rated output of the turbine | `generator:output:electricity` |
| `hub_height_m` | number (m) | Hub height | `height:hub` |
| `rotor_diameter_m` | number (m) | Rotor diameter | `rotor:diameter` |
| `rotor_axis` | `horizontal_axis` \| `vertical_axis` | Rotor axis orientation | `generator:type` |
| `offshore` | boolean | Stands offshore | `offshore` |
| `operator` | array of strings | Operating organisations | `operator`, split on `;` |
| `status` | INSPIRE ConditionOfFacilityValue code | Condition of the turbine | `status` |
| `last_updated` | date-time | Last edit of the source record | element `timestamp` |
| `commissioning_year` | integer (optional) | Year the turbine was commissioned | not tagged in the OSM snapshot; e.g. NVE turbine details |

All properties are optional and nullable, and additional properties are allowed. The example converter writes every property listed here, with `null` when the source does not state it or states it in a form that cannot be read unambiguously. The converter never fills in a default. For example, `offshore` is not set to `true` just because the turbine is at sea, and `status` is not set to `functional` when the tag is absent. Units are fixed by the property name, so `"15 MW"` becomes `15` and `"141"` (OSM's default unit is metres) becomes `141`. `generator:method=wind_turbine` and `generator:source=wind` are the selection criteria, so they are not repeated as properties.

The feature `id` is the URL of the source element, e.g. `https://www.openstreetmap.org/node/14185128565`.

## Semantics

`context.jsonld` maps `properties` with `@nest`, so the turbine attributes attach directly to the feature resource rather than to an intermediate node. Terms come from the shared windfarm ontology (`owf:`, [common-windfarm-ontology](../common-windfarm-ontology/)), which defines `owf:WindTurbine`, aligned by `rdfs:seeAlso` to the [IHO S-100 wind turbine](https://registry.iho.int/fdd/view5.do?idx=341&type=5&valueType=0) definition. It also defines the turbine properties, with QUDT units where they apply, and the rotor-axis concepts. `model` maps to `owf:modelName` (aligned with `skos:closeMatch` to `schema:model`), `last_updated` to `dcterms:modified`, and `status` to [INSPIRE ConditionOfFacilityValue](http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue) concepts.

## Examples

The examples are converted from the [windfarm-openstreetmap](../windfarm-openstreetmap/) source snapshot of 2026-10-27, which contains 283 turbine nodes in four wind farms. Known source quirks visible in the output:

- 100 turbines (MFW Bałtyk II and III) are tagged `generator:type=offshore`, which is not a rotor-axis value, so their `rotor_axis` is `null`. They also lack `generator:output:electricity`, so `rated_power_mw` is `null` even though the model name (SG 14-236 DD) implies 14 MW.
- `status` is tagged only on those 100 turbines (`construction` → `underConstruction`). The other turbines have no status tag, so their `status` is `null`.

OSM data is licensed under the [Open Database License 1.0](https://opendatacommons.org/licenses/odbl/1-0/); keep the attribution "© OpenStreetMap contributors" when redistributing.
