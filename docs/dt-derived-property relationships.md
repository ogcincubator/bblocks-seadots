Provenance-aware indicator relationships for coastal Digital Twins: the SeaDOTs PropertyRelationship building block
                                                                                                                                                                                                                                                                                
  Piotr Zaborowski¹, [co-authors]
  ¹ OGC Europe| Open Geospatial Consortium Europe, Leuven, Belgium                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                
  ---                                                                                                                                                                                                                                                                           
  Abstract                                                                                                                                                                                                                                                                      
                                                            
  Coastal Digital Twins (DTs) generate what-if scenario outputs that are meaningful only in relation to the dependency structure between the indicators they manipulate. In practice these dependencies — weighted, directed influence edges between observable properties — are stored in spreadsheets or bespoke formats that are neither FAIR nor interoperable across DT platforms. We present the PropertyRelationship OGC Building Block, developed in the SeaDOTs EU project, which encodes such relationships in a standard JSON/JSON-LD schema with full PROV-O provenance, QUDT-quantified weights, and SHACL validation. Applied to the Norwegian Utsira wind-farm demonstrator, the model enables machine-readable cross-impact matrices to be queried via SPARQL, embedded in STAC experiment records, and published alongside the SKOS indicator vocabulary in the EDITO platform. The building block is registered in the OGC Building Block Register and is designed for reuse across the ILIAD Ocean Digital Twin ecosystem.                                                                            
                                                            

 Introduction
                 
  Marine Digital Twins simulate socio-ecological processes and produce scenario outputs — projections of fisheries yield, renewable energy capacity, species abundance — that are compared and communicated to stakeholders. The outputs of these simulations acquire meaning only through the indicator dependency structures embedded in the underlying models: the fact that increasing wind-park area suppresses fisheries production, or that employment in the tourism sector reinforces bird-watching activity, is what makes a scenario  interpretable.
Despite their importance, these dependency structures are rarely represented in a FAIR [1] or interoperable way. Common practice in EU-funded projects is to maintain cross-impact matrices as worksheets, shared outside any formal data catalogue. Downstream consumers - other DTs, policy dashboards, model comparison services — cannot discover, validate, or query these relationships without bespoke integration work.

The SeaDOTs project (http://seadots-project.eu) operates three coastal Digital Twin demonstrators in Germany, Norway, and Sweden. Each demonstrator applies a Social-Ecological System (SES) model [2] in which indicators correspond to observable properties of the managed system, and model runs produce estimates of the directional influence between those properties. A core objective of SeaDOTs is to publish these indicator relationships in a machine-readable, provenance-rich form that is interoperable with the EDITO marine platform and the European Open Science Cloud (EOSC).                                                                                                                                                         
                                                            
Proposed Indicators relationship model is 3 level architecture. SES model level represents Actors, Governance, Resource System with Resource Units and their interactions. Variables level represents relationships discovered with Digital Twins or collected during desk research based on the scientific studies. Digital Twins execution level represent relationships between marine models; Agents Based Systems, numerical modeling, fuzzy-cognitive maps.
  
Background                                             
               
  Observable properties and SOSA/SSN. The W3C Semantic Sensor Network ontology (SOSA/SSN) [3] models observations as relationships between a sensor (or procedure), a feature of interest, and an observable property. In the OGC Ocean Information Model (OIM) [4] — SeaDOTs'
  cross-domain semantic layer — observable properties are identified by resolvable URIs, enabling datasets from different providers to share a common property vocabulary.                                                                                                      
  
  Provenance with PROV-O. W3C PROV-O [5] models the provenance of entities through activities and agents. An indicator relationship produced by a cross-impact analysis model is a prov:Entity generated by a prov:Activity (the model run) attributed to a prov:Agent (the     
  model itself). This attribution chain is essential for scientific reproducibility: a relationship weight of 0.5 between fisheries production and number of turbines is only interpretable together with the model version and experiment parameters that produced it.
                                                                                                                                                                                                                                                                                
  OGC Building Blocks. The OGC Building Block infrastructure [6] packages a JSON Schema, a JSON-LD semantic context, SHACL validation rules, and human-readable documentation into a single versioned, testable unit. Building blocks compose via $ref imports and are validated
   by a CI pipeline (bblocks-postprocess). The SeaDOTs building blocks are published at https://github.com/ogcincubator/bblocks-seadots.
 

Figure 1 Legend.

                                                                                                                                                                                                                                                                                
The PropertyRelationship model
                                                                                                                                                                                                                                                                                
  A PropertyRelationship instance links two sosa:observedProperty IRIs — fromProperty and toProperty — with a numeric weight quantifying the directional influence between them. Required fields are fromProperty, toProperty, weight.value, and model.id. The experiment object
   is optional but strongly recommended for traceability.                                                                                                                                                                                                                       
  
  {                                                                                                                                                                                                                                                                             
    "type": "PropertyRelationship",                         
    "fromProperty": "https://id3.seadots.eu/indicator/obs/fisheries-production",
    "toProperty":   "https://id3.seadots.eu/indicator/obs/number-of-turbines",                                                                                                                                                                                                  
    "weight": { "value": 0.5 },                                                                                                                                                                                                                                                 
    "model": {                                                                                                                                                                                                                                                                  
      "id":   "crossImpact-v1",                                                                                                                                                                                                                                                 
      "name": "Cross-Impact Analysis Model",                                                                                                                                                                                                                                    
      "uri":  "https://id3.seadots.eu/seadots/models/crossImpact-v1"                                                                                                                                                                                                               
    },                                                                                                                                                                                                                                                                          
    "experiment": {                                                                                                                                                                                                                                                             
      "id":    "utsira:exp-2024-01",                        
      "name":  "Utsira Wind Farm Impact Assessment",                                                                                                                                                                                                                            
      "start": "2024-01-15T08:00:00Z",
      "end":   "2024-01-15T17:30:00Z"                                                                                                                                                                                                                                           
    }                                                                                                                                                                                                                                                                           
  }                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                
  The JSON-LD context (context.jsonld) maps each field to a standard RDF predicate: model → prov:wasAttributedTo; experiment → prov:wasGeneratedBy; weight.value → qudt:numericValue; fromProperty / toProperty → properties of the prop-rel:PropertyRelationship OWL class. Any JSON payload can therefore be interpreted as an RDF graph by embedding the published context, without schema changes.
                                                                                                                                                                                                                                                                                
  The building block is published under the identifier ogc.hosted.seadots.property-relationship and imports the main OGC Building Block Register for cross-references. A SHACL shape validates that required fields are present and that property values are valid IRIs or  CURIEs. The supporting ontology (ontology.ttl) is uploaded to a hosted SPARQL triplestore on build, making the vocabulary queryable at http://defs-hosted.opengis.net/fuseki-hosted/query.
                                                                                                                                                                                                                                                                                
Application: Utsira wind-farm cross-impact matrix
                                                      
The Norwegian SeaDOTs demonstrator models the social-ecological system of the Utsira island wind farm, where key interactions occur between fisheries production, wind-park configuration, employment, and wildlife tourism. A cross-impact analysis produced eight directed weighted relationships between five indicator properties (Table 1).                                                                                                                                                                                                           
  
  Table 1. Utsira cross-impact matrix encoded as PropertyRelationship instances.                                                                                                                                                                                                
                
                                                            
  All eight instances are stored in a Turtle file loaded into an Apache Jena Fuseki SPARQL endpoint, and published in a SKOS concept scheme at EDITO. They are linked from the STAC experiment record for the Utsira model run via prov:wasGeneratedBy, so that the dependency structure is discoverable alongside the scenario outputs in the EDITO catalog.

Integration in the broader interoperability framework
                                                          
PropertyRelationship is one component of the SeaDOTs interoperability stack, which covers three data categories (multidimensional, tabular, and graph/knowledge data) and targets two publication platforms (EDITO and EOSC). The indicator properties referenced by fromProperty and toProperty are sosa:observedProperty instances from the SeaDOTs SKOS vocabulary, themselves profiled by the OIM observation schema (ogc.hosted.iliadapi.oim-obs). This means a single SPARQL query can traverse from an indicator relationship to the that measured the underlying properties.
                                                                                                                                                                                                                                                                                
  The building block approach is not SeaDOTs-specific. The PropertyRelationship schema and ontology are defined under the OGC-hosted namespace and designed to be reused across the ILIAD Ocean Digital Twin ecosystem and any domain where weighted, provenance-annotated      
  property graphs are required — marine ecosystem models, climate impact chains, or urban planning indicators.
                                                                                                                                                                                                                                                                                
Conclusions
                                                                                                                                                                                                                                                                                
  We have presented the PropertyRelationship OGC Building Block, which provides a standard, provenance-rich, machine-readable representation for weighted indicator relationships in coastal Digital Twins. Applied to the Utsira wind-farm case, it converts a spreadsheet
  cross-impact matrix into SPARQL-queryable, FAIR-compliant linked data embedded in the project's STAC catalog.                                                                                                                                                                 
                                                            
  Remaining work includes: publishing resolvable HTTP URIs for all SeaDOTs indicator properties (via OGC Rainbow); extending the schema with a typed influence classification (positive / negative / feedback); and applying the model to the German and Swedish demonstrators, 
  where indicator dependencies span biological, physical, and economic domains.

References
Wilkinson et al. (2016). The FAIR Guiding Principles for scientific data management. Scientific Data 3, 160018.                                                                                                                                                           
  [2] Ostrom, E. (1990). Governing the Commons. Cambridge University Press.
  [3] Haller et al. (2019). The Modular SSN Ontology: A Joint W3C and OGC Standard. Semantic Web 10(1), 9–32.                                                                                                                                                                   
  [5] Moreau & Missier (eds.) (2013). PROV-O: The PROV Ontology. W3C Recommendation.                                                                                                                                                                                            

Sitography 
  [4] ILIAD project (2023). Ocean Information Model. https://github.com/ILIAD-ocean-twin/OIM                                                                                                                                                                                    
  [6] OGC Incubator (2024). OGC Building Blocks. https://ogcincubator.github.io/bblocks-docs/                                                                                                                                                                                   
  [7] SeaDOTs project (2024). SeaDOTs interoperability building blocks. https://github.com/ogcincubator/bblocks-seadots                                                                                                                                                         
[8] https://edito-infra.eu    

ORCID:
First name Last name ,0000-0003-1283-2798
First name Last name ,0000-0003-1283-2798
 
