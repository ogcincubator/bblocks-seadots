# EMODnet windfarm OSM extension

This block profiles `ogc.hosted.seadots.windfarms.windfarm-designated-area-emodnet` and adds source-specific OSM identity, tags, and relation members. The base block remains unchanged. Each transformed feature retains its original GeoJSON geometry—including a null relation geometry—and its original `id`, `osm_type`, `osm_id`, complete `tags` object, and optional `members` array. Mapped properties are additive; they do not replace the source tags.

## Source-property coverage gaps

| OSM source property | EMODnet/profile property | Mapping |
|---|---|---|
| `tags.name`, otherwise `tags.seamark:name` | `name` | Copy first available value |
| `tags.plant:output:electricity`, otherwise `tags.generator:output:electricity` | `power_mw` | Parse a numeric value only when the explicit unit is MW; raw value remains in `tags` |
| `tags.status` | `status` | Copy source text without normalization |
| `tags.plant:type` | `type_inst` | Copy source text |
| `tags.start_date` | `year` | Copy source string; raw tag remains available to interpret the date meaning |
| `tags.turbines` | `n_turbines` | Parse only an integer count |
| Polygon or multipolygon relation plus `tags.industrial=windfarm`, `tags.seamark:landmark:production_area=wind_farm`, or `tags.plant:source=wind` and `tags.plant:type=offshore` | `category_of_offshore_production_area` | Add IHO enumerated code `1` (“Wind Farm”) only when area geometry/type and source tags support it |
| Point node with `tags.generator:method=wind_turbine` | `iho_feature_role` | Link to the local Wind Turbine concept, aligned to IHO S-32 and the S-101 Wind Turbine (LNDMRK) label |
| Polygon or multipolygon relation with explicit wind-farm area tags (above) | `iho_feature_role` | Link to the local Offshore Production Area concept, aligned to the S-101 Offshore Production Area (OSPARE) label |

No value is inferred for `country`, `dist_coast`, `notes`, `updateyear`, or area. The snapshot's geographic filter does not constitute per-feature country evidence. The transform does not normalize OSM statuses or assume an absent tag. For an electricity-output tag expressed in a unit other than MW or with an unparseable value, `power_mw` is omitted.

### Explicitly unmapped EMODnet properties

The source has no per-feature country code/name, coastal distance, source notes field, update year, or area measurement, so `country`, `dist_coast`, `notes`, `updateyear`, and `area_sqkm` remain absent. A bounding filter is not evidence that every feature lies within a national boundary. No OSM property maps to these fields without additional authoritative data.

The IHO Geospatial Information Registry defines Data Dictionary item 42, “Category of Offshore Production Area,” as classification of an area at sea within which production facilities exist; code `1` is “Wind Farm.” The local predicate `categoryOfOffshoreProductionArea` is linked to item 42 in `ontology.ttl`, and the data stores the registry's numeric code. The property is only attached to area features when OSM tags explicitly support it. `iho_feature_role` points to local concepts with SKOS close-match links to the cited IHO material; the transform does not invent an IHO registry IRI for a feature class. This follows the distinction in IHO S-101 between offshore production areas and individual wind turbines. See the [IHO registry item](https://registry.iho.int/fdd/view3.do?idx=42&type=3), [IHO S-101 Annex A](https://metanorma.github.io/iho-s-101/documents/2.0.0/annex-a/document.html), and the [IHO S-32 wind turbine definition](https://portal.iho.int/iho-ohi/S32/engView.php?page=303).

The source is a dated OpenStreetMap extract, not an authoritative national inventory. Its attribution and ODbL license are retained with the source representation and example. See [OpenStreetMap copyright](https://www.openstreetmap.org/copyright).
