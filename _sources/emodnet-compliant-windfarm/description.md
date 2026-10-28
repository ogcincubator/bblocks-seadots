# EMODnet windfarm

This is the single EMODnet windfarm representation in this register. It is a
GeoJSON representation aligned with the official EMODnet Human Activities
windfarms XSD. It uses the service's published attribute names and primitive
types and maps the official `the_geom` concept to GeoJSON `geometry`.

The XSD fields are optional and nillable, and the schema reflects that. The
`country` value is represented as the source country name, not as an ISO code;
the underlying field is a nullable `xsd:string`. `context.jsonld` and
`ontology.ttl` bind country names currently observed in the live service to the
[EU Publications Office Country authority table](http://publications.europa.eu/resource/authority/country/).

The properties are `country`, `n_turbines`, `power_mw`, `status`, `type_inst`,
`updateyear`, `year`, `dist_coast`, and `notes`.

Source-specific extracts, such as the Baltic exercise CSV, are translated into
this representation before being served. Their column mapping is exercise
configuration, not a second EMODnet data model.

The independent [`emodnet-compliant-windfarm-pl`](../emodnet-compliant-windfarm-pl/)
block uses this representation for Polish national-source integration, adding
project names, reporting details, provenance, and location matching. The
independent [`emodnet-compliant-windfarm-no`](../emodnet-compliant-windfarm-no/)
block demonstrates the same base model with Norwegian NVE source details.

This block is intended for publication as a GeoJSON Feature or WFS feature and
as an interchange layer before downstream semantic enrichment.
