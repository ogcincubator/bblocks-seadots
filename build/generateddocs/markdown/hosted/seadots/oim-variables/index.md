
# OIM Variables (Model)

`ogc.hosted.seadots.oim-variables` *v0.1*

Defines the OIM variable and indicator concept model for SEADOTS and ILIAD variable observations.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## OIM Variables and Indicators

This building block captures the OIM variable and indicator concept model used by the SEADOTS/ILIAD ecosystem. It defines observation properties, indicator concepts, and relationship edges in RDF, using SKOS, SOSA, PROV, and OWL class/property declarations.

The block is intended as a reusable semantic model for variable metadata, indicator definitions, and graph relationships between observed properties.

## Examples

### SEADOTS variable and indicator graph
#### ttl
```ttl
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix quantitykind: <http://qudt.org/vocab/quantitykind/> .
@prefix indo: <https://w3id.org/indicators/marine/obs/> .
@prefix indp: <https://w3id.org/indicators/marine/parameters/> .
@prefix ind: <https://w3id.org/indicators/marine/> .
@prefix inda: <https://w3id.org/indicators/marine/activity/> .
@prefix indr: <https://w3id.org/indicators/marine/relationships/> .
@prefix prop-rel: <https://w3id.org/ogc/hosted/seadots/prop-rel/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prez: <https://prez.dev> .
@prefix ssn: <http://www.w3.org/ns/ssn/> .
@prefix im: <https://w3id.org/indicators/marine/indicator-model/> .
@prefix dapsim: <https://w3id.org/indicators/marine/dapsim/> .
@prefix dwc: <http://rs.tdwg.org/dwc/terms/> .
@prefix sdn: <https://vocab.nerc.ac.uk/collection/SDN/current/> .


# --- CLASS DECLARATIONS ---
# Three semantic categories used in this register:
#   * Indicator           — high-level aggregated / derived KPI (sosa:ObservableProperty)
#   * ObservableProperty  — measured / observed state variable (sosa:ObservableProperty)
#   * Property            — model parameter, scenario switch, or configuration (ssn:Property)
ind:Indicator a owl:Class ;
    rdfs:subClassOf sosa:ObservableProperty ;
    rdfs:label "Indicator"@en ;
    skos:definition "A high-level aggregated or derived observable used as a KPI for decision-making."@en .

# --- CATALOG ENTRY (added for VocPrez/Prez UI visibility) ---
ind:catalog a dcat:Catalog ;
    rdfs:label "SEADOTS Resource Catalog"@en ;
    dcterms:title "SEADOTS Resource Catalog"@en ;
    dcterms:description "Main catalog for SEADOTS indicators and concepts."@en ;
    # Prez often needs dcterms:hasPart to show members in the list
    dcterms:hasPart ind:indicators-scheme ; 
    dcterms:hasPart ind:parameters-scheme ; 
    dcterms:hasPart ind:ind-rel-scheme ; 
    dcat:dataset ind:indicators-scheme ;
    dcat:dataset ind:parameters-scheme ;
    dcat:dataset ind:ind-rel-scheme ;
    dcat:dataset ind:ind-rel-scheme .

# --- SCHEME CONFIGURATION ---
ind:indicators-scheme a skos:ConceptScheme ;
    dcterms:isPartOf ind:catalog ; # Backlink for discovery
    skos:prefLabel "SEADOTS Indicator Scheme"@en ;
    skos:definition "A concept scheme for SEADOTS indicator concepts and observed properties."@en ;
    # --- TOP CONCEPTS (added for VocPrez/Prez UI visibility) ---
    # Only concepts WITHOUT skos:broader are listed — narrowers are reached via skos:broader.
    skos:hasTopConcept indo:number-of-jobs ,
                       indo:fisheries-production ,
                       indo:bird-tourism ,
                       indo:baseline-benthic-biomass-density ,
                       indo:floating-wind-reef-biomass-effect ,
                       # --- generic abstracts (narrowers reach them via skos:broader) ---
                       indo:fish-catch ,
                       indo:fish-landing-value ,
                       indo:fleet-value-added ,
                       indo:fleet-fuel-consumption ,
                       indo:fleet-fishing-radius ,
                       indo:fish-market-state ,
                       indo:fish-ex-vessel-price ,
                       indo:fish-stock-biomass ,
                       indo:fish-stock-growth-rate ,
                       indo:fish-stock-carrying-capacity-increment ,
                       indo:fish-stock-growth-suppression-flag ,
                       indo:fishing-season-state ,
                       indo:implemented-herring-tac ,
                       indo:herring-tac-increment ,
                       # --- non-grouped top observables (no broader anywhere) ---
                       indo:fuel_price ,
                       indo:winter_closure_length ,
                       indo:TAC_share_B_herring ,
                       indo:TAC_herring_est_error ,
                       indo:TAC_herring_type .

# --- SCHEME CONFIGURATION ---
ind:parameters-scheme a skos:ConceptScheme ;
    dcterms:isPartOf ind:catalog ; # Backlink for discovery
    skos:prefLabel "SEADOTS Models Parameters Scheme"@en ;
    skos:definition "A concept scheme for SEADOTS Digital Twins' parameters. Parameters can be sourced starting conditions, sourced time series of conditions for the period of simulations or model specific parameters including expert knowledge sourced factors."@en ;
    # --- TOP CONCEPTS (added for VocPrez/Prez UI visibility) ---
    # Only concepts WITHOUT skos:broader are listed — narrowers are reached via skos:broader.
    skos:hasTopConcept indp:number-of-turbines ,
                       indp:area-use-by-wind-park ,
                       indp:submerged-infrastructure-area ,
                       indp:reef-aggregation-index ,
                       indp:colonisation-time-factor ,
                       indp:repetitions ,
                       indp:ticks ,
                       indp:current_management_season ,
                       # --- generic abstracts (narrowers reach them via skos:broader) ---
                       indp:total-allowable-catch ,
                       indp:dispersal_rate_property ,
                       indp:closure_type_property ,
                       # --- non-grouped top parameters (no broader anywhere) ---
                       indp:trawling_limit ,
                       indp:fishing_algorithm ,
                       indp:current_year ,
                       indp:current_month ,
                       indp:year_tick ,
                       indp:reserved-for-future-use .

# --- Indicators (ind:Indicator, sosa:ObservableProperty) — high-level KPIs ---

indo:number-of-jobs a ind:Indicator, sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Number of jobs"@en ;
    skos:prefLabel "Number of jobs"@en ;
    skos:inScheme ind:indicators-scheme .

indo:bird-tourism a ind:Indicator, sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Bird tourism"@en ;
    skos:prefLabel "Bird tourism"@en ;
    skos:inScheme ind:indicators-scheme .

indo:fisheries-production a ind:Indicator, sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Fisheries production"@en ;
    skos:prefLabel "Fisheries production"@en ;
    skos:inScheme ind:indicators-scheme ;
    rdfs:comment "The amount of fish caught in a given area over a specific period of time." ;
    rdfs:seeAlso <https://en.wikipedia.org/wiki/Fisheries_production> ;
    owl:sameAs <http://aims.fao.org/aos/agrovoc/c_2934> ;
    skos:scopeNote "Concept definition adapted from AGROVOC and the SeaDOTs cross-impact model." ;
    prov:wasAttributedTo <http://seadots.eu> .

indo:fish-catch a ind:Indicator, sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Fish catch by fleet"@en ;
    skos:prefLabel "Fish catch by fleet"@en ;
    skos:definition "Abstract concept: mass of fish caught by a national fleet during a reporting tick, before specialisation by country or target species."@en ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Mass ;
    skos:narrower indo:catch_herring_SV_All ,
                              indo:catch_herring_LV_All ,
                              indo:catch_sprat_SV_All ,
                              indo:catch_sprat_LV_All .


indp:herring-tac skos:narrower indp:current_TAC_herring ,
                               indp:TAC_herring_share .

# --- Properties (ssn:Property) — model parameters / scenario controls / configuration ---
# These belong to ind:parameters-scheme.

indp:number-of-turbines a ssn:Property, skos:Concept ;
    rdfs:label "Number of turbines"@en ;
    skos:prefLabel "Number of turbines"@en ;
    skos:definition "Configured number of wind turbines in the simulated wind park."@en ;
    skos:inScheme ind:parameters-scheme .

indp:area-use-by-wind-park a ssn:Property, skos:Concept ;
    rdfs:label "Area used by wind park"@en ;
    skos:prefLabel "Area used by wind park"@en ;
    skos:definition "Configured sea-surface area allocated to the simulated wind park."@en ;
    skos:inScheme ind:parameters-scheme ;
    qudt:hasQuantityKind quantitykind:Area .

indp:total-allowable-catch a ssn:Property, skos:Concept ;
    rdfs:label "Total Allowable Catch (TAC)"@en ;
    skos:prefLabel "Total Allowable Catch (TAC)"@en ;
    skos:definition "Abstract management parameter: the maximum catch permitted under a fisheries-management rule, before specialisation by stock, country, or rule variant."@en ;
    skos:inScheme ind:parameters-scheme ;
    qudt:hasQuantityKind quantitykind:Mass ;
    skos:narrower indp:herring-tac ,
                indp:current_TAC_herring ,
                indp:TAC_herring_share .

indp:herring-tac a ssn:Property, skos:Concept ;
    rdfs:label "Herring TAC"@en ;
    skos:prefLabel "Herring TAC"@en ;
    skos:definition "Abstract management parameter: any Total Allowable Catch quantity or parameter specific to the herring stock."@en ;
    skos:broader indp:total-allowable-catch ;
    skos:inScheme ind:parameters-scheme ;
    qudt:hasQuantityKind quantitykind:Mass .



indo:fish-stock-biomass a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Fish stock biomass"@en ;
    skos:prefLabel "Fish stock biomass"@en ;
    skos:definition "Abstract concept: biomass of a simulated fish stock, before specialisation by species or spatial aggregation."@en ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Mass ;
    skos:broader "https://agrovoc.fao.org/browse/agrovoc/en/page/c_24251" ;
    skos:related "http://vocab.nerc.ac.uk/collection/S06/current/S0600087/" ;
    skos:related "http://vocab.nerc.ac.uk/collection/S06/current/S0600086/" ;
    skos:related "https://ec.europa.eu/eurostat/databrowser/view/sdg_14_21/default/table";
    skos:narrower indo:mean_biomass_herring ,
                                      indo:mean_biomass_sprat ,
                                      indo:B_herring_tot .

indo:fish-landing-value a ind:Indicator, sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Fish landing value by fleet"@en ;
    skos:prefLabel "Fish landing value by fleet"@en ;
    skos:definition "Abstract Indicator: monetary value of fish landed by a national fleet during a reporting tick, before specialisation by country or species."@en ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Currency ;
    skos:narrower indo:landing_value_herring_SV ,
                                      indo:landing_value_herring_LV ,
                                      indo:landing_value_sprat_SV ,
                                      indo:landing_value_sprat_LV .

indo:fish-ex-vessel-price a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Fish ex-vessel price"@en ;
    skos:prefLabel "Fish ex-vessel price"@en ;
    skos:definition "Abstract concept: ex-vessel price per unit mass of landed fish, before specialisation by species or end use."@en ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Price ;
    skos:narrower indo:herring_price_fish_meal ,
                                        indo:sprat_price ,
                                        indo:herring_price_human_cons .

indo:fleet-fuel-consumption a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Fleet fuel consumption"@en ;
    skos:prefLabel "Fleet fuel consumption"@en ;
    skos:definition "Abstract concept: marine fuel consumed by a national fishing fleet during a reporting tick, before specialisation by country."@en ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Volume ;
    skos:narrower indo:fuel_consumption_SV ,
                                          indo:fuel_consumption_LV .

indo:fleet-value-added a ind:Indicator, sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Fleet value added"@en ;
    skos:prefLabel "Fleet value added"@en ;
    skos:definition "Abstract Indicator: gross value added by a national fishing fleet during a reporting tick, before specialisation by country."@en ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Currency ;
    skos:narrower indo:VA_SV_All ,
                                     indo:VA_LV_All .

indo:fish-stock-growth-rate a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Fish stock growth rate"@en ;
    skos:prefLabel "Fish stock growth rate"@en ;
    skos:definition "Abstract concept: intrinsic biological growth rate of a fish stock, before specialisation by species."@en ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Dimensionless ;
    skos:narrower indo:yearly_growth_herring .

indo:fish-stock-carrying-capacity-increment a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Fish stock carrying-capacity increment"@en ;
    skos:prefLabel "Fish stock carrying-capacity increment"@en ;
    skos:definition "Abstract concept: per-period change applied to a fish stock's regional carrying capacity K, before specialisation by species or region."@en ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Mass ;
     skos:narrower indo:K_herring_reg_inc .

indo:fishing-season-state a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Fishing season state"@en ;
    skos:prefLabel "Fishing season state"@en ;
    skos:definition "Abstract concept: categorical state of a fishing season at the current time, before specialisation by stock."@en ;
    skos:inScheme ind:indicators-scheme ;
    skos:narrower indp:current_herring_season .

indo:fish-market-state a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Fish market state"@en ;
    skos:prefLabel "Fish market state"@en ;
    skos:definition "Abstract concept: categorical state of a national fish market governing landing prices and outlets, before specialisation by country or species."@en ;
    skos:inScheme ind:indicators-scheme ;
    skos:narrower indo:SV_herring_market .

indo:fleet-fishing-radius a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Fleet fishing radius"@en ;
    skos:prefLabel "Fleet fishing radius"@en ;
    skos:definition "Abstract concept: maximum operational radius from home port for a national fleet's vessel agents, before specialisation by country."@en ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Length ;
    skos:narrower indo:SV_fishing_radius .

indo:fish-stock-growth-suppression-flag a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Fish stock growth-suppression flag"@en ;
    skos:prefLabel "Fish stock growth-suppression flag"@en ;
    skos:definition "Abstract concept: boolean simulation switch that suspends biological growth of a fish stock for sensitivity analysis, before specialisation by species."@en ;
    skos:inScheme ind:indicators-scheme ;
    skos:narrower indo:stop_herring_growth .

indo:implemented-herring-tac a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Implemented herring TAC by country"@en ;
    skos:prefLabel "Implemented herring TAC by country"@en ;
    skos:definition "Abstract concept: herring Total Allowable Catch actually implemented by a national authority after adjustment of the advised share, before specialisation by country."@en ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Mass ;
    skos:narrower indo:TAC_herring_Sweden_impl .

indo:herring-tac-increment a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Herring TAC increment by country"@en ;
    skos:prefLabel "Herring TAC increment by country"@en ;
    skos:definition "Abstract concept: per-period adjustment (increment or decrement) applied to a national herring TAC under the management rule, before specialisation by country."@en ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Mass ;
    skos:narrower indo:TAC_herring_inc_SV .


# --- Simulation control & current-state Properties (ind:parameters-scheme) ---

indp:repetitions a ssn:Property, skos:Concept ;
    rdfs:label "Simulation repetitions"@en ;
    skos:prefLabel "Simulation repetitions"@en ;
    skos:altLabel "repetitions"@en ;
    skos:notation "repetitions" ;
    skos:definition "Configured number of independent repetitions performed for the simulation run."@en ;
    skos:inScheme ind:parameters-scheme .

indp:ticks a ssn:Property, skos:Concept ;
    rdfs:label "Simulation tick"@en ;
    skos:prefLabel "Simulation tick"@en ;
    skos:altLabel "ticks"@en ;
    skos:notation "ticks" ;
    skos:definition "Elapsed discrete-time step counter of the agent-based simulation since model initialisation."@en ;
    skos:inScheme ind:parameters-scheme .

indp:current_herring_season a ssn:Property, skos:Concept ;
    rdfs:label "Current herring fishing season"@en ;
    skos:prefLabel "Current herring fishing season"@en ;
    skos:altLabel "current_herring_season"@en ;
    skos:notation "current_herring_season" ;
    skos:definition "Categorical state-pointer giving the active herring fishing season at the current tick (e.g. open, spawning closure, winter closure)."@en ;
    skos:broader indo:fishing-season-state ;
    skos:inScheme ind:parameters-scheme .

indp:current_management_season a ssn:Property, skos:Concept ;
    rdfs:label "Current management season"@en ;
    skos:prefLabel "Current management season"@en ;
    skos:altLabel "current_management_season"@en ;
    skos:notation "current_management_season" ;
    skos:definition "Categorical state-pointer giving the active fisheries-management season at the current tick, used to switch between regulatory regimes."@en ;
    skos:inScheme ind:parameters-scheme .

indp:current_TAC_herring a ssn:Property, skos:Concept ;
    rdfs:label "Current TAC for herring"@en ;
    skos:prefLabel "Current TAC for herring"@en ;
    skos:altLabel "current_TAC_herring"@en ;
    skos:notation "current_TAC_herring" ;
    skos:definition "Total Allowable Catch for herring effective at the current tick, aggregated across all participating fleets."@en ;
    skos:broader indp:herring-tac ;
    skos:inScheme ind:parameters-scheme ;
    qudt:hasQuantityKind quantitykind:Mass .

indp:TAC_herring_share a ssn:Property, skos:Concept ;
    rdfs:label "Country share of herring TAC"@en ;
    skos:prefLabel "Country share of herring TAC"@en ;
    skos:altLabel "TAC_herring_share"@en ;
    skos:notation "TAC_herring_share" ;
    skos:definition "Abstract management parameter: fractional share of the total herring TAC allocated to a national fleet, before specialisation by country."@en ;
    skos:broader indp:herring-tac ;
    skos:narrower indp:TAC_herring_share_sv ;
    skos:inScheme ind:parameters-scheme ;
    qudt:hasQuantityKind quantitykind:Dimensionless .

indp:TAC_herring_share_sv a ssn:Property, skos:Concept ;
    rdfs:label "Small vessel share of herring TAC"@en ;
    skos:prefLabel "Small vessel share of herring TAC"@en ;
    skos:altLabel "TAC_herring_share_sv"@en ;
    skos:notation "TAC_herring_share_sv" ;
    skos:definition "Fractional share of the total herring TAC allocated to the Small vessel (SV) fleet."@en ;
    skos:broader indp:TAC_herring_share ;
    skos:inScheme ind:parameters-scheme ;
    qudt:hasQuantityKind quantitykind:Dimensionless .

# --- Dispersal rates (Properties: ind:parameters-scheme) ---
indp:dispersal_rate_property a ssn:Property, skos:Concept ;
    rdfs:label "Dispersal rate property"@en ;
    skos:prefLabel "Dispersal rate property"@en ;
    skos:definition "Generic simulation parameter defining the probability of an agent dispersing to a neighbouring patch."@en ;
    skos:inScheme ind:parameters-scheme ;
    skos:narrower indp:even_dispersal_rate ,
        indp:winter_dispersal_rate ,
        indp:spawning_dispersal_rate .

indp:even_dispersal_rate a ssn:Property, skos:Concept ;
    rdfs:label "Even dispersal rate"@en ;
    skos:prefLabel "Even dispersal rate"@en ;
    skos:altLabel "even_dispersal_rate"@en ;
    skos:notation "even_dispersal_rate" ;
    skos:definition "Per-tick probability that an agent disperses to a neighbouring patch under non-seasonal (even) conditions."@en ;
    skos:broader indp:dispersal_rate_property ;
    skos:inScheme ind:parameters-scheme ;
    qudt:hasQuantityKind quantitykind:Dimensionless .

indp:winter_dispersal_rate a ssn:Property, skos:Concept ;
    rdfs:label "Winter dispersal rate"@en ;
    skos:prefLabel "Winter dispersal rate"@en ;
    skos:altLabel "winter_dispersal_rate"@en ;
    skos:notation "winter_dispersal_rate" ;
    skos:definition "Per-tick probability that an agent disperses to a neighbouring patch during the winter season."@en ;
    skos:broader indp:dispersal_rate_property ;
    skos:inScheme ind:parameters-scheme ;
    qudt:hasQuantityKind quantitykind:Dimensionless .

indp:spawning_dispersal_rate a ssn:Property, skos:Concept ;
    rdfs:label "Spawning dispersal rate"@en ;
    skos:prefLabel "Spawning dispersal rate"@en ;
    skos:altLabel "spawning_dispersal_rate"@en ;
    skos:notation "spawning_dispersal_rate" ;
    skos:definition "Per-tick probability that a herring agent disperses to a neighbouring patch during the spawning season."@en ;
    skos:broader indp:dispersal_rate_property ;
    skos:inScheme ind:parameters-scheme ;
    qudt:hasQuantityKind quantitykind:Dimensionless .

# --- Closure-rule type (Properties: ind:parameters-scheme) ---
indp:closure_type_property a ssn:Property, skos:Concept ;
    rdfs:label "Closure type property"@en ;
    skos:prefLabel "Closure type property"@en ;
    skos:definition "Generic simulation parameter defining the qualitative management or policy scenario rule enforced during a specific season."@en ;
    skos:inScheme ind:parameters-scheme ;
    skos:narrower indp:winter_closure_type ,
        indp:spawning_closure_type .

indp:winter_closure_type a ssn:Property, skos:Concept ;
    rdfs:label "Winter closure type"@en ;
    skos:prefLabel "Winter closure type"@en ;
    skos:altLabel "winter_closure_type"@en ;
    skos:notation "winter_closure_type" ;
    skos:definition "Categorical scenario code identifying which spatial-temporal winter closure rule is enforced (e.g. none, partial, full)."@en ;
    skos:broader indp:closure_type_property ;
    skos:inScheme ind:parameters-scheme .

indp:spawning_closure_type a ssn:Property, skos:Concept ;
    rdfs:label "Spawning closure type"@en ;
    skos:prefLabel "Spawning closure type"@en ;
    skos:altLabel "spawning_closure_type"@en ;
    skos:notation "spawning_closure_type" ;
    skos:definition "Categorical scenario code identifying which spatial-temporal spawning-season closure rule is enforced."@en ;
    skos:broader indp:closure_type_property ;
    skos:inScheme ind:parameters-scheme .

# --- Fishery-control Properties (ind:parameters-scheme) ---
indp:trawling_limit a ssn:Property, skos:Concept ;
    rdfs:label "Trawling depth/distance limit"@en ;
    skos:prefLabel "Trawling depth/distance limit"@en ;
    skos:altLabel "trawling_limit"@en ;
    skos:notation "trawling_limit" ;
    skos:definition "Regulatory limit on trawling activity (depth or distance-from-coast threshold) applied in the current scenario."@en ;
    skos:inScheme ind:parameters-scheme .

indp:fishing_algorithm a ssn:Property, skos:Concept ;
    rdfs:label "Fishing-effort allocation algorithm"@en ;
    skos:prefLabel "Fishing-effort allocation algorithm"@en ;
    skos:altLabel "fishing_algorithm"@en ;
    skos:notation "fishing_algorithm" ;
    skos:definition "Identifier of the decision rule used by vessel agents to allocate fishing effort across patches and target species in a given tick."@en ;
    skos:inScheme ind:parameters-scheme .

# --- Reserved-for-future-use placeholder (ind:parameters-scheme) ---
# The source model emits a fixed block of output columns (currently `fu_01`
# .. `fu_17`) that are reserved for future use and always void/dummy (0) in
# the present data. No known external vocabulary defines a "reserved slot"
# term, so a single shared placeholder concept is proposed here rather than
# minting one concept per column; each column links to it via its own
# propertyUrl in the consuming building block, so no per-column label is
# declared here.
indp:reserved-for-future-use a ssn:Property, skos:Concept ;
    rdfs:label "Reserved for future use"@en ;
    skos:prefLabel "Reserved for future use"@en ;
    skos:definition "Placeholder property for a simulation output column reserved for future use. Current values are void/dummy (0) and carry no defined semantics; all reserved columns in a given output row share this single concept until a real, distinct property is defined for each."@en ;
    skos:scopeNote "Do not treat as a region, NUTS, or FU-area indicator without confirming with the model owner: source column name prefixes such as 'fu_' are naming artifacts of the originating model, not resolved vocabulary terms."@en ;
    skos:inScheme ind:parameters-scheme .

# --- Simulation-clock Properties (ind:parameters-scheme) ---
indp:current_year a ssn:Property, skos:Concept ;
    rdfs:label "Current simulation year"@en ;
    skos:prefLabel "Current simulation year"@en ;
    skos:altLabel "current_year"@en ;
    skos:notation "current_year" ;
    skos:definition "Calendar year corresponding to the current simulation tick."@en ;
    skos:inScheme ind:parameters-scheme .

indp:current_month a ssn:Property, skos:Concept ;
    rdfs:label "Current simulation month"@en ;
    skos:prefLabel "Current simulation month"@en ;
    skos:altLabel "current_month"@en ;
    skos:notation "current_month" ;
    skos:definition "Calendar month (1-12) corresponding to the current simulation tick."@en ;
    skos:inScheme ind:parameters-scheme .

indp:year_tick a ssn:Property, skos:Concept ;
    rdfs:label "Tick-of-year"@en ;
    skos:prefLabel "Tick-of-year"@en ;
    skos:altLabel "year_tick"@en ;
    skos:notation "year_tick" ;
    skos:definition "Index of the current simulation tick within the current calendar year (resets on each new year)."@en ;
    skos:inScheme ind:parameters-scheme .

indo:herring_price_fish_meal a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Herring price, fish-meal use"@en ;
    skos:prefLabel "Herring price, fish-meal use"@en ;
    skos:altLabel "herring_price_fish_meal"@en ;
    skos:notation "herring_price_fish_meal" ;
    skos:definition "Ex-vessel price per unit mass of herring landed for fish-meal/feed end use."@en ;
    skos:broader indo:fish-ex-vessel-price ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Price .

indo:sprat_price a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Sprat ex-vessel price"@en ;
    skos:prefLabel "Sprat ex-vessel price"@en ;
    skos:altLabel "sprat_price"@en ;
    skos:notation "sprat_price" ;
    skos:definition "Ex-vessel price per unit mass of landed sprat."@en ;
    skos:broader indo:fish-ex-vessel-price ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Price .

indo:fuel_price a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Marine fuel price"@en ;
    skos:prefLabel "Marine fuel price"@en ;
    skos:altLabel "fuel_price"@en ;
    skos:notation "fuel_price" ;
    skos:definition "Price per unit volume of marine fuel used by fishing vessels in the simulation."@en ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Price .

indo:fuel_consumption_SV a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Fuel consumption, Small vessel fleet"@en ;
    skos:prefLabel "Fuel consumption, Small vessel fleet"@en ;
    skos:altLabel "fuel_consumption_SV"@en ;
    skos:notation "fuel_consumption_SV" ;
    skos:definition "Total marine fuel consumed by the Small vessel (SV) fishing fleet during the reporting tick."@en ;
    skos:broader indo:fleet-fuel-consumption ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Volume .

indo:fuel_consumption_LV a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Fuel consumption, Large vessel fleet"@en ;
    skos:prefLabel "Fuel consumption, Large vessel fleet"@en ;
    skos:altLabel "fuel_consumption_LV"@en ;
    skos:notation "fuel_consumption_LV" ;
    skos:definition "Total marine fuel consumed by the Large vessel (LV) fishing fleet during the reporting tick."@en ;
    skos:broader indo:fleet-fuel-consumption ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Volume .

indo:stop_herring_growth a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Stop-herring-growth flag"@en ;
    skos:prefLabel "Stop-herring-growth flag"@en ;
    skos:altLabel "stop_herring_growth"@en ;
    skos:notation "stop_herring_growth" ;
    skos:definition "Boolean simulation switch that, when set, suspends biological growth of the herring stock for sensitivity analysis."@en ;
    skos:broader indo:fish-stock-growth-suppression-flag ;
    skos:inScheme ind:indicators-scheme .

indo:mean_biomass_herring a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Mean herring biomass"@en ;
    skos:prefLabel "Mean herring biomass"@en ;
    skos:altLabel "mean_biomass_herring"@en ;
    skos:notation "mean_biomass_herring" ;
    skos:definition "Spatially-averaged biomass of the simulated herring stock at the reporting tick."@en ;
    skos:broader indo:fish-stock-biomass ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Mass .

indo:mean_biomass_sprat a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Mean sprat biomass"@en ;
    skos:prefLabel "Mean sprat biomass"@en ;
    skos:altLabel "mean_biomass_sprat"@en , "mean_biomas_sprat"@en ;
    skos:notation "mean_biomass_sprat" , "mean_biomas_sprat" ;
    skos:definition "Spatially-averaged biomass of the simulated sprat stock at the reporting tick. NOTE: the original NetLogo identifier is misspelled as 'mean_biomas_sprat' (single 's'); both spellings are kept as notations / altLabels for lookup."@en ;
    skos:broader indo:fish-stock-biomass ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Mass .

indo:landing_value_herring_SV a ind:Indicator, sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Herring landing value, Small Vessel fleet"@en ;
    skos:prefLabel "Herring landing value, Small Vessel fleet"@en ;
    skos:altLabel "landing_value_herring_SV"@en ;
    skos:notation "landing_value_herring_SV" ;
    skos:definition "Monetary value of herring landings by the Small Vessel (SV) fleet during the reporting tick."@en ;
    skos:broader indo:fish-landing-value ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Currency .

indo:landing_value_herring_LV a ind:Indicator, sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Herring landing value, Large vessel fleet"@en ;
    skos:prefLabel "Herring landing value, Large vessel fleet"@en ;
    skos:altLabel "landing_value_herring_LV"@en ;
    skos:notation "landing_value_herring_LV" ;
    skos:definition "Monetary value of herring landings by the Large vessel (LV) fleet during the reporting tick."@en ;
    skos:broader indo:fish-landing-value ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Currency .

indo:landing_value_sprat_SV a ind:Indicator, sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Sprat landing value, Small Vessel fleet"@en ;
    skos:prefLabel "Sprat landing value, Small Vessel fleet"@en ;
    skos:altLabel "landing_value_sprat_SV"@en ;
    skos:notation "landing_value_sprat_SV" ;
    skos:definition "Monetary value of sprat landings by the Small Vessel (SV) fleet during the reporting tick."@en ;
    skos:broader indo:fish-landing-value ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Currency .

indo:landing_value_sprat_LV a ind:Indicator, sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Sprat landing value, Large vessel fleet"@en ;
    skos:prefLabel "Sprat landing value, Large vessel fleet"@en ;
    skos:altLabel "landing_value_sprat_LV"@en , "landing-value_sprat_LV"@en ;
    skos:notation "landing_value_sprat_LV" , "landing-value_sprat_LV" ;
    skos:definition "Monetary value of sprat landings by the Large vessel (LV) fleet during the reporting tick. NOTE: the original NetLogo identifier uses a hyphen ('landing-value_sprat_LV') rather than an underscore; both spellings are kept as notations / altLabels for lookup."@en ;
    skos:broader indo:fish-landing-value ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Currency .

indo:catch_herring_SV_All a ind:Indicator, sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Total herring catch, Small Vessel fleet (all vessels)"@en ;
    skos:prefLabel "Total herring catch, Small Vessel fleet (all vessels)"@en ;
    skos:altLabel "catch_herring_SV_All"@en ;
    skos:notation "catch_herring_SV_All" ;
    skos:definition "Total mass of herring caught by all Small Vessel (SV) vessels during the reporting tick."@en ;
    skos:broader indo:fish-catch ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Mass .

indo:catch_herring_LV_All a ind:Indicator, sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Total herring catch, Large vessel fleet (all vessels)"@en ;
    skos:prefLabel "Total herring catch, Large vessel fleet (all vessels)"@en ;
    skos:altLabel "catch_herring_LV_All"@en ;
    skos:notation "catch_herring_LV_All" ;
    skos:definition "Total mass of herring caught by all Large vessel (LV) vessels during the reporting tick."@en ;
    skos:broader indo:fish-catch ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Mass .

indo:catch_sprat_SV_All a ind:Indicator, sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Total sprat catch, Small Vessel fleet (all vessels)"@en ;
    skos:prefLabel "Total sprat catch, Small Vessel fleet (all vessels)"@en ;
    skos:altLabel "catch_sprat_SV_All"@en ;
    skos:notation "catch_sprat_SV_All" ;
    skos:definition "Total mass of sprat caught by all Small Vessel (SV) vessels during the reporting tick."@en ;
    skos:broader indo:fish-catch ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Mass .

indo:catch_sprat_LV_All a ind:Indicator, sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Total sprat catch, Large vessel fleet (all vessels)"@en ;
    skos:prefLabel "Total sprat catch, Large vessel fleet (all vessels)"@en ;
    skos:altLabel "catch_sprat_LV_All"@en ;
    skos:notation "catch_sprat_LV_All" ;
    skos:definition "Total mass of sprat caught by all Large vessel (LV) vessels during the reporting tick."@en ;
    skos:broader indo:fish-catch ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Mass .

indo:VA_SV_All a ind:Indicator, sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Value added, Small Vessel fleet (all vessels)"@en ;
    skos:prefLabel "Value added, Small Vessel fleet (all vessels)"@en ;
    skos:altLabel "VA_SV_All"@en ;
    skos:notation "VA_SV_All" ;
    skos:definition "Gross value added (landing revenue minus running costs) by all Small Vessel (SV) fishing vessels during the reporting tick."@en ;
    skos:broader indo:fleet-value-added ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Currency .

indo:VA_LV_All a ind:Indicator, sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Value added, Large vessel fleet (all vessels)"@en ;
    skos:prefLabel "Value added, Large vessel fleet (all vessels)"@en ;
    skos:altLabel "VA_LV_All"@en ;
    skos:notation "VA_LV_All" ;
    skos:definition "Gross value added (landing revenue minus running costs) by all Large vessel (LV) fishing vessels during the reporting tick."@en ;
    skos:broader indo:fleet-value-added ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Currency .

indo:yearly_growth_herring a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Annual herring stock growth rate"@en ;
    skos:prefLabel "Annual herring stock growth rate"@en ;
    skos:altLabel "yearly_growth_herring"@en ;
    skos:notation "yearly_growth_herring" ;
    skos:definition "Year-on-year intrinsic growth rate applied to the simulated herring biomass."@en ;
    skos:broader indo:fish-stock-growth-rate ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Dimensionless .

indo:winter_closure_length a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Winter closure length"@en ;
    skos:prefLabel "Winter closure length"@en ;
    skos:altLabel "winter_closure_length"@en ;
    skos:notation "winter_closure_length" ;
    skos:definition "Duration of the winter fishery closure (in months or ticks) imposed by the active management scenario."@en ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Time .

indo:TAC_share_B_herring a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Biomass-based TAC share for herring"@en ;
    skos:prefLabel "Biomass-based TAC share for herring"@en ;
    skos:altLabel "TAC_share_B_herring"@en ;
    skos:notation "TAC_share_B_herring" ;
    skos:definition "Fractional TAC share for herring derived from the current total herring biomass under the biomass-based harvest rule."@en ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Dimensionless .

indo:B_herring_tot a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Total herring biomass"@en ;
    skos:prefLabel "Total herring biomass"@en ;
    skos:altLabel "B_herring_tot"@en ;
    skos:notation "B_herring_tot" ;
    skos:definition "Aggregate biomass of the entire simulated herring stock (sum over all patches and age classes) at the reporting tick."@en ;
    skos:broader indo:fish-stock-biomass ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Mass .

indo:K_herring_reg_inc a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Regional herring carrying-capacity increment"@en ;
    skos:prefLabel "Regional herring carrying-capacity increment"@en ;
    skos:altLabel "K_herring_reg_inc"@en ;
    skos:notation "K_herring_reg_inc" ;
    skos:definition "Per-tick increment applied to the regional herring carrying capacity K, used to drive non-stationary K scenarios."@en ;
    skos:broader indo:fish-stock-carrying-capacity-increment ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Mass .

indo:TAC_herring_Sweden_impl a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Implemented Swedish herring TAC"@en ;
    skos:prefLabel "Implemented Swedish herring TAC"@en ;
    skos:altLabel "TAC_herring_Sweden_impl"@en ;
    skos:notation "TAC_herring_Sweden_impl" ;
    skos:definition "Herring TAC actually implemented for Sweden after national adjustment of the advised share."@en ;
    skos:broader indo:implemented-herring-tac ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Mass .

indo:herring_price_human_cons a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Herring price, human consumption"@en ;
    skos:prefLabel "Herring price, human consumption"@en ;
    skos:altLabel "herring_price_human_cons"@en ;
    skos:notation "herring_price_human_cons" ;
    skos:definition "Ex-vessel price per unit mass of herring landed for human-consumption end use."@en ;
    skos:broader indo:fish-ex-vessel-price ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Price .

indo:SV_herring_market a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Small Vessel herring market state"@en ;
    skos:prefLabel "Small Vessel herring market state"@en ;
    skos:altLabel "SV_herring_market"@en ;
    skos:notation "SV_herring_market" ;
    skos:notation "SV_herring_market" ;
    skos:definition "Categorical state of the Small Vessel (SV) herring market (e.g. human-consumption open, fish-meal only) governing which price applies to landings."@en ;
    skos:broader indo:fish-market-state ;
    skos:inScheme ind:indicators-scheme .

indo:TAC_herring_est_error a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Herring TAC estimation error"@en ;
    skos:prefLabel "Herring TAC estimation error"@en ;
    skos:altLabel "TAC_herring_est_error"@en ;
    skos:notation "TAC_herring_est_error" ;
    skos:definition "Relative error applied to the herring TAC to represent assessment uncertainty between true biomass and the value used for management."@en ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Dimensionless .

indo:SV_fishing_radius a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Small Vessel vessel fishing radius"@en ;
    skos:prefLabel "Small Vessel vessel fishing radius"@en ;
    skos:altLabel "SV_fishing_radius"@en ;
    skos:notation "SV_fishing_radius" ;
    skos:definition "Maximum operational radius from home port within which Small Vessel (SV) vessel agents search for and exploit fishing patches."@en ;
    skos:broader indo:fleet-fishing-radius ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Length .

indo:TAC_herring_inc_SV a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Small Vessel herring TAC increment"@en ;
    skos:prefLabel "Small Vessel herring TAC increment"@en ;
    skos:altLabel "TAC_herring_inc_SV"@en ;
    skos:notation "TAC_herring_inc_SV" ;
    skos:definition "Per-period adjustment (increment or decrement) applied to the Small Vessel (SV) herring TAC under the management rule, capturing year-to-year change in allowable catch."@en ;
    skos:broader indo:herring-tac-increment ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Mass .

indo:TAC_herring_type a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Herring TAC rule type"@en ;
    skos:prefLabel "Herring TAC rule type"@en ;
    skos:altLabel "TAC_herring_type"@en ;
    skos:notation "TAC_herring_type" ;
    skos:definition "Categorical identifier of the harvest-control rule used to derive the herring TAC (e.g. constant, F-based, biomass-based, escapement)."@en ;
    skos:inScheme ind:indicators-scheme .


# --- Reef-biomass equation: one Indicator (output) derived from four Properties (inputs) ---

indo:floating-wind-reef-biomass-effect a ind:Indicator, sosa:ObservableProperty, prov:Entity, skos:Concept ;
    rdfs:label "Floating-wind reef biomass effect"@en ;
    skos:prefLabel "Floating-wind reef biomass effect"@en ;
    skos:definition "Reef-associated biomass attributable to submerged floating-wind infrastructure, calculated as B_reef = sum_i (A_sub * D_pre,i * AF_i * C_t)."@en ;
    skos:notation """<mathml><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><msub><mi>B</mi><mi>reef</mi></msub><mo>=</mo><munder><mo>&#x2211;</mo><mi>i</mi></munder><mrow><mo>(</mo><msub><mi>A</mi><mi>sub</mi></msub><mo>&#x22C5;</mo><msub><mi>D</mi><mrow><mi>pre</mi><mo>,</mo><mi>i</mi></mrow></msub><mo>&#x22C5;</mo><msub><mi>AF</mi><mi>i</mi></msub><mo>&#x22C5;</mo><msub><mi>C</mi><mi>t</mi></msub><mo>)</mo></mrow></mrow></math></mathml>"""^^<http://www.w3.org/1998/Math/MathML> ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:Mass ;
    prov:wasDerivedFrom indp:submerged-infrastructure-area,
        indo:baseline-benthic-biomass-density,
        indp:reef-aggregation-index,
        indp:colonisation-time-factor ;
    rdfs:seeAlso <https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation> .


# Engineering-design Property (parameters-scheme).
indp:submerged-infrastructure-area a ssn:Property, skos:Concept ;
    rdfs:label "Submerged infrastructure area"@en ;
    skos:prefLabel "Submerged infrastructure area"@en ;
    skos:definition "Wetted submerged hard-substrate area of floating-wind infrastructure available for colonisation."@en ;
    skos:inScheme ind:parameters-scheme ;
    skos:narrower indp:submerged-infrastructure-area-utsira-design ;
    qudt:quantityKind quantitykind:Area ;
    qudt:hasQuantityKind quantitykind:Area .

# Baseline-density ObservableProperty (indicators-scheme) — measured from surveys, not a model parameter.
indo:baseline-benthic-biomass-density a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Baseline benthic biomass density"@en ;
    skos:prefLabel "Baseline benthic biomass density"@en ;
    skos:definition "Baseline benthic biomass per seabed area before installation or in a matched control area, indexed by taxon."@en ;
    skos:inScheme ind:indicators-scheme ;
    skos:narrower indo:benthic-biomass-density-mareano,
        indo:benthic-biomass-density-imr-baseline ;
    qudt:hasQuantityKind quantitykind:SurfaceDensity .

# Reef-aggregation-index Property (parameters-scheme).
indp:reef-aggregation-index a ssn:Property, skos:Concept ;
    rdfs:label "Reef aggregation index"@en ;
    skos:prefLabel "Reef aggregation index"@en ;
    skos:definition "Dimensionless per-taxon coefficient representing aggregation or enhancement on artificial reef infrastructure relative to a baseline habitat."@en ;
    skos:inScheme ind:parameters-scheme ;
    skos:narrower indp:reef-aggregation-index-mytilus,
        indp:reef-aggregation-index-buccinum,
        indp:reef-aggregation-index-asterias ;
    skos:related "http://vocab.nerc.ac.uk/collection/S06/current/S0600232/" ;
    skos:related indo:benthic-biomass-density ;
    qudt:hasQuantityKind quantitykind:Dimensionless .

# Colonisation-time-factor Property (parameters-scheme).
indp:colonisation-time-factor a ssn:Property, skos:Concept ;
    rdfs:label "Colonisation time factor"@en ;
    skos:prefLabel "Colonisation time factor"@en ;
    skos:definition "Dimensionless coefficient representing the development of colonisation through time."@en ;
    skos:inScheme ind:parameters-scheme ;
    skos:narrower indp:colonisation-time-factor-default ;
    qudt:hasQuantityKind quantitykind:Dimensionless .

# --- Narrower bindings (specific values) for the reef-related Properties / ObservableProperty ---

indp:submerged-infrastructure-area-utsira-design a ssn:Property, skos:Concept ;
    rdfs:label "Submerged infrastructure area, Utsira design"@en ;
    skos:prefLabel "Submerged infrastructure area, Utsira design"@en ;
    skos:definition "Utsira Nord engineering-design binding for submerged infrastructure area, covering wetted hull, mooring and anchor surfaces."@en ;
    skos:broader indp:submerged-infrastructure-area ;
    skos:inScheme ind:parameters-scheme ;
    qudt:hasQuantityKind quantitykind:Area ;
    skos:example <https://veiledere.nve.no/havvind/strategisk-konsekvensutredning-av-vindkraft-til-havs/> .

indo:benthic-biomass-density-mareano a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Benthic biomass density, MAREANO"@en ;
    skos:prefLabel "Benthic biomass density, MAREANO"@en ;
    skos:definition "Primary MAREANO binding for baseline benthic biomass density on the Norwegian shelf."@en ;
    skos:broader indo:baseline-benthic-biomass-density ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:SurfaceDensity ;
    rdfs:seeAlso <https://mareano.no/> .

indo:benthic-biomass-density-imr-baseline a sosa:ObservableProperty, skos:Concept ;
    rdfs:label "Benthic biomass density, IMR baseline"@en ;
    skos:prefLabel "Benthic biomass density, IMR baseline"@en ;
    skos:definition "Fallback regional baseline binding for benthic biomass density where MAREANO lacks taxon coverage."@en ;
    skos:broader indo:baseline-benthic-biomass-density ;
    skos:inScheme ind:indicators-scheme ;
    qudt:hasQuantityKind quantitykind:SurfaceDensity ;
    rdfs:seeAlso <https://www.hi.no/> .

indp:reef-aggregation-index-mytilus a ssn:Property, skos:Concept ;
    rdfs:label "Reef aggregation index for Mytilus edulis"@en ;
    skos:prefLabel "Reef aggregation index for Mytilus edulis"@en ;
    skos:definition "Per-taxon reef aggregation index binding for Mytilus edulis."@en ;
    skos:broader indp:reef-aggregation-index ;
    skos:inScheme ind:parameters-scheme ;
    qudt:hasQuantityKind quantitykind:Dimensionless ;
    rdfs:seeAlso <https://doi.org/10.5670/oceanog.2020.405> .

indp:reef-aggregation-index-buccinum a ssn:Property, skos:Concept ;
    rdfs:label "Reef aggregation index for Buccinum undatum"@en ;
    skos:prefLabel "Reef aggregation index for Buccinum undatum"@en ;
    skos:definition "Per-taxon reef aggregation index binding for Buccinum undatum."@en ;
    skos:broader indp:reef-aggregation-index ;
    skos:inScheme ind:parameters-scheme ;
    qudt:hasQuantityKind quantitykind:Dimensionless ;
    rdfs:seeAlso <https://www.windfloat-atlantic.com/> .

indp:reef-aggregation-index-asterias a ssn:Property, skos:Concept ;
    rdfs:label "Reef aggregation index for Asterias rubens"@en ;
    skos:prefLabel "Reef aggregation index for Asterias rubens"@en ;
    skos:definition "Per-taxon reef aggregation index binding for Asterias rubens."@en ;
    skos:broader indp:reef-aggregation-index ;
    skos:inScheme ind:parameters-scheme ;
    qudt:hasQuantityKind quantitykind:Dimensionless .

indp:colonisation-time-factor-default a ssn:Property, skos:Concept ;
    rdfs:label "Colonisation time factor, default"@en ;
    skos:prefLabel "Colonisation time factor, default"@en ;
    skos:definition "Default illustrative sigmoid colonisation-time coefficient, saturating at 24 months. The logistic curve form, parameters, and lookup values are taken from the SeaDOTs colonisation-time-factor example and are linked to Degraer et al. 2020 as a qualitative publication source; Degraer et al. do not publish these exact numeric sigmoid parameters."@en ;
    skos:notation "C(t) = L / (1 + exp(-k * (t - t0)))" ;
    skos:broader indp:colonisation-time-factor ;
    skos:inScheme ind:parameters-scheme ;
    skos:narrower indp:colonisation-time-factor-default-L ,
                  indp:colonisation-time-factor-default-k ,
                  indp:colonisation-time-factor-default-t0-months ,
                  indp:colonisation-time-factor-default-saturation-month ,
                  indp:colonisation-time-factor-default-Ct-0-months ,
                  indp:colonisation-time-factor-default-Ct-6-months ,
                  indp:colonisation-time-factor-default-Ct-12-months ,
                  indp:colonisation-time-factor-default-Ct-18-months ,
                  indp:colonisation-time-factor-default-Ct-24-months ;
    qudt:hasQuantityKind quantitykind:Dimensionless ;
    dcterms:source <https://doi.org/10.5670/oceanog.2020.405> ;
    prov:wasDerivedFrom <https://doi.org/10.5670/oceanog.2020.405> ;
    rdfs:seeAlso <https://w3id.org/ogc/hosted/seadots/colonisation-time-factor> ,
                 <https://doi.org/10.5670/oceanog.2020.405> .

indp:colonisation-time-factor-default-L a ssn:Property, skos:Concept ;
    rdfs:label "Default colonisation sigmoid saturation level L"@en ;
    skos:prefLabel "Default colonisation sigmoid saturation level L"@en ;
    skos:notation "L" ;
    skos:definition "Illustrative saturation level of the default logistic colonisation-time curve C(t)."@en ;
    skos:broader indp:colonisation-time-factor-default ;
    skos:inScheme ind:parameters-scheme ;
    rdf:value 1.0 ;
    qudt:hasQuantityKind quantitykind:Dimensionless ;
    dcterms:source <https://w3id.org/ogc/hosted/seadots/colonisation-time-factor> ;
    prov:wasDerivedFrom <https://doi.org/10.5670/oceanog.2020.405> .

indp:colonisation-time-factor-default-k a ssn:Property, skos:Concept ;
    rdfs:label "Default colonisation sigmoid growth rate k"@en ;
    skos:prefLabel "Default colonisation sigmoid growth rate k"@en ;
    skos:notation "k" ;
    skos:definition "Illustrative growth-rate parameter of the default logistic colonisation-time curve C(t)."@en ;
    skos:broader indp:colonisation-time-factor-default ;
    skos:inScheme ind:parameters-scheme ;
    rdf:value 0.30 ;
    qudt:hasQuantityKind quantitykind:Dimensionless ;
    dcterms:source <https://w3id.org/ogc/hosted/seadots/colonisation-time-factor> ;
    prov:wasDerivedFrom <https://doi.org/10.5670/oceanog.2020.405> .

indp:colonisation-time-factor-default-t0-months a ssn:Property, skos:Concept ;
    rdfs:label "Default colonisation sigmoid midpoint t0"@en ;
    skos:prefLabel "Default colonisation sigmoid midpoint t0"@en ;
    skos:notation "t0_months" ;
    skos:definition "Illustrative midpoint of the default logistic colonisation-time curve, expressed as months since installation."@en ;
    skos:broader indp:colonisation-time-factor-default ;
    skos:inScheme ind:parameters-scheme ;
    rdf:value 8 ;
    dcterms:source <https://w3id.org/ogc/hosted/seadots/colonisation-time-factor> ;
    prov:wasDerivedFrom <https://doi.org/10.5670/oceanog.2020.405> .

indp:colonisation-time-factor-default-saturation-month a ssn:Property, skos:Concept ;
    rdfs:label "Default colonisation saturation month"@en ;
    skos:prefLabel "Default colonisation saturation month"@en ;
    skos:notation "saturationMonth" ;
    skos:definition "Illustrative month at which the default colonisation-time curve is treated as saturated for the SeaDOTs worked example."@en ;
    skos:broader indp:colonisation-time-factor-default ;
    skos:inScheme ind:parameters-scheme ;
    rdf:value 24 ;
    dcterms:source <https://w3id.org/ogc/hosted/seadots/colonisation-time-factor> ;
    prov:wasDerivedFrom <https://doi.org/10.5670/oceanog.2020.405> .

indp:colonisation-time-factor-default-Ct-0-months a ssn:Property, skos:Concept ;
    rdfs:label "Default colonisation time factor at 0 months"@en ;
    skos:prefLabel "Default colonisation time factor at 0 months"@en ;
    skos:notation "C_t(t_months=0)" ;
    skos:definition "Illustrative lookup-table sample value of the default colonisation-time factor at 0 months since installation."@en ;
    skos:broader indp:colonisation-time-factor-default ;
    skos:inScheme ind:parameters-scheme ;
    rdf:value 0.08 ;
    qudt:hasQuantityKind quantitykind:Dimensionless ;
    dcterms:source <https://w3id.org/ogc/hosted/seadots/colonisation-time-factor> ;
    prov:wasDerivedFrom <https://doi.org/10.5670/oceanog.2020.405> .

indp:colonisation-time-factor-default-Ct-6-months a ssn:Property, skos:Concept ;
    rdfs:label "Default colonisation time factor at 6 months"@en ;
    skos:prefLabel "Default colonisation time factor at 6 months"@en ;
    skos:notation "C_t(t_months=6)" ;
    skos:definition "Illustrative lookup-table sample value of the default colonisation-time factor at 6 months since installation."@en ;
    skos:broader indp:colonisation-time-factor-default ;
    skos:inScheme ind:parameters-scheme ;
    rdf:value 0.32 ;
    qudt:hasQuantityKind quantitykind:Dimensionless ;
    dcterms:source <https://w3id.org/ogc/hosted/seadots/colonisation-time-factor> ;
    prov:wasDerivedFrom <https://doi.org/10.5670/oceanog.2020.405> .

indp:colonisation-time-factor-default-Ct-12-months a ssn:Property, skos:Concept ;
    rdfs:label "Default colonisation time factor at 12 months"@en ;
    skos:prefLabel "Default colonisation time factor at 12 months"@en ;
    skos:notation "C_t(t_months=12)" ;
    skos:definition "Illustrative lookup-table sample value of the default colonisation-time factor at 12 months since installation."@en ;
    skos:broader indp:colonisation-time-factor-default ;
    skos:inScheme ind:parameters-scheme ;
    rdf:value 0.71 ;
    qudt:hasQuantityKind quantitykind:Dimensionless ;
    dcterms:source <https://w3id.org/ogc/hosted/seadots/colonisation-time-factor> ;
    prov:wasDerivedFrom <https://doi.org/10.5670/oceanog.2020.405> .

indp:colonisation-time-factor-default-Ct-18-months a ssn:Property, skos:Concept ;
    rdfs:label "Default colonisation time factor at 18 months"@en ;
    skos:prefLabel "Default colonisation time factor at 18 months"@en ;
    skos:notation "C_t(t_months=18)" ;
    skos:definition "Illustrative lookup-table sample value of the default colonisation-time factor at 18 months since installation."@en ;
    skos:broader indp:colonisation-time-factor-default ;
    skos:inScheme ind:parameters-scheme ;
    rdf:value 0.93 ;
    qudt:hasQuantityKind quantitykind:Dimensionless ;
    dcterms:source <https://w3id.org/ogc/hosted/seadots/colonisation-time-factor> ;
    prov:wasDerivedFrom <https://doi.org/10.5670/oceanog.2020.405> .

indp:colonisation-time-factor-default-Ct-24-months a ssn:Property, skos:Concept ;
    rdfs:label "Default colonisation time factor at 24 months"@en ;
    skos:prefLabel "Default colonisation time factor at 24 months"@en ;
    skos:notation "C_t(t_months=24)" ;
    skos:definition "Illustrative lookup-table sample value of the default colonisation-time factor at 24 months since installation."@en ;
    skos:broader indp:colonisation-time-factor-default ;
    skos:inScheme ind:parameters-scheme ;
    rdf:value 0.99 ;
    qudt:hasQuantityKind quantitykind:Dimensionless ;
    dcterms:source <https://w3id.org/ogc/hosted/seadots/colonisation-time-factor> ;
    prov:wasDerivedFrom <https://doi.org/10.5670/oceanog.2020.405> .

ind:ind-rel-scheme a skos:ConceptScheme ;
    dcterms:isPartOf ind:catalog ; # Backlink for discovery
    skos:prefLabel "SEADOTS Indicator relationships Scheme"@en ;
    skos:definition "A concept scheme for SEADOTS relationships between indicator concepts and observed properties, using the SeaDOTs PropertyRelationship building block."@en ;
    rdfs:seeAlso <https://defs-hosted.opengis.net/prez-hosted/catalogs/bblocksseadots> ;
    # --- TOP CONCEPTS (added for VocPrez/Prez UI visibility) ---
    skos:hasTopConcept indr:crossImpact-Utsira-OWF-v1 .

# SeaDOTs property relationship model.
# Canonical model: https://defs-hosted.opengis.net/prez-hosted/catalogs/bblocksseadots

indr:crossImpact-Utsira-OWF-v1 a prov:Agent, skos:Concept ;
    rdfs:label "Cross-impact analysis model Utsira OWF v1"@en ;
    skos:prefLabel "Cross-impact analysis model Utsira OWF v1"@en ;
    skos:definition "Model that generated the Utsira indicator relationship weights."@en ;
    dcterms:identifier "crossImpact-Utsira-OWF-v1" ;
    skos:narrower indr:fisheries-production_2_number-of-turbines,
              indr:fisheries-production_2_area-use-by-wind-park,
              indr:fisheries-production_2_number-of-jobs,
              indr:number-of-turbines_2_area-use-by-wind-park,
              indr:area-use-by-wind-park_2_fisheries-production,
              indr:number-of-jobs_2_bird-tourism,
              indr:bird-tourism_2_number-of-jobs,
              indr:bird-tourism_2_bird-tourism ;
    skos:inScheme ind:ind-rel-scheme .

# Property relationships

indr:fisheries-production_2_number-of-turbines a prop-rel:PropertyRelationship, skos:Concept ;
    skos:prefLabel "Fisheries production to number of turbines"@en ;
    skos:inScheme ind:ind-rel-scheme ;
    skos:definition "Cross-impact relationship from fisheries production to number of turbines, with a weight of 0.5."@en ;
    skos:broader indr:crossImpact-Utsira-OWF-v1 ; # Backlink for discovery
    prop-rel:fromProperty indo:fisheries-production ;
    prop-rel:toProperty indp:number-of-turbines ;
    prop-rel:hasWeight [ qudt:numericValue 0.5 ] ;
    prov:wasAttributedTo indr:crossImpact-Utsira-OWF-v1 .

indr:fisheries-production_2_area-use-by-wind-park a prop-rel:PropertyRelationship, skos:Concept ;
    skos:prefLabel "Fisheries production to area use by wind park"@en ;
    skos:inScheme ind:ind-rel-scheme ;
    skos:definition "Cross-impact relationship from fisheries production to area use by wind park, with a weight of -0.5."@en ;
    skos:broader indr:crossImpact-Utsira-OWF-v1 ;
    prop-rel:fromProperty indo:fisheries-production ;
    prop-rel:toProperty indp:area-use-by-wind-park ;
    prop-rel:hasWeight [ qudt:numericValue -0.5 ] ;
    prov:wasAttributedTo indr:crossImpact-Utsira-OWF-v1 .

indr:fisheries-production_2_number-of-jobs a prop-rel:PropertyRelationship, skos:Concept ;
    skos:prefLabel "Fisheries production to number of jobs"@en ;
    skos:inScheme ind:ind-rel-scheme ;
    skos:definition "Cross-impact relationship from fisheries production to number of jobs, with a weight of 1."@en ;
    skos:broader indr:crossImpact-Utsira-OWF-v1 ;
    prop-rel:fromProperty indo:fisheries-production ;
    prop-rel:toProperty indo:number-of-jobs ;
    prop-rel:hasWeight [ qudt:numericValue 1 ] ;
    prov:wasAttributedTo indr:crossImpact-Utsira-OWF-v1 .

indr:number-of-turbines_2_area-use-by-wind-park a prop-rel:PropertyRelationship, skos:Concept ;
    skos:prefLabel "Number of turbines to area use by wind park"@en ;
    skos:inScheme ind:ind-rel-scheme ;
    skos:definition "Cross-impact relationship from number of turbines to area use by wind park, with a weight of 0.49."@en ;
    skos:broader indr:crossImpact-Utsira-OWF-v1 ;
    prop-rel:fromProperty indp:number-of-turbines ;
    prop-rel:toProperty indp:area-use-by-wind-park ;
    prop-rel:hasWeight [ qudt:numericValue 0.49 ] ;
    prov:wasAttributedTo indr:crossImpact-Utsira-OWF-v1 .

indr:area-use-by-wind-park_2_fisheries-production a prop-rel:PropertyRelationship, skos:Concept ;
    skos:prefLabel "Area use by wind park to fisheries production"@en ;
    skos:inScheme ind:ind-rel-scheme ;
    skos:definition "Cross-impact relationship from area use by wind park to fisheries production, with a weight of 1."@en ;
    skos:broader indr:crossImpact-Utsira-OWF-v1 ;
    prop-rel:fromProperty indp:area-use-by-wind-park ;
    prop-rel:toProperty indo:fisheries-production ;
    prop-rel:hasWeight [ qudt:numericValue 1 ] ;
    prov:wasAttributedTo indr:crossImpact-Utsira-OWF-v1 .

indr:number-of-jobs_2_bird-tourism a prop-rel:PropertyRelationship, skos:Concept ;
    skos:prefLabel "Number of jobs to bird tourism"@en ;
    skos:inScheme ind:ind-rel-scheme ;
    skos:definition "Cross-impact relationship from number of jobs to bird tourism, with a weight of 0.52."@en ;
    skos:broader indr:crossImpact-Utsira-OWF-v1 ;
    prop-rel:fromProperty indo:number-of-jobs ;
    prop-rel:toProperty indo:bird-tourism ;
    prop-rel:hasWeight [ qudt:numericValue 0.52 ] ;
    prov:wasAttributedTo indr:crossImpact-Utsira-OWF-v1 .

indr:bird-tourism_2_number-of-jobs a prop-rel:PropertyRelationship, skos:Concept ;
    skos:prefLabel "Bird tourism to number of jobs"@en ;
    skos:inScheme ind:ind-rel-scheme ;
    skos:definition "Cross-impact relationship from bird tourism to number of jobs, with a weight of 0.7."@en ;
    skos:broader indr:crossImpact-Utsira-OWF-v1 ;
    prop-rel:fromProperty indo:bird-tourism ;
    prop-rel:toProperty indo:number-of-jobs ;
    prop-rel:hasWeight [ qudt:numericValue 0.7 ] ;
    prov:wasAttributedTo indr:crossImpact-Utsira-OWF-v1 .

indr:bird-tourism_2_bird-tourism a prop-rel:PropertyRelationship, skos:Concept ;
    skos:prefLabel "Bird tourism self-reinforcing relationship"@en ;
    skos:inScheme ind:ind-rel-scheme ;
    skos:definition "Self-reinforcing relationship within bird tourism, with a weight of 1."@en ;
    skos:broader indr:crossImpact-Utsira-OWF-v1 ;
    prop-rel:fromProperty indo:bird-tourism ;
    prop-rel:toProperty indo:bird-tourism ;
    prop-rel:hasWeight [ qudt:numericValue 1 ] ;
    prov:wasAttributedTo indr:crossImpact-Utsira-OWF-v1 .


# =====================================================================
# --- EMODnet THEME MAPPING (proposal) ---
# Each Property and ObservableProperty is tagged with the EMODnet thematic
# portal(s) it belongs to. Concepts may be tagged with multiple themes when
# the topic spans more than one portal (e.g. artificial reefs = Biology +
# Seabed Habitats). Pure simulation-control variables and non-marine
# drought concepts have no EMODnet theme.
# Reference: https://emodnet.ec.europa.eu/en
# =====================================================================

ind:emodnet-bathymetry a skos:Concept ;
    skos:prefLabel "EMODnet — Bathymetry"@en ;
    skos:definition "EMODnet Bathymetry thematic portal."@en ;
    skos:exactMatch <https://emodnet.ec.europa.eu/en/bathymetry> .

ind:emodnet-biology a skos:Concept ;
    skos:prefLabel "EMODnet — Biology"@en ;
    skos:definition "EMODnet Biology thematic portal (species occurrences, abundance, distribution)."@en ;
    skos:exactMatch <https://emodnet.ec.europa.eu/en/biology> .

ind:emodnet-chemistry a skos:Concept ;
    skos:prefLabel "EMODnet — Chemistry"@en ;
    skos:definition "EMODnet Chemistry thematic portal (water chemistry, contaminants, eutrophication)."@en ;
    skos:exactMatch <https://emodnet.ec.europa.eu/en/chemistry> .

ind:emodnet-geology a skos:Concept ;
    skos:prefLabel "EMODnet — Geology"@en ;
    skos:definition "EMODnet Geology thematic portal (seabed substrate, sediment, geology)."@en ;
    skos:exactMatch <https://emodnet.ec.europa.eu/en/geology> .

ind:emodnet-human-activities a skos:Concept ;
    skos:prefLabel "EMODnet — Human Activities"@en ;
    skos:definition "EMODnet Human Activities thematic portal (fisheries, shipping, aquaculture, offshore installations, dredging)."@en ;
    skos:exactMatch <https://emodnet.ec.europa.eu/en/human-activities> .

ind:emodnet-physics a skos:Concept ;
    skos:prefLabel "EMODnet — Physics"@en ;
    skos:definition "EMODnet Physics thematic portal (temperature, salinity, currents, waves, sea level)."@en ;
    skos:exactMatch <https://emodnet.ec.europa.eu/en/physics> .

ind:emodnet-seabed-habitats a skos:Concept ;
    skos:prefLabel "EMODnet — Seabed Habitats"@en ;
    skos:definition "EMODnet Seabed Habitats thematic portal (broad-scale predictive habitat maps)."@en ;
    skos:exactMatch <https://emodnet.ec.europa.eu/en/seabed-habitats> .


# --- Theme assignments: Indicators & ObservableProperties (indo:) -----


# Socio-economic indicators.
indo:number-of-jobs                   dcterms:subject ind:emodnet-human-activities .
indo:fisheries-production             dcterms:subject ind:emodnet-human-activities .
indo:bird-tourism                     dcterms:subject ind:emodnet-human-activities , ind:emodnet-biology .

# Reef-effect equation output and its biological input baseline.
indo:floating-wind-reef-biomass-effect  dcterms:subject ind:emodnet-biology , ind:emodnet-seabed-habitats , ind:emodnet-human-activities .
indo:baseline-benthic-biomass-density   dcterms:subject ind:emodnet-biology , ind:emodnet-seabed-habitats .
indo:benthic-biomass-density-mareano    dcterms:subject ind:emodnet-biology , ind:emodnet-seabed-habitats .
indo:benthic-biomass-density-imr-baseline dcterms:subject ind:emodnet-biology , ind:emodnet-seabed-habitats .

# Catch indicators.
indo:fish-catch                       dcterms:subject ind:emodnet-human-activities .
indo:catch_herring_SV_All             dcterms:subject ind:emodnet-human-activities .
indo:catch_herring_LV_All             dcterms:subject ind:emodnet-human-activities .
indo:catch_sprat_SV_All               dcterms:subject ind:emodnet-human-activities .
indo:catch_sprat_LV_All               dcterms:subject ind:emodnet-human-activities .

# Landing-value indicators.
indo:fish-landing-value               dcterms:subject ind:emodnet-human-activities .
indo:landing_value_herring_SV         dcterms:subject ind:emodnet-human-activities .
indo:landing_value_herring_LV         dcterms:subject ind:emodnet-human-activities .
indo:landing_value_sprat_SV           dcterms:subject ind:emodnet-human-activities .
indo:landing_value_sprat_LV           dcterms:subject ind:emodnet-human-activities .

# Value-added indicators.
indo:fleet-value-added                dcterms:subject ind:emodnet-human-activities .
indo:VA_SV_All                        dcterms:subject ind:emodnet-human-activities .
indo:VA_LV_All                        dcterms:subject ind:emodnet-human-activities .

# Fish-stock biology observables.
indo:fish-stock-biomass               dcterms:subject ind:emodnet-biology .
indo:mean_biomass_herring             dcterms:subject ind:emodnet-biology .
indo:mean_biomass_sprat               dcterms:subject ind:emodnet-biology .
indo:B_herring_tot                    dcterms:subject ind:emodnet-biology .
indo:fish-stock-growth-rate           dcterms:subject ind:emodnet-biology .
indo:yearly_growth_herring            dcterms:subject ind:emodnet-biology .
indo:fish-stock-carrying-capacity-increment  dcterms:subject ind:emodnet-biology .
indo:K_herring_reg_inc                dcterms:subject ind:emodnet-biology .
indo:fish-stock-growth-suppression-flag      dcterms:subject ind:emodnet-biology .
indo:stop_herring_growth              dcterms:subject ind:emodnet-biology .

# Prices & markets.
indo:fish-ex-vessel-price             dcterms:subject ind:emodnet-human-activities .
indo:herring_price_fish_meal          dcterms:subject ind:emodnet-human-activities .
indo:sprat_price                      dcterms:subject ind:emodnet-human-activities .
indo:herring_price_human_cons         dcterms:subject ind:emodnet-human-activities .
indo:fuel_price                       dcterms:subject ind:emodnet-human-activities .
indo:fish-market-state                dcterms:subject ind:emodnet-human-activities .
indo:SV_herring_market                dcterms:subject ind:emodnet-human-activities .

# Fleet operations.
indo:fleet-fuel-consumption           dcterms:subject ind:emodnet-human-activities .
indo:fuel_consumption_SV              dcterms:subject ind:emodnet-human-activities .
indo:fuel_consumption_LV              dcterms:subject ind:emodnet-human-activities .
indo:fleet-fishing-radius             dcterms:subject ind:emodnet-human-activities .
indo:SV_fishing_radius                dcterms:subject ind:emodnet-human-activities .

# Management observables (TAC reporting, season/closure state).
indo:implemented-herring-tac          dcterms:subject ind:emodnet-human-activities .
indo:TAC_herring_Sweden_impl          dcterms:subject ind:emodnet-human-activities .
indo:herring-tac-increment            dcterms:subject ind:emodnet-human-activities .
indo:TAC_herring_inc_SV               dcterms:subject ind:emodnet-human-activities .
indo:TAC_share_B_herring              dcterms:subject ind:emodnet-human-activities .
indo:TAC_herring_est_error            dcterms:subject ind:emodnet-human-activities .
indo:TAC_herring_type                 dcterms:subject ind:emodnet-human-activities .
indo:fishing-season-state             dcterms:subject ind:emodnet-human-activities .
indo:winter_closure_length            dcterms:subject ind:emodnet-human-activities .


# --- Theme assignments: Properties (indp:) ----------------------------

# Offshore wind infrastructure (Human Activities; reef-related ones also Biology / Seabed Habitats).
indp:number-of-turbines               dcterms:subject ind:emodnet-human-activities .
indp:area-use-by-wind-park            dcterms:subject ind:emodnet-human-activities .
indp:submerged-infrastructure-area    dcterms:subject ind:emodnet-human-activities , ind:emodnet-seabed-habitats .
indp:submerged-infrastructure-area-utsira-design  dcterms:subject ind:emodnet-human-activities , ind:emodnet-seabed-habitats .

# Reef-effect equation biology parameters.
indp:reef-aggregation-index           dcterms:subject ind:emodnet-biology , ind:emodnet-seabed-habitats .
indp:reef-aggregation-index-mytilus   dcterms:subject ind:emodnet-biology , ind:emodnet-seabed-habitats .
indp:reef-aggregation-index-buccinum  dcterms:subject ind:emodnet-biology , ind:emodnet-seabed-habitats .
indp:reef-aggregation-index-asterias  dcterms:subject ind:emodnet-biology , ind:emodnet-seabed-habitats .
indp:colonisation-time-factor         dcterms:subject ind:emodnet-biology , ind:emodnet-seabed-habitats .
indp:colonisation-time-factor-default dcterms:subject ind:emodnet-biology , ind:emodnet-seabed-habitats .

# TAC management parameters.
indp:total-allowable-catch            dcterms:subject ind:emodnet-human-activities .
indp:herring-tac                      dcterms:subject ind:emodnet-human-activities .
indp:current_TAC_herring              dcterms:subject ind:emodnet-human-activities .
indp:TAC_herring_share                dcterms:subject ind:emodnet-human-activities .
indp:TAC_herring_share_sv             dcterms:subject ind:emodnet-human-activities .

# Dispersal-rate parameters (population dynamics = Biology).
indp:dispersal_rate_property          dcterms:subject ind:emodnet-biology .
indp:even_dispersal_rate              dcterms:subject ind:emodnet-biology .
indp:winter_dispersal_rate            dcterms:subject ind:emodnet-biology .
indp:spawning_dispersal_rate          dcterms:subject ind:emodnet-biology .

# Closure-rule and fishery-control parameters.
indp:closure_type_property            dcterms:subject ind:emodnet-human-activities .
indp:winter_closure_type              dcterms:subject ind:emodnet-human-activities .
indp:spawning_closure_type            dcterms:subject ind:emodnet-human-activities .
indp:trawling_limit                   dcterms:subject ind:emodnet-human-activities .
indp:fishing_algorithm                dcterms:subject ind:emodnet-human-activities .

# Season state parameters.
indp:current_herring_season           dcterms:subject ind:emodnet-human-activities .
indp:current_management_season        dcterms:subject ind:emodnet-human-activities .

```


### DAPSIM biomass-density conceptual model
#### ttl
```ttl
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix ssn: <http://www.w3.org/ns/ssn/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix quantitykind: <http://qudt.org/vocab/quantitykind/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix schema: <https://schema.org/> .
@prefix dwc: <http://rs.tdwg.org/dwc/terms/> .
@prefix sdn: <https://vocab.nerc.ac.uk/collection/SDN/current/> .
@prefix indo: <https://w3id.org/indicators/marine/obs/> .
@prefix indp: <https://w3id.org/indicators/marine/parameters/> .
@prefix ind: <https://w3id.org/indicators/marine/> .
@prefix dapsim: <https://w3id.org/indicators/marine/dapsim/> .
@prefix im: <https://w3id.org/indicators/marine/indicator-model/> .

ind:catalog a dcat:Catalog ;
    rdfs:label "SEADOTS Resource Catalog"@en ;
    dcterms:title "SEADOTS Resource Catalog"@en ;
    dcterms:description "Main catalog for SEADOTS indicators and conceptual models."@en ;
    dcterms:hasPart ind:dapsim-scheme ;
    dcat:dataset ind:dapsim-scheme .

ind:dapsim-scheme a skos:ConceptScheme ;
    dcterms:isPartOf ind:catalog ; # Backlink for discovery
    skos:prefLabel "SEADOTS DAPSIM Indicator Model Scheme"@en ;
    skos:definition "A concept scheme for DAPSIM-aligned SeaDOTs indicator conceptual models, roles, components, pipeline stages and validation hooks."@en ;
    # --- TOP CONCEPTS (added for VocPrez/Prez UI visibility) ---
    # Only concepts WITHOUT skos:broader are listed — narrowers are reached via skos:broader.
    skos:hasTopConcept im:dapsim-biomass-density-conceptual-model,
        dapsim:DAPSIMElement,
        im:IndicatorComponent,
        im:PipelineStage,
        im:ValidationProtocol .

im:dapsim-biomass-density-conceptual-model a dcat:Dataset, skos:Concept ;
    rdfs:label "DAPSIM conceptual model for benthic biomass-density indicators"@en ;
    skos:prefLabel "DAPSIM conceptual model for benthic biomass-density indicators"@en ;
    skos:definition "Conceptual model for representing benthic biomass density as a transparent DAPSIM State indicator with HELCOM-style components, FAIR semantic bindings, deterministic pipeline stages, validation hooks and policy context."@en ;
    skos:inScheme ind:dapsim-scheme ;
    skos:narrower im:offshore-renewable-energy-demand,
        im:floating-wind-farm-development,
        im:hard-substrate-introduction,
        im:benthic-biomass-density-state,
        im:reef-associated-biomass-impact,
        im:monitoring-and-adaptive-management ;
    dcterms:title "DAPSIM conceptual model for benthic biomass-density indicators"@en ;
    dcterms:description "Conceptual TTL model for representing benthic biomass density as a transparent DAPSIM State indicator with HELCOM-style indicator components, FAIR semantic bindings, deterministic pipeline stages, validation hooks and policy context."@en ;
    dcterms:source [
        dcterms:title "DAPSIM Framework and Technical Indicator Requirements"@en ;
        dcterms:description "User-provided recommendations document summarising DAPSIM alignment, HELCOM indicator components, FAIR semantics, deterministic workflows and validation protocols."@en
    ] ;
    dcterms:references indo:baseline-benthic-biomass-density,
        indo:benthic-biomass-density-mareano,
        indo:benthic-biomass-density-imr-baseline,
        <https://helcom.fi/baltic-sea-action-plan/>,
        <https://www.ices.dk/>,
        <https://dwc.tdwg.org/>,
        <https://vocab.nerc.ac.uk/> ;
    dcat:keyword "DAPSIM", "HELCOM", "indicator", "benthic biomass density", "FAIR", "Digital Twin" .

# ----------------------------------------------------------------------
# DAPSIM structural classes
# ----------------------------------------------------------------------

dapsim:DAPSIMElement a owl:Class, skos:Concept ;
    rdfs:label "DAPSIM element"@en ;
    skos:prefLabel "DAPSIM element"@en ;
    skos:definition "A causal-chain role in the DAPSIM framework: Driver, Activity, Pressure, State, Impact or Measure."@en ;
    skos:inScheme ind:dapsim-scheme ;
    skos:narrower dapsim:Driver,
        dapsim:Activity,
        dapsim:Pressure,
        dapsim:State,
        dapsim:Impact,
        dapsim:Measure .

dapsim:Driver a owl:Class, skos:Concept ;
    rdfs:subClassOf dapsim:DAPSIMElement ;
    rdfs:label "Driver"@en ;
    skos:prefLabel "Driver"@en ;
    skos:definition "A societal or natural driver that motivates activities affecting the marine environment."@en ;
    skos:broader dapsim:DAPSIMElement ;
    skos:narrower im:offshore-renewable-energy-demand ;
    skos:inScheme ind:dapsim-scheme .

dapsim:Activity a owl:Class, skos:Concept ;
    rdfs:subClassOf dapsim:DAPSIMElement ;
    rdfs:label "Activity"@en ;
    skos:prefLabel "Activity"@en ;
    skos:definition "A human activity or operational process that can produce pressures or collect evidence."@en ;
    skos:broader dapsim:DAPSIMElement ;
    skos:narrower im:floating-wind-farm-development ;
    skos:inScheme ind:dapsim-scheme .

dapsim:Pressure a owl:Class, skos:Concept ;
    rdfs:subClassOf dapsim:DAPSIMElement ;
    rdfs:label "Pressure"@en ;
    skos:prefLabel "Pressure"@en ;
    skos:definition "A direct pressure exerted on the ecosystem by an activity."@en ;
    skos:broader dapsim:DAPSIMElement ;
    skos:narrower im:hard-substrate-introduction ;
    skos:inScheme ind:dapsim-scheme .

dapsim:State a owl:Class, skos:Concept ;
    rdfs:subClassOf dapsim:DAPSIMElement ;
    rdfs:label "State"@en ;
    skos:prefLabel "State"@en ;
    skos:definition "An environmental state variable or indicator describing ecosystem condition."@en ;
    skos:broader dapsim:DAPSIMElement ;
    skos:narrower im:benthic-biomass-density-state ;
    skos:inScheme ind:dapsim-scheme .

dapsim:Impact a owl:Class, skos:Concept ;
    rdfs:subClassOf dapsim:DAPSIMElement ;
    rdfs:label "Impact"@en ;
    skos:prefLabel "Impact"@en ;
    skos:definition "A consequence of state change for ecosystems or society."@en ;
    skos:broader dapsim:DAPSIMElement ;
    skos:narrower im:reef-associated-biomass-impact ;
    skos:inScheme ind:dapsim-scheme .

dapsim:Measure a owl:Class, skos:Concept ;
    rdfs:subClassOf dapsim:DAPSIMElement ;
    rdfs:label "Measure"@en ;
    skos:prefLabel "Measure"@en ;
    skos:definition "A management response, policy action, mitigation or monitoring measure."@en ;
    skos:broader dapsim:DAPSIMElement ;
    skos:narrower im:monitoring-and-adaptive-management ;
    skos:inScheme ind:dapsim-scheme .

dapsim:hasDAPSIMRole a rdf:Property ;
    rdfs:label "has DAPSIM role"@en ;
    rdfs:domain sosa:ObservableProperty ;
    rdfs:range dapsim:DAPSIMElement .

dapsim:causallyPrecedes a rdf:Property ;
    rdfs:label "causally precedes"@en ;
    skos:definition "Links DAPSIM elements in the recommended causal order from Drivers and Activities through Pressures and State to Impacts and Measures."@en .

# ----------------------------------------------------------------------
# HELCOM-style indicator components and DT pipeline stages
# ----------------------------------------------------------------------

im:IndicatorComponent a owl:Class, skos:Concept ;
    rdfs:label "Indicator component"@en ;
    skos:prefLabel "Indicator component"@en ;
    skos:definition "A transparent indicator component recommended by HELCOM-style indicator guidance."@en ;
    skos:inScheme ind:dapsim-scheme ;
    skos:narrower im:ScientificConcept,
        im:AssessmentProtocol,
        im:MonitoringMethodology,
        im:ThresholdValue,
        im:DataManagement,
        im:EvaluationResult,
        im:PolicyContext .

im:ScientificConcept a owl:Class, skos:Concept ;
    rdfs:subClassOf im:IndicatorComponent ;
    rdfs:label "Scientific concept"@en ;
    skos:prefLabel "Scientific concept"@en ;
    skos:broader im:IndicatorComponent ;
    skos:narrower im:biomass-density-scientific-concept ;
    skos:inScheme ind:dapsim-scheme .

im:AssessmentProtocol a owl:Class, skos:Concept ;
    rdfs:subClassOf im:IndicatorComponent ;
    rdfs:label "Assessment protocol"@en ;
    skos:prefLabel "Assessment protocol"@en ;
    skos:broader im:IndicatorComponent ;
    skos:narrower im:biomass-density-assessment-protocol ;
    skos:inScheme ind:dapsim-scheme .

im:MonitoringMethodology a owl:Class, skos:Concept ;
    rdfs:subClassOf im:IndicatorComponent ;
    rdfs:label "Monitoring or methodology"@en ;
    skos:prefLabel "Monitoring or methodology"@en ;
    skos:broader im:IndicatorComponent ;
    skos:narrower im:biomass-density-monitoring-methodology ;
    skos:inScheme ind:dapsim-scheme .

im:ThresholdValue a owl:Class, skos:Concept ;
    rdfs:subClassOf im:IndicatorComponent ;
    rdfs:label "Threshold value"@en ;
    skos:prefLabel "Threshold value"@en ;
    skos:broader im:IndicatorComponent ;
    skos:narrower im:biomass-density-threshold ;
    skos:inScheme ind:dapsim-scheme .

im:DataManagement a owl:Class, skos:Concept ;
    rdfs:subClassOf im:IndicatorComponent ;
    rdfs:label "Data management"@en ;
    skos:prefLabel "Data management"@en ;
    skos:broader im:IndicatorComponent ;
    skos:narrower im:biomass-density-data-management ;
    skos:inScheme ind:dapsim-scheme .

im:EvaluationResult a owl:Class, skos:Concept ;
    rdfs:subClassOf im:IndicatorComponent ;
    rdfs:label "Evaluation result"@en ;
    skos:prefLabel "Evaluation result"@en ;
    skos:broader im:IndicatorComponent ;
    skos:narrower im:biomass-density-evaluation-result ;
    skos:inScheme ind:dapsim-scheme .

im:PolicyContext a owl:Class, skos:Concept ;
    rdfs:subClassOf im:IndicatorComponent ;
    rdfs:label "Policy context"@en ;
    skos:prefLabel "Policy context"@en ;
    skos:broader im:IndicatorComponent ;
    skos:narrower im:biomass-density-policy-context ;
    skos:inScheme ind:dapsim-scheme .

im:PipelineStage a owl:Class, skos:Concept ;
    rdfs:label "Digital Twin indicator pipeline stage"@en ;
    skos:prefLabel "Digital Twin indicator pipeline stage"@en ;
    skos:definition "A deterministic workflow stage used to move an indicator from model definition to regional deployment."@en ;
    skos:inScheme ind:dapsim-scheme ;
    skos:narrower im:biomass-density-model-definition,
        im:biomass-density-data-availability,
        im:biomass-density-model-binding,
        im:biomass-density-test-execution,
        im:biomass-density-scaling .

im:ValidationProtocol a owl:Class, skos:Concept ;
    rdfs:label "Validation protocol"@en ;
    skos:prefLabel "Validation protocol"@en ;
    skos:definition "A validation hook or rule set used to test whether indicator observations satisfy the conceptual model requirements."@en ;
    skos:inScheme ind:dapsim-scheme ;
    skos:narrower im:biomass-density-validation-shape .

im:hasComponent a rdf:Property ;
    rdfs:label "has indicator component"@en ;
    rdfs:domain sosa:ObservableProperty ;
    rdfs:range im:IndicatorComponent .

im:hasPipelineStage a rdf:Property ;
    rdfs:label "has pipeline stage"@en ;
    rdfs:domain sosa:ObservableProperty ;
    rdfs:range im:PipelineStage .

im:hasFormula a rdf:Property ;
    rdfs:label "has formula"@en ;
    skos:definition "Plain-text or machine-readable expression used to compute an indicator or variable."@en .

im:usesVocabulary a rdf:Property ;
    rdfs:label "uses vocabulary"@en ;
    skos:definition "External controlled vocabulary used by the model for semantic harmony."@en .

im:requiresValidation a rdf:Property ;
    rdfs:label "requires validation"@en ;
    skos:definition "Links an indicator to a validation requirement or SHACL shape."@en .

# ----------------------------------------------------------------------
# DAPSIM conceptual model for benthic biomass density
# ----------------------------------------------------------------------

im:offshore-renewable-energy-demand a dapsim:Driver, skos:Concept ;
    skos:prefLabel "Offshore renewable energy demand"@en ;
    skos:definition "Societal and policy demand for offshore renewable energy that motivates marine infrastructure planning."@en ;
    skos:broader im:dapsim-biomass-density-conceptual-model,
        dapsim:Driver ;
    skos:inScheme ind:dapsim-scheme .

im:floating-wind-farm-development a dapsim:Activity, skos:Concept ;
    skos:prefLabel "Floating wind farm development"@en ;
    skos:definition "Planning, installation and operation of floating offshore wind infrastructure."@en ;
    skos:broader im:dapsim-biomass-density-conceptual-model,
        dapsim:Activity ;
    skos:inScheme ind:dapsim-scheme .

im:hard-substrate-introduction a dapsim:Pressure, skos:Concept ;
    skos:prefLabel "Hard-substrate introduction"@en ;
    skos:definition "Introduction of submerged artificial hard substrate that changes available habitat and colonisation opportunity."@en ;
    skos:broader im:dapsim-biomass-density-conceptual-model,
        dapsim:Pressure ;
    skos:inScheme ind:dapsim-scheme .

im:benthic-biomass-density-state a dapsim:State, skos:Concept ;
    skos:prefLabel "Benthic biomass-density state"@en ;
    skos:definition "State of benthic biomass per seabed area, indexed by taxon, area and time."@en ;
    skos:broader im:dapsim-biomass-density-conceptual-model,
        dapsim:State ;
    skos:inScheme ind:dapsim-scheme ;
    skos:narrower indo:baseline-benthic-biomass-density ;
    skos:related indo:baseline-benthic-biomass-density ;
    dapsim:hasDAPSIMRole dapsim:State .

im:reef-associated-biomass-impact a dapsim:Impact, skos:Concept ;
    skos:prefLabel "Reef-associated biomass impact"@en ;
    skos:definition "Estimated change in reef-associated biomass attributable to infrastructure and colonisation."@en ;
    skos:broader im:dapsim-biomass-density-conceptual-model,
        dapsim:Impact ;
    skos:inScheme ind:dapsim-scheme ;
    skos:related indo:floating-wind-reef-biomass-effect ;
    prov:wasDerivedFrom indo:baseline-benthic-biomass-density,
        indp:submerged-infrastructure-area,
        indp:reef-aggregation-index,
        indp:colonisation-time-factor .

im:monitoring-and-adaptive-management a dapsim:Measure, skos:Concept ;
    skos:prefLabel "Monitoring and adaptive management"@en ;
    skos:definition "Measures that use transparent indicator results, thresholds and validation evidence to adapt monitoring or management."@en ;
    skos:broader im:dapsim-biomass-density-conceptual-model,
        dapsim:Measure ;
    skos:inScheme ind:dapsim-scheme .

im:offshore-renewable-energy-demand dapsim:causallyPrecedes im:floating-wind-farm-development .
im:floating-wind-farm-development dapsim:causallyPrecedes im:hard-substrate-introduction .
im:hard-substrate-introduction dapsim:causallyPrecedes im:benthic-biomass-density-state .
im:benthic-biomass-density-state dapsim:causallyPrecedes im:reef-associated-biomass-impact .
im:reef-associated-biomass-impact dapsim:causallyPrecedes im:monitoring-and-adaptive-management .

indo:baseline-benthic-biomass-density a dapsim:State, skos:Concept ;
    dapsim:hasDAPSIMRole dapsim:State ;
    skos:inScheme ind:dapsim-scheme ;
    skos:broader im:benthic-biomass-density-state ;
    skos:scopeNote "In the DAPSIM model this is a State indicator: it describes ecosystem condition before installation or in a matched control area, and it can feed Impact indicators such as floating-wind reef biomass effect."@en ;
    im:hasFormula "D_pre,i = sum(weight_kg) / sum(sampled_area_m2), grouped by taxon i, area and time" ;
    im:usesVocabulary dwc:scientificName,
        dwc:individualCount,
        dwc:materialSampleID,
        sosa:hasSimpleResult,
        sosa:usedProcedure,
        sdn:cruise,
        sdn:depthMax,
        qudt:QuantityValue,
        quantitykind:SurfaceDensity ;
    im:hasComponent im:biomass-density-scientific-concept,
        im:biomass-density-assessment-protocol,
        im:biomass-density-monitoring-methodology,
        im:biomass-density-threshold,
        im:biomass-density-data-management,
        im:biomass-density-evaluation-result,
        im:biomass-density-policy-context ;
    im:hasPipelineStage im:biomass-density-model-definition,
        im:biomass-density-data-availability,
        im:biomass-density-model-binding,
        im:biomass-density-test-execution,
        im:biomass-density-scaling ;
    im:requiresValidation im:biomass-density-validation-shape .

im:biomass-density-scientific-concept a im:ScientificConcept, skos:Concept ;
    skos:prefLabel "Scientific concept for benthic biomass density"@en ;
    skos:definition "Benthic biomass density is biomass per seabed area for a taxon or assemblage, used as a baseline ecosystem-state variable."@en ;
    skos:broader im:ScientificConcept ;
    skos:inScheme ind:dapsim-scheme ;
    qudt:hasQuantityKind quantitykind:SurfaceDensity ;
    schema:unitText "kg m-2" .

im:biomass-density-assessment-protocol a im:AssessmentProtocol, skos:Concept ;
    skos:prefLabel "Assessment protocol for benthic biomass density"@en ;
    skos:definition "Compute taxon-indexed density from harmonised observations, preserve provenance, compare against thresholds where agreed, and expose uncertainty and validation status."@en ;
    skos:broader im:AssessmentProtocol ;
    skos:inScheme ind:dapsim-scheme .

im:biomass-density-monitoring-methodology a im:MonitoringMethodology, skos:Concept ;
    skos:prefLabel "Monitoring methodology for benthic biomass density"@en ;
    skos:definition "Accept source observations from MAREANO, IMR or compatible survey programmes, with scientific name, sample identifier, station/locality, equipment/procedure, depth, count and weight mapped to controlled vocabularies."@en ;
    skos:broader im:MonitoringMethodology ;
    skos:inScheme ind:dapsim-scheme ;
    im:usesVocabulary dwc:scientificName,
        dwc:individualCount,
        dwc:materialSampleID,
        sosa:usedProcedure,
        sdn:cruise,
        sdn:depthMax .

im:biomass-density-threshold a im:ThresholdValue, skos:Concept ;
    skos:prefLabel "Benthic biomass-density threshold placeholder"@en ;
    skos:definition "Regionally agreed Good Status threshold for benthic biomass density. The current SeaDOTs examples do not assert a threshold; this node records the requirement and can be specialised per assessment unit, habitat or taxon."@en ;
    skos:broader im:ThresholdValue ;
    skos:inScheme ind:dapsim-scheme ;
    skos:narrower im:good-status-threshold-availability ;
    dqv:inDimension im:good-status-threshold-availability ;
    rdf:value "threshold-to-be-defined-regionally" .

im:good-status-threshold-availability a dqv:Dimension, skos:Concept ;
    skos:prefLabel "Good Status threshold availability"@en ;
    skos:definition "Whether a regionally agreed and scientifically justified Good Status threshold is available for this indicator."@en ;
    skos:broader im:biomass-density-threshold ;
    skos:inScheme ind:dapsim-scheme .

im:biomass-density-data-management a im:DataManagement, skos:Concept ;
    skos:prefLabel "Data management for benthic biomass density"@en ;
    skos:definition "Indicator data must be findable, accessible, interoperable and reusable, with source API links, licence, provenance, temporal scope, geometry, vocabulary mappings and validation reports."@en ;
    skos:broader im:DataManagement ;
    skos:inScheme ind:dapsim-scheme ;
    dcterms:conformsTo <https://www.go-fair.org/fair-principles/> .

im:biomass-density-evaluation-result a im:EvaluationResult, skos:Concept ;
    skos:prefLabel "Evaluation result for benthic biomass density"@en ;
    skos:definition "An evaluation result should carry density values, units, feature of interest, observation time, uncertainty, data-quality status and threshold comparison where thresholds exist."@en ;
    skos:broader im:EvaluationResult ;
    skos:inScheme ind:dapsim-scheme ;
    dcterms:conformsTo sosa:Observation .

im:biomass-density-policy-context a im:PolicyContext, skos:Concept ;
    skos:prefLabel "Policy context for benthic biomass density"@en ;
    skos:definition "Benthic biomass-density outputs support Baltic Sea Action Plan style ecosystem assessment and the traceability of routes from activity and pressure to environmental state and management measures."@en ;
    skos:broader im:PolicyContext ;
    skos:inScheme ind:dapsim-scheme ;
    rdfs:seeAlso <https://helcom.fi/baltic-sea-action-plan/> .

# Deterministic Digital Twin pipeline stages recommended by the source PDF.

im:biomass-density-model-definition a im:PipelineStage, skos:Concept ;
    skos:prefLabel "Model definition"@en ;
    skos:definition "Define variables, equations, units and semantic identifiers for biomass-density computation."@en ;
    skos:broader im:PipelineStage ;
    skos:inScheme ind:dapsim-scheme ;
    im:hasFormula "D_pre,i = biomass_i / sampled_area" .

im:biomass-density-data-availability a im:PipelineStage, skos:Concept ;
    skos:prefLabel "Data availability"@en ;
    skos:definition "Map raw survey observations to density-estimation inputs with controlled terms for taxa, samples, gear, station, depth and weight."@en ;
    skos:broader im:PipelineStage ;
    skos:inScheme ind:dapsim-scheme .

im:biomass-density-model-binding a im:PipelineStage, skos:Concept ;
    skos:prefLabel "Model binding"@en ;
    skos:definition "Bind MAREANO/IMR observations to standard assessment templates and to the SeaDOTs `baseline-benthic-biomass-density` property."@en ;
    skos:broader im:PipelineStage ;
    skos:inScheme ind:dapsim-scheme ;
    prov:used indo:benthic-biomass-density-mareano,
        indo:benthic-biomass-density-imr-baseline .

im:biomass-density-test-execution a im:PipelineStage, skos:Concept ;
    skos:prefLabel "Test execution"@en ;
    skos:definition "Execute the building-block harness and sandbox validation so results are not black-box outputs."@en ;
    skos:broader im:PipelineStage ;
    skos:inScheme ind:dapsim-scheme ;
    prov:used <https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-mareano>,
        <https://w3id.org/ogc/hosted/seadots/benthic-biomass-density-imr> .

im:biomass-density-scaling a im:PipelineStage, skos:Concept ;
    skos:prefLabel "Scaling"@en ;
    skos:definition "Deploy persistent building blocks and vocabularies for regional reuse across assessment units, taxa and time windows."@en ;
    skos:broader im:PipelineStage ;
    skos:inScheme ind:dapsim-scheme .

# Minimal SHACL hook for validation-protocol traceability.

im:biomass-density-validation-shape a sh:NodeShape, im:ValidationProtocol, skos:Concept ;
    rdfs:label "Benthic biomass-density validation shape"@en ;
    skos:prefLabel "Benthic biomass-density validation shape"@en ;
    skos:definition "Conceptual validation hook: observation features should identify the observed property, feature of interest, result value and unit before being accepted into an assessment pipeline."@en ;
    skos:broader im:ValidationProtocol ;
    skos:inScheme ind:dapsim-scheme ;
    sh:targetClass sosa:Observation ;
    sh:property [
        sh:path sosa:observedProperty ;
        sh:hasValue indo:baseline-benthic-biomass-density ;
        sh:minCount 1
    ] ;
    sh:property [
        sh:path sosa:hasFeatureOfInterest ;
        sh:minCount 1
    ] ;
    sh:property [
        sh:path sosa:hasSimpleResult ;
        sh:minCount 1
    ] .

```

## Sources

* [SEADOTS Indicator Vocabulary](https://w3id.org/indicators/marine/)
* [OIM Oceans Information Model](https://github.com/ILIAD-ocean-twin/OIM)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/oim-variables`

