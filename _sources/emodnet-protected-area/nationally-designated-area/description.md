# EMODnet-compliant nationally designated area

Target profile that reproduces the EMODnet Human Activities layer
`emodnet:nationallydesignatedareas`. EMODnet serves the EEA *Nationally
Designated Areas* dataset (formerly CDDA) in this layer, filtered to coastal and
marine sites (`coast_mar = 1`). A feature that validates against this profile has
the same 36 attribute names and primitive types as a feature from the EMODnet WFS
(`outputFormat=application/json`). A client, notebook or GIS style written for
EMODnet therefore reads it unchanged.

## Conformance rules beyond the JSON schema

1. **Complete attribute set.** Every attribute is present, and unknown values are `null`.
   Additional attributes are not allowed, so the source's national fields (e.g.
   `verneforskrift`) must not leak into the EMODnet view. They stay on the source
   collection, which is linked from the view (see `api-collection`).
2. **EMODnet encodings, not national ones.** `majorecosy`, `iucncatego` and
   `iucndesc` use EMODnet's English literals. `designatio` uses EEA designation type
   codes (`NO05`), which the JSON-LD context lifts to
   `http://dd.eionet.europa.eu/vocabulary/cdda/designationTypeCodeValue/NO05`.
3. **One feature per site** as a (Multi)Polygon in CRS84. `geomtype` is `polygon`.
4. **Derived measures are computed as EMODnet computes them.**
   - `sitearea` is in hectares.
   - `marinearea` is the marine share in per cent.
   - `shape_leng` / `shape_area` are planar measures on the lon/lat coordinates
     (degrees / square degrees).
5. **Feature id.** The feature id is `natdaid`. Sites not yet reported to the EEA
   (`natdaid` null) get `<countrycod>-<nationalid>`. Such features are *valid but not yet
   reconcilable* with EMODnet, and the view flags them (see the Norwegian source profile).

## Attributes that cannot come from a national source

EMODnet copies some attributes from the EEA reporting chain (Reportnet). A national
source does not carry them. The Seadots view fills them as follows and documents this
in the collection metadata:

| Attribute | EMODnet meaning | Value in the Seadots view |
|---|---|---|
| `id` | EEA database row id | `null` |
| `metadata_v` | Reportnet dataset snapshot URL | URL of the source dataset metadata record (e.g. the Geonorge record) |
| `metadata_b` | Reportnet snapshot date | Retrieval date of the source data |
| `metadata_s`, `metadata_f` | Reportnet validation status and flag | `null`, because no EEA validation has happened |
| `versionid`, `psversioni`, `metadata_1`, `iucnlink` | usually empty in EMODnet | `null` |

For JSON-LD, the context scopes the EMODnet attribute `id` to `pa:eeaRowId`, so it
does not collide with the feature's `@id`.
