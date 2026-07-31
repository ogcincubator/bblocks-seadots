# EMODnet-compliant windfarm

This block is a GeoJSON Feature profile aligned with the official EMODnet Human
Activities windfarms XSD. It uses the same published attribute names as the
service schema and maps the official `the_geom` concept to the GeoJSON
`geometry` object.

The profile is intentionally flat and service-aligned with the following
properties. The `country` value is represented as the source country name,
not as an ISO code, and is not restricted to a fixed enumeration — the
underlying EMODnet field is a free-text `xsd:string` (see
`examples/emodnet-windfarms.xsd`) and can hold any country name the service
publishes. `context.jsonld` and `ontology.ttl` bind the country names
currently observed in the live service (queried via WFS
`GetPropertyValue`: Belgium, Denmark, Estonia, Finland, France, Germany,
Greece, Ireland, Italy, Latvia, Lithuania, Malta, Netherlands, Norway,
Poland, Portugal, Romania, Spain, Sweden, United Kingdom) to the
[EU Publications Office Country authority table](http://publications.europa.eu/resource/authority/country/)
(e.g. Belgium -> `http://publications.europa.eu/resource/authority/country/BEL`),
whose ISO 3166-1 alpha-3 codes cover all countries, not just EU/EEA member
states. Any new country name appearing in the source data should be added
to both files following the same pattern.

- `country`
- `n_turbines`
- `power_mw`
- `status`
- `type_inst`
- `updateyear`
- `year`
- `dist_coast`
- `notes`

It is intended for direct publication as a GeoJSON Feature or WFS feature and
can be used as a minimal interchange layer before any downstream semantic
enrichment.
