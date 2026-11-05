
# Marine Protection Properties (Schema)

`ogc.hosted.seadots.linkeddata.marineProtectionProperties` *v0.1*

Attributes of a marine managed area in the ProtectedSeas Navigator dataset, including its designation, regulations, fishing protection level and the regulation status of fishing gears and marine activities, bound to the Marine Protections Ontology and the OGC Cross Domain Model.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Marine Protection Properties

The attributes of a site in the ProtectedSeas Navigator dataset, as served by the Ocean Data Platform features API.
The context maps each one to the [Marine Protections Ontology](../marine-protection-ontology) or directly to a term of
the OGC Cross Domain Model.

Property descriptions are taken from the [Navigator data dictionary](https://navigatormap.org/data-dictionary/). API
field names differ from the names in the dictionary, and some correspondences were inferred from their coded values or
content. These are recorded as `skos:editorialNote` in the ontology.

Constraints reflect the dictionary, and were checked against the 1000 items the API returns:

- **Regulation attributes** use the codes Allowed (0), Prohibited (1), Restricted (2), N/A or Unknown (3), and null for
  not yet coded.
- **`tribal_exemptions`** is coded Yes (0), No (1).
- **`level_fishing_protection`** allows 0 as well as the published 1-5 scale, because 0 occurs in the data. Its meaning
  is not documented.
- **`effective_from` and `effective_to`** allow an empty string as well as a date, because it occurs in the data.

`ogc_fid`, `focal_species_tokens` and `geom_complexity` are technical fields of the serving database. They are not in
the dictionary and have no semantic mapping, so are deliberately omitted from the context. Additional properties are
allowed, since the dictionary describes attributes that this API does not serve.

## Examples

### Attributes of a marine managed area
Properties of the Yurupari - Malpelo site, from the
[ProtectedSeas Navigator](https://navigatormap.org/) dataset (CC BY 4.0).
#### json
```json
{
  "ogc_fid": 40496,
  "site_id": "AICOL29",
  "site_name": "Yurupari - Malpelo",
  "country": "Colombia",
  "category_name": "Marine Protected Area",
  "designation": "Integrated Management District",
  "managing_authority": "Parques Nacionales Naturales de Colombia; Autoridad Nacional de Pesca y Acuicultura",
  "state": null,
  "wdpa_id": "555636046",
  "iucn_category": "VI",
  "purpose": "To sustainably and responsibly exploit the populations of straddling, highly migratory, demersal, and other species with fishing potential in the oceanic zone located west of the Yurupar\u00ed and Malpelo ridges in the Colombian Pacific, as a mechanism to contribute to the economic and social development of national fishing activities and as a strategy to help guarantee the country's food security and the conservation of fishery resources. To conserve and understand the ecosystems and species distributed in the oceanic zone located west of the Yurupar\u00ed and Malpelo ridges, as a strategy to conserve the national marine natural heritage in the Eastern Tropical Pacific. To contribute to the ecosystem connectivity of the Eastern Tropical Pacific, as a contribution to the environmental management of the marine territory and to complement other strategies for the conservation of regional biodiversity.",
  "restrictions": "Activities other than those of sustainable use, preservation, restoration, knowledge and enjoyment are prohibited",
  "allowed": "Activities in accordance with the restrictions are allowed.",
  "definitions": "",
  "regulation_titles": "Resoluci\u00f3n 1908 de septiembre 14, 2017 (Original resolution declaring the management area); Resoluci\u00f3n 0670 de junio 28, 2022 (expansion of Yurupari)",
  "regulation_urls": "Original declaration|https://www.minambiente.gov.co/wp-content/uploads/2021/10/Resolucion-1908-de-2017.pdf; Expansion|https://www.minambiente.gov.co/wp-content/uploads/2022/07/Resolucion-0670-de-2022.pdf",
  "urls": "https://www.parquesnacionales.gov.co/nuestros-parques/dmi-yurupari-malpelo/",
  "seasonality": "Year-round",
  "effective_from": null,
  "effective_to": null,
  "protection_focus": "Ecosystem",
  "species_of_concern": "Hawksbill Turtle (Eretmochelys imbricata); Scalloped Hammerhead (Sphyrna lewini); Whale Shark (Rhincodon typus); Green Turtle (Chelonia mydas); Common Thresher Shark (Alopias vulpinus); Bigeye Thresher Shark (Alopias superciliosus); Pelagic Thresher Shark (Alopias pelagicus); Oceanic Whitetip Shark (Carcharhinus longimanus); Giant Manta Ray (Mobula birostris); Bigeye Tuna (Thunnus obesus); Leatherback Turtle (Dermochelys coriacea); Sperm Whale (Physeter macrocephalus); Yellowfin Tuna (Thunnus albacares); Skipjack Tuna (Katsuwonus pelamis); Dorado / Mahi-mahi (Coryphaena hippurus); Wahoo (Acanthocybium solandri); Blue Marlin (Makaira nigricans); White Marlin (Kajikia albida); Striped Marlin (Kajikia audax); Sailfish (Istiophorus platypterus)",
  "focal_species_tokens": "'acanthocybium':69 'albacar':57 'albida':78 'alopia':20,25,30 'audax':82 'bigey':22,42 'birostri':41 'blue':71 'carcharhinus':35 'chelonia':15 'common':17 'coriacea':49 'coryphaena':66 'dermoch':48 'dorado':62 'eretmoch':3 'giant':37 'green':13 'hammerhead':6 'hawksbil':1 'hippurus':67 'imbricata':4 'istiophorus':84 'kajikia':77,81 'katsuwonus':60 'leatherback':46 'lewini':8 'longimanus':36 'macrocephalus':53 'mahi':64,65 'mahi-mahi':63 'makaira':73 'manta':38 'marlin':72,76,80 'mobula':40 'myda':16 'nigrican':74 'obesus':45 'ocean':32 'pelag':27 'pelagicus':31 'pelami':61 'physet':52 'platypterus':85 'ray':39 'rhincodon':11 'sailfish':83 'scallop':5 'shark':10,19,24,29,34 'skipjack':58 'solandri':70 'sperm':50 'sphyrna':7 'stripe':79 'superciliosus':26 'thresher':18,23,28 'thunnus':44,56 'tuna':43,55,59 'turtl':2,14,47 'typus':12 'vulpinus':21 'wahoo':68 'whale':9,51 'white':75 'whitetip':33 'yellowfin':54",
  "government_level": "National",
  "year_established": 2017,
  "other_links": null,
  "level_fishing_protection": 1,
  "recreational_fishing": 3,
  "commercial_fishing": 3,
  "artisanal_fishing": 3,
  "subsistence_fishing": 3,
  "bottom_trawling": 3,
  "pelagic_trawling": 3,
  "hook_and_line": 3,
  "trolling": 3,
  "purse_seine_surrounding_nets": 3,
  "gillnets_entangling_nets": 3,
  "trammel_nets": 3,
  "dip_scoop_nets": 3,
  "cast_nets": 3,
  "drift_nets": 3,
  "other_nets": 3,
  "dredges": 3,
  "traps_pots": 3,
  "spear_fishing": 3,
  "underwater_extraction_diving": 3,
  "hand_capture": 3,
  "fish_aggregating_devices": 3,
  "longlining": 3,
  "gillnetting_legacyV1": 3,
  "nets_other_legacyV1": 3,
  "gear_misc_legacyV1": 3,
  "tribal_exemptions": 1,
  "discharge": 3,
  "vessel_speed": 3,
  "vessel_entry": 3,
  "diving": 3,
  "historic_artifact_removal": 3,
  "vessel_stopping": 3,
  "anchoring": 3,
  "mooring": 3,
  "landing": 3,
  "dredging_dumping": 3,
  "industrial_exploration": 3,
  "industrial_extraction": 1,
  "aquaculture": 3,
  "construction": 3,
  "overflight_drones": 3,
  "anchor_dragging_legacyV1": 3,
  "dredging_legacyV1": 3,
  "drilling_legacyV1": 1,
  "subzone": 0,
  "primary_site_id": null,
  "coastline_match": null,
  "site_location": null,
  "boundary_source": "Registro Unico Nacional de Areas Protegidas",
  "s57_category_legacyV1": 4,
  "site_major_version": 2,
  "site_minor_version": 0,
  "version_start_date": "2025-09-03",
  "change_type_regulations": null,
  "change_type_boundary": null,
  "regulation_updates_legacyV1": null,
  "last_update": "2025-09-03",
  "last_reviewed": "2025-09-03",
  "geom_complexity": 461
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/linkeddata/marineProtectionProperties/context.jsonld",
  "ogc_fid": 40496,
  "site_id": "AICOL29",
  "site_name": "Yurupari - Malpelo",
  "country": "Colombia",
  "category_name": "Marine Protected Area",
  "designation": "Integrated Management District",
  "managing_authority": "Parques Nacionales Naturales de Colombia; Autoridad Nacional de Pesca y Acuicultura",
  "state": null,
  "wdpa_id": "555636046",
  "iucn_category": "VI",
  "purpose": "To sustainably and responsibly exploit the populations of straddling, highly migratory, demersal, and other species with fishing potential in the oceanic zone located west of the Yurupar\u00ed and Malpelo ridges in the Colombian Pacific, as a mechanism to contribute to the economic and social development of national fishing activities and as a strategy to help guarantee the country's food security and the conservation of fishery resources. To conserve and understand the ecosystems and species distributed in the oceanic zone located west of the Yurupar\u00ed and Malpelo ridges, as a strategy to conserve the national marine natural heritage in the Eastern Tropical Pacific. To contribute to the ecosystem connectivity of the Eastern Tropical Pacific, as a contribution to the environmental management of the marine territory and to complement other strategies for the conservation of regional biodiversity.",
  "restrictions": "Activities other than those of sustainable use, preservation, restoration, knowledge and enjoyment are prohibited",
  "allowed": "Activities in accordance with the restrictions are allowed.",
  "definitions": "",
  "regulation_titles": "Resoluci\u00f3n 1908 de septiembre 14, 2017 (Original resolution declaring the management area); Resoluci\u00f3n 0670 de junio 28, 2022 (expansion of Yurupari)",
  "regulation_urls": "Original declaration|https://www.minambiente.gov.co/wp-content/uploads/2021/10/Resolucion-1908-de-2017.pdf; Expansion|https://www.minambiente.gov.co/wp-content/uploads/2022/07/Resolucion-0670-de-2022.pdf",
  "urls": "https://www.parquesnacionales.gov.co/nuestros-parques/dmi-yurupari-malpelo/",
  "seasonality": "Year-round",
  "effective_from": null,
  "effective_to": null,
  "protection_focus": "Ecosystem",
  "species_of_concern": "Hawksbill Turtle (Eretmochelys imbricata); Scalloped Hammerhead (Sphyrna lewini); Whale Shark (Rhincodon typus); Green Turtle (Chelonia mydas); Common Thresher Shark (Alopias vulpinus); Bigeye Thresher Shark (Alopias superciliosus); Pelagic Thresher Shark (Alopias pelagicus); Oceanic Whitetip Shark (Carcharhinus longimanus); Giant Manta Ray (Mobula birostris); Bigeye Tuna (Thunnus obesus); Leatherback Turtle (Dermochelys coriacea); Sperm Whale (Physeter macrocephalus); Yellowfin Tuna (Thunnus albacares); Skipjack Tuna (Katsuwonus pelamis); Dorado / Mahi-mahi (Coryphaena hippurus); Wahoo (Acanthocybium solandri); Blue Marlin (Makaira nigricans); White Marlin (Kajikia albida); Striped Marlin (Kajikia audax); Sailfish (Istiophorus platypterus)",
  "focal_species_tokens": "'acanthocybium':69 'albacar':57 'albida':78 'alopia':20,25,30 'audax':82 'bigey':22,42 'birostri':41 'blue':71 'carcharhinus':35 'chelonia':15 'common':17 'coriacea':49 'coryphaena':66 'dermoch':48 'dorado':62 'eretmoch':3 'giant':37 'green':13 'hammerhead':6 'hawksbil':1 'hippurus':67 'imbricata':4 'istiophorus':84 'kajikia':77,81 'katsuwonus':60 'leatherback':46 'lewini':8 'longimanus':36 'macrocephalus':53 'mahi':64,65 'mahi-mahi':63 'makaira':73 'manta':38 'marlin':72,76,80 'mobula':40 'myda':16 'nigrican':74 'obesus':45 'ocean':32 'pelag':27 'pelagicus':31 'pelami':61 'physet':52 'platypterus':85 'ray':39 'rhincodon':11 'sailfish':83 'scallop':5 'shark':10,19,24,29,34 'skipjack':58 'solandri':70 'sperm':50 'sphyrna':7 'stripe':79 'superciliosus':26 'thresher':18,23,28 'thunnus':44,56 'tuna':43,55,59 'turtl':2,14,47 'typus':12 'vulpinus':21 'wahoo':68 'whale':9,51 'white':75 'whitetip':33 'yellowfin':54",
  "government_level": "National",
  "year_established": 2017,
  "other_links": null,
  "level_fishing_protection": 1,
  "recreational_fishing": 3,
  "commercial_fishing": 3,
  "artisanal_fishing": 3,
  "subsistence_fishing": 3,
  "bottom_trawling": 3,
  "pelagic_trawling": 3,
  "hook_and_line": 3,
  "trolling": 3,
  "purse_seine_surrounding_nets": 3,
  "gillnets_entangling_nets": 3,
  "trammel_nets": 3,
  "dip_scoop_nets": 3,
  "cast_nets": 3,
  "drift_nets": 3,
  "other_nets": 3,
  "dredges": 3,
  "traps_pots": 3,
  "spear_fishing": 3,
  "underwater_extraction_diving": 3,
  "hand_capture": 3,
  "fish_aggregating_devices": 3,
  "longlining": 3,
  "gillnetting_legacyV1": 3,
  "nets_other_legacyV1": 3,
  "gear_misc_legacyV1": 3,
  "tribal_exemptions": 1,
  "discharge": 3,
  "vessel_speed": 3,
  "vessel_entry": 3,
  "diving": 3,
  "historic_artifact_removal": 3,
  "vessel_stopping": 3,
  "anchoring": 3,
  "mooring": 3,
  "landing": 3,
  "dredging_dumping": 3,
  "industrial_exploration": 3,
  "industrial_extraction": 1,
  "aquaculture": 3,
  "construction": 3,
  "overflight_drones": 3,
  "anchor_dragging_legacyV1": 3,
  "dredging_legacyV1": 3,
  "drilling_legacyV1": 1,
  "subzone": 0,
  "primary_site_id": null,
  "coastline_match": null,
  "site_location": null,
  "boundary_source": "Registro Unico Nacional de Areas Protegidas",
  "s57_category_legacyV1": 4,
  "site_major_version": 2,
  "site_minor_version": 0,
  "version_start_date": "2025-09-03",
  "change_type_regulations": null,
  "change_type_boundary": null,
  "regulation_updates_legacyV1": null,
  "last_update": "2025-09-03",
  "last_reviewed": "2025-09-03",
  "geom_complexity": 461
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix mpr: <https://w3id.org/ogc/hosted/demo/marine-protections/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] dcterms:identifier "AICOL29" ;
    dcterms:modified "2025-09-03"^^xsd:date ;
    schema1:addressCountry "Colombia" ;
    schema1:name "Yurupari - Malpelo" ;
    mpr:allowedActivities "Activities in accordance with the restrictions are allowed." ;
    mpr:anchorDragging 3 ;
    mpr:anchoring 3 ;
    mpr:aquaculture 3 ;
    mpr:artisanalFishing 3 ;
    mpr:bottomTrawling 3 ;
    mpr:boundarySource "Registro Unico Nacional de Areas Protegidas" ;
    mpr:castNets 3 ;
    mpr:category "Marine Protected Area" ;
    mpr:commercialFishing 3 ;
    mpr:construction 3 ;
    mpr:designation "Integrated Management District" ;
    mpr:dipScoopNets 3 ;
    mpr:discharge 3 ;
    mpr:diving 3 ;
    mpr:dredges 3 ;
    mpr:dredging 3 ;
    mpr:dredgingDumping 3 ;
    mpr:driftNets 3 ;
    mpr:drilling 1 ;
    mpr:fishAggregatingDevices 3 ;
    mpr:gillnetsEntanglingNets 3 ;
    mpr:gillnetting 3 ;
    mpr:governmentLevel "National" ;
    mpr:handCapture 3 ;
    mpr:historicArtifactRemoval 3 ;
    mpr:hookAndLine 3 ;
    mpr:industrialExploration 3 ;
    mpr:industrialExtraction 1 ;
    mpr:iucnCategory "VI" ;
    mpr:landing 3 ;
    mpr:lastReviewed "2025-09-03"^^xsd:date ;
    mpr:levelOfFishingProtection 1 ;
    mpr:longlining 3 ;
    mpr:managingAuthority "Parques Nacionales Naturales de Colombia; Autoridad Nacional de Pesca y Acuicultura" ;
    mpr:miscellaneousGear 3 ;
    mpr:mooring 3 ;
    mpr:nets 3 ;
    mpr:otherNets 3 ;
    mpr:overflightDrones 3 ;
    mpr:pelagicTrawling 3 ;
    mpr:protectionFocus "Ecosystem" ;
    mpr:purpose "To sustainably and responsibly exploit the populations of straddling, highly migratory, demersal, and other species with fishing potential in the oceanic zone located west of the Yuruparí and Malpelo ridges in the Colombian Pacific, as a mechanism to contribute to the economic and social development of national fishing activities and as a strategy to help guarantee the country's food security and the conservation of fishery resources. To conserve and understand the ecosystems and species distributed in the oceanic zone located west of the Yuruparí and Malpelo ridges, as a strategy to conserve the national marine natural heritage in the Eastern Tropical Pacific. To contribute to the ecosystem connectivity of the Eastern Tropical Pacific, as a contribution to the environmental management of the marine territory and to complement other strategies for the conservation of regional biodiversity." ;
    mpr:purseSeineSurroundingNets 3 ;
    mpr:recreationalFishing 3 ;
    mpr:regulationName "Resolución 1908 de septiembre 14, 2017 (Original resolution declaring the management area); Resolución 0670 de junio 28, 2022 (expansion of Yurupari)" ;
    mpr:regulationUrl "Original declaration|https://www.minambiente.gov.co/wp-content/uploads/2021/10/Resolucion-1908-de-2017.pdf; Expansion|https://www.minambiente.gov.co/wp-content/uploads/2022/07/Resolucion-0670-de-2022.pdf" ;
    mpr:regulatoryDefinitions "" ;
    mpr:restrictions "Activities other than those of sustainable use, preservation, restoration, knowledge and enjoyment are prohibited" ;
    mpr:s57Category 4 ;
    mpr:season "Year-round" ;
    mpr:siteMajorVersion 2 ;
    mpr:siteMinorVersion 0 ;
    mpr:spearFishing 3 ;
    mpr:speciesOfConcern "Hawksbill Turtle (Eretmochelys imbricata); Scalloped Hammerhead (Sphyrna lewini); Whale Shark (Rhincodon typus); Green Turtle (Chelonia mydas); Common Thresher Shark (Alopias vulpinus); Bigeye Thresher Shark (Alopias superciliosus); Pelagic Thresher Shark (Alopias pelagicus); Oceanic Whitetip Shark (Carcharhinus longimanus); Giant Manta Ray (Mobula birostris); Bigeye Tuna (Thunnus obesus); Leatherback Turtle (Dermochelys coriacea); Sperm Whale (Physeter macrocephalus); Yellowfin Tuna (Thunnus albacares); Skipjack Tuna (Katsuwonus pelamis); Dorado / Mahi-mahi (Coryphaena hippurus); Wahoo (Acanthocybium solandri); Blue Marlin (Makaira nigricans); White Marlin (Kajikia albida); Striped Marlin (Kajikia audax); Sailfish (Istiophorus platypterus)" ;
    mpr:subsistenceFishing 3 ;
    mpr:subzone 0 ;
    mpr:trammelNets 3 ;
    mpr:trapsAndPots 3 ;
    mpr:tribalExemptions 1 ;
    mpr:trolling 3 ;
    mpr:underwaterExtractionDiving 3 ;
    mpr:versionStartDate "2025-09-03"^^xsd:date ;
    mpr:vesselEntry 3 ;
    mpr:vesselSpeed 3 ;
    mpr:vesselStopping 3 ;
    mpr:wdpaId "555636046" ;
    mpr:website "https://www.parquesnacionales.gov.co/nuestros-parques/dmi-yurupari-malpelo/" ;
    mpr:yearEstablished 2017 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Attributes of a marine managed area in the ProtectedSeas Navigator dataset,
  as served by the Ocean Data Platform features API.
type: object
properties:
  ogc_fid:
    description: Row identifier of the serving database. Not listed in the Navigator
      data dictionary; a technical field with no semantic mapping.
    type: integer
  site_id:
    description: ProtectedSeas-assigned unique identifier
    type: string
    x-jsonld-id: http://purl.org/dc/terms/identifier
  site_name:
    description: Site name
    type: string
    x-jsonld-id: http://schema.org/name
  country:
    description: Country name
    type: string
    x-jsonld-id: http://schema.org/addressCountry
  category_name:
    description: Site category. The value is the category name from the Navigator
      Site Categories table.
    type: string
    enum:
    - Marine Protected Area
    - Other Effective Area-Based Conservation Area
    - Fisheries Management Area
    - Water Quality/Human Health Area
    - Recreational Area
    - Vessel Restricted Area
    - Vessel Reporting Area
    - Voluntary Conservation Measure Area
    - Jurisdictional Authority Area
    - Other
    - To Be Determined
    - Local Marine Managed Area
    - Marine Spatial Planning Area
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/category
  designation:
    description: Specific site type (e.g. National Marine Sanctuary)
    type:
    - string
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/designation
  managing_authority:
    description: Agency(s) with presiding jurisdiction over this site
    type:
    - string
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/managingAuthority
  state:
    description: Subnational unit name, if applicable (e.g. State, Province)
    type:
    - string
    - 'null'
    x-jsonld-id: http://schema.org/addressRegion
  wdpa_id:
    description: WDPA-assigned unique identifier for site. NULL = Area not included
      in WDPA
    type:
    - string
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/wdpaId
  iucn_category:
    description: IUCN Protected Area Category. 'Unassigned' if no value found, not
      reported, or not applicable
    type:
    - string
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/iucnCategory
  purpose:
    description: Short summary explaining what is special about this marine area;
      number of habitats and endangered species
    type:
    - string
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/purpose
  restrictions:
    description: Lists prohibited or entirely banned marine-related activities (fishing,
      dumping, pollution, anchoring, boating) and outlines restricted commercial and/or
      recreational fishing activities
    type:
    - string
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/restrictions
  allowed:
    description: Lists allowed marine-related activities, including associated licenses/permits
      if applicable
    type:
    - string
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/allowedActivities
  definitions:
    description: Definitions, where necessary and possible, of terms contained in
      'Restrictions' or 'Allowed', e.g. fishing gear, enumerated species, or geographical
      locations
    type:
    - string
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/regulatoryDefinitions
  regulation_titles:
    description: List of names of the relevant regulations that established the site.
      Semicolon-separated.
    type:
    - string
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/regulationName
  regulation_urls:
    description: List of URLs of relevant regulations. Semicolon-separated.
    type:
    - string
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/regulationUrl
  urls:
    description: URL link to the most relevant webpage about the site
    type:
    - string
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/website
  seasonality:
    description: Temporal applicability of the listed restrictions; either Year-round
      (permanent) or Seasonal (only effective between Effective From and Effective
      To dates each year)
    type: string
    enum:
    - Year-round
    - Seasonal
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/season
  effective_from:
    description: Date restrictions begin, if seasonal
    type:
    - string
    - 'null'
    pattern: ^(\d{4}-\d{2}-\d{2})?$
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/effectiveFrom
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
  effective_to:
    description: Date restrictions end, if seasonal
    type:
    - string
    - 'null'
    pattern: ^(\d{4}-\d{2}-\d{2})?$
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/effectiveTo
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
  protection_focus:
    description: The focus of the protection afforded by the site.
    type: string
    enum:
    - Ecosystem
    - Focal Species
    - Human Health
    - Cultural Heritage
    - Human Safety
    - Water Quality
    - Marine Spatial Planning
    - Unknown
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/protectionFocus
  species_of_concern:
    description: General categories of species that are of interest or concern
    type:
    - string
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/speciesOfConcern
  focal_species_tokens:
    description: Search tokens derived from the species of concern. Not listed in
      the Navigator data dictionary; a technical field with no semantic mapping.
    type:
    - string
    - 'null'
  government_level:
    description: Agency(s) level of government. NULL = Not Yet Coded
    type:
    - string
    - 'null'
    enum:
    - National
    - Subnational
    - Local
    - Collaborative Governance
    - Partnership
    - Private
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/governmentLevel
  year_established:
    description: Year the site was first established
    type:
    - integer
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/yearEstablished
  other_links:
    description: Other helpful URL links related to site
    type:
    - string
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/otherLinks
  level_fishing_protection:
    description: An indicator of the strength of fishing regulations, coded on a 1-5
      scale, with higher scores indicating more restrictions and more protection.
    type: integer
    enum:
    - 0
    - 1
    - 2
    - 3
    - 4
    - 5
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/levelOfFishingProtection
  recreational_fishing:
    description: Fishing for recreational purposes - not sold
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/recreationalFishing
  commercial_fishing:
    description: Professional large-scale fisheries that use large, often impactful,
      gear
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/commercialFishing
  artisanal_fishing:
    description: 'Artisanal fisheries are those that use a relatively low level of
      technology: small canoes or boats instead of larger, more powerful vessels;
      no engines or very simple low-power engines; and traditional fishing gear such
      as spears or hand reels, some nets'
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/artisanalFishing
  subsistence_fishing:
    description: Fishing in order to feed the fisher's family - not sold
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/subsistenceFishing
  bottom_trawling:
    description: A fishing practice that herds and captures the target species, like
      ground fish or crabs, by towing a net along the ocean floor
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/bottomTrawling
  pelagic_trawling:
    description: Pelagic or midwater trawling involves towing a large net through
      the water column. Trawls are designed to capture and trap the target species
      inside the codend as the net is hauled through the water
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/pelagicTrawling
  hook_and_line:
    description: A fishing method that catches fish by means of a series of baited
      hooks, which are suspended on lines into the ocean. Excludes trolling and longline,
      which are separate categories
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/hookAndLine
  trolling:
    description: To trail artificial or natural baits behind a moving boat. The bait
      can be made to skip along the surface or trailed below at any depth to just
      above the bottom. A bait or lure trailed behind an angler walking along a pier,
      bridge, or breakwater is also called trolling
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/trolling
  purse_seine_surrounding_nets:
    description: A net that encircles schools of fish
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/purseSeineSurroundingNets
  gillnets_entangling_nets:
    description: Gillnets and entangling nets are walls of netting that hang in the
      water column, typically made of monofilament or multifilament nylon
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/gillnetsEntanglingNets
  trammel_nets:
    description: An entangling net that hangs down in several curtains
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/trammelNets
  dip_scoop_nets:
    description: A bag net with a handle that is used to scoop fish from the water
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/dipScoopNets
  cast_nets:
    description: A net constructed from a series of tailored netting sections joined
      together to produce a cone-shaped net with weights and a drawstring attached
      to the perimeter and cast by a fisher to catch fish
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/castNets
  drift_nets:
    description: A fishing net that drifts with the tide or current and is buoyed
      or attached to a boat
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/driftNets
  other_nets:
    description: Any fishing net types not accounted for
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/otherNets
  dredges:
    description: Dredges are dragged along the seafloor to catch shellfish. Dredges
      are made from an openmouthed frame that scoops shellfish from the seafloor.
      Attached to the back of the frame is a collection area made from metal rings
      or mesh
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/dredges
  traps_pots:
    description: Traps and pots are submerged three-dimensional wire or wood devices
      that permit organisms to enter the enclosure but make escape extremely difficult
      or impossible
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/trapsAndPots
  spear_fishing:
    description: Fishing with a shaft with one or more sharpened points at one end
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/spearFishing
  underwater_extraction_diving:
    description: Fishing or collecting marine life underwater by hand, spear, or harpoon
      gun with or without the use of an underwater breathing device gear
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/underwaterExtractionDiving
  hand_capture:
    description: Fishing or collecting by hand without the use of gear
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/handCapture
  fish_aggregating_devices:
    description: Floating objects that are designed and strategically placed to attract
      pelagic fish. Includes both static and free-floating
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/fishAggregatingDevices
  longlining:
    description: A line that is deployed horizontally to which gangions and hooks
      are attached. A longline may be a bottom longline, i.e., designed for use on
      the bottom, or a pelagic longline, i.e., designed for use off the bottom. The
      longline hauler may be manually, electrically, or hydraulically operated
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/longlining
  gillnetting_legacyV1:
    description: Gillnets are walls of netting that hang in the water column, typically
      made of monofilament or multifilament nylon
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/gillnetting
  nets_other_legacyV1:
    description: Any fishing net types not accounted for
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/nets
  gear_misc_legacyV1:
    description: Any fishing gear not included elsewhere
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/miscellaneousGear
  tribal_exemptions:
    description: Are there tribal exemptions to fishing restrictions? Yes (0); No
      (1); Not Yet Coded (null)
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/tribalExemptions
  discharge:
    description: The deliberate disposal at sea of wastes or other matter from vessels
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/discharge
  vessel_speed:
    description: Speed of vessel. Prohibited (i.e. no transit) (1); Restricted (2);
      N/A or Unknown (3); Not Yet Coded (null)
    type:
    - integer
    - 'null'
    enum:
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/vesselSpeed
  vessel_entry:
    description: Permittance of vessel types to enter or transit the area
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/vesselEntry
  diving:
    description: Recreational, non-extractive, SCUBA diving or freediving
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/diving
  historic_artifact_removal:
    description: Removal of fossils or artifacts
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/historicArtifactRemoval
  vessel_stopping:
    description: Permittance of vessels to stop in area (opposed to continuous transit
      required)
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/vesselStopping
  anchoring:
    description: Holding a vessel in place by mooring it to the seafloor with an anchor
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/anchoring
  mooring:
    description: Securing a vessel to a fixed object, such as a mooring buoy
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/mooring
  landing:
    description: Stopping a vessel to load and unload things or people to/from land
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/landing
  dredging_dumping:
    description: Removal of silt and other material from the bottom of bodies of water
      and/or dumping of dredged material
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/dredgingDumping
  industrial_exploration:
    description: Exploration methods for finding minerals, oil, and gas, for example
      seismic exploration
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/industrialExploration
  industrial_extraction:
    description: Extraction of oil, gas, or minerals
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/industrialExtraction
  aquaculture:
    description: Any type of marine farmed fishing
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/aquaculture
  construction:
    description: Development or construction of new infrastructure
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/construction
  overflight_drones:
    description: Overflight with manned or unmanned aircraft
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/overflightDrones
  anchor_dragging_legacyV1:
    description: Dragging an anchor along the seafloor
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/anchorDragging
  dredging_legacyV1:
    description: Removal of silt and other material from the bottom of bodies of water
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/dredging
  drilling_legacyV1:
    description: Drilling for the purpose of oil or gas extraction
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/drilling
  subzone:
    description: 1 = Subzone, 0 = not a subzone
    type: integer
    enum:
    - 0
    - 1
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/subzone
  primary_site_id:
    description: Site ID of the primary site of a subzone. NULL = not a subzone
    type:
    - string
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/primarySiteId
  coastline_match:
    description: Site boundary does not follow coastline (0); At least part of site
      boundary follows coastline (1)
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/coastlineMatch
  site_location:
    description: Marine (site is either completely or partially offshore) (0); Inland
      Water (main component) (1), Island (2); Inland Terrestrial (main component)
      (3)
    type:
    - integer
    - 'null'
    enum:
    - 0
    - 1
    - 2
    - 3
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/locationType
  boundary_source:
    description: Source of site boundary data
    type: string
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/boundarySource
  s57_category_legacyV1:
    description: S-57 Category
    type:
    - integer
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/s57Category
  site_major_version:
    description: Data major version of site attributes and boundary
    type: integer
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/siteMajorVersion
  site_minor_version:
    description: Data minor version of site attributes and boundary
    type: integer
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/siteMinorVersion
  version_start_date:
    description: Date this version became effective
    type: string
    pattern: ^\d{4}-\d{2}-\d{2}$
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/versionStartDate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
  change_type_regulations:
    description: Site regulations change between versions
    type:
    - string
    - 'null'
    enum:
    - Correction
    - Regulation Increase
    - Regulation Decrease
    - Regulation Neutral
    - New Site
    - Removed Site
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/changeTypeRegulations
  change_type_boundary:
    description: Site boundary change between versions
    type:
    - string
    - 'null'
    enum:
    - Correction
    - Boundary Increase
    - Boundary Decrease
    - Boundary Neutral
    - New Site
    - Removed Site
    - null
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/changeTypeBoundary
  regulation_updates_legacyV1:
    description: Email, phone number, and/or mailing lists to receive the latest updates
      on regulations regarding removal of marine life
    type:
    - string
    - 'null'
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/latestUpdates
  last_update:
    description: Date of the most recent site attributes update
    type:
    - string
    - 'null'
    pattern: ^\d{4}-\d{2}-\d{2}$
    x-jsonld-id: http://purl.org/dc/terms/modified
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
  last_reviewed:
    description: Date of most recent ProtectedSeas review
    type: string
    pattern: ^\d{4}-\d{2}-\d{2}$
    x-jsonld-id: https://w3id.org/ogc/hosted/demo/marine-protections/lastReviewed
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
  geom_complexity:
    description: Geometry complexity measure of the serving database (the sample value
      equals the vertex count of the geometry). Not listed in the Navigator data dictionary;
      a technical field with no semantic mapping.
    type: integer
required:
- site_id
- site_name
- country
- category_name
- level_fishing_protection
x-jsonld-prefixes:
  dct: http://purl.org/dc/terms/
  schema: http://schema.org/
  mpr: https://w3id.org/ogc/hosted/demo/marine-protections/
  xsd: http://www.w3.org/2001/XMLSchema#
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.linkeddata.marineProtectionProperties
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-05'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/linkeddata/marineProtectionProperties/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/linkeddata/marineProtectionProperties/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "site_id": "dct:identifier",
    "site_name": "schema:name",
    "country": "schema:addressCountry",
    "category_name": "mpr:category",
    "designation": "mpr:designation",
    "managing_authority": "mpr:managingAuthority",
    "state": "schema:addressRegion",
    "wdpa_id": "mpr:wdpaId",
    "iucn_category": "mpr:iucnCategory",
    "purpose": "mpr:purpose",
    "restrictions": "mpr:restrictions",
    "allowed": "mpr:allowedActivities",
    "definitions": "mpr:regulatoryDefinitions",
    "regulation_titles": "mpr:regulationName",
    "regulation_urls": "mpr:regulationUrl",
    "urls": "mpr:website",
    "seasonality": "mpr:season",
    "effective_from": {
      "@id": "mpr:effectiveFrom",
      "@type": "xsd:date"
    },
    "effective_to": {
      "@id": "mpr:effectiveTo",
      "@type": "xsd:date"
    },
    "protection_focus": "mpr:protectionFocus",
    "species_of_concern": "mpr:speciesOfConcern",
    "government_level": "mpr:governmentLevel",
    "year_established": "mpr:yearEstablished",
    "other_links": "mpr:otherLinks",
    "level_fishing_protection": "mpr:levelOfFishingProtection",
    "recreational_fishing": "mpr:recreationalFishing",
    "commercial_fishing": "mpr:commercialFishing",
    "artisanal_fishing": "mpr:artisanalFishing",
    "subsistence_fishing": "mpr:subsistenceFishing",
    "bottom_trawling": "mpr:bottomTrawling",
    "pelagic_trawling": "mpr:pelagicTrawling",
    "hook_and_line": "mpr:hookAndLine",
    "trolling": "mpr:trolling",
    "purse_seine_surrounding_nets": "mpr:purseSeineSurroundingNets",
    "gillnets_entangling_nets": "mpr:gillnetsEntanglingNets",
    "trammel_nets": "mpr:trammelNets",
    "dip_scoop_nets": "mpr:dipScoopNets",
    "cast_nets": "mpr:castNets",
    "drift_nets": "mpr:driftNets",
    "other_nets": "mpr:otherNets",
    "dredges": "mpr:dredges",
    "traps_pots": "mpr:trapsAndPots",
    "spear_fishing": "mpr:spearFishing",
    "underwater_extraction_diving": "mpr:underwaterExtractionDiving",
    "hand_capture": "mpr:handCapture",
    "fish_aggregating_devices": "mpr:fishAggregatingDevices",
    "longlining": "mpr:longlining",
    "gillnetting_legacyV1": "mpr:gillnetting",
    "nets_other_legacyV1": "mpr:nets",
    "gear_misc_legacyV1": "mpr:miscellaneousGear",
    "tribal_exemptions": "mpr:tribalExemptions",
    "discharge": "mpr:discharge",
    "vessel_speed": "mpr:vesselSpeed",
    "vessel_entry": "mpr:vesselEntry",
    "diving": "mpr:diving",
    "historic_artifact_removal": "mpr:historicArtifactRemoval",
    "vessel_stopping": "mpr:vesselStopping",
    "anchoring": "mpr:anchoring",
    "mooring": "mpr:mooring",
    "landing": "mpr:landing",
    "dredging_dumping": "mpr:dredgingDumping",
    "industrial_exploration": "mpr:industrialExploration",
    "industrial_extraction": "mpr:industrialExtraction",
    "aquaculture": "mpr:aquaculture",
    "construction": "mpr:construction",
    "overflight_drones": "mpr:overflightDrones",
    "anchor_dragging_legacyV1": "mpr:anchorDragging",
    "dredging_legacyV1": "mpr:dredging",
    "drilling_legacyV1": "mpr:drilling",
    "subzone": "mpr:subzone",
    "primary_site_id": "mpr:primarySiteId",
    "coastline_match": "mpr:coastlineMatch",
    "site_location": "mpr:locationType",
    "boundary_source": "mpr:boundarySource",
    "s57_category_legacyV1": "mpr:s57Category",
    "site_major_version": "mpr:siteMajorVersion",
    "site_minor_version": "mpr:siteMinorVersion",
    "version_start_date": {
      "@id": "mpr:versionStartDate",
      "@type": "xsd:date"
    },
    "change_type_regulations": "mpr:changeTypeRegulations",
    "change_type_boundary": "mpr:changeTypeBoundary",
    "regulation_updates_legacyV1": "mpr:latestUpdates",
    "last_update": {
      "@id": "dct:modified",
      "@type": "xsd:date"
    },
    "last_reviewed": {
      "@id": "mpr:lastReviewed",
      "@type": "xsd:date"
    },
    "dct": "http://purl.org/dc/terms/",
    "schema": "http://schema.org/",
    "mpr": "https://w3id.org/ogc/hosted/demo/marine-protections/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/linkeddata/marineProtectionProperties/context.jsonld)

## Sources

* [ProtectedSeas Navigator Data Dictionary](https://navigatormap.org/data-dictionary/)
* [Sample items from the Ocean Data Platform features API](https://api.hubocean.earth/api/features/collections/a608f54b-75c7-4df9-a3a8-cedbfa391873/items?limit=1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/linkeddata/marineProtectionProperties`

