
# Protected-area transform report (Schema)

`ogc.hosted.seadots.protected-area.transform-report` *v0.1*

Report member (`seadotsTransformReport`) that every protected-area transform adds to its output FeatureCollection: which source features were excluded and why, which were routed to another EMODnet layer instead of being duplicated, which are not yet reported to the EEA, which carry an inferred crosswalk value or need a geometric overlay, and where the transformed values differ from the EMODnet record for the same site.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Protected-area transform report

Every protected-area transform returns its output FeatureCollection with one extra member,
`seadotsTransformReport`, that says what the transform did **not** carry over unchanged. The view keeps
the national or regional source values, which are authoritative, and publishes where and why the
result departs from the source or from EMODnet instead of hiding it.

| Member | Written by | Meaning |
|---|---|---|
| `excluded` | Norway | source site left out, with the selection rule (not marine; no EEA designation type) |
| `notYetReportedToEEA` | Norway | site published without an EEA id; feature id `<country>-<nationalid>` |
| `needsMarineAreaOverlay` | Norway | `marinearea` not computed from a coastline overlay |
| `inferredDesignation` | Norway | EEA designation type taken from an *inferred* crosswalk row |
| `differsFromEMODnet` | Norway | field-level differences from the EMODnet record of the same site (`source` value kept, `emodnet` value reported) |
| `routedToNatura2000` | HELCOM layer 190 | Natura 2000 code, published by `emodnet:natura2000areas`; not duplicated |
| `routedToNationallyDesignatedAreas` | HELCOM layer 190 | EEA/WDPA site id, published by `emodnet:nationallydesignatedareas`; not duplicated |
| `unresolvedCode` | HELCOM layer 190 | national code matching no known scheme |
| `noStatusInRegister` | HELCOM layer 190 | HELCOM id without a layer-54 record, so no status; reported, not published |
| `mergedParts` | HELCOM | number of source polygons merged into one MultiPolygon per site |

The source blocks list this block in `dependsOn` because their transforms write the report; their
schemas do not refer to it, as the report is a foreign member of the output FeatureCollection.

The examples are the real reports produced by running each transform on its block's examples.

## Examples

### Report of the Norwegian transform (to-emodnet-nationally-designated-area)
Produced by running `to-emodnet-nationally-designated-area` on the example of `protected-area.source-norway-naturvernomrade` (Tauterryggen and Møysalen, retrieved 30 Sep 2026) with the EMODnet records of `emodnet-protected-area.nationally-designated-area` as reference. It records the Møysalen error in the EEA reporting chain: natdaid, designatio and iucncatego are swapped with the neighbouring site in EMODnet.

#### json
```json
{
  "excluded": [],
  "notYetReportedToEEA": [],
  "needsMarineAreaOverlay": [],
  "inferredDesignation": [],
  "differsFromEMODnet": [
    {
      "nationalid": "VV00002196",
      "fields": {
        "natdaid": {
          "source": 183154,
          "emodnet": 183144
        },
        "designatio": {
          "source": "NO01",
          "emodnet": "NO02"
        },
        "iucncatego": {
          "source": "II",
          "emodnet": "V"
        }
      }
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/protected-area/transform-report/context.jsonld",
  "excluded": [],
  "notYetReportedToEEA": [],
  "needsMarineAreaOverlay": [],
  "inferredDesignation": [],
  "differsFromEMODnet": [
    {
      "nationalid": "VV00002196",
      "fields": {
        "natdaid": {
          "source": 183154,
          "emodnet": 183144
        },
        "designatio": {
          "source": "NO01",
          "emodnet": "NO02"
        },
        "iucncatego": {
          "source": "II",
          "emodnet": "V"
        }
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix pa: <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

[] pa:differsFromEMODnet [ pa:fieldDifferences "{\"designatio\":{\"emodnet\":\"NO02\",\"source\":\"NO01\"},\"iucncatego\":{\"emodnet\":\"V\",\"source\":\"II\"},\"natdaid\":{\"emodnet\":183144,\"source\":183154}}"^^rdf:JSON ;
            pa:nationalSiteId "VV00002196" ] .


```


### Report of the HELCOM transform on layer 190 (to-emodnet-rsc-mpa)
Produced by running `to-emodnet-rsc-mpa` on the layer-190 example of `protected-area.source-helcom-mpa`, joined with its layer-54 example. The Natura 2000 code (Kuršių marios) and the EEA/WDPA id (Fehmarnbelt) are routed to the EMODnet layers that already publish them, instead of being duplicated.

#### json
```json
{
  "routedToNatura2000": [
    {
      "code": "LTSIU0012",
      "name": "Kuršių marios",
      "country": "Lithuania",
      "type": "Unclear",
      "target": "emodnet:natura2000areas?sitecode=LTSIU0012"
    }
  ],
  "routedToNationallyDesignatedAreas": [
    {
      "code": "555638668",
      "name": "Fehmarnbelt",
      "country": "Germany",
      "type": "HELCOM MPA",
      "target": "emodnet:nationallydesignatedareas?natdaid=555638668"
    }
  ],
  "unresolvedCode": [],
  "noStatusInRegister": [],
  "mergedParts": {}
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/protected-area/transform-report/context.jsonld",
  "routedToNatura2000": [
    {
      "code": "LTSIU0012",
      "name": "Kur\u0161i\u0173 marios",
      "country": "Lithuania",
      "type": "Unclear",
      "target": "emodnet:natura2000areas?sitecode=LTSIU0012"
    }
  ],
  "routedToNationallyDesignatedAreas": [
    {
      "code": "555638668",
      "name": "Fehmarnbelt",
      "country": "Germany",
      "type": "HELCOM MPA",
      "target": "emodnet:nationallydesignatedareas?natdaid=555638668"
    }
  ],
  "unresolvedCode": [],
  "noStatusInRegister": [],
  "mergedParts": {}
}
```

#### ttl
```ttl
@prefix pa: <https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

[] pa:mergedParts "{}"^^rdf:JSON ;
    pa:routedToNationallyDesignatedAreas [ pa:countryName "Germany" ;
            pa:routingTarget "emodnet:nationallydesignatedareas?natdaid=555638668" ;
            pa:siteCode "555638668" ;
            pa:siteName "Fehmarnbelt" ;
            pa:sourceDesignationTypeLabel "HELCOM MPA" ] ;
    pa:routedToNatura2000 [ pa:countryName "Lithuania" ;
            pa:routingTarget "emodnet:natura2000areas?sitecode=LTSIU0012" ;
            pa:siteCode "LTSIU0012" ;
            pa:siteName "Kuršių marios" ;
            pa:sourceDesignationTypeLabel "Unclear" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Protected-area transform report
description: 'The `seadotsTransformReport` member of a protected-area transform output.
  Each transform fills the members that apply to it and leaves the others out. Site
  references use the source''s own identifier (`nationalid` for Norwegian sites, `code`
  for HELCOM rows).

  '
type: object
additionalProperties: false
$defs:
  siteRef:
    type: object
    required:
    - code
    properties:
      code:
        type: string
        description: Site code as found in the source.
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/siteCode
      name:
        type: string
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/siteName
      country:
        type: string
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/countryName
      type:
        type: string
        description: Designation type label as found in the source.
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/sourceDesignationTypeLabel
properties:
  excluded:
    description: Source features left out of the output, with the selection rule that
      excluded them.
    type: array
    items:
      type: object
      required:
      - nationalid
      - reason
      properties:
        nationalid:
          type: string
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/nationalSiteId
        reason:
          type: string
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/exclusionReason
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/excludedSite
    x-jsonld-container: '@set'
  notYetReportedToEEA:
    description: National site ids published without an EEA id (feature id `<country>-<nationalid>`).
    type: array
    items:
      type: string
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/notYetReportedToEEA
    x-jsonld-container: '@set'
  needsMarineAreaOverlay:
    description: National site ids whose marine share was not computed from a coastline
      overlay.
    type: array
    items:
      type: string
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/needsMarineAreaOverlay
    x-jsonld-container: '@set'
  inferredDesignation:
    description: Sites whose EEA designation type comes from an *inferred* crosswalk
      row.
    type: array
    items:
      type: object
      required:
      - nationalid
      - verneform
      - designatio
      properties:
        nationalid:
          type: string
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/nationalSiteId
        verneform:
          type: string
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/nationalDesignationType
        designatio:
          type: string
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/designationType
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/inferredDesignation
    x-jsonld-container: '@set'
  differsFromEMODnet:
    description: 'Field-level differences between the transformed feature (source
      values, which are kept) and the EMODnet record for the same site.

      '
    type: array
    items:
      type: object
      required:
      - nationalid
      - fields
      properties:
        nationalid:
          type: string
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/nationalSiteId
        fields:
          type: object
          additionalProperties:
            type: object
            required:
            - source
            - emodnet
            properties:
              source: {}
              emodnet: {}
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/fieldDifferences
          x-jsonld-type: '@json'
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/differsFromEMODnet
    x-jsonld-container: '@set'
  routedToNatura2000:
    description: Rows whose code is a Natura 2000 site code; published by emodnet:natura2000areas,
      not duplicated.
    type: array
    items:
      allOf:
      - $ref: '#/$defs/siteRef'
      - required:
        - target
        properties:
          target:
            type: string
            pattern: ^emodnet:natura2000areas\?sitecode=
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/routingTarget
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/routedToNatura2000
    x-jsonld-container: '@set'
  routedToNationallyDesignatedAreas:
    description: Rows whose code is an EEA/WDPA site id; published by emodnet:nationallydesignatedareas,
      not duplicated.
    type: array
    items:
      allOf:
      - $ref: '#/$defs/siteRef'
      - required:
        - target
        properties:
          target:
            type: string
            pattern: ^emodnet:nationallydesignatedareas\?natdaid=
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/routingTarget
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/routedToNationallyDesignatedAreas
    x-jsonld-container: '@set'
  unresolvedCode:
    description: Rows whose code matches no known scheme (national codes).
    type: array
    items:
      $ref: '#/$defs/siteRef'
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/unresolvedCode
    x-jsonld-container: '@set'
    x-jsonld-extra-terms:
      target: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/routingTarget
  noStatusInRegister:
    description: HELCOM ids with no match in the HELCOM MPA register (layer 54), so
      no status; reported, not published.
    type: array
    items:
      type: object
      required:
      - code
      properties:
        code:
          type: integer
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/siteCode
        name:
          type: string
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/siteName
        country:
          type: string
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/countryName
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/noStatusInRegister
    x-jsonld-container: '@set'
    x-jsonld-extra-terms:
      type: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/sourceDesignationTypeLabel
      target: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/routingTarget
  mergedParts:
    description: Number of source polygons merged into one MultiPolygon, by site code.
    type: object
    additionalProperties:
      type: integer
      minimum: 2
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/mergedParts
    x-jsonld-type: '@json'
x-jsonld-extra-terms:
  seadotsTransformReport: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/transformReport
x-jsonld-prefixes:
  pa: https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.protected-area.transform-report
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-27'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/protected-area/transform-report/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/protected-area/transform-report/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "seadotsTransformReport": "pa:transformReport",
    "excluded": {
      "@context": {
        "nationalid": "pa:nationalSiteId",
        "reason": "pa:exclusionReason"
      },
      "@id": "pa:excludedSite",
      "@container": "@set"
    },
    "notYetReportedToEEA": {
      "@id": "pa:notYetReportedToEEA",
      "@container": "@set"
    },
    "needsMarineAreaOverlay": {
      "@id": "pa:needsMarineAreaOverlay",
      "@container": "@set"
    },
    "inferredDesignation": {
      "@context": {
        "nationalid": "pa:nationalSiteId",
        "verneform": "pa:nationalDesignationType",
        "designatio": "pa:designationType"
      },
      "@id": "pa:inferredDesignation",
      "@container": "@set"
    },
    "differsFromEMODnet": {
      "@context": {
        "nationalid": "pa:nationalSiteId",
        "fields": {
          "@id": "pa:fieldDifferences",
          "@type": "@json"
        }
      },
      "@id": "pa:differsFromEMODnet",
      "@container": "@set"
    },
    "routedToNatura2000": {
      "@context": {
        "code": "pa:siteCode",
        "name": "pa:siteName",
        "country": "pa:countryName",
        "type": "pa:sourceDesignationTypeLabel",
        "target": "pa:routingTarget"
      },
      "@id": "pa:routedToNatura2000",
      "@container": "@set"
    },
    "routedToNationallyDesignatedAreas": {
      "@context": {
        "code": "pa:siteCode",
        "name": "pa:siteName",
        "country": "pa:countryName",
        "type": "pa:sourceDesignationTypeLabel",
        "target": "pa:routingTarget"
      },
      "@id": "pa:routedToNationallyDesignatedAreas",
      "@container": "@set"
    },
    "unresolvedCode": {
      "@context": {
        "code": "pa:siteCode",
        "name": "pa:siteName",
        "country": "pa:countryName",
        "type": "pa:sourceDesignationTypeLabel",
        "target": "pa:routingTarget"
      },
      "@id": "pa:unresolvedCode",
      "@container": "@set"
    },
    "noStatusInRegister": {
      "@context": {
        "code": "pa:siteCode",
        "name": "pa:siteName",
        "country": "pa:countryName",
        "type": "pa:sourceDesignationTypeLabel",
        "target": "pa:routingTarget"
      },
      "@id": "pa:noStatusInRegister",
      "@container": "@set"
    },
    "mergedParts": {
      "@id": "pa:mergedParts",
      "@type": "@json"
    },
    "pa": "https://w3id.org/ogc/hosted/seadots/emodnet-protected-area/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/protected-area/transform-report/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/protected-area/transform-report`

