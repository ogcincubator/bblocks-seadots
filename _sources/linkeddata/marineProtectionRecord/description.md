## Marine Protection Dataset Record

A profile of [OGC API Records](https://github.com/opengeospatial/ogcapi-records), through its GeoDCAT binding, for
describing a dataset of [marine protection features](../marineProtectionFeature).

The profile adds these constraints:

- `type` must be `dataset`.
- `title`, `description`, `keywords`, `contacts`, `license`, `created`, `updated` and `time` are required.
- At least one contact must have the role `creator`.
- At least one link must have `rel: items` and `type: application/geo+json`, giving access to the features.

It also adds `isAccessibleForFree` and `citation`, which have no equivalent in OGC API Records, mapped to `schema.org`
terms from the OGC Cross Domain Model. Other properties inherit their mappings to DCAT and DCTERMS.

### Additions to the inherited context

The context of OGC API Records, inherited through the GeoDCAT binding, does not carry some of the values required here
into RDF. This profile therefore maps these terms, none of which the inherited context defines:

| Term | Maps to | Otherwise |
|------|---------|-----------|
| `dataset` (value of `type`) | `dcat:Dataset` | resolves to a meaningless IRI relative to the base URI |
| `interval` | `time:hasTime`, as an ordered list | the temporal extent is an empty node |
| `organization`, `roles`, `emails` | `vcard:organization-name`, `vcard:role`, `vcard:hasEmail` | contacts retain only their links |

vCard is not part of the OGC Cross Domain Model, but is the range DCAT specifies for `dcat:contactPoint`.

### Mapping from the source catalog entry

The Ocean Data Platform publishes this dataset's [catalog entry](https://api.hubocean.earth/api/public/catalog/v2/jsonld/datasets/a608f54b-75c7-4df9-a3a8-cedbfa391873)
as a `schema:Dataset` in JSON-LD, which is **not** itself an OGC API Records response. The example is a manual mapping
of that entry into a Record, as retrieved on 2026-11-03:

| schema.org | Record |
|------------|--------|
| `@id` | `id` (final path segment), and a `rel: alternate` link |
| `name`, `description`, `keywords` | `properties.title`, `.description`, `.keywords` |
| `dateCreated`, `dateModified` | `properties.created`, `.updated` |
| `license` | `properties.license` as an SPDX identifier, and a `rel: license` link |
| `creator`, `provider`, `maintainer` | `properties.contacts`, using the source property name as the role |
| `temporalCoverage` | `time.interval` |
| `geosparql:hasGeometry` | `geometry`, converted from WKT |
| `distribution` | `properties.formats`, and a `rel: items` link to the items of `contentUrl` |
| `isPartOf` | a `rel: collection` link |
| `url` | a `rel: about` link |
| `isAccessibleForFree`, `citation` | `properties.isAccessibleForFree`, `.citation` |

`spatialCoverage` is not mapped, since it duplicates the extent given by `geosparql:hasGeometry`.
