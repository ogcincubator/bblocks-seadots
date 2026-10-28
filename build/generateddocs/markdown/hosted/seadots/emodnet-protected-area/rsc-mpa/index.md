
# EMODnet-compliant Regional Sea Convention MPA (Schema)

`ogc.hosted.seadots.emodnet-protected-area.rsc-mpa` *v0.1*

GeoJSON Feature profile reproducing the attribute schema of the EMODnet Human Activities layer emodnet:marineprotectedareas (MPAs reported to the Regional Sea Conventions, rsc = HELCOM or OSPAR) with unchanged field names and types. Target profile for publishing HELCOM MPAs through OGC API - Features in EMODnet form.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# EMODnet-compliant Regional Sea Convention MPA

Target profile that reproduces the EMODnet Human Activities layer
`emodnet:marineprotectedareas`: MPAs as reported to the Regional Sea Conventions,
distinguished by `rsc` (`HELCOM` or `OSPAR`). For the Baltic Sea this is EMODnet's
representation of the HELCOM MPA network.

## Conformance rules beyond the JSON schema

1. **Complete attribute set, EMODnet names.** All 17 attributes are present and
   unknown values are `null`. No additional attributes are allowed.
2. **`code` is numeric.** EMODnet types `code` as `xsd:long`. HELCOM MPA database
   ids (e.g. `252`) qualify. Natura 2000 site codes (`LTSIU0012`), EEA site ids and
   national codes do not. Rows that carry those codes belong to other EMODnet layers
   (see the HELCOM source profile).
3. **Name goes in `name`.** EMODnet's HELCOM rows keep the site name in `name` and
   leave `orig_name` and `designatio` empty. The view does the same.
4. **HELCOM status vocabulary.** When `rsc = HELCOM`, `status` is one of
   *Designated and managed*, *Designated and partly managed* or *Designated*,
   exactly as HELCOM publishes it.
5. **Area fields stay empty for HELCOM** (`rep_area`, `gis_area`, …), as in EMODnet.
   A publisher that fills them must state the unit in the collection metadata,
   because EMODnet's own unit for these fields is undocumented.
6. **One feature per site** as a (Multi)Polygon in CRS84. `shape_leng` and `shape_area`
   are planar measures on the lon/lat coordinates.

Note: `DescribeFeatureType` for this layer lists `orig_name` but not `name`. However,
the GeoJSON and CSV `GetFeature` responses do include `name`, and it is the only
populated name field for HELCOM rows. This profile follows the actual responses.

## Examples

### Hatter Barn HELCOM MPA as published by EMODnet
A real record from the EMODnet Human Activities WFS (`rsc = HELCOM`, `code = 252`, retrieved 30 Sep 2026), used as the golden target for the HELCOM transform. Attribute values are verbatim; fields EMODnet leaves empty for HELCOM sites are null. The geometry is the site's WGS 84 bounding box, not the true boundary.

#### json
```json
{
  "type": "Feature",
  "id": 252,
  "geometry": {
    "type": "MultiPolygon",
    "coordinates": [
      [
        [
          [
            10.826701141116107,
            55.866699340329625
          ],
          [
            10.876702677777274,
            55.866699340329625
          ],
          [
            10.876702677777274,
            55.895498413889065
          ],
          [
            10.826701141116107,
            55.895498413889065
          ],
          [
            10.826701141116107,
            55.866699340329625
          ]
        ]
      ]
    ]
  },
  "properties": {
    "rsc": "HELCOM",
    "code": 252,
    "name": "Hatter Barn",
    "orig_name": null,
    "country": "Denmark",
    "designatio": null,
    "iucn_cat": null,
    "rep_m_area": null,
    "gis_m_area": null,
    "rep_area": null,
    "gis_area": null,
    "status": "Designated and managed",
    "status_yr": 2009,
    "mang_auth": null,
    "link": "http://mpas.helcom.fi/apex/f?p=103:12:::NO::P12_ID:252",
    "shape_leng": 0.12486362,
    "shape_area": 0.0009127
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/rsc-mpa/context.jsonld",
  "type": "Feature",
  "id": 252,
  "geometry": {
    "type": "MultiPolygon",
    "coordinates": [
      [
        [
          [
            10.826701141116107,
            55.866699340329625
          ],
          [
            10.876702677777274,
            55.866699340329625
          ],
          [
            10.876702677777274,
            55.895498413889065
          ],
          [
            10.826701141116107,
            55.895498413889065
          ],
          [
            10.826701141116107,
            55.866699340329625
          ]
        ]
      ]
    ]
  },
  "properties": {
    "rsc": "HELCOM",
    "code": 252,
    "name": "Hatter Barn",
    "orig_name": null,
    "country": "Denmark",
    "designatio": null,
    "iucn_cat": null,
    "rep_m_area": null,
    "gis_m_area": null,
    "rep_area": null,
    "gis_area": null,
    "status": "Designated and managed",
    "status_yr": 2009,
    "mang_auth": null,
    "link": "http://mpas.helcom.fi/apex/f?p=103:12:::NO::P12_ID:252",
    "shape_leng": 0.12486362,
    "shape_area": 0.0009127
  }
}
```

#### ttl
```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix pa: <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/252> a geojson:Feature ;
    foaf:page <http://mpas.helcom.fi/apex/f?p=103:12:::NO::P12_ID:252> ;
    geojson:geometry [ a geojson:MultiPolygon ;
            geojson:coordinates ( ( ( ( 1.08267e+01 5.58667e+01 ) ( 1.08767e+01 5.58667e+01 ) ( 1.08767e+01 5.58955e+01 ) ( 1.08267e+01 5.58955e+01 ) ( 1.08267e+01 5.58667e+01 ) ) ) ) ] ;
    pa:conventionSiteCode 252 ;
    pa:countryName "Denmark" ;
    pa:establishmentYear "2009"^^xsd:gYear ;
    pa:managementStatus "Designated and managed" ;
    pa:regionalSeaConvention <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/rsc/HELCOM> ;
    pa:shapeAreaSquareDegrees 9.127e-04 ;
    pa:shapeLengthDegrees 1.248636e-01 ;
    pa:siteName "Hatter Barn" .


```


### EMODnet reference records for HELCOM codes 252 and 239
The EMODnet marineprotectedareas records for Hatter Barn (252) and Jasmund National Park (239), retrieved 30 Sep 2026; golden targets of the HELCOM transform.

#### json
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 252,
      "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
          [
            [
              [
                10.826701141116107,
                55.866699340329625
              ],
              [
                10.876702677777274,
                55.866699340329625
              ],
              [
                10.876702677777274,
                55.895498413889065
              ],
              [
                10.826701141116107,
                55.895498413889065
              ],
              [
                10.826701141116107,
                55.866699340329625
              ]
            ]
          ]
        ]
      },
      "properties": {
        "rsc": "HELCOM",
        "code": 252,
        "name": "Hatter Barn",
        "orig_name": null,
        "country": "Denmark",
        "designatio": null,
        "iucn_cat": null,
        "rep_m_area": null,
        "gis_m_area": null,
        "rep_area": null,
        "gis_area": null,
        "status": "Designated and managed",
        "status_yr": 2009,
        "mang_auth": null,
        "link": "http://mpas.helcom.fi/apex/f?p=103:12:::NO::P12_ID:252",
        "shape_leng": 0.12486362,
        "shape_area": 0.0009127
      }
    },
    {
      "type": "Feature",
      "id": 239,
      "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
          [
            [
              [
                13.56584537567118,
                54.51825640887737
              ],
              [
                13.692069856216941,
                54.51825640887737
              ],
              [
                13.692069856216941,
                54.5919557374847
              ],
              [
                13.56584537567118,
                54.5919557374847
              ],
              [
                13.56584537567118,
                54.51825640887737
              ]
            ]
          ]
        ]
      },
      "properties": {
        "rsc": "HELCOM",
        "code": 239,
        "name": "Jasmund National Park",
        "orig_name": null,
        "country": "Germany",
        "designatio": null,
        "iucn_cat": null,
        "rep_m_area": null,
        "gis_m_area": null,
        "rep_area": null,
        "gis_area": null,
        "status": "Designated and managed",
        "status_yr": 1996,
        "mang_auth": null,
        "link": "http://mpas.helcom.fi/apex/f?p=103:12:::NO::P12_ID:239",
        "shape_leng": 0.60600583,
        "shape_area": 0.00431054
      }
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/rsc-mpa/context.jsonld",
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 252,
      "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
          [
            [
              [
                10.826701141116107,
                55.866699340329625
              ],
              [
                10.876702677777274,
                55.866699340329625
              ],
              [
                10.876702677777274,
                55.895498413889065
              ],
              [
                10.826701141116107,
                55.895498413889065
              ],
              [
                10.826701141116107,
                55.866699340329625
              ]
            ]
          ]
        ]
      },
      "properties": {
        "rsc": "HELCOM",
        "code": 252,
        "name": "Hatter Barn",
        "orig_name": null,
        "country": "Denmark",
        "designatio": null,
        "iucn_cat": null,
        "rep_m_area": null,
        "gis_m_area": null,
        "rep_area": null,
        "gis_area": null,
        "status": "Designated and managed",
        "status_yr": 2009,
        "mang_auth": null,
        "link": "http://mpas.helcom.fi/apex/f?p=103:12:::NO::P12_ID:252",
        "shape_leng": 0.12486362,
        "shape_area": 0.0009127
      }
    },
    {
      "type": "Feature",
      "id": 239,
      "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
          [
            [
              [
                13.56584537567118,
                54.51825640887737
              ],
              [
                13.692069856216941,
                54.51825640887737
              ],
              [
                13.692069856216941,
                54.5919557374847
              ],
              [
                13.56584537567118,
                54.5919557374847
              ],
              [
                13.56584537567118,
                54.51825640887737
              ]
            ]
          ]
        ]
      },
      "properties": {
        "rsc": "HELCOM",
        "code": 239,
        "name": "Jasmund National Park",
        "orig_name": null,
        "country": "Germany",
        "designatio": null,
        "iucn_cat": null,
        "rep_m_area": null,
        "gis_m_area": null,
        "rep_area": null,
        "gis_area": null,
        "status": "Designated and managed",
        "status_yr": 1996,
        "mang_auth": null,
        "link": "http://mpas.helcom.fi/apex/f?p=103:12:::NO::P12_ID:239",
        "shape_leng": 0.60600583,
        "shape_area": 0.00431054
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix pa: <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/239> a geojson:Feature ;
    foaf:page <http://mpas.helcom.fi/apex/f?p=103:12:::NO::P12_ID:239> ;
    geojson:geometry [ a geojson:MultiPolygon ;
            geojson:coordinates ( ( ( ( 1.356585e+01 5.451826e+01 ) ( 1.369207e+01 5.451826e+01 ) ( 1.369207e+01 5.459196e+01 ) ( 1.356585e+01 5.459196e+01 ) ( 1.356585e+01 5.451826e+01 ) ) ) ) ] ;
    pa:conventionSiteCode 239 ;
    pa:countryName "Germany" ;
    pa:establishmentYear "1996"^^xsd:gYear ;
    pa:managementStatus "Designated and managed" ;
    pa:regionalSeaConvention <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/rsc/HELCOM> ;
    pa:shapeAreaSquareDegrees 4.31054e-03 ;
    pa:shapeLengthDegrees 6.060058e-01 ;
    pa:siteName "Jasmund National Park" .

<file:///github/workspace/252> a geojson:Feature ;
    foaf:page <http://mpas.helcom.fi/apex/f?p=103:12:::NO::P12_ID:252> ;
    geojson:geometry [ a geojson:MultiPolygon ;
            geojson:coordinates ( ( ( ( 1.08267e+01 5.58667e+01 ) ( 1.08767e+01 5.58667e+01 ) ( 1.08767e+01 5.58955e+01 ) ( 1.08267e+01 5.58955e+01 ) ( 1.08267e+01 5.58667e+01 ) ) ) ) ] ;
    pa:conventionSiteCode 252 ;
    pa:countryName "Denmark" ;
    pa:establishmentYear "2009"^^xsd:gYear ;
    pa:managementStatus "Designated and managed" ;
    pa:regionalSeaConvention <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/rsc/HELCOM> ;
    pa:shapeAreaSquareDegrees 9.127e-04 ;
    pa:shapeLengthDegrees 1.248636e-01 ;
    pa:siteName "Hatter Barn" .

[] a geojson:FeatureCollection ;
    geojson:features <file:///github/workspace/239>,
        <file:///github/workspace/252> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EMODnet-compliant Regional Sea Convention MPA
description: 'GeoJSON Feature profile reproducing the EMODnet Human Activities layer
  `emodnet:marineprotectedareas` (MPAs as reported to HELCOM and OSPAR) with the service''s
  field names and primitive types. All attributes are present on every feature; attributes
  that EMODnet leaves empty for a convention are null.

  '
$defs:
  Feature:
    allOf:
    - $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/schema.yaml#/$defs/Feature
    - type: object
      properties:
        id:
          description: Feature id; equals `properties.code`.
          type: integer
        properties:
          type: object
          additionalProperties: false
          required:
          - rsc
          - code
          - name
          - orig_name
          - country
          - designatio
          - iucn_cat
          - rep_m_area
          - gis_m_area
          - rep_area
          - gis_area
          - status
          - status_yr
          - mang_auth
          - link
          - shape_leng
          - shape_area
          properties:
            rsc:
              description: Regional Sea Convention that reported the MPA.
              type: string
              enum:
              - HELCOM
              - OSPAR
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/regionalSeaConvention
              x-jsonld-type: '@vocab'
              x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/rsc/
            code:
              description: 'MPA identifier in the convention''s database (HELCOM MPA
                database id / OSPAR code). EMODnet types it xsd:long, so non-numeric
                codes are not admissible here.

                '
              type: integer
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/conventionSiteCode
            name:
              type: string
              minLength: 1
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/siteName
            orig_name:
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/originalSiteName
            country:
              description: Country name in English (Denmark, Estonia, Finland, Germany,
                Latvia, Lithuania, Poland, Russia, Sweden; Norway etc. for OSPAR).
              type: string
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/countryName
            designatio:
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/designationLabel
            iucn_cat:
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/iucnCategory
              x-jsonld-type: '@vocab'
              x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/iucn/
            rep_m_area:
              type:
              - number
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/reportedMarineArea
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#double
            gis_m_area:
              type:
              - number
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/gisMarineArea
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#double
            rep_area:
              type:
              - number
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/reportedArea
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#double
            gis_area:
              type:
              - number
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/gisArea
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#double
            status:
              description: For rsc = HELCOM, the HELCOM management status.
              type: string
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/managementStatus
            status_yr:
              description: Year of establishment.
              type:
              - integer
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/establishmentYear
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#gYear
            mang_auth:
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/managementAuthority
            link:
              description: Link to the site page in the convention's MPA database.
              type:
              - string
              - 'null'
              format: uri
              x-jsonld-id: http://xmlns.com/foaf/0.1/page
              x-jsonld-type: '@id'
            shape_leng:
              description: Perimeter in degrees, computed planar on the CRS84 geometry.
              type: number
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/shapeLengthDegrees
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#double
            shape_area:
              description: Area in square degrees, computed planar on the CRS84 geometry.
              type: number
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/shapeAreaSquareDegrees
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#double
      if:
        properties:
          properties:
            properties:
              rsc:
                const: HELCOM
      then:
        properties:
          properties:
            properties:
              status:
                enum:
                - Designated and managed
                - Designated and partly managed
                - Designated
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/managementStatus
  FeatureCollection:
    description: A FeatureCollection whose every member is a Feature of this profile.
    allOf:
    - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/featureCollection/schema.yaml
    - type: object
      properties:
        features:
          type: array
          items:
            $ref: '#/$defs/Feature'
oneOf:
- $ref: '#/$defs/Feature'
- $ref: '#/$defs/FeatureCollection'
x-jsonld-prefixes:
  pa: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/
  xsd: http://www.w3.org/2001/XMLSchema#
  foaf: http://xmlns.com/foaf/0.1/
  rdfs: http://www.w3.org/2000/01/rdf-schema#
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.emodnet-protected-area.rsc-mpa
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-27'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/rsc-mpa/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/rsc-mpa/schema.yaml)


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
    "geometry": {
      "@context": {
        "coordinates": {
          "@container": "@list",
          "@id": "geojson:coordinates"
        }
      },
      "@id": "geojson:geometry"
    },
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
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "dcterms": "http://purl.org/dc/terms/",
    "schema": "https://schema.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "prov": "http://www.w3.org/ns/prov#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "pa": "https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/",
    "pa-country": "pa:country/",
    "pa-iucn": "pa:iucn/",
    "eea-desig": "http://dd.eionet.europa.eu/vocabulary/cdda/designationTypeCodeValue/",
    "eu-country": "http://publications.europa.eu/resource/authority/country/",
    "inspire-iucn": "http://inspire.ec.europa.eu/codelist/IUCNCategoriesValue/",
    "rsc": {
      "@context": {
        "@vocab": "https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/rsc/"
      },
      "@id": "pa:regionalSeaConvention",
      "@type": "@vocab"
    },
    "code": "pa:conventionSiteCode",
    "name": "pa:siteName",
    "orig_name": "pa:originalSiteName",
    "country": "pa:countryName",
    "designatio": "pa:designationLabel",
    "iucn_cat": {
      "@context": {
        "@vocab": "https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/iucn/"
      },
      "@id": "pa:iucnCategory",
      "@type": "@vocab"
    },
    "rep_m_area": {
      "@id": "pa:reportedMarineArea",
      "@type": "xsd:double"
    },
    "gis_m_area": {
      "@id": "pa:gisMarineArea",
      "@type": "xsd:double"
    },
    "rep_area": {
      "@id": "pa:reportedArea",
      "@type": "xsd:double"
    },
    "gis_area": {
      "@id": "pa:gisArea",
      "@type": "xsd:double"
    },
    "status": "pa:managementStatus",
    "status_yr": {
      "@id": "pa:establishmentYear",
      "@type": "xsd:gYear"
    },
    "mang_auth": "pa:managementAuthority",
    "link": {
      "@id": "foaf:page",
      "@type": "@id"
    },
    "shape_leng": {
      "@id": "pa:shapeLengthDegrees",
      "@type": "xsd:double"
    },
    "shape_area": {
      "@id": "pa:shapeAreaSquareDegrees",
      "@type": "xsd:double"
    },
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/rsc-mpa/context.jsonld)

## Sources

* [EMODnet marineprotectedareas feature type (DescribeFeatureType)](https://ows.emodnet-humanactivities.eu/wfs?request=DescribeFeatureType&typeName=emodnet:marineprotectedareas)
* [HELCOM MPA database](http://mpas.helcom.fi/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/emodnet-protected-area/rsc-mpa`

