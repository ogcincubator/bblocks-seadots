
# EMODnet windfarm harmonized project extension (Schema)

`ogc.hosted.seadots.emodnet-compliant-windfarm.baltic-project-extension` *v0.1*

Canonical GeoJSON-LD windfarm feature combining all EMODnet windfarm fields with generic project, national reporting, provenance, and explicit location-crosswalk information. It supports raw EMODnet points and national-source records, including unmapped records with null geometry.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# EMODnet windfarm harmonized project extension

This Building Block translates Baltic national windfarm pipeline records and EMODnet windfarm records into the EMODnet-compliant windfarm property vocabulary. The shared fields retain the base block names (`power_mw`, `status`, `year`, `updateyear`, `n_turbines`, `type_inst`, `dist_coast`, and `notes`). The extension adds generic fields for project name and developer, the reporting date and meaning of a year, and dataset and record provenance.

Input-specific column labels are not carried into the harmonized output. Their values are translated. For example, a national `capacity_mw` value becomes `power_mw`; a source status such as `In planning (auction...)` becomes the normalized controlled status `Planned`, while its full wording is retained in `status_detail`; and `status_aug2026` is represented by generic `status`, `status_detail`, `status_as_of`, and `updateyear` properties.

The schema accepts complete EMODnet base features or sparse harmonized features. This is intentionally not declared as a strict profile of the base block: national pipeline sources do not provide every required EMODnet attribute. `dist_coast` is expressed in metres, matching the EMODnet input field. Location status and reference terms distinguish source-provided geometry, EMODnet-mapped locations, approximate public-source locations, and unmatched records.


The target also carries `source_type`, `location_status`, `location_method`, and `location_emodnet_ids`. A national location derived from one or more EMODnet sites is represented by that site or their centroid, with the crosswalk IDs and method retained. A national project without an identifiable EMODnet location remains `geometry: null` and `location_status: unmatched`.

## Examples

### Harmonized national pipeline record
National source values translated to EMODnet property names and generic extension fields. Geometry is null because the source has no coordinates.
#### json
```json
{
  "id": "urn:baltic-ses:national:1:example-project",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "name": "Example Baltic Wind",
    "country": "Poland",
    "n_turbines": null,
    "power_mw": 1200,
    "status": "Planned",
    "type_inst": null,
    "updateyear": "2026",
    "year": "2028",
    "dist_coast": null,
    "notes": "Year reported as assumed in the source.",
    "developer": "Example Energy",
    "status_detail": "In planning (auction pathway)",
    "status_as_of": "2026-08-26",
    "year_semantics": "planned first-power or completion year",
    "year_is_assumed": true,
    "source_dataset": "Polish national offshore wind project pipeline",
    "source_reference": "https://www.gramwzielone.pl/?p=20373718",
    "source_snapshot_date": "2026-08-26",
    "source_record_id": "national-1"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension/context.jsonld",
  "id": "urn:baltic-ses:national:1:example-project",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "name": "Example Baltic Wind",
    "country": "Poland",
    "n_turbines": null,
    "power_mw": 1200,
    "status": "Planned",
    "type_inst": null,
    "updateyear": "2026",
    "year": "2028",
    "dist_coast": null,
    "notes": "Year reported as assumed in the source.",
    "developer": "Example Energy",
    "status_detail": "In planning (auction pathway)",
    "status_as_of": "2026-08-26",
    "year_semantics": "planned first-power or completion year",
    "year_is_assumed": true,
    "source_dataset": "Polish national offshore wind project pipeline",
    "source_reference": "https://www.gramwzielone.pl/?p=20373718",
    "source_snapshot_date": "2026-08-26",
    "source_record_id": "national-1"
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix em: <https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix schema: <https://schema.org/> .
@prefix seadots-emodnet: <https://w3id.org/ogc/hosted/seadots/emodnet/> .
@prefix ses: <https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<urn:baltic-ses:national:1:example-project> a geojson:Feature ;
    geojson:properties [ dcterms:description "Year reported as assumed in the source." ;
            schema:addressCountry <http://publications.europa.eu/resource/authority/country/POL> ;
            schema:creator "Example Energy" ;
            schema:name "Example Baltic Wind" ;
            em:powerMW 1200 ;
            em:updateYear "2026" ;
            em:year "2028" ;
            ses:sourceDataset "Polish national offshore wind project pipeline" ;
            ses:sourceRecordId "national-1" ;
            ses:sourceReference <https://www.gramwzielone.pl/?p=20373718> ;
            ses:sourceSnapshotDate "2026-08-26"^^xsd:date ;
            ses:statusAsOf "2026-08-26"^^xsd:date ;
            ses:statusDetail "In planning (auction pathway)" ;
            ses:yearIsAssumed true ;
            ses:yearSemantics "planned first-power or completion year" ;
            seadots-emodnet: seadots-emodnet:Planned ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EMODnet windfarm harmonized project extension
description: A harmonized GeoJSON Feature using the EMODnet windfarm property vocabulary,
  augmented with generic project, reporting-time, year-semantics, and provenance fields.
  It accepts complete base-block features and sparse national pipeline records with
  null geometry. It is an aligned extension, not a strict profile of the base block
  because national records may not provide the base attributes.
anyOf:
- $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-compliant-windfarm/schema.yaml
- $ref: '#/$defs/sparseFeature'
$defs:
  sparseFeature:
    type: object
    required:
    - id
    - type
    - geometry
    - properties
    properties:
      id:
        type: string
        format: uri
        x-jsonld-id: '@id'
      type:
        const: Feature
        x-jsonld-id: '@type'
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
              - Point
              - Polygon
              - MultiPolygon
              x-jsonld-id: '@type'
            coordinates: {}
          additionalProperties: true
        x-jsonld-id: https://purl.org/geojson/vocab#geometry
      properties:
        type: object
        required:
        - name
        - country
        - power_mw
        - status
        - source_type
        - source_dataset
        - source_reference
        - source_snapshot_date
        - location_status
        properties:
          name:
            type: string
            x-jsonld-id: https://schema.org/name
          country:
            type: string
            x-jsonld-id: https://schema.org/addressCountry
            x-jsonld-type: '@vocab'
          n_turbines:
            type:
            - number
            - 'null'
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#nTurbines
          power_mw:
            type:
            - number
            - 'null'
            minimum: 0
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#powerMW
          status:
            oneOf:
            - type: string
              enum:
              - Planned
              - Production
              - Dismantled
              - Approved
              - Construction
            - type: 'null'
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet/
            x-jsonld-type: '@vocab'
          type_inst:
            type:
            - string
            - 'null'
            x-jsonld-id: https://schema.org/additionalType
          updateyear:
            type:
            - string
            - 'null'
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#updateYear
          year:
            type:
            - string
            - 'null'
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#year
          dist_coast:
            type:
            - number
            - 'null'
            minimum: 0
            description: Distance to coast in metres
            as in the EMODnet source field.: null
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#distanceToCoast
          notes:
            type:
            - string
            - 'null'
            x-jsonld-id: http://purl.org/dc/terms/description
          developer:
            type:
            - string
            - 'null'
            x-jsonld-id: https://schema.org/creator
          status_detail:
            type:
            - string
            - 'null'
            description: Source-reported status text before normalization.
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#statusDetail
          status_as_of:
            type:
            - string
            - 'null'
            format: date
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#statusAsOf
            x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
          year_semantics:
            type:
            - string
            - 'null'
            description: Meaning of the year value
            such as reported year or planned first-power/completion year.: null
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#yearSemantics
          year_is_assumed:
            type:
            - boolean
            - 'null'
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#yearIsAssumed
            x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
          source_type:
            type: string
            enum:
            - national
            - emodnet
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#sourceType
          source_dataset:
            type: string
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#sourceDataset
          source_reference:
            type: string
            format: uri
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#sourceReference
            x-jsonld-type: '@id'
          source_snapshot_date:
            type: string
            format: date
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#sourceSnapshotDate
            x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
          source_record_id:
            type:
            - string
            - 'null'
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#sourceRecordId
          location_status:
            type: string
            enum:
            - source-provided
            - mapped
            - anticipated
            - unmatched
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#locationStatus
          location_method:
            type:
            - string
            - 'null'
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#locationMethod
          location_reference:
            type:
            - string
            - 'null'
            format: uri
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#locationReference
            x-jsonld-type: '@id'
          location_emodnet_ids:
            type: array
            items:
              type: string
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#locationEmodnetIds
            x-jsonld-container: '@set'
        additionalProperties: false
        x-jsonld-id: https://purl.org/geojson/vocab#properties
    additionalProperties: false
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
  FeatureCollection: https://purl.org/geojson/vocab#FeatureCollection
  features:
    x-jsonld-id: https://purl.org/geojson/vocab#features
    x-jsonld-container: '@set'
  Poland: http://publications.europa.eu/resource/authority/country/POL
  MatchCandidate: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#MatchCandidate
  source_record:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#sourceRecord
    x-jsonld-type: '@id'
  target_record:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#targetRecord
    x-jsonld-type: '@id'
  match_method: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#matchMethod
  name_score:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#nameSimilarity
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  property_score:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#propertyAgreement
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  candidate_rank_score:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#candidateRankScore
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  capacity_similarity:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#capacitySimilarity
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  capacity_delta_mw:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#capacityDifferenceMW
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  status_match:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#statusMatch
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
  year_match:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#yearMatch
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
  distance_km:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#distanceKm
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  schema: https://schema.org/
  em: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#
  dcterms: http://purl.org/dc/terms/
  ses: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#
  seadots-emodnet: https://w3id.org/ogc/hosted/seadots/emodnet/
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.emodnet-compliant-windfarm.baltic-project-extension
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-27'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension/schema.yaml)


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
        "developer": "schema:creator",
        "status_detail": "ses:statusDetail",
        "status_as_of": {
          "@id": "ses:statusAsOf",
          "@type": "http://www.w3.org/2001/XMLSchema#date"
        },
        "year_semantics": "ses:yearSemantics",
        "year_is_assumed": {
          "@id": "ses:yearIsAssumed",
          "@type": "http://www.w3.org/2001/XMLSchema#boolean"
        },
        "source_type": "ses:sourceType",
        "source_dataset": "ses:sourceDataset",
        "source_reference": {
          "@id": "ses:sourceReference",
          "@type": "@id"
        },
        "source_snapshot_date": {
          "@id": "ses:sourceSnapshotDate",
          "@type": "http://www.w3.org/2001/XMLSchema#date"
        },
        "source_record_id": "ses:sourceRecordId",
        "location_status": "ses:locationStatus",
        "location_method": "ses:locationMethod",
        "location_reference": {
          "@id": "ses:locationReference",
          "@type": "@id"
        },
        "location_emodnet_ids": {
          "@id": "ses:locationEmodnetIds",
          "@container": "@set"
        }
      },
      "@id": "geojson:properties"
    },
    "FeatureCollection": "geojson:FeatureCollection",
    "features": {
      "@id": "geojson:features",
      "@container": "@set"
    },
    "Poland": "http://publications.europa.eu/resource/authority/country/POL",
    "MatchCandidate": "ses:MatchCandidate",
    "source_record": {
      "@id": "ses:sourceRecord",
      "@type": "@id"
    },
    "target_record": {
      "@id": "ses:targetRecord",
      "@type": "@id"
    },
    "match_method": "ses:matchMethod",
    "name_score": {
      "@id": "ses:nameSimilarity",
      "@type": "http://www.w3.org/2001/XMLSchema#decimal"
    },
    "property_score": {
      "@id": "ses:propertyAgreement",
      "@type": "http://www.w3.org/2001/XMLSchema#decimal"
    },
    "candidate_rank_score": {
      "@id": "ses:candidateRankScore",
      "@type": "http://www.w3.org/2001/XMLSchema#decimal"
    },
    "capacity_similarity": {
      "@id": "ses:capacitySimilarity",
      "@type": "http://www.w3.org/2001/XMLSchema#decimal"
    },
    "capacity_delta_mw": {
      "@id": "ses:capacityDifferenceMW",
      "@type": "http://www.w3.org/2001/XMLSchema#decimal"
    },
    "status_match": {
      "@id": "ses:statusMatch",
      "@type": "http://www.w3.org/2001/XMLSchema#boolean"
    },
    "year_match": {
      "@id": "ses:yearMatch",
      "@type": "http://www.w3.org/2001/XMLSchema#boolean"
    },
    "distance_km": {
      "@id": "ses:distanceKm",
      "@type": "http://www.w3.org/2001/XMLSchema#decimal"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "schema": "https://schema.org/",
    "seadots": "https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#",
    "dcterms": "http://purl.org/dc/terms/",
    "seadots-emodnet": "https://w3id.org/ogc/hosted/seadots/emodnet/",
    "inspire-cofv": "http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/",
    "em": "https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#",
    "ses": "https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-compliant-windfarm/baltic-project-extension/context.jsonld)

## Sources

* [EMODnet-compliant windfarm Building Block](https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm)
* [Polish offshore wind pipeline article](https://www.gramwzielone.pl/?p=20373718)
* [EMODnet Human Activities WFS](https://ows.emodnet-humanactivities.eu/wfs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/emodnet-compliant-windfarm/baltic-project-extension`

