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
