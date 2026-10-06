# Naturvernområder source profile with EMODnet transform

**Source:** Norwegian protected sites (Miljødirektoratet *Naturvernområder*, Geonorge
`5857ec0a-…`, ArcGIS `vern` layer 0). The Seadots pygeoapi instance serves them
unchanged as `no-live-naturvern-omrade` (live) and `no-snapshot-naturvern-omrade-marine`
(snapshot).

**Target:** `emodnet-protected-area.nationally-designated-area`, the same shape as
EMODnet's `nationallydesignatedareas`.

## Field mapping

| EMODnet attribute | Rule | Source field(s) |
|---|---|---|
| `natdaid` | integer | `cddaId` (null until the site is reported to the EEA) |
| `countrycod`, `regioncode` / `country` | constant | `NO` / `Norway` |
| `sitename` | copy (short name, **not** `offisieltNavn`) | `navn` |
| `legalfound` | year of the date | `vernedato` (epoch ms or ISO date) |
| `localid`, `nationalid`, `pslocalid` | copy | `naturvernId` |
| `namespace`, `psnamespac` | constant | `http://www.miljodirektoratet.no/naturbase` |
| `designatio` | crosswalk `verneform-designation.csv` | `verneform` |
| `iucncatego`, `iucndesc` | crosswalk `iucn.csv` | `iucn` |
| `majorecosy` | crosswalk `ecosystem.csv` | `majorEcosystemType` |
| `marinearea` | 100 / 0 from the crosswalk. For *MarinOgTerrestrisk*, a coastline overlay is needed (step 4) | `majorEcosystemType` + geometry |
| `sitearea` | m² ÷ 10 000, 2 decimals | `SHAPE.STArea()` / `SHAPE_STArea` (EPSG:25833) |
| `shape_leng`, `shape_area` | planar on the CRS84 geometry | geometry |
| `designated`, `coast_mar`, `geomtype`, `spatialdat`, `spatialres` | constant | `Designated site`, `1`, `polygon`, `public`, `Scale larger 100K` |
| `metadata_v`, `metadata_b` | provenance | Geonorge metadata URL, retrieval date |
| `id`, `versionid`, `metadata_s/f/1`, `iucnlink`, `psversioni`, `remark` | `null` | — |

All other source fields (`verneforskrift`, `faktaark`, `forvaltningsmyndighet`, `kommune`,
…) are dropped from the view. They stay available on the source collection, which the view
links to.

## Selection rules

- **Kept:** marine sites, i.e. `majorEcosystemType` *Marin* / *MarinOgTerrestrisk*. This
  matches EMODnet's `majorecosy <> 'Terrestrial'` subset for Norway (885 EMODnet vs 888
  source sites on 28 Sep 2026). Coastal *terrestrial* sites, which EMODnet also carries with
  `coast_mar = 1`, would need the EEA's coastal-proximity rule and are out of scope.
- **Excluded:** protection forms with no EEA designation type (`MidlertidigVernaOmraade`),
  and proposed sites (layer 4). EMODnet publishes neither.

## Crosswalk confidence

`crosswalk/verneform-designation.csv` records how each mapping was established:

- **observed**: confirmed by a joined EMODnet record;
- **label**: the Eionet label is the English name of the Norwegian form;
- **inferred**: variant forms and forms whose Eionet label is ambiguous. For example,
  NO17 and NO23 are both *Wildlife Conservation Area*.

`transforms/derive_crosswalk.py` (step 3) confirms the crosswalk from the ~1,500 joined
sites before inferred rows are relied on. The CSV drives the transform, and
`crosswalk/crosswalk.ttl` publishes the same table as SKOS: `exactMatch` for
observed/label rows, `closeMatch` for inferred rows.

## Report produced with every run

The transform returns the EMODnet features plus a `seadotsTransformReport` member with:

- `excluded`
- `notYetReportedToEEA`: sites without `cddaId`, e.g. the four MPAs decided on
  13 Feb 2026. Their feature id is `NO-<naturvernId>`.
- `inferredDesignation`
- `needsMarineAreaOverlay`
- `differsFromEMODnet`: field-level differences from an EMODnet reference.

On the example data it reproduces the EMODnet Tauterryggen record on every mapped
field. It also reports the Møysalen swap (natdaid, designatio, iucncatego), which comes
from the EEA reporting chain. **The view keeps the source values**, because the national
source is authoritative. The difference is surfaced rather than copied.
