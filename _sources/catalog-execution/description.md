# SeaDOTs Catalog Execution

An execution is one concrete experiment run: an instance of the same reusable workflow that links to the workflow, input records, and output records using OGC API Records and PROV-O relations.

The execution record is intentionally light. It avoids repeating descriptive
metadata that belongs in the linked records, so a run can be represented by its
identifier and relative references that work in local checkouts and published
registers.

## Role in the Catalog Metadata Model

This generic building block supports the SeaDOTs catalog model described in
`data_framework/INTEROPERABILITY.md` under `Catalog Metadata Model` and
`2.2 Provenance model (Open Science)`.

## Source-property coverage gaps

This block is a generic catalog template and is not derived from a raw source
dataset. No source properties are intentionally dropped.
