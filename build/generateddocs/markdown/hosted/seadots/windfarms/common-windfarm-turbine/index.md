
# Wind turbine (Schema)

`ogc.hosted.seadots.windfarms.common-windfarm-turbine` *v0.2*

GeoJSON representation of a single wind turbine (Feature with Point geometry) or a FeatureCollection of turbines, with harmonised properties: manufacturer, model, rated power, hub height, rotor diameter, rotor axis, operator, condition, and the wind farm it belongs to.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### Single wind turbine
Turbine 76 of the Baltic Power offshore wind farm (Vestas V236-15.0 MW), converted from [OSM node 14185128565](https://www.openstreetmap.org/node/14185128565). © [OpenStreetMap contributors](https://www.openstreetmap.org/copyright), [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/).

#### json
```json
{
  "type": "Feature",
  "id": "https://www.openstreetmap.org/node/14185128565",
  "geometry": {
    "type": "Point",
    "coordinates": [
      17.653582,
      55.006667
    ]
  },
  "properties": {
    "ref": "76",
    "windfarm_name": "Baltic Power",
    "windfarm": "https://www.openstreetmap.org/relation/21402440",
    "manufacturer": "Vestas",
    "model": "V236-15.0 MW",
    "rated_power_mw": 15.0,
    "hub_height_m": 141.0,
    "rotor_diameter_m": 236.0,
    "rotor_axis": "horizontal_axis",
    "offshore": true,
    "operator": null,
    "status": null,
    "last_updated": "2026-09-16T14:23:07Z",
    "commissioning_year": 2051
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/common-windfarm-turbine/context.jsonld",
  "type": "Feature",
  "id": "https://www.openstreetmap.org/node/14185128565",
  "geometry": {
    "type": "Point",
    "coordinates": [
      17.653582,
      55.006667
    ]
  },
  "properties": {
    "ref": "76",
    "windfarm_name": "Baltic Power",
    "windfarm": "https://www.openstreetmap.org/relation/21402440",
    "manufacturer": "Vestas",
    "model": "V236-15.0 MW",
    "rated_power_mw": 15.0,
    "hub_height_m": 141.0,
    "rotor_diameter_m": 236.0,
    "rotor_axis": "horizontal_axis",
    "offshore": true,
    "operator": null,
    "status": null,
    "last_updated": "2026-09-16T14:23:07Z",
    "commissioning_year": 2051
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix owf: <https://w3id.org/ogc/hosted/seadots/windfarm#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://www.openstreetmap.org/node/14185128565> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.765358e+01 5.500667e+01 ) ] ;
    owf:commissioningYear "2051"^^xsd:gYear ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "76" ;
    owf:windfarmName "Baltic Power" .


```


### Polish Baltic offshore wind turbines
FeatureCollection of all 283 wind turbines in the 2026-10-27 OpenStreetMap snapshot of the Polish Baltic offshore wind extent (Baltic Power, Baltica 2, MFW Bałtyk II and III), converted from the [windfarm-openstreetmap](../windfarm-openstreetmap/) source example. © [OpenStreetMap contributors](https://www.openstreetmap.org/copyright), [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/).

#### json
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128565",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.653582,
          55.006667
        ]
      },
      "properties": {
        "ref": "76",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128566",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.63486,
          55.020635
        ]
      },
      "properties": {
        "ref": "75",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128567",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.661072,
          55.080457
        ]
      },
      "properties": {
        "ref": "74",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128568",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.64328,
          55.060358
        ]
      },
      "properties": {
        "ref": "73",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128569",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.64,
          55.049375
        ]
      },
      "properties": {
        "ref": "72",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128570",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.66812,
          55.10027
        ]
      },
      "properties": {
        "ref": "71",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128571",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.610119,
          55.043869
        ]
      },
      "properties": {
        "ref": "70",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128572",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.683461,
          55.066143
        ]
      },
      "properties": {
        "ref": "69",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128573",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.747624,
          55.099235
        ]
      },
      "properties": {
        "ref": "68",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128574",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.654354,
          55.071385
        ]
      },
      "properties": {
        "ref": "67",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128575",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.640016,
          55.039663
        ]
      },
      "properties": {
        "ref": "66",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128576",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.635311,
          55.029823
        ]
      },
      "properties": {
        "ref": "65",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128577",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.628869,
          55.00997
        ]
      },
      "properties": {
        "ref": "64",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128578",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.626832,
          55.000814
        ]
      },
      "properties": {
        "ref": "63",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128579",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.589261,
          54.993376
        ]
      },
      "properties": {
        "ref": "62",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128580",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.716839,
          55.090599
        ]
      },
      "properties": {
        "ref": "61",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128581",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.663009,
          55.091074
        ]
      },
      "properties": {
        "ref": "60",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128582",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.67817,
          55.109397
        ]
      },
      "properties": {
        "ref": "59",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128583",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.672281,
          55.0146
        ]
      },
      "properties": {
        "ref": "58",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128584",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.672183,
          55.023284
        ]
      },
      "properties": {
        "ref": "57",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128585",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.675452,
          55.031888
        ]
      },
      "properties": {
        "ref": "56",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128586",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.675065,
          55.040864
        ]
      },
      "properties": {
        "ref": "55",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128587",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.673089,
          55.049809
        ]
      },
      "properties": {
        "ref": "54",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128588",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.668436,
          55.058796
        ]
      },
      "properties": {
        "ref": "53",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128589",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.685713,
          55.076469
        ]
      },
      "properties": {
        "ref": "52",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128590",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.689498,
          55.087969
        ]
      },
      "properties": {
        "ref": "51",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128591",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.694919,
          55.098781
        ]
      },
      "properties": {
        "ref": "50",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128592",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.701642,
          55.10965
        ]
      },
      "properties": {
        "ref": "49",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128593",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.594355,
          55.003223
        ]
      },
      "properties": {
        "ref": "48",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128594",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.602226,
          55.014896
        ]
      },
      "properties": {
        "ref": "47",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128595",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.604322,
          55.024106
        ]
      },
      "properties": {
        "ref": "46",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128596",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.606384,
          55.034685
        ]
      },
      "properties": {
        "ref": "45",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128597",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.616112,
          55.052976
        ]
      },
      "properties": {
        "ref": "44",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128598",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.61844,
          55.063799
        ]
      },
      "properties": {
        "ref": "43",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128599",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.624618,
          55.074478
        ]
      },
      "properties": {
        "ref": "42",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128600",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.632259,
          55.083729
        ]
      },
      "properties": {
        "ref": "41",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129401",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.636667,
          55.092805
        ]
      },
      "properties": {
        "ref": "40",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129402",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.638176,
          55.102896
        ]
      },
      "properties": {
        "ref": "39",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129403",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.654604,
          55.109176
        ]
      },
      "properties": {
        "ref": "38",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129404",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.722445,
          55.10092
        ]
      },
      "properties": {
        "ref": "37",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129405",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.724589,
          55.109811
        ]
      },
      "properties": {
        "ref": "36",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129406",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.747051,
          55.108198
        ]
      },
      "properties": {
        "ref": "35",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129407",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.743457,
          55.090149
        ]
      },
      "properties": {
        "ref": "34",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129408",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.769843,
          55.108576
        ]
      },
      "properties": {
        "ref": "33",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129409",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.771604,
          55.098788
        ]
      },
      "properties": {
        "ref": "32",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129410",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.76571,
          55.088551
        ]
      },
      "properties": {
        "ref": "31",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129411",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708551,
          55.080982
        ]
      },
      "properties": {
        "ref": "30",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129412",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708551,
          55.071803
        ]
      },
      "properties": {
        "ref": "29",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129413",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.70855,
          55.06282
        ]
      },
      "properties": {
        "ref": "28",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129414",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708564,
          55.053803
        ]
      },
      "properties": {
        "ref": "27",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129415",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.70858,
          55.044819
        ]
      },
      "properties": {
        "ref": "26",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129416",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708615,
          55.035834
        ]
      },
      "properties": {
        "ref": "25",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129417",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708638,
          55.023444
        ]
      },
      "properties": {
        "ref": "24",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129418",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708593,
          55.014232
        ]
      },
      "properties": {
        "ref": "23",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129419",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708956,
          55.005267
        ]
      },
      "properties": {
        "ref": "22",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129420",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.688873,
          55.008866
        ]
      },
      "properties": {
        "ref": "21",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129421",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.673768,
          55.001274
        ]
      },
      "properties": {
        "ref": "20",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129422",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.650697,
          54.995819
        ]
      },
      "properties": {
        "ref": "19",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129423",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.628481,
          54.991824
        ]
      },
      "properties": {
        "ref": "18",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129424",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.607432,
          54.987943
        ]
      },
      "properties": {
        "ref": "17",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129425",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.58752,
          54.982886
        ]
      },
      "properties": {
        "ref": "16",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129426",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.621821,
          55.108774
        ]
      },
      "properties": {
        "ref": "15",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129427",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.616341,
          55.099549
        ]
      },
      "properties": {
        "ref": "14",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129428",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.612253,
          55.088796
        ]
      },
      "properties": {
        "ref": "13",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129429",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.603759,
          55.079589
        ]
      },
      "properties": {
        "ref": "12",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129430",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.595467,
          55.070586
        ]
      },
      "properties": {
        "ref": "11",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129431",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.587049,
          55.061441
        ]
      },
      "properties": {
        "ref": "10",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129432",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.583794,
          55.05254
        ]
      },
      "properties": {
        "ref": "9",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129433",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.581526,
          55.043584
        ]
      },
      "properties": {
        "ref": "8",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129434",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.579247,
          55.034576
        ]
      },
      "properties": {
        "ref": "7",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129435",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.576959,
          55.025528
        ]
      },
      "properties": {
        "ref": "6",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129436",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.57467,
          55.016476
        ]
      },
      "properties": {
        "ref": "5",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129437",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.572366,
          55.007357
        ]
      },
      "properties": {
        "ref": "4",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129438",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.570083,
          54.998319
        ]
      },
      "properties": {
        "ref": "3",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129439",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.567802,
          54.989286
        ]
      },
      "properties": {
        "ref": "2",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129440",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.565519,
          54.980271
        ]
      },
      "properties": {
        "ref": "1",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537540",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.270053,
          54.998782
        ]
      },
      "properties": {
        "ref": "BK3 M04",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537541",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.275409,
          55.010672
        ]
      },
      "properties": {
        "ref": "BK3 M03",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537542",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.281049,
          55.022455
        ]
      },
      "properties": {
        "ref": "BK3 M02",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537543",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.283813,
          54.983888
        ]
      },
      "properties": {
        "ref": "BK3 L05",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537544",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.289463,
          54.99559
        ]
      },
      "properties": {
        "ref": "BK3 L04",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537545",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.29541,
          55.007347
        ]
      },
      "properties": {
        "ref": "BK3 L03",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537546",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.30046,
          55.019018
        ]
      },
      "properties": {
        "ref": "BK3 L02",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537547",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.306081,
          55.030645
        ]
      },
      "properties": {
        "ref": "BK3 L01",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537548",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.292501,
          54.957068
        ]
      },
      "properties": {
        "ref": "BK3 K07",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537549",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.298174,
          54.968722
        ]
      },
      "properties": {
        "ref": "BK3 K06",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537550",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.303485,
          54.980528
        ]
      },
      "properties": {
        "ref": "BK3 K05",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537551",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.308958,
          54.992256
        ]
      },
      "properties": {
        "ref": "BK3 K04",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537552",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.314493,
          55.003671
        ]
      },
      "properties": {
        "ref": "BK3 K03",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537553",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.319906,
          55.015593
        ]
      },
      "properties": {
        "ref": "BK3 K02",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537554",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.325594,
          55.027275
        ]
      },
      "properties": {
        "ref": "BK3 K01",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537555",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.311847,
          54.953732
        ]
      },
      "properties": {
        "ref": "BK3 J07",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537556",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.31743,
          54.965356
        ]
      },
      "properties": {
        "ref": "BK3 J06",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537557",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.322872,
          54.977064
        ]
      },
      "properties": {
        "ref": "BK3 J05",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537558",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.328485,
          54.988852
        ]
      },
      "properties": {
        "ref": "BK3 J04",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537559",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.333772,
          55.000446
        ]
      },
      "properties": {
        "ref": "BK3 J03",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537560",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.339309,
          55.012201
        ]
      },
      "properties": {
        "ref": "BK3 J02",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537561",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.344812,
          55.023919
        ]
      },
      "properties": {
        "ref": "BK3 J01",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537562",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.336774,
          54.962085
        ]
      },
      "properties": {
        "ref": "BK3 H06",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537563",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.342261,
          54.973665
        ]
      },
      "properties": {
        "ref": "BK3 H05",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537564",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.347981,
          54.985377
        ]
      },
      "properties": {
        "ref": "BK3 H04",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537565",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.364254,
          55.020548
        ]
      },
      "properties": {
        "ref": "BK3 H01",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537566",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.356131,
          54.958498
        ]
      },
      "properties": {
        "ref": "BK3 G06",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537567",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.361697,
          54.970311
        ]
      },
      "properties": {
        "ref": "BK3 G05",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537568",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.372896,
          54.993769
        ]
      },
      "properties": {
        "ref": "BK3 G03",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537569",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.378069,
          55.005452
        ]
      },
      "properties": {
        "ref": "BK3 G02",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537570",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.383622,
          55.017118
        ]
      },
      "properties": {
        "ref": "BK3 G01",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537571",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.381244,
          54.966888
        ]
      },
      "properties": {
        "ref": "BK3 F05",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537572",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.386526,
          54.978579
        ]
      },
      "properties": {
        "ref": "BK3 F04",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537573",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.392011,
          54.990222
        ]
      },
      "properties": {
        "ref": "BK3 F03",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537574",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.403106,
          55.013742
        ]
      },
      "properties": {
        "ref": "BK3 F01",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537575",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.400523,
          54.96347
        ]
      },
      "properties": {
        "ref": "BK3 E05",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537576",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.405782,
          54.975308
        ]
      },
      "properties": {
        "ref": "BK3 E04",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537577",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.411684,
          54.98702
        ]
      },
      "properties": {
        "ref": "BK3 E03",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537578",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.416964,
          54.998604
        ]
      },
      "properties": {
        "ref": "BK3 E02",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537579",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.42238,
          55.010324
        ]
      },
      "properties": {
        "ref": "BK3 E01",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537580",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.425285,
          54.971758
        ]
      },
      "properties": {
        "ref": "BK3 D04",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537581",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.430813,
          54.983522
        ]
      },
      "properties": {
        "ref": "BK3 D03",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537582",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.436202,
          54.995205
        ]
      },
      "properties": {
        "ref": "BK3 D02",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537583",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.441772,
          55.006915
        ]
      },
      "properties": {
        "ref": "BK3 D01",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537584",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.450155,
          54.980018
        ]
      },
      "properties": {
        "ref": "BK3 C03",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537585",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.455675,
          54.99177
        ]
      },
      "properties": {
        "ref": "BK3 C02",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537586",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.461272,
          55.003525
        ]
      },
      "properties": {
        "ref": "BK3 C01",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537587",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.47507,
          54.988381
        ]
      },
      "properties": {
        "ref": "BK3 B02",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537588",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.480568,
          54.999961
        ]
      },
      "properties": {
        "ref": "BK3 B01",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537589",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.499785,
          54.996564
        ]
      },
      "properties": {
        "ref": "BK3 A01",
        "windfarm_name": "MFW Bałtyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571017",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.7776,
          55.108004
        ]
      },
      "properties": {
        "ref": "BK2 J02",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571018",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.803137,
          55.086865
        ]
      },
      "properties": {
        "ref": "BK2 H04",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571019",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.80055,
          55.097815
        ]
      },
      "properties": {
        "ref": "BK2 H03",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571020",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.798163,
          55.108933
        ]
      },
      "properties": {
        "ref": "BK2 H02",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571021",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.825374,
          55.076584
        ]
      },
      "properties": {
        "ref": "BK2 G05",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571022",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.822962,
          55.087942
        ]
      },
      "properties": {
        "ref": "BK2 G04",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571023",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.820724,
          55.099058
        ]
      },
      "properties": {
        "ref": "BK2 G03",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571024",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.818688,
          55.109898
        ]
      },
      "properties": {
        "ref": "BK2 G02",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571025",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.816035,
          55.121208
        ]
      },
      "properties": {
        "ref": "BK2 G01",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571026",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.84783,
          55.066841
        ]
      },
      "properties": {
        "ref": "BK2 F06",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571027",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.845752,
          55.077734
        ]
      },
      "properties": {
        "ref": "BK2 F05",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571028",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.843453,
          55.088887
        ]
      },
      "properties": {
        "ref": "BK2 F04",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571029",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.841109,
          55.10004
        ]
      },
      "properties": {
        "ref": "BK2 F03",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571030",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.83836,
          55.111032
        ]
      },
      "properties": {
        "ref": "BK2 F02",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571031",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.836498,
          55.122311
        ]
      },
      "properties": {
        "ref": "BK2 F01",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571032",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.867979,
          55.067973
        ]
      },
      "properties": {
        "ref": "BK2 E06",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571033",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.865872,
          55.078913
        ]
      },
      "properties": {
        "ref": "BK2 E05",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571034",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.86363,
          55.090107
        ]
      },
      "properties": {
        "ref": "BK2 E04",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571035",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.858692,
          55.112335
        ]
      },
      "properties": {
        "ref": "BK2 E02",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571036",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.855997,
          55.12346
        ]
      },
      "properties": {
        "ref": "BK2 E01",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571037",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.891036,
          55.057788
        ]
      },
      "properties": {
        "ref": "BK2 D07",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571038",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.888075,
          55.068803
        ]
      },
      "properties": {
        "ref": "BK2 D06",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571039",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.886259,
          55.079969
        ]
      },
      "properties": {
        "ref": "BK2 D05",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571040",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.881528,
          55.102278
        ]
      },
      "properties": {
        "ref": "BK2 D03",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571041",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.878947,
          55.113625
        ]
      },
      "properties": {
        "ref": "BK2 D02",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571042",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.876683,
          55.124524
        ]
      },
      "properties": {
        "ref": "BK2 D01",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571043",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.913676,
          55.047667
        ]
      },
      "properties": {
        "ref": "BK2 C08",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571044",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.911206,
          55.058512
        ]
      },
      "properties": {
        "ref": "BK2 C07",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571045",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.908728,
          55.070153
        ]
      },
      "properties": {
        "ref": "BK2 C06",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571046",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.90412,
          55.092218
        ]
      },
      "properties": {
        "ref": "BK2 C04",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571047",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.898713,
          55.113625
        ]
      },
      "properties": {
        "ref": "BK2 C02",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571048",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.897143,
          55.125586
        ]
      },
      "properties": {
        "ref": "BK2 C01",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571049",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.936386,
          55.037346
        ]
      },
      "properties": {
        "ref": "BK2 B09",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571050",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.933612,
          55.048736
        ]
      },
      "properties": {
        "ref": "BK2 B08",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571051",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.931603,
          55.059844
        ]
      },
      "properties": {
        "ref": "BK2 B07",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571052",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.929119,
          55.07094
        ]
      },
      "properties": {
        "ref": "BK2 B06",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571053",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.927012,
          55.082075
        ]
      },
      "properties": {
        "ref": "BK2 B05",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571054",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.924474,
          55.093338
        ]
      },
      "properties": {
        "ref": "BK2 B04",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571055",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.922397,
          55.104129
        ]
      },
      "properties": {
        "ref": "BK2 B03",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571056",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.919539,
          55.115594
        ]
      },
      "properties": {
        "ref": "BK2 B02",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571057",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.917253,
          55.126734
        ]
      },
      "properties": {
        "ref": "BK2 B01",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571058",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.956572,
          55.038679
        ]
      },
      "properties": {
        "ref": "BK2 A09",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571059",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.954215,
          55.049798
        ]
      },
      "properties": {
        "ref": "BK2 A08",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571060",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.951729,
          55.060982
        ]
      },
      "properties": {
        "ref": "BK2 A07",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571061",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.949152,
          55.07234
        ]
      },
      "properties": {
        "ref": "BK2 A06",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571062",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.947122,
          55.08304
        ]
      },
      "properties": {
        "ref": "BK2 A05",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571063",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.944589,
          55.094174
        ]
      },
      "properties": {
        "ref": "BK2 A04",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571064",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.942171,
          55.105568
        ]
      },
      "properties": {
        "ref": "BK2 A03",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571065",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.940286,
          55.116807
        ]
      },
      "properties": {
        "ref": "BK2 A02",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571066",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.937141,
          55.127815
        ]
      },
      "properties": {
        "ref": "BK2 A01",
        "windfarm_name": "MFW Bałtyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911456",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0567631,
          55.0504196
        ]
      },
      "properties": {
        "ref": "G16",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911457",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1622825,
          55.0743378
        ]
      },
      "properties": {
        "ref": "F24",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911458",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0551455,
          55.0591053
        ]
      },
      "properties": {
        "ref": "F16",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911459",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9941304,
          55.0485219
        ]
      },
      "properties": {
        "ref": "F12",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911460",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0813636,
          55.0848456
        ]
      },
      "properties": {
        "ref": "F04",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911461",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2075857,
          55.0840771
        ]
      },
      "properties": {
        "ref": "F03",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911462",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1458066,
          55.0777019
        ]
      },
      "properties": {
        "ref": "E24",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911463",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1791493,
          55.0484522
        ]
      },
      "properties": {
        "ref": "E23",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911464",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2686514,
          55.0977064
        ]
      },
      "properties": {
        "ref": "E21",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911465",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2059193,
          55.0924367
        ]
      },
      "properties": {
        "ref": "E19",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911466",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9758563,
          55.0601681
        ]
      },
      "properties": {
        "ref": "E17",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911467",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0230822,
          55.0608831
        ]
      },
      "properties": {
        "ref": "E16",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911468",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0088411,
          55.0536374
        ]
      },
      "properties": {
        "ref": "E12",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911469",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9793608,
          55.0430696
        ]
      },
      "properties": {
        "ref": "E11",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911470",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0869851,
          55.0273099
        ]
      },
      "properties": {
        "ref": "E08",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911471",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0434323,
          55.1117412
        ]
      },
      "properties": {
        "ref": "E06",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911472",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0648528,
          55.0882262
        ]
      },
      "properties": {
        "ref": "E05",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911473",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1301531,
          55.0772407
        ]
      },
      "properties": {
        "ref": "E04",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911474",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.190976,
          55.0883098
        ]
      },
      "properties": {
        "ref": "E03",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911475",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1055493,
          55.1071516
        ]
      },
      "properties": {
        "ref": "E01",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911476",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1478105,
          55.0677214
        ]
      },
      "properties": {
        "ref": "D24",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911477",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1499056,
          55.0572808
        ]
      },
      "properties": {
        "ref": "D23",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911478",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2688604,
          55.0892943
        ]
      },
      "properties": {
        "ref": "D21",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911479",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2451116,
          55.1017964
        ]
      },
      "properties": {
        "ref": "D20",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911480",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2301688,
          55.0988386
        ]
      },
      "properties": {
        "ref": "D19",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911481",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9731758,
          55.0747308
        ]
      },
      "properties": {
        "ref": "D18",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911482",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.97761,
          55.051614
        ]
      },
      "properties": {
        "ref": "D17",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911483",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0369734,
          55.070254
        ]
      },
      "properties": {
        "ref": "D16",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911484",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1047817,
          55.070156
        ]
      },
      "properties": {
        "ref": "D15",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911485",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.996363,
          55.112844
        ]
      },
      "properties": {
        "ref": "D14",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911486",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9648261,
          55.1127935
        ]
      },
      "properties": {
        "ref": "D13",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911487",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9810708,
          55.0345578
        ]
      },
      "properties": {
        "ref": "D11",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911488",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0251062,
          55.0232963
        ]
      },
      "properties": {
        "ref": "D10",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911489",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0714114,
          55.0119444
        ]
      },
      "properties": {
        "ref": "D09",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911490",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0937594,
          55.0441843
        ]
      },
      "properties": {
        "ref": "D08",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911491",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0694532,
          55.0655434
        ]
      },
      "properties": {
        "ref": "D07",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911492",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0589623,
          55.1108384
        ]
      },
      "properties": {
        "ref": "D06",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911493",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0626572,
          55.099052
        ]
      },
      "properties": {
        "ref": "D05",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911494",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.097696,
          55.0817658
        ]
      },
      "properties": {
        "ref": "D04",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911495",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2146032,
          55.0999707
        ]
      },
      "properties": {
        "ref": "D02",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911496",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1210656,
          55.1063894
        ]
      },
      "properties": {
        "ref": "D01",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911497",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1645402,
          55.0628744
        ]
      },
      "properties": {
        "ref": "C24",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911498",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1646078,
          55.053155
        ]
      },
      "properties": {
        "ref": "C23",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911499",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1947779,
          55.0451286
        ]
      },
      "properties": {
        "ref": "C22",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911500",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2585975,
          55.0824562
        ]
      },
      "properties": {
        "ref": "C21",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968201",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2600125,
          55.1044594
        ]
      },
      "properties": {
        "ref": "C20",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968202",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2219999,
          55.0904785
        ]
      },
      "properties": {
        "ref": "C19",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968203",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.969432,
          55.0929672
        ]
      },
      "properties": {
        "ref": "C18",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968204",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9923752,
          55.057103
        ]
      },
      "properties": {
        "ref": "C17",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968205",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0403008,
          55.053899
        ]
      },
      "properties": {
        "ref": "C16",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968206",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.09799,
          55.0613748
        ]
      },
      "properties": {
        "ref": "C15",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968207",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9672475,
          55.1036004
        ]
      },
      "properties": {
        "ref": "C13",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968208",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9958896,
          55.0399172
        ]
      },
      "properties": {
        "ref": "C12",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968209",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9957653,
          55.0307631
        ]
      },
      "properties": {
        "ref": "C11",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968210",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0553818,
          55.0155813
        ]
      },
      "properties": {
        "ref": "C10",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968211",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0833658,
          55.0186629
        ]
      },
      "properties": {
        "ref": "C09",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968212",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0903423,
          55.0355816
        ]
      },
      "properties": {
        "ref": "C08",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968213",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0711803,
          55.0570204
        ]
      },
      "properties": {
        "ref": "C07",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968214",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0745694,
          55.1097361
        ]
      },
      "properties": {
        "ref": "C06",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968215",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0780704,
          55.1007932
        ]
      },
      "properties": {
        "ref": "C05",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968216",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1334114,
          55.0614587
        ]
      },
      "properties": {
        "ref": "C04",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968217",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.193193,
          55.0770045
        ]
      },
      "properties": {
        "ref": "C03",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968218",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1991803,
          55.101056
        ]
      },
      "properties": {
        "ref": "C02",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968219",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1523162,
          55.1042544
        ]
      },
      "properties": {
        "ref": "C01",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968220",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1789711,
          55.069725
        ]
      },
      "properties": {
        "ref": "B24",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968221",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.18146,
          55.057054
        ]
      },
      "properties": {
        "ref": "B23",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968222",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2084813,
          55.0496566
        ]
      },
      "properties": {
        "ref": "B22",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968223",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2484559,
          55.0756958
        ]
      },
      "properties": {
        "ref": "B21",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968224",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2531479,
          55.0921307
        ]
      },
      "properties": {
        "ref": "B20",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968225",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2241216,
          55.0801957
        ]
      },
      "properties": {
        "ref": "B19",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968226",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9712098,
          55.0843094
        ]
      },
      "properties": {
        "ref": "B18",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968227",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0069224,
          55.063323
        ]
      },
      "properties": {
        "ref": "B17",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968228",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0532572,
          55.0676888
        ]
      },
      "properties": {
        "ref": "B16",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968229",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0836215,
          55.0732349
        ]
      },
      "properties": {
        "ref": "B15",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968230",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9838966,
          55.098499
        ]
      },
      "properties": {
        "ref": "B13",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968231",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0124179,
          55.0363841
        ]
      },
      "properties": {
        "ref": "B12",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968232",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0107133,
          55.0269604
        ]
      },
      "properties": {
        "ref": "B11",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968233",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.040156,
          55.0194626
        ]
      },
      "properties": {
        "ref": "B10",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968234",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0621873,
          55.0229117
        ]
      },
      "properties": {
        "ref": "B09",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968235",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0750531,
          55.0384297
        ]
      },
      "properties": {
        "ref": "B08",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968236",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0948085,
          55.0531634
        ]
      },
      "properties": {
        "ref": "B07",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968237",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0901277,
          55.1082537
        ]
      },
      "properties": {
        "ref": "B06",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968238",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0941693,
          55.0992107
        ]
      },
      "properties": {
        "ref": "B05",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968239",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1244492,
          55.0686424
        ]
      },
      "properties": {
        "ref": "B04",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968240",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1766013,
          55.0813548
        ]
      },
      "properties": {
        "ref": "B03",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968241",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1834206,
          55.1021468
        ]
      },
      "properties": {
        "ref": "B02",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968242",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1954573,
          55.065972
        ]
      },
      "properties": {
        "ref": "A24",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968243",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1972907,
          55.0560367
        ]
      },
      "properties": {
        "ref": "A23",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968244",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2192328,
          55.0561984
        ]
      },
      "properties": {
        "ref": "A22",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968245",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2380662,
          55.068821
        ]
      },
      "properties": {
        "ref": "A21",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968246",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2386788,
          55.0861726
        ]
      },
      "properties": {
        "ref": "A20",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968247",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.209739,
          55.0734479
        ]
      },
      "properties": {
        "ref": "A19",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968248",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9880596,
          55.0774983
        ]
      },
      "properties": {
        "ref": "A18",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968249",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.034935,
          55.080421
        ]
      },
      "properties": {
        "ref": "A17",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968250",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0511983,
          55.0778228
        ]
      },
      "properties": {
        "ref": "A16",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968251",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0464878,
          55.1012788
        ]
      },
      "properties": {
        "ref": "A14",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968252",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0015856,
          55.0888283
        ]
      },
      "properties": {
        "ref": "A13",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968253",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0271258,
          55.0413545
        ]
      },
      "properties": {
        "ref": "A12",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968254",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.028885,
          55.0325845
        ]
      },
      "properties": {
        "ref": "A11",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968255",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0454692,
          55.02911
        ]
      },
      "properties": {
        "ref": "A10",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968256",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0606304,
          55.0313519
        ]
      },
      "properties": {
        "ref": "A09",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968257",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0590883,
          55.0397397
        ]
      },
      "properties": {
        "ref": "A08",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968258",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1101143,
          55.0981785
        ]
      },
      "properties": {
        "ref": "A06",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968259",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0958953,
          55.0906748
        ]
      },
      "properties": {
        "ref": "A05",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968260",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.159819,
          55.0856844
        ]
      },
      "properties": {
        "ref": "A03",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968261",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1678501,
          55.1031909
        ]
      },
      "properties": {
        "ref": "A02",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968262",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1265507,
          55.0951985
        ]
      },
      "properties": {
        "ref": "A01",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/common-windfarm-turbine/context.jsonld",
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128565",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.653582,
          55.006667
        ]
      },
      "properties": {
        "ref": "76",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128566",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.63486,
          55.020635
        ]
      },
      "properties": {
        "ref": "75",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128567",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.661072,
          55.080457
        ]
      },
      "properties": {
        "ref": "74",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128568",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.64328,
          55.060358
        ]
      },
      "properties": {
        "ref": "73",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128569",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.64,
          55.049375
        ]
      },
      "properties": {
        "ref": "72",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128570",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.66812,
          55.10027
        ]
      },
      "properties": {
        "ref": "71",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128571",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.610119,
          55.043869
        ]
      },
      "properties": {
        "ref": "70",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128572",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.683461,
          55.066143
        ]
      },
      "properties": {
        "ref": "69",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128573",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.747624,
          55.099235
        ]
      },
      "properties": {
        "ref": "68",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128574",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.654354,
          55.071385
        ]
      },
      "properties": {
        "ref": "67",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128575",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.640016,
          55.039663
        ]
      },
      "properties": {
        "ref": "66",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128576",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.635311,
          55.029823
        ]
      },
      "properties": {
        "ref": "65",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128577",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.628869,
          55.00997
        ]
      },
      "properties": {
        "ref": "64",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128578",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.626832,
          55.000814
        ]
      },
      "properties": {
        "ref": "63",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128579",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.589261,
          54.993376
        ]
      },
      "properties": {
        "ref": "62",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128580",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.716839,
          55.090599
        ]
      },
      "properties": {
        "ref": "61",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128581",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.663009,
          55.091074
        ]
      },
      "properties": {
        "ref": "60",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128582",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.67817,
          55.109397
        ]
      },
      "properties": {
        "ref": "59",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128583",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.672281,
          55.0146
        ]
      },
      "properties": {
        "ref": "58",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128584",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.672183,
          55.023284
        ]
      },
      "properties": {
        "ref": "57",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128585",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.675452,
          55.031888
        ]
      },
      "properties": {
        "ref": "56",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128586",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.675065,
          55.040864
        ]
      },
      "properties": {
        "ref": "55",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128587",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.673089,
          55.049809
        ]
      },
      "properties": {
        "ref": "54",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128588",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.668436,
          55.058796
        ]
      },
      "properties": {
        "ref": "53",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128589",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.685713,
          55.076469
        ]
      },
      "properties": {
        "ref": "52",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128590",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.689498,
          55.087969
        ]
      },
      "properties": {
        "ref": "51",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128591",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.694919,
          55.098781
        ]
      },
      "properties": {
        "ref": "50",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128592",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.701642,
          55.10965
        ]
      },
      "properties": {
        "ref": "49",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128593",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.594355,
          55.003223
        ]
      },
      "properties": {
        "ref": "48",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128594",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.602226,
          55.014896
        ]
      },
      "properties": {
        "ref": "47",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128595",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.604322,
          55.024106
        ]
      },
      "properties": {
        "ref": "46",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128596",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.606384,
          55.034685
        ]
      },
      "properties": {
        "ref": "45",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128597",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.616112,
          55.052976
        ]
      },
      "properties": {
        "ref": "44",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128598",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.61844,
          55.063799
        ]
      },
      "properties": {
        "ref": "43",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128599",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.624618,
          55.074478
        ]
      },
      "properties": {
        "ref": "42",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185128600",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.632259,
          55.083729
        ]
      },
      "properties": {
        "ref": "41",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129401",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.636667,
          55.092805
        ]
      },
      "properties": {
        "ref": "40",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129402",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.638176,
          55.102896
        ]
      },
      "properties": {
        "ref": "39",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129403",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.654604,
          55.109176
        ]
      },
      "properties": {
        "ref": "38",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129404",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.722445,
          55.10092
        ]
      },
      "properties": {
        "ref": "37",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129405",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.724589,
          55.109811
        ]
      },
      "properties": {
        "ref": "36",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129406",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.747051,
          55.108198
        ]
      },
      "properties": {
        "ref": "35",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129407",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.743457,
          55.090149
        ]
      },
      "properties": {
        "ref": "34",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129408",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.769843,
          55.108576
        ]
      },
      "properties": {
        "ref": "33",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129409",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.771604,
          55.098788
        ]
      },
      "properties": {
        "ref": "32",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129410",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.76571,
          55.088551
        ]
      },
      "properties": {
        "ref": "31",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129411",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708551,
          55.080982
        ]
      },
      "properties": {
        "ref": "30",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129412",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708551,
          55.071803
        ]
      },
      "properties": {
        "ref": "29",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129413",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.70855,
          55.06282
        ]
      },
      "properties": {
        "ref": "28",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129414",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708564,
          55.053803
        ]
      },
      "properties": {
        "ref": "27",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129415",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.70858,
          55.044819
        ]
      },
      "properties": {
        "ref": "26",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129416",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708615,
          55.035834
        ]
      },
      "properties": {
        "ref": "25",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129417",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708638,
          55.023444
        ]
      },
      "properties": {
        "ref": "24",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129418",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708593,
          55.014232
        ]
      },
      "properties": {
        "ref": "23",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129419",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708956,
          55.005267
        ]
      },
      "properties": {
        "ref": "22",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129420",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.688873,
          55.008866
        ]
      },
      "properties": {
        "ref": "21",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129421",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.673768,
          55.001274
        ]
      },
      "properties": {
        "ref": "20",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129422",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.650697,
          54.995819
        ]
      },
      "properties": {
        "ref": "19",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129423",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.628481,
          54.991824
        ]
      },
      "properties": {
        "ref": "18",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129424",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.607432,
          54.987943
        ]
      },
      "properties": {
        "ref": "17",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129425",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.58752,
          54.982886
        ]
      },
      "properties": {
        "ref": "16",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129426",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.621821,
          55.108774
        ]
      },
      "properties": {
        "ref": "15",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129427",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.616341,
          55.099549
        ]
      },
      "properties": {
        "ref": "14",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129428",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.612253,
          55.088796
        ]
      },
      "properties": {
        "ref": "13",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129429",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.603759,
          55.079589
        ]
      },
      "properties": {
        "ref": "12",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129430",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.595467,
          55.070586
        ]
      },
      "properties": {
        "ref": "11",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129431",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.587049,
          55.061441
        ]
      },
      "properties": {
        "ref": "10",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129432",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.583794,
          55.05254
        ]
      },
      "properties": {
        "ref": "9",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129433",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.581526,
          55.043584
        ]
      },
      "properties": {
        "ref": "8",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129434",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.579247,
          55.034576
        ]
      },
      "properties": {
        "ref": "7",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129435",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.576959,
          55.025528
        ]
      },
      "properties": {
        "ref": "6",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129436",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.57467,
          55.016476
        ]
      },
      "properties": {
        "ref": "5",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129437",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.572366,
          55.007357
        ]
      },
      "properties": {
        "ref": "4",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129438",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.570083,
          54.998319
        ]
      },
      "properties": {
        "ref": "3",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129439",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.567802,
          54.989286
        ]
      },
      "properties": {
        "ref": "2",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14185129440",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.565519,
          54.980271
        ]
      },
      "properties": {
        "ref": "1",
        "windfarm_name": "Baltic Power",
        "windfarm": "https://www.openstreetmap.org/relation/21402440",
        "manufacturer": "Vestas",
        "model": "V236-15.0 MW",
        "rated_power_mw": 15.0,
        "hub_height_m": 141.0,
        "rotor_diameter_m": 236.0,
        "rotor_axis": "horizontal_axis",
        "offshore": true,
        "operator": null,
        "status": null,
        "last_updated": "2026-09-16T14:23:07Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537540",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.270053,
          54.998782
        ]
      },
      "properties": {
        "ref": "BK3 M04",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537541",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.275409,
          55.010672
        ]
      },
      "properties": {
        "ref": "BK3 M03",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537542",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.281049,
          55.022455
        ]
      },
      "properties": {
        "ref": "BK3 M02",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537543",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.283813,
          54.983888
        ]
      },
      "properties": {
        "ref": "BK3 L05",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537544",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.289463,
          54.99559
        ]
      },
      "properties": {
        "ref": "BK3 L04",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537545",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.29541,
          55.007347
        ]
      },
      "properties": {
        "ref": "BK3 L03",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537546",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.30046,
          55.019018
        ]
      },
      "properties": {
        "ref": "BK3 L02",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537547",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.306081,
          55.030645
        ]
      },
      "properties": {
        "ref": "BK3 L01",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537548",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.292501,
          54.957068
        ]
      },
      "properties": {
        "ref": "BK3 K07",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537549",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.298174,
          54.968722
        ]
      },
      "properties": {
        "ref": "BK3 K06",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537550",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.303485,
          54.980528
        ]
      },
      "properties": {
        "ref": "BK3 K05",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537551",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.308958,
          54.992256
        ]
      },
      "properties": {
        "ref": "BK3 K04",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537552",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.314493,
          55.003671
        ]
      },
      "properties": {
        "ref": "BK3 K03",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537553",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.319906,
          55.015593
        ]
      },
      "properties": {
        "ref": "BK3 K02",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537554",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.325594,
          55.027275
        ]
      },
      "properties": {
        "ref": "BK3 K01",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537555",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.311847,
          54.953732
        ]
      },
      "properties": {
        "ref": "BK3 J07",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537556",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.31743,
          54.965356
        ]
      },
      "properties": {
        "ref": "BK3 J06",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537557",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.322872,
          54.977064
        ]
      },
      "properties": {
        "ref": "BK3 J05",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537558",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.328485,
          54.988852
        ]
      },
      "properties": {
        "ref": "BK3 J04",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537559",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.333772,
          55.000446
        ]
      },
      "properties": {
        "ref": "BK3 J03",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537560",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.339309,
          55.012201
        ]
      },
      "properties": {
        "ref": "BK3 J02",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537561",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.344812,
          55.023919
        ]
      },
      "properties": {
        "ref": "BK3 J01",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537562",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.336774,
          54.962085
        ]
      },
      "properties": {
        "ref": "BK3 H06",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537563",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.342261,
          54.973665
        ]
      },
      "properties": {
        "ref": "BK3 H05",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537564",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.347981,
          54.985377
        ]
      },
      "properties": {
        "ref": "BK3 H04",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537565",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.364254,
          55.020548
        ]
      },
      "properties": {
        "ref": "BK3 H01",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537566",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.356131,
          54.958498
        ]
      },
      "properties": {
        "ref": "BK3 G06",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537567",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.361697,
          54.970311
        ]
      },
      "properties": {
        "ref": "BK3 G05",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537568",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.372896,
          54.993769
        ]
      },
      "properties": {
        "ref": "BK3 G03",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537569",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.378069,
          55.005452
        ]
      },
      "properties": {
        "ref": "BK3 G02",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537570",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.383622,
          55.017118
        ]
      },
      "properties": {
        "ref": "BK3 G01",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537571",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.381244,
          54.966888
        ]
      },
      "properties": {
        "ref": "BK3 F05",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537572",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.386526,
          54.978579
        ]
      },
      "properties": {
        "ref": "BK3 F04",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537573",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.392011,
          54.990222
        ]
      },
      "properties": {
        "ref": "BK3 F03",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537574",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.403106,
          55.013742
        ]
      },
      "properties": {
        "ref": "BK3 F01",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537575",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.400523,
          54.96347
        ]
      },
      "properties": {
        "ref": "BK3 E05",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537576",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.405782,
          54.975308
        ]
      },
      "properties": {
        "ref": "BK3 E04",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537577",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.411684,
          54.98702
        ]
      },
      "properties": {
        "ref": "BK3 E03",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537578",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.416964,
          54.998604
        ]
      },
      "properties": {
        "ref": "BK3 E02",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537579",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.42238,
          55.010324
        ]
      },
      "properties": {
        "ref": "BK3 E01",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537580",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.425285,
          54.971758
        ]
      },
      "properties": {
        "ref": "BK3 D04",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537581",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.430813,
          54.983522
        ]
      },
      "properties": {
        "ref": "BK3 D03",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537582",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.436202,
          54.995205
        ]
      },
      "properties": {
        "ref": "BK3 D02",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537583",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.441772,
          55.006915
        ]
      },
      "properties": {
        "ref": "BK3 D01",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537584",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.450155,
          54.980018
        ]
      },
      "properties": {
        "ref": "BK3 C03",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537585",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.455675,
          54.99177
        ]
      },
      "properties": {
        "ref": "BK3 C02",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537586",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.461272,
          55.003525
        ]
      },
      "properties": {
        "ref": "BK3 C01",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537587",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.47507,
          54.988381
        ]
      },
      "properties": {
        "ref": "BK3 B02",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537588",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.480568,
          54.999961
        ]
      },
      "properties": {
        "ref": "BK3 B01",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191537589",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.499785,
          54.996564
        ]
      },
      "properties": {
        "ref": "BK3 A01",
        "windfarm_name": "MFW Ba\u0142tyk III",
        "windfarm": "https://www.openstreetmap.org/relation/21409512",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:34:04Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571017",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.7776,
          55.108004
        ]
      },
      "properties": {
        "ref": "BK2 J02",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571018",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.803137,
          55.086865
        ]
      },
      "properties": {
        "ref": "BK2 H04",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571019",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.80055,
          55.097815
        ]
      },
      "properties": {
        "ref": "BK2 H03",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571020",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.798163,
          55.108933
        ]
      },
      "properties": {
        "ref": "BK2 H02",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571021",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.825374,
          55.076584
        ]
      },
      "properties": {
        "ref": "BK2 G05",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571022",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.822962,
          55.087942
        ]
      },
      "properties": {
        "ref": "BK2 G04",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571023",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.820724,
          55.099058
        ]
      },
      "properties": {
        "ref": "BK2 G03",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571024",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.818688,
          55.109898
        ]
      },
      "properties": {
        "ref": "BK2 G02",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571025",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.816035,
          55.121208
        ]
      },
      "properties": {
        "ref": "BK2 G01",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571026",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.84783,
          55.066841
        ]
      },
      "properties": {
        "ref": "BK2 F06",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571027",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.845752,
          55.077734
        ]
      },
      "properties": {
        "ref": "BK2 F05",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571028",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.843453,
          55.088887
        ]
      },
      "properties": {
        "ref": "BK2 F04",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571029",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.841109,
          55.10004
        ]
      },
      "properties": {
        "ref": "BK2 F03",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571030",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.83836,
          55.111032
        ]
      },
      "properties": {
        "ref": "BK2 F02",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571031",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.836498,
          55.122311
        ]
      },
      "properties": {
        "ref": "BK2 F01",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571032",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.867979,
          55.067973
        ]
      },
      "properties": {
        "ref": "BK2 E06",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571033",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.865872,
          55.078913
        ]
      },
      "properties": {
        "ref": "BK2 E05",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571034",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.86363,
          55.090107
        ]
      },
      "properties": {
        "ref": "BK2 E04",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571035",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.858692,
          55.112335
        ]
      },
      "properties": {
        "ref": "BK2 E02",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571036",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.855997,
          55.12346
        ]
      },
      "properties": {
        "ref": "BK2 E01",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571037",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.891036,
          55.057788
        ]
      },
      "properties": {
        "ref": "BK2 D07",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571038",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.888075,
          55.068803
        ]
      },
      "properties": {
        "ref": "BK2 D06",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571039",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.886259,
          55.079969
        ]
      },
      "properties": {
        "ref": "BK2 D05",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571040",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.881528,
          55.102278
        ]
      },
      "properties": {
        "ref": "BK2 D03",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571041",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.878947,
          55.113625
        ]
      },
      "properties": {
        "ref": "BK2 D02",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571042",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.876683,
          55.124524
        ]
      },
      "properties": {
        "ref": "BK2 D01",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571043",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.913676,
          55.047667
        ]
      },
      "properties": {
        "ref": "BK2 C08",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571044",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.911206,
          55.058512
        ]
      },
      "properties": {
        "ref": "BK2 C07",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571045",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.908728,
          55.070153
        ]
      },
      "properties": {
        "ref": "BK2 C06",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571046",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.90412,
          55.092218
        ]
      },
      "properties": {
        "ref": "BK2 C04",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571047",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.898713,
          55.113625
        ]
      },
      "properties": {
        "ref": "BK2 C02",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571048",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.897143,
          55.125586
        ]
      },
      "properties": {
        "ref": "BK2 C01",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571049",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.936386,
          55.037346
        ]
      },
      "properties": {
        "ref": "BK2 B09",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571050",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.933612,
          55.048736
        ]
      },
      "properties": {
        "ref": "BK2 B08",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571051",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.931603,
          55.059844
        ]
      },
      "properties": {
        "ref": "BK2 B07",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571052",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.929119,
          55.07094
        ]
      },
      "properties": {
        "ref": "BK2 B06",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571053",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.927012,
          55.082075
        ]
      },
      "properties": {
        "ref": "BK2 B05",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571054",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.924474,
          55.093338
        ]
      },
      "properties": {
        "ref": "BK2 B04",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571055",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.922397,
          55.104129
        ]
      },
      "properties": {
        "ref": "BK2 B03",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571056",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.919539,
          55.115594
        ]
      },
      "properties": {
        "ref": "BK2 B02",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571057",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.917253,
          55.126734
        ]
      },
      "properties": {
        "ref": "BK2 B01",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571058",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.956572,
          55.038679
        ]
      },
      "properties": {
        "ref": "BK2 A09",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571059",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.954215,
          55.049798
        ]
      },
      "properties": {
        "ref": "BK2 A08",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571060",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.951729,
          55.060982
        ]
      },
      "properties": {
        "ref": "BK2 A07",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571061",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.949152,
          55.07234
        ]
      },
      "properties": {
        "ref": "BK2 A06",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571062",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.947122,
          55.08304
        ]
      },
      "properties": {
        "ref": "BK2 A05",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571063",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.944589,
          55.094174
        ]
      },
      "properties": {
        "ref": "BK2 A04",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571064",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.942171,
          55.105568
        ]
      },
      "properties": {
        "ref": "BK2 A03",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571065",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.940286,
          55.116807
        ]
      },
      "properties": {
        "ref": "BK2 A02",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191571066",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.937141,
          55.127815
        ]
      },
      "properties": {
        "ref": "BK2 A01",
        "windfarm_name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "windfarm": "https://www.openstreetmap.org/relation/21409513",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-236 DD",
        "rated_power_mw": null,
        "hub_height_m": null,
        "rotor_diameter_m": 236.0,
        "rotor_axis": null,
        "offshore": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "status": "underConstruction",
        "last_updated": "2026-09-18T12:35:13Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911456",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0567631,
          55.0504196
        ]
      },
      "properties": {
        "ref": "G16",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911457",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1622825,
          55.0743378
        ]
      },
      "properties": {
        "ref": "F24",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911458",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0551455,
          55.0591053
        ]
      },
      "properties": {
        "ref": "F16",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911459",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9941304,
          55.0485219
        ]
      },
      "properties": {
        "ref": "F12",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911460",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0813636,
          55.0848456
        ]
      },
      "properties": {
        "ref": "F04",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911461",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2075857,
          55.0840771
        ]
      },
      "properties": {
        "ref": "F03",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911462",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1458066,
          55.0777019
        ]
      },
      "properties": {
        "ref": "E24",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911463",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1791493,
          55.0484522
        ]
      },
      "properties": {
        "ref": "E23",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911464",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2686514,
          55.0977064
        ]
      },
      "properties": {
        "ref": "E21",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911465",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2059193,
          55.0924367
        ]
      },
      "properties": {
        "ref": "E19",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911466",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9758563,
          55.0601681
        ]
      },
      "properties": {
        "ref": "E17",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911467",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0230822,
          55.0608831
        ]
      },
      "properties": {
        "ref": "E16",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911468",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0088411,
          55.0536374
        ]
      },
      "properties": {
        "ref": "E12",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911469",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9793608,
          55.0430696
        ]
      },
      "properties": {
        "ref": "E11",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911470",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0869851,
          55.0273099
        ]
      },
      "properties": {
        "ref": "E08",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911471",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0434323,
          55.1117412
        ]
      },
      "properties": {
        "ref": "E06",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911472",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0648528,
          55.0882262
        ]
      },
      "properties": {
        "ref": "E05",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911473",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1301531,
          55.0772407
        ]
      },
      "properties": {
        "ref": "E04",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911474",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.190976,
          55.0883098
        ]
      },
      "properties": {
        "ref": "E03",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911475",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1055493,
          55.1071516
        ]
      },
      "properties": {
        "ref": "E01",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911476",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1478105,
          55.0677214
        ]
      },
      "properties": {
        "ref": "D24",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911477",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1499056,
          55.0572808
        ]
      },
      "properties": {
        "ref": "D23",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911478",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2688604,
          55.0892943
        ]
      },
      "properties": {
        "ref": "D21",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911479",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2451116,
          55.1017964
        ]
      },
      "properties": {
        "ref": "D20",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911480",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2301688,
          55.0988386
        ]
      },
      "properties": {
        "ref": "D19",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911481",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9731758,
          55.0747308
        ]
      },
      "properties": {
        "ref": "D18",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911482",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.97761,
          55.051614
        ]
      },
      "properties": {
        "ref": "D17",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911483",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0369734,
          55.070254
        ]
      },
      "properties": {
        "ref": "D16",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911484",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1047817,
          55.070156
        ]
      },
      "properties": {
        "ref": "D15",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911485",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.996363,
          55.112844
        ]
      },
      "properties": {
        "ref": "D14",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911486",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9648261,
          55.1127935
        ]
      },
      "properties": {
        "ref": "D13",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911487",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9810708,
          55.0345578
        ]
      },
      "properties": {
        "ref": "D11",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911488",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0251062,
          55.0232963
        ]
      },
      "properties": {
        "ref": "D10",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911489",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0714114,
          55.0119444
        ]
      },
      "properties": {
        "ref": "D09",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911490",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0937594,
          55.0441843
        ]
      },
      "properties": {
        "ref": "D08",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911491",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0694532,
          55.0655434
        ]
      },
      "properties": {
        "ref": "D07",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911492",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0589623,
          55.1108384
        ]
      },
      "properties": {
        "ref": "D06",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911493",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0626572,
          55.099052
        ]
      },
      "properties": {
        "ref": "D05",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911494",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.097696,
          55.0817658
        ]
      },
      "properties": {
        "ref": "D04",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911495",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2146032,
          55.0999707
        ]
      },
      "properties": {
        "ref": "D02",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911496",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1210656,
          55.1063894
        ]
      },
      "properties": {
        "ref": "D01",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911497",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1645402,
          55.0628744
        ]
      },
      "properties": {
        "ref": "C24",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911498",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1646078,
          55.053155
        ]
      },
      "properties": {
        "ref": "C23",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911499",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1947779,
          55.0451286
        ]
      },
      "properties": {
        "ref": "C22",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191911500",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2585975,
          55.0824562
        ]
      },
      "properties": {
        "ref": "C21",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968201",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2600125,
          55.1044594
        ]
      },
      "properties": {
        "ref": "C20",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968202",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2219999,
          55.0904785
        ]
      },
      "properties": {
        "ref": "C19",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968203",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.969432,
          55.0929672
        ]
      },
      "properties": {
        "ref": "C18",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968204",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9923752,
          55.057103
        ]
      },
      "properties": {
        "ref": "C17",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968205",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0403008,
          55.053899
        ]
      },
      "properties": {
        "ref": "C16",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968206",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.09799,
          55.0613748
        ]
      },
      "properties": {
        "ref": "C15",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968207",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9672475,
          55.1036004
        ]
      },
      "properties": {
        "ref": "C13",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968208",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9958896,
          55.0399172
        ]
      },
      "properties": {
        "ref": "C12",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968209",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9957653,
          55.0307631
        ]
      },
      "properties": {
        "ref": "C11",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968210",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0553818,
          55.0155813
        ]
      },
      "properties": {
        "ref": "C10",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968211",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0833658,
          55.0186629
        ]
      },
      "properties": {
        "ref": "C09",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968212",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0903423,
          55.0355816
        ]
      },
      "properties": {
        "ref": "C08",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968213",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0711803,
          55.0570204
        ]
      },
      "properties": {
        "ref": "C07",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968214",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0745694,
          55.1097361
        ]
      },
      "properties": {
        "ref": "C06",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968215",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0780704,
          55.1007932
        ]
      },
      "properties": {
        "ref": "C05",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968216",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1334114,
          55.0614587
        ]
      },
      "properties": {
        "ref": "C04",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968217",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.193193,
          55.0770045
        ]
      },
      "properties": {
        "ref": "C03",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968218",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1991803,
          55.101056
        ]
      },
      "properties": {
        "ref": "C02",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968219",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1523162,
          55.1042544
        ]
      },
      "properties": {
        "ref": "C01",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968220",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1789711,
          55.069725
        ]
      },
      "properties": {
        "ref": "B24",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968221",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.18146,
          55.057054
        ]
      },
      "properties": {
        "ref": "B23",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968222",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2084813,
          55.0496566
        ]
      },
      "properties": {
        "ref": "B22",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968223",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2484559,
          55.0756958
        ]
      },
      "properties": {
        "ref": "B21",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968224",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2531479,
          55.0921307
        ]
      },
      "properties": {
        "ref": "B20",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968225",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2241216,
          55.0801957
        ]
      },
      "properties": {
        "ref": "B19",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968226",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9712098,
          55.0843094
        ]
      },
      "properties": {
        "ref": "B18",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968227",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0069224,
          55.063323
        ]
      },
      "properties": {
        "ref": "B17",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968228",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0532572,
          55.0676888
        ]
      },
      "properties": {
        "ref": "B16",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968229",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0836215,
          55.0732349
        ]
      },
      "properties": {
        "ref": "B15",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968230",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9838966,
          55.098499
        ]
      },
      "properties": {
        "ref": "B13",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968231",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0124179,
          55.0363841
        ]
      },
      "properties": {
        "ref": "B12",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968232",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0107133,
          55.0269604
        ]
      },
      "properties": {
        "ref": "B11",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968233",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.040156,
          55.0194626
        ]
      },
      "properties": {
        "ref": "B10",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968234",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0621873,
          55.0229117
        ]
      },
      "properties": {
        "ref": "B09",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968235",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0750531,
          55.0384297
        ]
      },
      "properties": {
        "ref": "B08",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968236",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0948085,
          55.0531634
        ]
      },
      "properties": {
        "ref": "B07",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968237",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0901277,
          55.1082537
        ]
      },
      "properties": {
        "ref": "B06",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968238",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0941693,
          55.0992107
        ]
      },
      "properties": {
        "ref": "B05",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968239",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1244492,
          55.0686424
        ]
      },
      "properties": {
        "ref": "B04",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968240",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1766013,
          55.0813548
        ]
      },
      "properties": {
        "ref": "B03",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968241",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1834206,
          55.1021468
        ]
      },
      "properties": {
        "ref": "B02",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968242",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1954573,
          55.065972
        ]
      },
      "properties": {
        "ref": "A24",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968243",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1972907,
          55.0560367
        ]
      },
      "properties": {
        "ref": "A23",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968244",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2192328,
          55.0561984
        ]
      },
      "properties": {
        "ref": "A22",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968245",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2380662,
          55.068821
        ]
      },
      "properties": {
        "ref": "A21",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968246",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.2386788,
          55.0861726
        ]
      },
      "properties": {
        "ref": "A20",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968247",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.209739,
          55.0734479
        ]
      },
      "properties": {
        "ref": "A19",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968248",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.9880596,
          55.0774983
        ]
      },
      "properties": {
        "ref": "A18",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968249",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.034935,
          55.080421
        ]
      },
      "properties": {
        "ref": "A17",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968250",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0511983,
          55.0778228
        ]
      },
      "properties": {
        "ref": "A16",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968251",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0464878,
          55.1012788
        ]
      },
      "properties": {
        "ref": "A14",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968252",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0015856,
          55.0888283
        ]
      },
      "properties": {
        "ref": "A13",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968253",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0271258,
          55.0413545
        ]
      },
      "properties": {
        "ref": "A12",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968254",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.028885,
          55.0325845
        ]
      },
      "properties": {
        "ref": "A11",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968255",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0454692,
          55.02911
        ]
      },
      "properties": {
        "ref": "A10",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968256",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0606304,
          55.0313519
        ]
      },
      "properties": {
        "ref": "A09",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968257",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0590883,
          55.0397397
        ]
      },
      "properties": {
        "ref": "A08",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968258",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1101143,
          55.0981785
        ]
      },
      "properties": {
        "ref": "A06",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968259",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.0958953,
          55.0906748
        ]
      },
      "properties": {
        "ref": "A05",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968260",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.159819,
          55.0856844
        ]
      },
      "properties": {
        "ref": "A03",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968261",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1678501,
          55.1031909
        ]
      },
      "properties": {
        "ref": "A02",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/node/14191968262",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1265507,
          55.0951985
        ]
      },
      "properties": {
        "ref": "A01",
        "windfarm_name": "Baltica 2",
        "windfarm": "https://www.openstreetmap.org/relation/21410256",
        "manufacturer": "Siemens Gamesa",
        "model": "SG 14-222 DD",
        "rated_power_mw": 14.0,
        "hub_height_m": null,
        "rotor_diameter_m": 222.0,
        "rotor_axis": "horizontal_axis",
        "offshore": null,
        "operator": [
          "PGE",
          "Orsted"
        ],
        "status": null,
        "last_updated": "2026-09-27T23:02:59Z"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix inspire-cofv: <http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/> .
@prefix owf: <https://w3id.org/ogc/hosted/seadots/windfarm#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://www.openstreetmap.org/node/14185128565> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.765358e+01 5.500667e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "76" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128566> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.763486e+01 5.502063e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "75" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128567> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.766107e+01 5.508046e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "74" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128568> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.764328e+01 5.506036e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "73" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128569> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.764e+01 5.504937e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "72" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128570> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.766812e+01 5.510027e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "71" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128571> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.761012e+01 5.504387e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "70" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128572> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.768346e+01 5.506614e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "69" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128573> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.774762e+01 5.509924e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "68" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128574> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.765435e+01 5.507138e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "67" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128575> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.764002e+01 5.503966e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "66" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128576> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.763531e+01 5.502982e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "65" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128577> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.762887e+01 5.500997e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "64" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128578> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.762683e+01 5.500081e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "63" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128579> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.758926e+01 5.499338e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "62" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128580> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.771684e+01 5.50906e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "61" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128581> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.766301e+01 5.509107e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "60" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128582> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.767817e+01 5.51094e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "59" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128583> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.767228e+01 5.50146e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "58" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128584> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.767218e+01 5.502328e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "57" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128585> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.767545e+01 5.503189e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "56" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128586> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.767507e+01 5.504086e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "55" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128587> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.767309e+01 5.504981e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "54" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128588> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.766844e+01 5.50588e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "53" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128589> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.768571e+01 5.507647e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "52" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128590> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.76895e+01 5.508797e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "51" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128591> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.769492e+01 5.509878e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "50" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128592> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770164e+01 5.510965e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "49" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128593> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.759436e+01 5.500322e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "48" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128594> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.760223e+01 5.50149e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "47" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128595> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.760432e+01 5.502411e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "46" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128596> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.760638e+01 5.503469e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "45" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128597> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.761611e+01 5.505298e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "44" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128598> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.761844e+01 5.50638e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "43" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128599> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.762462e+01 5.507448e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "42" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185128600> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.763226e+01 5.508373e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "41" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129401> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.763667e+01 5.50928e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "40" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129402> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.763818e+01 5.51029e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "39" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129403> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.76546e+01 5.510918e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "38" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129404> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.772245e+01 5.510092e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "37" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129405> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.772459e+01 5.510981e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "36" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129406> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.774705e+01 5.51082e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "35" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129407> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.774346e+01 5.509015e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "34" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129408> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.776984e+01 5.510858e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "33" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129409> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.77716e+01 5.509879e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "32" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129410> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.776571e+01 5.508855e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "31" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129411> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770855e+01 5.508098e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "30" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129412> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770855e+01 5.50718e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "29" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129413> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770855e+01 5.506282e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "28" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129414> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770856e+01 5.50538e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "27" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129415> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770858e+01 5.504482e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "26" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129416> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770862e+01 5.503583e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "25" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129417> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770864e+01 5.502344e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "24" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129418> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770859e+01 5.501423e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "23" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129419> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770896e+01 5.500527e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "22" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129420> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.768887e+01 5.500887e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "21" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129421> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.767377e+01 5.500127e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "20" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129422> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.76507e+01 5.499582e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "19" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129423> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.762848e+01 5.499182e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "18" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129424> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.760743e+01 5.498794e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "17" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129425> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.758752e+01 5.498289e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "16" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129426> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.762182e+01 5.510877e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "15" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129427> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.761634e+01 5.509955e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "14" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129428> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.761225e+01 5.50888e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "13" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129429> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.760376e+01 5.507959e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "12" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129430> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.759547e+01 5.507059e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "11" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129431> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.758705e+01 5.506144e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "10" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129432> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.758379e+01 5.505254e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "9" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129433> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.758153e+01 5.504358e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "8" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129434> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.757925e+01 5.503458e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "7" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129435> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.757696e+01 5.502553e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "6" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129436> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.757467e+01 5.501648e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "5" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129437> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.757237e+01 5.500736e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "4" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129438> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.757008e+01 5.499832e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "3" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129439> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.75678e+01 5.498929e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "2" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14185129440> a geojson:Feature ;
    dcterms:modified "2026-09-16T14:23:07+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.756552e+01 5.498027e+01 ) ] ;
    owf:hubHeight 141.0 ;
    owf:manufacturerName "Vestas" ;
    owf:modelName "V236-15.0 MW" ;
    owf:offshore true ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21402440> ;
    owf:ratedPowerMW 15.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "1" ;
    owf:windfarmName "Baltic Power" .

<https://www.openstreetmap.org/node/14191537540> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.727005e+01 5.499878e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 M04" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537541> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.727541e+01 5.501067e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 M03" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537542> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.728105e+01 5.502246e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 M02" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537543> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.728381e+01 5.498389e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 L05" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537544> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.728946e+01 5.499559e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 L04" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537545> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.729541e+01 5.500735e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 L03" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537546> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.730046e+01 5.501902e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 L02" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537547> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.730608e+01 5.503064e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 L01" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537548> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.72925e+01 5.495707e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 K07" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537549> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.729817e+01 5.496872e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 K06" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537550> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.730348e+01 5.498053e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 K05" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537551> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.730896e+01 5.499226e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 K04" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537552> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.731449e+01 5.500367e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 K03" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537553> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.731991e+01 5.501559e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 K02" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537554> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.732559e+01 5.502728e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 K01" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537555> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.731185e+01 5.495373e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 J07" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537556> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.731743e+01 5.496536e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 J06" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537557> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.732287e+01 5.497706e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 J05" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537558> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.732849e+01 5.498885e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 J04" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537559> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.733377e+01 5.500045e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 J03" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537560> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.733931e+01 5.50122e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 J02" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537561> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.734481e+01 5.502392e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 J01" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537562> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.733677e+01 5.496209e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 H06" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537563> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.734226e+01 5.497366e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 H05" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537564> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.734798e+01 5.498538e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 H04" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537565> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.736425e+01 5.502055e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 H01" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537566> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.735613e+01 5.49585e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 G06" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537567> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.73617e+01 5.497031e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 G05" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537568> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.73729e+01 5.499377e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 G03" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537569> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.737807e+01 5.500545e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 G02" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537570> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.738362e+01 5.501712e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 G01" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537571> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.738124e+01 5.496689e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 F05" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537572> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.738653e+01 5.497858e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 F04" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537573> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.739201e+01 5.499022e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 F03" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537574> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.740311e+01 5.501374e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 F01" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537575> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.740052e+01 5.496347e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 E05" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537576> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.740578e+01 5.497531e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 E04" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537577> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.741168e+01 5.498702e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 E03" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537578> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.741696e+01 5.49986e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 E02" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537579> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.742238e+01 5.501032e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 E01" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537580> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.742528e+01 5.497176e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 D04" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537581> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.743081e+01 5.498352e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 D03" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537582> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.74362e+01 5.49952e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 D02" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537583> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.744177e+01 5.500691e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 D01" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537584> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.745015e+01 5.498002e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 C03" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537585> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.745567e+01 5.499177e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 C02" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537586> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.746127e+01 5.500353e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 C01" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537587> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.747507e+01 5.498838e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 B02" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537588> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.748057e+01 5.499996e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 B01" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191537589> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.749978e+01 5.499656e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409512> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK3 A01" ;
    owf:windfarmName "MFW Bałtyk III" .

<https://www.openstreetmap.org/node/14191571017> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.67776e+01 5.5108e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 J02" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571018> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.680314e+01 5.508687e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 H04" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571019> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.680055e+01 5.509781e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 H03" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571020> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.679816e+01 5.510893e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 H02" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571021> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.682537e+01 5.507658e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 G05" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571022> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.682296e+01 5.508794e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 G04" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571023> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.682072e+01 5.509906e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 G03" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571024> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.681869e+01 5.51099e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 G02" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571025> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.681603e+01 5.512121e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 G01" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571026> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.684783e+01 5.506684e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 F06" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571027> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.684575e+01 5.507773e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 F05" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571028> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.684345e+01 5.508889e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 F04" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571029> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.684111e+01 5.510004e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 F03" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571030> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.683836e+01 5.511103e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 F02" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571031> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.68365e+01 5.512231e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 F01" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571032> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.686798e+01 5.506797e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 E06" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571033> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.686587e+01 5.507891e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 E05" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571034> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.686363e+01 5.509011e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 E04" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571035> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.685869e+01 5.511234e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 E02" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571036> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.6856e+01 5.512346e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 E01" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571037> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.689104e+01 5.505779e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 D07" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571038> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.688808e+01 5.50688e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 D06" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571039> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.688626e+01 5.507997e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 D05" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571040> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.688153e+01 5.510228e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 D03" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571041> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.687895e+01 5.511362e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 D02" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571042> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.687668e+01 5.512452e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 D01" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571043> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.691368e+01 5.504767e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 C08" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571044> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.691121e+01 5.505851e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 C07" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571045> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.690873e+01 5.507015e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 C06" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571046> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.690412e+01 5.509222e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 C04" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571047> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.689871e+01 5.511362e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 C02" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571048> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.689714e+01 5.512559e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 C01" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571049> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.693639e+01 5.503735e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 B09" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571050> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.693361e+01 5.504874e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 B08" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571051> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.69316e+01 5.505984e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 B07" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571052> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.692912e+01 5.507094e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 B06" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571053> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.692701e+01 5.508208e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 B05" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571054> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.692447e+01 5.509334e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 B04" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571055> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.69224e+01 5.510413e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 B03" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571056> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.691954e+01 5.511559e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 B02" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571057> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.691725e+01 5.512673e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 B01" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571058> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.695657e+01 5.503868e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 A09" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571059> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.695422e+01 5.50498e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 A08" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571060> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.695173e+01 5.506098e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 A07" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571061> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.694915e+01 5.507234e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 A06" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571062> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.694712e+01 5.508304e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 A05" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571063> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.694459e+01 5.509417e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 A04" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571064> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.694217e+01 5.510557e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 A03" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571065> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.694029e+01 5.511681e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 A02" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191571066> a geojson:Feature ;
    dcterms:modified "2026-09-18T12:35:13+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.693714e+01 5.512781e+01 ) ] ;
    owf:conditionOfFacility inspire-cofv:underConstruction ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-236 DD" ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21409513> ;
    owf:rotorDiameter 236.0 ;
    owf:turbineReference "BK2 A01" ;
    owf:windfarmName "MFW Bałtyk II Offshore Wind Farm" .

<https://www.openstreetmap.org/node/14191911456> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.705676e+01 5.505042e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "G16" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911457> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.716228e+01 5.507434e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "F24" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911458> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.705515e+01 5.505911e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "F16" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911459> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.699413e+01 5.504852e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "F12" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911460> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.708136e+01 5.508485e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "F04" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911461> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.720759e+01 5.508408e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "F03" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911462> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.714581e+01 5.50777e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "E24" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911463> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.717915e+01 5.504845e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "E23" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911464> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.726865e+01 5.509771e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "E21" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911465> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.720592e+01 5.509244e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "E19" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911466> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.697586e+01 5.506017e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "E17" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911467> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.702308e+01 5.506088e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "E16" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911468> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.700884e+01 5.505364e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "E12" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911469> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.697936e+01 5.504307e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "E11" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911470> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.708699e+01 5.502731e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "E08" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911471> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.704343e+01 5.511174e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "E06" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911472> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.706485e+01 5.508823e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "E05" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911473> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.713015e+01 5.507724e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "E04" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911474> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.719098e+01 5.508831e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "E03" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911475> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.710555e+01 5.510715e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "E01" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911476> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.714781e+01 5.506772e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D24" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911477> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.714991e+01 5.505728e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D23" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911478> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.726886e+01 5.508929e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D21" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911479> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.724511e+01 5.51018e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D20" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911480> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.723017e+01 5.509884e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D19" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911481> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.697318e+01 5.507473e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D18" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911482> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.697761e+01 5.505161e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D17" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911483> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.703697e+01 5.507025e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D16" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911484> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.710478e+01 5.507016e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D15" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911485> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.699636e+01 5.511284e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D14" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911486> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.696483e+01 5.511279e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D13" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911487> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.698107e+01 5.503456e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D11" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911488> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.702511e+01 5.50233e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D10" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911489> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.707141e+01 5.501194e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D09" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911490> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.709376e+01 5.504418e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D08" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911491> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.706945e+01 5.506554e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D07" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911492> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.705896e+01 5.511084e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D06" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911493> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.706266e+01 5.509905e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D05" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911494> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.70977e+01 5.508177e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D04" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911495> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.72146e+01 5.509997e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D02" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911496> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.712107e+01 5.510639e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "D01" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911497> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.716454e+01 5.506287e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C24" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911498> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.716461e+01 5.505315e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C23" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911499> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.719478e+01 5.504513e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C22" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191911500> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.72586e+01 5.508246e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C21" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968201> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.726001e+01 5.510446e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C20" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968202> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.7222e+01 5.509048e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C19" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968203> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.696943e+01 5.509297e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C18" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968204> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.699238e+01 5.50571e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C17" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968205> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.70403e+01 5.50539e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C16" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968206> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.709799e+01 5.506137e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C15" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968207> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.696725e+01 5.51036e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C13" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968208> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.699589e+01 5.503992e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C12" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968209> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.699577e+01 5.503076e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C11" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968210> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.705538e+01 5.501558e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C10" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968211> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.708337e+01 5.501866e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C09" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968212> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.709034e+01 5.503558e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C08" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968213> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.707118e+01 5.505702e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C07" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968214> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.707457e+01 5.510974e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C06" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968215> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.707807e+01 5.510079e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C05" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968216> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.713341e+01 5.506146e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C04" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968217> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.719319e+01 5.5077e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C03" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968218> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.719918e+01 5.510106e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C02" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968219> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.715232e+01 5.510425e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "C01" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968220> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.717897e+01 5.506972e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B24" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968221> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.718146e+01 5.505705e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B23" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968222> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.720848e+01 5.504966e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B22" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968223> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.724846e+01 5.50757e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B21" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968224> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.725315e+01 5.509213e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B20" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968225> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.722412e+01 5.50802e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B19" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968226> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.697121e+01 5.508431e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B18" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968227> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.700692e+01 5.506332e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B17" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968228> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.705326e+01 5.506769e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B16" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968229> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.708362e+01 5.507323e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B15" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968230> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.69839e+01 5.50985e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B13" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968231> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.701242e+01 5.503638e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B12" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968232> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.701071e+01 5.502696e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B11" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968233> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.704016e+01 5.501946e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B10" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968234> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.706219e+01 5.502291e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B09" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968235> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.707505e+01 5.503843e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B08" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968236> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.709481e+01 5.505316e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B07" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968237> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.709013e+01 5.510825e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B06" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968238> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.709417e+01 5.509921e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B05" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968239> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.712445e+01 5.506864e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B04" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968240> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.71766e+01 5.508135e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B03" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968241> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.718342e+01 5.510215e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "B02" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968242> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.719546e+01 5.506597e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A24" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968243> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.719729e+01 5.505604e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A23" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968244> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.721923e+01 5.50562e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A22" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968245> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.723807e+01 5.506882e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A21" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968246> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.723868e+01 5.508617e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A20" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968247> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.720974e+01 5.507345e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A19" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968248> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.698806e+01 5.50775e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A18" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968249> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.703494e+01 5.508042e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A17" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968250> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.70512e+01 5.507782e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A16" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968251> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.704649e+01 5.510128e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A14" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968252> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.700159e+01 5.508883e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A13" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968253> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.702713e+01 5.504135e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A12" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968254> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.702888e+01 5.503258e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A11" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968255> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.704547e+01 5.502911e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A10" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968256> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.706063e+01 5.503135e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A09" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968257> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.705909e+01 5.503974e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A08" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968258> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.711011e+01 5.509818e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A06" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968259> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.70959e+01 5.509067e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A05" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968260> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.715982e+01 5.508568e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A03" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968261> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.716785e+01 5.510319e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A02" ;
    owf:windfarmName "Baltica 2" .

<https://www.openstreetmap.org/node/14191968262> a geojson:Feature ;
    dcterms:modified "2026-09-27T23:02:59+00:00"^^xsd:dateTime ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.712655e+01 5.50952e+01 ) ] ;
    owf:manufacturerName "Siemens Gamesa" ;
    owf:modelName "SG 14-222 DD" ;
    owf:operatorName "Orsted",
        "PGE" ;
    owf:partOfWindfarm <https://www.openstreetmap.org/relation/21410256> ;
    owf:ratedPowerMW 14.0 ;
    owf:rotorAxis owf:HorizontalAxis ;
    owf:rotorDiameter 222.0 ;
    owf:turbineReference "A01" ;
    owf:windfarmName "Baltica 2" .

[] a geojson:FeatureCollection ;
    geojson:features <https://www.openstreetmap.org/node/14185128565>,
        <https://www.openstreetmap.org/node/14185128566>,
        <https://www.openstreetmap.org/node/14185128567>,
        <https://www.openstreetmap.org/node/14185128568>,
        <https://www.openstreetmap.org/node/14185128569>,
        <https://www.openstreetmap.org/node/14185128570>,
        <https://www.openstreetmap.org/node/14185128571>,
        <https://www.openstreetmap.org/node/14185128572>,
        <https://www.openstreetmap.org/node/14185128573>,
        <https://www.openstreetmap.org/node/14185128574>,
        <https://www.openstreetmap.org/node/14185128575>,
        <https://www.openstreetmap.org/node/14185128576>,
        <https://www.openstreetmap.org/node/14185128577>,
        <https://www.openstreetmap.org/node/14185128578>,
        <https://www.openstreetmap.org/node/14185128579>,
        <https://www.openstreetmap.org/node/14185128580>,
        <https://www.openstreetmap.org/node/14185128581>,
        <https://www.openstreetmap.org/node/14185128582>,
        <https://www.openstreetmap.org/node/14185128583>,
        <https://www.openstreetmap.org/node/14185128584>,
        <https://www.openstreetmap.org/node/14185128585>,
        <https://www.openstreetmap.org/node/14185128586>,
        <https://www.openstreetmap.org/node/14185128587>,
        <https://www.openstreetmap.org/node/14185128588>,
        <https://www.openstreetmap.org/node/14185128589>,
        <https://www.openstreetmap.org/node/14185128590>,
        <https://www.openstreetmap.org/node/14185128591>,
        <https://www.openstreetmap.org/node/14185128592>,
        <https://www.openstreetmap.org/node/14185128593>,
        <https://www.openstreetmap.org/node/14185128594>,
        <https://www.openstreetmap.org/node/14185128595>,
        <https://www.openstreetmap.org/node/14185128596>,
        <https://www.openstreetmap.org/node/14185128597>,
        <https://www.openstreetmap.org/node/14185128598>,
        <https://www.openstreetmap.org/node/14185128599>,
        <https://www.openstreetmap.org/node/14185128600>,
        <https://www.openstreetmap.org/node/14185129401>,
        <https://www.openstreetmap.org/node/14185129402>,
        <https://www.openstreetmap.org/node/14185129403>,
        <https://www.openstreetmap.org/node/14185129404>,
        <https://www.openstreetmap.org/node/14185129405>,
        <https://www.openstreetmap.org/node/14185129406>,
        <https://www.openstreetmap.org/node/14185129407>,
        <https://www.openstreetmap.org/node/14185129408>,
        <https://www.openstreetmap.org/node/14185129409>,
        <https://www.openstreetmap.org/node/14185129410>,
        <https://www.openstreetmap.org/node/14185129411>,
        <https://www.openstreetmap.org/node/14185129412>,
        <https://www.openstreetmap.org/node/14185129413>,
        <https://www.openstreetmap.org/node/14185129414>,
        <https://www.openstreetmap.org/node/14185129415>,
        <https://www.openstreetmap.org/node/14185129416>,
        <https://www.openstreetmap.org/node/14185129417>,
        <https://www.openstreetmap.org/node/14185129418>,
        <https://www.openstreetmap.org/node/14185129419>,
        <https://www.openstreetmap.org/node/14185129420>,
        <https://www.openstreetmap.org/node/14185129421>,
        <https://www.openstreetmap.org/node/14185129422>,
        <https://www.openstreetmap.org/node/14185129423>,
        <https://www.openstreetmap.org/node/14185129424>,
        <https://www.openstreetmap.org/node/14185129425>,
        <https://www.openstreetmap.org/node/14185129426>,
        <https://www.openstreetmap.org/node/14185129427>,
        <https://www.openstreetmap.org/node/14185129428>,
        <https://www.openstreetmap.org/node/14185129429>,
        <https://www.openstreetmap.org/node/14185129430>,
        <https://www.openstreetmap.org/node/14185129431>,
        <https://www.openstreetmap.org/node/14185129432>,
        <https://www.openstreetmap.org/node/14185129433>,
        <https://www.openstreetmap.org/node/14185129434>,
        <https://www.openstreetmap.org/node/14185129435>,
        <https://www.openstreetmap.org/node/14185129436>,
        <https://www.openstreetmap.org/node/14185129437>,
        <https://www.openstreetmap.org/node/14185129438>,
        <https://www.openstreetmap.org/node/14185129439>,
        <https://www.openstreetmap.org/node/14185129440>,
        <https://www.openstreetmap.org/node/14191537540>,
        <https://www.openstreetmap.org/node/14191537541>,
        <https://www.openstreetmap.org/node/14191537542>,
        <https://www.openstreetmap.org/node/14191537543>,
        <https://www.openstreetmap.org/node/14191537544>,
        <https://www.openstreetmap.org/node/14191537545>,
        <https://www.openstreetmap.org/node/14191537546>,
        <https://www.openstreetmap.org/node/14191537547>,
        <https://www.openstreetmap.org/node/14191537548>,
        <https://www.openstreetmap.org/node/14191537549>,
        <https://www.openstreetmap.org/node/14191537550>,
        <https://www.openstreetmap.org/node/14191537551>,
        <https://www.openstreetmap.org/node/14191537552>,
        <https://www.openstreetmap.org/node/14191537553>,
        <https://www.openstreetmap.org/node/14191537554>,
        <https://www.openstreetmap.org/node/14191537555>,
        <https://www.openstreetmap.org/node/14191537556>,
        <https://www.openstreetmap.org/node/14191537557>,
        <https://www.openstreetmap.org/node/14191537558>,
        <https://www.openstreetmap.org/node/14191537559>,
        <https://www.openstreetmap.org/node/14191537560>,
        <https://www.openstreetmap.org/node/14191537561>,
        <https://www.openstreetmap.org/node/14191537562>,
        <https://www.openstreetmap.org/node/14191537563>,
        <https://www.openstreetmap.org/node/14191537564>,
        <https://www.openstreetmap.org/node/14191537565>,
        <https://www.openstreetmap.org/node/14191537566>,
        <https://www.openstreetmap.org/node/14191537567>,
        <https://www.openstreetmap.org/node/14191537568>,
        <https://www.openstreetmap.org/node/14191537569>,
        <https://www.openstreetmap.org/node/14191537570>,
        <https://www.openstreetmap.org/node/14191537571>,
        <https://www.openstreetmap.org/node/14191537572>,
        <https://www.openstreetmap.org/node/14191537573>,
        <https://www.openstreetmap.org/node/14191537574>,
        <https://www.openstreetmap.org/node/14191537575>,
        <https://www.openstreetmap.org/node/14191537576>,
        <https://www.openstreetmap.org/node/14191537577>,
        <https://www.openstreetmap.org/node/14191537578>,
        <https://www.openstreetmap.org/node/14191537579>,
        <https://www.openstreetmap.org/node/14191537580>,
        <https://www.openstreetmap.org/node/14191537581>,
        <https://www.openstreetmap.org/node/14191537582>,
        <https://www.openstreetmap.org/node/14191537583>,
        <https://www.openstreetmap.org/node/14191537584>,
        <https://www.openstreetmap.org/node/14191537585>,
        <https://www.openstreetmap.org/node/14191537586>,
        <https://www.openstreetmap.org/node/14191537587>,
        <https://www.openstreetmap.org/node/14191537588>,
        <https://www.openstreetmap.org/node/14191537589>,
        <https://www.openstreetmap.org/node/14191571017>,
        <https://www.openstreetmap.org/node/14191571018>,
        <https://www.openstreetmap.org/node/14191571019>,
        <https://www.openstreetmap.org/node/14191571020>,
        <https://www.openstreetmap.org/node/14191571021>,
        <https://www.openstreetmap.org/node/14191571022>,
        <https://www.openstreetmap.org/node/14191571023>,
        <https://www.openstreetmap.org/node/14191571024>,
        <https://www.openstreetmap.org/node/14191571025>,
        <https://www.openstreetmap.org/node/14191571026>,
        <https://www.openstreetmap.org/node/14191571027>,
        <https://www.openstreetmap.org/node/14191571028>,
        <https://www.openstreetmap.org/node/14191571029>,
        <https://www.openstreetmap.org/node/14191571030>,
        <https://www.openstreetmap.org/node/14191571031>,
        <https://www.openstreetmap.org/node/14191571032>,
        <https://www.openstreetmap.org/node/14191571033>,
        <https://www.openstreetmap.org/node/14191571034>,
        <https://www.openstreetmap.org/node/14191571035>,
        <https://www.openstreetmap.org/node/14191571036>,
        <https://www.openstreetmap.org/node/14191571037>,
        <https://www.openstreetmap.org/node/14191571038>,
        <https://www.openstreetmap.org/node/14191571039>,
        <https://www.openstreetmap.org/node/14191571040>,
        <https://www.openstreetmap.org/node/14191571041>,
        <https://www.openstreetmap.org/node/14191571042>,
        <https://www.openstreetmap.org/node/14191571043>,
        <https://www.openstreetmap.org/node/14191571044>,
        <https://www.openstreetmap.org/node/14191571045>,
        <https://www.openstreetmap.org/node/14191571046>,
        <https://www.openstreetmap.org/node/14191571047>,
        <https://www.openstreetmap.org/node/14191571048>,
        <https://www.openstreetmap.org/node/14191571049>,
        <https://www.openstreetmap.org/node/14191571050>,
        <https://www.openstreetmap.org/node/14191571051>,
        <https://www.openstreetmap.org/node/14191571052>,
        <https://www.openstreetmap.org/node/14191571053>,
        <https://www.openstreetmap.org/node/14191571054>,
        <https://www.openstreetmap.org/node/14191571055>,
        <https://www.openstreetmap.org/node/14191571056>,
        <https://www.openstreetmap.org/node/14191571057>,
        <https://www.openstreetmap.org/node/14191571058>,
        <https://www.openstreetmap.org/node/14191571059>,
        <https://www.openstreetmap.org/node/14191571060>,
        <https://www.openstreetmap.org/node/14191571061>,
        <https://www.openstreetmap.org/node/14191571062>,
        <https://www.openstreetmap.org/node/14191571063>,
        <https://www.openstreetmap.org/node/14191571064>,
        <https://www.openstreetmap.org/node/14191571065>,
        <https://www.openstreetmap.org/node/14191571066>,
        <https://www.openstreetmap.org/node/14191911456>,
        <https://www.openstreetmap.org/node/14191911457>,
        <https://www.openstreetmap.org/node/14191911458>,
        <https://www.openstreetmap.org/node/14191911459>,
        <https://www.openstreetmap.org/node/14191911460>,
        <https://www.openstreetmap.org/node/14191911461>,
        <https://www.openstreetmap.org/node/14191911462>,
        <https://www.openstreetmap.org/node/14191911463>,
        <https://www.openstreetmap.org/node/14191911464>,
        <https://www.openstreetmap.org/node/14191911465>,
        <https://www.openstreetmap.org/node/14191911466>,
        <https://www.openstreetmap.org/node/14191911467>,
        <https://www.openstreetmap.org/node/14191911468>,
        <https://www.openstreetmap.org/node/14191911469>,
        <https://www.openstreetmap.org/node/14191911470>,
        <https://www.openstreetmap.org/node/14191911471>,
        <https://www.openstreetmap.org/node/14191911472>,
        <https://www.openstreetmap.org/node/14191911473>,
        <https://www.openstreetmap.org/node/14191911474>,
        <https://www.openstreetmap.org/node/14191911475>,
        <https://www.openstreetmap.org/node/14191911476>,
        <https://www.openstreetmap.org/node/14191911477>,
        <https://www.openstreetmap.org/node/14191911478>,
        <https://www.openstreetmap.org/node/14191911479>,
        <https://www.openstreetmap.org/node/14191911480>,
        <https://www.openstreetmap.org/node/14191911481>,
        <https://www.openstreetmap.org/node/14191911482>,
        <https://www.openstreetmap.org/node/14191911483>,
        <https://www.openstreetmap.org/node/14191911484>,
        <https://www.openstreetmap.org/node/14191911485>,
        <https://www.openstreetmap.org/node/14191911486>,
        <https://www.openstreetmap.org/node/14191911487>,
        <https://www.openstreetmap.org/node/14191911488>,
        <https://www.openstreetmap.org/node/14191911489>,
        <https://www.openstreetmap.org/node/14191911490>,
        <https://www.openstreetmap.org/node/14191911491>,
        <https://www.openstreetmap.org/node/14191911492>,
        <https://www.openstreetmap.org/node/14191911493>,
        <https://www.openstreetmap.org/node/14191911494>,
        <https://www.openstreetmap.org/node/14191911495>,
        <https://www.openstreetmap.org/node/14191911496>,
        <https://www.openstreetmap.org/node/14191911497>,
        <https://www.openstreetmap.org/node/14191911498>,
        <https://www.openstreetmap.org/node/14191911499>,
        <https://www.openstreetmap.org/node/14191911500>,
        <https://www.openstreetmap.org/node/14191968201>,
        <https://www.openstreetmap.org/node/14191968202>,
        <https://www.openstreetmap.org/node/14191968203>,
        <https://www.openstreetmap.org/node/14191968204>,
        <https://www.openstreetmap.org/node/14191968205>,
        <https://www.openstreetmap.org/node/14191968206>,
        <https://www.openstreetmap.org/node/14191968207>,
        <https://www.openstreetmap.org/node/14191968208>,
        <https://www.openstreetmap.org/node/14191968209>,
        <https://www.openstreetmap.org/node/14191968210>,
        <https://www.openstreetmap.org/node/14191968211>,
        <https://www.openstreetmap.org/node/14191968212>,
        <https://www.openstreetmap.org/node/14191968213>,
        <https://www.openstreetmap.org/node/14191968214>,
        <https://www.openstreetmap.org/node/14191968215>,
        <https://www.openstreetmap.org/node/14191968216>,
        <https://www.openstreetmap.org/node/14191968217>,
        <https://www.openstreetmap.org/node/14191968218>,
        <https://www.openstreetmap.org/node/14191968219>,
        <https://www.openstreetmap.org/node/14191968220>,
        <https://www.openstreetmap.org/node/14191968221>,
        <https://www.openstreetmap.org/node/14191968222>,
        <https://www.openstreetmap.org/node/14191968223>,
        <https://www.openstreetmap.org/node/14191968224>,
        <https://www.openstreetmap.org/node/14191968225>,
        <https://www.openstreetmap.org/node/14191968226>,
        <https://www.openstreetmap.org/node/14191968227>,
        <https://www.openstreetmap.org/node/14191968228>,
        <https://www.openstreetmap.org/node/14191968229>,
        <https://www.openstreetmap.org/node/14191968230>,
        <https://www.openstreetmap.org/node/14191968231>,
        <https://www.openstreetmap.org/node/14191968232>,
        <https://www.openstreetmap.org/node/14191968233>,
        <https://www.openstreetmap.org/node/14191968234>,
        <https://www.openstreetmap.org/node/14191968235>,
        <https://www.openstreetmap.org/node/14191968236>,
        <https://www.openstreetmap.org/node/14191968237>,
        <https://www.openstreetmap.org/node/14191968238>,
        <https://www.openstreetmap.org/node/14191968239>,
        <https://www.openstreetmap.org/node/14191968240>,
        <https://www.openstreetmap.org/node/14191968241>,
        <https://www.openstreetmap.org/node/14191968242>,
        <https://www.openstreetmap.org/node/14191968243>,
        <https://www.openstreetmap.org/node/14191968244>,
        <https://www.openstreetmap.org/node/14191968245>,
        <https://www.openstreetmap.org/node/14191968246>,
        <https://www.openstreetmap.org/node/14191968247>,
        <https://www.openstreetmap.org/node/14191968248>,
        <https://www.openstreetmap.org/node/14191968249>,
        <https://www.openstreetmap.org/node/14191968250>,
        <https://www.openstreetmap.org/node/14191968251>,
        <https://www.openstreetmap.org/node/14191968252>,
        <https://www.openstreetmap.org/node/14191968253>,
        <https://www.openstreetmap.org/node/14191968254>,
        <https://www.openstreetmap.org/node/14191968255>,
        <https://www.openstreetmap.org/node/14191968256>,
        <https://www.openstreetmap.org/node/14191968257>,
        <https://www.openstreetmap.org/node/14191968258>,
        <https://www.openstreetmap.org/node/14191968259>,
        <https://www.openstreetmap.org/node/14191968260>,
        <https://www.openstreetmap.org/node/14191968261>,
        <https://www.openstreetmap.org/node/14191968262> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Wind turbine
description: 'A single wind turbine as a GeoJSON Feature with Point geometry, or a
  FeatureCollection of such turbines. Properties are harmonised from source tags:
  numeric values are parsed into SI-based units named in the property, and values
  that cannot be read unambiguously are null.

  '
anyOf:
- $ref: '#/$defs/WindTurbine'
- $ref: '#/$defs/WindTurbineCollection'
$defs:
  WindTurbineCollection:
    allOf:
    - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/schema.yaml
    - type: object
      required:
      - features
      properties:
        features:
          type: array
          items:
            $ref: '#/$defs/WindTurbine'
          x-jsonld-id: https://purl.org/geojson/vocab#features
          x-jsonld-container: '@set'
  WindTurbine:
    allOf:
    - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.yaml
    - type: object
      required:
      - id
      - geometry
      - properties
      properties:
        id:
          type: string
          format: uri
          description: Persistent identifier of the turbine, e.g. its OpenStreetMap
            node URL.
          x-jsonld-id: '@id'
        geometry:
          type: object
          required:
          - type
          - coordinates
          properties:
            type:
              const: Point
              x-jsonld-id: '@type'
          x-jsonld-id: https://purl.org/geojson/vocab#geometry
        properties:
          type: object
          properties:
            ref:
              type:
              - string
              - 'null'
              description: Turbine reference label within its wind farm, as assigned
                by the source.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#turbineReference
            windfarm_name:
              type:
              - string
              - 'null'
              description: Name of the wind farm the turbine belongs to.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#windfarmName
            windfarm:
              type:
              - string
              - 'null'
              format: uri
              description: Identifier of the wind farm the turbine belongs to, e.g.
                its OpenStreetMap relation URL.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#partOfWindfarm
              x-jsonld-type: '@id'
            manufacturer:
              type:
              - string
              - 'null'
              description: Turbine manufacturer name.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#manufacturerName
            model:
              type:
              - string
              - 'null'
              description: Turbine model designation.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#modelName
            rated_power_mw:
              type:
              - number
              - 'null'
              minimum: 0
              description: Rated (nameplate) electrical output of the turbine in megawatts.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#ratedPowerMW
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
            hub_height_m:
              type:
              - number
              - 'null'
              minimum: 0
              description: Height of the rotor hub in metres.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#hubHeight
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
            rotor_diameter_m:
              type:
              - number
              - 'null'
              minimum: 0
              description: Rotor diameter in metres.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#rotorDiameter
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
            rotor_axis:
              enum:
              - horizontal_axis
              - vertical_axis
              - null
              description: Orientation of the rotor axis.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#rotorAxis
              x-jsonld-type: '@vocab'
            offshore:
              type:
              - boolean
              - 'null'
              description: Whether the turbine stands offshore; null when the source
                does not say.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#offshore
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
            operator:
              type:
              - array
              - 'null'
              minItems: 1
              items:
                type: string
              description: Operating organisation(s).
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#operatorName
              x-jsonld-container: '@set'
            status:
              enum:
              - projected
              - underConstruction
              - functional
              - disused
              - decommissioned
              - null
              description: Condition of the turbine as an INSPIRE ConditionOfFacilityValue
                code; null when the source does not state it.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#conditionOfFacility
              x-jsonld-type: '@vocab'
            last_updated:
              type:
              - string
              - 'null'
              format: date-time
              description: Time of the last edit of the source record.
              x-jsonld-id: http://purl.org/dc/terms/modified
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
            commissioning_year:
              type:
              - integer
              - 'null'
              minimum: 1900
              maximum: 2100
              description: Year the turbine was commissioned; null when the source
                does not state it.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#commissioningYear
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#gYear
          x-jsonld-id: '@nest'
x-jsonld-extra-terms:
  FeatureCollection: https://purl.org/geojson/vocab#FeatureCollection
  Feature: https://purl.org/geojson/vocab#Feature
  Point: https://purl.org/geojson/vocab#Point
  coordinates:
    x-jsonld-id: https://purl.org/geojson/vocab#coordinates
    x-jsonld-container: '@list'
  WindTurbine: https://w3id.org/ogc/hosted/seadots/windfarm#WindTurbine
  horizontal_axis: https://w3id.org/ogc/hosted/seadots/windfarm#HorizontalAxis
  vertical_axis: https://w3id.org/ogc/hosted/seadots/windfarm#VerticalAxis
  projected: http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/projected
  underConstruction: http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/underConstruction
  functional: http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/functional
  disused: http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/disused
  decommissioned: http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/decommissioned
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  owf: https://w3id.org/ogc/hosted/seadots/windfarm#
  xsd: http://www.w3.org/2001/XMLSchema#
  inspire-cofv: http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/
  dcterms: http://purl.org/dc/terms/
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.windfarms.common-windfarm-turbine
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.2'
  dateOfLastChange: '2026-11-04'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/common-windfarm-turbine/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/common-windfarm-turbine/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "features": {
      "@container": "@set",
      "@id": "geojson:features"
    },
    "type": "@type",
    "id": "@id",
    "properties": "@nest",
    "geometry": "geojson:geometry",
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "links": {
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "ref": "owf:turbineReference",
    "windfarm_name": "owf:windfarmName",
    "windfarm": {
      "@id": "owf:partOfWindfarm",
      "@type": "@id"
    },
    "manufacturer": "owf:manufacturerName",
    "model": "owf:modelName",
    "rated_power_mw": {
      "@id": "owf:ratedPowerMW",
      "@type": "xsd:decimal"
    },
    "hub_height_m": {
      "@id": "owf:hubHeight",
      "@type": "xsd:decimal"
    },
    "rotor_diameter_m": {
      "@id": "owf:rotorDiameter",
      "@type": "xsd:decimal"
    },
    "rotor_axis": {
      "@id": "owf:rotorAxis",
      "@type": "@vocab"
    },
    "offshore": {
      "@id": "owf:offshore",
      "@type": "xsd:boolean"
    },
    "operator": {
      "@id": "owf:operatorName",
      "@container": "@set"
    },
    "status": {
      "@id": "owf:conditionOfFacility",
      "@type": "@vocab"
    },
    "last_updated": {
      "@id": "dct:modified",
      "@type": "xsd:dateTime"
    },
    "commissioning_year": {
      "@id": "owf:commissioningYear",
      "@type": "xsd:gYear"
    },
    "coordinates": {
      "@id": "geojson:coordinates",
      "@container": "@list"
    },
    "WindTurbine": "owf:WindTurbine",
    "horizontal_axis": "owf:HorizontalAxis",
    "vertical_axis": "owf:VerticalAxis",
    "projected": "inspire-cofv:projected",
    "underConstruction": "inspire-cofv:underConstruction",
    "functional": "inspire-cofv:functional",
    "disused": "inspire-cofv:disused",
    "decommissioned": "inspire-cofv:decommissioned",
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "owf": "https://w3id.org/ogc/hosted/seadots/windfarm#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "inspire-cofv": "http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/",
    "dcterms": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/common-windfarm-turbine/context.jsonld)

## Sources

* [IHO wind turbine definition in S-100](https://registry.iho.int/fdd/view5.do?idx=341&type=5&valueType=0)
* [OpenStreetMap wind turbine tagging (generator:source=wind)](https://wiki.openstreetmap.org/wiki/Tag:generator:source%3Dwind)
* [INSPIRE ConditionOfFacilityValue code list](http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/windfarms/common-windfarm-turbine`

