
# Windfarm designated area (Schema)

`ogc.hosted.seadots.windfarms.common-windfarm-designated-area` *v0.2*

GeoJSON representation of a wind farm as a designated area or project, without individual devices such as turbines. A single Feature or a FeatureCollection, with EMODnet windfarm attributes extended by the windpark parameters found in OpenStreetMap, the Norwegian NVE register, and the Polish national pipeline, plus source and location provenance.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### Single wind farm area (Baltic Power, OpenStreetMap)
The Baltic Power wind farm area converted from [OSM relation 21402440](https://www.openstreetmap.org/relation/21402440) and its outer way. `same_as` links the outer way and the matching EMODnet record. © [OpenStreetMap contributors](https://www.openstreetmap.org/copyright), [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/).

#### json
```json
{
  "type": "Feature",
  "id": "https://www.openstreetmap.org/relation/21402440",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          17.5641164,
          54.9776003
        ],
        [
          17.6514242,
          54.9950473
        ],
        [
          17.718161,
          55.0049784
        ],
        [
          17.7161404,
          55.0852456
        ],
        [
          17.7686688,
          55.0834771
        ],
        [
          17.7804527,
          55.1113339
        ],
        [
          17.6206968,
          55.1113719
        ],
        [
          17.5882777,
          55.0748161
        ],
        [
          17.5641164,
          54.9776003
        ]
      ]
    ]
  },
  "properties": {
    "name": "Baltic Power",
    "country": null,
    "n_turbines": 76,
    "power_mw": 1200.0,
    "status": "Production",
    "status_detail": null,
    "status_as_of": null,
    "type_inst": null,
    "offshore": true,
    "year": null,
    "year_semantics": null,
    "year_is_assumed": null,
    "updateyear": null,
    "operational_date": null,
    "dist_coast": null,
    "area_sqkm": 122.01,
    "operator": [
      "Baltic Power"
    ],
    "owner": null,
    "developer": null,
    "licence_status": null,
    "licensing_case": null,
    "admin_units": null,
    "electricity_price_area": null,
    "mean_annual_production_gwh": null,
    "notes": null,
    "source_type": "osm",
    "source_dataset": "OpenStreetMap",
    "source_reference": "https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824",
    "source_record_id": "relation/21402440",
    "source_snapshot_date": "2026-10-27",
    "last_updated": "2026-09-18T16:06:52Z",
    "location_status": "source-provided",
    "location_method": "outer way 1532855580 of the OSM element",
    "location_reference": null,
    "same_as": [
      "https://www.openstreetmap.org/way/1532855580",
      "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.268"
    ]
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/common-windfarm-designated-area/context.jsonld",
  "type": "Feature",
  "id": "https://www.openstreetmap.org/relation/21402440",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          17.5641164,
          54.9776003
        ],
        [
          17.6514242,
          54.9950473
        ],
        [
          17.718161,
          55.0049784
        ],
        [
          17.7161404,
          55.0852456
        ],
        [
          17.7686688,
          55.0834771
        ],
        [
          17.7804527,
          55.1113339
        ],
        [
          17.6206968,
          55.1113719
        ],
        [
          17.5882777,
          55.0748161
        ],
        [
          17.5641164,
          54.9776003
        ]
      ]
    ]
  },
  "properties": {
    "name": "Baltic Power",
    "country": null,
    "n_turbines": 76,
    "power_mw": 1200.0,
    "status": "Production",
    "status_detail": null,
    "status_as_of": null,
    "type_inst": null,
    "offshore": true,
    "year": null,
    "year_semantics": null,
    "year_is_assumed": null,
    "updateyear": null,
    "operational_date": null,
    "dist_coast": null,
    "area_sqkm": 122.01,
    "operator": [
      "Baltic Power"
    ],
    "owner": null,
    "developer": null,
    "licence_status": null,
    "licensing_case": null,
    "admin_units": null,
    "electricity_price_area": null,
    "mean_annual_production_gwh": null,
    "notes": null,
    "source_type": "osm",
    "source_dataset": "OpenStreetMap",
    "source_reference": "https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824",
    "source_record_id": "relation/21402440",
    "source_snapshot_date": "2026-10-27",
    "last_updated": "2026-09-18T16:06:52Z",
    "location_status": "source-provided",
    "location_method": "outer way 1532855580 of the OSM element",
    "location_reference": null,
    "same_as": [
      "https://www.openstreetmap.org/way/1532855580",
      "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.268"
    ]
  }
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/ogc/hosted/seadots/emodnet/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix owf: <https://w3id.org/ogc/hosted/seadots/windfarm#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://www.openstreetmap.org/relation/21402440> a geojson:Feature ;
    dcterms:identifier "relation/21402440" ;
    dcterms:modified "2026-09-18T16:06:52+00:00"^^xsd:dateTime ;
    dcterms:source <https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824> ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.756412e+01 5.49776e+01 ) ( 1.765142e+01 5.499505e+01 ) ( 1.771816e+01 5.500498e+01 ) ( 1.771614e+01 5.508525e+01 ) ( 1.776867e+01 5.508348e+01 ) ( 1.778045e+01 5.511133e+01 ) ( 1.76207e+01 5.511137e+01 ) ( 1.758828e+01 5.507482e+01 ) ( 1.756412e+01 5.49776e+01 ) ) ) ] ;
    schema:name "Baltic Power" ;
    schema:sameAs <https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.268>,
        <https://www.openstreetmap.org/way/1532855580> ;
    owf:areaSqKm 122.01 ;
    owf:conditionOfFacility :Production ;
    owf:locationMethod "outer way 1532855580 of the OSM element" ;
    owf:locationStatus owf:LocationSourceProvided ;
    owf:nTurbines 76 ;
    owf:offshore true ;
    owf:operatorName "Baltic Power" ;
    owf:powerMW 1200.0 ;
    owf:sourceDataset "OpenStreetMap" ;
    owf:sourceSnapshotDate "2026-10-27"^^xsd:date ;
    owf:sourceType owf:OpenStreetMapSource .


```


### Wind farm areas from OSM, EMODnet, NVE and the Polish pipeline
FeatureCollection with one feature per source record: five Polish Baltic wind farms from the 2026-10-27 OpenStreetMap snapshot, the matching five EMODnet Human Activities records (WFS, retrieved 2026-11-04), the NVE Smøla record from [emodnet-compliant-windfarm-no](../emodnet-compliant-windfarm-no/), and the national pipeline record from [emodnet-compliant-windfarm-pl](../emodnet-compliant-windfarm-pl/). Records of the same farm are linked with `same_as`. OSM data © OpenStreetMap contributors (ODbL 1.0).

#### json
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/relation/21402440",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              17.5641164,
              54.9776003
            ],
            [
              17.6514242,
              54.9950473
            ],
            [
              17.718161,
              55.0049784
            ],
            [
              17.7161404,
              55.0852456
            ],
            [
              17.7686688,
              55.0834771
            ],
            [
              17.7804527,
              55.1113339
            ],
            [
              17.6206968,
              55.1113719
            ],
            [
              17.5882777,
              55.0748161
            ],
            [
              17.5641164,
              54.9776003
            ]
          ]
        ]
      },
      "properties": {
        "name": "Baltic Power",
        "country": null,
        "n_turbines": 76,
        "power_mw": 1200.0,
        "status": "Production",
        "status_detail": null,
        "status_as_of": null,
        "type_inst": null,
        "offshore": true,
        "year": null,
        "year_semantics": null,
        "year_is_assumed": null,
        "updateyear": null,
        "operational_date": null,
        "dist_coast": null,
        "area_sqkm": 122.01,
        "operator": [
          "Baltic Power"
        ],
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "osm",
        "source_dataset": "OpenStreetMap",
        "source_reference": "https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824",
        "source_record_id": "relation/21402440",
        "source_snapshot_date": "2026-10-27",
        "last_updated": "2026-09-18T16:06:52Z",
        "location_status": "source-provided",
        "location_method": "outer way 1532855580 of the OSM element",
        "location_reference": null,
        "same_as": [
          "https://www.openstreetmap.org/way/1532855580",
          "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.268"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/relation/21410256",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              17.0488829,
              55.0159008
            ],
            [
              16.9791503,
              55.0336525
            ],
            [
              16.9626103,
              55.1142444
            ],
            [
              17.0305922,
              55.1141769
            ],
            [
              17.0905683,
              55.1096853
            ],
            [
              17.0906639,
              55.1096786
            ],
            [
              17.1600869,
              55.1049367
            ],
            [
              17.1600947,
              55.1049361
            ],
            [
              17.2277706,
              55.1003139
            ],
            [
              17.2278758,
              55.1003069
            ],
            [
              17.2283875,
              55.1002856
            ],
            [
              17.2288992,
              55.1002833
            ],
            [
              17.2294122,
              55.1003006
            ],
            [
              17.2299211,
              55.1003367
            ],
            [
              17.230425,
              55.1003919
            ],
            [
              17.2309211,
              55.1004658
            ],
            [
              17.2310894,
              55.1004956
            ],
            [
              17.26984,
              55.1075956
            ],
            [
              17.2715453,
              55.0892258
            ],
            [
              17.2570575,
              55.0795728
            ],
            [
              17.2439575,
              55.0708386
            ],
            [
              17.2273725,
              55.0597736
            ],
            [
              17.2012272,
              55.0423133
            ],
            [
              17.1864494,
              55.0430644
            ],
            [
              17.1790169,
              55.0454525
            ],
            [
              17.1282531,
              55.0617422
            ],
            [
              17.1201028,
              55.0695211
            ],
            [
              17.1200661,
              55.0695558
            ],
            [
              17.1197839,
              55.0698014
            ],
            [
              17.1194742,
              55.0700356
            ],
            [
              17.1191386,
              55.0702578
            ],
            [
              17.1187783,
              55.0704669
            ],
            [
              17.118395,
              55.0706622
            ],
            [
              17.1179903,
              55.0708425
            ],
            [
              17.1175658,
              55.0710072
            ],
            [
              17.1171236,
              55.0711558
            ],
            [
              17.1166667,
              55.0712872
            ],
            [
              17.1161928,
              55.0714014
            ],
            [
              17.1157086,
              55.0714975
            ],
            [
              17.1152144,
              55.0715753
            ],
            [
              17.1147122,
              55.0716344
            ],
            [
              17.1142047,
              55.0716744
            ],
            [
              17.113819,
              55.0716959
            ],
            [
              17.1126694,
              55.0716794
            ],
            [
              17.1121611,
              55.0716428
            ],
            [
              17.1116578,
              55.0715869
            ],
            [
              17.1106184,
              55.0417445
            ],
            [
              17.1106384,
              55.041711
            ],
            [
              17.1100125,
              55.0416711
            ],
            [
              17.1097406,
              55.0416248
            ],
            [
              17.1092953,
              55.0415724
            ],
            [
              17.1088675,
              55.0415141
            ],
            [
              17.1084592,
              55.0414501
            ],
            [
              17.1080719,
              55.0413808
            ],
            [
              17.1077075,
              55.0413063
            ],
            [
              17.1073675,
              55.0412271
            ],
            [
              17.1070231,
              55.0411435
            ],
            [
              17.1067632,
              55.0410558
            ],
            [
              17.1065073,
              55.0409645
            ],
            [
              17.1061014,
              55.0408698
            ],
            [
              17.1060786,
              55.0407722
            ],
            [
              17.1059124,
              55.0406721
            ],
            [
              17.1057796,
              55.0405701
            ],
            [
              17.1057665,
              55.0405615
            ],
            [
              17.0883056,
              55.0252414
            ],
            [
              17.0822189,
              55.0097236
            ],
            [
              17.0821817,
              55.0087331
            ],
            [
              17.0488829,
              55.0159008
            ]
          ]
        ]
      },
      "properties": {
        "name": "Baltica 2",
        "country": null,
        "n_turbines": 107,
        "power_mw": 1500.0,
        "status": "Construction",
        "status_detail": "construction:power=plant",
        "status_as_of": null,
        "type_inst": null,
        "offshore": null,
        "year": null,
        "year_semantics": null,
        "year_is_assumed": null,
        "updateyear": null,
        "operational_date": null,
        "dist_coast": null,
        "area_sqkm": 139.894,
        "operator": [
          "PGE Baltica",
          "Orsted"
        ],
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "osm",
        "source_dataset": "OpenStreetMap",
        "source_reference": "https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824",
        "source_record_id": "relation/21410256",
        "source_snapshot_date": "2026-10-27",
        "last_updated": "2026-09-18T15:33:23Z",
        "location_status": "source-provided",
        "location_method": "outer way 1560193205 of the OSM element",
        "location_reference": null,
        "same_as": [
          "https://www.openstreetmap.org/way/1560193205",
          "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.270"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/way/1560193204",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              17.3048544,
              55.0423678
            ],
            [
              17.3209678,
              55.0530986
            ],
            [
              17.3392028,
              55.0536478
            ],
            [
              17.3393014,
              55.0536867
            ],
            [
              17.3844589,
              55.0549986
            ],
            [
              17.3847472,
              55.05501
            ],
            [
              17.3852556,
              55.0550456
            ],
            [
              17.3857592,
              55.0551003
            ],
            [
              17.3862553,
              55.0551736
            ],
            [
              17.3867419,
              55.0552656
            ],
            [
              17.3872169,
              55.0553753
            ],
            [
              17.3876786,
              55.0555031
            ],
            [
              17.3881247,
              55.0556475
            ],
            [
              17.3885533,
              55.0558086
            ],
            [
              17.3889628,
              55.0559853
            ],
            [
              17.3893514,
              55.0561769
            ],
            [
              17.3897169,
              55.0563831
            ],
            [
              17.3900586,
              55.0566022
            ],
            [
              17.3903742,
              55.0568336
            ],
            [
              17.3906631,
              55.0570767
            ],
            [
              17.3909233,
              55.0573297
            ],
            [
              17.3911544,
              55.0575922
            ],
            [
              17.391355,
              55.0578628
            ],
            [
              17.3912189,
              55.0581406
            ],
            [
              17.3916619,
              55.0584236
            ],
            [
              17.3917667,
              55.0587117
            ],
            [
              17.3918386,
              55.0590028
            ],
            [
              17.3918769,
              55.0592961
            ],
            [
              17.3918736,
              55.0597178
            ],
            [
              17.3884753,
              55.0975811
            ],
            [
              17.4556206,
              55.0995556
            ],
            [
              17.4556253,
              55.0995583
            ],
            [
              17.552685,
              55.1023775
            ],
            [
              17.5407375,
              55.0652203
            ],
            [
              17.5407331,
              55.0652064
            ],
            [
              17.5344233,
              55.0452031
            ],
            [
              17.5289289,
              55.0391519
            ],
            [
              17.5287781,
              55.0389767
            ],
            [
              17.5285764,
              55.0387064
            ],
            [
              17.5284061,
              55.0384289
            ],
            [
              17.5282681,
              55.0381458
            ],
            [
              17.5281622,
              55.0378581
            ],
            [
              17.5280894,
              55.0375669
            ],
            [
              17.52805,
              55.0372722
            ],
            [
              17.5280439,
              55.0369797
            ],
            [
              17.5280714,
              55.0366861
            ],
            [
              17.5280956,
              55.0365506
            ],
            [
              17.5351314,
              55.0020858
            ],
            [
              17.3133019,
              55.0408989
            ],
            [
              17.3048544,
              55.0423678
            ]
          ]
        ]
      },
      "properties": {
        "name": "Baltica 3 OWF",
        "country": null,
        "n_turbines": null,
        "power_mw": null,
        "status": null,
        "status_detail": null,
        "status_as_of": null,
        "type_inst": null,
        "offshore": null,
        "year": null,
        "year_semantics": null,
        "year_is_assumed": null,
        "updateyear": null,
        "operational_date": null,
        "dist_coast": null,
        "area_sqkm": 100.759,
        "operator": [
          "PGE / Ørsted"
        ],
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "osm",
        "source_dataset": "OpenStreetMap",
        "source_reference": "https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824",
        "source_record_id": "way/1560193204",
        "source_snapshot_date": "2026-10-27",
        "last_updated": "2026-10-12T09:47:18Z",
        "location_status": "source-provided",
        "location_method": "outer way 1560193204 of the OSM element",
        "location_reference": null,
        "same_as": [
          "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.272"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/relation/21409513",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              16.975191,
              55.014034
            ],
            [
              16.85987,
              55.035072
            ],
            [
              16.848045,
              55.035325
            ],
            [
              16.773259,
              55.10242
            ],
            [
              16.771994,
              55.103288
            ],
            [
              16.74361,
              55.118394
            ],
            [
              16.785634,
              55.123612
            ],
            [
              16.841296,
              55.13174
            ],
            [
              16.892898,
              55.134811
            ],
            [
              16.922123,
              55.138241
            ],
            [
              16.949991,
              55.136688
            ],
            [
              16.975191,
              55.014034
            ]
          ]
        ]
      },
      "properties": {
        "name": "MFW Bałtyk II Offshore Wind Farm",
        "country": null,
        "n_turbines": 50,
        "power_mw": 720.0,
        "status": "Construction",
        "status_detail": "construction",
        "status_as_of": null,
        "type_inst": null,
        "offshore": true,
        "year": "2027",
        "year_semantics": "planned start of operation (OSM start_date)",
        "year_is_assumed": null,
        "updateyear": null,
        "operational_date": null,
        "dist_coast": null,
        "area_sqkm": 121.664,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "osm",
        "source_dataset": "OpenStreetMap",
        "source_reference": "https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824",
        "source_record_id": "relation/21409513",
        "source_snapshot_date": "2026-10-27",
        "last_updated": "2026-09-18T15:33:23Z",
        "location_status": "source-provided",
        "location_method": "outer way 1560146691 of the OSM element",
        "location_reference": null,
        "same_as": [
          "https://www.openstreetmap.org/way/1560146691",
          "https://www.openstreetmap.org/way/1560132096",
          "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.275"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/relation/21409512",
      "geometry": null,
      "properties": {
        "name": "MFW Bałtyk III",
        "country": null,
        "n_turbines": 47,
        "power_mw": 720.0,
        "status": "Construction",
        "status_detail": "construction:power=plant",
        "status_as_of": null,
        "type_inst": null,
        "offshore": null,
        "year": null,
        "year_semantics": null,
        "year_is_assumed": null,
        "updateyear": null,
        "operational_date": null,
        "dist_coast": null,
        "area_sqkm": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "osm",
        "source_dataset": "OpenStreetMap",
        "source_reference": "https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824",
        "source_record_id": "relation/21409512",
        "source_snapshot_date": "2026-10-27",
        "last_updated": "2026-09-18T12:34:04Z",
        "location_status": "unmatched",
        "location_method": "no OSM area contains this wind farm's turbines; geometry left null",
        "location_reference": null,
        "same_as": [
          "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.276"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.268",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.65,
          55.05
        ]
      },
      "properties": {
        "name": "Baltic Power",
        "country": "Poland",
        "n_turbines": 76,
        "power_mw": 1140.0,
        "status": "Construction",
        "status_detail": null,
        "status_as_of": null,
        "type_inst": "Grounded",
        "offshore": null,
        "year": "2026",
        "year_semantics": "EMODnet reported project year",
        "year_is_assumed": null,
        "updateyear": "2026",
        "operational_date": null,
        "dist_coast": 28426.9069649,
        "area_sqkm": null,
        "operator": null,
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "emodnet",
        "source_dataset": "EMODnet Human Activities - Wind Farms (emodnet:windfarms)",
        "source_reference": "https://ows.emodnet-humanactivities.eu/wfs",
        "source_record_id": "windfarms.268",
        "source_snapshot_date": "2026-11-04",
        "last_updated": null,
        "location_status": "source-provided",
        "location_method": "EMODnet point location",
        "location_reference": null,
        "same_as": [
          "https://www.openstreetmap.org/relation/21402440"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.270",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1,
          55.07
        ]
      },
      "properties": {
        "name": "Baltica 2",
        "country": "Poland",
        "n_turbines": null,
        "power_mw": 1498.0,
        "status": "Planned",
        "status_detail": null,
        "status_as_of": null,
        "type_inst": "Grounded",
        "offshore": null,
        "year": "2027",
        "year_semantics": "EMODnet reported project year",
        "year_is_assumed": null,
        "updateyear": "2026",
        "operational_date": null,
        "dist_coast": 38842.0660973,
        "area_sqkm": null,
        "operator": null,
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "emodnet",
        "source_dataset": "EMODnet Human Activities - Wind Farms (emodnet:windfarms)",
        "source_reference": "https://ows.emodnet-humanactivities.eu/wfs",
        "source_record_id": "windfarms.270",
        "source_snapshot_date": "2026-11-04",
        "last_updated": null,
        "location_status": "source-provided",
        "location_method": "EMODnet point location",
        "location_reference": null,
        "same_as": [
          "https://www.openstreetmap.org/relation/21410256"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.272",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.45,
          55.06
        ]
      },
      "properties": {
        "name": "Baltica 3",
        "country": "Poland",
        "n_turbines": null,
        "power_mw": 1045.5,
        "status": "Planned",
        "status_detail": null,
        "status_as_of": null,
        "type_inst": "Grounded",
        "offshore": null,
        "year": "2030",
        "year_semantics": "EMODnet reported project year",
        "year_is_assumed": null,
        "updateyear": "2026",
        "operational_date": null,
        "dist_coast": 33058.5337673,
        "area_sqkm": null,
        "operator": null,
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "emodnet",
        "source_dataset": "EMODnet Human Activities - Wind Farms (emodnet:windfarms)",
        "source_reference": "https://ows.emodnet-humanactivities.eu/wfs",
        "source_record_id": "windfarms.272",
        "source_snapshot_date": "2026-11-04",
        "last_updated": null,
        "location_status": "source-provided",
        "location_method": "EMODnet point location",
        "location_reference": null,
        "same_as": [
          "https://www.openstreetmap.org/way/1560193204"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.275",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.88,
          55.08
        ]
      },
      "properties": {
        "name": "Baltyk II",
        "country": "Poland",
        "n_turbines": null,
        "power_mw": 720.0,
        "status": "Planned",
        "status_detail": null,
        "status_as_of": null,
        "type_inst": "Grounded",
        "offshore": null,
        "year": "2028",
        "year_semantics": "EMODnet reported project year",
        "year_is_assumed": null,
        "updateyear": "2026",
        "operational_date": null,
        "dist_coast": 38794.6271149,
        "area_sqkm": null,
        "operator": null,
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "emodnet",
        "source_dataset": "EMODnet Human Activities - Wind Farms (emodnet:windfarms)",
        "source_reference": "https://ows.emodnet-humanactivities.eu/wfs",
        "source_record_id": "windfarms.275",
        "source_snapshot_date": "2026-11-04",
        "last_updated": null,
        "location_status": "source-provided",
        "location_method": "EMODnet point location",
        "location_reference": null,
        "same_as": [
          "https://www.openstreetmap.org/relation/21409513"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.276",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.36,
          54.99
        ]
      },
      "properties": {
        "name": "Baltyk III",
        "country": "Poland",
        "n_turbines": null,
        "power_mw": 720.0,
        "status": "Planned",
        "status_detail": null,
        "status_as_of": null,
        "type_inst": "Grounded",
        "offshore": null,
        "year": "2028",
        "year_semantics": "EMODnet reported project year",
        "year_is_assumed": null,
        "updateyear": "2026",
        "operational_date": null,
        "dist_coast": 26496.0077637,
        "area_sqkm": null,
        "operator": null,
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "emodnet",
        "source_dataset": "EMODnet Human Activities - Wind Farms (emodnet:windfarms)",
        "source_reference": "https://ows.emodnet-humanactivities.eu/wfs",
        "source_record_id": "windfarms.276",
        "source_snapshot_date": "2026-11-04",
        "last_updated": null,
        "location_status": "source-provided",
        "location_method": "EMODnet point location",
        "location_reference": null,
        "same_as": [
          "https://www.openstreetmap.org/relation/21409512"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://www.nve.no/energi/energisystem/vindkraft-paa-land/data-for-utbygde-vindkraftverk-i-norge/vindkraftverk-sider/vindkraftverk/?id=9591",
      "geometry": null,
      "properties": {
        "name": "Smøla",
        "country": "Norway",
        "n_turbines": 66,
        "power_mw": 145.8,
        "status": "Production",
        "status_detail": null,
        "status_as_of": null,
        "type_inst": null,
        "offshore": false,
        "year": "2005",
        "year_semantics": "year of entry into operation",
        "year_is_assumed": null,
        "updateyear": null,
        "operational_date": "2005-11-21",
        "dist_coast": null,
        "area_sqkm": null,
        "operator": null,
        "owner": "SMØLA VIND 2 AS",
        "developer": null,
        "licence_status": "Konsesjon gitt",
        "licensing_case": "https://www.nve.no/konsesjon/konsesjonssaker/konsesjonssak?id=3&type=A",
        "admin_units": [
          "Møre og Romsdal",
          "Smøla"
        ],
        "electricity_price_area": "NO 3",
        "mean_annual_production_gwh": 316.9,
        "notes": "NVE onshore wind power plant example. Geometry is null here because this worked example uses the facility detail page; obtain the facility geometry from the NVE GIS distribution for mapping.",
        "source_type": "national",
        "source_dataset": "NVE wind power plants (vindkraftverk)",
        "source_reference": "https://www.nve.no/energi/energisystem/vindkraft-paa-land/data-for-utbygde-vindkraftverk-i-norge/vindkraftverk-sider/vindkraftverk/?id=9591",
        "source_record_id": "9591",
        "source_snapshot_date": null,
        "last_updated": null,
        "location_status": "unmatched",
        "location_method": "geometry not taken from the NVE facility page",
        "location_reference": null,
        "same_as": null
      }
    },
    {
      "type": "Feature",
      "id": "urn:baltic-ses:national:1:example-project",
      "geometry": null,
      "properties": {
        "name": "Example Baltic Wind",
        "country": "Poland",
        "n_turbines": null,
        "power_mw": 1200,
        "status": "Planned",
        "status_detail": "In planning (auction pathway)",
        "status_as_of": "2026-08-26",
        "type_inst": null,
        "offshore": null,
        "year": "2028",
        "year_semantics": "planned first-power or completion year",
        "year_is_assumed": true,
        "updateyear": "2026",
        "operational_date": null,
        "dist_coast": null,
        "area_sqkm": null,
        "operator": null,
        "owner": null,
        "developer": "Example Energy",
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": "Year reported as assumed in the source.",
        "source_type": "national",
        "source_dataset": "Polish national offshore wind project pipeline",
        "source_reference": "https://www.gramwzielone.pl/?p=20373718",
        "source_record_id": "national-1",
        "source_snapshot_date": "2026-08-26",
        "last_updated": null,
        "location_status": "unmatched",
        "location_method": null,
        "location_reference": null,
        "same_as": null
      }
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/common-windfarm-designated-area/context.jsonld",
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/relation/21402440",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              17.5641164,
              54.9776003
            ],
            [
              17.6514242,
              54.9950473
            ],
            [
              17.718161,
              55.0049784
            ],
            [
              17.7161404,
              55.0852456
            ],
            [
              17.7686688,
              55.0834771
            ],
            [
              17.7804527,
              55.1113339
            ],
            [
              17.6206968,
              55.1113719
            ],
            [
              17.5882777,
              55.0748161
            ],
            [
              17.5641164,
              54.9776003
            ]
          ]
        ]
      },
      "properties": {
        "name": "Baltic Power",
        "country": null,
        "n_turbines": 76,
        "power_mw": 1200.0,
        "status": "Production",
        "status_detail": null,
        "status_as_of": null,
        "type_inst": null,
        "offshore": true,
        "year": null,
        "year_semantics": null,
        "year_is_assumed": null,
        "updateyear": null,
        "operational_date": null,
        "dist_coast": null,
        "area_sqkm": 122.01,
        "operator": [
          "Baltic Power"
        ],
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "osm",
        "source_dataset": "OpenStreetMap",
        "source_reference": "https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824",
        "source_record_id": "relation/21402440",
        "source_snapshot_date": "2026-10-27",
        "last_updated": "2026-09-18T16:06:52Z",
        "location_status": "source-provided",
        "location_method": "outer way 1532855580 of the OSM element",
        "location_reference": null,
        "same_as": [
          "https://www.openstreetmap.org/way/1532855580",
          "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.268"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/relation/21410256",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              17.0488829,
              55.0159008
            ],
            [
              16.9791503,
              55.0336525
            ],
            [
              16.9626103,
              55.1142444
            ],
            [
              17.0305922,
              55.1141769
            ],
            [
              17.0905683,
              55.1096853
            ],
            [
              17.0906639,
              55.1096786
            ],
            [
              17.1600869,
              55.1049367
            ],
            [
              17.1600947,
              55.1049361
            ],
            [
              17.2277706,
              55.1003139
            ],
            [
              17.2278758,
              55.1003069
            ],
            [
              17.2283875,
              55.1002856
            ],
            [
              17.2288992,
              55.1002833
            ],
            [
              17.2294122,
              55.1003006
            ],
            [
              17.2299211,
              55.1003367
            ],
            [
              17.230425,
              55.1003919
            ],
            [
              17.2309211,
              55.1004658
            ],
            [
              17.2310894,
              55.1004956
            ],
            [
              17.26984,
              55.1075956
            ],
            [
              17.2715453,
              55.0892258
            ],
            [
              17.2570575,
              55.0795728
            ],
            [
              17.2439575,
              55.0708386
            ],
            [
              17.2273725,
              55.0597736
            ],
            [
              17.2012272,
              55.0423133
            ],
            [
              17.1864494,
              55.0430644
            ],
            [
              17.1790169,
              55.0454525
            ],
            [
              17.1282531,
              55.0617422
            ],
            [
              17.1201028,
              55.0695211
            ],
            [
              17.1200661,
              55.0695558
            ],
            [
              17.1197839,
              55.0698014
            ],
            [
              17.1194742,
              55.0700356
            ],
            [
              17.1191386,
              55.0702578
            ],
            [
              17.1187783,
              55.0704669
            ],
            [
              17.118395,
              55.0706622
            ],
            [
              17.1179903,
              55.0708425
            ],
            [
              17.1175658,
              55.0710072
            ],
            [
              17.1171236,
              55.0711558
            ],
            [
              17.1166667,
              55.0712872
            ],
            [
              17.1161928,
              55.0714014
            ],
            [
              17.1157086,
              55.0714975
            ],
            [
              17.1152144,
              55.0715753
            ],
            [
              17.1147122,
              55.0716344
            ],
            [
              17.1142047,
              55.0716744
            ],
            [
              17.113819,
              55.0716959
            ],
            [
              17.1126694,
              55.0716794
            ],
            [
              17.1121611,
              55.0716428
            ],
            [
              17.1116578,
              55.0715869
            ],
            [
              17.1106184,
              55.0417445
            ],
            [
              17.1106384,
              55.041711
            ],
            [
              17.1100125,
              55.0416711
            ],
            [
              17.1097406,
              55.0416248
            ],
            [
              17.1092953,
              55.0415724
            ],
            [
              17.1088675,
              55.0415141
            ],
            [
              17.1084592,
              55.0414501
            ],
            [
              17.1080719,
              55.0413808
            ],
            [
              17.1077075,
              55.0413063
            ],
            [
              17.1073675,
              55.0412271
            ],
            [
              17.1070231,
              55.0411435
            ],
            [
              17.1067632,
              55.0410558
            ],
            [
              17.1065073,
              55.0409645
            ],
            [
              17.1061014,
              55.0408698
            ],
            [
              17.1060786,
              55.0407722
            ],
            [
              17.1059124,
              55.0406721
            ],
            [
              17.1057796,
              55.0405701
            ],
            [
              17.1057665,
              55.0405615
            ],
            [
              17.0883056,
              55.0252414
            ],
            [
              17.0822189,
              55.0097236
            ],
            [
              17.0821817,
              55.0087331
            ],
            [
              17.0488829,
              55.0159008
            ]
          ]
        ]
      },
      "properties": {
        "name": "Baltica 2",
        "country": null,
        "n_turbines": 107,
        "power_mw": 1500.0,
        "status": "Construction",
        "status_detail": "construction:power=plant",
        "status_as_of": null,
        "type_inst": null,
        "offshore": null,
        "year": null,
        "year_semantics": null,
        "year_is_assumed": null,
        "updateyear": null,
        "operational_date": null,
        "dist_coast": null,
        "area_sqkm": 139.894,
        "operator": [
          "PGE Baltica",
          "Orsted"
        ],
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "osm",
        "source_dataset": "OpenStreetMap",
        "source_reference": "https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824",
        "source_record_id": "relation/21410256",
        "source_snapshot_date": "2026-10-27",
        "last_updated": "2026-09-18T15:33:23Z",
        "location_status": "source-provided",
        "location_method": "outer way 1560193205 of the OSM element",
        "location_reference": null,
        "same_as": [
          "https://www.openstreetmap.org/way/1560193205",
          "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.270"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/way/1560193204",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              17.3048544,
              55.0423678
            ],
            [
              17.3209678,
              55.0530986
            ],
            [
              17.3392028,
              55.0536478
            ],
            [
              17.3393014,
              55.0536867
            ],
            [
              17.3844589,
              55.0549986
            ],
            [
              17.3847472,
              55.05501
            ],
            [
              17.3852556,
              55.0550456
            ],
            [
              17.3857592,
              55.0551003
            ],
            [
              17.3862553,
              55.0551736
            ],
            [
              17.3867419,
              55.0552656
            ],
            [
              17.3872169,
              55.0553753
            ],
            [
              17.3876786,
              55.0555031
            ],
            [
              17.3881247,
              55.0556475
            ],
            [
              17.3885533,
              55.0558086
            ],
            [
              17.3889628,
              55.0559853
            ],
            [
              17.3893514,
              55.0561769
            ],
            [
              17.3897169,
              55.0563831
            ],
            [
              17.3900586,
              55.0566022
            ],
            [
              17.3903742,
              55.0568336
            ],
            [
              17.3906631,
              55.0570767
            ],
            [
              17.3909233,
              55.0573297
            ],
            [
              17.3911544,
              55.0575922
            ],
            [
              17.391355,
              55.0578628
            ],
            [
              17.3912189,
              55.0581406
            ],
            [
              17.3916619,
              55.0584236
            ],
            [
              17.3917667,
              55.0587117
            ],
            [
              17.3918386,
              55.0590028
            ],
            [
              17.3918769,
              55.0592961
            ],
            [
              17.3918736,
              55.0597178
            ],
            [
              17.3884753,
              55.0975811
            ],
            [
              17.4556206,
              55.0995556
            ],
            [
              17.4556253,
              55.0995583
            ],
            [
              17.552685,
              55.1023775
            ],
            [
              17.5407375,
              55.0652203
            ],
            [
              17.5407331,
              55.0652064
            ],
            [
              17.5344233,
              55.0452031
            ],
            [
              17.5289289,
              55.0391519
            ],
            [
              17.5287781,
              55.0389767
            ],
            [
              17.5285764,
              55.0387064
            ],
            [
              17.5284061,
              55.0384289
            ],
            [
              17.5282681,
              55.0381458
            ],
            [
              17.5281622,
              55.0378581
            ],
            [
              17.5280894,
              55.0375669
            ],
            [
              17.52805,
              55.0372722
            ],
            [
              17.5280439,
              55.0369797
            ],
            [
              17.5280714,
              55.0366861
            ],
            [
              17.5280956,
              55.0365506
            ],
            [
              17.5351314,
              55.0020858
            ],
            [
              17.3133019,
              55.0408989
            ],
            [
              17.3048544,
              55.0423678
            ]
          ]
        ]
      },
      "properties": {
        "name": "Baltica 3 OWF",
        "country": null,
        "n_turbines": null,
        "power_mw": null,
        "status": null,
        "status_detail": null,
        "status_as_of": null,
        "type_inst": null,
        "offshore": null,
        "year": null,
        "year_semantics": null,
        "year_is_assumed": null,
        "updateyear": null,
        "operational_date": null,
        "dist_coast": null,
        "area_sqkm": 100.759,
        "operator": [
          "PGE / \u00d8rsted"
        ],
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "osm",
        "source_dataset": "OpenStreetMap",
        "source_reference": "https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824",
        "source_record_id": "way/1560193204",
        "source_snapshot_date": "2026-10-27",
        "last_updated": "2026-10-12T09:47:18Z",
        "location_status": "source-provided",
        "location_method": "outer way 1560193204 of the OSM element",
        "location_reference": null,
        "same_as": [
          "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.272"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/relation/21409513",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              16.975191,
              55.014034
            ],
            [
              16.85987,
              55.035072
            ],
            [
              16.848045,
              55.035325
            ],
            [
              16.773259,
              55.10242
            ],
            [
              16.771994,
              55.103288
            ],
            [
              16.74361,
              55.118394
            ],
            [
              16.785634,
              55.123612
            ],
            [
              16.841296,
              55.13174
            ],
            [
              16.892898,
              55.134811
            ],
            [
              16.922123,
              55.138241
            ],
            [
              16.949991,
              55.136688
            ],
            [
              16.975191,
              55.014034
            ]
          ]
        ]
      },
      "properties": {
        "name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "country": null,
        "n_turbines": 50,
        "power_mw": 720.0,
        "status": "Construction",
        "status_detail": "construction",
        "status_as_of": null,
        "type_inst": null,
        "offshore": true,
        "year": "2027",
        "year_semantics": "planned start of operation (OSM start_date)",
        "year_is_assumed": null,
        "updateyear": null,
        "operational_date": null,
        "dist_coast": null,
        "area_sqkm": 121.664,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "osm",
        "source_dataset": "OpenStreetMap",
        "source_reference": "https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824",
        "source_record_id": "relation/21409513",
        "source_snapshot_date": "2026-10-27",
        "last_updated": "2026-09-18T15:33:23Z",
        "location_status": "source-provided",
        "location_method": "outer way 1560146691 of the OSM element",
        "location_reference": null,
        "same_as": [
          "https://www.openstreetmap.org/way/1560146691",
          "https://www.openstreetmap.org/way/1560132096",
          "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.275"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://www.openstreetmap.org/relation/21409512",
      "geometry": null,
      "properties": {
        "name": "MFW Ba\u0142tyk III",
        "country": null,
        "n_turbines": 47,
        "power_mw": 720.0,
        "status": "Construction",
        "status_detail": "construction:power=plant",
        "status_as_of": null,
        "type_inst": null,
        "offshore": null,
        "year": null,
        "year_semantics": null,
        "year_is_assumed": null,
        "updateyear": null,
        "operational_date": null,
        "dist_coast": null,
        "area_sqkm": null,
        "operator": [
          "Equinor",
          "Polenergia"
        ],
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "osm",
        "source_dataset": "OpenStreetMap",
        "source_reference": "https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824",
        "source_record_id": "relation/21409512",
        "source_snapshot_date": "2026-10-27",
        "last_updated": "2026-09-18T12:34:04Z",
        "location_status": "unmatched",
        "location_method": "no OSM area contains this wind farm's turbines; geometry left null",
        "location_reference": null,
        "same_as": [
          "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.276"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.268",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.65,
          55.05
        ]
      },
      "properties": {
        "name": "Baltic Power",
        "country": "Poland",
        "n_turbines": 76,
        "power_mw": 1140.0,
        "status": "Construction",
        "status_detail": null,
        "status_as_of": null,
        "type_inst": "Grounded",
        "offshore": null,
        "year": "2026",
        "year_semantics": "EMODnet reported project year",
        "year_is_assumed": null,
        "updateyear": "2026",
        "operational_date": null,
        "dist_coast": 28426.9069649,
        "area_sqkm": null,
        "operator": null,
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "emodnet",
        "source_dataset": "EMODnet Human Activities - Wind Farms (emodnet:windfarms)",
        "source_reference": "https://ows.emodnet-humanactivities.eu/wfs",
        "source_record_id": "windfarms.268",
        "source_snapshot_date": "2026-11-04",
        "last_updated": null,
        "location_status": "source-provided",
        "location_method": "EMODnet point location",
        "location_reference": null,
        "same_as": [
          "https://www.openstreetmap.org/relation/21402440"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.270",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.1,
          55.07
        ]
      },
      "properties": {
        "name": "Baltica 2",
        "country": "Poland",
        "n_turbines": null,
        "power_mw": 1498.0,
        "status": "Planned",
        "status_detail": null,
        "status_as_of": null,
        "type_inst": "Grounded",
        "offshore": null,
        "year": "2027",
        "year_semantics": "EMODnet reported project year",
        "year_is_assumed": null,
        "updateyear": "2026",
        "operational_date": null,
        "dist_coast": 38842.0660973,
        "area_sqkm": null,
        "operator": null,
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "emodnet",
        "source_dataset": "EMODnet Human Activities - Wind Farms (emodnet:windfarms)",
        "source_reference": "https://ows.emodnet-humanactivities.eu/wfs",
        "source_record_id": "windfarms.270",
        "source_snapshot_date": "2026-11-04",
        "last_updated": null,
        "location_status": "source-provided",
        "location_method": "EMODnet point location",
        "location_reference": null,
        "same_as": [
          "https://www.openstreetmap.org/relation/21410256"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.272",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.45,
          55.06
        ]
      },
      "properties": {
        "name": "Baltica 3",
        "country": "Poland",
        "n_turbines": null,
        "power_mw": 1045.5,
        "status": "Planned",
        "status_detail": null,
        "status_as_of": null,
        "type_inst": "Grounded",
        "offshore": null,
        "year": "2030",
        "year_semantics": "EMODnet reported project year",
        "year_is_assumed": null,
        "updateyear": "2026",
        "operational_date": null,
        "dist_coast": 33058.5337673,
        "area_sqkm": null,
        "operator": null,
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "emodnet",
        "source_dataset": "EMODnet Human Activities - Wind Farms (emodnet:windfarms)",
        "source_reference": "https://ows.emodnet-humanactivities.eu/wfs",
        "source_record_id": "windfarms.272",
        "source_snapshot_date": "2026-11-04",
        "last_updated": null,
        "location_status": "source-provided",
        "location_method": "EMODnet point location",
        "location_reference": null,
        "same_as": [
          "https://www.openstreetmap.org/way/1560193204"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.275",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.88,
          55.08
        ]
      },
      "properties": {
        "name": "Baltyk II",
        "country": "Poland",
        "n_turbines": null,
        "power_mw": 720.0,
        "status": "Planned",
        "status_detail": null,
        "status_as_of": null,
        "type_inst": "Grounded",
        "offshore": null,
        "year": "2028",
        "year_semantics": "EMODnet reported project year",
        "year_is_assumed": null,
        "updateyear": "2026",
        "operational_date": null,
        "dist_coast": 38794.6271149,
        "area_sqkm": null,
        "operator": null,
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "emodnet",
        "source_dataset": "EMODnet Human Activities - Wind Farms (emodnet:windfarms)",
        "source_reference": "https://ows.emodnet-humanactivities.eu/wfs",
        "source_record_id": "windfarms.275",
        "source_snapshot_date": "2026-11-04",
        "last_updated": null,
        "location_status": "source-provided",
        "location_method": "EMODnet point location",
        "location_reference": null,
        "same_as": [
          "https://www.openstreetmap.org/relation/21409513"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.276",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.36,
          54.99
        ]
      },
      "properties": {
        "name": "Baltyk III",
        "country": "Poland",
        "n_turbines": null,
        "power_mw": 720.0,
        "status": "Planned",
        "status_detail": null,
        "status_as_of": null,
        "type_inst": "Grounded",
        "offshore": null,
        "year": "2028",
        "year_semantics": "EMODnet reported project year",
        "year_is_assumed": null,
        "updateyear": "2026",
        "operational_date": null,
        "dist_coast": 26496.0077637,
        "area_sqkm": null,
        "operator": null,
        "owner": null,
        "developer": null,
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": null,
        "source_type": "emodnet",
        "source_dataset": "EMODnet Human Activities - Wind Farms (emodnet:windfarms)",
        "source_reference": "https://ows.emodnet-humanactivities.eu/wfs",
        "source_record_id": "windfarms.276",
        "source_snapshot_date": "2026-11-04",
        "last_updated": null,
        "location_status": "source-provided",
        "location_method": "EMODnet point location",
        "location_reference": null,
        "same_as": [
          "https://www.openstreetmap.org/relation/21409512"
        ]
      }
    },
    {
      "type": "Feature",
      "id": "https://www.nve.no/energi/energisystem/vindkraft-paa-land/data-for-utbygde-vindkraftverk-i-norge/vindkraftverk-sider/vindkraftverk/?id=9591",
      "geometry": null,
      "properties": {
        "name": "Sm\u00f8la",
        "country": "Norway",
        "n_turbines": 66,
        "power_mw": 145.8,
        "status": "Production",
        "status_detail": null,
        "status_as_of": null,
        "type_inst": null,
        "offshore": false,
        "year": "2005",
        "year_semantics": "year of entry into operation",
        "year_is_assumed": null,
        "updateyear": null,
        "operational_date": "2005-11-21",
        "dist_coast": null,
        "area_sqkm": null,
        "operator": null,
        "owner": "SM\u00d8LA VIND 2 AS",
        "developer": null,
        "licence_status": "Konsesjon gitt",
        "licensing_case": "https://www.nve.no/konsesjon/konsesjonssaker/konsesjonssak?id=3&type=A",
        "admin_units": [
          "M\u00f8re og Romsdal",
          "Sm\u00f8la"
        ],
        "electricity_price_area": "NO 3",
        "mean_annual_production_gwh": 316.9,
        "notes": "NVE onshore wind power plant example. Geometry is null here because this worked example uses the facility detail page; obtain the facility geometry from the NVE GIS distribution for mapping.",
        "source_type": "national",
        "source_dataset": "NVE wind power plants (vindkraftverk)",
        "source_reference": "https://www.nve.no/energi/energisystem/vindkraft-paa-land/data-for-utbygde-vindkraftverk-i-norge/vindkraftverk-sider/vindkraftverk/?id=9591",
        "source_record_id": "9591",
        "source_snapshot_date": null,
        "last_updated": null,
        "location_status": "unmatched",
        "location_method": "geometry not taken from the NVE facility page",
        "location_reference": null,
        "same_as": null
      }
    },
    {
      "type": "Feature",
      "id": "urn:baltic-ses:national:1:example-project",
      "geometry": null,
      "properties": {
        "name": "Example Baltic Wind",
        "country": "Poland",
        "n_turbines": null,
        "power_mw": 1200,
        "status": "Planned",
        "status_detail": "In planning (auction pathway)",
        "status_as_of": "2026-08-26",
        "type_inst": null,
        "offshore": null,
        "year": "2028",
        "year_semantics": "planned first-power or completion year",
        "year_is_assumed": true,
        "updateyear": "2026",
        "operational_date": null,
        "dist_coast": null,
        "area_sqkm": null,
        "operator": null,
        "owner": null,
        "developer": "Example Energy",
        "licence_status": null,
        "licensing_case": null,
        "admin_units": null,
        "electricity_price_area": null,
        "mean_annual_production_gwh": null,
        "notes": "Year reported as assumed in the source.",
        "source_type": "national",
        "source_dataset": "Polish national offshore wind project pipeline",
        "source_reference": "https://www.gramwzielone.pl/?p=20373718",
        "source_record_id": "national-1",
        "source_snapshot_date": "2026-08-26",
        "last_updated": null,
        "location_status": "unmatched",
        "location_method": null,
        "location_reference": null,
        "same_as": null
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/ogc/hosted/seadots/emodnet/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix owf: <https://w3id.org/ogc/hosted/seadots/windfarm#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<urn:baltic-ses:national:1:example-project> a geojson:Feature ;
    dcterms:description "Year reported as assumed in the source." ;
    dcterms:identifier "national-1" ;
    dcterms:source <https://www.gramwzielone.pl/?p=20373718> ;
    schema:addressCountry :Poland ;
    schema:name "Example Baltic Wind" ;
    owf:conditionOfFacility :Planned ;
    owf:developerName "Example Energy" ;
    owf:locationStatus owf:LocationUnmatched ;
    owf:powerMW 1200.0 ;
    owf:sourceDataset "Polish national offshore wind project pipeline" ;
    owf:sourceSnapshotDate "2026-08-26"^^xsd:date ;
    owf:sourceType owf:NationalSource ;
    owf:statusAsOf "2026-08-26"^^xsd:date ;
    owf:statusDetail "In planning (auction pathway)" ;
    owf:updateYear "2026" ;
    owf:year "2028" ;
    owf:yearIsAssumed true ;
    owf:yearSemantics "planned first-power or completion year" .

<https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.268> a geojson:Feature ;
    dcterms:identifier "windfarms.268" ;
    dcterms:source <https://ows.emodnet-humanactivities.eu/wfs> ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.765e+01 5.505e+01 ) ] ;
    schema:addressCountry :Poland ;
    schema:name "Baltic Power" ;
    schema:sameAs <https://www.openstreetmap.org/relation/21402440> ;
    owf:conditionOfFacility :Construction ;
    owf:distanceToCoast 28426.9069649 ;
    owf:installationType "Grounded" ;
    owf:locationMethod "EMODnet point location" ;
    owf:locationStatus owf:LocationSourceProvided ;
    owf:nTurbines 76 ;
    owf:powerMW 1140.0 ;
    owf:sourceDataset "EMODnet Human Activities - Wind Farms (emodnet:windfarms)" ;
    owf:sourceSnapshotDate "2026-11-04"^^xsd:date ;
    owf:sourceType owf:EmodnetSource ;
    owf:updateYear "2026" ;
    owf:year "2026" ;
    owf:yearSemantics "EMODnet reported project year" .

<https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.270> a geojson:Feature ;
    dcterms:identifier "windfarms.270" ;
    dcterms:source <https://ows.emodnet-humanactivities.eu/wfs> ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.71e+01 5.507e+01 ) ] ;
    schema:addressCountry :Poland ;
    schema:name "Baltica 2" ;
    schema:sameAs <https://www.openstreetmap.org/relation/21410256> ;
    owf:conditionOfFacility :Planned ;
    owf:distanceToCoast 38842.0660973 ;
    owf:installationType "Grounded" ;
    owf:locationMethod "EMODnet point location" ;
    owf:locationStatus owf:LocationSourceProvided ;
    owf:powerMW 1498.0 ;
    owf:sourceDataset "EMODnet Human Activities - Wind Farms (emodnet:windfarms)" ;
    owf:sourceSnapshotDate "2026-11-04"^^xsd:date ;
    owf:sourceType owf:EmodnetSource ;
    owf:updateYear "2026" ;
    owf:year "2027" ;
    owf:yearSemantics "EMODnet reported project year" .

<https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.272> a geojson:Feature ;
    dcterms:identifier "windfarms.272" ;
    dcterms:source <https://ows.emodnet-humanactivities.eu/wfs> ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.745e+01 5.506e+01 ) ] ;
    schema:addressCountry :Poland ;
    schema:name "Baltica 3" ;
    schema:sameAs <https://www.openstreetmap.org/way/1560193204> ;
    owf:conditionOfFacility :Planned ;
    owf:distanceToCoast 33058.5337673 ;
    owf:installationType "Grounded" ;
    owf:locationMethod "EMODnet point location" ;
    owf:locationStatus owf:LocationSourceProvided ;
    owf:powerMW 1045.5 ;
    owf:sourceDataset "EMODnet Human Activities - Wind Farms (emodnet:windfarms)" ;
    owf:sourceSnapshotDate "2026-11-04"^^xsd:date ;
    owf:sourceType owf:EmodnetSource ;
    owf:updateYear "2026" ;
    owf:year "2030" ;
    owf:yearSemantics "EMODnet reported project year" .

<https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.275> a geojson:Feature ;
    dcterms:identifier "windfarms.275" ;
    dcterms:source <https://ows.emodnet-humanactivities.eu/wfs> ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.688e+01 5.508e+01 ) ] ;
    schema:addressCountry :Poland ;
    schema:name "Baltyk II" ;
    schema:sameAs <https://www.openstreetmap.org/relation/21409513> ;
    owf:conditionOfFacility :Planned ;
    owf:distanceToCoast 38794.6271149 ;
    owf:installationType "Grounded" ;
    owf:locationMethod "EMODnet point location" ;
    owf:locationStatus owf:LocationSourceProvided ;
    owf:powerMW 720.0 ;
    owf:sourceDataset "EMODnet Human Activities - Wind Farms (emodnet:windfarms)" ;
    owf:sourceSnapshotDate "2026-11-04"^^xsd:date ;
    owf:sourceType owf:EmodnetSource ;
    owf:updateYear "2026" ;
    owf:year "2028" ;
    owf:yearSemantics "EMODnet reported project year" .

<https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.276> a geojson:Feature ;
    dcterms:identifier "windfarms.276" ;
    dcterms:source <https://ows.emodnet-humanactivities.eu/wfs> ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.736e+01 5.499e+01 ) ] ;
    schema:addressCountry :Poland ;
    schema:name "Baltyk III" ;
    schema:sameAs <https://www.openstreetmap.org/relation/21409512> ;
    owf:conditionOfFacility :Planned ;
    owf:distanceToCoast 26496.0077637 ;
    owf:installationType "Grounded" ;
    owf:locationMethod "EMODnet point location" ;
    owf:locationStatus owf:LocationSourceProvided ;
    owf:powerMW 720.0 ;
    owf:sourceDataset "EMODnet Human Activities - Wind Farms (emodnet:windfarms)" ;
    owf:sourceSnapshotDate "2026-11-04"^^xsd:date ;
    owf:sourceType owf:EmodnetSource ;
    owf:updateYear "2026" ;
    owf:year "2028" ;
    owf:yearSemantics "EMODnet reported project year" .

<https://www.nve.no/energi/energisystem/vindkraft-paa-land/data-for-utbygde-vindkraftverk-i-norge/vindkraftverk-sider/vindkraftverk/?id=9591> a geojson:Feature ;
    dcterms:description "NVE onshore wind power plant example. Geometry is null here because this worked example uses the facility detail page; obtain the facility geometry from the NVE GIS distribution for mapping." ;
    dcterms:identifier "9591" ;
    dcterms:source <https://www.nve.no/energi/energisystem/vindkraft-paa-land/data-for-utbygde-vindkraftverk-i-norge/vindkraftverk-sider/vindkraftverk/?id=9591> ;
    schema:addressCountry :Norway ;
    schema:name "Smøla" ;
    owf:administrativeUnit "Møre og Romsdal",
        "Smøla" ;
    owf:conditionOfFacility :Production ;
    owf:electricityPriceArea "NO 3" ;
    owf:licenceStatus "Konsesjon gitt" ;
    owf:licensingCase <https://www.nve.no/konsesjon/konsesjonssaker/konsesjonssak?id=3&type=A> ;
    owf:locationMethod "geometry not taken from the NVE facility page" ;
    owf:locationStatus owf:LocationUnmatched ;
    owf:meanAnnualProductionGWh 316.9 ;
    owf:nTurbines 66 ;
    owf:offshore false ;
    owf:operationalDate "2005-11-21"^^xsd:date ;
    owf:ownerName "SMØLA VIND 2 AS" ;
    owf:powerMW 145.8 ;
    owf:sourceDataset "NVE wind power plants (vindkraftverk)" ;
    owf:sourceType owf:NationalSource ;
    owf:year "2005" ;
    owf:yearSemantics "year of entry into operation" .

<https://www.openstreetmap.org/relation/21402440> a geojson:Feature ;
    dcterms:identifier "relation/21402440" ;
    dcterms:modified "2026-09-18T16:06:52+00:00"^^xsd:dateTime ;
    dcterms:source <https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824> ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.756412e+01 5.49776e+01 ) ( 1.765142e+01 5.499505e+01 ) ( 1.771816e+01 5.500498e+01 ) ( 1.771614e+01 5.508525e+01 ) ( 1.776867e+01 5.508348e+01 ) ( 1.778045e+01 5.511133e+01 ) ( 1.76207e+01 5.511137e+01 ) ( 1.758828e+01 5.507482e+01 ) ( 1.756412e+01 5.49776e+01 ) ) ) ] ;
    schema:name "Baltic Power" ;
    schema:sameAs <https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.268>,
        <https://www.openstreetmap.org/way/1532855580> ;
    owf:areaSqKm 122.01 ;
    owf:conditionOfFacility :Production ;
    owf:locationMethod "outer way 1532855580 of the OSM element" ;
    owf:locationStatus owf:LocationSourceProvided ;
    owf:nTurbines 76 ;
    owf:offshore true ;
    owf:operatorName "Baltic Power" ;
    owf:powerMW 1200.0 ;
    owf:sourceDataset "OpenStreetMap" ;
    owf:sourceSnapshotDate "2026-10-27"^^xsd:date ;
    owf:sourceType owf:OpenStreetMapSource .

<https://www.openstreetmap.org/relation/21409512> a geojson:Feature ;
    dcterms:identifier "relation/21409512" ;
    dcterms:modified "2026-09-18T12:34:04+00:00"^^xsd:dateTime ;
    dcterms:source <https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824> ;
    schema:name "MFW Bałtyk III" ;
    schema:sameAs <https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.276> ;
    owf:conditionOfFacility :Construction ;
    owf:locationMethod "no OSM area contains this wind farm's turbines; geometry left null" ;
    owf:locationStatus owf:LocationUnmatched ;
    owf:nTurbines 47 ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:powerMW 720.0 ;
    owf:sourceDataset "OpenStreetMap" ;
    owf:sourceSnapshotDate "2026-10-27"^^xsd:date ;
    owf:sourceType owf:OpenStreetMapSource ;
    owf:statusDetail "construction:power=plant" .

<https://www.openstreetmap.org/relation/21409513> a geojson:Feature ;
    dcterms:identifier "relation/21409513" ;
    dcterms:modified "2026-09-18T15:33:23+00:00"^^xsd:dateTime ;
    dcterms:source <https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824> ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.697519e+01 5.501403e+01 ) ( 1.685987e+01 5.503507e+01 ) ( 1.684804e+01 5.503533e+01 ) ( 1.677326e+01 5.510242e+01 ) ( 1.677199e+01 5.510329e+01 ) ( 1.674361e+01 5.511839e+01 ) ( 1.678563e+01 5.512361e+01 ) ( 1.68413e+01 5.513174e+01 ) ( 1.68929e+01 5.513481e+01 ) ( 1.692212e+01 5.513824e+01 ) ( 1.694999e+01 5.513669e+01 ) ( 1.697519e+01 5.501403e+01 ) ) ) ] ;
    schema:name "MFW Bałtyk II Offshore Wind Farm" ;
    schema:sameAs <https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.275>,
        <https://www.openstreetmap.org/way/1560132096>,
        <https://www.openstreetmap.org/way/1560146691> ;
    owf:areaSqKm 121.664 ;
    owf:conditionOfFacility :Construction ;
    owf:locationMethod "outer way 1560146691 of the OSM element" ;
    owf:locationStatus owf:LocationSourceProvided ;
    owf:nTurbines 50 ;
    owf:offshore true ;
    owf:operatorName "Equinor",
        "Polenergia" ;
    owf:powerMW 720.0 ;
    owf:sourceDataset "OpenStreetMap" ;
    owf:sourceSnapshotDate "2026-10-27"^^xsd:date ;
    owf:sourceType owf:OpenStreetMapSource ;
    owf:statusDetail "construction" ;
    owf:year "2027" ;
    owf:yearSemantics "planned start of operation (OSM start_date)" .

<https://www.openstreetmap.org/relation/21410256> a geojson:Feature ;
    dcterms:identifier "relation/21410256" ;
    dcterms:modified "2026-09-18T15:33:23+00:00"^^xsd:dateTime ;
    dcterms:source <https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824> ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.704888e+01 5.50159e+01 ) ( 1.697915e+01 5.503365e+01 ) ( 1.696261e+01 5.511424e+01 ) ( 1.703059e+01 5.511418e+01 ) ( 1.709057e+01 5.510969e+01 ) ( 1.709066e+01 5.510968e+01 ) ( 1.716009e+01 5.510494e+01 ) ( 1.716009e+01 5.510494e+01 ) ( 1.722777e+01 5.510031e+01 ) ( 1.722788e+01 5.510031e+01 ) ( 1.722839e+01 5.510029e+01 ) ( 1.72289e+01 5.510028e+01 ) ( 1.722941e+01 5.51003e+01 ) ( 1.722992e+01 5.510034e+01 ) ( 1.723043e+01 5.510039e+01 ) ( 1.723092e+01 5.510047e+01 ) ( 1.723109e+01 5.51005e+01 ) ( 1.726984e+01 5.51076e+01 ) ( 1.727155e+01 5.508923e+01 ) ( 1.725706e+01 5.507957e+01 ) ( 1.724396e+01 5.507084e+01 ) ( 1.722737e+01 5.505977e+01 ) ( 1.720123e+01 5.504231e+01 ) ( 1.718645e+01 5.504306e+01 ) ( 1.717902e+01 5.504545e+01 ) ( 1.712825e+01 5.506174e+01 ) ( 1.71201e+01 5.506952e+01 ) ( 1.712007e+01 5.506956e+01 ) ( 1.711978e+01 5.50698e+01 ) ( 1.711947e+01 5.507004e+01 ) ( 1.711914e+01 5.507026e+01 ) ( 1.711878e+01 5.507047e+01 ) ( 1.711839e+01 5.507066e+01 ) ( 1.711799e+01 5.507084e+01 ) ( 1.711757e+01 5.507101e+01 ) ( 1.711712e+01 5.507116e+01 ) ( 1.711667e+01 5.507129e+01 ) ( 1.711619e+01 5.50714e+01 ) ( 1.711571e+01 5.50715e+01 ) ( 1.711521e+01 5.507158e+01 ) ( 1.711471e+01 5.507163e+01 ) ( 1.71142e+01 5.507167e+01 ) ( 1.711382e+01 5.50717e+01 ) ( 1.711267e+01 5.507168e+01 ) ( 1.711216e+01 5.507164e+01 ) ( 1.711166e+01 5.507159e+01 ) ( 1.711062e+01 5.504174e+01 ) ( 1.711064e+01 5.504171e+01 ) ( 1.711001e+01 5.504167e+01 ) ( 1.710974e+01 5.504162e+01 ) ( 1.71093e+01 5.504157e+01 ) ( 1.710887e+01 5.504151e+01 ) ( 1.710846e+01 5.504145e+01 ) ( 1.710807e+01 5.504138e+01 ) ( 1.710771e+01 5.504131e+01 ) ( 1.710737e+01 5.504123e+01 ) ( 1.710702e+01 5.504114e+01 ) ( 1.710676e+01 5.504106e+01 ) ( 1.710651e+01 5.504096e+01 ) ( 1.71061e+01 5.504087e+01 ) ( 1.710608e+01 5.504077e+01 ) ( 1.710591e+01 5.504067e+01 ) ( 1.710578e+01 5.504057e+01 ) ( 1.710577e+01 5.504056e+01 ) ( 1.708831e+01 5.502524e+01 ) ( 1.708222e+01 5.500972e+01 ) ( 1.708218e+01 5.500873e+01 ) ( 1.704888e+01 5.50159e+01 ) ) ) ] ;
    schema:name "Baltica 2" ;
    schema:sameAs <https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.270>,
        <https://www.openstreetmap.org/way/1560193205> ;
    owf:areaSqKm 139.894 ;
    owf:conditionOfFacility :Construction ;
    owf:locationMethod "outer way 1560193205 of the OSM element" ;
    owf:locationStatus owf:LocationSourceProvided ;
    owf:nTurbines 107 ;
    owf:operatorName "Orsted",
        "PGE Baltica" ;
    owf:powerMW 1500.0 ;
    owf:sourceDataset "OpenStreetMap" ;
    owf:sourceSnapshotDate "2026-10-27"^^xsd:date ;
    owf:sourceType owf:OpenStreetMapSource ;
    owf:statusDetail "construction:power=plant" .

<https://www.openstreetmap.org/way/1560193204> a geojson:Feature ;
    dcterms:identifier "way/1560193204" ;
    dcterms:modified "2026-10-12T09:47:18+00:00"^^xsd:dateTime ;
    dcterms:source <https://api.openstreetmap.org/api/0.6/map.json?bbox=16.74361,54.953732,17.78045,55.13824> ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.730485e+01 5.504237e+01 ) ( 1.732097e+01 5.50531e+01 ) ( 1.73392e+01 5.505365e+01 ) ( 1.73393e+01 5.505369e+01 ) ( 1.738446e+01 5.5055e+01 ) ( 1.738475e+01 5.505501e+01 ) ( 1.738526e+01 5.505505e+01 ) ( 1.738576e+01 5.50551e+01 ) ( 1.738626e+01 5.505517e+01 ) ( 1.738674e+01 5.505527e+01 ) ( 1.738722e+01 5.505538e+01 ) ( 1.738768e+01 5.50555e+01 ) ( 1.738812e+01 5.505565e+01 ) ( 1.738855e+01 5.505581e+01 ) ( 1.738896e+01 5.505599e+01 ) ( 1.738935e+01 5.505618e+01 ) ( 1.738972e+01 5.505638e+01 ) ( 1.739006e+01 5.50566e+01 ) ( 1.739037e+01 5.505683e+01 ) ( 1.739066e+01 5.505708e+01 ) ( 1.739092e+01 5.505733e+01 ) ( 1.739115e+01 5.505759e+01 ) ( 1.739136e+01 5.505786e+01 ) ( 1.739122e+01 5.505814e+01 ) ( 1.739166e+01 5.505842e+01 ) ( 1.739177e+01 5.505871e+01 ) ( 1.739184e+01 5.5059e+01 ) ( 1.739188e+01 5.50593e+01 ) ( 1.739187e+01 5.505972e+01 ) ( 1.738848e+01 5.509758e+01 ) ( 1.745562e+01 5.509956e+01 ) ( 1.745563e+01 5.509956e+01 ) ( 1.755269e+01 5.510238e+01 ) ( 1.754074e+01 5.506522e+01 ) ( 1.754073e+01 5.506521e+01 ) ( 1.753442e+01 5.50452e+01 ) ( 1.752893e+01 5.503915e+01 ) ( 1.752878e+01 5.503898e+01 ) ( 1.752858e+01 5.503871e+01 ) ( 1.752841e+01 5.503843e+01 ) ( 1.752827e+01 5.503815e+01 ) ( 1.752816e+01 5.503786e+01 ) ( 1.752809e+01 5.503757e+01 ) ( 1.752805e+01 5.503727e+01 ) ( 1.752804e+01 5.503698e+01 ) ( 1.752807e+01 5.503669e+01 ) ( 1.75281e+01 5.503655e+01 ) ( 1.753513e+01 5.500209e+01 ) ( 1.73133e+01 5.50409e+01 ) ( 1.730485e+01 5.504237e+01 ) ) ) ] ;
    schema:name "Baltica 3 OWF" ;
    schema:sameAs <https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.272> ;
    owf:areaSqKm 100.759 ;
    owf:locationMethod "outer way 1560193204 of the OSM element" ;
    owf:locationStatus owf:LocationSourceProvided ;
    owf:operatorName "PGE / Ørsted" ;
    owf:sourceDataset "OpenStreetMap" ;
    owf:sourceSnapshotDate "2026-10-27"^^xsd:date ;
    owf:sourceType owf:OpenStreetMapSource .

[] a geojson:FeatureCollection ;
    geojson:features <https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.268>,
        <https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.270>,
        <https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.272>,
        <https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.275>,
        <https://ows.emodnet-humanactivities.eu/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=emodnet:windfarms&featureID=windfarms.276>,
        <https://www.nve.no/energi/energisystem/vindkraft-paa-land/data-for-utbygde-vindkraftverk-i-norge/vindkraftverk-sider/vindkraftverk/?id=9591>,
        <https://www.openstreetmap.org/relation/21402440>,
        <https://www.openstreetmap.org/relation/21409512>,
        <https://www.openstreetmap.org/relation/21409513>,
        <https://www.openstreetmap.org/relation/21410256>,
        <https://www.openstreetmap.org/way/1560193204>,
        <urn:baltic-ses:national:1:example-project> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Windfarm designated area
description: 'A wind farm as a designated area or project, without its individual
  devices (turbines, substations, cables). A single GeoJSON Feature or a FeatureCollection
  of such features. Property names extend the EMODnet Human Activities windfarm attributes
  with the windpark parameters found in OpenStreetMap, the Norwegian NVE register,
  and the Polish national pipeline. Values a source does not state are null.

  '
anyOf:
- $ref: '#/$defs/WindfarmArea'
- $ref: '#/$defs/WindfarmAreaCollection'
$defs:
  nullableString:
    type:
    - string
    - 'null'
  nullableUri:
    type:
    - string
    - 'null'
    format: uri
  WindfarmAreaCollection:
    allOf:
    - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/schema.yaml
    - type: object
      required:
      - features
      properties:
        features:
          type: array
          items:
            $ref: '#/$defs/WindfarmArea'
          x-jsonld-id: https://purl.org/geojson/vocab#features
          x-jsonld-container: '@set'
  WindfarmArea:
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
          description: Identifier of the source record, e.g. an OSM element URL or
            an EMODnet WFS feature URL.
          x-jsonld-id: '@id'
        geometry:
          oneOf:
          - type: 'null'
          - type: object
            required:
            - type
            - coordinates
            properties:
              type:
                enum:
                - Polygon
                - MultiPolygon
                - Point
                x-jsonld-id: '@type'
          x-jsonld-id: https://purl.org/geojson/vocab#geometry
        properties:
          type: object
          required:
          - name
          - country
          - status
          - source_type
          - source_reference
          - location_status
          properties:
            name:
              $ref: '#/$defs/nullableString'
              description: Wind farm name as reported by the source.
              x-jsonld-id: https://schema.org/name
            country:
              $ref: '#/$defs/nullableString'
              description: Country name, as used by EMODnet (e.g. "Poland"); null
                when the source does not state it.
              x-jsonld-id: https://schema.org/addressCountry
              x-jsonld-type: '@vocab'
            n_turbines:
              type:
              - integer
              - 'null'
              minimum: 0
              description: Number of turbines in the wind farm (a count, not the devices
                themselves).
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#nTurbines
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
            power_mw:
              type:
              - number
              - 'null'
              minimum: 0
              description: Installed or planned capacity of the wind farm in MW.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#powerMW
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
            status:
              enum:
              - Planned
              - Approved
              - Construction
              - Production
              - Dismantled
              - null
              description: Project status using the EMODnet status vocabulary.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#conditionOfFacility
              x-jsonld-type: '@vocab'
            status_detail:
              $ref: '#/$defs/nullableString'
              description: Status wording or tag as given by the source, before normalisation.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#statusDetail
            status_as_of:
              type:
              - string
              - 'null'
              format: date
              description: Date on which the status was reported.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#statusAsOf
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
            type_inst:
              $ref: '#/$defs/nullableString'
              description: Foundation / installation type as published by EMODnet
                (e.g. Grounded, Floating).
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#installationType
            offshore:
              type:
              - boolean
              - 'null'
              description: Whether the wind farm is offshore.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#offshore
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
            year:
              $ref: '#/$defs/nullableString'
              description: Year associated with the project; see year_semantics for
                its meaning.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#year
            year_semantics:
              $ref: '#/$defs/nullableString'
              description: What the year represents, e.g. reported project year or
                planned start of operation.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#yearSemantics
            year_is_assumed:
              type:
              - boolean
              - 'null'
              description: True when the year is an estimate rather than an explicit
                source statement.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#yearIsAssumed
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
            updateyear:
              $ref: '#/$defs/nullableString'
              description: Year the source record was last updated (EMODnet updateyear).
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#updateYear
            operational_date:
              type:
              - string
              - 'null'
              format: date
              description: Date the wind farm entered operation.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#operationalDate
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
            dist_coast:
              type:
              - number
              - 'null'
              minimum: 0
              description: Distance to the coast in metres, as published by EMODnet.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#distanceToCoast
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
            area_sqkm:
              type:
              - number
              - 'null'
              minimum: 0
              description: "Area of the designated area polygon in km\xB2."
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#areaSqKm
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
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
            owner:
              $ref: '#/$defs/nullableString'
              description: Owning organisation.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#ownerName
            developer:
              $ref: '#/$defs/nullableString'
              description: Developing organisation.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#developerName
            licence_status:
              $ref: '#/$defs/nullableString'
              description: Licensing status as worded by the licensing authority,
                independent of the operational status.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#licenceStatus
            licensing_case:
              $ref: '#/$defs/nullableUri'
              description: URI of the licensing case.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#licensingCase
              x-jsonld-type: '@id'
            admin_units:
              type:
              - array
              - 'null'
              items:
                type: string
              description: Administrative units (counties, municipalities) the wind
                farm lies in.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#administrativeUnit
              x-jsonld-container: '@set'
            electricity_price_area:
              $ref: '#/$defs/nullableString'
              description: Electricity price (bidding) area.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#electricityPriceArea
            mean_annual_production_gwh:
              type:
              - number
              - 'null'
              minimum: 0
              description: Mean annual electrical production in GWh.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#meanAnnualProductionGWh
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
            notes:
              $ref: '#/$defs/nullableString'
              x-jsonld-id: http://purl.org/dc/terms/description
            source_type:
              enum:
              - osm
              - emodnet
              - national
              description: Kind of source the record comes from.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#sourceType
              x-jsonld-type: '@vocab'
            source_dataset:
              $ref: '#/$defs/nullableString'
              description: Name of the source dataset.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#sourceDataset
            source_reference:
              type: string
              format: uri
              description: URI of the source service, dataset, or publication.
              x-jsonld-id: http://purl.org/dc/terms/source
              x-jsonld-type: '@id'
            source_record_id:
              $ref: '#/$defs/nullableString'
              description: Identifier of the record in the source dataset.
              x-jsonld-id: http://purl.org/dc/terms/identifier
            source_snapshot_date:
              type:
              - string
              - 'null'
              format: date
              description: Date the source snapshot was retrieved.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#sourceSnapshotDate
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
            last_updated:
              type:
              - string
              - 'null'
              format: date-time
              description: Time of the last edit of the source record.
              x-jsonld-id: http://purl.org/dc/terms/modified
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
            location_status:
              enum:
              - source-provided
              - mapped
              - anticipated
              - unmatched
              description: How the geometry was obtained; unmatched when geometry
                is null.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#locationStatus
              x-jsonld-type: '@vocab'
            location_method:
              $ref: '#/$defs/nullableString'
              description: How the geometry was obtained or why it is missing.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#locationMethod
            location_reference:
              $ref: '#/$defs/nullableUri'
              description: URI of a source supporting the location.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/windfarm#locationReference
              x-jsonld-type: '@id'
            same_as:
              type:
              - array
              - 'null'
              items:
                type: string
                format: uri
              description: Other records (in this or other sources) describing the
                same wind farm.
              x-jsonld-id: https://schema.org/sameAs
              x-jsonld-type: '@id'
              x-jsonld-container: '@set'
          additionalProperties: false
          x-jsonld-id: '@nest'
x-jsonld-extra-terms:
  FeatureCollection: https://purl.org/geojson/vocab#FeatureCollection
  Feature: https://purl.org/geojson/vocab#Feature
  Point: https://purl.org/geojson/vocab#Point
  Polygon: https://purl.org/geojson/vocab#Polygon
  MultiPolygon: https://purl.org/geojson/vocab#MultiPolygon
  coordinates:
    x-jsonld-id: https://purl.org/geojson/vocab#coordinates
    x-jsonld-container: '@list'
  WindfarmArea: https://w3id.org/ogc/hosted/seadots/windfarm#WindfarmArea
  osm: https://w3id.org/ogc/hosted/seadots/windfarm#OpenStreetMapSource
  emodnet: https://w3id.org/ogc/hosted/seadots/windfarm#EmodnetSource
  national: https://w3id.org/ogc/hosted/seadots/windfarm#NationalSource
  source-provided: https://w3id.org/ogc/hosted/seadots/windfarm#LocationSourceProvided
  mapped: https://w3id.org/ogc/hosted/seadots/windfarm#LocationMapped
  anticipated: https://w3id.org/ogc/hosted/seadots/windfarm#LocationAnticipated
  unmatched: https://w3id.org/ogc/hosted/seadots/windfarm#LocationUnmatched
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/emodnet/
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  owf: https://w3id.org/ogc/hosted/seadots/windfarm#
  schema: https://schema.org/
  xsd: http://www.w3.org/2001/XMLSchema#
  dcterms: http://purl.org/dc/terms/
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.windfarms.common-windfarm-designated-area
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.2'
  dateOfLastChange: '2026-11-04'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/common-windfarm-designated-area/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/common-windfarm-designated-area/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/emodnet/",
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
    "coordinates": {
      "@id": "geojson:coordinates",
      "@container": "@list"
    },
    "WindfarmArea": "owf:WindfarmArea",
    "osm": "owf:OpenStreetMapSource",
    "emodnet": "owf:EmodnetSource",
    "national": "owf:NationalSource",
    "source-provided": "owf:LocationSourceProvided",
    "mapped": "owf:LocationMapped",
    "anticipated": "owf:LocationAnticipated",
    "unmatched": "owf:LocationUnmatched",
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "owf": "https://w3id.org/ogc/hosted/seadots/windfarm#",
    "schema": "https://schema.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "name": "schema:name",
    "country": {
      "@id": "schema:addressCountry",
      "@type": "@vocab"
    },
    "n_turbines": {
      "@id": "owf:nTurbines",
      "@type": "xsd:integer"
    },
    "power_mw": {
      "@id": "owf:powerMW",
      "@type": "xsd:decimal"
    },
    "status": {
      "@id": "owf:conditionOfFacility",
      "@type": "@vocab"
    },
    "status_detail": "owf:statusDetail",
    "status_as_of": {
      "@id": "owf:statusAsOf",
      "@type": "xsd:date"
    },
    "type_inst": "owf:installationType",
    "offshore": {
      "@id": "owf:offshore",
      "@type": "xsd:boolean"
    },
    "year": "owf:year",
    "year_semantics": "owf:yearSemantics",
    "year_is_assumed": {
      "@id": "owf:yearIsAssumed",
      "@type": "xsd:boolean"
    },
    "updateyear": "owf:updateYear",
    "operational_date": {
      "@id": "owf:operationalDate",
      "@type": "xsd:date"
    },
    "dist_coast": {
      "@id": "owf:distanceToCoast",
      "@type": "xsd:decimal"
    },
    "area_sqkm": {
      "@id": "owf:areaSqKm",
      "@type": "xsd:decimal"
    },
    "operator": {
      "@id": "owf:operatorName",
      "@container": "@set"
    },
    "owner": "owf:ownerName",
    "developer": "owf:developerName",
    "licence_status": "owf:licenceStatus",
    "licensing_case": {
      "@id": "owf:licensingCase",
      "@type": "@id"
    },
    "admin_units": {
      "@id": "owf:administrativeUnit",
      "@container": "@set"
    },
    "electricity_price_area": "owf:electricityPriceArea",
    "mean_annual_production_gwh": {
      "@id": "owf:meanAnnualProductionGWh",
      "@type": "xsd:decimal"
    },
    "notes": "dct:description",
    "source_type": {
      "@id": "owf:sourceType",
      "@type": "@vocab"
    },
    "source_dataset": "owf:sourceDataset",
    "source_reference": {
      "@id": "dct:source",
      "@type": "@id"
    },
    "source_record_id": "dct:identifier",
    "source_snapshot_date": {
      "@id": "owf:sourceSnapshotDate",
      "@type": "xsd:date"
    },
    "last_updated": {
      "@id": "dct:modified",
      "@type": "xsd:dateTime"
    },
    "location_status": {
      "@id": "owf:locationStatus",
      "@type": "@vocab"
    },
    "location_method": "owf:locationMethod",
    "location_reference": {
      "@id": "owf:locationReference",
      "@type": "@id"
    },
    "same_as": {
      "@id": "schema:sameAs",
      "@type": "@id",
      "@container": "@set"
    },
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/common-windfarm-designated-area/context.jsonld)

## Sources

* [EMODnet Human Activities — Wind Farms service](https://www.emodnet-humanactivities.eu/)
* [OpenStreetMap power plant tagging](https://wiki.openstreetmap.org/wiki/Tag:power%3Dplant)
* [NVE wind power plants dataset](https://data.norge.no/nb/datasets/363af211-1914-3814-a365-8439d12466cf/vindkraftverk)
* [IHO windfarm definition in S-100](https://registry.iho.int/fdd/view1.do?idx=798&type=1)
* [EU Publications Office Country authority table](http://publications.europa.eu/resource/authority/country/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/windfarms/common-windfarm-designated-area`

