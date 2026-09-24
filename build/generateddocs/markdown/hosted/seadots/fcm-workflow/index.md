
# FCM solver workflow (Schema)

`ogc.hosted.seadots.fcm-workflow` *v0.1*

SeaDOTs Catalog Workflow profile for the fuzzy-cognitive-map solver: the workflow record that consumes a map and produces solutions or sequences. Declares the activation functions the solver actually implements, the fixed inference rule, and the execution parameters that exist only as code arguments and are therefore absent from every serialised artefact.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# FCM solver workflow

SeaDOTs Catalog Workflow profile for the fuzzy-cognitive-map solver of
[FuzzyCognitiveMapTools.jl](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl)
v0.1.0: the record that makes the solver discoverable as the step between a map (input)
and its solutions or sequences (output).

It iterates `x ← f(Wᵀx)` from many random initial states, clusters the endpoints that
agree within tolerance, and reports one representative equilibrium per cluster with its
componentwise spread.

## Why this block exists

A map is self-contained: it carries its own activation specification, so nothing about
the *function being iterated* has to be supplied at run time. That sounds like it makes a
workflow record unnecessary. It does the opposite.

Because the map carries everything it can carry, everything that distinguishes one run
from another lives **only as Julia keyword arguments** and is serialised nowhere — not in
the map, not in the solution, not in the sequence. Take the worked solution of the
researcher-proposal map: it cannot be reproduced from the published artefacts, because
nothing in them records that 1000 trials were run, from states drawn in `[0, 1]` and
clamped to `[0.1, 0.9]`, capped at 100 iterations, converged at `1e-10` and clustered at
`1e-6`.

The `solver` object is where those go. It also declares the two things a consumer cannot
infer from the data model at all: which activation functions are implemented, and which
inference rule is applied.

## What the solver can actually run

The activation scheme names ten concepts, because it names what the *FCM literature and
tool ecosystem* use. This solver implements **three** of them — the three branches of
`to_proc`:

| concept | upstream label | computes |
| --- | --- | --- |
| `fcmact:logistic` | `"logistic"` | `a / (1 + exp(−λ(x − b)))` |
| `fcmact:logistic-of-square` | `"gaussian"` | `a / (1 + exp(−λ(x − b)²))` |
| `fcmact:offset` | `"other"` | `x + a` |

Anything else raises `"Unknown activation function"` at load time. A map naming
`fcmact:hyperbolic-tangent` is perfectly well-formed and simply cannot be run here, which
is exactly the mismatch `supportedActivation` exists to let a catalog detect before
dispatch rather than after.

The label correction is visible in that table: upstream `"gaussian"` appears as
`logistic-of-square` because that is what the code computes — a logistic of the squared
deviation, not a bell curve. See `ogc.hosted.seadots.fcm-activation-scheme`.

`inferenceRule` is `kosko` and nothing else: `single_fcm_trial` hard-codes `mul!(x_next,
W', x)` with no parameter to select another rule. It is declared as an enum rather than a
constant so a record describing a later release can say something different without a
schema change.

## Three things to know before trusting a run

**The execution parameters cannot currently be set.** `run_trials` calls
`single_fcm_trial(fcm)` with no overrides and carries the comment `# TODO parameters to
be passed to single_fcm_trial`. So through the public entry point every run uses the
compiled defaults, and the values in `executionParameters` describe what *did* happen
rather than what was chosen. Recording them is still worth doing — they are what a
reproduction needs — but a record claiming non-default values for v0.1.0 is describing
something the public API cannot produce.

**Trials that never converged are still counted.** `run_trials` pushes every trial's
endpoint into the clustering regardless of `trial.b_converged`, so a trial that exhausted
`maxIterations` with a large residual contributes to a centroid and inflates the matching
`maxdists`. Combined with `b_success` never being set false, this makes `maxdists` the
only real quality signal a consumer has. See `ogc.hosted.seadots.fcm-solution`.

**The sampling range is wider than the clamp range.** `x0Range` is `[0, 1]` and
`x0ClampRange` is `[0.1, 0.9]`, and the clamp is applied after sampling. The extremes of
the sampling range are therefore never explored: any draw below 0.1 or above 0.9 collapses
onto the boundary. Whether that is deliberate — keeping starts off the saturated tails of
the logistic — or an artefact of two defaults chosen independently is worth asking
upstream. Both fields are declared so a record cannot hide the discrepancy.

## Refinement runs under different settings

The optional second pass (`refine_centroid_fcm`) re-solves from each cluster mean to
sharpen the centroid, and it does **not** inherit the trial settings: it uses 3000
iterations, tolerance `1e-13`, and clamp range `[0, 1]` — the full range, not the narrowed
one. If the refined point lands further than `checkTolerance` from the cluster mean the
run `error`s out rather than warning. The `refinement` object records these separately for
that reason; folding them into `executionParameters` would assert a single set of settings
that does not exist.

## JSON-LD projection

`solver` maps to `fcm:solverCapability`, `inferenceRule` and `supportedActivation` to
`fcm:inferenceRule` and `fcm:supportsActivation` (both resolving to scheme IRIs), and
`stochasticMapsSupported` to `fcm:supportsStochasticMaps`. `fcm:SolverCapabilityShape`
checks that a capability names at least one activation function and exactly one inference
rule — the failure mode that would let a map be routed to a solver that cannot run it.

`executionParameters` and `refinement` are **not** mapped. They are numeric run settings
with no ontology terms behind them, and minting a dozen datatype properties to hold
values that the upstream API cannot yet vary would be modelling ahead of the code. They
are schema-validated and left out of RDF, which is the same call made for
`activation_spec.*.params` in `ogc.hosted.seadots.fcm`. Revisit when `fcm-execution` is
written against a real run.

## Relationship to other blocks

| | |
| --- | --- |
| `catalog-workflow` | the generic record profiled here |
| `fcm` | the input this workflow consumes |
| `fcm-solution`, `fcm-sequence` | the outputs it produces |
| `fcm-activation-scheme` | the vocabulary `supportedActivation` and `inferenceRule` draw on |
| `catalog-execution` | where a *particular* run would be recorded — deferred until one exists |

## Deferred

`fcm-execution` (a `catalog-execution` profile) is not written. It should be, once there
is a real run to describe: the execution record is where the parameter values actually
used, the input map's identifier and the resulting solution's identifier belong, and
writing it against a hypothetical run would invent all three. `fcm-process` (an OGC API
Processes description) waits on the solver getting an endpoint; today it is a library, not
a service.

## Examples

### FuzzyCognitiveMapTools.jl solver
#### json
```json
{
  "@context": [
    "https://ogcincubator.github.io/geodcat-ogcapi-records/build/annotated/geo/geodcat/geodcat-records/context.jsonld",
    "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-workflow/context.jsonld"
  ],
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/workflow/fcm-solver",
  "type": "Feature",
  "itemType": "record",
  "conformsTo": [
    "https://docs.ogc.org/is/20-004/20-004.html",
    "http://www.w3.org/TR/prov-o/"
  ],
  "geometry": null,
  "properties": {
    "title": "Fuzzy cognitive map solver (FuzzyCognitiveMapTools.jl)",
    "description": "Iterates a fuzzy cognitive map from many random initial states until each trial converges, clusters the endpoints that agree within tolerance, and reports one representative equilibrium per cluster with its componentwise spread. Applied stepwise over a time-indexed series of maps it produces a sequence.",
    "type": "Workflow",
    "applicationCategory": "Model",
    "version": "0.1.0",
    "method": "Iterate x <- f(transpose(W) x) from num_trials random initial states; cluster the converged endpoints; report per-cluster centroids and componentwise spread.",
    "softwareVersion": "0.1.0",
    "programmingLanguage": "Julia",
    "solver": {
      "inferenceRule": "kosko",
      "supportedActivation": [
        "https://w3id.org/ogc/hosted/seadots/fcm/activation/logistic",
        "https://w3id.org/ogc/hosted/seadots/fcm/activation/logistic-of-square",
        "https://w3id.org/ogc/hosted/seadots/fcm/activation/offset"
      ],
      "executionParameters": {
        "numTrials": 1000,
        "x0Range": [0.0, 1.0],
        "x0ClampRange": [0.1, 0.9],
        "maxIterations": 100,
        "convergenceTolerance": 1.0e-10,
        "clusteringTolerance": 1.0e-6
      },
      "refinement": {
        "enabled": true,
        "maxIterations": 3000,
        "convergenceTolerance": 1.0e-13,
        "x0ClampRange": [0.0, 1.0],
        "checkTolerance": 1.0e-6
      },
      "stochasticMapsSupported": false
    },
    "inputs": [
      {
        "profileId": "ogc.hosted.seadots.fcm",
        "required": true,
        "role": "map",
        "description": "The fuzzy cognitive map to solve. Self-contained: it carries its own activation specification."
      }
    ],
    "outputs": [
      {
        "profileId": "ogc.hosted.seadots.fcm-solution",
        "required": true,
        "role": "equilibria",
        "description": "Equilibria of one map. Index-aligned with that map's vertex order and uninterpretable without it."
      },
      {
        "profileId": "ogc.hosted.seadots.fcm-sequence",
        "required": false,
        "role": "sequence",
        "description": "Produced only when the solver is applied stepwise over a time-indexed series of maps."
      }
    ],
    "keywords": [
      "fuzzy-cognitive-map",
      "participatory-modelling",
      "digital-twin",
      "open-science"
    ],
    "license": "https://creativecommons.org/licenses/by/4.0/"
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.fcm-workflow",
      "type": "application/schema+json"
    },
    {
      "rel": "related",
      "href": "https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl",
      "type": "text/html",
      "title": "FuzzyCognitiveMapTools.jl source repository"
    }
  ]
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: FCM solver workflow
description: 'SeaDOTs Catalog Workflow profile for the fuzzy-cognitive-map solver
  of FuzzyCognitiveMapTools.jl: the record that makes the solver discoverable as the
  step between a map (input) and its solutions or sequences (output).

  The profile exists for one reason. A map is self-contained -- it carries its own
  activation specification -- so the ONLY thing that distinguishes one run from another
  is a set of parameters that live exclusively as Julia keyword arguments and are
  serialised nowhere. Without them a solution is not reproducible. The `solver` object
  declares them, together with the two things a consumer cannot discover from the
  data model: which activation functions are actually implemented, and which inference
  rule is applied.

  '
allOf:
- $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-workflow/schema.yaml
properties:
  properties:
    type: object
    required:
    - solver
    properties:
      type:
        const: Workflow
        x-jsonld-id: '@type'
      solver:
        type: object
        description: 'What this solver does and how it may be parameterised. Values
          reflect FuzzyCognitiveMapTools.jl v0.1.0 and should be re-checked against
          the release the record describes.

          '
        required:
        - inferenceRule
        - supportedActivation
        properties:
          inferenceRule:
            type: string
            enum:
            - kosko
            description: 'The update applied at each iteration. Only `kosko` -- classic
              f(transpose(W) x) -- exists: it is hard-coded in `single_fcm_trial`
              with no parameter to select another. Declared as an enum rather than
              a constant so that a record describing a later release can say something
              different without a schema change.

              '
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/inferenceRule
            x-jsonld-type: '@vocab'
          supportedActivation:
            type: array
            minItems: 1
            uniqueItems: true
            description: 'Concepts of ogc.hosted.seadots.fcm-activation-scheme this
              solver can actually execute. A map whose `activation_spec.label` resolves
              outside this list will be rejected at load time -- `to_proc` raises
              "Unknown activation function".

              The three listed below are the whole of v0.1.0. Note that the upstream
              label "gaussian" appears here as `logistic-of-square`, because that
              is what the implementation computes; see the activation scheme block.

              '
            items:
              type: string
              enum:
              - https://w3id.org/ogc/hosted/seadots/fcm/activation/logistic
              - https://w3id.org/ogc/hosted/seadots/fcm/activation/logistic-of-square
              - https://w3id.org/ogc/hosted/seadots/fcm/activation/offset
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/supportsActivation
            x-jsonld-type: '@id'
            x-jsonld-container: '@set'
          executionParameters:
            type: object
            description: 'The parameters that are NOT in any serialised artefact.
              Each carries the default compiled into v0.1.0; a record for a specific
              run should state the value actually used. See description.md on why
              several of these cannot currently be set at all through the public entry
              point.

              '
            properties:
              numTrials:
                type: integer
                minimum: 1
                default: 1000
                description: Number of randomly-started trials clustered into equilibria
                  (`run_trials`).
              x0Range:
                $ref: '#/$defs/Interval'
                default:
                - 0.0
                - 1.0
                description: Range the random initial state is drawn from.
              x0ClampRange:
                $ref: '#/$defs/Interval'
                default:
                - 0.1
                - 0.9
                description: 'Range the initial state is clamped to after sampling.
                  Note this is NARROWER than `x0Range`, so the extremes of the sampling
                  range are never actually explored.

                  '
              maxIterations:
                type: integer
                minimum: 1
                default: 100
                description: 'Iteration cap per trial. A trial that hits it is NOT
                  discarded; see description.md.

                  '
              convergenceTolerance:
                type: number
                exclusiveMinimum: 0
                default: 1.0e-10
                description: Residual below which a trial is declared converged.
              clusteringTolerance:
                type: number
                exclusiveMinimum: 0
                default: 1.0e-06
                description: 'Distance within which two trial endpoints are treated
                  as the same equilibrium. Must be larger than the supremum of the
                  terminal residual, per the upstream docstring.

                  '
            additionalProperties: false
          refinement:
            type: object
            description: 'Optional second pass that re-solves from each cluster mean
              to sharpen the centroid (`refine_centroid_fcm`). It runs with its own
              hard-coded settings, which differ from the trial settings above.

              '
            properties:
              enabled:
                type: boolean
                default: false
              maxIterations:
                type: integer
                default: 3000
              convergenceTolerance:
                type: number
                default: 1.0e-13
              x0ClampRange:
                $ref: '#/$defs/Interval'
                default:
                - 0.0
                - 1.0
              checkTolerance:
                type: number
                default: 1.0e-06
                description: 'A refined centroid further than this from the cluster
                  mean is an error, not a warning: the run aborts.

                  '
            additionalProperties: false
          stochasticMapsSupported:
            type: boolean
            default: false
            description: 'Whether the solver accepts maps with distribution-valued
              edge weights. False for v0.1.0, which has no serialisation for them
              at all.

              '
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/supportsStochasticMaps
            x-jsonld-type: http://www.w3.org/2001/XMLSchema#boolean
        additionalProperties: true
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/solverCapability
    x-jsonld-id: '@nest'
$defs:
  Interval:
    type: array
    description: A closed interval [lower, upper], serialised as a two-element array.
    minItems: 2
    maxItems: 2
    items:
      type: number
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
  FeatureCollection: https://purl.org/geojson/vocab#FeatureCollection
  GeometryCollection: https://purl.org/geojson/vocab#GeometryCollection
  LineString: https://purl.org/geojson/vocab#LineString
  MultiLineString: https://purl.org/geojson/vocab#MultiLineString
  MultiPoint: https://purl.org/geojson/vocab#MultiPoint
  MultiPolygon: https://purl.org/geojson/vocab#MultiPolygon
  Point: https://purl.org/geojson/vocab#Point
  Polygon: https://purl.org/geojson/vocab#Polygon
  features:
    x-jsonld-container: '@set'
    x-jsonld-id: https://purl.org/geojson/vocab#features
  id: '@id'
  geometry:
    x-jsonld-context:
      coordinates:
        '@container': '@list'
        '@id': https://purl.org/geojson/vocab#coordinates
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
  bbox:
    x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#bbox
  links:
    x-jsonld-context:
      rel:
        '@context':
          '@base': http://www.iana.org/assignments/relation/
        '@id': http://www.iana.org/assignments/relation
        '@type': '@id'
      type: http://purl.org/dc/terms/type
      hreflang: http://purl.org/dc/terms/language
      title: http://www.w3.org/2000/01/rdf-schema#label
      length: http://purl.org/dc/terms/extent
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
  conformsTo:
    x-jsonld-container: '@set'
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
  time: http://purl.org/dc/terms/temporal
  linkTemplates:
    x-jsonld-context:
      rel:
        '@context':
          '@base': http://www.iana.org/assignments/relation/
        '@id': http://www.iana.org/assignments/relation
        '@type': '@id'
      type: http://purl.org/dc/terms/format
      hreflang: http://purl.org/dc/terms/language
      title: http://www.w3.org/2000/01/rdf-schema#label
      length: http://purl.org/dc/terms/extent
      uriTemplate:
        '@type': http://www.w3.org/2001/XMLSchema#string
        '@id': https://www.opengis.net/def/ogc-api/records/uriTemplate
      varBase: https://www.opengis.net/def/ogc-api/records/varBase
      variables:
        '@id': https://www.opengis.net/def/ogc-api/records/hasVariable
        '@container': '@index'
        '@index': http://purl.org/dc/terms/identifier
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/hasLinkTemplate
  created: http://purl.org/dc/terms/created
  updated: http://purl.org/dc/terms/modified
  title:
    x-jsonld-container: '@set'
    x-jsonld-id: http://purl.org/dc/terms/title
  description:
    x-jsonld-container: '@set'
    x-jsonld-id: http://purl.org/dc/terms/description
  keywords:
    x-jsonld-container: '@set'
    x-jsonld-id: http://www.w3.org/ns/dcat#keyword
  language:
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/language
    x-jsonld-context:
      code: https://www.opengis.net/def/ogc-api/records/languageCode
      name: http://www.w3.org/2004/02/skos/core#prefLabel
  languages:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/languages
    x-jsonld-context:
      code: https://www.opengis.net/def/ogc-api/records/languageCode
      name: http://www.w3.org/2004/02/skos/core#prefLabel
  resourceLanguages:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/resourceLanguages
    x-jsonld-context:
      code: https://www.opengis.net/def/ogc-api/records/languageCode
      name: http://www.w3.org/2004/02/skos/core#prefLabel
  externalIds:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/scopedIdentifier
    x-jsonld-context:
      scheme: https://www.opengis.net/def/ogc-api/records/scheme
      value: https://www.opengis.net/def/ogc-api/records/id
  themes:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/themes
    x-jsonld-context:
      concepts:
        '@id': https://www.opengis.net/def/ogc-api/records/concept
        '@context':
          id:
            '@type': http://www.w3.org/2001/XMLSchema#string
            '@id': https://www.opengis.net/def/ogc-api/records/conceptID
          url:
            '@type': '@id'
            '@id': http://www.w3.org/ns/dcat#theme
      scheme: https://www.opengis.net/def/ogc-api/records/scheme
  formats:
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/format
    x-jsonld-context:
      name: https://www.opengis.net/def/ogc-api/records/name
  contacts:
    x-jsonld-container: '@set'
    x-jsonld-id: http://www.w3.org/ns/dcat#contactPoint
    x-jsonld-type: '@id'
  license: http://purl.org/dc/terms/license
  accessrights: http://purl.org/dc/terms/accessRights
  variables:
    x-jsonld-container: '@id'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/hasVariable
    x-jsonld-context:
      '@base': http://example.com/variables/
      '@vocab': https://www.opengis.net/def/ogc-api/records/
  wasInfluencedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasInfluencedBy
    x-jsonld-type: '@id'
  qualifiedInfluence:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInfluence
    x-jsonld-type: '@id'
  hadMember:
    x-jsonld-id: http://www.w3.org/ns/prov#hadMember
    x-jsonld-type: '@id'
  provType: '@type'
  featureType: '@type'
  entityType: '@type'
  has_provenance:
    x-jsonld-id: http://purl.org/dc/terms/provenance
    x-jsonld-type: '@id'
  wasGeneratedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
    x-jsonld-type: '@id'
  wasAttributedTo:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAttributedTo
    x-jsonld-type: '@id'
  wasDerivedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
    x-jsonld-type: '@id'
  alternateOf:
    x-jsonld-id: http://www.w3.org/ns/prov#alternateOf
    x-jsonld-type: '@id'
  hadPrimarySource:
    x-jsonld-id: http://www.w3.org/ns/prov#hadPrimarySource
    x-jsonld-type: '@id'
  specializationOf:
    x-jsonld-id: http://www.w3.org/ns/prov#specializationOf
    x-jsonld-type: '@id'
  wasInvalidatedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasInvalidatedBy
    x-jsonld-type: '@id'
  wasQuotedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasQuotedFrom
    x-jsonld-type: '@id'
  wasRevisionOf:
    x-jsonld-id: http://www.w3.org/ns/prov#wasRevisionOf
    x-jsonld-type: '@id'
  generatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#generatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  invalidatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#invalidatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  value: http://www.w3.org/ns/prov#value
  qualifiedPrimarySource:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedPrimarySource
    x-jsonld-type: '@id'
  qualifiedQuotation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedQuotation
    x-jsonld-type: '@id'
  qualifiedRevision:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedRevision
    x-jsonld-type: '@id'
  atLocation:
    x-jsonld-id: http://www.w3.org/ns/prov#atLocation
    x-jsonld-type: '@id'
  qualifiedGeneration:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedGeneration
    x-jsonld-type: '@id'
  qualifiedInvalidation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInvalidation
    x-jsonld-type: '@id'
  qualifiedDerivation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedDerivation
    x-jsonld-type: '@id'
  qualifiedAttribution:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedAttribution
    x-jsonld-type: '@id'
  activityType: '@type'
  agentType: '@type'
  Activity: http://www.w3.org/ns/prov#Activity
  ActivityInfluence: http://www.w3.org/ns/prov#ActivityInfluence
  Agent: http://www.w3.org/ns/prov#Agent
  AgentInfluence: http://www.w3.org/ns/prov#AgentInfluence
  Association: http://www.w3.org/ns/prov#Association
  Attribution: http://www.w3.org/ns/prov#Attribution
  Bundle: http://www.w3.org/ns/prov#Bundle
  Collection: http://www.w3.org/ns/prov#Collection
  Communication: http://www.w3.org/ns/prov#Communication
  Delegation: http://www.w3.org/ns/prov#Delegation
  Derivation: http://www.w3.org/ns/prov#Derivation
  EmptyCollection: http://www.w3.org/ns/prov#EmptyCollection
  End: http://www.w3.org/ns/prov#End
  Entity: http://www.w3.org/ns/prov#Entity
  EntityInfluence: http://www.w3.org/ns/prov#EntityInfluence
  Generation: http://www.w3.org/ns/prov#Generation
  Influence: http://www.w3.org/ns/prov#Influence
  InstantaneousEvent: http://www.w3.org/ns/prov#InstantaneousEvent
  Invalidation: http://www.w3.org/ns/prov#Invalidation
  Location: http://www.w3.org/ns/prov#Location
  Organization: http://www.w3.org/ns/prov#Organization
  Person: http://www.w3.org/ns/prov#Person
  Plan: http://www.w3.org/ns/prov#Plan
  PrimarySource: http://www.w3.org/ns/prov#PrimarySource
  Quotation: http://www.w3.org/ns/prov#Quotation
  Revision: http://www.w3.org/ns/prov#Revision
  Role: http://www.w3.org/ns/prov#Role
  SoftwareAgent: http://www.w3.org/ns/prov#SoftwareAgent
  Start: http://www.w3.org/ns/prov#Start
  Usage: http://www.w3.org/ns/prov#Usage
  ServiceDescription: http://www.w3.org/ns/prov#ServiceDescription
  DirectQueryService: http://www.w3.org/ns/prov#DirectQueryService
  Accept: http://www.w3.org/ns/prov#Accept
  Contribute: http://www.w3.org/ns/prov#Contribute
  Contributor: http://www.w3.org/ns/prov#Contributor
  Copyright: http://www.w3.org/ns/prov#Copyright
  Create: http://www.w3.org/ns/prov#Create
  Creator: http://www.w3.org/ns/prov#Creator
  Modify: http://www.w3.org/ns/prov#Modify
  Publish: http://www.w3.org/ns/prov#Publish
  Publisher: http://www.w3.org/ns/prov#Publisher
  Replace: http://www.w3.org/ns/prov#Replace
  RightsAssignment: http://www.w3.org/ns/prov#RightsAssignment
  RightsHolder: http://www.w3.org/ns/prov#RightsHolder
  Submit: http://www.w3.org/ns/prov#Submit
  Dictionary: http://www.w3.org/ns/prov#Dictionary
  EmptyDictionary: http://www.w3.org/ns/prov#EmptyDictionary
  KeyEntityPair: http://www.w3.org/ns/prov#KeyEntityPair
  Insertion: http://www.w3.org/ns/prov#Insertion
  Removal: http://www.w3.org/ns/prov#Removal
  atTime:
    x-jsonld-id: http://www.w3.org/ns/prov#atTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  endedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#endedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  startedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#startedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  provenanceUriTemplate: http://www.w3.org/ns/prov#provenanceUriTemplate
  pairKey:
    x-jsonld-id: http://www.w3.org/ns/prov#pairKey
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  removedKey:
    x-jsonld-id: http://www.w3.org/ns/prov#removedKey
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  actedOnBehalfOf:
    x-jsonld-id: http://www.w3.org/ns/prov#actedOnBehalfOf
    x-jsonld-type: '@id'
  agent:
    x-jsonld-id: http://www.w3.org/ns/prov#agent
    x-jsonld-type: '@id'
  entity:
    x-jsonld-id: http://www.w3.org/ns/prov#entity
    x-jsonld-type: '@id'
  generated:
    x-jsonld-id: http://www.w3.org/ns/prov#generated
    x-jsonld-type: '@id'
  hadActivity:
    x-jsonld-id: http://www.w3.org/ns/prov#hadActivity
    x-jsonld-type: '@id'
  activity:
    x-jsonld-id: http://www.w3.org/ns/prov#activity
    x-jsonld-type: '@id'
  hadGeneration:
    x-jsonld-id: http://www.w3.org/ns/prov#hadGeneration
    x-jsonld-type: '@id'
  hadPlan:
    x-jsonld-id: http://www.w3.org/ns/prov#hadPlan
    x-jsonld-type: '@id'
  hadRole:
    x-jsonld-id: http://www.w3.org/ns/prov#hadRole
    x-jsonld-type: '@id'
  hadUsage:
    x-jsonld-id: http://www.w3.org/ns/prov#hadUsage
    x-jsonld-type: '@id'
  influenced:
    x-jsonld-id: http://www.w3.org/ns/prov#influenced
    x-jsonld-type: '@id'
  influencer:
    x-jsonld-id: http://www.w3.org/ns/prov#influencer
    x-jsonld-type: '@id'
  invalidated:
    x-jsonld-id: http://www.w3.org/ns/prov#invalidated
    x-jsonld-type: '@id'
  qualifiedAssociation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedAssociation
    x-jsonld-type: '@id'
  qualifiedCommunication:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedCommunication
    x-jsonld-type: '@id'
  qualifiedDelegation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedDelegation
    x-jsonld-type: '@id'
  qualifiedEnd:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedEnd
    x-jsonld-type: '@id'
  qualifiedStart:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedStart
    x-jsonld-type: '@id'
  qualifiedUsage:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedUsage
    x-jsonld-type: '@id'
  used:
    x-jsonld-id: http://www.w3.org/ns/prov#used
    x-jsonld-type: '@id'
  wasAssociatedWith:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAssociatedWith
    x-jsonld-type: '@id'
  wasEndedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasEndedBy
    x-jsonld-type: '@id'
  wasInformedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasInformedBy
    x-jsonld-type: '@id'
  wasStartedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasStartedBy
    x-jsonld-type: '@id'
  has_anchor:
    x-jsonld-id: http://www.w3.org/ns/prov#has_anchor
    x-jsonld-type: '@id'
  has_query_service:
    x-jsonld-id: http://www.w3.org/ns/prov#has_query_service
    x-jsonld-type: '@id'
  describesService:
    x-jsonld-id: http://www.w3.org/ns/prov#describesService
    x-jsonld-type: '@id'
  pingback:
    x-jsonld-id: http://www.w3.org/ns/prov#pingback
    x-jsonld-type: '@id'
  dictionary:
    x-jsonld-id: http://www.w3.org/ns/prov#dictionary
    x-jsonld-type: '@id'
  derivedByInsertionFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#derivedByInsertionFrom
    x-jsonld-type: '@id'
  derivedByRemovalFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#derivedByRemovalFrom
    x-jsonld-type: '@id'
  insertedKeyEntityPair:
    x-jsonld-id: http://www.w3.org/ns/prov#insertedKeyEntityPair
    x-jsonld-type: '@id'
  hadDictionaryMember:
    x-jsonld-id: http://www.w3.org/ns/prov#hadDictionaryMember
    x-jsonld-type: '@id'
  pairEntity:
    x-jsonld-id: http://www.w3.org/ns/prov#pairEntity
    x-jsonld-type: '@id'
  qualifiedInsertion:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInsertion
    x-jsonld-type: '@id'
  qualifiedRemoval:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedRemoval
    x-jsonld-type: '@id'
  asInBundle:
    x-jsonld-id: http://www.w3.org/ns/prov#asInBundle
    x-jsonld-type: '@id'
  mentionOf:
    x-jsonld-id: http://www.w3.org/ns/prov#mentionOf
    x-jsonld-type: '@id'
  name: http://www.w3.org/2000/01/rdf-schema#label
  href:
    x-jsonld-type: '@id'
    x-jsonld-id: http://www.w3.org/ns/oa#hasTarget
  rights: http://www.w3.org/ns/dcat#rights
  Workflow: http://www.w3.org/ns/prov#Plan
  applicationCategory: https://schema.org/applicationCategory
  version: http://purl.org/dc/terms/hasVersion
  method: http://purl.org/dc/terms/method
  softwareVersion: https://schema.org/softwareVersion
  programmingLanguage: https://schema.org/programmingLanguage
  applicationPackage:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#applicationPackage
    x-jsonld-type: '@id'
  inputs:
    x-jsonld-context:
      profileId:
        '@id': http://purl.org/dc/terms/conformsTo
        '@type': '@id'
      required:
        '@id': https://w3id.org/ogc/hosted/seadots/catalog#required
        '@type': http://www.w3.org/2001/XMLSchema#boolean
      role: https://w3id.org/ogc/hosted/seadots/catalog#role
    x-jsonld-id: https://w3id.org/apkg/terms/inputs
    x-jsonld-container: '@set'
  outputs:
    x-jsonld-context:
      profileId:
        '@id': http://purl.org/dc/terms/conformsTo
        '@type': '@id'
      required:
        '@id': https://w3id.org/ogc/hosted/seadots/catalog#required
        '@type': http://www.w3.org/2001/XMLSchema#boolean
      role: https://w3id.org/ogc/hosted/seadots/catalog#role
    x-jsonld-id: https://w3id.org/apkg/terms/outputs
    x-jsonld-container: '@set'
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/catalog#
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  dct: http://purl.org/dc/terms/
  rec: https://www.opengis.net/def/ogc-api/records/
  xsd: http://www.w3.org/2001/XMLSchema#
  dcat: http://www.w3.org/ns/dcat#
  skos: http://www.w3.org/2004/02/skos/core#
  prov: http://www.w3.org/ns/prov#
  oa: http://www.w3.org/ns/oa#
  schema: https://schema.org/
  seadots: https://w3id.org/ogc/hosted/seadots/catalog#
  apkg: https://w3id.org/apkg/terms/
  fcm: https://w3id.org/ogc/hosted/seadots/fcm/
  fcmact: https://w3id.org/ogc/hosted/seadots/fcm/activation/
  owl: http://www.w3.org/2002/07/owl#
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  w3ctime: http://www.w3.org/2006/time#
  dctype: http://purl.org/dc/dcmitype/
  vcard: http://www.w3.org/2006/vcard/ns#
  foaf: http://xmlns.com/foaf/0.1/
  thns: https://w3id.org/ogc/stac/themes/
  dcterms: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-workflow/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-workflow/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/catalog#",
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
        "type": "dct:type",
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
          "@id": "rec:concept",
          "@context": {
            "id": {
              "@type": "xsd:string",
              "@id": "rec:conceptID"
            },
            "url": {
              "@type": "@id",
              "@id": "dcat:theme"
            }
          }
        },
        "scheme": "rec:scheme"
      }
    },
    "formats": {
      "@id": "rec:format",
      "@context": {
        "name": "rec:name"
      }
    },
    "contacts": {
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "license": "dct:license",
    "accessrights": "dct:accessRights",
    "variables": {
      "@container": "@id",
      "@id": "rec:hasVariable",
      "@context": {
        "@base": "http://example.com/variables/",
        "@vocab": "https://www.opengis.net/def/ogc-api/records/"
      }
    },
    "wasInfluencedBy": {
      "@id": "prov:wasInfluencedBy",
      "@type": "@id"
    },
    "qualifiedInfluence": {
      "@id": "prov:qualifiedInfluence",
      "@type": "@id"
    },
    "hadMember": {
      "@id": "prov:hadMember",
      "@type": "@id"
    },
    "provType": "@type",
    "featureType": "@type",
    "entityType": "@type",
    "has_provenance": {
      "@id": "dct:provenance",
      "@type": "@id"
    },
    "wasGeneratedBy": {
      "@id": "prov:wasGeneratedBy",
      "@type": "@id"
    },
    "wasAttributedTo": {
      "@id": "prov:wasAttributedTo",
      "@type": "@id"
    },
    "wasDerivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@type": "@id"
    },
    "alternateOf": {
      "@id": "prov:alternateOf",
      "@type": "@id"
    },
    "hadPrimarySource": {
      "@id": "prov:hadPrimarySource",
      "@type": "@id"
    },
    "specializationOf": {
      "@id": "prov:specializationOf",
      "@type": "@id"
    },
    "wasInvalidatedBy": {
      "@id": "prov:wasInvalidatedBy",
      "@type": "@id"
    },
    "wasQuotedFrom": {
      "@id": "prov:wasQuotedFrom",
      "@type": "@id"
    },
    "wasRevisionOf": {
      "@id": "prov:wasRevisionOf",
      "@type": "@id"
    },
    "generatedAtTime": {
      "@id": "prov:generatedAtTime",
      "@type": "xsd:dateTime"
    },
    "invalidatedAtTime": {
      "@id": "prov:invalidatedAtTime",
      "@type": "xsd:dateTime"
    },
    "value": "prov:value",
    "qualifiedPrimarySource": {
      "@id": "prov:qualifiedPrimarySource",
      "@type": "@id"
    },
    "qualifiedQuotation": {
      "@id": "prov:qualifiedQuotation",
      "@type": "@id"
    },
    "qualifiedRevision": {
      "@id": "prov:qualifiedRevision",
      "@type": "@id"
    },
    "atLocation": {
      "@id": "prov:atLocation",
      "@type": "@id"
    },
    "qualifiedGeneration": {
      "@id": "prov:qualifiedGeneration",
      "@type": "@id"
    },
    "qualifiedInvalidation": {
      "@id": "prov:qualifiedInvalidation",
      "@type": "@id"
    },
    "qualifiedDerivation": {
      "@id": "prov:qualifiedDerivation",
      "@type": "@id"
    },
    "qualifiedAttribution": {
      "@id": "prov:qualifiedAttribution",
      "@type": "@id"
    },
    "activityType": "@type",
    "agentType": "@type",
    "Activity": "prov:Activity",
    "ActivityInfluence": "prov:ActivityInfluence",
    "Agent": "prov:Agent",
    "AgentInfluence": "prov:AgentInfluence",
    "Association": "prov:Association",
    "Attribution": "prov:Attribution",
    "Bundle": "prov:Bundle",
    "Collection": "prov:Collection",
    "Communication": "prov:Communication",
    "Delegation": "prov:Delegation",
    "Derivation": "prov:Derivation",
    "EmptyCollection": "prov:EmptyCollection",
    "End": "prov:End",
    "Entity": "prov:Entity",
    "EntityInfluence": "prov:EntityInfluence",
    "Generation": "prov:Generation",
    "Influence": "prov:Influence",
    "InstantaneousEvent": "prov:InstantaneousEvent",
    "Invalidation": "prov:Invalidation",
    "Location": "prov:Location",
    "Organization": "prov:Organization",
    "Person": "prov:Person",
    "Plan": "prov:Plan",
    "PrimarySource": "prov:PrimarySource",
    "Quotation": "prov:Quotation",
    "Revision": "prov:Revision",
    "Role": "prov:Role",
    "SoftwareAgent": "prov:SoftwareAgent",
    "Start": "prov:Start",
    "Usage": "prov:Usage",
    "ServiceDescription": "prov:ServiceDescription",
    "DirectQueryService": "prov:DirectQueryService",
    "Accept": "prov:Accept",
    "Contribute": "prov:Contribute",
    "Contributor": "prov:Contributor",
    "Copyright": "prov:Copyright",
    "Create": "prov:Create",
    "Creator": "prov:Creator",
    "Modify": "prov:Modify",
    "Publish": "prov:Publish",
    "Publisher": "prov:Publisher",
    "Replace": "prov:Replace",
    "RightsAssignment": "prov:RightsAssignment",
    "RightsHolder": "prov:RightsHolder",
    "Submit": "prov:Submit",
    "Dictionary": "prov:Dictionary",
    "EmptyDictionary": "prov:EmptyDictionary",
    "KeyEntityPair": "prov:KeyEntityPair",
    "Insertion": "prov:Insertion",
    "Removal": "prov:Removal",
    "atTime": {
      "@id": "prov:atTime",
      "@type": "xsd:dateTime"
    },
    "endedAtTime": {
      "@id": "prov:endedAtTime",
      "@type": "xsd:dateTime"
    },
    "startedAtTime": {
      "@id": "prov:startedAtTime",
      "@type": "xsd:dateTime"
    },
    "provenanceUriTemplate": "prov:provenanceUriTemplate",
    "pairKey": {
      "@id": "prov:pairKey",
      "@type": "rdfs:Literal"
    },
    "removedKey": {
      "@id": "prov:removedKey",
      "@type": "rdfs:Literal"
    },
    "actedOnBehalfOf": {
      "@id": "prov:actedOnBehalfOf",
      "@type": "@id"
    },
    "agent": {
      "@id": "prov:agent",
      "@type": "@id"
    },
    "entity": {
      "@id": "prov:entity",
      "@type": "@id"
    },
    "generated": {
      "@id": "prov:generated",
      "@type": "@id"
    },
    "hadActivity": {
      "@id": "prov:hadActivity",
      "@type": "@id"
    },
    "activity": {
      "@id": "prov:activity",
      "@type": "@id"
    },
    "hadGeneration": {
      "@id": "prov:hadGeneration",
      "@type": "@id"
    },
    "hadPlan": {
      "@id": "prov:hadPlan",
      "@type": "@id"
    },
    "hadRole": {
      "@id": "prov:hadRole",
      "@type": "@id"
    },
    "hadUsage": {
      "@id": "prov:hadUsage",
      "@type": "@id"
    },
    "influenced": {
      "@id": "prov:influenced",
      "@type": "@id"
    },
    "influencer": {
      "@id": "prov:influencer",
      "@type": "@id"
    },
    "invalidated": {
      "@id": "prov:invalidated",
      "@type": "@id"
    },
    "qualifiedAssociation": {
      "@id": "prov:qualifiedAssociation",
      "@type": "@id"
    },
    "qualifiedCommunication": {
      "@id": "prov:qualifiedCommunication",
      "@type": "@id"
    },
    "qualifiedDelegation": {
      "@id": "prov:qualifiedDelegation",
      "@type": "@id"
    },
    "qualifiedEnd": {
      "@id": "prov:qualifiedEnd",
      "@type": "@id"
    },
    "qualifiedStart": {
      "@id": "prov:qualifiedStart",
      "@type": "@id"
    },
    "qualifiedUsage": {
      "@id": "prov:qualifiedUsage",
      "@type": "@id"
    },
    "used": {
      "@id": "prov:used",
      "@type": "@id"
    },
    "wasAssociatedWith": {
      "@id": "prov:wasAssociatedWith",
      "@type": "@id"
    },
    "wasEndedBy": {
      "@id": "prov:wasEndedBy",
      "@type": "@id"
    },
    "wasInformedBy": {
      "@id": "prov:wasInformedBy",
      "@type": "@id"
    },
    "wasStartedBy": {
      "@id": "prov:wasStartedBy",
      "@type": "@id"
    },
    "has_anchor": {
      "@id": "prov:has_anchor",
      "@type": "@id"
    },
    "has_query_service": {
      "@id": "prov:has_query_service",
      "@type": "@id"
    },
    "describesService": {
      "@id": "prov:describesService",
      "@type": "@id"
    },
    "pingback": {
      "@id": "prov:pingback",
      "@type": "@id"
    },
    "dictionary": {
      "@id": "prov:dictionary",
      "@type": "@id"
    },
    "derivedByInsertionFrom": {
      "@id": "prov:derivedByInsertionFrom",
      "@type": "@id"
    },
    "derivedByRemovalFrom": {
      "@id": "prov:derivedByRemovalFrom",
      "@type": "@id"
    },
    "insertedKeyEntityPair": {
      "@id": "prov:insertedKeyEntityPair",
      "@type": "@id"
    },
    "hadDictionaryMember": {
      "@id": "prov:hadDictionaryMember",
      "@type": "@id"
    },
    "pairEntity": {
      "@id": "prov:pairEntity",
      "@type": "@id"
    },
    "qualifiedInsertion": {
      "@id": "prov:qualifiedInsertion",
      "@type": "@id"
    },
    "qualifiedRemoval": {
      "@id": "prov:qualifiedRemoval",
      "@type": "@id"
    },
    "asInBundle": {
      "@id": "prov:asInBundle",
      "@type": "@id"
    },
    "mentionOf": {
      "@id": "prov:mentionOf",
      "@type": "@id"
    },
    "name": "rdfs:label",
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "rights": "dcat:rights",
    "Workflow": "prov:Plan",
    "applicationCategory": "schema:applicationCategory",
    "version": "dct:hasVersion",
    "method": "dct:method",
    "softwareVersion": "schema:softwareVersion",
    "programmingLanguage": "schema:programmingLanguage",
    "applicationPackage": {
      "@id": "seadots:applicationPackage",
      "@type": "@id"
    },
    "inputs": {
      "@context": {
        "profileId": {
          "@id": "dct:conformsTo",
          "@type": "@id"
        },
        "required": {
          "@id": "seadots:required",
          "@type": "xsd:boolean"
        },
        "role": "seadots:role"
      },
      "@id": "apkg:inputs",
      "@container": "@set"
    },
    "outputs": {
      "@context": {
        "profileId": {
          "@id": "dct:conformsTo",
          "@type": "@id"
        },
        "required": {
          "@id": "seadots:required",
          "@type": "xsd:boolean"
        },
        "role": "seadots:role"
      },
      "@id": "apkg:outputs",
      "@container": "@set"
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
    "schema": "https://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "seadots": "https://w3id.org/ogc/hosted/seadots/catalog#",
    "apkg": "https://w3id.org/apkg/terms/",
    "fcm": "https://w3id.org/ogc/hosted/seadots/fcm/",
    "fcmact": "fcm:activation/",
    "solver": {
      "@context": {
        "inferenceRule": {
          "@id": "fcm:inferenceRule",
          "@type": "@vocab"
        },
        "supportedActivation": {
          "@id": "fcm:supportsActivation",
          "@type": "@id",
          "@container": "@set"
        },
        "stochasticMapsSupported": {
          "@id": "fcm:supportsStochasticMaps",
          "@type": "xsd:boolean"
        }
      },
      "@id": "fcm:solverCapability"
    },
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-workflow/context.jsonld)

## Sources

* [FuzzyCognitiveMapTools.jl v0.1.0](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl)
* [FCM data specifications (dataspecs/fcm_dataspecs__20260630.md)](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl/-/blob/main/dataspecs/fcm_dataspecs__20260630.md)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/_staging/fcm-workflow`

