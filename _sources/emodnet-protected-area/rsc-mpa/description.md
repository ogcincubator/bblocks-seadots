# EMODnet-compliant Regional Sea Convention MPA

Target profile that reproduces the EMODnet Human Activities layer
`emodnet:marineprotectedareas`: MPAs as reported to the Regional Sea Conventions,
distinguished by `rsc` (`HELCOM` or `OSPAR`). For the Baltic Sea this is EMODnet's
representation of the HELCOM MPA network.

## Conformance rules beyond the JSON schema

1. **Complete attribute set, EMODnet names.** All 17 attributes are present and
   unknown values are `null`. No additional attributes are allowed.
2. **`code` is numeric.** EMODnet types `code` as `xsd:long`. HELCOM MPA database
   ids (e.g. `252`) qualify. Natura 2000 site codes (`LTSIU0012`), EEA site ids and
   national codes do not. Rows that carry those codes belong to other EMODnet layers
   (see the HELCOM source profile).
3. **Name goes in `name`.** EMODnet's HELCOM rows keep the site name in `name` and
   leave `orig_name` and `designatio` empty. The view does the same.
4. **HELCOM status vocabulary.** When `rsc = HELCOM`, `status` is one of
   *Designated and managed*, *Designated and partly managed* or *Designated*,
   exactly as HELCOM publishes it.
5. **Area fields stay empty for HELCOM** (`rep_area`, `gis_area`, …), as in EMODnet.
   A publisher that fills them must state the unit in the collection metadata,
   because EMODnet's own unit for these fields is undocumented.
6. **One feature per site** as a (Multi)Polygon in CRS84. `shape_leng` and `shape_area`
   are planar measures on the lon/lat coordinates.

Note: `DescribeFeatureType` for this layer lists `orig_name` but not `name`. However,
the GeoJSON and CSV `GetFeature` responses do include `name`, and it is the only
populated name field for HELCOM rows. This profile follows the actual responses.
