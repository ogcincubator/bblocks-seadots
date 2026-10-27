
# Naturvernområder source profile with EMODnet transform (Schema)

`ogc.hosted.seadots.protected-area.source-norway-naturvernomrade` *v0.1*

Source-faithful profile of Norwegian protected sites (Miljødirektoratet Naturvernområder, vern layer 0) as served by the Seadots OGC API - Features collections, with the crosswalks (verneform to EEA designation type, IUCN, ecosystem) and the Python transform that produces the EMODnet-compliant nationally designated area view.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Naturvernområder source profile with EMODnet transform

**Source:** Norwegian protected sites (Miljødirektoratet *Naturvernområder*, Geonorge
`5857ec0a-…`, ArcGIS `vern` layer 0). The Seadots pygeoapi instance serves them
unchanged as `no-live-naturvern-omrade` (live) and `no-snapshot-naturvern-omrade-marine`
(snapshot).

**Target:** `emodnet-protected-area.nationally-designated-area`, the same shape as
EMODnet's `nationallydesignatedareas`.

## Field mapping

| EMODnet attribute | Rule | Source field(s) |
|---|---|---|
| `natdaid` | integer | `cddaId` (null until the site is reported to the EEA) |
| `countrycod`, `regioncode` / `country` | constant | `NO` / `Norway` |
| `sitename` | copy (short name, **not** `offisieltNavn`) | `navn` |
| `legalfound` | year of the date | `vernedato` (epoch ms or ISO date) |
| `localid`, `nationalid`, `pslocalid` | copy | `naturvernId` |
| `namespace`, `psnamespac` | constant | `http://www.miljodirektoratet.no/naturbase` |
| `designatio` | crosswalk `verneform-designation.csv` | `verneform` |
| `iucncatego`, `iucndesc` | crosswalk `iucn.csv` | `iucn` |
| `majorecosy` | crosswalk `ecosystem.csv` | `majorEcosystemType` |
| `marinearea` | 100 / 0 from the crosswalk. For *MarinOgTerrestrisk*, a coastline overlay is needed (step 4) | `majorEcosystemType` + geometry |
| `sitearea` | m² ÷ 10 000, 2 decimals | `SHAPE.STArea()` / `SHAPE_STArea` (EPSG:25833) |
| `shape_leng`, `shape_area` | planar on the CRS84 geometry | geometry |
| `designated`, `coast_mar`, `geomtype`, `spatialdat`, `spatialres` | constant | `Designated site`, `1`, `polygon`, `public`, `Scale larger 100K` |
| `metadata_v`, `metadata_b` | provenance | Geonorge metadata URL, retrieval date |
| `id`, `versionid`, `metadata_s/f/1`, `iucnlink`, `psversioni`, `remark` | `null` | — |

All other source fields (`verneforskrift`, `faktaark`, `forvaltningsmyndighet`, `kommune`,
…) are dropped from the view. They stay available on the source collection, which the view
links to.

## Selection rules

- **Kept:** marine sites, i.e. `majorEcosystemType` *Marin* / *MarinOgTerrestrisk*. This
  matches EMODnet's `majorecosy <> 'Terrestrial'` subset for Norway (885 EMODnet vs 888
  source sites on 28 Sep 2026). Coastal *terrestrial* sites, which EMODnet also carries with
  `coast_mar = 1`, would need the EEA's coastal-proximity rule and are out of scope.
- **Excluded:** protection forms with no EEA designation type (`MidlertidigVernaOmraade`),
  and proposed sites (layer 4). EMODnet publishes neither.

## Crosswalk confidence

`crosswalk/verneform-designation.csv` records how each mapping was established:

- **observed**: confirmed by a joined EMODnet record;
- **label**: the Eionet label is the English name of the Norwegian form;
- **inferred**: variant forms and forms whose Eionet label is ambiguous. For example,
  NO17 and NO23 are both *Wildlife Conservation Area*.

`transforms/derive_crosswalk.py` (step 3) confirms the crosswalk from the ~1,500 joined
sites before inferred rows are relied on. The CSV drives the transform, and
`crosswalk/crosswalk.ttl` publishes the same table as SKOS: `exactMatch` for
observed/label rows, `closeMatch` for inferred rows.

## Report produced with every run

The transform returns the EMODnet features plus a `seadotsTransformReport` member with:

- `excluded`
- `notYetReportedToEEA`: sites without `cddaId`, e.g. the four MPAs decided on
  13 Feb 2026. Their feature id is `NO-<naturvernId>`.
- `inferredDesignation`
- `needsMarineAreaOverlay`
- `differsFromEMODnet`: field-level differences from an EMODnet reference.

On the example data it reproduces the EMODnet Tauterryggen record on every mapped
field. It also reports the Møysalen swap (natdaid, designatio, iucncatego), which comes
from the EEA reporting chain. **The view keeps the source values**, because the national
source is authoritative. The difference is surfaced rather than copied.

## Examples

### Two Norwegian marine protected sites as served by the source service
Tauterryggen (marine protected area) and Møysalen (national park, marine and terrestrial), attributes verbatim from Miljødirektoratet's ArcGIS layer (retrieved 30 Sep 2026); geometry is each site's WGS 84 bounding box. Transforming it with `to-emodnet-nationally-designated-area` reproduces the EMODnet Tauterryggen record (reference records in `emodnet-protected-area.nationally-designated-area`) on every mapped field, and reports for Møysalen the three fields where EMODnet itself is wrong (natdaid, designatio, iucncatego are swapped with the neighbouring landscape protection area in the EEA reporting chain).

#### geojson
```geojson
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 27847,
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              10.457511907153181,
              63.54449862545976
            ],
            [
              10.70521663732499,
              63.54449862545976
            ],
            [
              10.70521663732499,
              63.610169044894384
            ],
            [
              10.457511907153181,
              63.610169044894384
            ],
            [
              10.457511907153181,
              63.54449862545976
            ]
          ]
        ]
      },
      "properties": {
        "naturvernId": "VV00003080",
        "cddaId": "555560034",
        "navn": "Tauterryggen",
        "offisieltNavn": "Tauterryggen marine verneområde",
        "faktaark": "https://faktaark.naturbase.no/?id=VV00003080",
        "verneform": "MarintVerneomraade",
        "verneforskrift": "https://lovdata.no/forskrift/2013-06-21-693",
        "vernedato": 1371772800000,
        "foerstegangVernet": null,
        "verneplan": "MarinVerneplan",
        "kommune": "Frosta (5036),Indre Fosen (5054)",
        "forvaltningsmyndighet": "Statsforvalteren i Trøndelag",
        "forvaltningsmyndighetType": "Statsforvalter",
        "iucn": "IkkeVurdert",
        "revisjon": "IkkeRevidert",
        "truetVurdering": "IkkeTruet",
        "majorEcosystemType": "Marin",
        "GlobalID": "{78721747-9952-4EBA-9F87-350E536170ED}",
        "verneformAggregert": "marintVerneområde",
        "OBJECTID": 27847,
        "NaturvernFKID": "{E2526605-D2F6-4EB7-820C-07F41501AB53}",
        "SHAPE.STArea()": 43775604.353393555,
        "SHAPE.STLength()": 36105.4020980059
      }
    },
    {
      "type": "Feature",
      "id": 28621,
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              15.40355857131027,
              68.47523840481642
            ],
            [
              15.670743627821489,
              68.47523840481642
            ],
            [
              15.670743627821489,
              68.54736979208998
            ],
            [
              15.40355857131027,
              68.54736979208998
            ],
            [
              15.40355857131027,
              68.47523840481642
            ]
          ]
        ]
      },
      "properties": {
        "naturvernId": "VV00002196",
        "cddaId": "183154",
        "navn": "Møysalen",
        "offisieltNavn": "Møysalen nasjonalpark",
        "faktaark": "https://faktaark.naturbase.no/?id=VV00002196",
        "verneform": "Nasjonalpark",
        "verneforskrift": "https://lovdata.no/forskrift/2003-08-29-1100",
        "vernedato": 1062115200000,
        "foerstegangVernet": 1062115200000,
        "verneplan": "VerneplanNasjonalpark",
        "kommune": "Hadsel (1866),Sortland - Suortá (1870),Lødingen (1851),Kvæfjord (5510)",
        "forvaltningsmyndighet": "Møysalen nasjonalparkstyre",
        "forvaltningsmyndighetType": "Nasjonalparkstyre",
        "iucn": "IUCN_II",
        "revisjon": "Revidert",
        "truetVurdering": "IkkeTruet",
        "majorEcosystemType": "MarinOgTerrestrisk",
        "GlobalID": "{03B1D3EA-46B8-46AF-AA3F-441E0A23A98B}",
        "verneformAggregert": "nasjonalpark",
        "OBJECTID": 28621,
        "NaturvernFKID": "{E31F7688-D020-4222-BEDF-6E0C108F0673}",
        "SHAPE.STArea()": 51327048.04296875,
        "SHAPE.STLength()": 37784.19953691021
      }
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/protected-area/source-norway-naturvernomrade/context.jsonld",
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 27847,
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              10.457511907153181,
              63.54449862545976
            ],
            [
              10.70521663732499,
              63.54449862545976
            ],
            [
              10.70521663732499,
              63.610169044894384
            ],
            [
              10.457511907153181,
              63.610169044894384
            ],
            [
              10.457511907153181,
              63.54449862545976
            ]
          ]
        ]
      },
      "properties": {
        "naturvernId": "VV00003080",
        "cddaId": "555560034",
        "navn": "Tauterryggen",
        "offisieltNavn": "Tauterryggen marine verneomr\u00e5de",
        "faktaark": "https://faktaark.naturbase.no/?id=VV00003080",
        "verneform": "MarintVerneomraade",
        "verneforskrift": "https://lovdata.no/forskrift/2013-06-21-693",
        "vernedato": 1371772800000,
        "foerstegangVernet": null,
        "verneplan": "MarinVerneplan",
        "kommune": "Frosta (5036),Indre Fosen (5054)",
        "forvaltningsmyndighet": "Statsforvalteren i Tr\u00f8ndelag",
        "forvaltningsmyndighetType": "Statsforvalter",
        "iucn": "IkkeVurdert",
        "revisjon": "IkkeRevidert",
        "truetVurdering": "IkkeTruet",
        "majorEcosystemType": "Marin",
        "GlobalID": "{78721747-9952-4EBA-9F87-350E536170ED}",
        "verneformAggregert": "marintVerneomr\u00e5de",
        "OBJECTID": 27847,
        "NaturvernFKID": "{E2526605-D2F6-4EB7-820C-07F41501AB53}",
        "SHAPE.STArea()": 43775604.353393555,
        "SHAPE.STLength()": 36105.4020980059
      }
    },
    {
      "type": "Feature",
      "id": 28621,
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              15.40355857131027,
              68.47523840481642
            ],
            [
              15.670743627821489,
              68.47523840481642
            ],
            [
              15.670743627821489,
              68.54736979208998
            ],
            [
              15.40355857131027,
              68.54736979208998
            ],
            [
              15.40355857131027,
              68.47523840481642
            ]
          ]
        ]
      },
      "properties": {
        "naturvernId": "VV00002196",
        "cddaId": "183154",
        "navn": "M\u00f8ysalen",
        "offisieltNavn": "M\u00f8ysalen nasjonalpark",
        "faktaark": "https://faktaark.naturbase.no/?id=VV00002196",
        "verneform": "Nasjonalpark",
        "verneforskrift": "https://lovdata.no/forskrift/2003-08-29-1100",
        "vernedato": 1062115200000,
        "foerstegangVernet": 1062115200000,
        "verneplan": "VerneplanNasjonalpark",
        "kommune": "Hadsel (1866),Sortland - Suort\u00e1 (1870),L\u00f8dingen (1851),Kv\u00e6fjord (5510)",
        "forvaltningsmyndighet": "M\u00f8ysalen nasjonalparkstyre",
        "forvaltningsmyndighetType": "Nasjonalparkstyre",
        "iucn": "IUCN_II",
        "revisjon": "Revidert",
        "truetVurdering": "IkkeTruet",
        "majorEcosystemType": "MarinOgTerrestrisk",
        "GlobalID": "{03B1D3EA-46B8-46AF-AA3F-441E0A23A98B}",
        "verneformAggregert": "nasjonalpark",
        "OBJECTID": 28621,
        "NaturvernFKID": "{E31F7688-D020-4222-BEDF-6E0C108F0673}",
        "SHAPE.STArea()": 51327048.04296875,
        "SHAPE.STLength()": 37784.19953691021
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
@prefix pa-no: <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/27847> a geojson:Feature ;
    foaf:page <https://faktaark.naturbase.no/?id=VV00003080> ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.045751e+01 6.35445e+01 ) ( 1.070522e+01 6.35445e+01 ) ( 1.070522e+01 6.361017e+01 ) ( 1.045751e+01 6.361017e+01 ) ( 1.045751e+01 6.35445e+01 ) ) ) ] ;
    pa:designationDate 1371772800000 ;
    pa:eeaSiteId "555560034" ;
    pa:legalAct <https://lovdata.no/forskrift/2013-06-21-693> ;
    pa:managementAuthority "Statsforvalteren i Trøndelag" ;
    pa:nationalSiteId "VV00003080" ;
    pa-no:iucn <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/iucn/IkkeVurdert> ;
    pa-no:majorEcosystemType <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/ecosystem/Marin> ;
    pa-no:municipality "Frosta (5036),Indre Fosen (5054)" ;
    pa-no:verneform <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/verneform/MarintVerneomraade> ;
    pa:officialSiteName "Tauterryggen marine verneområde" ;
    pa:siteName "Tauterryggen" .

<file:///github/workspace/28621> a geojson:Feature ;
    foaf:page <https://faktaark.naturbase.no/?id=VV00002196> ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.540356e+01 6.847524e+01 ) ( 1.567074e+01 6.847524e+01 ) ( 1.567074e+01 6.854737e+01 ) ( 1.540356e+01 6.854737e+01 ) ( 1.540356e+01 6.847524e+01 ) ) ) ] ;
    pa:designationDate 1062115200000 ;
    pa:eeaSiteId "183154" ;
    pa:legalAct <https://lovdata.no/forskrift/2003-08-29-1100> ;
    pa:managementAuthority "Møysalen nasjonalparkstyre" ;
    pa:nationalSiteId "VV00002196" ;
    pa-no:iucn <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/iucn/IUCN_II> ;
    pa-no:majorEcosystemType <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/ecosystem/MarinOgTerrestrisk> ;
    pa-no:municipality "Hadsel (1866),Sortland - Suortá (1870),Lødingen (1851),Kvæfjord (5510)" ;
    pa-no:verneform <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/verneform/Nasjonalpark> ;
    pa:officialSiteName "Møysalen nasjonalpark" ;
    pa:siteName "Møysalen" .

[] a geojson:FeatureCollection ;
    geojson:features <file:///github/workspace/27847>,
        <file:///github/workspace/28621> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: "Naturvernomr\xE5der source feature (Milj\xF8direktoratet vern layer 0)"
description: 'Source-faithful GeoJSON profile of a Norwegian protected site as served
  by the Seadots pygeoapi collections `no-live-naturvern-omrade` (ESRI provider over
  kart.miljodirektoratet.no/arcgis/rest/services/vern/mapserver/0) and `no-snapshot-naturvern-omrade-marine`
  (GeoPackage snapshot). Field names are the source''s own. The live service gives
  dates as epoch milliseconds and area as `SHAPE.STArea()`; the snapshot gives ISO
  dates and `SHAPE_STArea`. Both are accepted.

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
          type: object
          required:
          - naturvernId
          - navn
          - verneform
          - majorEcosystemType
          - iucn
          properties:
            naturvernId:
              type: string
              pattern: ^VV\d{8}$
              description: National site id (INSPIRE localId).
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/nationalSiteId
            cddaId:
              type:
              - string
              - 'null'
              pattern: ^\d+$
              description: EEA site id; null until the site is reported to the EEA.
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/eeaSiteId
            navn:
              type: string
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/siteName
            offisieltNavn:
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/officialSiteName
            faktaark:
              type:
              - string
              - 'null'
              format: uri
              x-jsonld-id: http://xmlns.com/foaf/0.1/page
              x-jsonld-type: '@id'
            verneform:
              type: string
              enum:
              - Biotopvern
              - BiotopvernSvalbard
              - BiotopvernVilt
              - Dyrefredningsomrade
              - Dyrelivsfredning
              - GeotopvernSvalbard
              - Landskapsvernomraade
              - LandskapsvernomraadeDyrelivsfredning
              - LandskapsvernomraadePlanteOgDyrelivsfredning
              - LandskapsvernomraadePlantelivsfredning
              - MarintVerneomraadeAnnet
              - MarintVerneomraade
              - MidlertidigVernaOmraade
              - Nasjonalpark
              - NasjonalparkSvalbard
              - Naturminne
              - Naturreservat
              - NaturreservatSvalbard
              - PlanteOgDyrefredningsomraade
              - PlanteOgDyrelivsfredning
              - Plantefredningsomraade
              - Plantelivsfredning
              - LandskapsvernomraadeBiotopvern
              - NaturreservatJanMayen
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/verneform
              x-jsonld-type: '@vocab'
              x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/verneform/
            verneforskrift:
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/legalAct
              x-jsonld-type: '@id'
            vernedato:
              type:
              - integer
              - string
              - 'null'
              description: Date of designation (epoch ms or ISO 8601).
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/designationDate
            foerstegangVernet:
              type:
              - integer
              - string
              - 'null'
            verneplan:
              type:
              - string
              - 'null'
            kommune:
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/municipality
            forvaltningsmyndighet:
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/managementAuthority
            forvaltningsmyndighetType:
              type:
              - string
              - 'null'
            iucn:
              type: string
              enum:
              - IUCN_IA
              - IUCN_IB
              - IUCN_II
              - IUCN_III
              - IUCN_IV
              - IUCN_V
              - IUCN_VI
              - IkkeVurdert
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/iucn
              x-jsonld-type: '@vocab'
              x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/iucn/
            majorEcosystemType:
              type: string
              enum:
              - Marin
              - MarinOgTerrestrisk
              - Terrestrisk
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/majorEcosystemType
              x-jsonld-type: '@vocab'
              x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/ecosystem/
            SHAPE.STArea():
              type: number
              description: "Area in m\xB2 (EPSG:25833)."
            SHAPE_STArea:
              type: number
              description: Same as SHAPE.STArea() in the GeoPackage snapshot.
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
  foaf: http://xmlns.com/foaf/0.1/
  pa-no: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/
  dcterms: http://purl.org/dc/terms/
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  xsd: http://www.w3.org/2001/XMLSchema#
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.protected-area.source-norway-naturvernomrade
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-27'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/protected-area/source-norway-naturvernomrade/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/protected-area/source-norway-naturvernomrade/schema.yaml)


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
    "foaf": "http://xmlns.com/foaf/0.1/",
    "pa-no": "pa:no/",
    "dcterms": "http://purl.org/dc/terms/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "naturvernId": "pa:nationalSiteId",
    "cddaId": "pa:eeaSiteId",
    "navn": "pa:siteName",
    "offisieltNavn": "pa:officialSiteName",
    "faktaark": {
      "@id": "foaf:page",
      "@type": "@id"
    },
    "verneform": {
      "@context": {
        "@vocab": "https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/verneform/"
      },
      "@id": "pa:no/verneform",
      "@type": "@vocab"
    },
    "verneforskrift": {
      "@id": "pa:legalAct",
      "@type": "@id"
    },
    "vernedato": "pa:designationDate",
    "kommune": "pa:no/municipality",
    "forvaltningsmyndighet": "pa:managementAuthority",
    "iucn": {
      "@context": {
        "@vocab": "https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/iucn/"
      },
      "@id": "pa:no/iucn",
      "@type": "@vocab"
    },
    "majorEcosystemType": {
      "@context": {
        "@vocab": "https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/no/ecosystem/"
      },
      "@id": "pa:no/majorEcosystemType",
      "@type": "@vocab"
    },
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/protected-area/source-norway-naturvernomrade/context.jsonld)

## Sources

* [Geonorge: Naturvernområder (5857ec0a-8d2c-4cd8-baa2-0dc54ae213b4)](https://kartkatalog.geonorge.no/metadata/5857ec0a-8d2c-4cd8-baa2-0dc54ae213b4)
* [Miljødirektoratet ArcGIS REST vern layer 0](https://kart.miljodirektoratet.no/arcgis/rest/services/vern/mapserver/0)
* [Eionet designation type codes](https://dd.eionet.europa.eu/vocabulary/cdda/designationTypeCodeValue)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/protected-area/source-norway-naturvernomrade`

