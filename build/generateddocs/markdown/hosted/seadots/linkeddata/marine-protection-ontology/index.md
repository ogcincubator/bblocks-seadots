
# Marine Protections Ontology (Model)

`ogc.hosted.seadots.linkeddata.marine-protection-ontology` *v0.1*

Example ontology for the regulation of marine managed areas, minting only the terms that have no exact equivalent in the ontologies of the OGC Cross Domain Model. Definitions are taken from the ProtectedSeas Navigator data dictionary.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Marine Protections Ontology

Defines the concepts needed to describe how marine managed areas are regulated, based on the
attributes coded for each site in the [ProtectedSeas Navigator](https://navigatormap.org/data-dictionary/) dataset.

> Note these URIs may be mapped to properties in **any** JSON schema.

### Reuse of the OGC Cross Domain Model

Terms are reused from the ontologies of the [Cross Domain Model](https://github.com/ogcincubator/cross-domain-model)
wherever one means the same thing, and are therefore not declared here:

| Concept | Term | Cross Domain Model block |
|---------|------|--------------------------|
| Site ID | `dct:identifier` | `ogc.model.cross-domain.dcterms` |
| Date of last update | `dct:modified` | `ogc.model.cross-domain.dcterms` |
| Site name | `schema:name` | `ogc.model.cross-domain.schema-org` |
| Country | `schema:addressCountry` | `ogc.model.cross-domain.schema-org` |
| Subnational unit | `schema:addressRegion` | `ogc.model.cross-domain.schema-org` |

Where a term is close but not exact, a local term is minted and aligned to it:

- `rdfs:subPropertyOf` where every value is also a value of the broader term, e.g. `mpr:purpose` to
  `dct:description`, `mpr:wdpaId` to `dct:identifier`, `mpr:siteMajorVersion` to `pav:version`.
- `skos:closeMatch` where the upstream term has a different scope, e.g. `mpr:effectiveFrom` to `schema:validFrom`,
  because seasonal dates recur each year. Likewise `mpr:website` to `schema:url`, because source values may hold
  several URLs.

`mpr:MarineManagedArea` specialises `geo:Feature` (`ogc.model.cross-domain.geosparql`) and `schema:Place`.

### Coded values

Regulation attributes hold integer codes rather than concept IRIs, so that the source data maps directly.
The `mpr:regulationStatuses` scheme documents the codes, with `skos:notation` holding the integer. All such
properties are sub-properties of `mpr:fishingRegulation` or `mpr:marineActivityRegulation`.

### Status of this namespace

`https://w3id.org/ogc/hosted/demo/marine-protections/` is an example namespace. It is not published or endorsed by
ProtectedSeas, and terms do not currently resolve. Labels are in English only, since this is the only language of
the source definitions.

## Examples

### A marine managed area
Uses a subset of the values of the Yurupari - Malpelo site in the
[ProtectedSeas Navigator](https://navigatormap.org/) dataset (CC BY 4.0).
#### turtle
```turtle
<https://w3id.org/ogc/hosted/demo/marine-protections/site/AICOL29> a mpr:MarineManagedArea ;
  dct:identifier "AICOL29" ;
  schema:name "Yurupari - Malpelo" ;
  schema:addressCountry "Colombia" ;
  mpr:category "Marine Protected Area" ;
  mpr:designation "Integrated Management District" ;
  mpr:wdpaId "555636046" ;
  mpr:iucnCategory "VI" ;
  mpr:levelOfFishingProtection 1 ;
  mpr:bottomTrawling 3 ;
  mpr:vesselEntry 3 ;
  mpr:yearEstablished 2017 ;
  dct:modified "2025-09-03"^^xsd:date .

```

## Sources

* [ProtectedSeas Navigator Data Dictionary](https://navigatormap.org/data-dictionary/)
* [ProtectedSeas Navigator Methodology](https://navigatormap.org/methodology/)
* [ProtectedSeas Navigator: What Areas do we Include?](https://navigatormap.org/what-do-we-include/)
* [DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl)
* [Schema.org vocabulary](https://schema.org/version/latest/schemaorg-current-https.ttl)
* [Provenance, Authoring and Versioning (PAV) ontology](https://pav-ontology.github.io/pav/pav.rdf)
* [OGC Cross Domain Model](https://github.com/ogcincubator/cross-domain-model)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/linkeddata/marine-protection-ontology`

