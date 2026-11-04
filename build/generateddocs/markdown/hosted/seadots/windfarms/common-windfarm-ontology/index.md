
# Windfarm ontology (designated areas and wind turbines) (Model)

`ogc.hosted.seadots.windfarms.common-windfarm-ontology` *v0.2*

Shared ontology for wind farms as designated areas and for individual wind turbines, used by the common-windfarm-designated-area and common-windfarm-turbine building blocks. It aligns EMODnet Human Activities, OpenStreetMap, IHO S-100 and national (NVE, Polish) source properties, with SKOS concept schemes for status, country, rotor axis, source type and location status.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Windfarm ontology

This is the shared ontology `https://w3id.org/ogc/hosted/seadots/windfarm` (prefix `owf:`) behind two schema blocks:

- [common-windfarm-designated-area](../common-windfarm-designated-area/): a wind farm as a designated area or project, without its devices;
- [common-windfarm-turbine](../common-windfarm-turbine/): a single wind turbine, linked to its wind farm.

Each of those blocks has a `context.jsonld` that maps every schema property and every coded value to a term defined here, or to DCAT/Dublin Core and PROV terms (`dcterms:title`, `dcterms:source`, `dcterms:identifier`, `dcterms:description`, `dcterms:modified`, `prov:alternateOf`). INSPIRE code lists are used for coded values, and schema.org appears only as `skos:closeMatch` alignments. The ontology IRI is the `owf:` namespace without `#`, so a w3id lookup of any `owf:` term resolves to this ontology. Its earlier IRI `https://w3id.org/ogc/hosted/seadots/offshore-windfarm` is kept as `owl:priorVersion`.

## Classes

| Class | Meaning | Alignment |
|---|---|---|
| `owf:WindfarmArea` | Wind farm as a designated area or project | [IHO S-100 windfarm](https://registry.iho.int/fdd/view1.do?idx=798&type=1) |
| `owf:WindTurbine` | Single wind turbine at a point | [IHO S-100 wind turbine](https://registry.iho.int/fdd/view5.do?idx=341&type=5&valueType=0) |

## Properties

- **Wind farm** (`rdfs:domain owf:WindfarmArea`):
  - EMODnet attributes: `nTurbines`, `powerMW`, `year`, `updateYear`, `distanceToCoast`, `areaSqKm`, `installationType`, and `shapeLength`/`shapeArea` for the EMODnet service;
  - status and time: `statusDetail`, `statusAsOf`, `yearSemantics`, `yearIsAssumed`, `operationalDate`;
  - organisations: `ownerName`, `developerName`;
  - licensing and administration: `licenceStatus`, `licensingCase`, `administrativeUnit`, `electricityPriceArea`, `meanAnnualProductionGWh`;
  - provenance: `sourceType`, `sourceDataset`, `sourceSnapshotDate`, `locationStatus`, `locationMethod`, `locationReference`.
- **Turbine** (`rdfs:domain owf:WindTurbine`): `turbineReference`, `partOfWindfarm`, `manufacturerName`, `modelName`, `ratedPowerMW`, `hubHeight`, `rotorDiameter`, `rotorAxis`, `commissioningYear`.
- **Shared**: `windfarmName` (sub-property of `dcterms:title`), `operatorName`, `offshore`, `conditionOfFacility`.
- **Country**: `country`, a proxy for INSPIRE CountryCode. INSPIRE publishes that code list without resolvable item URIs, so its values are the `seadots-emodnet:Country` concepts. Each carries the INSPIRE code (EU Interinstitutional Style Guide, e.g. `PL`, `EL`, `UK`) as `skos:notation` and has `skos:exactMatch` to the EU Publications Office country authority.

Quantities carry `qudt:unit` and `qudt:hasQuantityKind`: MW, m, km², GWh. Where the Norwegian ([emodnet-compliant-windfarm-no](../emodnet-compliant-windfarm-no/), `nve:`) or Polish ([emodnet-compliant-windfarm-pl](../emodnet-compliant-windfarm-pl/), `ses:`) blocks define the same property, it is declared `owl:equivalentProperty`. `sourceType` and `locationStatus` take concepts rather than strings, so they only refer to the Polish terms with `rdfs:seeAlso`.

## Concept schemes

| Scheme | Concepts | Used by |
|---|---|---|
| `seadots-emodnet:WindfarmStatus` | Planned, Approved, Construction, Production, TestSuite, Dismantled, each matched to INSPIRE ConditionOfFacilityValue | `status` (designated area) |
| `seadots-emodnet:Country` | Country names returned by the EMODnet windfarms WFS, with INSPIRE CountryCode notation, matched to the EU country authority table | `country` (designated area, EMODnet, PL) |
| INSPIRE ConditionOfFacilityValue | projected, underConstruction, functional, disused, decommissioned | `status` (turbine) |
| `owf:RotorAxis` | HorizontalAxis, VerticalAxis | `rotor_axis` (turbine) |
| `owf:SourceType` | OpenStreetMapSource, EmodnetSource, NationalSource (`osm`, `emodnet`, `national`) | `source_type` (designated area) |
| `owf:LocationStatus` | LocationSourceProvided, LocationMapped, LocationAnticipated, LocationUnmatched | `location_status` (designated area) |

## Sources

* [EMODnet Human Activities — Wind Farms service](https://www.emodnet-humanactivities.eu/)
* [EMODnet windfarms XSD, NOTE XSD does not match Feature services which contain additional 3 fields: ](https://ows.emodnet-humanactivities.eu/wfs?request=DescribeFeatureType&typeName=emodnet:windfarms)
* [EU Publications Office Country authority table](http://publications.europa.eu/resource/authority/country/)
* [IHO windfarm definition in S-100](https://registry.iho.int/fdd/view1.do?idx=798&type=1)
* [IHO wind turbine definition in S-100](https://registry.iho.int/fdd/view5.do?idx=341&type=5&valueType=0)
* [INSPIRE ConditionOfFacilityValue code list](http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue)
* [QUDT units and quantity kinds](https://qudt.org/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/windfarms/common-windfarm-ontology`

