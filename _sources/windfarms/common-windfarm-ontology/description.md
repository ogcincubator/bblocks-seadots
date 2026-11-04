# Windfarm ontology

This is the shared ontology `https://w3id.org/ogc/hosted/seadots/windfarm` (prefix `owf:`) behind two schema blocks:

- [common-windfarm-designated-area](../common-windfarm-designated-area/): a wind farm as a designated area or project, without its devices;
- [common-windfarm-turbine](../common-windfarm-turbine/): a single wind turbine, linked to its wind farm.

Each of those blocks has a `context.jsonld` that maps every schema property and every coded value to a term defined here, or to a standard vocabulary (`schema:name`, `schema:model`, `schema:addressCountry`, `schema:sameAs`, `dcterms:source`, `dcterms:identifier`, `dcterms:description`, `dcterms:modified`). The ontology IRI is the `owf:` namespace without `#`, so a w3id lookup of any `owf:` term resolves to this ontology. Its earlier IRI `https://w3id.org/ogc/hosted/seadots/offshore-windfarm` is kept as `owl:priorVersion`.

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
- **Turbine** (`rdfs:domain owf:WindTurbine`): `turbineReference`, `partOfWindfarm`, `manufacturerName`, `ratedPowerMW`, `hubHeight`, `rotorDiameter`, `rotorAxis`.
- **Shared**: `windfarmName`, `operatorName`, `offshore`, `conditionOfFacility`.

Quantities carry `qudt:unit` and `qudt:hasQuantityKind`: MW, m, km², GWh. Where the Norwegian ([emodnet-compliant-windfarm-no](../emodnet-compliant-windfarm-no/), `nve:`) or Polish ([emodnet-compliant-windfarm-pl](../emodnet-compliant-windfarm-pl/), `ses:`) blocks define the same property, it is declared `owl:equivalentProperty`. `sourceType` and `locationStatus` take concepts rather than strings, so they only refer to the Polish terms with `rdfs:seeAlso`.

## Concept schemes

| Scheme | Concepts | Used by |
|---|---|---|
| `seadots-emodnet:WindfarmStatus` | Planned, Approved, Construction, Production, TestSuite, Dismantled, each matched to INSPIRE ConditionOfFacilityValue | `status` (designated area) |
| `seadots-emodnet:Country` | Country names returned by the EMODnet windfarms WFS, matched to the EU country authority table | `country` (designated area) |
| INSPIRE ConditionOfFacilityValue | projected, underConstruction, functional, disused, decommissioned | `status` (turbine) |
| `owf:RotorAxis` | HorizontalAxis, VerticalAxis | `rotor_axis` (turbine) |
| `owf:SourceType` | OpenStreetMapSource, EmodnetSource, NationalSource (`osm`, `emodnet`, `national`) | `source_type` (designated area) |
| `owf:LocationStatus` | LocationSourceProvided, LocationMapped, LocationAnticipated, LocationUnmatched | `location_status` (designated area) |
