
# FCM time specification (Schema)

`ogc.hosted.seadots.fcm-timespec` *v0.1*

The four interchangeable ways a fuzzy cognitive map and its solution can be placed in time -- an instant, a week of a year, a month of a year, or an explicit interval -- as serialised by FuzzyCognitiveMapTools.jl. Discriminated on the 'type' field.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# FCM time specification

When a fuzzy cognitive map and the solution computed from it apply. This is the element
type of the `timespec_series` array of a sequence, factored out into its own block because
it is the one FCM structure with reuse value outside the FCM stack.

Four disjoint forms, discriminated on `type`, source-faithful to the `AbstractTimeSpec`
subtypes of
[FuzzyCognitiveMapTools.jl](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl)
v0.1.0 (`src/fcm/timespecs.jl`):

| `type` | fields | interval it denotes |
| --- | --- | --- |
| `pointtimespec` | `dt` | the instant itself, `[dt, dt]` |
| `weekofyeartimespec` | `year`, `week` | `[1 Jan + (week-1) weeks, + 1 week)` |
| `monthofyeartimespec` | `year`, `month` | the calendar month |
| `rangetimespec` | `start`, `stop` | `[start, stop)` |

Four forms rather than one exist because the SeaDOTs participatory survey rounds are not
yet committed to a reporting period; the upstream author states this explicitly. All four
reduce to a `(start, stop)` pair through `bounds`, so consumers that only need an interval
can normalise on ingest and ignore the distinction.

## Two things that are not what they look like

**`week` is not an ISO 8601 week.** `bounds(::WeekOfYearTimeSpec)` computes
`Date(year, 1, 1) + Week(week - 1)`, counting from 1 January rather than from the first
Thursday of the year. Week 1 therefore does not in general coincide with ISO week 1, and
week 53 begins on day 365 and runs past the end of the year. Anything mapping these onto
ISO weeks, or onto `time:` intervals, must use the upstream arithmetic, not a week-number
library.

**`dt`, `start` and `stop` are not `format: date-time`.** The Julia serialiser emits a
bare `DateTime`: no UTC offset, and a trailing fractional second —
`"2026-01-02T03:04:05.0"`. RFC 3339 requires an offset, so JSON Schema's `date-time`
format rejects every datetime this tool has ever written. Declaring the format would fail
the upstream example files, which is not a defect this block should paper over, so the
fields are declared as strings with a pattern that accepts the upstream form and a
properly zoned one alike. The block will not need revising when the defect is fixed
upstream.

The same lexical form **is** a valid `xsd:dateTime`, where the offset is optional, so the
RDF projection is unaffected and `fcm:instant`, `fcm:intervalStart` and `fcm:intervalStop`
keep their `xsd:dateTime` range. The divergence is purely between two datetime profiles of
differing strictness, which is worth knowing before someone "fixes" the context.

## Constraints this schema does not carry

That `start` precedes `stop` in a `rangetimespec` relates two sibling values and is not
expressible in JSON Schema. It is carried as a SHACL constraint by
`ogc.hosted.seadots.fcm-ontology`.

A stronger constraint applies to a *series* of these rather than to one: upstream
`Base.isless` **throws** `ArgumentError("cannot order overlapping time intervals")` when
two specs overlap, so a sequence's `timespec_series` must be pairwise non-overlapping to
be sortable at all. That is a constraint of `ogc.hosted.seadots.fcm-sequence`, recorded
there.

Two bounds in this schema are **additions**, not upstream rules: `week` 1..53 and `month`
1..12. Upstream both are bare `Int` with no validation. They are stated here because a
month of 13 has no interpretation under `bounds`, and 53 is the last week that still
begins within its year.

## JSON-LD projection

The `type` discriminator is mapped to `@type`, with the four upstream label strings
declared as terms resolving to the corresponding ontology classes — `"pointtimespec"` →
`fcm:PointTimeSpec` and so on. This works precisely because the discriminator is present
in the JSON: a JSON-LD context cannot inject an `rdf:type` that the document does not
carry, which is why the sibling `fcm` block has to target its SHACL shapes by property
instead. Here the type arrives honestly and every shape can target by class.

Every field of all four forms is mapped. There are no context gaps in this block.

## Relationship to other blocks

| | |
| --- | --- |
| `fcm-ontology` | `fcm:TimeSpec` and its four subclasses; the `start < stop` constraint |
| `fcm-sequence` | consumes this as the element type of `timespec_series` |
| `fcm` | the map that holds at the time this specifies |

## Source-property coverage

Every field of `PointTimeSpec`, `WeekOfYearTimeSpec`, `MonthOfYearTimeSpec` and
`RangeTimeSpec` is present. Nothing is dropped, nothing is renamed.

Note that the upstream `dataspecs` markdown documents `PointTimeSpec.t`, while the code
and every example file use `dt`. This block follows the code.

## Examples

### Instant
#### json
```json
{
    "type": "pointtimespec",
    "dt": "2026-01-02T03:04:05.0"
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-timespec/context.jsonld",
  "type": "pointtimespec",
  "dt": "2026-01-02T03:04:05.0"
}
```

#### ttl
```ttl
@prefix fcm: <https://w3id.org/ogc/hosted/seadots/fcm/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a fcm:PointTimeSpec ;
    fcm:instant "2026-01-02T03:04:05"^^xsd:dateTime .


```


### Week of year
#### json
```json
{
    "type": "weekofyeartimespec",
    "year": 2026,
    "week": 4
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-timespec/context.jsonld",
  "type": "weekofyeartimespec",
  "year": 2026,
  "week": 4
}
```

#### ttl
```ttl
@prefix fcm: <https://w3id.org/ogc/hosted/seadots/fcm/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a fcm:WeekOfYearTimeSpec ;
    fcm:week 4 ;
    fcm:year 2026 .


```


### Month of year
#### json
```json
{
    "type": "monthofyeartimespec",
    "year": 2026,
    "month": 2
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-timespec/context.jsonld",
  "type": "monthofyeartimespec",
  "year": 2026,
  "month": 2
}
```

#### ttl
```ttl
@prefix fcm: <https://w3id.org/ogc/hosted/seadots/fcm/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a fcm:MonthOfYearTimeSpec ;
    fcm:month 2 ;
    fcm:year 2026 .


```


### Explicit interval
#### json
```json
{
    "type": "rangetimespec",
    "start": "2026-05-01T00:00:00.0",
    "stop": "2026-06-02T00:00:00.0"
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-timespec/context.jsonld",
  "type": "rangetimespec",
  "start": "2026-05-01T00:00:00.0",
  "stop": "2026-06-02T00:00:00.0"
}
```

#### ttl
```ttl
@prefix fcm: <https://w3id.org/ogc/hosted/seadots/fcm/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a fcm:RangeTimeSpec ;
    fcm:intervalStart "2026-05-01T00:00:00"^^xsd:dateTime ;
    fcm:intervalStop "2026-06-02T00:00:00"^^xsd:dateTime .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: FCM time specification
description: 'When a fuzzy cognitive map and its solution apply. Four disjoint forms,
  discriminated on `type`, reflecting that participatory survey rounds are not yet
  committed to a single reporting period: an instant, a week of a year, a month of
  a year, or an explicit interval.

  This block describes ONE time specification. The `timespec_series` array of a sequence
  is a list of these; see ogc.hosted.seadots.fcm-sequence.

  '
oneOf:
- $ref: '#/$defs/PointTimeSpec'
- $ref: '#/$defs/WeekOfYearTimeSpec'
- $ref: '#/$defs/MonthOfYearTimeSpec'
- $ref: '#/$defs/RangeTimeSpec'
$defs:
  LocalOrZonedDateTime:
    type: string
    description: 'A date and time. NOT declared with `format: date-time`: the upstream
      Julia serialiser emits a bare `DateTime` with no UTC offset and a trailing fractional
      second, e.g. "2026-01-02T03:04:05.0", which RFC 3339 -- and therefore JSON Schema
      `date-time` -- rejects for the missing offset. The same lexical form IS a valid
      `xsd:dateTime`, where the offset is optional, so the JSON-LD projection is unaffected.
      The pattern below accepts the upstream form and a properly zoned one alike,
      so that this block does not have to be revised when the defect is fixed upstream.
      See description.md.

      '
    pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?$
  PointTimeSpec:
    type: object
    description: A single instant.
    required:
    - type
    - dt
    properties:
      type:
        const: pointtimespec
        x-jsonld-id: '@type'
      dt:
        $ref: '#/$defs/LocalOrZonedDateTime'
        description: The instant the map and its solution apply to.
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/instant
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
    additionalProperties: false
  WeekOfYearTimeSpec:
    type: object
    description: 'The week-long interval beginning (week - 1) weeks after 1 January
      of the given year -- `Date(year, 1, 1) + Week(week - 1)` in `bounds(::WeekOfYearTimeSpec)`.
      This is NOT ISO 8601 week numbering: it counts from 1 January rather than from
      the first Thursday, so week 1 of a year does not in general coincide with ISO
      week 1, and week 53 runs past the end of the year.

      The 1..53 bound is ADDED here; upstream the field is a bare `Int` with no validation.
      53 is the last week that still begins within the year.

      '
    required:
    - type
    - year
    - week
    properties:
      type:
        const: weekofyeartimespec
        x-jsonld-id: '@type'
      year:
        type: integer
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/year
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
      week:
        type: integer
        minimum: 1
        maximum: 53
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/week
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
    additionalProperties: false
  MonthOfYearTimeSpec:
    type: object
    description: The calendar month of the given year.
    required:
    - type
    - year
    - month
    properties:
      type:
        const: monthofyeartimespec
        x-jsonld-id: '@type'
      year:
        type: integer
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/year
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
      month:
        type: integer
        minimum: 1
        maximum: 12
        description: 'The 1..12 bound is ADDED here; upstream the field is a bare
          `Int` with no validation.

          '
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/month
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
    additionalProperties: false
  RangeTimeSpec:
    type: object
    description: 'An explicit half-open interval [start, stop). That `start` precedes
      `stop` relates two sibling values and is not expressible in JSON Schema; it
      is carried as a SHACL constraint by ogc.hosted.seadots.fcm-ontology.

      '
    required:
    - type
    - start
    - stop
    properties:
      type:
        const: rangetimespec
        x-jsonld-id: '@type'
      start:
        $ref: '#/$defs/LocalOrZonedDateTime'
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/intervalStart
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
      stop:
        $ref: '#/$defs/LocalOrZonedDateTime'
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/fcm/intervalStop
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
    additionalProperties: false
x-jsonld-extra-terms:
  id: '@id'
  pointtimespec: https://w3id.org/ogc/hosted/seadots/fcm/PointTimeSpec
  weekofyeartimespec: https://w3id.org/ogc/hosted/seadots/fcm/WeekOfYearTimeSpec
  monthofyeartimespec: https://w3id.org/ogc/hosted/seadots/fcm/MonthOfYearTimeSpec
  rangetimespec: https://w3id.org/ogc/hosted/seadots/fcm/RangeTimeSpec
x-jsonld-prefixes:
  fcm: https://w3id.org/ogc/hosted/seadots/fcm/
  xsd: http://www.w3.org/2001/XMLSchema#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-timespec/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-timespec/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "type": "@type",
    "dt": {
      "@id": "fcm:instant",
      "@type": "xsd:dateTime"
    },
    "year": {
      "@id": "fcm:year",
      "@type": "xsd:integer"
    },
    "week": {
      "@id": "fcm:week",
      "@type": "xsd:integer"
    },
    "month": {
      "@id": "fcm:month",
      "@type": "xsd:integer"
    },
    "start": {
      "@id": "fcm:intervalStart",
      "@type": "xsd:dateTime"
    },
    "stop": {
      "@id": "fcm:intervalStop",
      "@type": "xsd:dateTime"
    },
    "id": "@id",
    "pointtimespec": "fcm:PointTimeSpec",
    "weekofyeartimespec": "fcm:WeekOfYearTimeSpec",
    "monthofyeartimespec": "fcm:MonthOfYearTimeSpec",
    "rangetimespec": "fcm:RangeTimeSpec",
    "fcm": "https://w3id.org/ogc/hosted/seadots/fcm/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/fcm-timespec/context.jsonld)

## Sources

* [FuzzyCognitiveMapTools.jl v0.1.0](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl)
* [FCM data specifications (dataspecs/fcm_dataspecs__20260630.md)](https://gitlab.sintef.no/seadots-eu-project/tools/fuzzycognitivemaptools.jl/-/blob/main/dataspecs/fcm_dataspecs__20260630.md)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/_staging/fcm-timespec`

