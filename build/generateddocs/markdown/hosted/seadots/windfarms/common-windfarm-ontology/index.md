
# Offshore Windfarm (OWF) and Wind Turbine (WT) ontology with properties available in IHO, EmodNet, OpenStreetMaps, national sources (Model)

`ogc.hosted.seadots.windfarms.common-windfarm-ontology` *v0.1*

Ontology defined terms for Offshore Windfarm (OWF) and Wind Turbine (WT) with properties available in IHO, EmodNet, OpenStreetMaps, national sources.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# EMODnet windfarm

This is the single EMODnet windfarm representation in this register. It is a
GeoJSON representation aligned with the official EMODnet Human Activities
windfarms XSD. It uses the service's published attribute names and primitive
types and maps the official `the_geom` concept to GeoJSON `geometry`.

The XSD fields are optional and nillable, and the schema reflects that. The
`country` value is represented as the source country name, not as an ISO code;
the underlying field is a nullable `xsd:string`. `context.jsonld` and
`ontology.ttl` bind country names currently observed in the live service to the
[EU Publications Office Country authority table](http://publications.europa.eu/resource/authority/country/).

The properties are `country`, `n_turbines`, `power_mw`, `status`, `type_inst`,
`updateyear`, `year`, `dist_coast`, and `notes`.

Source-specific extracts, such as the Baltic exercise CSV, are translated into
this representation before being served. Their column mapping is exercise
configuration, not a second EMODnet data model.

The independent [`emodnet-compliant-windfarm-pl`](../emodnet-compliant-windfarm-pl/)
block uses this representation for Polish national-source integration, adding
project names, reporting details, provenance, and location matching. The
independent [`emodnet-compliant-windfarm-no`](../emodnet-compliant-windfarm-no/)
block demonstrates the same base model with Norwegian NVE source details.

This block is intended for publication as a GeoJSON Feature or WFS feature and
as an interchange layer before downstream semantic enrichment.

## Examples

### EMODnet sample windfarm feature
An example does not mirrors the official EMODnet windfarms XSD field names and uses the same geometry-to-attribute mapping as the service.

#### json
*Snippet unavailable: [Errno 2] No such file or directory: '/github/workspace/_sources/windfarms/common-windfarm-ontology/examples/operational-offshore-wind-farm.json'*


### Ocean Data Platform sample windfarm feature taken from EMODnet
this is real data from the 

#### json
*Snippet unavailable: [Errno 2] No such file or directory: '/github/workspace/_sources/windfarms/common-windfarm-ontology/examples/ocean_data_hub-windfarms.json'*

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EMODnet windfarm feature
description: 'GeoJSON representation of the EMODnet Human Activities windfarms feature
  type. Property names, optionality, nullability, and value types follow the service''s
  published windfarms XSD.

  '
allOf:
- $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.yaml
- type: object
  required:
  - properties
  properties:
    properties:
      type: object
      properties:
        country:
          type:
          - string
          - 'null'
          description: Country name as published by EMODnet; the XSD type is nullable
            xsd:string.
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
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#powerMW
        status:
          type:
          - string
          - 'null'
          description: Status text as published by EMODnet (nullable xsd:string).
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
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#distanceToCoast
        notes:
          type:
          - string
          - 'null'
          x-jsonld-id: http://purl.org/dc/terms/description
        shape_leng:
          type:
          - number
          - 'null'
        shape_area:
          type:
          - number
          - 'null'
        name:
          type:
          - string
          - 'null'
        area_sqkm:
          type:
          - number
          - 'null'
      x-jsonld-id: https://purl.org/geojson/vocab#properties
    additionalProperties: {}
x-jsonld-extra-terms:
  id: '@id'
  type: '@type'
  Feature: https://purl.org/geojson/vocab#Feature
  Point: https://purl.org/geojson/vocab#Point
  Polygon: https://purl.org/geojson/vocab#Polygon
  MultiPolygon: https://purl.org/geojson/vocab#MultiPolygon
  geometry: https://purl.org/geojson/vocab#geometry
  coordinates:
    x-jsonld-id: https://purl.org/geojson/vocab#coordinates
    x-jsonld-container: '@list'
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/emodnet/
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  schema: https://schema.org/
  seadots: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#
  dcterms: http://purl.org/dc/terms/
  seadots-emodnet: https://w3id.org/ogc/hosted/seadots/emodnet/
  inspire-cofv: http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.windfarms.common-windfarm-ontology
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-05'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/common-windfarm-ontology/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/common-windfarm-ontology/schema.yaml)


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
        "notes": "dct:description"
      },
      "@id": "geojson:properties"
    },
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
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "schema": "https://schema.org/",
    "seadots": "https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#",
    "dcterms": "http://purl.org/dc/terms/",
    "seadots-emodnet": "https://w3id.org/ogc/hosted/seadots/emodnet/",
    "inspire-cofv": "http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/common-windfarm-ontology/context.jsonld)

## Sources

* [EMODnet Human Activities — Wind Farms service](https://www.emodnet-humanactivities.eu/)
* [EMODnet windfarms XSD, NOTE XSD does not match Feature services which contain additional 3 fields: ](https://ows.emodnet-humanactivities.eu/wfs?request=DescribeFeatureType&typeName=emodnet:windfarms)
* [EU Publications Office Country authority table](http://publications.europa.eu/resource/authority/country/)
* [IHO windfarm definition in S-100](https://registry.iho.int/fdd/view1.do?idx=798&type=1)
* [IHO wind turbine definition in S-100](https://registry.iho.int/fdd/view5.do?idx=341&type=5&valueType=0)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/windfarms/common-windfarm-ontology`

