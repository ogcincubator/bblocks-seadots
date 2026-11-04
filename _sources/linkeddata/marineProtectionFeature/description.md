## Marine Protection Feature

A "Feature Type": a marine managed area modelled as a GeoJSON Feature with its own domain model. The attributes are
defined by [Marine Protection Properties](../marineProtectionProperties), so they are managed independently of the
Feature container.

The source API responds with a `FeatureCollection`, and the example extracts its member Feature. The dataset is
described by a [Marine Protection Dataset Record](../marineProtectionRecord).

### Semantic uplift

A JSON-LD context cannot express everything needed for the intended RDF, so `semantic-uplift.yaml` adds:

- **A stable identity:** the API `id` is a row offset (`0`, `1`, `2`...), not an identifier of the site, so `site_id`
  provides the identity of the RDF resource.
- **Removal of empty values:** the source uses `""` and `"null"` for missing text and dates, which would otherwise
  produce misleading or invalid literals.
- **A class assertion:** each Feature is typed as `mpr:MarineManagedArea`, which also brings it in scope of the shapes
  of the [ontology](../marine-protection-ontology).

These steps only affect the RDF: the JSON served by the API is valid as it stands. Consumers using the JSON-LD context
at run-time need to apply them too.
