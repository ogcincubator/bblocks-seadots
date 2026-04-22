
# Property relationship (Schema)

`ogc.hosted.seadots.property-relationship` *v1.0*

Provides a common model for defining property relationships bound to the ontology

[*Status*](http://www.opengis.net/def/status): Under development

## Description

A `PropertyRelationship` links two observable properties (`fromProperty` → `toProperty`) with a numeric weight
expressing the strength of their relationship, as produced by a specific model and experiment.

The `model` identifies the algorithm or system that generated the relationship, while `experiment` captures the
activity that ran it, including optional start and end timestamps. Both map to PROV-O concepts
(`prov:wasAttributedTo` and `prov:wasGeneratedBy` respectively).
## Examples

### Minimal relationship
A minimal property relationship with only the required fields: source property,
target property, weight value, and model identifier. Derived from the Utsira wind
farm toy dataset, expressing that fisheries production has a positive relationship
(weight 0.5) with the number of turbines.

#### json
```json
{
  "fromProperty": "utsira:fisheries-production",
  "toProperty": "utsira:number-of-turbines",
  "weight": {
    "value": 0.5
  },
  "model": {
    "id": "crossImpact-v1"
  }
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "utsira": "https://example.org/seadots/utsira/"
    },
    "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/property-relationship/context.jsonld"
  ],
  "fromProperty": "utsira:fisheries-production",
  "toProperty": "utsira:number-of-turbines",
  "weight": {
    "value": 0.5
  },
  "model": {
    "id": "crossImpact-v1"
  }
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix prop-rel: <https://w3id.org/ogc/hosted/seadots/prop-rel/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix utsira: <https://example.org/seadots/utsira/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] prov:wasAttributedTo [ dct:identifier "crossImpact-v1" ] ;
    prop-rel:fromProperty utsira:fisheries-production ;
    prop-rel:hasWeight [ qudt:numericValue 5e-01 ] ;
    prop-rel:toProperty utsira:number-of-turbines .


```


### Relationship with model attribution
A property relationship that includes full model attribution metadata — name and URI
in addition to the model identifier. The negative weight (-0.5) expresses that
increasing the area used by the wind park has an adverse effect on fisheries production.

#### json
```json
{
  "type": "PropertyRelationship",
  "fromProperty": "utsira:fisheries-production",
  "toProperty": "utsira:area-use-by-wind-park",
  "weight": {
    "value": -0.5
  },
  "model": {
    "id": "utsira:crossImpact-v1",
    "name": "Cross-Impact Analysis Model",
    "uri": "https://example.org/seadots/models/crossImpact-v1"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "utsira": "https://example.org/seadots/utsira/"
    },
    "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/property-relationship/context.jsonld"
  ],
  "type": "PropertyRelationship",
  "fromProperty": "utsira:fisheries-production",
  "toProperty": "utsira:area-use-by-wind-park",
  "weight": {
    "value": -0.5
  },
  "model": {
    "id": "utsira:crossImpact-v1",
    "name": "Cross-Impact Analysis Model",
    "uri": "https://example.org/seadots/models/crossImpact-v1"
  }
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix prop-rel: <https://w3id.org/ogc/hosted/seadots/prop-rel/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix utsira: <https://example.org/seadots/utsira/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/seadots/models/crossImpact-v1> rdfs:label "Cross-Impact Analysis Model" ;
    dct:identifier "utsira:crossImpact-v1" .

[] a prop-rel:PropertyRelationship ;
    prov:wasAttributedTo <https://example.org/seadots/models/crossImpact-v1> ;
    prop-rel:fromProperty utsira:fisheries-production ;
    prop-rel:hasWeight [ qudt:numericValue -5e-01 ] ;
    prop-rel:toProperty utsira:area-use-by-wind-park .


```


### Relationship with model and experiment provenance
A fully annotated property relationship including both model attribution and the
experiment that generated it, with start and end timestamps. This example expresses
a positive relationship (weight 0.52) between the number of jobs and bird tourism
at the Utsira site, as produced by a named cross-impact analysis experiment.

#### json
```json
{
  "type": "PropertyRelationship",
  "id": "utsira:runs/e7c5de87-940b-458c-b9b2-1bd000ec4328",
  "fromProperty": "utsira:number-of-jobs",
  "toProperty": "utsira:bird-tourism",
  "weight": {
    "value": 0.52
  },
  "model": {
    "id": "utsira:crossImpact-v1",
    "name": "Cross-Impact Analysis Model",
    "uri": "https://example.org/seadots/models/crossImpact-v1"
  },
  "experiment": {
    "id": "utsira:exp-2024-01",
    "name": "Utsira Wind Farm Impact Assessment",
    "start": "2024-01-15T08:00:00Z",
    "end": "2024-01-15T17:30:00Z"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "utsira": "https://example.org/seadots/utsira/"
    },
    "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/property-relationship/context.jsonld"
  ],
  "type": "PropertyRelationship",
  "id": "utsira:runs/e7c5de87-940b-458c-b9b2-1bd000ec4328",
  "fromProperty": "utsira:number-of-jobs",
  "toProperty": "utsira:bird-tourism",
  "weight": {
    "value": 0.52
  },
  "model": {
    "id": "utsira:crossImpact-v1",
    "name": "Cross-Impact Analysis Model",
    "uri": "https://example.org/seadots/models/crossImpact-v1"
  },
  "experiment": {
    "id": "utsira:exp-2024-01",
    "name": "Utsira Wind Farm Impact Assessment",
    "start": "2024-01-15T08:00:00Z",
    "end": "2024-01-15T17:30:00Z"
  }
}
```

#### ttl
```ttl
@prefix dct: <http://purl.org/dc/terms/> .
@prefix prop-rel: <https://w3id.org/ogc/hosted/seadots/prop-rel/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix utsira: <https://example.org/seadots/utsira/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/seadots/utsira/runs/e7c5de87-940b-458c-b9b2-1bd000ec4328> a prop-rel:PropertyRelationship ;
    prov:wasAttributedTo <https://example.org/seadots/models/crossImpact-v1> ;
    prov:wasGeneratedBy [ rdfs:label "Utsira Wind Farm Impact Assessment" ;
            dct:identifier "utsira:exp-2024-01" ;
            prov:endedAtTime "2024-01-15T17:30:00+00:00"^^xsd:dateTime ;
            prov:startedAtTime "2024-01-15T08:00:00+00:00"^^xsd:dateTime ] ;
    prop-rel:fromProperty utsira:number-of-jobs ;
    prop-rel:hasWeight [ qudt:numericValue 5.2e-01 ] ;
    prop-rel:toProperty utsira:bird-tourism .

<https://example.org/seadots/models/crossImpact-v1> rdfs:label "Cross-Impact Analysis Model" ;
    dct:identifier "utsira:crossImpact-v1" .


```

## Schema

```yaml
type: object
required:
- fromProperty
- toProperty
- weight
- model
properties:
  id:
    $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
    description: Identifier (IRI or CURIE) for the relationship, if any
    x-jsonld-id: '@id'
  type:
    const: PropertyRelationship
    x-jsonld-id: '@type'
  fromProperty:
    $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
    description: IRI or CURIE of the source property in the relationship.
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/fromProperty
    x-jsonld-type: '@id'
  toProperty:
    $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
    description: IRI or CURIE of the target property in the relationship.
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/toProperty
    x-jsonld-type: '@id'
  weight:
    description: Quantified strength of the relationship between the two properties
      (qudt:numericValue).
    type: object
    required:
    - value
    properties:
      value:
        type: number
        description: Numeric value of the weight.
        x-jsonld-id: http://qudt.org/schema/qudt/numericValue
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/prop-rel/hasWeight
    x-jsonld-type: '@id'
  model:
    description: Model that generated this relationship (prov:wasAttributedTo).
    type: object
    required:
    - id
    properties:
      id:
        type: string
        description: Identifier of the model (dct:identifier).
        x-jsonld-id: http://purl.org/dc/terms/identifier
      name:
        type: string
        description: Human-readable label of the model (rdfs:label).
        x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#label
      uri:
        type: string
        description: URI of the model resource.
        x-jsonld-id: '@id'
    x-jsonld-id: http://www.w3.org/ns/prov#wasAttributedTo
  experiment:
    description: Experiment activity that produced this relationship (prov:wasGeneratedBy).
    type: object
    required:
    - id
    properties:
      id:
        type: string
        description: Identifier of the experiment (dct:identifier).
        x-jsonld-id: http://purl.org/dc/terms/identifier
      name:
        type: string
        description: Human-readable label of the experiment (rdfs:label).
        x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#label
      uri:
        type: string
        description: URI of the experiment resource.
        x-jsonld-id: '@id'
      start:
        type: string
        format: date-time
        pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?$
        description: Date and time when the experiment started (prov:startedAtTime).
        x-jsonld-id: http://www.w3.org/ns/prov#startedAtTime
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
      end:
        type: string
        format: date-time
        pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?$
        description: Date and time when the experiment ended (prov:endedAtTime).
        x-jsonld-id: http://www.w3.org/ns/prov#endedAtTime
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
    x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
x-jsonld-extra-terms:
  PropertyRelationship: https://w3id.org/ogc/hosted/seadots/prop-rel/PropertyRelationship
x-jsonld-prefixes:
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  prop-rel: https://w3id.org/ogc/hosted/seadots/prop-rel/
  qudt: http://qudt.org/schema/qudt/
  prov: http://www.w3.org/ns/prov#
  dct: http://purl.org/dc/terms/
  xsd: http://www.w3.org/2001/XMLSchema#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/property-relationship/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/property-relationship/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "PropertyRelationship": "prop-rel:PropertyRelationship",
    "id": "@id",
    "type": "@type",
    "fromProperty": {
      "@id": "prop-rel:fromProperty",
      "@type": "@id"
    },
    "toProperty": {
      "@id": "prop-rel:toProperty",
      "@type": "@id"
    },
    "weight": {
      "@context": {
        "value": "qudt:numericValue"
      },
      "@id": "prop-rel:hasWeight",
      "@type": "@id"
    },
    "model": {
      "@context": {
        "id": "dct:identifier",
        "name": "rdfs:label",
        "uri": "@id"
      },
      "@id": "prov:wasAttributedTo"
    },
    "experiment": {
      "@context": {
        "id": "dct:identifier",
        "name": "rdfs:label",
        "uri": "@id",
        "start": {
          "@id": "prov:startedAtTime",
          "@type": "xsd:dateTime"
        },
        "end": {
          "@id": "prov:endedAtTime",
          "@type": "xsd:dateTime"
        }
      },
      "@id": "prov:wasGeneratedBy"
    },
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "prop-rel": "https://w3id.org/ogc/hosted/seadots/prop-rel/",
    "qudt": "http://qudt.org/schema/qudt/",
    "prov": "http://www.w3.org/ns/prov#",
    "dct": "http://purl.org/dc/terms/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/property-relationship/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/property-relationship`

