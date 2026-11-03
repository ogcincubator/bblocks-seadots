## Marine Protection Properties

The attributes of a site in the ProtectedSeas Navigator dataset, as served by the Ocean Data Platform features API.
The context maps each one to the [Marine Protections Ontology](../marine-protection-ontology) or directly to a term of
the OGC Cross Domain Model.

Property descriptions are taken from the [Navigator data dictionary](https://navigatormap.org/data-dictionary/). API
field names differ from the names in the dictionary, and some correspondences were inferred from their coded values or
content. These are recorded as `skos:editorialNote` in the ontology.

Constraints reflect the dictionary, and were checked against the 1000 items the API returns:

- **Regulation attributes** use the codes Allowed (0), Prohibited (1), Restricted (2), N/A or Unknown (3), and null for
  not yet coded.
- **`tribal_exemptions`** is coded Yes (0), No (1).
- **`level_fishing_protection`** allows 0 as well as the published 1-5 scale, because 0 occurs in the data. Its meaning
  is not documented.
- **`effective_from` and `effective_to`** allow an empty string as well as a date, because it occurs in the data.

`ogc_fid`, `focal_species_tokens` and `geom_complexity` are technical fields of the serving database. They are not in
the dictionary and have no semantic mapping, so are deliberately omitted from the context. Additional properties are
allowed, since the dictionary describes attributes that this API does not serve.
