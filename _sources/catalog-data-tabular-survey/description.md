# SeaDOTs Catalog Data Tabular Survey

This profile is intended for survey-style tabular datasets such as the Norwegian saltmarsh perceptions workbook. It extends the SeaDOTs tabular catalog profile with survey-specific metadata for questionnaire variables, controlled-vocabulary links, and DDI-style variable descriptions.

## Why this is tabular rather than generic

The source is a rectangular questionnaire export with repeated response columns and coded categories. That makes it a good fit for the tabular catalog profile, because the data asset is still a table with rows and columns, even though the metadata is richer than a generic data record. The richer semantics are captured here without forcing the entire dataset into a generic catalog record.

## Semantic hooks

- ELSST: use the `survey:conceptUri` and `survey:controlledVocabulary` fields to reference thesaurus concepts for environmental and social-science terms.
- CESSDA: use `survey:controlledVocabulary` with a `scheme` and `uri` to point at controlled vocabularies used by survey instruments.
- DDI: use `survey:variableMetadata[].ddi:variableDescription` and `survey:studyDescription` to preserve questionnaire and variable-level documentation.

## Recommended usage

Use this block when the data asset is an Excel/CSV/Parquet survey export and you need to describe questionnaire variables and their controlled-vocabulary mappings in the catalog record.
