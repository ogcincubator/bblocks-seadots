
# EMODnet-compliant nationally designated area (Schema)

`ogc.hosted.seadots.emodnet-protected-area.nationally-designated-area` *v0.1*

GeoJSON Feature profile reproducing the 36-attribute schema of the EMODnet Human Activities layer emodnet:nationallydesignatedareas (EEA Nationally Designated Areas) with unchanged field names and types. Target profile for publishing Norwegian protected sites (Miljødirektoratet Naturvernområder) through OGC API - Features in EMODnet form.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# EMODnet-compliant nationally designated area

Target profile that reproduces the EMODnet Human Activities layer
`emodnet:nationallydesignatedareas`. EMODnet serves the EEA *Nationally
Designated Areas* dataset (formerly CDDA) in this layer, filtered to coastal and
marine sites (`coast_mar = 1`). A feature that validates against this profile has
the same 36 attribute names and primitive types as a feature from the EMODnet WFS
(`outputFormat=application/json`). A client, notebook or GIS style written for
EMODnet therefore reads it unchanged.

## Conformance rules beyond the JSON schema

1. **Complete attribute set.** Every attribute is present, and unknown values are `null`.
   Additional attributes are not allowed, so the source's national fields (e.g.
   `verneforskrift`) must not leak into the EMODnet view. They stay on the source
   collection, which is linked from the view (see `api-collection`).
2. **EMODnet encodings, not national ones.** `majorecosy`, `iucncatego` and
   `iucndesc` use EMODnet's English literals. `designatio` uses EEA designation type
   codes (`NO05`), which the JSON-LD context lifts to
   `http://dd.eionet.europa.eu/vocabulary/cdda/designationTypeCodeValue/NO05`.
3. **One feature per site** as a (Multi)Polygon in CRS84. `geomtype` is `polygon`.
4. **Derived measures are computed as EMODnet computes them.**
   - `sitearea` is in hectares.
   - `marinearea` is the marine share in per cent.
   - `shape_leng` / `shape_area` are planar measures on the lon/lat coordinates
     (degrees / square degrees).
5. **Feature id.** The feature id is `natdaid`. Sites not yet reported to the EEA
   (`natdaid` null) get `<countrycod>-<nationalid>`. Such features are *valid but not yet
   reconcilable* with EMODnet, and the view flags them (see the Norwegian source profile).

## Attributes that cannot come from a national source

EMODnet copies some attributes from the EEA reporting chain (Reportnet). A national
source does not carry them. The Seadots view fills them as follows and documents this
in the collection metadata:

| Attribute | EMODnet meaning | Value in the Seadots view |
|---|---|---|
| `id` | EEA database row id | `null` |
| `metadata_v` | Reportnet dataset snapshot URL | URL of the source dataset metadata record (e.g. the Geonorge record) |
| `metadata_b` | Reportnet snapshot date | Retrieval date of the source data |
| `metadata_s`, `metadata_f` | Reportnet validation status and flag | `null`, because no EEA validation has happened |
| `versionid`, `psversioni`, `metadata_1`, `iucnlink` | usually empty in EMODnet | `null` |

For JSON-LD, the context scopes the EMODnet attribute `id` to `pa:eeaRowId`, so it
does not collide with the feature's `@id`.

## Examples

### Tauterryggen marine protected area as published by EMODnet
A real record from the EMODnet Human Activities WFS (`nationalid = VV00003080`, retrieved 30 Sep 2026), used as the golden target for the Norwegian transform. All attribute values are verbatim. The geometry is the site's WGS 84 bounding box (from the Miljødirektoratet service), not the true boundary, so `shape_leng` and `shape_area` (which EMODnet computed on the true boundary) do not match it.

#### json
```json
{
  "type": "Feature",
  "id": 555560034,
  "geometry": {
    "type": "MultiPolygon",
    "coordinates": [
      [
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
    ]
  },
  "properties": {
    "natdaid": 555560034,
    "countrycod": "NO",
    "country": "Norway",
    "regioncode": "NO",
    "sitename": "Tauterryggen",
    "legalfound": 2013,
    "localid": "VV00003080",
    "namespace": "http://www.miljodirektoratet.no/naturbase",
    "versionid": null,
    "metadata_v": "https://reportnet.europa.eu/dataflow/1752/dataCollection/99142?countryCode=NO&snapshotId=104962&tableName=ProtectedSite",
    "metadata_b": "2026-04-07",
    "metadata_s": "valid",
    "metadata_f": "A",
    "metadata_1": null,
    "geomtype": "polygon",
    "id": 1147327,
    "coast_mar": 1,
    "nationalid": "VV00003080",
    "designated": "Designated site",
    "designatio": "NO05",
    "iucncatego": "notReported",
    "iucndesc": "Not reported",
    "iucnlink": null,
    "sitearea": 4377.56,
    "majorecosy": "Marine",
    "marinearea": 100,
    "spatialdat": "public",
    "spatialres": "Scale larger 100K",
    "pslocalid": "VV00003080",
    "psnamespac": "http://www.miljodirektoratet.no/naturbase",
    "psversioni": null,
    "remark": null,
    "shape_leng": 0.60349362,
    "shape_area": 0.00790442
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/nationally-designated-area/context.jsonld",
  "type": "Feature",
  "id": 555560034,
  "geometry": {
    "type": "MultiPolygon",
    "coordinates": [
      [
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
    ]
  },
  "properties": {
    "natdaid": 555560034,
    "countrycod": "NO",
    "country": "Norway",
    "regioncode": "NO",
    "sitename": "Tauterryggen",
    "legalfound": 2013,
    "localid": "VV00003080",
    "namespace": "http://www.miljodirektoratet.no/naturbase",
    "versionid": null,
    "metadata_v": "https://reportnet.europa.eu/dataflow/1752/dataCollection/99142?countryCode=NO&snapshotId=104962&tableName=ProtectedSite",
    "metadata_b": "2026-04-07",
    "metadata_s": "valid",
    "metadata_f": "A",
    "metadata_1": null,
    "geomtype": "polygon",
    "_emodnetRowId": 1147327,
    "coast_mar": 1,
    "nationalid": "VV00003080",
    "designated": "Designated site",
    "designatio": "NO05",
    "iucncatego": "notReported",
    "iucndesc": "Not reported",
    "iucnlink": null,
    "sitearea": 4377.56,
    "majorecosy": "Marine",
    "marinearea": 100,
    "spatialdat": "public",
    "spatialres": "Scale larger 100K",
    "pslocalid": "VV00003080",
    "psnamespac": "http://www.miljodirektoratet.no/naturbase",
    "psversioni": null,
    "remark": null,
    "shape_leng": 0.60349362,
    "shape_area": 0.00790442
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix eea-desig: <http://dd.eionet.europa.eu/vocabulary/cdda/designationTypeCodeValue/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix pa: <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/> .
@prefix pa-country: <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/country/> .
@prefix pa-iucn: <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/iucn/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/555560034> a geojson:Feature ;
    dcterms:identifier "VV00003080" ;
    geojson:geometry [ a geojson:MultiPolygon ;
            geojson:coordinates ( ( ( ( 1.045751e+01 6.35445e+01 ) ( 1.070522e+01 6.35445e+01 ) ( 1.070522e+01 6.361017e+01 ) ( 1.045751e+01 6.361017e+01 ) ( 1.045751e+01 6.35445e+01 ) ) ) ) ] ;
    schema:addressCountry pa-country:NO ;
    pa:coastalOrMarine 1 ;
    pa:countryName "Norway" ;
    pa:designationStatus "Designated site" ;
    pa:designationType eea-desig:NO05 ;
    pa:eeaRowId 1147327 ;
    pa:eeaSiteId 555560034 ;
    pa:geometryType "polygon" ;
    pa:identifierNamespace "http://www.miljodirektoratet.no/naturbase" ;
    pa:iucnCategory pa-iucn:notReported ;
    pa:iucnCategoryLabel "Not reported" ;
    pa:legalFoundationYear "2013"^^xsd:gYear ;
    pa:majorEcosystemType "Marine" ;
    pa:marineAreaPercent 1e+02 ;
    pa:nationalSiteId "VV00003080" ;
    pa:protectedSiteLocalId "VV00003080" ;
    pa:protectedSiteNamespace "http://www.miljodirektoratet.no/naturbase" ;
    pa:regionCode "NO" ;
    pa:reportingDataset "https://reportnet.europa.eu/dataflow/1752/dataCollection/99142?countryCode=NO&snapshotId=104962&tableName=ProtectedSite" ;
    pa:reportingDate "2026-04-07" ;
    pa:reportingFlag "A" ;
    pa:reportingStatus "valid" ;
    pa:shapeAreaSquareDegrees 7.90442e-03 ;
    pa:shapeLengthDegrees 6.034936e-01 ;
    pa:siteAreaHectares 4.37756e+03 ;
    pa:siteName "Tauterryggen" ;
    pa:spatialDataAccess "public" ;
    pa:spatialResolution "Scale larger 100K" .


```


### EMODnet reference records for Tauterryggen and Møysalen
The EMODnet nationallydesignatedareas records for VV00003080 and VV00002196 (retrieved 30 Sep 2026), used as the reconciliation reference of the Norwegian transform (`emodnetReference`). The Møysalen record carries the EEA reporting-chain error described in `protected-area.source-norway-naturvernomrade`.

#### json
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 555560034,
      "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
          [
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
        ]
      },
      "properties": {
        "natdaid": 555560034,
        "countrycod": "NO",
        "country": "Norway",
        "regioncode": "NO",
        "sitename": "Tauterryggen",
        "legalfound": 2013,
        "localid": "VV00003080",
        "namespace": "http://www.miljodirektoratet.no/naturbase",
        "versionid": null,
        "metadata_v": "https://reportnet.europa.eu/dataflow/1752/dataCollection/99142?countryCode=NO&snapshotId=104962&tableName=ProtectedSite",
        "metadata_b": "2026-04-07",
        "metadata_s": "valid",
        "metadata_f": "A",
        "metadata_1": null,
        "geomtype": "polygon",
        "id": 1147327,
        "coast_mar": 1,
        "nationalid": "VV00003080",
        "designated": "Designated site",
        "designatio": "NO05",
        "iucncatego": "notReported",
        "iucndesc": "Not reported",
        "iucnlink": null,
        "sitearea": 4377.56,
        "majorecosy": "Marine",
        "marinearea": 100,
        "spatialdat": "public",
        "spatialres": "Scale larger 100K",
        "pslocalid": "VV00003080",
        "psnamespac": "http://www.miljodirektoratet.no/naturbase",
        "psversioni": null,
        "remark": null,
        "shape_leng": 0.60349362,
        "shape_area": 0.00790442
      }
    },
    {
      "type": "Feature",
      "id": 183144,
      "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
          [
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
        ]
      },
      "properties": {
        "natdaid": 183144,
        "countrycod": "NO",
        "country": "Norway",
        "regioncode": "NO",
        "sitename": "Møysalen",
        "legalfound": 2003,
        "localid": "VV00002196",
        "namespace": "http://www.miljodirektoratet.no/naturbase",
        "versionid": null,
        "metadata_v": "https://reportnet.europa.eu/dataflow/1752/dataCollection/99142?countryCode=NO&snapshotId=104962&tableName=ProtectedSite",
        "metadata_b": "2026-04-07",
        "metadata_s": "valid",
        "metadata_f": "A",
        "metadata_1": null,
        "geomtype": "polygon",
        "id": 1150571,
        "coast_mar": 1,
        "nationalid": "VV00002196",
        "designated": "Designated site",
        "designatio": "NO02",
        "iucncatego": "V",
        "iucndesc": "Protected Landscape/ Seascape",
        "iucnlink": null,
        "sitearea": 5132.7,
        "majorecosy": "Marine and terrestrial",
        "marinearea": 8.69,
        "spatialdat": "public",
        "spatialres": "Scale larger 100K",
        "pslocalid": "VV00002196",
        "psnamespac": "http://www.miljodirektoratet.no/naturbase",
        "psversioni": null,
        "remark": null,
        "shape_leng": 0.70769049,
        "shape_area": 0.0112638
      }
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/nationally-designated-area/context.jsonld",
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 555560034,
      "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
          [
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
        ]
      },
      "properties": {
        "natdaid": 555560034,
        "countrycod": "NO",
        "country": "Norway",
        "regioncode": "NO",
        "sitename": "Tauterryggen",
        "legalfound": 2013,
        "localid": "VV00003080",
        "namespace": "http://www.miljodirektoratet.no/naturbase",
        "versionid": null,
        "metadata_v": "https://reportnet.europa.eu/dataflow/1752/dataCollection/99142?countryCode=NO&snapshotId=104962&tableName=ProtectedSite",
        "metadata_b": "2026-04-07",
        "metadata_s": "valid",
        "metadata_f": "A",
        "metadata_1": null,
        "geomtype": "polygon",
        "_emodnetRowId": 1147327,
        "coast_mar": 1,
        "nationalid": "VV00003080",
        "designated": "Designated site",
        "designatio": "NO05",
        "iucncatego": "notReported",
        "iucndesc": "Not reported",
        "iucnlink": null,
        "sitearea": 4377.56,
        "majorecosy": "Marine",
        "marinearea": 100,
        "spatialdat": "public",
        "spatialres": "Scale larger 100K",
        "pslocalid": "VV00003080",
        "psnamespac": "http://www.miljodirektoratet.no/naturbase",
        "psversioni": null,
        "remark": null,
        "shape_leng": 0.60349362,
        "shape_area": 0.00790442
      }
    },
    {
      "type": "Feature",
      "id": 183144,
      "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
          [
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
        ]
      },
      "properties": {
        "natdaid": 183144,
        "countrycod": "NO",
        "country": "Norway",
        "regioncode": "NO",
        "sitename": "M\u00f8ysalen",
        "legalfound": 2003,
        "localid": "VV00002196",
        "namespace": "http://www.miljodirektoratet.no/naturbase",
        "versionid": null,
        "metadata_v": "https://reportnet.europa.eu/dataflow/1752/dataCollection/99142?countryCode=NO&snapshotId=104962&tableName=ProtectedSite",
        "metadata_b": "2026-04-07",
        "metadata_s": "valid",
        "metadata_f": "A",
        "metadata_1": null,
        "geomtype": "polygon",
        "_emodnetRowId": 1150571,
        "coast_mar": 1,
        "nationalid": "VV00002196",
        "designated": "Designated site",
        "designatio": "NO02",
        "iucncatego": "V",
        "iucndesc": "Protected Landscape/ Seascape",
        "iucnlink": null,
        "sitearea": 5132.7,
        "majorecosy": "Marine and terrestrial",
        "marinearea": 8.69,
        "spatialdat": "public",
        "spatialres": "Scale larger 100K",
        "pslocalid": "VV00002196",
        "psnamespac": "http://www.miljodirektoratet.no/naturbase",
        "psversioni": null,
        "remark": null,
        "shape_leng": 0.70769049,
        "shape_area": 0.0112638
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix eea-desig: <http://dd.eionet.europa.eu/vocabulary/cdda/designationTypeCodeValue/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix pa: <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/> .
@prefix pa-country: <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/country/> .
@prefix pa-iucn: <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/iucn/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/183144> a geojson:Feature ;
    dcterms:identifier "VV00002196" ;
    geojson:geometry [ a geojson:MultiPolygon ;
            geojson:coordinates ( ( ( ( 1.540356e+01 6.847524e+01 ) ( 1.567074e+01 6.847524e+01 ) ( 1.567074e+01 6.854737e+01 ) ( 1.540356e+01 6.854737e+01 ) ( 1.540356e+01 6.847524e+01 ) ) ) ) ] ;
    schema:addressCountry pa-country:NO ;
    pa:coastalOrMarine 1 ;
    pa:countryName "Norway" ;
    pa:designationStatus "Designated site" ;
    pa:designationType eea-desig:NO02 ;
    pa:eeaRowId 1150571 ;
    pa:eeaSiteId 183144 ;
    pa:geometryType "polygon" ;
    pa:identifierNamespace "http://www.miljodirektoratet.no/naturbase" ;
    pa:iucnCategory pa-iucn:V ;
    pa:iucnCategoryLabel "Protected Landscape/ Seascape" ;
    pa:legalFoundationYear "2003"^^xsd:gYear ;
    pa:majorEcosystemType "Marine and terrestrial" ;
    pa:marineAreaPercent 8.69e+00 ;
    pa:nationalSiteId "VV00002196" ;
    pa:protectedSiteLocalId "VV00002196" ;
    pa:protectedSiteNamespace "http://www.miljodirektoratet.no/naturbase" ;
    pa:regionCode "NO" ;
    pa:reportingDataset "https://reportnet.europa.eu/dataflow/1752/dataCollection/99142?countryCode=NO&snapshotId=104962&tableName=ProtectedSite" ;
    pa:reportingDate "2026-04-07" ;
    pa:reportingFlag "A" ;
    pa:reportingStatus "valid" ;
    pa:shapeAreaSquareDegrees 1.12638e-02 ;
    pa:shapeLengthDegrees 7.076905e-01 ;
    pa:siteAreaHectares 5.1327e+03 ;
    pa:siteName "Møysalen" ;
    pa:spatialDataAccess "public" ;
    pa:spatialResolution "Scale larger 100K" .

<file:///github/workspace/555560034> a geojson:Feature ;
    dcterms:identifier "VV00003080" ;
    geojson:geometry [ a geojson:MultiPolygon ;
            geojson:coordinates ( ( ( ( 1.045751e+01 6.35445e+01 ) ( 1.070522e+01 6.35445e+01 ) ( 1.070522e+01 6.361017e+01 ) ( 1.045751e+01 6.361017e+01 ) ( 1.045751e+01 6.35445e+01 ) ) ) ) ] ;
    schema:addressCountry pa-country:NO ;
    pa:coastalOrMarine 1 ;
    pa:countryName "Norway" ;
    pa:designationStatus "Designated site" ;
    pa:designationType eea-desig:NO05 ;
    pa:eeaRowId 1147327 ;
    pa:eeaSiteId 555560034 ;
    pa:geometryType "polygon" ;
    pa:identifierNamespace "http://www.miljodirektoratet.no/naturbase" ;
    pa:iucnCategory pa-iucn:notReported ;
    pa:iucnCategoryLabel "Not reported" ;
    pa:legalFoundationYear "2013"^^xsd:gYear ;
    pa:majorEcosystemType "Marine" ;
    pa:marineAreaPercent 1e+02 ;
    pa:nationalSiteId "VV00003080" ;
    pa:protectedSiteLocalId "VV00003080" ;
    pa:protectedSiteNamespace "http://www.miljodirektoratet.no/naturbase" ;
    pa:regionCode "NO" ;
    pa:reportingDataset "https://reportnet.europa.eu/dataflow/1752/dataCollection/99142?countryCode=NO&snapshotId=104962&tableName=ProtectedSite" ;
    pa:reportingDate "2026-04-07" ;
    pa:reportingFlag "A" ;
    pa:reportingStatus "valid" ;
    pa:shapeAreaSquareDegrees 7.90442e-03 ;
    pa:shapeLengthDegrees 6.034936e-01 ;
    pa:siteAreaHectares 4.37756e+03 ;
    pa:siteName "Tauterryggen" ;
    pa:spatialDataAccess "public" ;
    pa:spatialResolution "Scale larger 100K" .

[] a geojson:FeatureCollection ;
    geojson:features <file:///github/workspace/183144>,
        <file:///github/workspace/555560034> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EMODnet-compliant nationally designated area
description: 'GeoJSON Feature profile that reproduces the attribute set of the EMODnet
  Human Activities layer `emodnet:nationallydesignatedareas` (EEA Nationally Designated
  Areas, formerly CDDA) with the service''s published field names and primitive types.
  All 36 attributes are present on every feature (null where the value is not known),
  so a client written against the EMODnet WFS reads this API''s features unchanged.

  '
$defs:
  Feature:
    allOf:
    - $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/schema.yaml#/$defs/Feature
    - type: object
      properties:
        id:
          description: 'Feature id. Equals `properties.natdaid` when the site has
            an EEA id; for sites not yet reported to the EEA (natdaid null) it is
            `<countrycod>-<nationalid>`, e.g. `NO-VV00003931`.

            '
          type:
          - integer
          - string
        properties:
          type: object
          additionalProperties: false
          required:
          - natdaid
          - countrycod
          - country
          - regioncode
          - sitename
          - legalfound
          - localid
          - namespace
          - versionid
          - metadata_v
          - metadata_b
          - metadata_s
          - metadata_f
          - metadata_1
          - geomtype
          - id
          - coast_mar
          - nationalid
          - designated
          - designatio
          - iucncatego
          - iucndesc
          - iucnlink
          - sitearea
          - majorecosy
          - marinearea
          - spatialdat
          - spatialres
          - pslocalid
          - psnamespac
          - psversioni
          - remark
          - shape_leng
          - shape_area
          properties:
            natdaid:
              description: EEA site identifier (Norwegian source field cddaId). Null
                for sites not yet reported to the EEA.
              type:
              - integer
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/eeaSiteId
            countrycod:
              description: ISO 3166-1 alpha-2 country code.
              type: string
              pattern: ^[A-Z]{2}$
              x-jsonld-id: https://schema.org/addressCountry
              x-jsonld-type: '@vocab'
              x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/country/
            country:
              description: Country name in English, as published by EMODnet.
              type: string
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/countryName
            regioncode:
              description: Reporting region code; for Norway equal to the country
                code.
              type: string
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/regionCode
            sitename:
              type: string
              minLength: 1
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/siteName
            legalfound:
              description: Year of the legal act that designated the site.
              type:
              - integer
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/legalFoundationYear
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#gYear
            localid:
              description: INSPIRE local identifier of the site (the national site
                id).
              type: string
              x-jsonld-id: http://purl.org/dc/terms/identifier
            namespace:
              description: INSPIRE namespace of the local identifier.
              type: string
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/identifierNamespace
            versionid:
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/versionId
            metadata_v:
              description: EEA reporting-chain field (URL of the reported dataset
                snapshot). See the description for how the Seadots view fills it.
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/reportingDataset
            metadata_b:
              description: EEA reporting-chain field (date, ISO 8601, optionally suffixed
                with Z).
              type:
              - string
              - 'null'
              pattern: ^\d{4}-\d{2}-\d{2}Z?$
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/reportingDate
            metadata_s:
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/reportingStatus
            metadata_f:
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/reportingFlag
            metadata_1:
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/reportingNote
            geomtype:
              type: string
              enum:
              - polygon
              - point
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/geometryType
            id:
              description: 'EEA database row id. Not derivable from national sources;
                null in the Seadots view. In the JSON-LD uplift it is renamed to `_emodnetRowId`
                first (semantic-uplift.yaml), because under the GeoJSON `@nest` context
                `id` would be the Feature''s own `@id`.

                '
              type:
              - integer
              - 'null'
            coast_mar:
              description: 1 when the site is coastal or marine. EMODnet keeps only
                such sites.
              type: integer
              enum:
              - 0
              - 1
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/coastalOrMarine
            nationalid:
              description: National site identifier (Norway naturvernId, e.g. VV00003080).
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/nationalSiteId
            designated:
              type: string
              enum:
              - Designated site
              - Designated Site
              - Proposed site
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/designationStatus
            designatio:
              description: EEA designation type code, bound to http://dd.eionet.europa.eu/vocabulary/cdda/designationTypeCodeValue/{code}.
              type: string
              pattern: ^[A-Z]{2}[0-9A-Z]{2,3}$
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/designationType
              x-jsonld-type: '@vocab'
              x-jsonld-vocab: http://dd.eionet.europa.eu/vocabulary/cdda/designationTypeCodeValue/
            iucncatego:
              type: string
              enum:
              - Ia
              - Ib
              - II
              - III
              - IV
              - V
              - VI
              - notReported
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/iucnCategory
              x-jsonld-type: '@vocab'
              x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/iucn/
            iucndesc:
              type: string
              enum:
              - Strict Nature Reserve
              - Wilderness Area
              - National Park
              - Natural Monument or Feature
              - Habitat/Species Management Area
              - Protected Landscape/ Seascape
              - Protected area with sustainable use of natural resources
              - Not reported
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/iucnCategoryLabel
            iucnlink:
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/iucnCategoryReference
              x-jsonld-type: '@id'
            sitearea:
              description: Site area in hectares.
              type:
              - number
              - 'null'
              minimum: 0
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/siteAreaHectares
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#double
            majorecosy:
              type: string
              enum:
              - Marine
              - Marine and terrestrial
              - Terrestrial
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/majorEcosystemType
            marinearea:
              description: Marine share of the site area, in per cent.
              type:
              - number
              - 'null'
              minimum: 0
              maximum: 100
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/marineAreaPercent
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#double
            spatialdat:
              type: string
              enum:
              - public
              - restricted
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/spatialDataAccess
            spatialres:
              type: string
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/spatialResolution
            pslocalid:
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/protectedSiteLocalId
            psnamespac:
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/protectedSiteNamespace
            psversioni:
              type:
              - string
              - 'null'
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/protectedSiteVersionId
            remark:
              type:
              - string
              - 'null'
              x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#comment
            shape_leng:
              description: Perimeter in degrees, computed planar on the CRS84 geometry
                (as EMODnet does).
              type: number
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/shapeLengthDegrees
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#double
            shape_area:
              description: Area in square degrees, computed planar on the CRS84 geometry
                (as EMODnet does).
              type: number
              x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/shapeAreaSquareDegrees
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#double
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
x-jsonld-extra-terms:
  _emodnetRowId: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/eeaRowId
x-jsonld-prefixes:
  pa: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/
  schema: https://schema.org/
  xsd: http://www.w3.org/2001/XMLSchema#
  dcterms: http://purl.org/dc/terms/
  rdfs: http://www.w3.org/2000/01/rdf-schema#
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.emodnet-protected-area.nationally-designated-area
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-27'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/nationally-designated-area/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/nationally-designated-area/schema.yaml)


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
    "_emodnetRowId": "pa:eeaRowId",
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
    "natdaid": "pa:eeaSiteId",
    "countrycod": {
      "@context": {
        "@vocab": "https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/country/"
      },
      "@id": "schema:addressCountry",
      "@type": "@vocab"
    },
    "country": "pa:countryName",
    "regioncode": "pa:regionCode",
    "sitename": "pa:siteName",
    "legalfound": {
      "@id": "pa:legalFoundationYear",
      "@type": "xsd:gYear"
    },
    "localid": "dct:identifier",
    "namespace": "pa:identifierNamespace",
    "versionid": "pa:versionId",
    "metadata_v": "pa:reportingDataset",
    "metadata_b": "pa:reportingDate",
    "metadata_s": "pa:reportingStatus",
    "metadata_f": "pa:reportingFlag",
    "metadata_1": "pa:reportingNote",
    "geomtype": "pa:geometryType",
    "coast_mar": "pa:coastalOrMarine",
    "nationalid": "pa:nationalSiteId",
    "designated": "pa:designationStatus",
    "designatio": {
      "@context": {
        "@vocab": "http://dd.eionet.europa.eu/vocabulary/cdda/designationTypeCodeValue/"
      },
      "@id": "pa:designationType",
      "@type": "@vocab"
    },
    "iucncatego": {
      "@context": {
        "@vocab": "https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/iucn/"
      },
      "@id": "pa:iucnCategory",
      "@type": "@vocab"
    },
    "iucndesc": "pa:iucnCategoryLabel",
    "iucnlink": {
      "@id": "pa:iucnCategoryReference",
      "@type": "@id"
    },
    "sitearea": {
      "@id": "pa:siteAreaHectares",
      "@type": "xsd:double"
    },
    "majorecosy": "pa:majorEcosystemType",
    "marinearea": {
      "@id": "pa:marineAreaPercent",
      "@type": "xsd:double"
    },
    "spatialdat": "pa:spatialDataAccess",
    "spatialres": "pa:spatialResolution",
    "pslocalid": "pa:protectedSiteLocalId",
    "psnamespac": "pa:protectedSiteNamespace",
    "psversioni": "pa:protectedSiteVersionId",
    "remark": "rdfs:comment",
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
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/emodnet-protected-area/nationally-designated-area/context.jsonld)

## Sources

* [EMODnet nationallydesignatedareas feature type (DescribeFeatureType)](https://ows.emodnet-humanactivities.eu/wfs?request=DescribeFeatureType&typeName=emodnet:nationallydesignatedareas)
* [EEA Nationally designated areas (CDDA/NatDA)](https://www.eea.europa.eu/en/datahub/datahubitem-view/f60cec02-6494-4d08-b12d-17a37012cb28)
* [Eionet designation type codes](https://dd.eionet.europa.eu/vocabulary/cdda/designationTypeCodeValue)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/emodnet-protected-area/nationally-designated-area`

