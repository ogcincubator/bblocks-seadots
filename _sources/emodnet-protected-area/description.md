# EMODnet-compliant protected areas

This building block and its children specify the **additional steps** needed to
turn the protected-area collections of the Seadots OGC API - Features instance (pygeoapi)
into collections whose features are **field-for-field compatible with EMODnet Human
Activities**.

- **Norway:** Miljødirektoratet *Naturvernområder*.
- **Baltic Sea:** HELCOM MPAs.

The existing collections already serve the sources *unchanged*. They use OGC API
syntax, but each source keeps its own schema. Nothing on the API tells a client which
EMODnet layer a source corresponds to, or how its fields and codes translate.

## Building blocks in this set

| Block (`ogc.hosted.seadots.…`) | Role |
|---|---|
| `emodnet-protected-area` (this block) | Common Feature envelope and shared vocabularies: IUCN, country and ecosystem bound to INSPIRE / EU authority tables; SHACL for coded values |
| `emodnet-protected-area.nationally-designated-area` | **Target** = EMODnet `nationallydesignatedareas` (36 attributes, EEA NatDA/CDDA), with the golden EMODnet records |
| `emodnet-protected-area.rsc-mpa` | **Target** = EMODnet `marineprotectedareas` (17 attributes, `rsc` = HELCOM / OSPAR), with the golden EMODnet records |
| `emodnet-protected-area.api-collection` | **API** profile of the collection description for the new EMODnet views |
| `protected-area.source-norway-naturvernomrade` | **Source** profile, crosswalks (CSV + SKOS), transform, crosswalk derivation, contract test |
| `protected-area.source-helcom-mpa` | **Source** profile (layers 54 and 190), transform with code classification and routing, contract test |
| `protected-area.transform-report` | Schema of the `seadotsTransformReport` member every transform writes |

Source profiles live under `protected-area` because they are not EMODnet-specific: the canonical
protected-area model will sit there too, and every source is mapped to it.

Every feature profile accepts a single Feature or a FeatureCollection of such Features, so both
the API's `/items` responses and the transform outputs validate against it.

The blocks reuse `ogc.geo.features.feature`, `ogc.api.features.v1.schemas.collection` and,
for the dataset records, the Seadots `catalog-data` profile. EMODnet's field names are kept
exactly as the service publishes them. This follows the pattern of the existing
`emodnet-compliant-windfarm` block. Semantics are added by the JSON-LD contexts, never by
renaming fields.

## Source → EMODnet layer assignment

| Source collection (Seadots API) | EMODnet target layer | Target block | Fit |
|---|---|---|---|
| `no-live-naturvern-omrade`, `no-snapshot-naturvern-omrade-marine` | `nationallydesignatedareas` | `nationally-designated-area` | Full, after crosswalk. `marinearea` needs an overlay for mixed sites |
| `helcom-live-mpas` (MADS layer 54) | `marineprotectedareas`, `rsc = HELCOM` | `rsc-mpa` | Full (lossless on the example sites) |
| `helcom-live-mpa-network-2026` (layer 190) | split by code scheme | `rsc-mpa` for HELCOM ids; other rows are routed | Partial (see step 4) |
| Norwegian proposed sites (layer 4) | none | — | EMODnet publishes no proposed sites |

## The steps

Each step is carried by a building block, and each block's description has the details.

### Step 1: Pin the source and target contracts
*Blocks: `source-*`, `nationally-designated-area`, `rsc-mpa`.*

- Describe each source collection with a **source-faithful** schema, keeping its own field
  names. Both the live (ArcGIS epoch-ms dates, `SHAPE.STArea()`) and snapshot
  (`SHAPE_STArea`) variants are accepted.
- Describe each EMODnet layer with a **target** schema that has every attribute, EMODnet's
  names and primitive types, and `additionalProperties: false`.
- The targets were derived from `DescribeFeatureType` plus actual `GetFeature` responses.
  These disagree for `marineprotectedareas.name`: the schema lacks it, but responses carry it.
- Each target ships a **golden example**, i.e. a real EMODnet record retrieved 30 Sep 2026.

### Step 2: Build the code crosswalks
*Blocks: `emodnet-protected-area` (vocabulary.ttl), `source-norway-naturvernomrade` (crosswalk/).*

- Norwegian `verneform` (24 values) → EEA designation type (`NO01`…`NO53`, Eionet vocabulary).
- `iucn` → `iucncatego` / `iucndesc` (EMODnet literals, bound to INSPIRE IUCNCategoriesValue).
- `majorEcosystemType` → `majorecosy`.
- Every crosswalk row records its evidence: *observed*, *label* or *inferred*.
- The CSV drives the transform; the same table is published as SKOS
  (`exactMatch` / `closeMatch`). A test keeps the two in sync.

### Step 3: Confirm the crosswalk from data
*Block: `source-norway-naturvernomrade` (`transforms/derive_crosswalk.py`).*

- Join the Norwegian snapshot with the EMODnet snapshot on `naturvernId = nationalid`
  (≈1,527 shared sites).
- Tabulate `verneform × designatio` and `iucn × iucncatego`.
- Promote *inferred* rows that are ≥ 98 % consistent. Investigate split rows: they are either
  crosswalk errors or reporting-chain errors (Møysalen).
- Re-run after every EEA reporting cycle.

### Step 4: Transform
*Blocks: `source-*` (`transforms.yaml` → Python, standard library only).*

- **Structure:**
  - rename fields;
  - set constants (`countrycod`, `namespace`, `rsc`, …);
  - convert units (`SHAPE.STArea()` m² → `sitearea` ha; `vernedato` → `legalfound` year);
  - dissolve to one MultiPolygon per site;
  - output in CRS84;
  - compute `shape_leng` / `shape_area` planar on lon/lat, as EMODnet does.
- **Selection:**
  - Norway: marine sites only, excluding forms that have no EEA designation.
  - HELCOM layer 190: classify `Code` by pattern and publish only HELCOM MPA ids.
    - Natura 2000 codes are **routed** to `emodnet:natura2000areas`.
    - EEA/WDPA ids are **routed** to `emodnet:nationallydesignatedareas`.
    - Routed rows are not duplicated. Both routes were checked against live EMODnet records.
- **Report:** each run returns `seadotsTransformReport`: excluded, routed, not yet reported to
  the EEA, inferred designations, needs overlay, differences from EMODnet.

### Step 5: Enrich fields the source does not carry
*Blocks: `source-*`, `nationally-designated-area` (description).*

- `marinearea` for *MarinOgTerrestrisk* sites needs an overlay with a coastline (e.g.
  Kartverket or the EEA coastline). Until that runs, the value is reused from an EMODnet
  reference for the same site, and the report says so.
- HELCOM layer 190 has no status: join `MPA_status`, `Year_est` and `Site_link` from layer 54.
  Ids without a match are reported, not published.
- EEA reporting-chain fields (`metadata_*`, `id`) are filled with Seadots provenance or `null`,
  as documented per field.

### Step 6: Reconcile with EMODnet
*Blocks: `source-*` (`--emodnet-reference` / `emodnetReference`, contract tests).*

- Compare each output feature with the EMODnet record for the same site.
- **Policy:** the national or regional source is authoritative. The view keeps source values
  and publishes the differences.
- On the example data:
  - Tauterryggen equals EMODnet on all 22 source-derivable fields.
  - The Møysalen error in EMODnet (natdaid, designatio, iucncatego swapped with the
    neighbouring site) is reported.
  - Hatter Barn and Jasmund equal EMODnet on all non-geometric fields.
- Sites that EMODnet does not have yet (e.g. the four Norwegian MPAs of 13 Feb 2026) are
  published with `natdaid = null` and id `NO-<naturvernId>`.

### Step 7: Publish as new OGC API collections
*Block: `api-collection`.*

- Add the collections `emodnet-view-no-nationallydesignatedareas` and
  `emodnet-view-helcom-rsc-mpa` next to the unchanged source collections.
- **Recommended implementation for pygeoapi (materialised):**
  1. At setup, run the transforms over the source collections' items.
  2. Write GeoPackages, and serve them with the SQLiteGPKG provider (`id_field` = `natdaid` or
     `code`; for Norway a surrogate id column, because `natdaid` can be null).
  3. Refresh on the same schedule as the snapshots.
- **Live alternative:** a small provider plugin that wraps the ESRI provider and applies the
  transform per request. It costs more per request and does not support property filters on
  EMODnet names without pushing the reverse mapping down to ArcGIS.
- The collection description must link to:
  - the profile (`rel=profile`, the bblock);
  - the item schema (`describedby`, `application/schema+json`);
  - queryables;
  - the source collection (`derived-from`);
  - the EMODnet layer (`related`);
  - the licence and source metadata;
  - the transform report.

  pygeoapi's per-resource `links:` setting provides all of these.
- Queryables then carry EMODnet names, so the same filter works on both services, e.g.
  `designatio=NO05`, `countrycod=NO` or `rsc=HELCOM&country=Finland`.

### Step 8: Catalogue the views
*Block: `ogc.hosted.seadots.catalog-data`.*

- Add one dataset record per view to `seadots-mpa-sources`, taking it from 11 to 13 records.
- Each record carries:
  - `conformsTo` with the target bblock;
  - PROV `wasDerivedFrom` pointing to the source dataset record;
  - the transform (`transforms.yaml` id) as the activity;
  - a link to the view's collection.

### Step 9: Validate continuously
*All blocks.*

- The register CI (`bblocks-postprocess`) validates examples against the schemas, uplifts
  them with the JSON-LD contexts and runs the SHACL rules.
- The register CI also runs each transform on its block's GeoJSON examples (options from the
  transform's `metadata` in `transforms.yaml`) and validates the output against the target profile.
- `transform-tests/test-transform.sh` in each source block pins the transform contracts against the
  golden EMODnet records.
- `tools/validate_protected_areas.py` runs the same checks offline.
- In production, run `scripts/smoke_test.py` with a check that a sample of view items
  validates against the target schema.

## Known limits and open decisions

- **Norway, coastal terrestrial sites.** EMODnet also carries Norwegian *terrestrial* sites
  with `coast_mar = 1` (coastal proximity rule of the EEA). The view is limited to marine
  sites. Reproducing the coastal set needs the EEA rule and a coastline.
- **OSPAR.** EMODnet's `marineprotectedareas` also holds 31 Norwegian OSPAR MPAs. The national
  source does not flag OSPAR membership, so an OSPAR view needs the OSPAR MPA list as a join.
- **HELCOM 2026 network.** Its national type labels (Finnish, Danish, Swedish, …) have no
  field in the RSC schema. Mapping them to EEA designation types would need one crosswalk
  per country (step 2 pattern). New HELCOM ids wait for the HELCOM MPA database (step 5).
- **Semantics of some EMODnet fields are undocumented** (`metadata_f`, the unit of
  `rep_area` / `gis_area`). The view leaves them `null` rather than guessing.
- **Inferred crosswalk rows** (8 of 24 `verneform` values) must be confirmed in step 3
  before a production release.
