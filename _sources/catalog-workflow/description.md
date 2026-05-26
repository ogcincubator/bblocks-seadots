# SeaDOTs Catalog Workflow

A workflow is the reusable catalog-facing plan for a digital twin application,
model, transformer, or processing service. It is represented as an OGC API
Records item with PROV-O plan semantics, so it carries both discovery metadata
and the intended method, model chain, version, expected inputs, expected
outputs, and planned Activity pattern repeated by every execution.

Runnable implementation details are linked through `applicationPackage`, which
points to the APKG/CWL-aligned `catalog-application-package` block. This avoids
maintaining a separate `catalog-application` record with duplicate metadata.

## Role in the Catalog Metadata Model

This generic building block supports the SeaDOTs catalog model described in
`data_framework/INTEROPERABILITY.md` under `Catalog Metadata Model` and
`2.2 Provenance model (Open Science)`.

## Source-property coverage gaps

This block is a generic catalog template and is not derived from a raw source
dataset. No source properties are intentionally dropped.
