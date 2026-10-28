
# HELCOM MPA source profile with EMODnet transform (Schema)

`ogc.hosted.seadots.protected-area.source-helcom-mpa` *v0.1*

Source-faithful profile of HELCOM marine protected areas (HELCOM MADS layer 54 'HELCOM MPAs' and layer 190 'Baltic Sea MPA network 2026') as served by the Seadots OGC API - Features collections, with the Python transform that produces the EMODnet-compliant Regional Sea Convention MPA view and routes non-HELCOM codes to the EMODnet layers that already publish them.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# HELCOM MPA source profile with EMODnet transform

**Sources.** The Seadots pygeoapi instance serves two HELCOM ArcGIS layers unchanged:

| Collection | HELCOM MADS layer | Granularity | Codes |
|---|---|---|---|
| `helcom-live-mpas` | 54 *HELCOM MPAs* | one row per MPA | `MPA_ID`, the HELCOM MPA database id |
| `helcom-live-mpa-network-2026` | 190 *Baltic Sea MPA network 2026* | one row per polygon (3,537 rows on 30 Sep 2026) | `Code`, which mixes four schemes |

**Target:** `emodnet-protected-area.rsc-mpa` with `rsc = HELCOM`, the same shape as
EMODnet's `marineprotectedareas`.

## Field mapping (layer 54)

| EMODnet | Source | Rule |
|---|---|---|
| `rsc` | — | constant `HELCOM` |
| `code` | `MPA_ID` | integer |
| `name` | `Name` | copy |
| `country` | `Country` | copy (English names match EMODnet) |
| `status` | `MPA_status` | copy (same three values) |
| `status_yr` | `Year_est` | copy (`Date_est` is dropped; EMODnet keeps only the year) |
| `link` | `Site_link` | copy |
| `shape_leng`, `shape_area` | geometry | planar on CRS84 |
| `orig_name`, `designatio`, `iucn_cat`, `*_area`, `mang_auth` | — | `null`, as in EMODnet's HELCOM rows |

Layer 54 maps losslessly. On the example data, both sites equal the EMODnet records on
every attribute except the geometry-derived ones.

## Layer 190: classify, join, dissolve, route

EMODnet has not published the 2026 network, and its `code` is `xsd:long`. Layer 190 therefore
needs three extra steps before any row can enter the profile:

1. **Classify `Code`** by pattern:
   - `^\d{1,5}$` is a HELCOM MPA id, and the row enters this profile.
   - `^\d{6,10}$` is an EEA/WDPA site id. The row is routed to `emodnet:nationallydesignatedareas`
     (`natdaid`). Example: Fehmarnbelt `555638668` → EMODnet `DE02AWZ_4`.
   - `^[A-Z]{2}[A-Z0-9]{7}$` is a Natura 2000 code. The row is routed to `emodnet:natura2000areas`
     (`sitecode`). Example: Kuršių marios `LTSIU0012`.
   - Any other code is national and is reported as unresolved.

   Routed rows are **not duplicated** into the RSC view. The report carries the
   EMODnet key they resolve to, so the API can link to them instead.
2. **Join layer 54** on the HELCOM id to obtain `MPA_status`, `Year_est` and `Site_link`. Layer 190
   has no status field. An id with no layer-54 match (a newly added MPA) has no status, so it is
   reported and not published until HELCOM publishes it in the MPA database.
3. **Dissolve** rows that share an id into one MultiPolygon. The transform concatenates the parts
   and does not union them. This is correct for the disjoint parts in layer 190. If parts overlap,
   union them first (e.g. `ST_Union` in the GeoPackage), or `shape_area` counts the overlap twice.

The 2026 `Type` / `TypeSpecification` labels (e.g. *Kansallispuisto*, *Natur- og vildtreservater*)
have no field in the EMODnet RSC schema. They survive only on the source collection. Mapping them
to EEA designation types would be a separate crosswalk per country, similar to the Norwegian
`verneform` crosswalk.

## Examples

### HELCOM MPAs (layer 54)
Hatter Barn (DK) and Jasmund National Park (DE), attributes verbatim from HELCOM MADS layer 54 (retrieved 30 Sep 2026); geometry is each site's WGS 84 bounding box. Transformed with `to-emodnet-rsc-mpa`, both equal the EMODnet reference records of `emodnet-protected-area.rsc-mpa` on every attribute except the geometry-derived shape_leng / shape_area.

#### geojson
```geojson
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 17,
      "geometry": {
        "type": "Polygon",
        "coordinates": [
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
      },
      "properties": {
        "OBJECTID": 17,
        "Name": "Hatter Barn",
        "MPA_ID": 252,
        "Country": "Denmark",
        "Site_link": "http://mpas.helcom.fi/apex/f?p=103:12:::NO::P12_ID:252",
        "MPA_status": "Designated and managed",
        "Date_est": "10.09.2009",
        "Year_est": 2009,
        "Shape_Leng": 9884.28012434
      }
    },
    {
      "type": "Feature",
      "id": 109,
      "geometry": {
        "type": "Polygon",
        "coordinates": [
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
      },
      "properties": {
        "OBJECTID": 109,
        "Name": "Jasmund National Park",
        "MPA_ID": 239,
        "Country": "Germany",
        "Site_link": "http://mpas.helcom.fi/apex/f?p=103:12:::NO::P12_ID:239",
        "MPA_status": "Designated and managed",
        "Date_est": "04.09.1996",
        "Year_est": 1996,
        "Shape_Leng": 48390.1697459
      }
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/protected-area/source-helcom-mpa/context.jsonld",
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 17,
      "geometry": {
        "type": "Polygon",
        "coordinates": [
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
      },
      "properties": {
        "OBJECTID": 17,
        "Name": "Hatter Barn",
        "MPA_ID": 252,
        "Country": "Denmark",
        "Site_link": "http://mpas.helcom.fi/apex/f?p=103:12:::NO::P12_ID:252",
        "MPA_status": "Designated and managed",
        "Date_est": "10.09.2009",
        "Year_est": 2009,
        "Shape_Leng": 9884.28012434
      }
    },
    {
      "type": "Feature",
      "id": 109,
      "geometry": {
        "type": "Polygon",
        "coordinates": [
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
      },
      "properties": {
        "OBJECTID": 109,
        "Name": "Jasmund National Park",
        "MPA_ID": 239,
        "Country": "Germany",
        "Site_link": "http://mpas.helcom.fi/apex/f?p=103:12:::NO::P12_ID:239",
        "MPA_status": "Designated and managed",
        "Date_est": "04.09.1996",
        "Year_est": 1996,
        "Shape_Leng": 48390.1697459
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
@prefix pa-helcom: <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/helcom/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/109> a geojson:Feature ;
    foaf:page <http://mpas.helcom.fi/apex/f?p=103:12:::NO::P12_ID:239> ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.356585e+01 5.451826e+01 ) ( 1.369207e+01 5.451826e+01 ) ( 1.369207e+01 5.459196e+01 ) ( 1.356585e+01 5.459196e+01 ) ( 1.356585e+01 5.451826e+01 ) ) ) ] ;
    pa:conventionSiteCode 239 ;
    pa:countryName "Germany" ;
    pa:establishmentYear "1996"^^xsd:gYear ;
    pa-helcom:establishmentDate "04.09.1996" ;
    pa:managementStatus "Designated and managed" ;
    pa:siteName "Jasmund National Park" .

<file:///github/workspace/17> a geojson:Feature ;
    foaf:page <http://mpas.helcom.fi/apex/f?p=103:12:::NO::P12_ID:252> ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.08267e+01 5.58667e+01 ) ( 1.08767e+01 5.58667e+01 ) ( 1.08767e+01 5.58955e+01 ) ( 1.08267e+01 5.58955e+01 ) ( 1.08267e+01 5.58667e+01 ) ) ) ] ;
    pa:conventionSiteCode 252 ;
    pa:countryName "Denmark" ;
    pa:establishmentYear "2009"^^xsd:gYear ;
    pa-helcom:establishmentDate "10.09.2009" ;
    pa:managementStatus "Designated and managed" ;
    pa:siteName "Hatter Barn" .

[] a geojson:FeatureCollection ;
    geojson:features <file:///github/workspace/109>,
        <file:///github/workspace/17> .


```


### Baltic Sea MPA network 2026 (layer 190) - three code schemes
Three real layer-190 rows: Kuršių marios (Natura 2000 code LTSIU0012 -> routed to emodnet:natura2000areas, where it exists), Fehmarnbelt (EEA/WDPA id 555638668 -> routed to emodnet:nationallydesignatedareas, where it exists as DE02AWZ_4) and Jasmund National Park (HELCOM MPA id 239 -> published in this profile, status joined from layer 54). Attributes are verbatim from HELCOM MADS layer 190; on 7 Oct 2026 all three rows were checked field by field against the live service and are unchanged (https://maps.helcom.fi/arcgis/rest/services/MADS/Biodiversity/MapServer/190/query?where=OBJECTID+IN+(1,2740,2857)&outFields=*&returnGeometry=false&f=json). The geometry is each site's WGS 84 bounding box, not the true boundary.

#### geojson
```geojson
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 1,
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              20.984144572112506,
              55.245580267031144
            ],
            [
              21.297918717602144,
              55.245580267031144
            ],
            [
              21.297918717602144,
              55.63379146271399
            ],
            [
              20.984144572112506,
              55.63379146271399
            ],
            [
              20.984144572112506,
              55.245580267031144
            ]
          ]
        ]
      },
      "properties": {
        "OBJECTID": 1,
        "Name": "Kuršių marios",
        "Type": "Unclear",
        "TypeSpecification": "SAC/SPA",
        "Code": "LTSIU0012",
        "Country": "Lithuania",
        "HasCoastalArea": "Yes",
        "polygon_affiliation": "81",
        "site_polygon_id": "1",
        "Shape_Length": 277843.02887324407,
        "Shape_Area": 1172034118.3959205
      }
    },
    {
      "type": "Feature",
      "id": 2740,
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              10.731861109736467,
              54.4697871105662
            ],
            [
              11.409778790299207,
              54.4697871105662
            ],
            [
              11.409778790299207,
              54.640554940352
            ],
            [
              10.731861109736467,
              54.640554940352
            ],
            [
              10.731861109736467,
              54.4697871105662
            ]
          ]
        ]
      },
      "properties": {
        "OBJECTID": 2740,
        "Name": "Fehmarnbelt",
        "Type": "HELCOM MPA",
        "TypeSpecification": null,
        "Code": "555638668",
        "Country": "Germany",
        "HasCoastalArea": "Yes",
        "polygon_affiliation": "78",
        "site_polygon_id": "2740",
        "Shape_Length": 191593.22332921537,
        "Shape_Area": 831552568.9034636
      }
    },
    {
      "type": "Feature",
      "id": 2857,
      "geometry": {
        "type": "Polygon",
        "coordinates": [
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
      },
      "properties": {
        "OBJECTID": 2857,
        "Name": "Jasmund National Park",
        "Type": "HELCOM MPA",
        "TypeSpecification": "Old MPA Data",
        "Code": "239",
        "Country": "Germany",
        "HasCoastalArea": "Yes",
        "polygon_affiliation": "78",
        "site_polygon_id": "2857",
        "Shape_Length": 83349.38566238541,
        "Shape_Area": 92108460.86603956
      }
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/protected-area/source-helcom-mpa/context.jsonld",
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 1,
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              20.984144572112506,
              55.245580267031144
            ],
            [
              21.297918717602144,
              55.245580267031144
            ],
            [
              21.297918717602144,
              55.63379146271399
            ],
            [
              20.984144572112506,
              55.63379146271399
            ],
            [
              20.984144572112506,
              55.245580267031144
            ]
          ]
        ]
      },
      "properties": {
        "OBJECTID": 1,
        "Name": "Kur\u0161i\u0173 marios",
        "Type": "Unclear",
        "TypeSpecification": "SAC/SPA",
        "Code": "LTSIU0012",
        "Country": "Lithuania",
        "HasCoastalArea": "Yes",
        "polygon_affiliation": "81",
        "site_polygon_id": "1",
        "Shape_Length": 277843.02887324407,
        "Shape_Area": 1172034118.3959205
      }
    },
    {
      "type": "Feature",
      "id": 2740,
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              10.731861109736467,
              54.4697871105662
            ],
            [
              11.409778790299207,
              54.4697871105662
            ],
            [
              11.409778790299207,
              54.640554940352
            ],
            [
              10.731861109736467,
              54.640554940352
            ],
            [
              10.731861109736467,
              54.4697871105662
            ]
          ]
        ]
      },
      "properties": {
        "OBJECTID": 2740,
        "Name": "Fehmarnbelt",
        "Type": "HELCOM MPA",
        "TypeSpecification": null,
        "Code": "555638668",
        "Country": "Germany",
        "HasCoastalArea": "Yes",
        "polygon_affiliation": "78",
        "site_polygon_id": "2740",
        "Shape_Length": 191593.22332921537,
        "Shape_Area": 831552568.9034636
      }
    },
    {
      "type": "Feature",
      "id": 2857,
      "geometry": {
        "type": "Polygon",
        "coordinates": [
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
      },
      "properties": {
        "OBJECTID": 2857,
        "Name": "Jasmund National Park",
        "Type": "HELCOM MPA",
        "TypeSpecification": "Old MPA Data",
        "Code": "239",
        "Country": "Germany",
        "HasCoastalArea": "Yes",
        "polygon_affiliation": "78",
        "site_polygon_id": "2857",
        "Shape_Length": 83349.38566238541,
        "Shape_Area": 92108460.86603956
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix pa: <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/> .
@prefix pa-helcom: <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/helcom/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/1> a geojson:Feature ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 2.098414e+01 5.524558e+01 ) ( 2.129792e+01 5.524558e+01 ) ( 2.129792e+01 5.563379e+01 ) ( 2.098414e+01 5.563379e+01 ) ( 2.098414e+01 5.524558e+01 ) ) ) ] ;
    pa:countryName "Lithuania" ;
    pa-helcom:designationType "Unclear" ;
    pa-helcom:designationTypeSpecification "SAC/SPA" ;
    pa-helcom:hasCoastalArea "Yes" ;
    pa-helcom:siteCode "LTSIU0012" ;
    pa:siteName "Kuršių marios" .

<file:///github/workspace/2740> a geojson:Feature ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.073186e+01 5.446979e+01 ) ( 1.140978e+01 5.446979e+01 ) ( 1.140978e+01 5.464055e+01 ) ( 1.073186e+01 5.464055e+01 ) ( 1.073186e+01 5.446979e+01 ) ) ) ] ;
    pa:countryName "Germany" ;
    pa-helcom:designationType "HELCOM MPA" ;
    pa-helcom:hasCoastalArea "Yes" ;
    pa-helcom:siteCode "555638668" ;
    pa:siteName "Fehmarnbelt" .

<file:///github/workspace/2857> a geojson:Feature ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.356585e+01 5.451826e+01 ) ( 1.369207e+01 5.451826e+01 ) ( 1.369207e+01 5.459196e+01 ) ( 1.356585e+01 5.459196e+01 ) ( 1.356585e+01 5.451826e+01 ) ) ) ] ;
    pa:countryName "Germany" ;
    pa-helcom:designationType "HELCOM MPA" ;
    pa-helcom:designationTypeSpecification "Old MPA Data" ;
    pa-helcom:hasCoastalArea "Yes" ;
    pa-helcom:siteCode "239" ;
    pa:siteName "Jasmund National Park" .

[] a geojson:FeatureCollection ;
    geojson:features <file:///github/workspace/1>,
        <file:///github/workspace/2740>,
        <file:///github/workspace/2857> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: HELCOM MPA source feature (HELCOM MADS layers 54 and 190)
description: 'Source-faithful GeoJSON profile of HELCOM marine protected areas as
  served by the Seadots pygeoapi collections `helcom-live-mpas` (ESRI provider over
  HELCOM MADS Biodiversity layer 54, "HELCOM MPAs", one row per MPA) and `helcom-live-mpa-network-2026`
  (layer 190, "Baltic Sea MPA network 2026", one row per polygon, heterogeneous national
  types and codes). Field names are HELCOM''s own.

  '
$defs:
  Feature:
    allOf:
    - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.yaml
    - type: object
      required:
      - geometry
      - properties
      properties:
        geometry:
          type: object
          properties:
            type:
              enum:
              - Polygon
              - MultiPolygon
        properties:
          oneOf:
          - title: Layer 54 - HELCOM MPAs
            type: object
            required:
            - Name
            - MPA_ID
            - Country
            - MPA_status
            properties:
              OBJECTID:
                type: integer
              Name:
                type: string
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/siteName
              MPA_ID:
                type: integer
                description: HELCOM MPA database id.
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/conventionSiteCode
              Country:
                type: string
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/countryName
              Site_link:
                type:
                - string
                - 'null'
                format: uri
                x-jsonld-id: http://xmlns.com/foaf/0.1/page
                x-jsonld-type: '@id'
              MPA_status:
                type: string
                enum:
                - Designated and managed
                - Designated and partly managed
                - Designated
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/managementStatus
              Date_est:
                type:
                - string
                - 'null'
                pattern: ^\d{2}\.\d{2}\.\d{4}$
                description: Date of establishment
                DD.MM.YYYY.: null
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/helcom/establishmentDate
              Year_est:
                type:
                - integer
                - 'null'
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/establishmentYear
                x-jsonld-type: http://www.w3.org/2001/XMLSchema#gYear
              Shape_Leng:
                type:
                - number
                - 'null'
          - title: Layer 190 - Baltic Sea MPA network 2026
            type: object
            required:
            - Name
            - Type
            - Code
            - Country
            properties:
              OBJECTID:
                type: integer
              Name:
                type: string
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/siteName
              Type:
                type: string
                description: National or international designation type
                in the reporting country's language or English.: null
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/helcom/designationType
              TypeSpecification:
                type:
                - string
                - 'null'
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/helcom/designationTypeSpecification
              Code:
                type: string
                description: 'Site code. Mixes HELCOM MPA ids (e.g. 239), EEA/WDPA
                  site ids (e.g. 555638668), Natura 2000 site codes (e.g. LTSIU0012)
                  and national codes.

                  '
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/helcom/siteCode
              Country:
                type: string
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/countryName
              HasCoastalArea:
                type:
                - string
                - 'null'
                enum:
                - 'Yes'
                - 'No'
                - null
                x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/helcom/hasCoastalArea
              polygon_affiliation:
                type:
                - string
                - 'null'
              site_polygon_id:
                type:
                - string
                - 'null'
              Shape_Length:
                type:
                - number
                - 'null'
              Shape_Area:
                type:
                - number
                - 'null'
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
  pa-helcom: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/helcom/
  foaf: http://xmlns.com/foaf/0.1/
  xsd: http://www.w3.org/2001/XMLSchema#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.protected-area.source-helcom-mpa
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-27'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/protected-area/source-helcom-mpa/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/protected-area/source-helcom-mpa/schema.yaml)


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
    "pa": "https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/",
    "pa-helcom": "pa:helcom/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "Name": "pa:siteName",
    "MPA_ID": "pa:conventionSiteCode",
    "Country": "pa:countryName",
    "Site_link": {
      "@id": "foaf:page",
      "@type": "@id"
    },
    "MPA_status": "pa:managementStatus",
    "Date_est": "pa:helcom/establishmentDate",
    "Year_est": {
      "@id": "pa:establishmentYear",
      "@type": "xsd:gYear"
    },
    "Type": "pa:helcom/designationType",
    "TypeSpecification": "pa:helcom/designationTypeSpecification",
    "Code": "pa:helcom/siteCode",
    "HasCoastalArea": "pa:helcom/hasCoastalArea",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/protected-area/source-helcom-mpa/context.jsonld)

## Sources

* [HELCOM MADS Biodiversity layer 54: HELCOM MPAs](https://maps.helcom.fi/arcgis/rest/services/MADS/Biodiversity/MapServer/54)
* [HELCOM MADS Biodiversity layer 190: Baltic Sea MPA network 2026](https://maps.helcom.fi/arcgis/rest/services/MADS/Biodiversity/MapServer/190)
* [HELCOM MPA database](http://mpas.helcom.fi/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/protected-area/source-helcom-mpa`

