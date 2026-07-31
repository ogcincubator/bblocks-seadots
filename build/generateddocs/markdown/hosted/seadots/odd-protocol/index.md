
# ODD Protocol Description Record (Schema)

`ogc.hosted.seadots.odd-protocol` *v0.1*

OGC API Records profile for simulation model publications using the ODD Protocol (Overview, Design concepts, Details). Provides a structured, open-ended scaffold for describing agent-based and individual-based models; domain-specific vocabularies (NERC, CF, Darwin Core, ICES) are injected at the entity and variable level by domain profiles.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ODD Protocol Description Record

## Purpose

This building block defines an OGC API Records profile for publications and descriptions that use the **ODD Protocol** (Overview, Design concepts, Details) for documenting agent-based and individual-based simulation models (Grimm et al. 2020, https://doi.org/10.18564/jasss.4259).

The record combines:

- **GeoDCAT-Records** (`ogc.geo.geodcat.geodcat-records`) as the outer bibliographic scaffold — providing title, authors, DOI, themes, keywords, and links via OGC API Records / DCAT
- **PROV profile** (`ogc.geo.geodcat.geodcat-records-prov`) for model lineage and derivation chains
- **Open Science** (`ogc.osc.ontology.openscience`) for code and workflow links
- An **`odd` extension object** encoding all seven ODD elements as structured, machine-readable properties

## Design Philosophy

The `odd` extension is intentionally **open-ended at the vocabulary level**. State variable `vocabularyTerm` fields and `inputData[].vocabularyTerm` fields are annotation slots where domain profiles inject authoritative URIs:

| Domain | Preferred vocabulary |
|---|---|
| Marine physics / chemistry | NERC P01/P02/P06, CF standard names |
| Marine biology | Darwin Core, WoRMS/OBIS AphiaID |
| Fish stocks | ICES vocabulary |
| Social simulation | FOAF, schema.org, CESSDA |
| General units | QUDT |

This means the base block validates any string in those fields. A domain sub-profile (e.g. `odd-protocol-marine`) would constrain `vocabularyTerm` to a specific vocabulary URI pattern.

## ODD Seven Elements

| Element | Section | Schema key |
|---|---|---|
| Purpose and Patterns | Overview | `odd.purpose`, `odd.patterns` |
| Entities, State Variables and Scales | Overview | `odd.entities` |
| Process Overview and Scheduling | Overview | `odd.processOverview` |
| Design Concepts | Design Concepts | `odd.designConcepts` |
| Initialization | Details | `odd.initialization` |
| Input Data | Details | `odd.inputData` |
| Submodels | Details | `odd.submodels` |

The 11 design concepts (`basicPrinciples`, `emergence`, `adaptation`, `objectives`, `learning`, `prediction`, `sensing`, `interaction`, `stochasticity`, `collectives`, `observation`) are all free-text fields within `odd.designConcepts`.

## Namespace

The `odd:` namespace is provisionally `https://w3id.org/iliad/odd#`. Terms without an established external ontology mapping are defined there. A formal ODD ontology may be registered once the vocabulary stabilises.

## Relationship to TRACE

The TRACE framework (Transparent and Comprehensive model Evaluation) documents broader model development and testing. TRACE documents may be linked via `links[rel="related"]`; a separate `odd-trace` profile would extend this block if structured TRACE encoding is needed.

## Examples

### ODD Protocol second update — Grimm et al. 2020 (JASSS)
#### json
```json
{
  "id": "doi:10.18564/jasss.4259",
  "type": "Feature",
  "geometry": null,
  "time": {
    "date": "2020-03-31"
  },
  "properties": {
    "type": "ScholarlyArticle",
    "title": "The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism",
    "description": "The ODD (Overview, Design concepts, Details) protocol for describing agent-based and individual-based models is now widely used but has persistent weaknesses. This second update addresses those limitations through improved guidance, summary templates, hierarchical approaches for complex models, code-linking recommendations, and explicit pattern-oriented modeling integration.",
    "created": "2020-03-31",
    "updated": "2020-03-31",
    "language": { "code": "en" },
    "externalIds": [
      {
        "scheme": "doi",
        "value": "10.18564/jasss.4259"
      },
      {
        "scheme": "issn",
        "value": "1460-7425"
      }
    ],
    "contacts": [
      {
        "name": "Volker Grimm",
        "roles": ["author"],
        "organization": "Helmholtz Centre for Environmental Research – UFZ; University of Potsdam"
      },
      {
        "name": "Steven F. Railsback",
        "roles": ["author"],
        "organization": "Lang, Railsback & Associates; Humboldt State University"
      },
      {
        "name": "Christian E. Vincenot",
        "roles": ["author"],
        "organization": "Kyoto University"
      },
      {
        "name": "Uta Berger",
        "roles": ["author"],
        "organization": "Technische Universität Dresden"
      }
    ],
    "themes": [
      {
        "concepts": [
          { "id": "agent-based-model",    "label": "Agent-Based Model" },
          { "id": "individual-based-model","label": "Individual-Based Model" },
          { "id": "simulation",            "label": "Simulation" },
          { "id": "model-documentation",   "label": "Model Documentation" },
          { "id": "protocol",              "label": "Protocol" }
        ],
        "scheme": "https://vocabularies.jasss.org/themes"
      }
    ],
    "keywords": [
      "ODD", "agent-based model", "individual-based model",
      "simulation", "model documentation", "protocol", "replication",
      "pattern-oriented modeling", "TRACE"
    ],
    "license": "https://creativecommons.org/licenses/by/3.0/",
    "formats": [
      { "mediaType": "text/html" }
    ],

    "odd": {
      "purpose": "The ODD protocol provides a standardised, community-agreed framework for describing agent-based and individual-based simulation models (ABMs/IBMs). Its purpose is to enable model replication, understanding, and comparison by enforcing complete and logically ordered documentation. This second update improves clarity, supports replication of complex models, and strengthens linkage to Pattern-Oriented Modeling (POM) and the TRACE evaluation framework.",

      "patterns": [
        {
          "name": "Pattern-Oriented Modeling (POM)",
          "description": "A strategy for using multiple observed patterns — at different levels of organisation and for different model structural elements — to constrain, parameterise, and validate a model. Patterns that a model must reproduce become explicit design criteria documented under Purpose.",
          "reference": "https://doi.org/10.1371/journal.pcbi.1000356"
        }
      ],

      "entities": [
        {
          "name": "Simulation Model (abstract template)",
          "entityType": "abstract",
          "stateVariables": [],
          "scales": {
            "spatial": "Domain-specific — must be stated explicitly in the implementing ODD",
            "temporal": "Domain-specific — must state time step unit and total simulation duration"
          }
        }
      ],

      "processOverview": {
        "scheduling": "ODD requires an explicit description of temporal ordering: which processes run within each time step, in what order, and whether agent execution is synchronous, asynchronous, or in randomised order. Scheduling must match the implementation exactly.",
        "processes": [
          {
            "name": "Submodel execution",
            "executedBy": "Simulation engine / scheduling loop",
            "description": "Each process listed in the process overview is executed per step according to the scheduling rules. All processes are detailed in the Submodels section."
          }
        ]
      },

      "designConcepts": {
        "basicPrinciples": "What general theoretical or empirical frame underlies the model? Examples: evolutionary optimisation, decision-field theory, patch dynamics, social norms. Reference the theories explicitly.",
        "emergence": "Which key results emerge from individual agent behaviours and interactions rather than being encoded directly as global model rules? Emergence should be identified and justified, not just asserted.",
        "adaptation": "What adaptive traits do agents have? What environmental or internal information drives adaptive decisions? Describe the decision algorithm (e.g. if-then rules, utility maximisation, evolved strategies).",
        "objectives": "What objectives do agents attempt to satisfy? How are objectives measured (fitness proxy, utility function, simple rule)? Objectives need not be explicit if only implicit in adaptive behaviour.",
        "learning": "Do agents modify their behaviour based on accumulated experience? If so, describe the learning algorithm (reinforcement learning, genetic algorithms, imitation, memory decay).",
        "prediction": "Do agents anticipate future conditions to make decisions? Describe the prediction horizon, method, and any assumptions about agent cognitive capacity.",
        "sensing": "What information about the environment and other agents can an agent perceive? Are all sensing assumptions realistic and justified? Consider information cost and error.",
        "interaction": "What direct interactions occur (e.g. competition, predation, communication, trade)? What indirect interactions occur through shared environmental resources or global variables?",
        "stochasticity": "Which processes use random numbers and why? What probability distributions are used? Is stochasticity used to represent true variability or to represent uncertainty?",
        "collectives": "Are agents aggregated into groups, populations, or networks that exhibit their own behaviours? How do collectives emerge or are they predefined? How do they affect individual agent behaviour?",
        "observation": "How are model outputs collected for analysis? What state variables, aggregated statistics, or emergent patterns are recorded, at what frequency, and at what level of organisation?"
      },

      "initialization": {
        "description": "ODD requires: the number and type of agents at t=0, their initial attribute values (means, distributions, or exact values), spatial configuration, and the rationale for the chosen initial state. For stochastic initialisation, describe how seeds are set.",
        "seed": "Random seeds for initialisation must be reported. State whether results are averaged over multiple seeds or whether a single seed is used for all analyses.",
        "links": []
      },

      "inputData": [],

      "submodels": [
        {
          "name": "Generic Submodel Documentation Template",
          "description": "Each submodel in an implementing ODD must describe: (1) purpose and relationship to the process overview, (2) mathematical equations or algorithmic pseudocode, (3) all parameters with units, values, ranges, and sources, (4) simplifying assumptions and their justification.",
          "equations": "Provide full mathematical specification. Where equations come from published literature, cite sources. Where parameterised empirically, describe the calibration procedure.",
          "parameterization": "All parameters must be listed with: symbol, description, value, unit, source (empirical data, literature, or calibration). Calibrated parameters must reference Supplement S7 for experiment design.",
          "links": []
        }
      ]
    }
  },

  "links": [
    {
      "href": "https://www.jasss.org/23/2/7.html",
      "rel": "canonical",
      "type": "text/html",
      "title": "JASSS 23(2)7 — journal article"
    },
    {
      "href": "https://doi.org/10.18564/jasss.4259",
      "rel": "cite-as",
      "type": "text/html",
      "title": "DOI"
    },
    {
      "href": "https://www.jasss.org/23/2/7/S1.pdf",
      "rel": "related",
      "type": "application/pdf",
      "title": "Supplement S1 — ODD Guidance and checklists"
    },
    {
      "href": "https://www.jasss.org/23/2/7/S2.pdf",
      "rel": "related",
      "type": "application/pdf",
      "title": "Supplement S2 — Summary ODD templates"
    },
    {
      "href": "https://www.jasss.org/23/2/7/S3.pdf",
      "rel": "related",
      "type": "application/pdf",
      "title": "Supplement S3 — Nested ODD for complex models"
    },
    {
      "href": "https://www.jasss.org/23/2/7/S4.pdf",
      "rel": "related",
      "type": "application/pdf",
      "title": "Supplement S4 — ODD for modified/reused models"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/odd-protocol/context.jsonld",
  "id": "doi:10.18564/jasss.4259",
  "type": "Feature",
  "geometry": null,
  "time": {
    "date": "2020-03-31"
  },
  "properties": {
    "type": "ScholarlyArticle",
    "title": "The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism",
    "description": "The ODD (Overview, Design concepts, Details) protocol for describing agent-based and individual-based models is now widely used but has persistent weaknesses. This second update addresses those limitations through improved guidance, summary templates, hierarchical approaches for complex models, code-linking recommendations, and explicit pattern-oriented modeling integration.",
    "created": "2020-03-31",
    "updated": "2020-03-31",
    "language": {
      "code": "en"
    },
    "externalIds": [
      {
        "scheme": "doi",
        "value": "10.18564/jasss.4259"
      },
      {
        "scheme": "issn",
        "value": "1460-7425"
      }
    ],
    "contacts": [
      {
        "name": "Volker Grimm",
        "roles": [
          "author"
        ],
        "organization": "Helmholtz Centre for Environmental Research \u2013 UFZ; University of Potsdam"
      },
      {
        "name": "Steven F. Railsback",
        "roles": [
          "author"
        ],
        "organization": "Lang, Railsback & Associates; Humboldt State University"
      },
      {
        "name": "Christian E. Vincenot",
        "roles": [
          "author"
        ],
        "organization": "Kyoto University"
      },
      {
        "name": "Uta Berger",
        "roles": [
          "author"
        ],
        "organization": "Technische Universit\u00e4t Dresden"
      }
    ],
    "themes": [
      {
        "concepts": [
          {
            "id": "agent-based-model",
            "label": "Agent-Based Model"
          },
          {
            "id": "individual-based-model",
            "label": "Individual-Based Model"
          },
          {
            "id": "simulation",
            "label": "Simulation"
          },
          {
            "id": "model-documentation",
            "label": "Model Documentation"
          },
          {
            "id": "protocol",
            "label": "Protocol"
          }
        ],
        "scheme": "https://vocabularies.jasss.org/themes"
      }
    ],
    "keywords": [
      "ODD",
      "agent-based model",
      "individual-based model",
      "simulation",
      "model documentation",
      "protocol",
      "replication",
      "pattern-oriented modeling",
      "TRACE"
    ],
    "license": "https://creativecommons.org/licenses/by/3.0/",
    "formats": [
      {
        "mediaType": "text/html"
      }
    ],
    "odd": {
      "purpose": "The ODD protocol provides a standardised, community-agreed framework for describing agent-based and individual-based simulation models (ABMs/IBMs). Its purpose is to enable model replication, understanding, and comparison by enforcing complete and logically ordered documentation. This second update improves clarity, supports replication of complex models, and strengthens linkage to Pattern-Oriented Modeling (POM) and the TRACE evaluation framework.",
      "patterns": [
        {
          "name": "Pattern-Oriented Modeling (POM)",
          "description": "A strategy for using multiple observed patterns \u2014 at different levels of organisation and for different model structural elements \u2014 to constrain, parameterise, and validate a model. Patterns that a model must reproduce become explicit design criteria documented under Purpose.",
          "reference": "https://doi.org/10.1371/journal.pcbi.1000356"
        }
      ],
      "entities": [
        {
          "name": "Simulation Model (abstract template)",
          "entityType": "abstract",
          "stateVariables": [],
          "scales": {
            "spatial": "Domain-specific \u2014 must be stated explicitly in the implementing ODD",
            "temporal": "Domain-specific \u2014 must state time step unit and total simulation duration"
          }
        }
      ],
      "processOverview": {
        "scheduling": "ODD requires an explicit description of temporal ordering: which processes run within each time step, in what order, and whether agent execution is synchronous, asynchronous, or in randomised order. Scheduling must match the implementation exactly.",
        "processes": [
          {
            "name": "Submodel execution",
            "executedBy": "Simulation engine / scheduling loop",
            "description": "Each process listed in the process overview is executed per step according to the scheduling rules. All processes are detailed in the Submodels section."
          }
        ]
      },
      "designConcepts": {
        "basicPrinciples": "What general theoretical or empirical frame underlies the model? Examples: evolutionary optimisation, decision-field theory, patch dynamics, social norms. Reference the theories explicitly.",
        "emergence": "Which key results emerge from individual agent behaviours and interactions rather than being encoded directly as global model rules? Emergence should be identified and justified, not just asserted.",
        "adaptation": "What adaptive traits do agents have? What environmental or internal information drives adaptive decisions? Describe the decision algorithm (e.g. if-then rules, utility maximisation, evolved strategies).",
        "objectives": "What objectives do agents attempt to satisfy? How are objectives measured (fitness proxy, utility function, simple rule)? Objectives need not be explicit if only implicit in adaptive behaviour.",
        "learning": "Do agents modify their behaviour based on accumulated experience? If so, describe the learning algorithm (reinforcement learning, genetic algorithms, imitation, memory decay).",
        "prediction": "Do agents anticipate future conditions to make decisions? Describe the prediction horizon, method, and any assumptions about agent cognitive capacity.",
        "sensing": "What information about the environment and other agents can an agent perceive? Are all sensing assumptions realistic and justified? Consider information cost and error.",
        "interaction": "What direct interactions occur (e.g. competition, predation, communication, trade)? What indirect interactions occur through shared environmental resources or global variables?",
        "stochasticity": "Which processes use random numbers and why? What probability distributions are used? Is stochasticity used to represent true variability or to represent uncertainty?",
        "collectives": "Are agents aggregated into groups, populations, or networks that exhibit their own behaviours? How do collectives emerge or are they predefined? How do they affect individual agent behaviour?",
        "observation": "How are model outputs collected for analysis? What state variables, aggregated statistics, or emergent patterns are recorded, at what frequency, and at what level of organisation?"
      },
      "initialization": {
        "description": "ODD requires: the number and type of agents at t=0, their initial attribute values (means, distributions, or exact values), spatial configuration, and the rationale for the chosen initial state. For stochastic initialisation, describe how seeds are set.",
        "seed": "Random seeds for initialisation must be reported. State whether results are averaged over multiple seeds or whether a single seed is used for all analyses.",
        "links": []
      },
      "inputData": [],
      "submodels": [
        {
          "name": "Generic Submodel Documentation Template",
          "description": "Each submodel in an implementing ODD must describe: (1) purpose and relationship to the process overview, (2) mathematical equations or algorithmic pseudocode, (3) all parameters with units, values, ranges, and sources, (4) simplifying assumptions and their justification.",
          "equations": "Provide full mathematical specification. Where equations come from published literature, cite sources. Where parameterised empirically, describe the calibration procedure.",
          "parameterization": "All parameters must be listed with: symbol, description, value, unit, source (empirical data, literature, or calibration). Calibrated parameters must reference Supplement S7 for experiment design.",
          "links": []
        }
      ]
    }
  },
  "links": [
    {
      "href": "https://www.jasss.org/23/2/7.html",
      "rel": "canonical",
      "type": "text/html",
      "title": "JASSS 23(2)7 \u2014 journal article"
    },
    {
      "href": "https://doi.org/10.18564/jasss.4259",
      "rel": "cite-as",
      "type": "text/html",
      "title": "DOI"
    },
    {
      "href": "https://www.jasss.org/23/2/7/S1.pdf",
      "rel": "related",
      "type": "application/pdf",
      "title": "Supplement S1 \u2014 ODD Guidance and checklists"
    },
    {
      "href": "https://www.jasss.org/23/2/7/S2.pdf",
      "rel": "related",
      "type": "application/pdf",
      "title": "Supplement S2 \u2014 Summary ODD templates"
    },
    {
      "href": "https://www.jasss.org/23/2/7/S3.pdf",
      "rel": "related",
      "type": "application/pdf",
      "title": "Supplement S3 \u2014 Nested ODD for complex models"
    },
    {
      "href": "https://www.jasss.org/23/2/7/S4.pdf",
      "rel": "related",
      "type": "application/pdf",
      "title": "Supplement S4 \u2014 ODD for modified/reused models"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix odd: <https://w3id.org/iliad/odd#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix thns: <https://w3id.org/ogc/stac/themes/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<doi:10.18564/jasss.4259> a <file:///github/workspace/ScholarlyArticle>,
        geojson:Feature ;
    dcterms:created "2020-03-31" ;
    dcterms:description "The ODD (Overview, Design concepts, Details) protocol for describing agent-based and individual-based models is now widely used but has persistent weaknesses. This second update addresses those limitations through improved guidance, summary templates, hierarchical approaches for complex models, code-linking recommendations, and explicit pattern-oriented modeling integration." ;
    dcterms:modified "2020-03-31" ;
    dcterms:temporal [ ] ;
    dcterms:title "The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism" ;
    rdfs:seeAlso [ rdfs:label "DOI" ;
            dcterms:format "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://doi.org/10.18564/jasss.4259> ],
        [ rdfs:label "Supplement S2 — Summary ODD templates" ;
            dcterms:format "application/pdf" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://www.jasss.org/23/2/7/S2.pdf> ],
        [ rdfs:label "Supplement S3 — Nested ODD for complex models" ;
            dcterms:format "application/pdf" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://www.jasss.org/23/2/7/S3.pdf> ],
        [ rdfs:label "Supplement S4 — ODD for modified/reused models" ;
            dcterms:format "application/pdf" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://www.jasss.org/23/2/7/S4.pdf> ],
        [ rdfs:label "Supplement S1 — ODD Guidance and checklists" ;
            dcterms:format "application/pdf" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://www.jasss.org/23/2/7/S1.pdf> ],
        [ rdfs:label "JASSS 23(2)7 — journal article" ;
            dcterms:format "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/canonical> ;
            oa:hasTarget <https://www.jasss.org/23/2/7.html> ] ;
    dcat:contactPoint [ ],
        [ ],
        [ ],
        [ ] ;
    dcat:keyword "ODD",
        "TRACE",
        "agent-based model",
        "individual-based model",
        "model documentation",
        "pattern-oriented modeling",
        "protocol",
        "replication",
        "simulation" ;
    dcat:license "https://creativecommons.org/licenses/by/3.0/" ;
    odd: [ odd:designConcepts [ odd:adaptation "What adaptive traits do agents have? What environmental or internal information drives adaptive decisions? Describe the decision algorithm (e.g. if-then rules, utility maximisation, evolved strategies)." ;
                    odd:basicPrinciples "What general theoretical or empirical frame underlies the model? Examples: evolutionary optimisation, decision-field theory, patch dynamics, social norms. Reference the theories explicitly." ;
                    odd:collectives "Are agents aggregated into groups, populations, or networks that exhibit their own behaviours? How do collectives emerge or are they predefined? How do they affect individual agent behaviour?" ;
                    odd:emergence "Which key results emerge from individual agent behaviours and interactions rather than being encoded directly as global model rules? Emergence should be identified and justified, not just asserted." ;
                    odd:interaction "What direct interactions occur (e.g. competition, predation, communication, trade)? What indirect interactions occur through shared environmental resources or global variables?" ;
                    odd:learning "Do agents modify their behaviour based on accumulated experience? If so, describe the learning algorithm (reinforcement learning, genetic algorithms, imitation, memory decay)." ;
                    odd:objectives "What objectives do agents attempt to satisfy? How are objectives measured (fitness proxy, utility function, simple rule)? Objectives need not be explicit if only implicit in adaptive behaviour." ;
                    odd:observation "How are model outputs collected for analysis? What state variables, aggregated statistics, or emergent patterns are recorded, at what frequency, and at what level of organisation?" ;
                    odd:prediction "Do agents anticipate future conditions to make decisions? Describe the prediction horizon, method, and any assumptions about agent cognitive capacity." ;
                    odd:sensing "What information about the environment and other agents can an agent perceive? Are all sensing assumptions realistic and justified? Consider information cost and error." ;
                    odd:stochasticity "Which processes use random numbers and why? What probability distributions are used? Is stochasticity used to represent true variability or to represent uncertainty?" ] ;
            odd:entities ( [ dcterms:title "Simulation Model (abstract template)" ;
                        odd:entityType "abstract" ;
                        odd:scales [ odd:spatialScale "Domain-specific — must be stated explicitly in the implementing ODD" ;
                                odd:temporalScale "Domain-specific — must state time step unit and total simulation duration" ] ;
                        odd:stateVariables () ] ) ;
            odd:initialization [ dcterms:description "ODD requires: the number and type of agents at t=0, their initial attribute values (means, distributions, or exact values), spatial configuration, and the rationale for the chosen initial state. For stochastic initialisation, describe how seeds are set." ;
                    rdfs:seeAlso () ;
                    odd:randomSeed "Random seeds for initialisation must be reported. State whether results are averaged over multiple seeds or whether a single seed is used for all analyses." ] ;
            odd:inputData () ;
            odd:patterns ( [ dcterms:description "A strategy for using multiple observed patterns — at different levels of organisation and for different model structural elements — to constrain, parameterise, and validate a model. Patterns that a model must reproduce become explicit design criteria documented under Purpose." ;
                        dcterms:references <https://doi.org/10.1371/journal.pcbi.1000356> ;
                        dcterms:title "Pattern-Oriented Modeling (POM)" ] ) ;
            odd:processOverview [ odd:processes ( [ dcterms:description "Each process listed in the process overview is executed per step according to the scheduling rules. All processes are detailed in the Submodels section." ;
                                dcterms:title "Submodel execution" ;
                                odd:executedBy "Simulation engine / scheduling loop" ] ) ;
                    odd:scheduling "ODD requires an explicit description of temporal ordering: which processes run within each time step, in what order, and whether agent execution is synchronous, asynchronous, or in randomised order. Scheduling must match the implementation exactly." ] ;
            odd:purpose "The ODD protocol provides a standardised, community-agreed framework for describing agent-based and individual-based simulation models (ABMs/IBMs). Its purpose is to enable model replication, understanding, and comparison by enforcing complete and logically ordered documentation. This second update improves clarity, supports replication of complex models, and strengthens linkage to Pattern-Oriented Modeling (POM) and the TRACE evaluation framework." ;
            odd:submodels ( [ dcterms:description "Each submodel in an implementing ODD must describe: (1) purpose and relationship to the process overview, (2) mathematical equations or algorithmic pseudocode, (3) all parameters with units, values, ranges, and sources, (4) simplifying assumptions and their justification." ;
                        dcterms:title "Generic Submodel Documentation Template" ;
                        rdfs:seeAlso () ;
                        odd:equations "Provide full mathematical specification. Where equations come from published literature, cite sources. Where parameterised empirically, describe the calibration procedure." ;
                        odd:parameterization "All parameters must be listed with: symbol, description, value, unit, source (empirical data, literature, or calibration). Calibrated parameters must reference Supplement S7 for experiment design." ] ) ] ;
    rec:format [ rec:mediaType "text/html" ] ;
    rec:language [ rec:languageCode "en" ] ;
    rec:scopedIdentifier [ rec:id "10.18564/jasss.4259" ;
            rec:scheme "doi" ],
        [ rec:id "1460-7425" ;
            rec:scheme "issn" ] ;
    rec:themes [ thns:concepts [ thns:id "individual-based-model"^^xsd:string ],
                [ thns:id "protocol"^^xsd:string ],
                [ thns:id "agent-based-model"^^xsd:string ],
                [ thns:id "model-documentation"^^xsd:string ],
                [ thns:id "simulation"^^xsd:string ] ;
            thns:scheme "https://vocabularies.jasss.org/themes" ] .


```


### OSMOSE — marine multispecies IBM (ODD)
#### json
```json
{
  "id": "https://osmose-model.org/",
  "type": "Feature",
  "geometry": null,
  "time": {
    "date": "2009-01-01"
  },
  "properties": {
    "type": "SoftwareApplication",
    "title": "OSMOSE — Object-oriented Simulator of Marine Ecosystems: ODD Protocol Description",
    "description": "OSMOSE (Object-oriented Simulator of Marine Ecosystems) is a multispecies, spatially-explicit, individual-based model for marine fish communities. It represents fish populations as super-individuals (schools) and models size-based predation, growth, reproduction, and mortality. The model is designed to investigate the effects of fishing and environmental forcing on ecosystem structure and functioning.",
    "created": "2009-01-01",
    "updated": "2020-01-01",
    "language": { "code": "en" },
    "externalIds": [
      {
        "scheme": "doi",
        "value": "10.1016/j.ecolmodel.2009.07.031"
      },
      {
        "scheme": "url",
        "value": "https://osmose-model.org/"
      },
      {
        "scheme": "github",
        "value": "https://github.com/osmose-model/osmose"
      }
    ],
    "contacts": [
      {
        "name": "Yunne-Jai Shin",
        "roles": ["author", "pointOfContact"],
        "organization": "IRD (Institut de Recherche pour le Développement), MARBEC"
      },
      {
        "name": "Morgane Travers-Trolet",
        "roles": ["author"],
        "organization": "IFREMER"
      },
      {
        "name": "Philippe Cury",
        "roles": ["author"],
        "organization": "IRD"
      },
      {
        "name": "Ricardo Oliveros-Ramos",
        "roles": ["author"],
        "organization": "IRD / IMARPE"
      }
    ],
    "themes": [
      {
        "concepts": [
          { "id": "individual-based-model",   "label": "Individual-Based Model" },
          { "id": "multispecies-model",        "label": "Multispecies Model" },
          { "id": "marine-ecosystem",          "label": "Marine Ecosystem" },
          { "id": "size-based-predation",      "label": "Size-Based Predation" },
          { "id": "fish-community",            "label": "Fish Community" },
          { "id": "end-to-end-model",          "label": "End-to-End Ecosystem Model" }
        ],
        "scheme": "https://vocabularies.osmose-model.org/"
      },
      {
        "concepts": [
          { "id": "http://vocab.nerc.ac.uk/collection/P02/current/FISH/", "label": "Fish abundance" },
          { "id": "http://vocab.nerc.ac.uk/collection/P02/current/BIOL/", "label": "Biological variables" }
        ],
        "scheme": "http://vocab.nerc.ac.uk/collection/P02/current/"
      }
    ],
    "keywords": [
      "OSMOSE", "individual-based model", "multispecies",
      "marine fish", "size-based predation", "super-individual",
      "ecosystem model", "fishing", "low trophic level", "emergent behaviour"
    ],
    "license": "https://www.gnu.org/licenses/gpl-3.0.html",
    "formats": [
      { "mediaType": "application/java-archive", "title": "Java executable (JAR)" },
      { "mediaType": "text/csv",                  "title": "Configuration files" }
    ],

    "odd": {

      "purpose": "OSMOSE was developed to explore the emergent trophic structure of marine fish communities under size-based predation. Its primary purpose is to (1) investigate the multispecies effects of fishing on ecosystem functioning and community structure, (2) simulate the response of fish communities to environmental forcing (e.g. changes in low trophic level production from climate models), and (3) produce realistic predictions of catches, biomass, size spectra, and diet composition that can be compared against observed fisheries and survey data. The model uses a Pattern-Oriented Modeling (POM) approach: schools, catches, biomass time series, mean lengths-at-age, and diet compositions observed in the study area are used simultaneously as calibration targets.",

      "patterns": [
        {
          "name": "Multispecies catch time series",
          "description": "Observed nominal catches (tonnes) per species per year from fisheries statistics. Used to constrain total fishing mortality and species-level biomass in calibration.",
          "reference": "http://vocab.nerc.ac.uk/collection/P01/current/FSHBMS01/"
        },
        {
          "name": "Survey biomass indices",
          "description": "Relative biomass indices (B-hat) from scientific trawl surveys. Used to constrain interannual biomass dynamics per species.",
          "reference": "http://vocab.nerc.ac.uk/collection/P01/current/SDBIOL02/"
        },
        {
          "name": "Mean length at age",
          "description": "Mean length-at-age data from otolith/age-reading programmes used to validate growth submodel trajectories.",
          "reference": "http://vocab.nerc.ac.uk/collection/P01/current/OBSINDL01/"
        },
        {
          "name": "Diet composition",
          "description": "Proportion of each prey type in predator stomach contents from stomach-content analyses. Used to validate the size-based predation submodel.",
          "reference": "https://doi.org/10.1016/S0304-3800(03)00148-8"
        }
      ],

      "entities": [
        {
          "name": "School",
          "entityType": "agent",
          "stateVariables": [
            {
              "name": "species",
              "type": "integer",
              "unit": "dimensionless",
              "range": "[0, nSpecies-1]",
              "description": "Index identifying the focal species this school belongs to"
            },
            {
              "name": "age",
              "type": "real",
              "unit": "years",
              "range": "[0, lifespan]",
              "description": "Age of the school cohort in years",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/AGEBIOLX/"
            },
            {
              "name": "length",
              "type": "real",
              "unit": "cm",
              "range": "[0, Linf]",
              "description": "Mean fork or total length of individual fish within the school",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/OBSINDL01/"
            },
            {
              "name": "weight",
              "type": "real",
              "unit": "g",
              "range": "[0, Wmax]",
              "description": "Mean individual wet weight of fish within the school",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/OBSINDW01/"
            },
            {
              "name": "abundance",
              "type": "real",
              "unit": "#",
              "range": "non-negative",
              "description": "Number of individual fish represented by this super-individual school",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/OBSINDN01/"
            },
            {
              "name": "trophicLevel",
              "type": "real",
              "unit": "dimensionless",
              "range": "[1, 6]",
              "description": "Trophic level estimated dynamically from diet composition at each time step",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/TRPHINDX/"
            },
            {
              "name": "ingestedBiomass",
              "type": "real",
              "unit": "tonnes",
              "range": "non-negative",
              "description": "Total biomass ingested by the school in the current time step across all prey items"
            },
            {
              "name": "starvationMortalityRate",
              "type": "real",
              "unit": "dt-1",
              "range": "[0, 1]",
              "description": "Instantaneous mortality rate from starvation, computed from ratio of ingested biomass to maximum ration"
            },
            {
              "name": "cell",
              "type": "integer",
              "unit": "dimensionless",
              "range": "[0, nCells-1]",
              "description": "Index of the grid cell currently occupied by the school"
            },
            {
              "name": "dietMatrix",
              "type": "list",
              "unit": "tonnes",
              "description": "Vector of biomass consumed from each prey species/size class in the current time step"
            }
          ],
          "scales": {
            "spatial": "One cell per school per time step; cell size is configuration-dependent (typically 0.25° × 0.25° to 1° × 1°)",
            "temporal": "Time step configurable (default 1 month = 1/12 year); lifespan 1–45 years depending on species"
          }
        },
        {
          "name": "BackgroundSchool",
          "entityType": "agent",
          "stateVariables": [
            {
              "name": "species",
              "type": "integer",
              "description": "Index of the background (non-focal) species"
            },
            {
              "name": "length",
              "type": "real",
              "unit": "cm",
              "description": "Mean length of individuals in the background school",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/OBSINDL01/"
            },
            {
              "name": "biomass",
              "type": "real",
              "unit": "tonnes",
              "description": "Total biomass of the background school",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/SDBIOL02/"
            },
            {
              "name": "cell",
              "type": "integer",
              "description": "Current grid cell of the background school"
            }
          ],
          "scales": {
            "spatial": "Same grid as focal schools",
            "temporal": "Updated at each time step from input time series"
          }
        },
        {
          "name": "Resource",
          "entityType": "environment",
          "stateVariables": [
            {
              "name": "biomass",
              "type": "real",
              "unit": "tonnes km-2",
              "range": "non-negative",
              "description": "Areal biomass density of low trophic level resource (phytoplankton, zooplankton, benthos) per grid cell",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/SDBIOL02/"
            },
            {
              "name": "resourceType",
              "type": "string",
              "description": "Functional type: phytoplankton | microzooplankton | mesozooplankton | macrozooplankton | benthos"
            },
            {
              "name": "cell",
              "type": "integer",
              "description": "Grid cell to which this resource unit belongs"
            }
          ],
          "scales": {
            "spatial": "One resource object per functional type per grid cell",
            "temporal": "Updated each time step from external biogeochemical model forcing (ROMS-NPZD or NEMO-ECO3M/PISCES)"
          }
        },
        {
          "name": "Cell",
          "entityType": "patch",
          "stateVariables": [
            {
              "name": "latitude",
              "type": "real",
              "unit": "degrees_north",
              "description": "Latitude of cell centre",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/ALATZZ01/"
            },
            {
              "name": "longitude",
              "type": "real",
              "unit": "degrees_east",
              "description": "Longitude of cell centre",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/ALONZZ01/"
            },
            {
              "name": "area",
              "type": "real",
              "unit": "km2",
              "description": "Planimetric area of the cell (used for biomass density computation)"
            },
            {
              "name": "land",
              "type": "boolean",
              "description": "True if cell is land (excluded from simulation)"
            },
            {
              "name": "schoolsPresent",
              "type": "list",
              "description": "List of School and BackgroundSchool agents currently located in this cell"
            },
            {
              "name": "resourceBiomass",
              "type": "list",
              "unit": "tonnes",
              "description": "Biomass of each low trophic level functional group within the cell"
            }
          ],
          "scales": {
            "spatial": "Fixed regular grid; typical resolution 0.25°–1°; domain covers the study area (e.g. Benguela Current, Mediterranean, Bay of Biscay)",
            "temporal": "Static geometry; resource biomass updated at each time step"
          }
        },
        {
          "name": "Species",
          "entityType": "other",
          "stateVariables": [
            {
              "name": "speciesName",
              "type": "string",
              "description": "Common or scientific name of the focal species",
              "vocabularyTerm": "http://rs.tdwg.org/dwc/terms/scientificName"
            },
            {
              "name": "aphiaID",
              "type": "string",
              "description": "WoRMS AphiaID for taxonomic linkage",
              "vocabularyTerm": "http://rs.tdwg.org/dwc/terms/taxonID"
            },
            {
              "name": "Linf",
              "type": "real",
              "unit": "cm",
              "description": "Von Bertalanffy asymptotic length (or Gompertz plateau length)",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/OBSINDL01/"
            },
            {
              "name": "K",
              "type": "real",
              "unit": "year-1",
              "description": "Von Bertalanffy growth coefficient"
            },
            {
              "name": "t0",
              "type": "real",
              "unit": "years",
              "description": "Von Bertalanffy age at zero length (t-zero)"
            },
            {
              "name": "alphaGompertz",
              "type": "real",
              "unit": "dimensionless",
              "description": "Gompertz growth rate parameter (used when Gompertz selected)"
            },
            {
              "name": "betaGompertz",
              "type": "real",
              "unit": "year-1",
              "description": "Gompertz decline-rate parameter"
            },
            {
              "name": "lengthWeightAlpha",
              "type": "real",
              "unit": "g cm-b",
              "description": "Allometric length-weight coefficient a in W = a × L^b"
            },
            {
              "name": "lengthWeightBeta",
              "type": "real",
              "unit": "dimensionless",
              "description": "Allometric length-weight exponent b"
            },
            {
              "name": "lifespan",
              "type": "real",
              "unit": "years",
              "description": "Maximum age; schools reaching lifespan are removed"
            },
            {
              "name": "ageMat",
              "type": "real",
              "unit": "years",
              "description": "Age at first maturity; only mature schools contribute to reproduction"
            },
            {
              "name": "FRAC_fem",
              "type": "real",
              "unit": "dimensionless",
              "range": "[0, 1]",
              "description": "Fraction of females in the mature population"
            },
            {
              "name": "alpha",
              "type": "real",
              "unit": "eggs female-1 dt-1",
              "description": "Maximum egg production per female per time step (fecundity parameter)"
            },
            {
              "name": "predLengthRatioMin",
              "type": "real",
              "unit": "dimensionless",
              "description": "Minimum predator-to-prey length ratio (R_min) for predation to occur"
            },
            {
              "name": "predLengthRatioMax",
              "type": "real",
              "unit": "dimensionless",
              "description": "Maximum predator-to-prey length ratio (R_max) for predation to occur; prey must satisfy R_max < L_pred/L_prey ≤ R_min"
            },
            {
              "name": "naturalMortalityRate",
              "type": "real",
              "unit": "year-1",
              "description": "Background (non-predation, non-starvation) natural mortality rate"
            }
          ]
        },
        {
          "name": "Configuration",
          "entityType": "other",
          "stateVariables": [
            {
              "name": "nSpecies",
              "type": "integer",
              "description": "Number of focal species"
            },
            {
              "name": "nBackgroundSpecies",
              "type": "integer",
              "description": "Number of background (non-focal) species"
            },
            {
              "name": "nResourceGroups",
              "type": "integer",
              "description": "Number of low trophic level resource functional groups"
            },
            {
              "name": "nTimeStepsPerYear",
              "type": "integer",
              "description": "Time steps per year (e.g. 12 for monthly)"
            },
            {
              "name": "nYears",
              "type": "integer",
              "description": "Total simulation duration in years"
            },
            {
              "name": "nSchoolsPerSpecies",
              "type": "integer",
              "description": "Number of super-individual schools per species age class per time step"
            }
          ]
        }
      ],

      "processOverview": {
        "scheduling": "Sequential, fixed-order loop executed nTimeStepsPerYear times per simulated year. At each time step, all processes are executed globally (not per-agent) in the prescribed order. Within predation, schools compete for prey in randomised species order to avoid artefactual priority effects. Reproduction creates new schools at the end of the reproductive season. The time step dt = 1/nTimeStepsPerYear years.",
        "processes": [
          {
            "name": "1. Incoming flux",
            "executedBy": "Simulation engine",
            "description": "New recruits (age-0 schools) are introduced into the domain for each species according to the prescribed recruitment time series or internal spawning output."
          },
          {
            "name": "2. School initialisation",
            "executedBy": "Simulation engine",
            "description": "For each new school, assign initial length from the growth equation at age dt/2, compute weight from the allometric relationship W = a × L^b, and place the school in a randomly selected non-land cell."
          },
          {
            "name": "3. Low trophic level (LTL) update",
            "executedBy": "Resource objects",
            "description": "Read LTL biomass fields (phytoplankton, zooplankton classes, benthos) from the external biogeochemical forcing NetCDF file for the current time step and distribute them across grid cells."
          },
          {
            "name": "4. Spatial distribution",
            "executedBy": "School and BackgroundSchool",
            "description": "Each school is redistributed among grid cells according to species-specific spatial accessibility maps weighted by LTL biomass availability. Redistribution is stochastic (multinomial draw over accessible cells)."
          },
          {
            "name": "5a. Predation mortality",
            "executedBy": "School",
            "description": "For each predator school, identify available prey (focal schools, background schools, and LTL resources) sharing the same cell. Apply predator-prey size ratio criterion: prey is consumable if R_max < L_pred/L_prey ≤ R_min. Compute predation biomass proportional to prey availability and maximum ration. Update prey abundance and predator ingested biomass. Execute in randomised species order to avoid predator priority bias."
          },
          {
            "name": "5b. Starvation mortality",
            "executedBy": "School",
            "description": "After predation, compute starvation mortality rate M_starv from the ratio of ingested biomass to critical ration. Remove fish from school: N_starv = N × (1 - exp(-M_starv × dt))."
          },
          {
            "name": "5c. Natural mortality",
            "executedBy": "School",
            "description": "Apply background (non-predation, non-starvation) natural mortality rate: remove N_nat = N × (1 - exp(-M_nat × dt)) fish."
          },
          {
            "name": "5d. Fishing mortality",
            "executedBy": "Simulation engine / School",
            "description": "For each species with non-zero fishing, apply fishing mortality F from the fishing effort map or constant fishing rate: remove N_fish = N × (1 - exp(-F × dt)) fish of catchable size."
          },
          {
            "name": "5e. Migration / out-of-domain mortality",
            "executedBy": "School",
            "description": "Schools that leave the model domain during spatial redistribution incur an out-of-domain mortality representing emigration or boundary effects."
          },
          {
            "name": "6. Growth",
            "executedBy": "School",
            "description": "Update length of each school using Von Bertalanffy or Gompertz equation for the time step dt. Recompute weight from the updated length using the allometric relationship. Age is incremented by dt."
          },
          {
            "name": "7. Reproduction",
            "executedBy": "Species / Simulation engine",
            "description": "At reproductive season time steps, compute egg output for each mature school: N_eggs = FRAC_fem × alpha × seasonality × B_mat. Eggs hatch into age-0 schools (cohort) in the next recruiting time step."
          },
          {
            "name": "8. Update indicators",
            "executedBy": "Simulation engine",
            "description": "Compute and record aggregated outputs: total biomass per species, catches per species, mean length-at-age, trophic level distribution, diet matrix."
          },
          {
            "name": "9. Remove dead schools",
            "executedBy": "Simulation engine",
            "description": "Schools with zero abundance or that have exceeded maximum age (lifespan) are removed from the active school list."
          },
          {
            "name": "10. Merge schools",
            "executedBy": "Simulation engine",
            "description": "If the total number of active schools exceeds the configured maximum (nSchoolsPerSpecies × nSpecies × nAgeClasses), schools of the same species and age class in the same cell are merged into a single super-individual to maintain computational tractability."
          }
        ]
      },

      "designConcepts": {
        "basicPrinciples": "OSMOSE is founded on two key principles: (1) size-based predation — in marine ecosystems, predator-prey interactions are primarily determined by the relative sizes of predator and prey rather than species identity, following the 'fish eat fish' paradigm of Sheldon et al. (1972) and Kerr (1974); (2) the super-individual concept (Scheffer et al. 1995) — large populations of fish are represented as cohorts (schools) of identical individuals, reducing computational cost while preserving population-level statistics. Bioenergetics (growth, reproduction, starvation) follow standard empirical relationships (Von Bertalanffy or Gompertz growth, allometric weight-length scaling). The model does not incorporate individual-level cognitive processes.",

        "emergence": "The following key outputs emerge from local size-based predation interactions between super-individual schools: (1) multispecies trophic structure and food-web topology — which species prey on which, and at what life stages; (2) population biomass dynamics — boom-bust cycles, competitive exclusion, recovery trajectories; (3) community size spectrum (Sheldon spectrum); (4) diet composition matrices; (5) mean trophic levels; (6) catch dynamics under fishing. None of these are prescribed by species-level rules — they arise entirely from individual-scale size-ratio interactions at the school level.",

        "adaptation": "No explicit adaptive behaviour. Schools do not modify their foraging strategy, habitat use, or life-history parameters in response to experience or environment. Predation is purely opportunistic — any prey satisfying the size-ratio criterion and co-occurring in the same cell is consumed in proportion to availability. Spatial distribution is driven by fixed species-specific accessibility maps and LTL biomass density.",

        "objectives": "Agents have no explicit fitness objectives. Predation follows a passive encounter model: schools consume available prey to maximise ingested biomass up to their maximum ration, but do not optimise or choose among prey. Life-history parameters (growth, reproduction) are externally prescribed per species from empirical data, not evolved or optimised within the model.",

        "learning": "No learning. All behaviour rules and species parameters are fixed for the duration of the simulation. Parameter values are calibrated externally (multi-criterion optimisation against observed patterns) before simulation, not updated during model runs.",

        "prediction": "No predictive behaviour. Schools do not anticipate future resource availability, predation risk, or climate conditions. All processes are reactive (based on current time-step state) with no look-ahead.",

        "sensing": "Schools perceive the complete set of prey schools and LTL resource biomass present within their current grid cell. There is no distance-limited sensing or information decay — all schools in a cell are fully accessible to predators satisfying the size criterion. This is a simplifying assumption justified by the coarse grid resolution (0.25°–1°) and the aggregation of many real fish into each school.",

        "interaction": "Direct interactions: size-based predation — predator schools consume prey schools and LTL resource in the same cell when the predator-prey length ratio satisfies R_max < L_pred/L_prey ≤ R_min. Consumption reduces prey abundance. Indirect interactions: competition for shared food resources (LTL biomass and smaller schools) in the same cell; schools of the same species compete for a finite LTL budget. No communication, territory, or social interactions are represented.",

        "stochasticity": "Stochastic processes: (1) spatial redistribution — school placement at each time step is a multinomial random draw over accessible cells weighted by LTL biomass; (2) predation order — the sequence in which predator species are processed within a time step is randomised to avoid order-dependent artefacts; (3) initialisation — initial school placement and abundance are drawn from configured distributions. Growth, mortality rates, and reproduction parameters are deterministic given the current state. Multiple simulation replicates are recommended to quantify variability from stochastic spatial distribution.",

        "collectives": "Fish populations are represented as schools — super-individuals in the sense of Scheffer et al. (1995). Each school represents a cohort of identical fish (same species, age, length, weight). The number of schools per species per age class (nSchoolsPerSpecies) is a configuration parameter controlling the trade-off between resolution and computational cost. Schools can be merged when their number exceeds a maximum threshold. Schools do not self-organise or exhibit emergent collective behaviour — they are computational abstractions rather than behavioural units.",

        "observation": "At each time step the model records: (1) total biomass (tonnes) and abundance (#) per species; (2) nominal catch (tonnes) per species from fishing mortality; (3) mean length-at-age per species; (4) trophic level time series per species; (5) full diet composition matrix (fraction of each prey type in each predator's diet); (6) spatial biomass maps (tonnes per cell per species). Annual aggregates are used for comparison with survey indices and fisheries statistics. Monte Carlo averaging across multiple stochastic replicates is used to estimate mean and variance of all indicators."
      },

      "initialization": {
        "description": "OSMOSE supports three initialisation modes: (1) Seeding mode — schools are created for each species covering all age classes from age-0 to lifespan, with lengths computed from the growth equation and abundances set to achieve a user-supplied target biomass. Schools are distributed randomly across non-land cells. (2) NetCDF restart — the full school list (species, age, length, weight, abundance, cell) is read from a saved NetCDF state file, allowing warm-start continuation from a previous run. (3) Relative biomass mode — total initial biomass per species is specified as a fraction of carrying capacity; schools are seeded with abundances scaled accordingly. For all modes, a spin-up period (typically 50–100 years) is run before analysis to eliminate transient initialisation effects. Initial LTL biomass is set from the first time step of the biogeochemical forcing file.",
        "seed": "The random seed for stochastic spatial distribution is set explicitly per simulation run in the configuration file. Calibration and ensemble runs use a fixed set of seeds; final analyses report mean ± 95 % confidence interval across 20–50 stochastic replicates.",
        "links": [
          {
            "href": "https://osmose-model.org/documentation/configuration",
            "title": "OSMOSE configuration guide — initialization parameters",
            "type": "text/html"
          }
        ]
      },

      "inputData": [
        {
          "name": "Species configuration files",
          "description": "CSV or properties files defining all species-level parameters: Von Bertalanffy/Gompertz growth coefficients (Linf, K, t0), allometric length-weight parameters (a, b), lifespan, age at maturity, fecundity, natural mortality rate, predator-prey size ratio bounds (R_min, R_max), and fraction females (FRAC_fem).",
          "format": "text/csv",
          "vocabularyTerm": "http://rs.tdwg.org/dwc/terms/Taxon"
        },
        {
          "name": "Spatial accessibility maps",
          "description": "Grid maps (nCells × nSpecies) defining the relative probability of each species occupying each cell at each time step of the year. Derived from larval drift models, tagging data, or scientific survey distributions. One CSV file per species per season.",
          "format": "text/csv",
          "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/ALONZZ01/"
        },
        {
          "name": "Fishing effort / mortality maps",
          "description": "Spatiotemporal fishing mortality rate maps (nCells × nSpecies × nTimeSteps) derived from vessel monitoring system (VMS) data or effort statistics. Combined with species-specific catchability coefficients to yield effective fishing mortality F.",
          "format": "text/csv",
          "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/FSHBMS01/"
        },
        {
          "name": "Low trophic level (LTL) biogeochemical forcing",
          "description": "Time series of phytoplankton, microzooplankton, mesozooplankton, macrozooplankton, and benthos biomass density (mg C m-3 or mmol N m-3) on the OSMOSE grid, derived from a coupled physical-biogeochemical model (e.g. ROMS-NPZD for the Benguela, NEMO-ECO3M or PISCES for the Mediterranean). Regridded to the OSMOSE cell size.",
          "format": "application/x-netcdf",
          "temporalCoverage": "model spin-up plus analysis period (typically 1960–present)",
          "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/PHYTBM01/"
        },
        {
          "name": "Observed catches for calibration",
          "description": "Annual nominal catch time series (tonnes per species) from national/regional fisheries statistics (e.g. FAO, ICES) used as calibration targets in the multi-criterion optimisation. Provided as a multi-species CSV table.",
          "format": "text/csv",
          "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/FSHBMS01/"
        },
        {
          "name": "Survey biomass indices",
          "description": "Relative biomass indices from trawl surveys (e.g. IBTS, MEDITS, DEMERSAL surveys) used as calibration targets. Provided as CSV files with year, species, and standardised CPUE or biomass index.",
          "format": "text/csv",
          "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/SDBIOL02/"
        },
        {
          "name": "Diet composition observations",
          "description": "Fraction of each prey type in predator stomach contents from stomach-content analysis programmes. Used to validate the predation submodel. One CSV per predator species listing prey proportions by length class.",
          "format": "text/csv",
          "vocabularyTerm": "https://doi.org/10.1016/S0304-3800(03)00148-8"
        }
      ],

      "submodels": [
        {
          "name": "Growth — Von Bertalanffy",
          "description": "Standard Von Bertalanffy somatic growth. Length increments are computed analytically from the integral of the VBGF over one time step dt. Weight is recomputed from the allometric relationship after each length update.",
          "equations": "L(a + dt) = Linf × (1 - exp(-K × (a + dt - t0)))\nΔL = L(a + dt) - L(a)\nW = a_LW × L^b_LW\n\nParameters: Linf [cm] asymptotic length; K [year-1] growth coefficient; t0 [years] age at zero length; a_LW [g cm^-b] length-weight coefficient; b_LW [-] length-weight exponent.",
          "parameterization": "Linf, K, t0 fitted by least-squares regression to age-length keys from stock assessment working groups (ICES WGNSSK, WGMHSA) or published otolith-ageing studies. Length-weight parameters from FishBase or regional survey data. All values species-specific and region-specific.",
          "links": [
            {
              "href": "https://www.fishbase.org/",
              "rel": "related",
              "title": "FishBase — source for growth parameters"
            }
          ]
        },
        {
          "name": "Growth — Gompertz (alternative)",
          "description": "Gompertz growth model, used as an alternative to Von Bertalanffy for species where it provides a better fit (typically faster-growing short-lived species or early juvenile stages).",
          "equations": "L(a) = Linf × exp(-alpha_G × exp(-beta_G × a))\nΔL = L(a + dt) - L(a)\n\nParameters: Linf [cm] plateau length; alpha_G [-] dimensionless Gompertz rate; beta_G [year-1] Gompertz decline-rate parameter.",
          "parameterization": "alpha_G and beta_G fitted to age-length data where Gompertz AIC is lower than Von Bertalanffy AIC. Applied e.g. to early juvenile anchovy and sardine cohorts in Mediterranean applications."
        },
        {
          "name": "Predation mortality",
          "description": "Size-based opportunistic predation. A predator school consumes all accessible prey (schools and LTL resources) sharing its cell up to its maximum ingestion capacity. Prey accessibility is determined by a predator-prey length ratio criterion. Predation is processed in randomised species order.",
          "equations": "Predation criterion: R_max < (L_pred / L_prey) ≤ R_min\n  where R_min and R_max are species-specific maximum and minimum predator-prey length ratios.\n\nMaximum ration: Rmax_pred = criticalRatio × W_pred (W_pred individual weight of predator)\n\nActual ingestion from prey school p:\n  ΔB_p = min(N_pred × Rmax_pred, B_p_available) × (B_p / ΣB_accessible)\n  ΔN_p = ΔB_p / w_p  (prey abundance removed)\n\nPredator trophic level:\n  TL_pred = 1 + Σ(TL_prey_j × w_j) / Σw_j  (biomass-weighted average)",
          "parameterization": "R_min and R_max calibrated per species from observed diet composition data (stomach contents) and are typically in the range [2, 10] and [1, 5] respectively. criticalRatio (maximum ration as a fraction of body weight) is set to 0.57 dt in the default parameterisation, based on bioenergetics literature."
        },
        {
          "name": "Starvation mortality",
          "description": "Fish that ingest below a critical ration threshold incur starvation mortality. The starvation rate increases linearly as ingestion falls below the critical ration.",
          "equations": "Critical ration: Rcrit = xi × W_pred  (xi ≈ 0.57 × criticalRatio, default 0.57 × 0.57)\n\nStarvation mortality rate:\n  M_starv = max(0, starvMax × (1 - ingestedBiomass / (N × Rcrit)))\n  where starvMax is the maximum starvation mortality rate [dt-1]\n\nFish removed by starvation:\n  ΔN_starv = N × (1 - exp(-M_starv × dt))",
          "parameterization": "starvMax is a species-specific calibration parameter, typically 0.3–0.8 dt-1. xi is derived from the critical ration fraction of body weight from bioenergetics experiments."
        },
        {
          "name": "Reproduction",
          "description": "At each reproductive season time step, mature schools produce eggs. Eggs are aggregated into a cohort that becomes the new age-0 school cohort at the next time step.",
          "equations": "Egg production:\n  N_eggs_s = FRAC_fem_s × alpha_s × season_s(t) × B_mat_s\n  where:\n    FRAC_fem_s  = fraction of females in species s\n    alpha_s     = maximum fecundity [eggs female-1 dt-1]\n    season_s(t) = seasonal spawning coefficient ∈ [0,1] for time step t\n    B_mat_s     = total biomass of schools ≥ ageMat [tonnes]\n\nNew school abundance:\n  N_recruits = N_eggs_s × survivalEgg_s × dt",
          "parameterization": "alpha_s estimated from published fecundity-weight relationships (FishBase or stock assessment reports). FRAC_fem_s typically 0.5 for most teleosts. season_s(t) is a prescribed monthly profile from spawning ground surveys or ichthyoplankton sampling. survivalEgg_s is a combined egg+larval survival rate calibrated during multi-criterion optimisation."
        },
        {
          "name": "Spatial distribution",
          "description": "At each time step all schools are redistributed across the domain according to species-specific spatial accessibility maps. The distribution is stochastic, with cell selection probability proportional to the product of the accessibility map value and local LTL biomass density.",
          "equations": "Probability of school occupying cell c at time t:\n  P(c,t) = acc_s(c,t) × LTL(c,t) / Σ_c [acc_s(c,t) × LTL(c,t)]\n  where:\n    acc_s(c,t) = species-specific accessibility coefficient for cell c at time step t ∈ [0,1]\n    LTL(c,t)   = total low trophic level biomass in cell c at time t [tonnes]\n\nCell assignment drawn from Multinomial(1, P(·,t)) for each school independently.",
          "parameterization": "acc_s(c,t) maps derived from scientific surveys, larval drift model outputs, or expert knowledge. For each species 12 monthly maps (nCells values each) are required. Where LTL maps are unavailable, uniform LTL weighting can be used."
        },
        {
          "name": "Incoming flux",
          "description": "New age-0 recruits are introduced each time step according to a prescribed recruitment flux or spawning-stock-recruitment (SSR) relationship.",
          "equations": "Flux-based: N_recruits(t) = flux_s(t) [number or biomass read from input time series]\n\nSSR-based (Beverton-Holt):\n  R_s(t) = (alpha_BH × S_s(t)) / (beta_BH + S_s(t))\n  where S_s(t) = total spawning stock biomass of species s at time t-lag.",
          "parameterization": "For the flux mode, observed recruitment indices from ICES or DEPM surveys are prescribed. For SSR, alpha_BH and beta_BH are calibrated. Recruitment time lag (egg-to-recruit duration) is set from species-specific larval duration data."
        }
      ]
    }
  },

  "links": [
    {
      "href": "https://osmose-model.org/",
      "rel": "canonical",
      "type": "text/html",
      "title": "OSMOSE model website"
    },
    {
      "href": "https://doi.org/10.1016/j.ecolmodel.2009.07.031",
      "rel": "cite-as",
      "type": "text/html",
      "title": "Travers et al. 2009 — OSMOSE ODD paper (Ecological Modelling)"
    },
    {
      "href": "https://doi.org/10.1016/S0304-3800(03)00148-8",
      "rel": "related",
      "type": "text/html",
      "title": "Shannon et al. 2003 — Patterns for model calibration (Ecological Modelling)"
    },
    {
      "href": "https://github.com/osmose-model/osmose",
      "rel": "related",
      "type": "text/html",
      "title": "OSMOSE source code (GitHub)"
    },
    {
      "href": "https://osmose-model.org/documentation/odd",
      "rel": "related",
      "type": "application/pdf",
      "title": "OSMOSE ODD Protocol description document"
    },
    {
      "href": "https://doi.org/10.1371/journal.pcbi.1000356",
      "rel": "related",
      "type": "text/html",
      "title": "Grimm et al. 2005 — Pattern-Oriented Modeling (used in calibration)"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/odd-protocol/context.jsonld",
  "id": "https://osmose-model.org/",
  "type": "Feature",
  "geometry": null,
  "time": {
    "date": "2009-01-01"
  },
  "properties": {
    "type": "SoftwareApplication",
    "title": "OSMOSE \u2014 Object-oriented Simulator of Marine Ecosystems: ODD Protocol Description",
    "description": "OSMOSE (Object-oriented Simulator of Marine Ecosystems) is a multispecies, spatially-explicit, individual-based model for marine fish communities. It represents fish populations as super-individuals (schools) and models size-based predation, growth, reproduction, and mortality. The model is designed to investigate the effects of fishing and environmental forcing on ecosystem structure and functioning.",
    "created": "2009-01-01",
    "updated": "2020-01-01",
    "language": {
      "code": "en"
    },
    "externalIds": [
      {
        "scheme": "doi",
        "value": "10.1016/j.ecolmodel.2009.07.031"
      },
      {
        "scheme": "url",
        "value": "https://osmose-model.org/"
      },
      {
        "scheme": "github",
        "value": "https://github.com/osmose-model/osmose"
      }
    ],
    "contacts": [
      {
        "name": "Yunne-Jai Shin",
        "roles": [
          "author",
          "pointOfContact"
        ],
        "organization": "IRD (Institut de Recherche pour le D\u00e9veloppement), MARBEC"
      },
      {
        "name": "Morgane Travers-Trolet",
        "roles": [
          "author"
        ],
        "organization": "IFREMER"
      },
      {
        "name": "Philippe Cury",
        "roles": [
          "author"
        ],
        "organization": "IRD"
      },
      {
        "name": "Ricardo Oliveros-Ramos",
        "roles": [
          "author"
        ],
        "organization": "IRD / IMARPE"
      }
    ],
    "themes": [
      {
        "concepts": [
          {
            "id": "individual-based-model",
            "label": "Individual-Based Model"
          },
          {
            "id": "multispecies-model",
            "label": "Multispecies Model"
          },
          {
            "id": "marine-ecosystem",
            "label": "Marine Ecosystem"
          },
          {
            "id": "size-based-predation",
            "label": "Size-Based Predation"
          },
          {
            "id": "fish-community",
            "label": "Fish Community"
          },
          {
            "id": "end-to-end-model",
            "label": "End-to-End Ecosystem Model"
          }
        ],
        "scheme": "https://vocabularies.osmose-model.org/"
      },
      {
        "concepts": [
          {
            "id": "http://vocab.nerc.ac.uk/collection/P02/current/FISH/",
            "label": "Fish abundance"
          },
          {
            "id": "http://vocab.nerc.ac.uk/collection/P02/current/BIOL/",
            "label": "Biological variables"
          }
        ],
        "scheme": "http://vocab.nerc.ac.uk/collection/P02/current/"
      }
    ],
    "keywords": [
      "OSMOSE",
      "individual-based model",
      "multispecies",
      "marine fish",
      "size-based predation",
      "super-individual",
      "ecosystem model",
      "fishing",
      "low trophic level",
      "emergent behaviour"
    ],
    "license": "https://www.gnu.org/licenses/gpl-3.0.html",
    "formats": [
      {
        "mediaType": "application/java-archive",
        "title": "Java executable (JAR)"
      },
      {
        "mediaType": "text/csv",
        "title": "Configuration files"
      }
    ],
    "odd": {
      "purpose": "OSMOSE was developed to explore the emergent trophic structure of marine fish communities under size-based predation. Its primary purpose is to (1) investigate the multispecies effects of fishing on ecosystem functioning and community structure, (2) simulate the response of fish communities to environmental forcing (e.g. changes in low trophic level production from climate models), and (3) produce realistic predictions of catches, biomass, size spectra, and diet composition that can be compared against observed fisheries and survey data. The model uses a Pattern-Oriented Modeling (POM) approach: schools, catches, biomass time series, mean lengths-at-age, and diet compositions observed in the study area are used simultaneously as calibration targets.",
      "patterns": [
        {
          "name": "Multispecies catch time series",
          "description": "Observed nominal catches (tonnes) per species per year from fisheries statistics. Used to constrain total fishing mortality and species-level biomass in calibration.",
          "reference": "http://vocab.nerc.ac.uk/collection/P01/current/FSHBMS01/"
        },
        {
          "name": "Survey biomass indices",
          "description": "Relative biomass indices (B-hat) from scientific trawl surveys. Used to constrain interannual biomass dynamics per species.",
          "reference": "http://vocab.nerc.ac.uk/collection/P01/current/SDBIOL02/"
        },
        {
          "name": "Mean length at age",
          "description": "Mean length-at-age data from otolith/age-reading programmes used to validate growth submodel trajectories.",
          "reference": "http://vocab.nerc.ac.uk/collection/P01/current/OBSINDL01/"
        },
        {
          "name": "Diet composition",
          "description": "Proportion of each prey type in predator stomach contents from stomach-content analyses. Used to validate the size-based predation submodel.",
          "reference": "https://doi.org/10.1016/S0304-3800(03)00148-8"
        }
      ],
      "entities": [
        {
          "name": "School",
          "entityType": "agent",
          "stateVariables": [
            {
              "name": "species",
              "type": "integer",
              "unit": "dimensionless",
              "range": "[0, nSpecies-1]",
              "description": "Index identifying the focal species this school belongs to"
            },
            {
              "name": "age",
              "type": "real",
              "unit": "years",
              "range": "[0, lifespan]",
              "description": "Age of the school cohort in years",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/AGEBIOLX/"
            },
            {
              "name": "length",
              "type": "real",
              "unit": "cm",
              "range": "[0, Linf]",
              "description": "Mean fork or total length of individual fish within the school",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/OBSINDL01/"
            },
            {
              "name": "weight",
              "type": "real",
              "unit": "g",
              "range": "[0, Wmax]",
              "description": "Mean individual wet weight of fish within the school",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/OBSINDW01/"
            },
            {
              "name": "abundance",
              "type": "real",
              "unit": "#",
              "range": "non-negative",
              "description": "Number of individual fish represented by this super-individual school",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/OBSINDN01/"
            },
            {
              "name": "trophicLevel",
              "type": "real",
              "unit": "dimensionless",
              "range": "[1, 6]",
              "description": "Trophic level estimated dynamically from diet composition at each time step",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/TRPHINDX/"
            },
            {
              "name": "ingestedBiomass",
              "type": "real",
              "unit": "tonnes",
              "range": "non-negative",
              "description": "Total biomass ingested by the school in the current time step across all prey items"
            },
            {
              "name": "starvationMortalityRate",
              "type": "real",
              "unit": "dt-1",
              "range": "[0, 1]",
              "description": "Instantaneous mortality rate from starvation, computed from ratio of ingested biomass to maximum ration"
            },
            {
              "name": "cell",
              "type": "integer",
              "unit": "dimensionless",
              "range": "[0, nCells-1]",
              "description": "Index of the grid cell currently occupied by the school"
            },
            {
              "name": "dietMatrix",
              "type": "list",
              "unit": "tonnes",
              "description": "Vector of biomass consumed from each prey species/size class in the current time step"
            }
          ],
          "scales": {
            "spatial": "One cell per school per time step; cell size is configuration-dependent (typically 0.25\u00b0 \u00d7 0.25\u00b0 to 1\u00b0 \u00d7 1\u00b0)",
            "temporal": "Time step configurable (default 1 month = 1/12 year); lifespan 1\u201345 years depending on species"
          }
        },
        {
          "name": "BackgroundSchool",
          "entityType": "agent",
          "stateVariables": [
            {
              "name": "species",
              "type": "integer",
              "description": "Index of the background (non-focal) species"
            },
            {
              "name": "length",
              "type": "real",
              "unit": "cm",
              "description": "Mean length of individuals in the background school",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/OBSINDL01/"
            },
            {
              "name": "biomass",
              "type": "real",
              "unit": "tonnes",
              "description": "Total biomass of the background school",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/SDBIOL02/"
            },
            {
              "name": "cell",
              "type": "integer",
              "description": "Current grid cell of the background school"
            }
          ],
          "scales": {
            "spatial": "Same grid as focal schools",
            "temporal": "Updated at each time step from input time series"
          }
        },
        {
          "name": "Resource",
          "entityType": "environment",
          "stateVariables": [
            {
              "name": "biomass",
              "type": "real",
              "unit": "tonnes km-2",
              "range": "non-negative",
              "description": "Areal biomass density of low trophic level resource (phytoplankton, zooplankton, benthos) per grid cell",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/SDBIOL02/"
            },
            {
              "name": "resourceType",
              "type": "string",
              "description": "Functional type: phytoplankton | microzooplankton | mesozooplankton | macrozooplankton | benthos"
            },
            {
              "name": "cell",
              "type": "integer",
              "description": "Grid cell to which this resource unit belongs"
            }
          ],
          "scales": {
            "spatial": "One resource object per functional type per grid cell",
            "temporal": "Updated each time step from external biogeochemical model forcing (ROMS-NPZD or NEMO-ECO3M/PISCES)"
          }
        },
        {
          "name": "Cell",
          "entityType": "patch",
          "stateVariables": [
            {
              "name": "latitude",
              "type": "real",
              "unit": "degrees_north",
              "description": "Latitude of cell centre",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/ALATZZ01/"
            },
            {
              "name": "longitude",
              "type": "real",
              "unit": "degrees_east",
              "description": "Longitude of cell centre",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/ALONZZ01/"
            },
            {
              "name": "area",
              "type": "real",
              "unit": "km2",
              "description": "Planimetric area of the cell (used for biomass density computation)"
            },
            {
              "name": "land",
              "type": "boolean",
              "description": "True if cell is land (excluded from simulation)"
            },
            {
              "name": "schoolsPresent",
              "type": "list",
              "description": "List of School and BackgroundSchool agents currently located in this cell"
            },
            {
              "name": "resourceBiomass",
              "type": "list",
              "unit": "tonnes",
              "description": "Biomass of each low trophic level functional group within the cell"
            }
          ],
          "scales": {
            "spatial": "Fixed regular grid; typical resolution 0.25\u00b0\u20131\u00b0; domain covers the study area (e.g. Benguela Current, Mediterranean, Bay of Biscay)",
            "temporal": "Static geometry; resource biomass updated at each time step"
          }
        },
        {
          "name": "Species",
          "entityType": "other",
          "stateVariables": [
            {
              "name": "speciesName",
              "type": "string",
              "description": "Common or scientific name of the focal species",
              "vocabularyTerm": "http://rs.tdwg.org/dwc/terms/scientificName"
            },
            {
              "name": "aphiaID",
              "type": "string",
              "description": "WoRMS AphiaID for taxonomic linkage",
              "vocabularyTerm": "http://rs.tdwg.org/dwc/terms/taxonID"
            },
            {
              "name": "Linf",
              "type": "real",
              "unit": "cm",
              "description": "Von Bertalanffy asymptotic length (or Gompertz plateau length)",
              "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/OBSINDL01/"
            },
            {
              "name": "K",
              "type": "real",
              "unit": "year-1",
              "description": "Von Bertalanffy growth coefficient"
            },
            {
              "name": "t0",
              "type": "real",
              "unit": "years",
              "description": "Von Bertalanffy age at zero length (t-zero)"
            },
            {
              "name": "alphaGompertz",
              "type": "real",
              "unit": "dimensionless",
              "description": "Gompertz growth rate parameter (used when Gompertz selected)"
            },
            {
              "name": "betaGompertz",
              "type": "real",
              "unit": "year-1",
              "description": "Gompertz decline-rate parameter"
            },
            {
              "name": "lengthWeightAlpha",
              "type": "real",
              "unit": "g cm-b",
              "description": "Allometric length-weight coefficient a in W = a \u00d7 L^b"
            },
            {
              "name": "lengthWeightBeta",
              "type": "real",
              "unit": "dimensionless",
              "description": "Allometric length-weight exponent b"
            },
            {
              "name": "lifespan",
              "type": "real",
              "unit": "years",
              "description": "Maximum age; schools reaching lifespan are removed"
            },
            {
              "name": "ageMat",
              "type": "real",
              "unit": "years",
              "description": "Age at first maturity; only mature schools contribute to reproduction"
            },
            {
              "name": "FRAC_fem",
              "type": "real",
              "unit": "dimensionless",
              "range": "[0, 1]",
              "description": "Fraction of females in the mature population"
            },
            {
              "name": "alpha",
              "type": "real",
              "unit": "eggs female-1 dt-1",
              "description": "Maximum egg production per female per time step (fecundity parameter)"
            },
            {
              "name": "predLengthRatioMin",
              "type": "real",
              "unit": "dimensionless",
              "description": "Minimum predator-to-prey length ratio (R_min) for predation to occur"
            },
            {
              "name": "predLengthRatioMax",
              "type": "real",
              "unit": "dimensionless",
              "description": "Maximum predator-to-prey length ratio (R_max) for predation to occur; prey must satisfy R_max < L_pred/L_prey \u2264 R_min"
            },
            {
              "name": "naturalMortalityRate",
              "type": "real",
              "unit": "year-1",
              "description": "Background (non-predation, non-starvation) natural mortality rate"
            }
          ]
        },
        {
          "name": "Configuration",
          "entityType": "other",
          "stateVariables": [
            {
              "name": "nSpecies",
              "type": "integer",
              "description": "Number of focal species"
            },
            {
              "name": "nBackgroundSpecies",
              "type": "integer",
              "description": "Number of background (non-focal) species"
            },
            {
              "name": "nResourceGroups",
              "type": "integer",
              "description": "Number of low trophic level resource functional groups"
            },
            {
              "name": "nTimeStepsPerYear",
              "type": "integer",
              "description": "Time steps per year (e.g. 12 for monthly)"
            },
            {
              "name": "nYears",
              "type": "integer",
              "description": "Total simulation duration in years"
            },
            {
              "name": "nSchoolsPerSpecies",
              "type": "integer",
              "description": "Number of super-individual schools per species age class per time step"
            }
          ]
        }
      ],
      "processOverview": {
        "scheduling": "Sequential, fixed-order loop executed nTimeStepsPerYear times per simulated year. At each time step, all processes are executed globally (not per-agent) in the prescribed order. Within predation, schools compete for prey in randomised species order to avoid artefactual priority effects. Reproduction creates new schools at the end of the reproductive season. The time step dt = 1/nTimeStepsPerYear years.",
        "processes": [
          {
            "name": "1. Incoming flux",
            "executedBy": "Simulation engine",
            "description": "New recruits (age-0 schools) are introduced into the domain for each species according to the prescribed recruitment time series or internal spawning output."
          },
          {
            "name": "2. School initialisation",
            "executedBy": "Simulation engine",
            "description": "For each new school, assign initial length from the growth equation at age dt/2, compute weight from the allometric relationship W = a \u00d7 L^b, and place the school in a randomly selected non-land cell."
          },
          {
            "name": "3. Low trophic level (LTL) update",
            "executedBy": "Resource objects",
            "description": "Read LTL biomass fields (phytoplankton, zooplankton classes, benthos) from the external biogeochemical forcing NetCDF file for the current time step and distribute them across grid cells."
          },
          {
            "name": "4. Spatial distribution",
            "executedBy": "School and BackgroundSchool",
            "description": "Each school is redistributed among grid cells according to species-specific spatial accessibility maps weighted by LTL biomass availability. Redistribution is stochastic (multinomial draw over accessible cells)."
          },
          {
            "name": "5a. Predation mortality",
            "executedBy": "School",
            "description": "For each predator school, identify available prey (focal schools, background schools, and LTL resources) sharing the same cell. Apply predator-prey size ratio criterion: prey is consumable if R_max < L_pred/L_prey \u2264 R_min. Compute predation biomass proportional to prey availability and maximum ration. Update prey abundance and predator ingested biomass. Execute in randomised species order to avoid predator priority bias."
          },
          {
            "name": "5b. Starvation mortality",
            "executedBy": "School",
            "description": "After predation, compute starvation mortality rate M_starv from the ratio of ingested biomass to critical ration. Remove fish from school: N_starv = N \u00d7 (1 - exp(-M_starv \u00d7 dt))."
          },
          {
            "name": "5c. Natural mortality",
            "executedBy": "School",
            "description": "Apply background (non-predation, non-starvation) natural mortality rate: remove N_nat = N \u00d7 (1 - exp(-M_nat \u00d7 dt)) fish."
          },
          {
            "name": "5d. Fishing mortality",
            "executedBy": "Simulation engine / School",
            "description": "For each species with non-zero fishing, apply fishing mortality F from the fishing effort map or constant fishing rate: remove N_fish = N \u00d7 (1 - exp(-F \u00d7 dt)) fish of catchable size."
          },
          {
            "name": "5e. Migration / out-of-domain mortality",
            "executedBy": "School",
            "description": "Schools that leave the model domain during spatial redistribution incur an out-of-domain mortality representing emigration or boundary effects."
          },
          {
            "name": "6. Growth",
            "executedBy": "School",
            "description": "Update length of each school using Von Bertalanffy or Gompertz equation for the time step dt. Recompute weight from the updated length using the allometric relationship. Age is incremented by dt."
          },
          {
            "name": "7. Reproduction",
            "executedBy": "Species / Simulation engine",
            "description": "At reproductive season time steps, compute egg output for each mature school: N_eggs = FRAC_fem \u00d7 alpha \u00d7 seasonality \u00d7 B_mat. Eggs hatch into age-0 schools (cohort) in the next recruiting time step."
          },
          {
            "name": "8. Update indicators",
            "executedBy": "Simulation engine",
            "description": "Compute and record aggregated outputs: total biomass per species, catches per species, mean length-at-age, trophic level distribution, diet matrix."
          },
          {
            "name": "9. Remove dead schools",
            "executedBy": "Simulation engine",
            "description": "Schools with zero abundance or that have exceeded maximum age (lifespan) are removed from the active school list."
          },
          {
            "name": "10. Merge schools",
            "executedBy": "Simulation engine",
            "description": "If the total number of active schools exceeds the configured maximum (nSchoolsPerSpecies \u00d7 nSpecies \u00d7 nAgeClasses), schools of the same species and age class in the same cell are merged into a single super-individual to maintain computational tractability."
          }
        ]
      },
      "designConcepts": {
        "basicPrinciples": "OSMOSE is founded on two key principles: (1) size-based predation \u2014 in marine ecosystems, predator-prey interactions are primarily determined by the relative sizes of predator and prey rather than species identity, following the 'fish eat fish' paradigm of Sheldon et al. (1972) and Kerr (1974); (2) the super-individual concept (Scheffer et al. 1995) \u2014 large populations of fish are represented as cohorts (schools) of identical individuals, reducing computational cost while preserving population-level statistics. Bioenergetics (growth, reproduction, starvation) follow standard empirical relationships (Von Bertalanffy or Gompertz growth, allometric weight-length scaling). The model does not incorporate individual-level cognitive processes.",
        "emergence": "The following key outputs emerge from local size-based predation interactions between super-individual schools: (1) multispecies trophic structure and food-web topology \u2014 which species prey on which, and at what life stages; (2) population biomass dynamics \u2014 boom-bust cycles, competitive exclusion, recovery trajectories; (3) community size spectrum (Sheldon spectrum); (4) diet composition matrices; (5) mean trophic levels; (6) catch dynamics under fishing. None of these are prescribed by species-level rules \u2014 they arise entirely from individual-scale size-ratio interactions at the school level.",
        "adaptation": "No explicit adaptive behaviour. Schools do not modify their foraging strategy, habitat use, or life-history parameters in response to experience or environment. Predation is purely opportunistic \u2014 any prey satisfying the size-ratio criterion and co-occurring in the same cell is consumed in proportion to availability. Spatial distribution is driven by fixed species-specific accessibility maps and LTL biomass density.",
        "objectives": "Agents have no explicit fitness objectives. Predation follows a passive encounter model: schools consume available prey to maximise ingested biomass up to their maximum ration, but do not optimise or choose among prey. Life-history parameters (growth, reproduction) are externally prescribed per species from empirical data, not evolved or optimised within the model.",
        "learning": "No learning. All behaviour rules and species parameters are fixed for the duration of the simulation. Parameter values are calibrated externally (multi-criterion optimisation against observed patterns) before simulation, not updated during model runs.",
        "prediction": "No predictive behaviour. Schools do not anticipate future resource availability, predation risk, or climate conditions. All processes are reactive (based on current time-step state) with no look-ahead.",
        "sensing": "Schools perceive the complete set of prey schools and LTL resource biomass present within their current grid cell. There is no distance-limited sensing or information decay \u2014 all schools in a cell are fully accessible to predators satisfying the size criterion. This is a simplifying assumption justified by the coarse grid resolution (0.25\u00b0\u20131\u00b0) and the aggregation of many real fish into each school.",
        "interaction": "Direct interactions: size-based predation \u2014 predator schools consume prey schools and LTL resource in the same cell when the predator-prey length ratio satisfies R_max < L_pred/L_prey \u2264 R_min. Consumption reduces prey abundance. Indirect interactions: competition for shared food resources (LTL biomass and smaller schools) in the same cell; schools of the same species compete for a finite LTL budget. No communication, territory, or social interactions are represented.",
        "stochasticity": "Stochastic processes: (1) spatial redistribution \u2014 school placement at each time step is a multinomial random draw over accessible cells weighted by LTL biomass; (2) predation order \u2014 the sequence in which predator species are processed within a time step is randomised to avoid order-dependent artefacts; (3) initialisation \u2014 initial school placement and abundance are drawn from configured distributions. Growth, mortality rates, and reproduction parameters are deterministic given the current state. Multiple simulation replicates are recommended to quantify variability from stochastic spatial distribution.",
        "collectives": "Fish populations are represented as schools \u2014 super-individuals in the sense of Scheffer et al. (1995). Each school represents a cohort of identical fish (same species, age, length, weight). The number of schools per species per age class (nSchoolsPerSpecies) is a configuration parameter controlling the trade-off between resolution and computational cost. Schools can be merged when their number exceeds a maximum threshold. Schools do not self-organise or exhibit emergent collective behaviour \u2014 they are computational abstractions rather than behavioural units.",
        "observation": "At each time step the model records: (1) total biomass (tonnes) and abundance (#) per species; (2) nominal catch (tonnes) per species from fishing mortality; (3) mean length-at-age per species; (4) trophic level time series per species; (5) full diet composition matrix (fraction of each prey type in each predator's diet); (6) spatial biomass maps (tonnes per cell per species). Annual aggregates are used for comparison with survey indices and fisheries statistics. Monte Carlo averaging across multiple stochastic replicates is used to estimate mean and variance of all indicators."
      },
      "initialization": {
        "description": "OSMOSE supports three initialisation modes: (1) Seeding mode \u2014 schools are created for each species covering all age classes from age-0 to lifespan, with lengths computed from the growth equation and abundances set to achieve a user-supplied target biomass. Schools are distributed randomly across non-land cells. (2) NetCDF restart \u2014 the full school list (species, age, length, weight, abundance, cell) is read from a saved NetCDF state file, allowing warm-start continuation from a previous run. (3) Relative biomass mode \u2014 total initial biomass per species is specified as a fraction of carrying capacity; schools are seeded with abundances scaled accordingly. For all modes, a spin-up period (typically 50\u2013100 years) is run before analysis to eliminate transient initialisation effects. Initial LTL biomass is set from the first time step of the biogeochemical forcing file.",
        "seed": "The random seed for stochastic spatial distribution is set explicitly per simulation run in the configuration file. Calibration and ensemble runs use a fixed set of seeds; final analyses report mean \u00b1 95 % confidence interval across 20\u201350 stochastic replicates.",
        "links": [
          {
            "href": "https://osmose-model.org/documentation/configuration",
            "title": "OSMOSE configuration guide \u2014 initialization parameters",
            "type": "text/html"
          }
        ]
      },
      "inputData": [
        {
          "name": "Species configuration files",
          "description": "CSV or properties files defining all species-level parameters: Von Bertalanffy/Gompertz growth coefficients (Linf, K, t0), allometric length-weight parameters (a, b), lifespan, age at maturity, fecundity, natural mortality rate, predator-prey size ratio bounds (R_min, R_max), and fraction females (FRAC_fem).",
          "format": "text/csv",
          "vocabularyTerm": "http://rs.tdwg.org/dwc/terms/Taxon"
        },
        {
          "name": "Spatial accessibility maps",
          "description": "Grid maps (nCells \u00d7 nSpecies) defining the relative probability of each species occupying each cell at each time step of the year. Derived from larval drift models, tagging data, or scientific survey distributions. One CSV file per species per season.",
          "format": "text/csv",
          "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/ALONZZ01/"
        },
        {
          "name": "Fishing effort / mortality maps",
          "description": "Spatiotemporal fishing mortality rate maps (nCells \u00d7 nSpecies \u00d7 nTimeSteps) derived from vessel monitoring system (VMS) data or effort statistics. Combined with species-specific catchability coefficients to yield effective fishing mortality F.",
          "format": "text/csv",
          "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/FSHBMS01/"
        },
        {
          "name": "Low trophic level (LTL) biogeochemical forcing",
          "description": "Time series of phytoplankton, microzooplankton, mesozooplankton, macrozooplankton, and benthos biomass density (mg C m-3 or mmol N m-3) on the OSMOSE grid, derived from a coupled physical-biogeochemical model (e.g. ROMS-NPZD for the Benguela, NEMO-ECO3M or PISCES for the Mediterranean). Regridded to the OSMOSE cell size.",
          "format": "application/x-netcdf",
          "temporalCoverage": "model spin-up plus analysis period (typically 1960\u2013present)",
          "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/PHYTBM01/"
        },
        {
          "name": "Observed catches for calibration",
          "description": "Annual nominal catch time series (tonnes per species) from national/regional fisheries statistics (e.g. FAO, ICES) used as calibration targets in the multi-criterion optimisation. Provided as a multi-species CSV table.",
          "format": "text/csv",
          "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/FSHBMS01/"
        },
        {
          "name": "Survey biomass indices",
          "description": "Relative biomass indices from trawl surveys (e.g. IBTS, MEDITS, DEMERSAL surveys) used as calibration targets. Provided as CSV files with year, species, and standardised CPUE or biomass index.",
          "format": "text/csv",
          "vocabularyTerm": "http://vocab.nerc.ac.uk/collection/P01/current/SDBIOL02/"
        },
        {
          "name": "Diet composition observations",
          "description": "Fraction of each prey type in predator stomach contents from stomach-content analysis programmes. Used to validate the predation submodel. One CSV per predator species listing prey proportions by length class.",
          "format": "text/csv",
          "vocabularyTerm": "https://doi.org/10.1016/S0304-3800(03)00148-8"
        }
      ],
      "submodels": [
        {
          "name": "Growth \u2014 Von Bertalanffy",
          "description": "Standard Von Bertalanffy somatic growth. Length increments are computed analytically from the integral of the VBGF over one time step dt. Weight is recomputed from the allometric relationship after each length update.",
          "equations": "L(a + dt) = Linf \u00d7 (1 - exp(-K \u00d7 (a + dt - t0)))\n\u0394L = L(a + dt) - L(a)\nW = a_LW \u00d7 L^b_LW\n\nParameters: Linf [cm] asymptotic length; K [year-1] growth coefficient; t0 [years] age at zero length; a_LW [g cm^-b] length-weight coefficient; b_LW [-] length-weight exponent.",
          "parameterization": "Linf, K, t0 fitted by least-squares regression to age-length keys from stock assessment working groups (ICES WGNSSK, WGMHSA) or published otolith-ageing studies. Length-weight parameters from FishBase or regional survey data. All values species-specific and region-specific.",
          "links": [
            {
              "href": "https://www.fishbase.org/",
              "rel": "related",
              "title": "FishBase \u2014 source for growth parameters"
            }
          ]
        },
        {
          "name": "Growth \u2014 Gompertz (alternative)",
          "description": "Gompertz growth model, used as an alternative to Von Bertalanffy for species where it provides a better fit (typically faster-growing short-lived species or early juvenile stages).",
          "equations": "L(a) = Linf \u00d7 exp(-alpha_G \u00d7 exp(-beta_G \u00d7 a))\n\u0394L = L(a + dt) - L(a)\n\nParameters: Linf [cm] plateau length; alpha_G [-] dimensionless Gompertz rate; beta_G [year-1] Gompertz decline-rate parameter.",
          "parameterization": "alpha_G and beta_G fitted to age-length data where Gompertz AIC is lower than Von Bertalanffy AIC. Applied e.g. to early juvenile anchovy and sardine cohorts in Mediterranean applications."
        },
        {
          "name": "Predation mortality",
          "description": "Size-based opportunistic predation. A predator school consumes all accessible prey (schools and LTL resources) sharing its cell up to its maximum ingestion capacity. Prey accessibility is determined by a predator-prey length ratio criterion. Predation is processed in randomised species order.",
          "equations": "Predation criterion: R_max < (L_pred / L_prey) \u2264 R_min\n  where R_min and R_max are species-specific maximum and minimum predator-prey length ratios.\n\nMaximum ration: Rmax_pred = criticalRatio \u00d7 W_pred (W_pred individual weight of predator)\n\nActual ingestion from prey school p:\n  \u0394B_p = min(N_pred \u00d7 Rmax_pred, B_p_available) \u00d7 (B_p / \u03a3B_accessible)\n  \u0394N_p = \u0394B_p / w_p  (prey abundance removed)\n\nPredator trophic level:\n  TL_pred = 1 + \u03a3(TL_prey_j \u00d7 w_j) / \u03a3w_j  (biomass-weighted average)",
          "parameterization": "R_min and R_max calibrated per species from observed diet composition data (stomach contents) and are typically in the range [2, 10] and [1, 5] respectively. criticalRatio (maximum ration as a fraction of body weight) is set to 0.57 dt in the default parameterisation, based on bioenergetics literature."
        },
        {
          "name": "Starvation mortality",
          "description": "Fish that ingest below a critical ration threshold incur starvation mortality. The starvation rate increases linearly as ingestion falls below the critical ration.",
          "equations": "Critical ration: Rcrit = xi \u00d7 W_pred  (xi \u2248 0.57 \u00d7 criticalRatio, default 0.57 \u00d7 0.57)\n\nStarvation mortality rate:\n  M_starv = max(0, starvMax \u00d7 (1 - ingestedBiomass / (N \u00d7 Rcrit)))\n  where starvMax is the maximum starvation mortality rate [dt-1]\n\nFish removed by starvation:\n  \u0394N_starv = N \u00d7 (1 - exp(-M_starv \u00d7 dt))",
          "parameterization": "starvMax is a species-specific calibration parameter, typically 0.3\u20130.8 dt-1. xi is derived from the critical ration fraction of body weight from bioenergetics experiments."
        },
        {
          "name": "Reproduction",
          "description": "At each reproductive season time step, mature schools produce eggs. Eggs are aggregated into a cohort that becomes the new age-0 school cohort at the next time step.",
          "equations": "Egg production:\n  N_eggs_s = FRAC_fem_s \u00d7 alpha_s \u00d7 season_s(t) \u00d7 B_mat_s\n  where:\n    FRAC_fem_s  = fraction of females in species s\n    alpha_s     = maximum fecundity [eggs female-1 dt-1]\n    season_s(t) = seasonal spawning coefficient \u2208 [0,1] for time step t\n    B_mat_s     = total biomass of schools \u2265 ageMat [tonnes]\n\nNew school abundance:\n  N_recruits = N_eggs_s \u00d7 survivalEgg_s \u00d7 dt",
          "parameterization": "alpha_s estimated from published fecundity-weight relationships (FishBase or stock assessment reports). FRAC_fem_s typically 0.5 for most teleosts. season_s(t) is a prescribed monthly profile from spawning ground surveys or ichthyoplankton sampling. survivalEgg_s is a combined egg+larval survival rate calibrated during multi-criterion optimisation."
        },
        {
          "name": "Spatial distribution",
          "description": "At each time step all schools are redistributed across the domain according to species-specific spatial accessibility maps. The distribution is stochastic, with cell selection probability proportional to the product of the accessibility map value and local LTL biomass density.",
          "equations": "Probability of school occupying cell c at time t:\n  P(c,t) = acc_s(c,t) \u00d7 LTL(c,t) / \u03a3_c [acc_s(c,t) \u00d7 LTL(c,t)]\n  where:\n    acc_s(c,t) = species-specific accessibility coefficient for cell c at time step t \u2208 [0,1]\n    LTL(c,t)   = total low trophic level biomass in cell c at time t [tonnes]\n\nCell assignment drawn from Multinomial(1, P(\u00b7,t)) for each school independently.",
          "parameterization": "acc_s(c,t) maps derived from scientific surveys, larval drift model outputs, or expert knowledge. For each species 12 monthly maps (nCells values each) are required. Where LTL maps are unavailable, uniform LTL weighting can be used."
        },
        {
          "name": "Incoming flux",
          "description": "New age-0 recruits are introduced each time step according to a prescribed recruitment flux or spawning-stock-recruitment (SSR) relationship.",
          "equations": "Flux-based: N_recruits(t) = flux_s(t) [number or biomass read from input time series]\n\nSSR-based (Beverton-Holt):\n  R_s(t) = (alpha_BH \u00d7 S_s(t)) / (beta_BH + S_s(t))\n  where S_s(t) = total spawning stock biomass of species s at time t-lag.",
          "parameterization": "For the flux mode, observed recruitment indices from ICES or DEPM surveys are prescribed. For SSR, alpha_BH and beta_BH are calibrated. Recruitment time lag (egg-to-recruit duration) is set from species-specific larval duration data."
        }
      ]
    }
  },
  "links": [
    {
      "href": "https://osmose-model.org/",
      "rel": "canonical",
      "type": "text/html",
      "title": "OSMOSE model website"
    },
    {
      "href": "https://doi.org/10.1016/j.ecolmodel.2009.07.031",
      "rel": "cite-as",
      "type": "text/html",
      "title": "Travers et al. 2009 \u2014 OSMOSE ODD paper (Ecological Modelling)"
    },
    {
      "href": "https://doi.org/10.1016/S0304-3800(03)00148-8",
      "rel": "related",
      "type": "text/html",
      "title": "Shannon et al. 2003 \u2014 Patterns for model calibration (Ecological Modelling)"
    },
    {
      "href": "https://github.com/osmose-model/osmose",
      "rel": "related",
      "type": "text/html",
      "title": "OSMOSE source code (GitHub)"
    },
    {
      "href": "https://osmose-model.org/documentation/odd",
      "rel": "related",
      "type": "application/pdf",
      "title": "OSMOSE ODD Protocol description document"
    },
    {
      "href": "https://doi.org/10.1371/journal.pcbi.1000356",
      "rel": "related",
      "type": "text/html",
      "title": "Grimm et al. 2005 \u2014 Pattern-Oriented Modeling (used in calibration)"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix odd: <https://w3id.org/iliad/odd#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix schema: <https://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix thns: <https://w3id.org/ogc/stac/themes/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://osmose-model.org/> a <file:///github/workspace/SoftwareApplication>,
        geojson:Feature ;
    dcterms:created "2009-01-01" ;
    dcterms:description "OSMOSE (Object-oriented Simulator of Marine Ecosystems) is a multispecies, spatially-explicit, individual-based model for marine fish communities. It represents fish populations as super-individuals (schools) and models size-based predation, growth, reproduction, and mortality. The model is designed to investigate the effects of fishing and environmental forcing on ecosystem structure and functioning." ;
    dcterms:modified "2020-01-01" ;
    dcterms:temporal [ ] ;
    dcterms:title "OSMOSE — Object-oriented Simulator of Marine Ecosystems: ODD Protocol Description" ;
    rdfs:seeAlso [ rdfs:label "Travers et al. 2009 — OSMOSE ODD paper (Ecological Modelling)" ;
            dcterms:format "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/cite-as> ;
            oa:hasTarget <https://doi.org/10.1016/j.ecolmodel.2009.07.031> ],
        [ rdfs:label "Shannon et al. 2003 — Patterns for model calibration (Ecological Modelling)" ;
            dcterms:format "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://doi.org/10.1016/S0304-3800(03)00148-8> ],
        [ rdfs:label "OSMOSE model website" ;
            dcterms:format "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/canonical> ;
            oa:hasTarget <https://osmose-model.org/> ],
        [ rdfs:label "OSMOSE ODD Protocol description document" ;
            dcterms:format "application/pdf" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://osmose-model.org/documentation/odd> ],
        [ rdfs:label "OSMOSE source code (GitHub)" ;
            dcterms:format "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://github.com/osmose-model/osmose> ],
        [ rdfs:label "Grimm et al. 2005 — Pattern-Oriented Modeling (used in calibration)" ;
            dcterms:format "text/html" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://doi.org/10.1371/journal.pcbi.1000356> ] ;
    dcat:contactPoint [ ],
        [ ],
        [ ],
        [ ] ;
    dcat:keyword "OSMOSE",
        "ecosystem model",
        "emergent behaviour",
        "fishing",
        "individual-based model",
        "low trophic level",
        "marine fish",
        "multispecies",
        "size-based predation",
        "super-individual" ;
    dcat:license "https://www.gnu.org/licenses/gpl-3.0.html" ;
    odd: [ odd:designConcepts [ odd:adaptation "No explicit adaptive behaviour. Schools do not modify their foraging strategy, habitat use, or life-history parameters in response to experience or environment. Predation is purely opportunistic — any prey satisfying the size-ratio criterion and co-occurring in the same cell is consumed in proportion to availability. Spatial distribution is driven by fixed species-specific accessibility maps and LTL biomass density." ;
                    odd:basicPrinciples "OSMOSE is founded on two key principles: (1) size-based predation — in marine ecosystems, predator-prey interactions are primarily determined by the relative sizes of predator and prey rather than species identity, following the 'fish eat fish' paradigm of Sheldon et al. (1972) and Kerr (1974); (2) the super-individual concept (Scheffer et al. 1995) — large populations of fish are represented as cohorts (schools) of identical individuals, reducing computational cost while preserving population-level statistics. Bioenergetics (growth, reproduction, starvation) follow standard empirical relationships (Von Bertalanffy or Gompertz growth, allometric weight-length scaling). The model does not incorporate individual-level cognitive processes." ;
                    odd:collectives "Fish populations are represented as schools — super-individuals in the sense of Scheffer et al. (1995). Each school represents a cohort of identical fish (same species, age, length, weight). The number of schools per species per age class (nSchoolsPerSpecies) is a configuration parameter controlling the trade-off between resolution and computational cost. Schools can be merged when their number exceeds a maximum threshold. Schools do not self-organise or exhibit emergent collective behaviour — they are computational abstractions rather than behavioural units." ;
                    odd:emergence "The following key outputs emerge from local size-based predation interactions between super-individual schools: (1) multispecies trophic structure and food-web topology — which species prey on which, and at what life stages; (2) population biomass dynamics — boom-bust cycles, competitive exclusion, recovery trajectories; (3) community size spectrum (Sheldon spectrum); (4) diet composition matrices; (5) mean trophic levels; (6) catch dynamics under fishing. None of these are prescribed by species-level rules — they arise entirely from individual-scale size-ratio interactions at the school level." ;
                    odd:interaction "Direct interactions: size-based predation — predator schools consume prey schools and LTL resource in the same cell when the predator-prey length ratio satisfies R_max < L_pred/L_prey ≤ R_min. Consumption reduces prey abundance. Indirect interactions: competition for shared food resources (LTL biomass and smaller schools) in the same cell; schools of the same species compete for a finite LTL budget. No communication, territory, or social interactions are represented." ;
                    odd:learning "No learning. All behaviour rules and species parameters are fixed for the duration of the simulation. Parameter values are calibrated externally (multi-criterion optimisation against observed patterns) before simulation, not updated during model runs." ;
                    odd:objectives "Agents have no explicit fitness objectives. Predation follows a passive encounter model: schools consume available prey to maximise ingested biomass up to their maximum ration, but do not optimise or choose among prey. Life-history parameters (growth, reproduction) are externally prescribed per species from empirical data, not evolved or optimised within the model." ;
                    odd:observation "At each time step the model records: (1) total biomass (tonnes) and abundance (#) per species; (2) nominal catch (tonnes) per species from fishing mortality; (3) mean length-at-age per species; (4) trophic level time series per species; (5) full diet composition matrix (fraction of each prey type in each predator's diet); (6) spatial biomass maps (tonnes per cell per species). Annual aggregates are used for comparison with survey indices and fisheries statistics. Monte Carlo averaging across multiple stochastic replicates is used to estimate mean and variance of all indicators." ;
                    odd:prediction "No predictive behaviour. Schools do not anticipate future resource availability, predation risk, or climate conditions. All processes are reactive (based on current time-step state) with no look-ahead." ;
                    odd:sensing "Schools perceive the complete set of prey schools and LTL resource biomass present within their current grid cell. There is no distance-limited sensing or information decay — all schools in a cell are fully accessible to predators satisfying the size criterion. This is a simplifying assumption justified by the coarse grid resolution (0.25°–1°) and the aggregation of many real fish into each school." ;
                    odd:stochasticity "Stochastic processes: (1) spatial redistribution — school placement at each time step is a multinomial random draw over accessible cells weighted by LTL biomass; (2) predation order — the sequence in which predator species are processed within a time step is randomised to avoid order-dependent artefacts; (3) initialisation — initial school placement and abundance are drawn from configured distributions. Growth, mortality rates, and reproduction parameters are deterministic given the current state. Multiple simulation replicates are recommended to quantify variability from stochastic spatial distribution." ] ;
            odd:entities ( [ dcterms:title "School" ;
                        odd:entityType "agent" ;
                        odd:scales [ odd:spatialScale "One cell per school per time step; cell size is configuration-dependent (typically 0.25° × 0.25° to 1° × 1°)" ;
                                odd:temporalScale "Time step configurable (default 1 month = 1/12 year); lifespan 1–45 years depending on species" ] ;
                        odd:stateVariables ( [ dcterms:description "Index identifying the focal species this school belongs to" ;
                                    dcterms:title "species" ;
                                    qudt:unit "dimensionless" ;
                                    odd:range "[0, nSpecies-1]" ;
                                    odd:variableType "integer" ] [ dcterms:description "Age of the school cohort in years" ;
                                    dcterms:title "age" ;
                                    qudt:unit "years" ;
                                    skos:exactMatch <http://vocab.nerc.ac.uk/collection/P01/current/AGEBIOLX/> ;
                                    odd:range "[0, lifespan]" ;
                                    odd:variableType "real" ] [ dcterms:description "Mean fork or total length of individual fish within the school" ;
                                    dcterms:title "length" ;
                                    qudt:unit "cm" ;
                                    skos:exactMatch <http://vocab.nerc.ac.uk/collection/P01/current/OBSINDL01/> ;
                                    odd:range "[0, Linf]" ;
                                    odd:variableType "real" ] [ dcterms:description "Mean individual wet weight of fish within the school" ;
                                    dcterms:title "weight" ;
                                    qudt:unit "g" ;
                                    skos:exactMatch <http://vocab.nerc.ac.uk/collection/P01/current/OBSINDW01/> ;
                                    odd:range "[0, Wmax]" ;
                                    odd:variableType "real" ] [ dcterms:description "Number of individual fish represented by this super-individual school" ;
                                    dcterms:title "abundance" ;
                                    qudt:unit "#" ;
                                    skos:exactMatch <http://vocab.nerc.ac.uk/collection/P01/current/OBSINDN01/> ;
                                    odd:range "non-negative" ;
                                    odd:variableType "real" ] [ dcterms:description "Trophic level estimated dynamically from diet composition at each time step" ;
                                    dcterms:title "trophicLevel" ;
                                    qudt:unit "dimensionless" ;
                                    skos:exactMatch <http://vocab.nerc.ac.uk/collection/P01/current/TRPHINDX/> ;
                                    odd:range "[1, 6]" ;
                                    odd:variableType "real" ] [ dcterms:description "Total biomass ingested by the school in the current time step across all prey items" ;
                                    dcterms:title "ingestedBiomass" ;
                                    qudt:unit "tonnes" ;
                                    odd:range "non-negative" ;
                                    odd:variableType "real" ] [ dcterms:description "Instantaneous mortality rate from starvation, computed from ratio of ingested biomass to maximum ration" ;
                                    dcterms:title "starvationMortalityRate" ;
                                    qudt:unit "dt-1" ;
                                    odd:range "[0, 1]" ;
                                    odd:variableType "real" ] [ dcterms:description "Index of the grid cell currently occupied by the school" ;
                                    dcterms:title "cell" ;
                                    qudt:unit "dimensionless" ;
                                    odd:range "[0, nCells-1]" ;
                                    odd:variableType "integer" ] [ dcterms:description "Vector of biomass consumed from each prey species/size class in the current time step" ;
                                    dcterms:title "dietMatrix" ;
                                    qudt:unit "tonnes" ;
                                    odd:variableType "list" ] ) ] [ dcterms:title "BackgroundSchool" ;
                        odd:entityType "agent" ;
                        odd:scales [ odd:spatialScale "Same grid as focal schools" ;
                                odd:temporalScale "Updated at each time step from input time series" ] ;
                        odd:stateVariables ( [ dcterms:description "Index of the background (non-focal) species" ;
                                    dcterms:title "species" ;
                                    odd:variableType "integer" ] [ dcterms:description "Mean length of individuals in the background school" ;
                                    dcterms:title "length" ;
                                    qudt:unit "cm" ;
                                    skos:exactMatch <http://vocab.nerc.ac.uk/collection/P01/current/OBSINDL01/> ;
                                    odd:variableType "real" ] [ dcterms:description "Total biomass of the background school" ;
                                    dcterms:title "biomass" ;
                                    qudt:unit "tonnes" ;
                                    skos:exactMatch <http://vocab.nerc.ac.uk/collection/P01/current/SDBIOL02/> ;
                                    odd:variableType "real" ] [ dcterms:description "Current grid cell of the background school" ;
                                    dcterms:title "cell" ;
                                    odd:variableType "integer" ] ) ] [ dcterms:title "Resource" ;
                        odd:entityType "environment" ;
                        odd:scales [ odd:spatialScale "One resource object per functional type per grid cell" ;
                                odd:temporalScale "Updated each time step from external biogeochemical model forcing (ROMS-NPZD or NEMO-ECO3M/PISCES)" ] ;
                        odd:stateVariables ( [ dcterms:description "Areal biomass density of low trophic level resource (phytoplankton, zooplankton, benthos) per grid cell" ;
                                    dcterms:title "biomass" ;
                                    qudt:unit "tonnes km-2" ;
                                    skos:exactMatch <http://vocab.nerc.ac.uk/collection/P01/current/SDBIOL02/> ;
                                    odd:range "non-negative" ;
                                    odd:variableType "real" ] [ dcterms:description "Functional type: phytoplankton | microzooplankton | mesozooplankton | macrozooplankton | benthos" ;
                                    dcterms:title "resourceType" ;
                                    odd:variableType "string" ] [ dcterms:description "Grid cell to which this resource unit belongs" ;
                                    dcterms:title "cell" ;
                                    odd:variableType "integer" ] ) ] [ dcterms:title "Cell" ;
                        odd:entityType "patch" ;
                        odd:scales [ odd:spatialScale "Fixed regular grid; typical resolution 0.25°–1°; domain covers the study area (e.g. Benguela Current, Mediterranean, Bay of Biscay)" ;
                                odd:temporalScale "Static geometry; resource biomass updated at each time step" ] ;
                        odd:stateVariables ( [ dcterms:description "Latitude of cell centre" ;
                                    dcterms:title "latitude" ;
                                    qudt:unit "degrees_north" ;
                                    skos:exactMatch <http://vocab.nerc.ac.uk/collection/P01/current/ALATZZ01/> ;
                                    odd:variableType "real" ] [ dcterms:description "Longitude of cell centre" ;
                                    dcterms:title "longitude" ;
                                    qudt:unit "degrees_east" ;
                                    skos:exactMatch <http://vocab.nerc.ac.uk/collection/P01/current/ALONZZ01/> ;
                                    odd:variableType "real" ] [ dcterms:description "Planimetric area of the cell (used for biomass density computation)" ;
                                    dcterms:title "area" ;
                                    qudt:unit "km2" ;
                                    odd:variableType "real" ] [ dcterms:description "True if cell is land (excluded from simulation)" ;
                                    dcterms:title "land" ;
                                    odd:variableType "boolean" ] [ dcterms:description "List of School and BackgroundSchool agents currently located in this cell" ;
                                    dcterms:title "schoolsPresent" ;
                                    odd:variableType "list" ] [ dcterms:description "Biomass of each low trophic level functional group within the cell" ;
                                    dcterms:title "resourceBiomass" ;
                                    qudt:unit "tonnes" ;
                                    odd:variableType "list" ] ) ] [ dcterms:title "Species" ;
                        odd:entityType "other" ;
                        odd:stateVariables ( [ dcterms:description "Common or scientific name of the focal species" ;
                                    dcterms:title "speciesName" ;
                                    skos:exactMatch <http://rs.tdwg.org/dwc/terms/scientificName> ;
                                    odd:variableType "string" ] [ dcterms:description "WoRMS AphiaID for taxonomic linkage" ;
                                    dcterms:title "aphiaID" ;
                                    skos:exactMatch <http://rs.tdwg.org/dwc/terms/taxonID> ;
                                    odd:variableType "string" ] [ dcterms:description "Von Bertalanffy asymptotic length (or Gompertz plateau length)" ;
                                    dcterms:title "Linf" ;
                                    qudt:unit "cm" ;
                                    skos:exactMatch <http://vocab.nerc.ac.uk/collection/P01/current/OBSINDL01/> ;
                                    odd:variableType "real" ] [ dcterms:description "Von Bertalanffy growth coefficient" ;
                                    dcterms:title "K" ;
                                    qudt:unit "year-1" ;
                                    odd:variableType "real" ] [ dcterms:description "Von Bertalanffy age at zero length (t-zero)" ;
                                    dcterms:title "t0" ;
                                    qudt:unit "years" ;
                                    odd:variableType "real" ] [ dcterms:description "Gompertz growth rate parameter (used when Gompertz selected)" ;
                                    dcterms:title "alphaGompertz" ;
                                    qudt:unit "dimensionless" ;
                                    odd:variableType "real" ] [ dcterms:description "Gompertz decline-rate parameter" ;
                                    dcterms:title "betaGompertz" ;
                                    qudt:unit "year-1" ;
                                    odd:variableType "real" ] [ dcterms:description "Allometric length-weight coefficient a in W = a × L^b" ;
                                    dcterms:title "lengthWeightAlpha" ;
                                    qudt:unit "g cm-b" ;
                                    odd:variableType "real" ] [ dcterms:description "Allometric length-weight exponent b" ;
                                    dcterms:title "lengthWeightBeta" ;
                                    qudt:unit "dimensionless" ;
                                    odd:variableType "real" ] [ dcterms:description "Maximum age; schools reaching lifespan are removed" ;
                                    dcterms:title "lifespan" ;
                                    qudt:unit "years" ;
                                    odd:variableType "real" ] [ dcterms:description "Age at first maturity; only mature schools contribute to reproduction" ;
                                    dcterms:title "ageMat" ;
                                    qudt:unit "years" ;
                                    odd:variableType "real" ] [ dcterms:description "Fraction of females in the mature population" ;
                                    dcterms:title "FRAC_fem" ;
                                    qudt:unit "dimensionless" ;
                                    odd:range "[0, 1]" ;
                                    odd:variableType "real" ] [ dcterms:description "Maximum egg production per female per time step (fecundity parameter)" ;
                                    dcterms:title "alpha" ;
                                    qudt:unit "eggs female-1 dt-1" ;
                                    odd:variableType "real" ] [ dcterms:description "Minimum predator-to-prey length ratio (R_min) for predation to occur" ;
                                    dcterms:title "predLengthRatioMin" ;
                                    qudt:unit "dimensionless" ;
                                    odd:variableType "real" ] [ dcterms:description "Maximum predator-to-prey length ratio (R_max) for predation to occur; prey must satisfy R_max < L_pred/L_prey ≤ R_min" ;
                                    dcterms:title "predLengthRatioMax" ;
                                    qudt:unit "dimensionless" ;
                                    odd:variableType "real" ] [ dcterms:description "Background (non-predation, non-starvation) natural mortality rate" ;
                                    dcterms:title "naturalMortalityRate" ;
                                    qudt:unit "year-1" ;
                                    odd:variableType "real" ] ) ] [ dcterms:title "Configuration" ;
                        odd:entityType "other" ;
                        odd:stateVariables ( [ dcterms:description "Number of focal species" ;
                                    dcterms:title "nSpecies" ;
                                    odd:variableType "integer" ] [ dcterms:description "Number of background (non-focal) species" ;
                                    dcterms:title "nBackgroundSpecies" ;
                                    odd:variableType "integer" ] [ dcterms:description "Number of low trophic level resource functional groups" ;
                                    dcterms:title "nResourceGroups" ;
                                    odd:variableType "integer" ] [ dcterms:description "Time steps per year (e.g. 12 for monthly)" ;
                                    dcterms:title "nTimeStepsPerYear" ;
                                    odd:variableType "integer" ] [ dcterms:description "Total simulation duration in years" ;
                                    dcterms:title "nYears" ;
                                    odd:variableType "integer" ] [ dcterms:description "Number of super-individual schools per species age class per time step" ;
                                    dcterms:title "nSchoolsPerSpecies" ;
                                    odd:variableType "integer" ] ) ] ) ;
            odd:initialization [ dcterms:description "OSMOSE supports three initialisation modes: (1) Seeding mode — schools are created for each species covering all age classes from age-0 to lifespan, with lengths computed from the growth equation and abundances set to achieve a user-supplied target biomass. Schools are distributed randomly across non-land cells. (2) NetCDF restart — the full school list (species, age, length, weight, abundance, cell) is read from a saved NetCDF state file, allowing warm-start continuation from a previous run. (3) Relative biomass mode — total initial biomass per species is specified as a fraction of carrying capacity; schools are seeded with abundances scaled accordingly. For all modes, a spin-up period (typically 50–100 years) is run before analysis to eliminate transient initialisation effects. Initial LTL biomass is set from the first time step of the biogeochemical forcing file." ;
                    rdfs:seeAlso ( [ dcterms:title "OSMOSE configuration guide — initialization parameters" ;
                                schema:url <https://osmose-model.org/documentation/configuration> ;
                                odd:variableType "text/html" ] ) ;
                    odd:randomSeed "The random seed for stochastic spatial distribution is set explicitly per simulation run in the configuration file. Calibration and ensemble runs use a fixed set of seeds; final analyses report mean ± 95 % confidence interval across 20–50 stochastic replicates." ] ;
            odd:inputData ( [ dcterms:description "CSV or properties files defining all species-level parameters: Von Bertalanffy/Gompertz growth coefficients (Linf, K, t0), allometric length-weight parameters (a, b), lifespan, age at maturity, fecundity, natural mortality rate, predator-prey size ratio bounds (R_min, R_max), and fraction females (FRAC_fem)." ;
                        dcterms:format "text/csv" ;
                        dcterms:title "Species configuration files" ;
                        skos:exactMatch <http://rs.tdwg.org/dwc/terms/Taxon> ] [ dcterms:description "Grid maps (nCells × nSpecies) defining the relative probability of each species occupying each cell at each time step of the year. Derived from larval drift models, tagging data, or scientific survey distributions. One CSV file per species per season." ;
                        dcterms:format "text/csv" ;
                        dcterms:title "Spatial accessibility maps" ;
                        skos:exactMatch <http://vocab.nerc.ac.uk/collection/P01/current/ALONZZ01/> ] [ dcterms:description "Spatiotemporal fishing mortality rate maps (nCells × nSpecies × nTimeSteps) derived from vessel monitoring system (VMS) data or effort statistics. Combined with species-specific catchability coefficients to yield effective fishing mortality F." ;
                        dcterms:format "text/csv" ;
                        dcterms:title "Fishing effort / mortality maps" ;
                        skos:exactMatch <http://vocab.nerc.ac.uk/collection/P01/current/FSHBMS01/> ] [ dcterms:description "Time series of phytoplankton, microzooplankton, mesozooplankton, macrozooplankton, and benthos biomass density (mg C m-3 or mmol N m-3) on the OSMOSE grid, derived from a coupled physical-biogeochemical model (e.g. ROMS-NPZD for the Benguela, NEMO-ECO3M or PISCES for the Mediterranean). Regridded to the OSMOSE cell size." ;
                        dcterms:format "application/x-netcdf" ;
                        dcterms:temporal "model spin-up plus analysis period (typically 1960–present)" ;
                        dcterms:title "Low trophic level (LTL) biogeochemical forcing" ;
                        skos:exactMatch <http://vocab.nerc.ac.uk/collection/P01/current/PHYTBM01/> ] [ dcterms:description "Annual nominal catch time series (tonnes per species) from national/regional fisheries statistics (e.g. FAO, ICES) used as calibration targets in the multi-criterion optimisation. Provided as a multi-species CSV table." ;
                        dcterms:format "text/csv" ;
                        dcterms:title "Observed catches for calibration" ;
                        skos:exactMatch <http://vocab.nerc.ac.uk/collection/P01/current/FSHBMS01/> ] [ dcterms:description "Relative biomass indices from trawl surveys (e.g. IBTS, MEDITS, DEMERSAL surveys) used as calibration targets. Provided as CSV files with year, species, and standardised CPUE or biomass index." ;
                        dcterms:format "text/csv" ;
                        dcterms:title "Survey biomass indices" ;
                        skos:exactMatch <http://vocab.nerc.ac.uk/collection/P01/current/SDBIOL02/> ] [ dcterms:description "Fraction of each prey type in predator stomach contents from stomach-content analysis programmes. Used to validate the predation submodel. One CSV per predator species listing prey proportions by length class." ;
                        dcterms:format "text/csv" ;
                        dcterms:title "Diet composition observations" ;
                        skos:exactMatch <https://doi.org/10.1016/S0304-3800(03)00148-8> ] ) ;
            odd:patterns ( [ dcterms:description "Observed nominal catches (tonnes) per species per year from fisheries statistics. Used to constrain total fishing mortality and species-level biomass in calibration." ;
                        dcterms:references <http://vocab.nerc.ac.uk/collection/P01/current/FSHBMS01/> ;
                        dcterms:title "Multispecies catch time series" ] [ dcterms:description "Relative biomass indices (B-hat) from scientific trawl surveys. Used to constrain interannual biomass dynamics per species." ;
                        dcterms:references <http://vocab.nerc.ac.uk/collection/P01/current/SDBIOL02/> ;
                        dcterms:title "Survey biomass indices" ] [ dcterms:description "Mean length-at-age data from otolith/age-reading programmes used to validate growth submodel trajectories." ;
                        dcterms:references <http://vocab.nerc.ac.uk/collection/P01/current/OBSINDL01/> ;
                        dcterms:title "Mean length at age" ] [ dcterms:description "Proportion of each prey type in predator stomach contents from stomach-content analyses. Used to validate the size-based predation submodel." ;
                        dcterms:references <https://doi.org/10.1016/S0304-3800(03)00148-8> ;
                        dcterms:title "Diet composition" ] ) ;
            odd:processOverview [ odd:processes ( [ dcterms:description "New recruits (age-0 schools) are introduced into the domain for each species according to the prescribed recruitment time series or internal spawning output." ;
                                dcterms:title "1. Incoming flux" ;
                                odd:executedBy "Simulation engine" ] [ dcterms:description "For each new school, assign initial length from the growth equation at age dt/2, compute weight from the allometric relationship W = a × L^b, and place the school in a randomly selected non-land cell." ;
                                dcterms:title "2. School initialisation" ;
                                odd:executedBy "Simulation engine" ] [ dcterms:description "Read LTL biomass fields (phytoplankton, zooplankton classes, benthos) from the external biogeochemical forcing NetCDF file for the current time step and distribute them across grid cells." ;
                                dcterms:title "3. Low trophic level (LTL) update" ;
                                odd:executedBy "Resource objects" ] [ dcterms:description "Each school is redistributed among grid cells according to species-specific spatial accessibility maps weighted by LTL biomass availability. Redistribution is stochastic (multinomial draw over accessible cells)." ;
                                dcterms:title "4. Spatial distribution" ;
                                odd:executedBy "School and BackgroundSchool" ] [ dcterms:description "For each predator school, identify available prey (focal schools, background schools, and LTL resources) sharing the same cell. Apply predator-prey size ratio criterion: prey is consumable if R_max < L_pred/L_prey ≤ R_min. Compute predation biomass proportional to prey availability and maximum ration. Update prey abundance and predator ingested biomass. Execute in randomised species order to avoid predator priority bias." ;
                                dcterms:title "5a. Predation mortality" ;
                                odd:executedBy "School" ] [ dcterms:description "After predation, compute starvation mortality rate M_starv from the ratio of ingested biomass to critical ration. Remove fish from school: N_starv = N × (1 - exp(-M_starv × dt))." ;
                                dcterms:title "5b. Starvation mortality" ;
                                odd:executedBy "School" ] [ dcterms:description "Apply background (non-predation, non-starvation) natural mortality rate: remove N_nat = N × (1 - exp(-M_nat × dt)) fish." ;
                                dcterms:title "5c. Natural mortality" ;
                                odd:executedBy "School" ] [ dcterms:description "For each species with non-zero fishing, apply fishing mortality F from the fishing effort map or constant fishing rate: remove N_fish = N × (1 - exp(-F × dt)) fish of catchable size." ;
                                dcterms:title "5d. Fishing mortality" ;
                                odd:executedBy "Simulation engine / School" ] [ dcterms:description "Schools that leave the model domain during spatial redistribution incur an out-of-domain mortality representing emigration or boundary effects." ;
                                dcterms:title "5e. Migration / out-of-domain mortality" ;
                                odd:executedBy "School" ] [ dcterms:description "Update length of each school using Von Bertalanffy or Gompertz equation for the time step dt. Recompute weight from the updated length using the allometric relationship. Age is incremented by dt." ;
                                dcterms:title "6. Growth" ;
                                odd:executedBy "School" ] [ dcterms:description "At reproductive season time steps, compute egg output for each mature school: N_eggs = FRAC_fem × alpha × seasonality × B_mat. Eggs hatch into age-0 schools (cohort) in the next recruiting time step." ;
                                dcterms:title "7. Reproduction" ;
                                odd:executedBy "Species / Simulation engine" ] [ dcterms:description "Compute and record aggregated outputs: total biomass per species, catches per species, mean length-at-age, trophic level distribution, diet matrix." ;
                                dcterms:title "8. Update indicators" ;
                                odd:executedBy "Simulation engine" ] [ dcterms:description "Schools with zero abundance or that have exceeded maximum age (lifespan) are removed from the active school list." ;
                                dcterms:title "9. Remove dead schools" ;
                                odd:executedBy "Simulation engine" ] [ dcterms:description "If the total number of active schools exceeds the configured maximum (nSchoolsPerSpecies × nSpecies × nAgeClasses), schools of the same species and age class in the same cell are merged into a single super-individual to maintain computational tractability." ;
                                dcterms:title "10. Merge schools" ;
                                odd:executedBy "Simulation engine" ] ) ;
                    odd:scheduling "Sequential, fixed-order loop executed nTimeStepsPerYear times per simulated year. At each time step, all processes are executed globally (not per-agent) in the prescribed order. Within predation, schools compete for prey in randomised species order to avoid artefactual priority effects. Reproduction creates new schools at the end of the reproductive season. The time step dt = 1/nTimeStepsPerYear years." ] ;
            odd:purpose "OSMOSE was developed to explore the emergent trophic structure of marine fish communities under size-based predation. Its primary purpose is to (1) investigate the multispecies effects of fishing on ecosystem functioning and community structure, (2) simulate the response of fish communities to environmental forcing (e.g. changes in low trophic level production from climate models), and (3) produce realistic predictions of catches, biomass, size spectra, and diet composition that can be compared against observed fisheries and survey data. The model uses a Pattern-Oriented Modeling (POM) approach: schools, catches, biomass time series, mean lengths-at-age, and diet compositions observed in the study area are used simultaneously as calibration targets." ;
            odd:submodels ( [ dcterms:description "Standard Von Bertalanffy somatic growth. Length increments are computed analytically from the integral of the VBGF over one time step dt. Weight is recomputed from the allometric relationship after each length update." ;
                        dcterms:title "Growth — Von Bertalanffy" ;
                        rdfs:seeAlso ( [ dcterms:title "FishBase — source for growth parameters" ;
                                    schema:url <https://www.fishbase.org/> ;
                                    odd:linkRel "related" ] ) ;
                        odd:equations """L(a + dt) = Linf × (1 - exp(-K × (a + dt - t0)))
ΔL = L(a + dt) - L(a)
W = a_LW × L^b_LW

Parameters: Linf [cm] asymptotic length; K [year-1] growth coefficient; t0 [years] age at zero length; a_LW [g cm^-b] length-weight coefficient; b_LW [-] length-weight exponent.""" ;
                        odd:parameterization "Linf, K, t0 fitted by least-squares regression to age-length keys from stock assessment working groups (ICES WGNSSK, WGMHSA) or published otolith-ageing studies. Length-weight parameters from FishBase or regional survey data. All values species-specific and region-specific." ] [ dcterms:description "Gompertz growth model, used as an alternative to Von Bertalanffy for species where it provides a better fit (typically faster-growing short-lived species or early juvenile stages)." ;
                        dcterms:title "Growth — Gompertz (alternative)" ;
                        odd:equations """L(a) = Linf × exp(-alpha_G × exp(-beta_G × a))
ΔL = L(a + dt) - L(a)

Parameters: Linf [cm] plateau length; alpha_G [-] dimensionless Gompertz rate; beta_G [year-1] Gompertz decline-rate parameter.""" ;
                        odd:parameterization "alpha_G and beta_G fitted to age-length data where Gompertz AIC is lower than Von Bertalanffy AIC. Applied e.g. to early juvenile anchovy and sardine cohorts in Mediterranean applications." ] [ dcterms:description "Size-based opportunistic predation. A predator school consumes all accessible prey (schools and LTL resources) sharing its cell up to its maximum ingestion capacity. Prey accessibility is determined by a predator-prey length ratio criterion. Predation is processed in randomised species order." ;
                        dcterms:title "Predation mortality" ;
                        odd:equations """Predation criterion: R_max < (L_pred / L_prey) ≤ R_min
  where R_min and R_max are species-specific maximum and minimum predator-prey length ratios.

Maximum ration: Rmax_pred = criticalRatio × W_pred (W_pred individual weight of predator)

Actual ingestion from prey school p:
  ΔB_p = min(N_pred × Rmax_pred, B_p_available) × (B_p / ΣB_accessible)
  ΔN_p = ΔB_p / w_p  (prey abundance removed)

Predator trophic level:
  TL_pred = 1 + Σ(TL_prey_j × w_j) / Σw_j  (biomass-weighted average)""" ;
                        odd:parameterization "R_min and R_max calibrated per species from observed diet composition data (stomach contents) and are typically in the range [2, 10] and [1, 5] respectively. criticalRatio (maximum ration as a fraction of body weight) is set to 0.57 dt in the default parameterisation, based on bioenergetics literature." ] [ dcterms:description "Fish that ingest below a critical ration threshold incur starvation mortality. The starvation rate increases linearly as ingestion falls below the critical ration." ;
                        dcterms:title "Starvation mortality" ;
                        odd:equations """Critical ration: Rcrit = xi × W_pred  (xi ≈ 0.57 × criticalRatio, default 0.57 × 0.57)

Starvation mortality rate:
  M_starv = max(0, starvMax × (1 - ingestedBiomass / (N × Rcrit)))
  where starvMax is the maximum starvation mortality rate [dt-1]

Fish removed by starvation:
  ΔN_starv = N × (1 - exp(-M_starv × dt))""" ;
                        odd:parameterization "starvMax is a species-specific calibration parameter, typically 0.3–0.8 dt-1. xi is derived from the critical ration fraction of body weight from bioenergetics experiments." ] [ dcterms:description "At each reproductive season time step, mature schools produce eggs. Eggs are aggregated into a cohort that becomes the new age-0 school cohort at the next time step." ;
                        dcterms:title "Reproduction" ;
                        odd:equations """Egg production:
  N_eggs_s = FRAC_fem_s × alpha_s × season_s(t) × B_mat_s
  where:
    FRAC_fem_s  = fraction of females in species s
    alpha_s     = maximum fecundity [eggs female-1 dt-1]
    season_s(t) = seasonal spawning coefficient ∈ [0,1] for time step t
    B_mat_s     = total biomass of schools ≥ ageMat [tonnes]

New school abundance:
  N_recruits = N_eggs_s × survivalEgg_s × dt""" ;
                        odd:parameterization "alpha_s estimated from published fecundity-weight relationships (FishBase or stock assessment reports). FRAC_fem_s typically 0.5 for most teleosts. season_s(t) is a prescribed monthly profile from spawning ground surveys or ichthyoplankton sampling. survivalEgg_s is a combined egg+larval survival rate calibrated during multi-criterion optimisation." ] [ dcterms:description "At each time step all schools are redistributed across the domain according to species-specific spatial accessibility maps. The distribution is stochastic, with cell selection probability proportional to the product of the accessibility map value and local LTL biomass density." ;
                        dcterms:title "Spatial distribution" ;
                        odd:equations """Probability of school occupying cell c at time t:
  P(c,t) = acc_s(c,t) × LTL(c,t) / Σ_c [acc_s(c,t) × LTL(c,t)]
  where:
    acc_s(c,t) = species-specific accessibility coefficient for cell c at time step t ∈ [0,1]
    LTL(c,t)   = total low trophic level biomass in cell c at time t [tonnes]

Cell assignment drawn from Multinomial(1, P(·,t)) for each school independently.""" ;
                        odd:parameterization "acc_s(c,t) maps derived from scientific surveys, larval drift model outputs, or expert knowledge. For each species 12 monthly maps (nCells values each) are required. Where LTL maps are unavailable, uniform LTL weighting can be used." ] [ dcterms:description "New age-0 recruits are introduced each time step according to a prescribed recruitment flux or spawning-stock-recruitment (SSR) relationship." ;
                        dcterms:title "Incoming flux" ;
                        odd:equations """Flux-based: N_recruits(t) = flux_s(t) [number or biomass read from input time series]

SSR-based (Beverton-Holt):
  R_s(t) = (alpha_BH × S_s(t)) / (beta_BH + S_s(t))
  where S_s(t) = total spawning stock biomass of species s at time t-lag.""" ;
                        odd:parameterization "For the flux mode, observed recruitment indices from ICES or DEPM surveys are prescribed. For SSR, alpha_BH and beta_BH are calibrated. Recruitment time lag (egg-to-recruit duration) is set from species-specific larval duration data." ] ) ] ;
    rec:format [ dcterms:title "Java executable (JAR)" ;
            rec:mediaType "application/java-archive" ],
        [ dcterms:title "Configuration files" ;
            rec:mediaType "text/csv" ] ;
    rec:language [ rec:languageCode "en" ] ;
    rec:scopedIdentifier [ rec:id "https://osmose-model.org/" ;
            rec:scheme "url" ],
        [ rec:id "10.1016/j.ecolmodel.2009.07.031" ;
            rec:scheme "doi" ],
        [ rec:id "https://github.com/osmose-model/osmose" ;
            rec:scheme "github" ] ;
    rec:themes [ thns:concepts [ thns:id "http://vocab.nerc.ac.uk/collection/P02/current/FISH/"^^xsd:string ],
                [ thns:id "http://vocab.nerc.ac.uk/collection/P02/current/BIOL/"^^xsd:string ] ;
            thns:scheme "http://vocab.nerc.ac.uk/collection/P02/current/" ],
        [ thns:concepts [ thns:id "individual-based-model"^^xsd:string ],
                [ thns:id "end-to-end-model"^^xsd:string ],
                [ thns:id "marine-ecosystem"^^xsd:string ],
                [ thns:id "multispecies-model"^^xsd:string ],
                [ thns:id "size-based-predation"^^xsd:string ],
                [ thns:id "fish-community"^^xsd:string ] ;
            thns:scheme "https://vocabularies.osmose-model.org/" ] .


```


### Utsira reef-biomass demonstrator — one-submodel ODD with linked equation record
#### json
```json
{
  "id": "https://example.org/norwegian-ses/odd/utsira-reef-biomass-demonstrator-v1",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [4.40, 59.20],
      [5.10, 59.20],
      [5.10, 59.55],
      [4.40, 59.55],
      [4.40, 59.20]
    ]]
  },
  "time": {
    "date": "2026-05-13"
  },
  "properties": {
    "type": "SoftwareSourceCode",
    "title": "Utsira reef-biomass demonstrator — one-submodel ODD",
    "description": "Minimal ODD-Protocol record demonstrating how a single submodel can reference an exemplar equation declared in the seadots `equation-property-relationship` bblock. The submodel `Reef-associated biomass` mirrors the equation B_{reef} = sum_i (A_{sub} . D_{pre,i} . AF_i . C_t) and links out to the canonical `reef-biomass-equation.json` instance for the full symbol table, bindings, and provenance.",
    "created": "2026-05-13",
    "updated": "2026-05-13",
    "language": { "code": "en" },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "contacts": [
      {
        "name": "Utsira biomass upscaler v1",
        "roles": ["author"],
        "organization": "SINTEF Ocean (SeaDOTs)"
      }
    ],
    "themes": [
      {
        "concepts": [
          { "id": "reef-effect",        "label": "Floating-wind reef effect" },
          { "id": "benthic-biomass",    "label": "Benthic biomass" },
          { "id": "impact-assessment",  "label": "Impact assessment" }
        ],
        "scheme": "https://id3.seadots.eu/themes"
      }
    ],
    "keywords": [
      "ODD", "demonstrator", "Utsira", "floating wind",
      "reef biomass", "equation-property-relationship", "SeaDOTs"
    ],
    "formats": [
      { "mediaType": "application/json" }
    ],

    "odd": {
      "purpose": "Estimate the reef-associated biomass that develops on submerged floating-wind infrastructure at Utsira Nord under the Norwegian SES scenario. Demonstrator: one submodel only, with the full equation, symbol table and per-taxon bindings carried by the linked `equation-property-relationship` record.",

      "entities": [
        {
          "name": "TaxonGroup",
          "entityType": "agent",
          "stateVariables": [
            {
              "name": "scientificName",
              "type": "string",
              "description": "Scientific name of the taxon iterated by index i.",
              "vocabularyTerm": "http://rs.tdwg.org/dwc/terms/scientificName"
            },
            {
              "name": "AF_i",
              "type": "real",
              "unit": "1",
              "range": "[0, +inf)",
              "description": "Per-taxon reef aggregation index (dimensionless).",
              "vocabularyTerm": "https://w3id.org/indicators/marine/parameters/reef-aggregation-index"
            },
            {
              "name": "D_pre",
              "type": "real",
              "unit": "kg m-2",
              "description": "Baseline benthic biomass density before installation.",
              "vocabularyTerm": "https://w3id.org/indicators/marine/obs/baseline-benthic-biomass-density"
            }
          ],
          "scales": {
            "spatial": "Utsira Nord licence polygon (~1000 km²)",
            "temporal": "annual aggregation; scenario T0 + 24 months"
          }
        }
      ],

      "processOverview": {
        "scheduling": "Single deterministic pass: for every taxon group i, evaluate the reef-biomass submodel and sum.",
        "processes": [
          {
            "name": "Compute reef-associated biomass",
            "executedBy": "biomass-upscaler",
            "description": "Iterates over TaxonGroup instances and applies the reef-biomass equation defined by the linked equation-property-relationship record."
          }
        ]
      },

      "inputData": [
        {
          "name": "Reef-biomass equation record",
          "description": "Canonical equation-property-relationship instance carrying the full symbol table (A_{sub}, D_{pre,i}, AF_i, C_t) with per-symbol kind, dimension kind, indexing and bindings to concrete Rainbow IRIs.",
          "source": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
          "format": "application/ld+json",
          "vocabularyTerm": "https://w3id.org/ogc/hosted/seadots/prop-rel/EquationPropertyRelationship"
        },
        {
          "name": "Per-taxon reef aggregation index (dimensionless)",
          "description": "https://w3id.org/indicators/marine/parameters/reef-aggregation-index",
          "source": "",
          "format": "application/ld+json",
          "vocabularyTerm": "example.com/reef aggregation index"
        },
        {
          "name": "Baseline benthic biomass density before installation.",
          "description": "Baseline benthic biomass density before installation.",
          "source": "",
          "format": "application/ld+json",
          "vocabularyTerm": "example.com/baseline-benthic-biomass-dataset"
        }
      ],
      "outputData": [
        {
          "name": "Reef-associated biomass",
          "description": "Sum of per-taxon reef biomass attached to submerged infrastructure.",
          "source": "",
          "format": "application/ld+json",
          "vocabularyTerm": "example.com/reef-associated-biomass"
        }
      ],

      "submodels": [
        {
          "name": "Reef-associated biomass",
          "description": "Sum of per-taxon reef biomass attached to submerged infrastructure. The full symbol table, dimensional typing, per-taxon bindings (Mytilus edulis, Buccinum undatum, Asterias rubens) and provenance are carried by the linked `equation-property-relationship` record — this submodel only restates the equation in human-readable form.",
          "equations": "B_{reef} = sum_i ( A_{sub} . D_{pre,i} . AF_i . C_t )",
          "parameterization": "Parameters are sourced through the linked equation-property-relationship instance: A_{sub} → indp:submerged-infrastructure-area-utsira-design (NVE strategic assessment); D_{pre,i} → indo:benthic-biomass-density-mareano (primary) or indo:benthic-biomass-density-imr-baseline (fallback); AF_i → indp:reef-aggregation-index-{mytilus,buccinum,asterias} expanded over odd:TaxonGroup; C_t → indp:colonisation-time-factor-default (sigmoid saturating at 24 months).",
          "links": [
            {
              "href": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
              "rel": "describedby",
              "title": "Reef-biomass equation — full symbol table, bindings and provenance"
            },
            {
              "href": "bblocks://ogc.hosted.seadots.equation-property-relationship",
              "rel": "profile",
              "title": "EquationPropertyRelationship bblock — schema and context for the linked record"
            },
            {
              "href": "https://doi.org/10.5670/oceanog.2020.405",
              "rel": "cite-as",
              "title": "Degraer et al. 2020 — artificial-reef effect prior used to parameterise AF_i"
            }
          ]
        }
      ]
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.odd-protocol",
      "type": "application/schema+json",
      "title": "ODD Protocol bblock — describes the structure of this record"
    },
    {
      "rel": "related",
      "href": "https://example.org/norwegian-ses/utsira-biomass-upscaler-v1",
      "type": "application/json",
      "title": "Utsira biomass upscaler v1 — model attribution"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/odd-protocol/context.jsonld",
  "id": "https://example.org/norwegian-ses/odd/utsira-reef-biomass-demonstrator-v1",
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          4.4,
          59.2
        ],
        [
          5.1,
          59.2
        ],
        [
          5.1,
          59.55
        ],
        [
          4.4,
          59.55
        ],
        [
          4.4,
          59.2
        ]
      ]
    ]
  },
  "time": {
    "date": "2026-05-13"
  },
  "properties": {
    "type": "SoftwareSourceCode",
    "title": "Utsira reef-biomass demonstrator \u2014 one-submodel ODD",
    "description": "Minimal ODD-Protocol record demonstrating how a single submodel can reference an exemplar equation declared in the seadots `equation-property-relationship` bblock. The submodel `Reef-associated biomass` mirrors the equation B_{reef} = sum_i (A_{sub} . D_{pre,i} . AF_i . C_t) and links out to the canonical `reef-biomass-equation.json` instance for the full symbol table, bindings, and provenance.",
    "created": "2026-05-13",
    "updated": "2026-05-13",
    "language": {
      "code": "en"
    },
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "contacts": [
      {
        "name": "Utsira biomass upscaler v1",
        "roles": [
          "author"
        ],
        "organization": "SINTEF Ocean (SeaDOTs)"
      }
    ],
    "themes": [
      {
        "concepts": [
          {
            "id": "reef-effect",
            "label": "Floating-wind reef effect"
          },
          {
            "id": "benthic-biomass",
            "label": "Benthic biomass"
          },
          {
            "id": "impact-assessment",
            "label": "Impact assessment"
          }
        ],
        "scheme": "https://id3.seadots.eu/themes"
      }
    ],
    "keywords": [
      "ODD",
      "demonstrator",
      "Utsira",
      "floating wind",
      "reef biomass",
      "equation-property-relationship",
      "SeaDOTs"
    ],
    "formats": [
      {
        "mediaType": "application/json"
      }
    ],
    "odd": {
      "purpose": "Estimate the reef-associated biomass that develops on submerged floating-wind infrastructure at Utsira Nord under the Norwegian SES scenario. Demonstrator: one submodel only, with the full equation, symbol table and per-taxon bindings carried by the linked `equation-property-relationship` record.",
      "entities": [
        {
          "name": "TaxonGroup",
          "entityType": "agent",
          "stateVariables": [
            {
              "name": "scientificName",
              "type": "string",
              "description": "Scientific name of the taxon iterated by index i.",
              "vocabularyTerm": "http://rs.tdwg.org/dwc/terms/scientificName"
            },
            {
              "name": "AF_i",
              "type": "real",
              "unit": "1",
              "range": "[0, +inf)",
              "description": "Per-taxon reef aggregation index (dimensionless).",
              "vocabularyTerm": "https://w3id.org/indicators/marine/parameters/reef-aggregation-index"
            },
            {
              "name": "D_pre",
              "type": "real",
              "unit": "kg m-2",
              "description": "Baseline benthic biomass density before installation.",
              "vocabularyTerm": "https://w3id.org/indicators/marine/obs/baseline-benthic-biomass-density"
            }
          ],
          "scales": {
            "spatial": "Utsira Nord licence polygon (~1000 km\u00b2)",
            "temporal": "annual aggregation; scenario T0 + 24 months"
          }
        }
      ],
      "processOverview": {
        "scheduling": "Single deterministic pass: for every taxon group i, evaluate the reef-biomass submodel and sum.",
        "processes": [
          {
            "name": "Compute reef-associated biomass",
            "executedBy": "biomass-upscaler",
            "description": "Iterates over TaxonGroup instances and applies the reef-biomass equation defined by the linked equation-property-relationship record."
          }
        ]
      },
      "inputData": [
        {
          "name": "Reef-biomass equation record",
          "description": "Canonical equation-property-relationship instance carrying the full symbol table (A_{sub}, D_{pre,i}, AF_i, C_t) with per-symbol kind, dimension kind, indexing and bindings to concrete Rainbow IRIs.",
          "source": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
          "format": "application/ld+json",
          "vocabularyTerm": "https://w3id.org/ogc/hosted/seadots/prop-rel/EquationPropertyRelationship"
        },
        {
          "name": "Per-taxon reef aggregation index (dimensionless)",
          "description": "https://w3id.org/indicators/marine/parameters/reef-aggregation-index",
          "source": "",
          "format": "application/ld+json",
          "vocabularyTerm": "example.com/reef aggregation index"
        },
        {
          "name": "Baseline benthic biomass density before installation.",
          "description": "Baseline benthic biomass density before installation.",
          "source": "",
          "format": "application/ld+json",
          "vocabularyTerm": "example.com/baseline-benthic-biomass-dataset"
        }
      ],
      "outputData": [
        {
          "name": "Reef-associated biomass",
          "description": "Sum of per-taxon reef biomass attached to submerged infrastructure.",
          "source": "",
          "format": "application/ld+json",
          "vocabularyTerm": "example.com/reef-associated-biomass"
        }
      ],
      "submodels": [
        {
          "name": "Reef-associated biomass",
          "description": "Sum of per-taxon reef biomass attached to submerged infrastructure. The full symbol table, dimensional typing, per-taxon bindings (Mytilus edulis, Buccinum undatum, Asterias rubens) and provenance are carried by the linked `equation-property-relationship` record \u2014 this submodel only restates the equation in human-readable form.",
          "equations": "B_{reef} = sum_i ( A_{sub} . D_{pre,i} . AF_i . C_t )",
          "parameterization": "Parameters are sourced through the linked equation-property-relationship instance: A_{sub} \u2192 indp:submerged-infrastructure-area-utsira-design (NVE strategic assessment); D_{pre,i} \u2192 indo:benthic-biomass-density-mareano (primary) or indo:benthic-biomass-density-imr-baseline (fallback); AF_i \u2192 indp:reef-aggregation-index-{mytilus,buccinum,asterias} expanded over odd:TaxonGroup; C_t \u2192 indp:colonisation-time-factor-default (sigmoid saturating at 24 months).",
          "links": [
            {
              "href": "https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation",
              "rel": "describedby",
              "title": "Reef-biomass equation \u2014 full symbol table, bindings and provenance"
            },
            {
              "href": "bblocks://ogc.hosted.seadots.equation-property-relationship",
              "rel": "profile",
              "title": "EquationPropertyRelationship bblock \u2014 schema and context for the linked record"
            },
            {
              "href": "https://doi.org/10.5670/oceanog.2020.405",
              "rel": "cite-as",
              "title": "Degraer et al. 2020 \u2014 artificial-reef effect prior used to parameterise AF_i"
            }
          ]
        }
      ]
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.odd-protocol",
      "type": "application/schema+json",
      "title": "ODD Protocol bblock \u2014 describes the structure of this record"
    },
    {
      "rel": "related",
      "href": "https://example.org/norwegian-ses/utsira-biomass-upscaler-v1",
      "type": "application/json",
      "title": "Utsira biomass upscaler v1 \u2014 model attribution"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix odd: <https://w3id.org/iliad/odd#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix schema: <https://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix thns: <https://w3id.org/ogc/stac/themes/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/norwegian-ses/odd/utsira-reef-biomass-demonstrator-v1> a <file:///github/workspace/SoftwareSourceCode>,
        geojson:Feature ;
    dcterms:created "2026-05-13" ;
    dcterms:description "Minimal ODD-Protocol record demonstrating how a single submodel can reference an exemplar equation declared in the seadots `equation-property-relationship` bblock. The submodel `Reef-associated biomass` mirrors the equation B_{reef} = sum_i (A_{sub} . D_{pre,i} . AF_i . C_t) and links out to the canonical `reef-biomass-equation.json` instance for the full symbol table, bindings, and provenance." ;
    dcterms:modified "2026-05-13" ;
    dcterms:temporal [ ] ;
    dcterms:title "Utsira reef-biomass demonstrator — one-submodel ODD" ;
    rdfs:seeAlso [ rdfs:label "Utsira biomass upscaler v1 — model attribution" ;
            dcterms:format "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/related> ;
            oa:hasTarget <https://example.org/norwegian-ses/utsira-biomass-upscaler-v1> ],
        [ rdfs:label "ODD Protocol bblock — describes the structure of this record" ;
            dcterms:format "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.odd-protocol> ] ;
    dcat:contactPoint [ ] ;
    dcat:keyword "ODD",
        "SeaDOTs",
        "Utsira",
        "demonstrator",
        "equation-property-relationship",
        "floating wind",
        "reef biomass" ;
    dcat:license "https://creativecommons.org/licenses/by/4.0/" ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 4.4e+00 5.92e+01 ) ( 5.1e+00 5.92e+01 ) ( 5.1e+00 5.955e+01 ) ( 4.4e+00 5.955e+01 ) ( 4.4e+00 5.92e+01 ) ) ) ] ;
    odd: [ odd:entities ( [ dcterms:title "TaxonGroup" ;
                        odd:entityType "agent" ;
                        odd:scales [ odd:spatialScale "Utsira Nord licence polygon (~1000 km²)" ;
                                odd:temporalScale "annual aggregation; scenario T0 + 24 months" ] ;
                        odd:stateVariables ( [ dcterms:description "Scientific name of the taxon iterated by index i." ;
                                    dcterms:title "scientificName" ;
                                    skos:exactMatch <http://rs.tdwg.org/dwc/terms/scientificName> ;
                                    odd:variableType "string" ] [ dcterms:description "Per-taxon reef aggregation index (dimensionless)." ;
                                    dcterms:title "AF_i" ;
                                    qudt:unit "1" ;
                                    skos:exactMatch <https://w3id.org/indicators/marine/parameters/reef-aggregation-index> ;
                                    odd:range "[0, +inf)" ;
                                    odd:variableType "real" ] [ dcterms:description "Baseline benthic biomass density before installation." ;
                                    dcterms:title "D_pre" ;
                                    qudt:unit "kg m-2" ;
                                    skos:exactMatch <https://w3id.org/indicators/marine/obs/baseline-benthic-biomass-density> ;
                                    odd:variableType "real" ] ) ] ) ;
            odd:inputData ( [ dcterms:description "Canonical equation-property-relationship instance carrying the full symbol table (A_{sub}, D_{pre,i}, AF_i, C_t) with per-symbol kind, dimension kind, indexing and bindings to concrete Rainbow IRIs." ;
                        dcterms:format "application/ld+json" ;
                        dcterms:title "Reef-biomass equation record" ;
                        skos:exactMatch <https://w3id.org/ogc/hosted/seadots/prop-rel/EquationPropertyRelationship> ;
                        dcat:accessURL <https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation> ] [ dcterms:description "https://w3id.org/indicators/marine/parameters/reef-aggregation-index" ;
                        dcterms:format "application/ld+json" ;
                        dcterms:title "Per-taxon reef aggregation index (dimensionless)" ;
                        skos:exactMatch <file:///github/workspace/> ;
                        dcat:accessURL <file:///github/workspace/> ] [ dcterms:description "Baseline benthic biomass density before installation." ;
                        dcterms:format "application/ld+json" ;
                        dcterms:title "Baseline benthic biomass density before installation." ;
                        skos:exactMatch <file:///github/workspace/example.com/baseline-benthic-biomass-dataset> ;
                        dcat:accessURL <file:///github/workspace/> ] ) ;
            odd:processOverview [ odd:processes ( [ dcterms:description "Iterates over TaxonGroup instances and applies the reef-biomass equation defined by the linked equation-property-relationship record." ;
                                dcterms:title "Compute reef-associated biomass" ;
                                odd:executedBy "biomass-upscaler" ] ) ;
                    odd:scheduling "Single deterministic pass: for every taxon group i, evaluate the reef-biomass submodel and sum." ] ;
            odd:purpose "Estimate the reef-associated biomass that develops on submerged floating-wind infrastructure at Utsira Nord under the Norwegian SES scenario. Demonstrator: one submodel only, with the full equation, symbol table and per-taxon bindings carried by the linked `equation-property-relationship` record." ;
            odd:submodels ( [ dcterms:description "Sum of per-taxon reef biomass attached to submerged infrastructure. The full symbol table, dimensional typing, per-taxon bindings (Mytilus edulis, Buccinum undatum, Asterias rubens) and provenance are carried by the linked `equation-property-relationship` record — this submodel only restates the equation in human-readable form." ;
                        dcterms:title "Reef-associated biomass" ;
                        rdfs:seeAlso ( [ dcterms:title "Reef-biomass equation — full symbol table, bindings and provenance" ;
                                    schema:url <https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation> ;
                                    odd:linkRel "describedby" ] [ dcterms:title "EquationPropertyRelationship bblock — schema and context for the linked record" ;
                                    schema:url <bblocks://ogc.hosted.seadots.equation-property-relationship> ;
                                    odd:linkRel "profile" ] [ dcterms:title "Degraer et al. 2020 — artificial-reef effect prior used to parameterise AF_i" ;
                                    schema:url <https://doi.org/10.5670/oceanog.2020.405> ;
                                    odd:linkRel "cite-as" ] ) ;
                        odd:equations "B_{reef} = sum_i ( A_{sub} . D_{pre,i} . AF_i . C_t )" ;
                        odd:parameterization "Parameters are sourced through the linked equation-property-relationship instance: A_{sub} → indp:submerged-infrastructure-area-utsira-design (NVE strategic assessment); D_{pre,i} → indo:benthic-biomass-density-mareano (primary) or indo:benthic-biomass-density-imr-baseline (fallback); AF_i → indp:reef-aggregation-index-{mytilus,buccinum,asterias} expanded over odd:TaxonGroup; C_t → indp:colonisation-time-factor-default (sigmoid saturating at 24 months)." ] ) ] ;
    rec:format [ rec:mediaType "application/json" ] ;
    rec:language [ rec:languageCode "en" ] ;
    rec:themes [ thns:concepts [ thns:id "reef-effect"^^xsd:string ],
                [ thns:id "impact-assessment"^^xsd:string ],
                [ thns:id "benthic-biomass"^^xsd:string ] ;
            thns:scheme "https://id3.seadots.eu/themes" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ODD Protocol Description Record
description: 'OGC API Records profile for simulation model publications described
  using the ODD Protocol (Grimm et al. 2020). Extends GeoDCAT-Records with a structured
  `odd` sub-object covering the three ODD sections: Overview (purpose, patterns, entities,
  process overview), Design Concepts (11 concepts), and Details (initialization, input
  data, submodels). Vocabulary terms for entities and variables are intentionally
  open-ended to allow domain-specific narrowing.

  '
allOf:
- $ref: https://ogcincubator.github.io/geodcat-ogcapi-records/build/annotated/geo/geodcat/geodcat-records/schema.yaml
properties:
  properties:
    type: object
    properties:
      odd:
        type: object
        description: 'ODD Protocol structured description. Keys map directly to the
          seven ODD elements. Each text field accepts plain prose; structured sub-fields
          provide vocabulary anchor points for domain profiles.

          '
        properties:
          purpose:
            type: string
            description: 'Why was the model developed? What question(s) does it address?
              Include any patterns the model is intended to reproduce (Pattern-Oriented
              Modeling).

              '
            x-jsonld-id: https://w3id.org/iliad/odd#purpose
          patterns:
            type: array
            description: 'Empirical or stylised patterns used to design, parameterise,
              or validate the model. Each entry links to an observation or dataset
              (domain vocabulary slot).

              '
            items:
              type: object
              required:
              - name
              properties:
                name:
                  type: string
                  x-jsonld-id: http://purl.org/dc/terms/title
                description:
                  type: string
                  x-jsonld-id: http://purl.org/dc/terms/description
                reference:
                  type: string
                  format: uri
                  description: DOI, URL, or vocabulary term URI for the pattern source
                  x-jsonld-id: http://purl.org/dc/terms/references
                  x-jsonld-type: '@id'
            x-jsonld-id: https://w3id.org/iliad/odd#patterns
            x-jsonld-container: '@list'
          entities:
            type: array
            description: "Agent types, environmental entities, and other model components.
              `stateVariables[].vocabularyTerm` is the slot for domain vocabulary
              injection (NERC, CF, Darwin Core, ICES, \u2026).\n"
            items:
              type: object
              required:
              - name
              properties:
                name:
                  type: string
                  x-jsonld-id: http://purl.org/dc/terms/title
                entityType:
                  type: string
                  description: 'Role of the entity: agent | patch | grid-cell | network-node
                    | network-link | environment | resource | observer | other

                    '
                  x-jsonld-id: https://w3id.org/iliad/odd#entityType
                stateVariables:
                  type: array
                  items:
                    type: object
                    required:
                    - name
                    properties:
                      name:
                        type: string
                        x-jsonld-id: http://purl.org/dc/terms/title
                      type:
                        type: string
                        description: "Data type (boolean, integer, real, string, list,
                          \u2026)"
                        x-jsonld-id: https://w3id.org/iliad/odd#variableType
                      unit:
                        type: string
                        description: 'Physical unit string (e.g. "m s-1"). For QUDT
                          or NERC unit alignment, use vocabularyTerm.

                          '
                        x-jsonld-id: http://qudt.org/schema/qudt/unit
                      range:
                        type: string
                        description: Valid range or enumeration (e.g. "[0, 1]", "non-negative")
                        x-jsonld-id: https://w3id.org/iliad/odd#range
                      description:
                        type: string
                        x-jsonld-id: http://purl.org/dc/terms/description
                      vocabularyTerm:
                        type: string
                        format: uri
                        description: 'Authoritative URI for the variable concept.
                          Priority: NERC > CF > Darwin Core > OBIS > ICES > OGC >
                          schema.org

                          '
                        x-jsonld-id: http://www.w3.org/2004/02/skos/core#exactMatch
                        x-jsonld-type: '@id'
                  x-jsonld-id: https://w3id.org/iliad/odd#stateVariables
                  x-jsonld-container: '@list'
                scales:
                  type: object
                  properties:
                    spatial:
                      type: string
                      description: "Spatial resolution and extent (e.g. \"1 m grid,
                        10 km \xD7 10 km\")"
                      x-jsonld-id: https://w3id.org/iliad/odd#spatialScale
                    temporal:
                      type: string
                      description: Time step and total duration (e.g. "1 day, 30 years")
                      x-jsonld-id: https://w3id.org/iliad/odd#temporalScale
                  x-jsonld-id: https://w3id.org/iliad/odd#scales
            x-jsonld-id: https://w3id.org/iliad/odd#entities
            x-jsonld-container: '@list'
          processOverview:
            type: object
            description: 'Which processes are executed, by whom, and in what order?
              The scheduling field must describe the temporal ordering precisely (e.g.
              "synchronous, random order within step").

              '
            properties:
              scheduling:
                type: string
                x-jsonld-id: https://w3id.org/iliad/odd#scheduling
              processes:
                type: array
                items:
                  type: object
                  required:
                  - name
                  properties:
                    name:
                      type: string
                      x-jsonld-id: http://purl.org/dc/terms/title
                    executedBy:
                      type: string
                      description: Entity type that runs this process
                      x-jsonld-id: https://w3id.org/iliad/odd#executedBy
                    description:
                      type: string
                      x-jsonld-id: http://purl.org/dc/terms/description
                x-jsonld-id: https://w3id.org/iliad/odd#processes
                x-jsonld-container: '@list'
            x-jsonld-id: https://w3id.org/iliad/odd#processOverview
          designConcepts:
            type: object
            description: 'The 11 design concepts defined by ODD. Each is a free-text
              field; domain profiles may add controlled-vocabulary annotations alongside.

              '
            properties:
              basicPrinciples:
                type: string
                description: 'Which general theoretical or empirical concepts (theories,
                  hypotheses, heuristics) underlie the model?

                  '
                x-jsonld-id: https://w3id.org/iliad/odd#basicPrinciples
              emergence:
                type: string
                description: 'Which key model results emerge from agent interactions
                  rather than being imposed directly on the agents?

                  '
                x-jsonld-id: https://w3id.org/iliad/odd#emergence
              adaptation:
                type: string
                description: 'What adaptive traits do agents have, and on what information
                  are adaptation decisions based?

                  '
                x-jsonld-id: https://w3id.org/iliad/odd#adaptation
              objectives:
                type: string
                description: 'What objectives do agents seek to achieve, and how are
                  the objectives measured?

                  '
                x-jsonld-id: https://w3id.org/iliad/odd#objectives
              learning:
                type: string
                description: 'Do agents adapt their behaviour over time in response
                  to experience? What algorithm is used?

                  '
                x-jsonld-id: https://w3id.org/iliad/odd#learning
              prediction:
                type: string
                description: 'Do agents make predictions about future conditions?
                  What methods or models are used for prediction?

                  '
                x-jsonld-id: https://w3id.org/iliad/odd#prediction
              sensing:
                type: string
                description: 'What information can agents perceive about themselves
                  and the environment? Are sensing assumptions justified?

                  '
                x-jsonld-id: https://w3id.org/iliad/odd#sensing
              interaction:
                type: string
                description: 'What direct and indirect interactions occur among agents
                  and between agents and the environment?

                  '
                x-jsonld-id: https://w3id.org/iliad/odd#interaction
              stochasticity:
                type: string
                description: 'Which processes are represented as stochastic? How and
                  why?

                  '
                x-jsonld-id: https://w3id.org/iliad/odd#stochasticity
              collectives:
                type: string
                description: 'Are there collectives (groups, flocks, organisations,
                  markets)? How are they represented and how do they affect agent
                  behaviour?

                  '
                x-jsonld-id: https://w3id.org/iliad/odd#collectives
              observation:
                type: string
                description: 'What data are collected from the model for analysis?
                  How are collectives, individuals, and the environment observed?

                  '
                x-jsonld-id: https://w3id.org/iliad/odd#observation
            x-jsonld-id: https://w3id.org/iliad/odd#designConcepts
          initialization:
            type: object
            description: 'State of the model at t=0: number of agents, their initial
              attributes, spatial configuration, and how the initial state was chosen.

              '
            properties:
              description:
                type: string
                x-jsonld-id: http://purl.org/dc/terms/description
              seed:
                type: string
                description: How the random seed is specified or varied across runs
                x-jsonld-id: https://w3id.org/iliad/odd#randomSeed
              links:
                type: array
                description: 'References to initialization data files or datasets
                  (domain vocabulary slot for DCAT Dataset links).

                  '
                items:
                  type: object
                  required:
                  - href
                  properties:
                    href:
                      type: string
                      format: uri
                      x-jsonld-id: https://schema.org/url
                      x-jsonld-type: '@id'
                    title:
                      type: string
                      x-jsonld-id: http://purl.org/dc/terms/title
                    type:
                      type: string
                      description: Media type
                      x-jsonld-id: https://w3id.org/iliad/odd#variableType
                x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
                x-jsonld-type: '@id'
                x-jsonld-container: '@list'
            x-jsonld-id: https://w3id.org/iliad/odd#initialization
          inputData:
            type: array
            description: 'External data sources (time series, maps, tables) used to
              drive or parameterise the model. `vocabularyTerm` is the domain slot
              for NERC, CF, or dataset-catalogue URIs.

              '
            items:
              type: object
              required:
              - name
              properties:
                name:
                  type: string
                  x-jsonld-id: http://purl.org/dc/terms/title
                description:
                  type: string
                  x-jsonld-id: http://purl.org/dc/terms/description
                source:
                  type: string
                  format: uri
                  description: Access URL (DCAT Distribution, OGC API, or DOI)
                  x-jsonld-id: http://www.w3.org/ns/dcat#accessURL
                  x-jsonld-type: '@id'
                format:
                  type: string
                  description: Media type or format name (e.g. "text/csv", "NetCDF")
                  x-jsonld-id: http://purl.org/dc/terms/format
                temporalCoverage:
                  type: string
                  x-jsonld-id: http://purl.org/dc/terms/temporal
                vocabularyTerm:
                  type: string
                  format: uri
                  description: 'Concept URI for the variable or dataset type. Priority:
                    NERC > CF > Darwin Core > OBIS > ICES > EMODnet

                    '
                  x-jsonld-id: http://www.w3.org/2004/02/skos/core#exactMatch
                  x-jsonld-type: '@id'
            x-jsonld-id: https://w3id.org/iliad/odd#inputData
            x-jsonld-container: '@list'
          submodels:
            type: array
            description: 'Detailed descriptions of each submodel. Equations and parameterisation
              choices that are not derivable from first principles must be fully documented
              here.

              '
            items:
              type: object
              required:
              - name
              properties:
                name:
                  type: string
                  x-jsonld-id: http://purl.org/dc/terms/title
                description:
                  type: string
                  x-jsonld-id: http://purl.org/dc/terms/description
                equations:
                  type: string
                  description: Mathematical specification (LaTeX or plain text)
                  x-jsonld-id: https://w3id.org/iliad/odd#equations
                parameterization:
                  type: string
                  description: Parameter values, sources, and calibration approach
                  x-jsonld-id: https://w3id.org/iliad/odd#parameterization
                links:
                  type: array
                  description: References to code, data, or supplementary material
                  items:
                    type: object
                    required:
                    - href
                    properties:
                      href:
                        type: string
                        format: uri
                        x-jsonld-id: https://schema.org/url
                        x-jsonld-type: '@id'
                      rel:
                        type: string
                        x-jsonld-id: https://w3id.org/iliad/odd#linkRel
                      title:
                        type: string
                        x-jsonld-id: http://purl.org/dc/terms/title
                  x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
                  x-jsonld-type: '@id'
                  x-jsonld-container: '@list'
            x-jsonld-id: https://w3id.org/iliad/odd#submodels
            x-jsonld-container: '@list'
        x-jsonld-id: https://w3id.org/iliad/odd#
x-jsonld-prefixes:
  odd: https://w3id.org/iliad/odd#
  dcterms: http://purl.org/dc/terms/
  qudt: http://qudt.org/schema/qudt/
  skos: http://www.w3.org/2004/02/skos/core#
  dcat: http://www.w3.org/ns/dcat#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  schema: https://schema.org/
  prov: http://www.w3.org/ns/prov#
  xsd: http://www.w3.org/2001/XMLSchema#
  sosa: http://www.w3.org/ns/sosa/
  foaf: http://xmlns.com/foaf/0.1/
  bibo: http://purl.org/ontology/bibo/
  osc: https://github.com/ILIAD-ocean-twin/OIM/blob/main/openscience#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/odd-protocol/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/odd-protocol/schema.yaml)


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
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:format",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "conformsTo": {
      "@container": "@set",
      "@id": "dct:conformsTo",
      "@type": "@id"
    },
    "time": "dct:temporal",
    "linkTemplates": {
      "@context": {
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:format",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent",
        "uriTemplate": {
          "@type": "xsd:string",
          "@id": "rec:uriTemplate"
        },
        "varBase": "rec:varBase",
        "variables": {
          "@id": "rec:hasVariable",
          "@container": "@index",
          "@index": "dct:identifier"
        }
      },
      "@id": "rec:hasLinkTemplate"
    },
    "created": "dct:created",
    "updated": "dct:modified",
    "title": {
      "@container": "@set",
      "@id": "dct:title"
    },
    "description": {
      "@container": "@set",
      "@id": "dct:description"
    },
    "keywords": {
      "@container": "@set",
      "@id": "dcat:keyword"
    },
    "language": {
      "@id": "rec:language",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "languages": {
      "@container": "@set",
      "@id": "rec:languages",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "resourceLanguages": {
      "@container": "@set",
      "@id": "rec:resourceLanguages",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "externalIds": {
      "@container": "@set",
      "@id": "rec:scopedIdentifier",
      "@context": {
        "scheme": "rec:scheme",
        "value": "rec:id"
      }
    },
    "themes": {
      "@container": "@set",
      "@id": "rec:themes",
      "@context": {
        "concepts": {
          "@id": "thns:concepts",
          "@context": {
            "id": {
              "@type": "xsd:string",
              "@id": "thns:id"
            },
            "url": {
              "@type": "@id",
              "@id": "@id"
            }
          },
          "@container": "@set"
        },
        "scheme": "thns:scheme"
      }
    },
    "formats": {
      "@id": "rec:format",
      "@context": {
        "name": "rec:name",
        "mediaType": "rec:mediaType"
      },
      "@container": "@set",
      "@type": "@id"
    },
    "contacts": {
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "license": "dcat:license",
    "accessrights": "dct:accessRights",
    "variables": {
      "@container": "@id",
      "@id": "rec:hasVariable",
      "@context": {
        "@base": "http://example.com/variables/",
        "@vocab": "https://www.opengis.net/def/ogc-api/records/"
      }
    },
    "odd": {
      "@context": {
        "purpose": "https://w3id.org/iliad/odd#purpose",
        "patterns": {
          "@context": {
            "name": "dct:title",
            "reference": {
              "@id": "dct:references",
              "@type": "@id"
            }
          },
          "@id": "https://w3id.org/iliad/odd#patterns",
          "@container": "@list"
        },
        "entities": {
          "@context": {
            "name": "dct:title",
            "entityType": "https://w3id.org/iliad/odd#entityType",
            "stateVariables": {
              "@context": {
                "type": "https://w3id.org/iliad/odd#variableType",
                "unit": "qudt:unit",
                "range": "https://w3id.org/iliad/odd#range",
                "vocabularyTerm": {
                  "@id": "skos:exactMatch",
                  "@type": "@id"
                }
              },
              "@id": "https://w3id.org/iliad/odd#stateVariables",
              "@container": "@list"
            },
            "scales": {
              "@context": {
                "spatial": "https://w3id.org/iliad/odd#spatialScale",
                "temporal": "https://w3id.org/iliad/odd#temporalScale"
              },
              "@id": "https://w3id.org/iliad/odd#scales"
            }
          },
          "@id": "https://w3id.org/iliad/odd#entities",
          "@container": "@list"
        },
        "processOverview": {
          "@context": {
            "scheduling": "https://w3id.org/iliad/odd#scheduling",
            "processes": {
              "@context": {
                "name": "dct:title",
                "executedBy": "https://w3id.org/iliad/odd#executedBy"
              },
              "@id": "https://w3id.org/iliad/odd#processes",
              "@container": "@list"
            }
          },
          "@id": "https://w3id.org/iliad/odd#processOverview"
        },
        "designConcepts": {
          "@context": {
            "basicPrinciples": "https://w3id.org/iliad/odd#basicPrinciples",
            "emergence": "https://w3id.org/iliad/odd#emergence",
            "adaptation": "https://w3id.org/iliad/odd#adaptation",
            "objectives": "https://w3id.org/iliad/odd#objectives",
            "learning": "https://w3id.org/iliad/odd#learning",
            "prediction": "https://w3id.org/iliad/odd#prediction",
            "sensing": "https://w3id.org/iliad/odd#sensing",
            "interaction": "https://w3id.org/iliad/odd#interaction",
            "stochasticity": "https://w3id.org/iliad/odd#stochasticity",
            "collectives": "https://w3id.org/iliad/odd#collectives",
            "observation": "https://w3id.org/iliad/odd#observation"
          },
          "@id": "https://w3id.org/iliad/odd#designConcepts"
        },
        "initialization": {
          "@context": {
            "seed": "https://w3id.org/iliad/odd#randomSeed",
            "links": {
              "@context": {
                "href": {
                  "@id": "schema:url",
                  "@type": "@id"
                },
                "type": "https://w3id.org/iliad/odd#variableType"
              },
              "@id": "rdfs:seeAlso",
              "@type": "@id",
              "@container": "@list"
            }
          },
          "@id": "https://w3id.org/iliad/odd#initialization"
        },
        "inputData": {
          "@context": {
            "name": "dct:title",
            "source": {
              "@id": "dcat:accessURL",
              "@type": "@id"
            },
            "format": "dct:format",
            "temporalCoverage": "dct:temporal",
            "vocabularyTerm": {
              "@id": "skos:exactMatch",
              "@type": "@id"
            }
          },
          "@id": "https://w3id.org/iliad/odd#inputData",
          "@container": "@list"
        },
        "submodels": {
          "@context": {
            "name": "dct:title",
            "equations": "https://w3id.org/iliad/odd#equations",
            "parameterization": "https://w3id.org/iliad/odd#parameterization",
            "links": {
              "@context": {
                "href": {
                  "@id": "schema:url",
                  "@type": "@id"
                },
                "rel": "https://w3id.org/iliad/odd#linkRel"
              },
              "@id": "rdfs:seeAlso",
              "@type": "@id",
              "@container": "@list"
            }
          },
          "@id": "https://w3id.org/iliad/odd#submodels",
          "@container": "@list"
        }
      },
      "@id": "https://w3id.org/iliad/odd#"
    },
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "rec": "https://www.opengis.net/def/ogc-api/records/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "w3ctime": "http://www.w3.org/2006/time#",
    "dctype": "http://purl.org/dc/dcmitype/",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "prov": "http://www.w3.org/ns/prov#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "thns": "https://w3id.org/ogc/stac/themes/",
    "dcterms": "http://purl.org/dc/terms/",
    "qudt": "http://qudt.org/schema/qudt/",
    "schema": "https://schema.org/",
    "sosa": "http://www.w3.org/ns/sosa/",
    "bibo": "http://purl.org/ontology/bibo/",
    "osc": "https://github.com/ILIAD-ocean-twin/OIM/blob/main/openscience#",
    "rights": "dcat:rights",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/odd-protocol/context.jsonld)

## Sources

* [The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update](https://doi.org/10.18564/jasss.4259)
* [GeoDCAT mapping for OGC API Records](https://ogcincubator.github.io/geodcat-ogcapi-records/)
* [Open Science Building Blocks](https://ogcincubator.github.io/bblocks-openscience/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/odd-protocol`

