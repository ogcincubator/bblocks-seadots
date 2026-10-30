# Windfarm data integration exercise

This is a standalone companion exercise to the Baltic SES notebooks. It lets you inspect each source as supplied, then compare their records in a shared canonical model served as GeoJSON and JSON-LD by pygeoapi.

## The three views

| Collection | What it shows | Geometry |
|---|---|---|
| `national-source` | Original national CSV fields, unchanged | Null: the national input has no coordinates |
| `emodnet-source` | EMODnet fields translated to the published windfarms feature schema | Source point geometry |
| `harmonized-windfarms` | Target Building Block fields, provenance and mapped locations | EMODnet points for EMODnet records; crosswalk centroid for matched national records; Baltic West has a separately labelled approximate point; null for other unmatched projects |

The EMODnet model is `ogc.hosted.seadots.emodnet-compliant-windfarm`; the harmonized Polish target is the independent block `ogc.hosted.seadots.emodnet-compliant-windfarm-pl`. National-source translation lives with its source block. The EMODnet CSV-to-feature mapping is exercise configuration in `config/emodnet-source-translation.json`, because the bundled CSV is an extract rather than a second EMODnet data model. The exercise builder reads the EMODnet and Polish-target JSON-LD contexts and builds a pygeoapi config from them. pygeoapi's built-in GeoJSON feature provider serves the generated collections; its linked-data response decorator uses the configured contexts for `f=jsonld`.

The base EMODnet feature has the XSD fields `country`, `n_turbines`, `power_mw`, `status`, `type_inst`, `updateyear`, `year`, `dist_coast`, and `notes`; the XSD makes these optional and nullable. The source CSV `name` is retained as the feature identifier, and `lon`/`lat` construct GeoJSON geometry. `dist_coast_m` maps to `dist_coast` in metres. National translations are: `farm` → `name`, `capacity_mw` → `power_mw`, `status_aug2026` → normalized `status` plus preserved `status_detail`, and `first_power_or_completion_year` → `year` with its meaning and assumed status recorded. Fields absent from a source remain null in the harmonized extension.

`data/emodnet-source-input-example.json` shows the CSV-derived input shape before that translation; the published `emodnet-source` collection uses the XSD-aligned EMODnet representation.

## Build and run

From this directory, install the isolated pygeoapi environment and build the collections:

```sh
./setup_pygeoapi.sh
python3 build_windfarm_service.py
./service/run.sh
```

The setup script installs pygeoapi 0.19.0 and its compatible Pydantic 1 dependency in a local `.venv`; it does not alter the global Anaconda environment. The launcher uses this isolated executable, generates the OpenAPI document from the generated configuration, then starts the service. The builder creates the service directory with source and harmonized GeoJSON, pygeoapi configuration, templates and static assets. It does not modify the source CSV files.

Open these endpoints:

- `http://localhost:5000/collections/national-source/items?f=json`
- `http://localhost:5000/collections/emodnet-source/items?f=json`
- `http://localhost:5000/collections/harmonized-windfarms/items?f=json`
- Replace `f=json` with `f=jsonld` to inspect each collection as JSON-LD.

## Location matching

The national records contain no location. `config/location-mapping.json` therefore records explicit project-name to EMODnet-name associations. Where a project maps to multiple EMODnet sites, the harmonized national record uses their mean longitude and latitude and records `location_status: mapped`, the method, and all matched EMODnet names. This is a display/association point, not a surveyed project centroid. Baltic West has no defensible match in this EMODnet snapshot. ORLEN Neptun describes its four licensed areas on the Odra Bank about 26.5 km offshore; the config therefore supplies an approximate representative point at `[15.45, 54.40]` and marks it `location_status: anticipated`, with low confidence and a source link. It is not a published farm centroid or boundary. Other unmatched projects retain null geometry. You can inspect these distinctions in the harmonized collection.

## Exercise prompts

1. Which fields are present in the national source but absent from EMODnet, and vice versa?
2. How do the two sources differ in capacity and status for the same projects?
3. Which national projects received mapped locations, and what does the mapping method mean?
4. Why is Baltic West unmatched in this snapshot?
5. Which provenance and reporting-time fields make a harmonized value traceable to its source?

## Second notebook: four sources, one model, one API

`windfarm_sources_to_ogcapi.ipynb` extends this exercise to four sources — OpenStreetMap, the EMODnet WFS, the HubOcean ODP copy of EMODnet, and the national list. The notebook only calls functions:

```
raw data ──lift(block)──▶ RDF ──align──▶ common RDF ──validate──▶ ──resolve──▶ RDF ──lower(target block)──▶ GeoJSON / OGC API
          bblocks_ld        *.rq + crosswalk        SHACL        policy          bblocks_ld
```

| File | Role |
|---|---|
| `bblocks_ld.py` | **generic**: `BuildingBlock` (context, JSON Schema, SHACL from a bblocks repository or the published register), `lift(data, block) → RDF`, `lower(RDF, block, type) → GeoJSON` (JSON-LD framing with the block's context, PyLD), `construct`, `select`, `shacl_report`. Input data may be GeoJSON, a GeoDataFrame or GeoParquet. |
| `windfarm_harmonise.py` | one function per step for this case (read, uplift, align, link zones, validate, resolve, to_profile), analysis helpers, `HarmonisedProvider` for pygeoapi and service helpers |
| `../viz.py` | maps (geopandas/folium) and charts used by the notebook |
| `config/multisource/sources.json` | raw files, the building block that lifts each one (`bblock:<name>` or a local context), IRI patterns, licences |
| `config/multisource/tbox/offshore-wind-common.ttl` | common TBox: reuses `em:`, `seadots-emodnet:`, `ses:`; adds turbines, planning zones and source records (`owc:`, local to the exercise) |
| `config/multisource/alignments/*.rq` | SPARQL CONSTRUCT per source shape; `emodnet-points.rq` serves both the WFS and the ODP copy |
| `config/multisource/farm-crosswalk.json` | same-farm links (national ↔ EMODnet from `location-mapping.json`, OSM elements and turbine rules) |
| `config/multisource/shapes/offshore-wind-common.shacl.ttl` | rules for every translated record, plus cross-source warnings |
| `config/multisource/projection.json` | which source wins for each property |
| `config/multisource/projections/farms-pl.rq` | resolved common RDF → the RDF shape of `emodnet-compliant-windfarm-pl` |
| `config/multisource/contexts/` | OSM context, the common-model context, and `pl-status-terms.jsonld` (a patch for the Polish block's status terms, see below) |
| `service-multisource/` | generated by the notebook: raw collections, harmonised snapshots, pygeoapi configuration and `run.sh` (port 5001) |

**Finding about `emodnet-compliant-windfarm-pl`.** Its context sets `@vocab` to the profile namespace and types `status` as `@vocab`, so `"Construction"` lifts to `…emodnet-compliant-windfarm-pl#Construction` rather than `seadots-emodnet:Construction`; lowering needs the local patch. Defining the five status terms in the block context would fix it. The base block maps `name` to `seadots-emodnet:name` (via `@vocab`) while the profile uses `schema:name`.

The harmonised collections run the pipeline inside pygeoapi: re-run `./setup_pygeoapi.sh` once (the requirements now include rdflib, PyLD, geopandas), then `./service-multisource/run.sh`. Collections: `raw-osm`, `raw-emodnet-points`, `raw-emodnet-zones`, `raw-odp-points`, `raw-odp-zones`, `raw-national` (as received; `f=jsonld` applies the source's block context) and `farms-pl`, `farms-common`, `turbines`, `zones` (translated on request; `bbox` is supported). The notebook itself needs the packages in `../requirements.txt`.
