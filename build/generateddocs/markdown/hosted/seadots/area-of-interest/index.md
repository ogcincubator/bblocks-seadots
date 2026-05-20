
# Marine Area of Interest (Schema)

`ogc.hosted.seadots.area-of-interest` *v0.1*

OGC Feature profile for a polygon delimiting a marine area of interest (AOI) used by experiments, monitoring programmes, or impact assessments. Carries the bbox, centroid, area, and CRS as a self-contained inline `data` block with mandatory provenance. Geometry travels in the top-level GeoJSON `geometry` field.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Marine Area of Interest

OGC API Records / OGC Feature profile for a polygon delimiting a marine area of interest.

The geometry is carried by the top-level `geometry` field (GeoJSON Polygon). The `data` block carries derived scalars (bbox, centroid, area_km2, CRS) so a consumer can read the AOI without re-parsing the geometry. Mandatory `data.provenance` documents whether the polygon was retrieved from an authoritative source or hand-drawn / illustrative.

## Dependency

Inherits the OIM feature shape from `ogc.hosted.iliad.api.features.oim`.

## Vocabulary

- `bbox`, `centroid`, `area_km2` carried as local terms (`seadots:` namespace) — see `validation-report.md` for terms still pending authoritative vocabulary URIs.
- `crs` is a string identifier (e.g. `EPSG:4326`); a future revision MAY upgrade to an OGC CRS register URI.

## Examples

### AOI — surroundings of Utsira island
#### json
```json
{
  "id": "https://example.org/norwegian-ses/area-of-interest/utsira-surroundings",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [4.20, 59.10],
      [5.30, 59.10],
      [5.30, 59.70],
      [4.20, 59.70],
      [4.20, 59.10]
    ]]
  },
  "properties": {
    "type": "Dataset",
    "title": "AOI — surroundings of Utsira island",
    "description": "Polygon delimiting the broader study area around Utsira island (~3500 km²). Extends the Utsira Nord licence polygon outward to cover the surroundings, while preserving the western and southern boundaries used by the original demonstrator.",
    "created": "2026-05-18",
    "updated": "2026-05-19",
    "language": { "code": "en" },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "themes": [{ "concepts": [{ "id": "AOI", "label": "Area of interest" }], "scheme": "https://id3.seadots.eu/themes" }],
    "keywords": ["AOI", "Utsira", "surroundings", "polygon"],
    "formats": [{ "mediaType": "application/geo+json" }],
    "areaOfInterest": {
      "name": "AOI polygon (surroundings of Utsira)",
      "description": "Polygon delimiting the broader study area around Utsira island.",
      "role": "study area",
      "source": "aoi/utsira_surroundings_polygon.geojson",
      "format": "application/geo+json",
      "vocabularyTerm": "http://www.opengis.net/def/property/OGC/0/area-of-interest",
      "data": {
        "bbox": [4.20, 59.10, 5.30, 59.70],
        "centroid": [4.75, 59.40],
        "area_km2": 3520,
        "crs": "EPSG:4326",
        "note": "Polygon coordinates are carried by the top-level `geometry` field per OGC Records.",
        "provenance": {
          "values": "illustrative",
          "note": "Bbox, centroid, and area_km2 are derived from the illustrative polygon drawn in this record's top-level geometry — not from an authoritative licence-area dataset.",
          "nearestAuthoritativeSource": {
            "url": "https://veiledere.nve.no/havvind/strategisk-konsekvensutredning-av-vindkraft-til-havs/",
            "note": "NVE strategic assessment hosts the licensed Utsira Nord polygon. For real Norwegian offshore-wind area polygons, retrieve via the Geonorge catalogue (https://www.geonorge.no/)."
          }
        }
      }
    }
  },
  "links": [
    { "rel": "describedby", "href": "bblocks://ogc.hosted.seadots.area-of-interest", "type": "application/schema+json", "title": "Marine Area of Interest bblock" },
    { "rel": "profile", "href": "bblocks://ogc.hosted.iliad.api.features.oim", "type": "application/schema+json", "title": "OIM feature profile" }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/area-of-interest/context.jsonld",
  "id": "https://example.org/norwegian-ses/area-of-interest/utsira-surroundings",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          4.2,
          59.1
        ],
        [
          5.3,
          59.1
        ],
        [
          5.3,
          59.7
        ],
        [
          4.2,
          59.7
        ],
        [
          4.2,
          59.1
        ]
      ]
    ]
  },
  "properties": {
    "type": "Dataset",
    "title": "AOI \u2014 surroundings of Utsira island",
    "description": "Polygon delimiting the broader study area around Utsira island (~3500 km\u00b2). Extends the Utsira Nord licence polygon outward to cover the surroundings, while preserving the western and southern boundaries used by the original demonstrator.",
    "created": "2026-05-18",
    "updated": "2026-05-19",
    "language": {
      "code": "en"
    },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "themes": [
      {
        "concepts": [
          {
            "id": "AOI",
            "label": "Area of interest"
          }
        ],
        "scheme": "https://id3.seadots.eu/themes"
      }
    ],
    "keywords": [
      "AOI",
      "Utsira",
      "surroundings",
      "polygon"
    ],
    "formats": [
      {
        "mediaType": "application/geo+json"
      }
    ],
    "areaOfInterest": {
      "name": "AOI polygon (surroundings of Utsira)",
      "description": "Polygon delimiting the broader study area around Utsira island.",
      "role": "study area",
      "source": "aoi/utsira_surroundings_polygon.geojson",
      "format": "application/geo+json",
      "vocabularyTerm": "http://www.opengis.net/def/property/OGC/0/area-of-interest",
      "data": {
        "bbox": [
          4.2,
          59.1,
          5.3,
          59.7
        ],
        "centroid": [
          4.75,
          59.4
        ],
        "area_km2": 3520,
        "crs": "EPSG:4326",
        "note": "Polygon coordinates are carried by the top-level `geometry` field per OGC Records.",
        "provenance": {
          "values": "illustrative",
          "note": "Bbox, centroid, and area_km2 are derived from the illustrative polygon drawn in this record's top-level geometry \u2014 not from an authoritative licence-area dataset.",
          "nearestAuthoritativeSource": {
            "url": "https://veiledere.nve.no/havvind/strategisk-konsekvensutredning-av-vindkraft-til-havs/",
            "note": "NVE strategic assessment hosts the licensed Utsira Nord polygon. For real Norwegian offshore-wind area polygons, retrieve via the Geonorge catalogue (https://www.geonorge.no/)."
          }
        }
      }
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.area-of-interest",
      "type": "application/schema+json",
      "title": "Marine Area of Interest bblock"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.iliad.api.features.oim",
      "type": "application/schema+json",
      "title": "OIM feature profile"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/area-of-interest#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/norwegian-ses/area-of-interest/utsira-surroundings> a geojson:Feature ;
    rdfs:seeAlso [ rdfs:label "Marine Area of Interest bblock" ;
            dcterms:format "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.area-of-interest> ],
        [ rdfs:label "OIM feature profile" ;
            dcterms:format "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/profile> ;
            oa:hasTarget <bblocks://ogc.hosted.iliad.api.features.oim> ] ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 4.2e+00 5.91e+01 ) ( 5.3e+00 5.91e+01 ) ( 5.3e+00 5.97e+01 ) ( 4.2e+00 5.97e+01 ) ( 4.2e+00 5.91e+01 ) ) ) ] ;
    geojson:properties [ a seadots:Dataset ;
            dcterms:created "2026-05-18" ;
            dcterms:description "Polygon delimiting the broader study area around Utsira island (~3500 km²). Extends the Utsira Nord licence polygon outward to cover the surroundings, while preserving the western and southern boundaries used by the original demonstrator." ;
            dcterms:license "https://creativecommons.org/licenses/by/4.0/" ;
            dcterms:modified "2026-05-19" ;
            dcterms:title "AOI — surroundings of Utsira island" ;
            dcat:keyword "AOI",
                "Utsira",
                "polygon",
                "surroundings" ;
            seadots:areaOfInterest [ dcterms:description "Polygon delimiting the broader study area around Utsira island." ;
                    dcterms:format "application/geo+json" ;
                    dcterms:title "AOI polygon (surroundings of Utsira)" ;
                    skos:exactMatch <http://www.opengis.net/def/property/OGC/0/area-of-interest> ;
                    dcat:accessURL <file:///github/workspace/aoi/utsira_surroundings_polygon.geojson> ;
                    seadots:data [ skos:note "Polygon coordinates are carried by the top-level `geometry` field per OGC Records." ;
                            prov:wasDerivedFrom [ skos:note "Bbox, centroid, and area_km2 are derived from the illustrative polygon drawn in this record's top-level geometry — not from an authoritative licence-area dataset." ;
                                    seadots:nearestAuthoritativeSource [ skos:note "NVE strategic assessment hosts the licensed Utsira Nord polygon. For real Norwegian offshore-wind area polygons, retrieve via the Geonorge catalogue (https://www.geonorge.no/)." ;
                                            dcat:accessURL <https://veiledere.nve.no/havvind/strategisk-konsekvensutredning-av-vindkraft-til-havs/> ] ;
                                    seadots:provenanceValues "illustrative" ] ;
                            geojson:bbox ( 4.2e+00 5.91e+01 5.3e+00 5.97e+01 ) ;
                            seadots:area_km2 3520 ;
                            seadots:centroid 4.75e+00,
                                5.94e+01 ;
                            seadots:crs "EPSG:4326" ] ;
                    seadots:role "study area" ] ;
            rec:format [ dcterms:format "application/geo+json" ] ;
            rec:language [ rec:languageCode "en" ] ;
            rec:themes [ rec:concept [ skos:prefLabel "Area of interest" ;
                            rec:conceptID "AOI"^^xsd:string ] ;
                    rec:scheme "https://id3.seadots.eu/themes" ] ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Marine Area of Interest
description: 'Polygon-delimited marine area used by experiments, monitoring programmes,
  or impact assessments. Inherits the OIM feature shape; adds an `areaOfInterest`
  property carrying inline scalars (bbox, centroid, area, CRS) and mandatory provenance.

  '
allOf:
- $ref: https://ogcincubator.github.io/geodcat-ogcapi-records/build/annotated/geo/geodcat/geodcat-records/schema.yaml
properties:
  geometry:
    description: GeoJSON Polygon delimiting the AOI.
    type: object
    required:
    - type
    - coordinates
    properties:
      type:
        const: Polygon
        x-jsonld-id: '@type'
      coordinates:
        type: array
        x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
  properties:
    type: object
    required:
    - areaOfInterest
    properties:
      areaOfInterest:
        type: object
        required:
        - name
        - source
        - data
        properties:
          name:
            type: string
            x-jsonld-id: http://purl.org/dc/terms/title
          description:
            type: string
            x-jsonld-id: http://purl.org/dc/terms/description
          role:
            type: string
            description: Role the AOI plays (e.g. `study area`, `monitoring footprint`,
              `licence polygon`).
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/area-of-interest#role
          source:
            type: string
            description: Access URI or file path for the canonical polygon.
            x-jsonld-id: http://www.w3.org/ns/dcat#accessURL
            x-jsonld-type: '@id'
          format:
            type: string
            description: Media type (e.g. application/geo+json).
            x-jsonld-id: http://purl.org/dc/terms/format
          vocabularyTerm:
            type: string
            format: uri
            x-jsonld-id: http://www.w3.org/2004/02/skos/core#exactMatch
            x-jsonld-type: '@id'
          data:
            type: object
            required:
            - provenance
            properties:
              bbox:
                type: array
                items:
                  type: number
                minItems: 4
                maxItems: 4
                x-jsonld-id: https://purl.org/geojson/vocab#bbox
              centroid:
                type: array
                items:
                  type: number
                minItems: 2
                maxItems: 2
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/area-of-interest#centroid
              area_km2:
                type: number
                minimum: 0
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/area-of-interest#area_km2
              crs:
                type: string
                description: CRS identifier, e.g. EPSG:4326.
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/area-of-interest#crs
              note:
                type: string
                x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
              provenance:
                type: object
                required:
                - values
                properties:
                  values:
                    type: string
                    enum:
                    - retrieved
                    - illustrative
                    - mixed
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/area-of-interest#provenanceValues
                  retrievalApiCall:
                    type: string
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/area-of-interest#retrievalApiCall
                    x-jsonld-type: '@id'
                  verifiedOn:
                    type: string
                    format: date
                    x-jsonld-id: http://purl.org/dc/terms/date
                  primarySource:
                    type: object
                    x-jsonld-id: http://purl.org/dc/terms/source
                  nearestAuthoritativeSource:
                    type: object
                    properties:
                      url:
                        type: string
                        format: uri
                        x-jsonld-id: http://www.w3.org/ns/dcat#accessURL
                        x-jsonld-type: '@id'
                      note:
                        type: string
                        x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
                    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/area-of-interest#nearestAuthoritativeSource
                  note:
                    type: string
                    x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
                x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/area-of-interest#data
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/area-of-interest#areaOfInterest
    x-jsonld-id: https://purl.org/geojson/vocab#properties
x-jsonld-extra-terms:
  id: '@id'
  Feature: https://purl.org/geojson/vocab#Feature
  Polygon: https://purl.org/geojson/vocab#Polygon
  links:
    x-jsonld-id: http://www.w3.org/ns/iana/link-relations/relation
    x-jsonld-container: '@set'
  href: '@id'
  rel: https://purl.org/geojson/vocab#rel
  title: http://purl.org/dc/terms/title
  created: http://purl.org/dc/terms/created
  updated: http://purl.org/dc/terms/modified
  language: http://purl.org/dc/terms/language
  code: http://purl.org/dc/terms/identifier
  license: http://purl.org/dc/terms/license
  keywords:
    x-jsonld-id: http://www.w3.org/ns/dcat#keyword
    x-jsonld-container: '@set'
  themes:
    x-jsonld-id: http://www.w3.org/ns/dcat#theme
    x-jsonld-container: '@set'
  concepts:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#Concept
    x-jsonld-container: '@set'
  scheme: http://www.w3.org/2004/02/skos/core#inScheme
  label: http://www.w3.org/2004/02/skos/core#prefLabel
  formats:
    x-jsonld-id: http://purl.org/dc/terms/format
    x-jsonld-container: '@set'
  mediaType: http://purl.org/dc/terms/format
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/area-of-interest#
x-jsonld-prefixes:
  dcterms: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#
  skos: http://www.w3.org/2004/02/skos/core#
  seadots: https://w3id.org/ogc/hosted/seadots/area-of-interest#
  prov: http://www.w3.org/ns/prov#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/area-of-interest/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/area-of-interest/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/area-of-interest#",
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
    "properties": {
      "@context": {
        "areaOfInterest": {
          "@context": {
            "name": "dct:title",
            "role": "seadots:role",
            "source": {
              "@id": "dcat:accessURL",
              "@type": "@id"
            },
            "format": "dct:format",
            "vocabularyTerm": {
              "@id": "skos:exactMatch",
              "@type": "@id"
            },
            "data": {
              "@context": {
                "centroid": "seadots:centroid",
                "area_km2": "seadots:area_km2",
                "crs": "seadots:crs",
                "note": "skos:note",
                "provenance": {
                  "@context": {
                    "values": "seadots:provenanceValues",
                    "retrievalApiCall": {
                      "@id": "seadots:retrievalApiCall",
                      "@type": "@id"
                    },
                    "verifiedOn": "dct:date",
                    "primarySource": "dct:source",
                    "nearestAuthoritativeSource": {
                      "@context": {
                        "url": {
                          "@id": "dcat:accessURL",
                          "@type": "@id"
                        }
                      },
                      "@id": "seadots:nearestAuthoritativeSource"
                    }
                  },
                  "@id": "prov:wasDerivedFrom"
                }
              },
              "@id": "seadots:data"
            }
          },
          "@id": "seadots:areaOfInterest"
        }
      },
      "@id": "geojson:properties"
    },
    "geometry": {
      "@context": {
        "coordinates": {
          "@id": "geojson:coordinates",
          "@container": "@list"
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
        "type": "dct:format",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "conformsTo": {
      "@container": "@set",
      "@id": "dct:conformsTo",
      "@type": "@id"
    },
    "time": "dct:temporal",
    "linkTemplates": {
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
        "type": "dct:format",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent",
        "uriTemplate": {
          "@type": "xsd:string",
          "@id": "rec:uriTemplate"
        },
        "varBase": "rec:varBase",
        "variables": {
          "@id": "rec:hasVariable",
          "@container": "@index",
          "@index": "dct:identifier"
        }
      },
      "@id": "rec:hasLinkTemplate"
    },
    "created": "dct:created",
    "updated": "dct:modified",
    "title": {
      "@container": "@set",
      "@id": "dct:title"
    },
    "description": {
      "@container": "@set",
      "@id": "dct:description"
    },
    "keywords": {
      "@container": "@set",
      "@id": "dcat:keyword"
    },
    "language": {
      "@id": "rec:language",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "languages": {
      "@container": "@set",
      "@id": "rec:languages",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "resourceLanguages": {
      "@container": "@set",
      "@id": "rec:resourceLanguages",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "externalIds": {
      "@container": "@set",
      "@id": "rec:scopedIdentifier",
      "@context": {
        "scheme": "rec:scheme",
        "value": "rec:id"
      }
    },
    "themes": {
      "@container": "@set",
      "@id": "rec:themes",
      "@context": {
        "concepts": {
          "@id": "rec:concept",
          "@context": {
            "id": {
              "@type": "xsd:string",
              "@id": "rec:conceptID"
            },
            "url": {
              "@type": "@id",
              "@id": "dcat:theme"
            }
          }
        },
        "scheme": "rec:scheme"
      }
    },
    "formats": {
      "@id": "rec:format",
      "@context": {
        "name": "rec:name"
      }
    },
    "contacts": {
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "license": "dct:license",
    "accessrights": "dct:accessRights",
    "variables": {
      "@container": "@id",
      "@id": "rec:hasVariable",
      "@context": {
        "@base": "http://example.com/variables/",
        "@vocab": "https://www.opengis.net/def/ogc-api/records/"
      }
    },
    "href": "@id",
    "rel": "geojson:rel",
    "code": "dct:identifier",
    "concepts": {
      "@id": "skos:Concept",
      "@container": "@set"
    },
    "scheme": "skos:inScheme",
    "label": "skos:prefLabel",
    "mediaType": "dct:format",
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "rec": "https://www.opengis.net/def/ogc-api/records/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "w3ctime": "http://www.w3.org/2006/time#",
    "dctype": "http://purl.org/dc/dcmitype/",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "prov": "http://www.w3.org/ns/prov#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "thns": "https://w3id.org/ogc/stac/themes/",
    "dcterms": "http://purl.org/dc/terms/",
    "seadots": "https://w3id.org/ogc/hosted/seadots/area-of-interest#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/area-of-interest/context.jsonld)

## Sources

* [GeoDCAT-Records](https://ogcincubator.github.io/geodcat-ogcapi-records/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/area-of-interest`

