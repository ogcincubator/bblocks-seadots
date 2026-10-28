
# Norwegian NVE windfarm extension for EMODnet (Schema)

`ogc.hosted.seadots.emodnet-compliant-windfarm-no` *v0.1*

Example profile that maps a Norwegian Water Resources and Energy Directorate (NVE) windfarm record to the EMODnet windfarm model and preserves Norway-specific licensing, ownership, production, and turbine details.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Norwegian NVE windfarm extension for EMODnet

This block profiles the [EMODnet windfarm model](../emodnet-compliant-windfarm/)
for an example record from the Norwegian Water Resources and Energy Directorate
(NVE) wind power plant dataset. It demonstrates mapping national fields into the
shared EMODnet properties while keeping useful Norwegian source details.

The NVE dataset covers licensed wind power plants and facilities that have been
or are being processed by NVE. It is a **land-based wind power dataset**. This
example therefore shows reuse of the EMODnet windfarm vocabulary for Norwegian
national data; it does not claim that the Smøla facility is an offshore
EMODnet record.

## Mapping in the example

The example uses NVE's Smøla facility detail page and its associated licensing
case. NVE reports 66 operative turbines, maximum power of 145.8 MW, mean annual
production of 316.9 GWh, the owner, administrative areas, price area, and
turbine models. These map to EMODnet `n_turbines`, `power_mw`, `status`,
`country`, and `year` where the source has a comparable value. NVE's original
licensing status (`Konsesjon gitt`) is retained separately from the mapped
operating status (`Production`), since a licence decision and a facility's
operating state describe different things.

The NVE facility page provides details but not a GeoJSON geometry. Accordingly,
the worked example has `geometry: null`; the NVE windfarm GIS distribution must
provide the geometry for a mapped feature. `dist_coast` and `type_inst` are also
null because this onshore source does not provide equivalent EMODnet offshore
values.

The extension fields retain NVE's facility identifier, licence status,
operational date, owner, counties, municipalities, price area, mean annual
production, turbine details, and links to the facility and licensing records.

## Sources

- [NVE Windkraftverk dataset](https://data.norge.no/nb/datasets/363af211-1914-3814-a365-8439d12466cf/vindkraftverk)
- [NVE Smøla windfarm details](https://www.nve.no/energi/energisystem/vindkraft-paa-land/data-for-utbygde-vindkraftverk-i-norge/vindkraftverk-sider/vindkraftverk/?id=9591)
- [NVE Smøla licensing case](https://www.nve.no/konsesjon/konsesjonssaker/konsesjonssak?id=3&type=A)

## Examples

### NVE Smøla windfarm mapped to EMODnet with Norwegian source extension
Worked Norway example. EMODnet properties carry the mapped country, operating status, turbine count, capacity, and year. The extension retains NVE's licensing status, owner, production, administrative areas, and turbine details. The NVE facility has GIS geometry, but it is omitted from this page-derived example and must be taken from the NVE spatial download before using the record as a mapped feature.
#### json
```json
{
  "id": "https://example.org/wind-farms/north-sea-demo-01",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [4.9000, 54.2000],
      [4.9800, 54.2000],
      [4.9800, 54.2600],
      [4.9000, 54.2600],
      [4.9000, 54.2000]
    ]]
  },

  "properties": {
    "title": "North Sea Demonstrator Offshore Wind Farm",
    "description": "Illustrative EMODnet Human Activities contribution record for an operational offshore wind-farm field.",
    "windFarm": {
      "identifier": "NS-DEMO-01",
      "name": "North Sea Demonstrator Offshore Wind Farm",
      "country": "NL",
      "lifecycleStatus": "operational",
      "turbineCount": 24,
      "installedCapacityMW": 288,
      "validFrom": "2025-01-01",
      "commissioningDate": "2025-01-01",
      "operator": "Example Offshore Energy B.V.",
      "sourceDataset": "https://example.org/datasets/north-sea-demo-wind-farm.geojson",
      "metadataRecord": "https://example.org/metadata/north-sea-demo-wind-farm",
      "updateDate": "2026-07-01",
      "positionalAccuracyM": 10,
      "remarks": "Illustrative record; replace all example URLs and values with the authoritative provider data and metadata record before publication."
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-compliant-windfarm-no/context.jsonld",
  "id": "https://example.org/wind-farms/north-sea-demo-01",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          4.9,
          54.2
        ],
        [
          4.98,
          54.2
        ],
        [
          4.98,
          54.26
        ],
        [
          4.9,
          54.26
        ],
        [
          4.9,
          54.2
        ]
      ]
    ]
  },
  "properties": {
    "title": "North Sea Demonstrator Offshore Wind Farm",
    "description": "Illustrative EMODnet Human Activities contribution record for an operational offshore wind-farm field.",
    "windFarm": {
      "identifier": "NS-DEMO-01",
      "name": "North Sea Demonstrator Offshore Wind Farm",
      "country": "NL",
      "lifecycleStatus": "operational",
      "turbineCount": 24,
      "installedCapacityMW": 288,
      "validFrom": "2025-01-01",
      "commissioningDate": "2025-01-01",
      "operator": "Example Offshore Energy B.V.",
      "sourceDataset": "https://example.org/datasets/north-sea-demo-wind-farm.geojson",
      "metadataRecord": "https://example.org/metadata/north-sea-demo-wind-farm",
      "updateDate": "2026-07-01",
      "positionalAccuracyM": 10,
      "remarks": "Illustrative record; replace all example URLs and values with the authoritative provider data and metadata record before publication."
    }
  }
}
```

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix seadots-emodnet: <https://w3id.org/ogc/hosted/seadots/emodnet/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/wind-farms/north-sea-demo-01> a geojson:Feature ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 4.9e+00 5.42e+01 ) ( 4.98e+00 5.42e+01 ) ( 4.98e+00 5.426e+01 ) ( 4.9e+00 5.426e+01 ) ( 4.9e+00 5.42e+01 ) ) ) ] ;
    geojson:properties [ seadots-emodnet:description "Illustrative EMODnet Human Activities contribution record for an operational offshore wind-farm field." ;
            seadots-emodnet:title "North Sea Demonstrator Offshore Wind Farm" ;
            seadots-emodnet:windFarm [ schema:addressCountry seadots-emodnet:NL ;
                    schema:name "North Sea Demonstrator Offshore Wind Farm" ;
                    seadots-emodnet:commissioningDate "2025-01-01" ;
                    seadots-emodnet:identifier "NS-DEMO-01" ;
                    seadots-emodnet:installedCapacityMW 288 ;
                    seadots-emodnet:lifecycleStatus "operational" ;
                    seadots-emodnet:metadataRecord "https://example.org/metadata/north-sea-demo-wind-farm" ;
                    seadots-emodnet:operator "Example Offshore Energy B.V." ;
                    seadots-emodnet:positionalAccuracyM 10 ;
                    seadots-emodnet:remarks "Illustrative record; replace all example URLs and values with the authoritative provider data and metadata record before publication." ;
                    seadots-emodnet:sourceDataset "https://example.org/datasets/north-sea-demo-wind-farm.geojson" ;
                    seadots-emodnet:turbineCount 24 ;
                    seadots-emodnet:updateDate "2026-07-01" ;
                    seadots-emodnet:validFrom "2025-01-01" ] ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Norwegian NVE windfarm extension for EMODnet
description: EMODnet windfarm feature extended with fields from the Norwegian NVE
  wind power plant dataset. NVE licensing status and facility details remain available
  alongside the mapped EMODnet attributes.
allOf:
- $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-compliant-windfarm/schema.yaml
- type: object
  required:
  - properties
  properties:
    properties:
      type: object
      required:
      - name
      - nve_facility_id
      - nve_licence_status
      - nve_operational_date
      - nve_owner
      - nve_mean_annual_production_gwh
      - nve_price_area
      - nve_turbine_details
      - nve_source_record
      properties:
        name:
          type: string
          description: Facility name as published by NVE.
          x-jsonld-id: https://schema.org/name
        nve_facility_id:
          type: string
          description: Identifier in the NVE wind power plant facility pages.
          x-jsonld-id: http://purl.org/dc/terms/identifier
        nve_licence_status:
          type: string
          description: Original Norwegian licensing status, preserved without mapping
            to an operating status.
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm-no#licenceStatus
        nve_operational_date:
          type:
          - string
          - 'null'
          format: date
          description: Facility operation date reported by NVE, when available.
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm-no#operationalDate
          x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
        nve_owner:
          type: string
          description: Facility owner reported by NVE.
          x-jsonld-id: https://schema.org/owner
        nve_counties:
          type: array
          items:
            type: string
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm-no#county
          x-jsonld-container: '@set'
        nve_municipalities:
          type: array
          items:
            type: string
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm-no#municipality
          x-jsonld-container: '@set'
        nve_mean_annual_production_gwh:
          type:
          - number
          - 'null'
          minimum: 0
          description: Mean annual electrical production reported by NVE, in GWh.
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm-no#meanAnnualProductionGWh
        nve_price_area:
          type: string
          description: Norwegian electricity price area as reported by NVE.
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm-no#electricityPriceArea
        nve_turbine_details:
          type: array
          items:
            type: object
            required:
            - manufacturer
            - model
            - count
            - commissioning_year
            properties:
              manufacturer:
                type: string
                x-jsonld-id: https://schema.org/manufacturer
              model:
                type: string
                x-jsonld-id: https://schema.org/model
              count:
                type: integer
                minimum: 1
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm-no#turbineCount
              commissioning_year:
                type: integer
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm-no#commissioningYear
            additionalProperties: false
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm-no#turbineDetails
          x-jsonld-container: '@set'
        nve_source_record:
          type: string
          format: uri
          description: URI of the NVE facility record used for this feature.
          x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
          x-jsonld-type: '@id'
        nve_licensing_case:
          type:
          - string
          - 'null'
          format: uri
          description: URI of the NVE licensing case for this facility.
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm-no#licensingCase
          x-jsonld-type: '@id'
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm-no#
x-jsonld-prefixes:
  schema: https://schema.org/
  dcterms: http://purl.org/dc/terms/
  nve: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm-no#
  prov: http://www.w3.org/ns/prov#
  em: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.emodnet-compliant-windfarm-no
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-28'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-compliant-windfarm-no/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-compliant-windfarm-no/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/emodnet/",
    "Feature": "geojson:Feature",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "MultiPolygon": "geojson:MultiPolygon",
    "id": "@id",
    "type": "@type",
    "geometry": {
      "@context": {
        "coordinates": {
          "@id": "geojson:coordinates",
          "@container": "@list"
        }
      },
      "@id": "geojson:geometry"
    },
    "properties": {
      "@context": {
        "country": {
          "@id": "schema:addressCountry",
          "@type": "@vocab"
        },
        "n_turbines": "seadots:nTurbines",
        "power_mw": "seadots:powerMW",
        "status": {
          "@id": "https://w3id.org/ogc/hosted/seadots/emodnet/",
          "@type": "@vocab"
        },
        "type_inst": "schema:additionalType",
        "updateyear": "seadots:updateYear",
        "year": "seadots:year",
        "dist_coast": "seadots:distanceToCoast",
        "notes": "dcterms:description",
        "name": "schema:name",
        "nve_facility_id": "dcterms:identifier",
        "nve_licence_status": "nve:licenceStatus",
        "nve_operational_date": {
          "@id": "nve:operationalDate",
          "@type": "http://www.w3.org/2001/XMLSchema#date"
        },
        "nve_owner": "schema:owner",
        "nve_counties": {
          "@id": "nve:county",
          "@container": "@set"
        },
        "nve_municipalities": {
          "@id": "nve:municipality",
          "@container": "@set"
        },
        "nve_mean_annual_production_gwh": "nve:meanAnnualProductionGWh",
        "nve_price_area": "nve:electricityPriceArea",
        "nve_turbine_details": {
          "@context": {
            "manufacturer": "schema:manufacturer",
            "model": "schema:model",
            "count": "nve:turbineCount",
            "commissioning_year": "nve:commissioningYear"
          },
          "@id": "nve:turbineDetails",
          "@container": "@set"
        },
        "nve_source_record": {
          "@id": "prov:wasDerivedFrom",
          "@type": "@id"
        },
        "nve_licensing_case": {
          "@id": "nve:licensingCase",
          "@type": "@id"
        }
      },
      "@id": "geojson:properties"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "schema": "https://schema.org/",
    "seadots": "https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#",
    "dcterms": "http://purl.org/dc/terms/",
    "seadots-emodnet": "https://w3id.org/ogc/hosted/seadots/emodnet/",
    "inspire-cofv": "http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/",
    "nve": "https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm-no#",
    "prov": "http://www.w3.org/ns/prov#",
    "em": "https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-compliant-windfarm-no/context.jsonld)

## Sources

* [NVE wind power plants dataset](https://data.norge.no/nb/datasets/363af211-1914-3814-a365-8439d12466cf/vindkraftverk)
* [NVE Smøla wind farm record](https://www.nve.no/energi/energisystem/vindkraft-paa-land/data-for-utbygde-vindkraftverk-i-norge/vindkraftverk-sider/vindkraftverk/?id=9591)
* [NVE Smøla licensing case](https://www.nve.no/konsesjon/konsesjonssaker/konsesjonssak?id=3&type=A)
* [Base EMODnet windfarm block](https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/emodnet-compliant-windfarm-no`

