# Windfarm data integration exercise

This is a standalone companion exercise to the Baltic SES notebooks. It lets you inspect each source as supplied, then compare their records in a shared canonical model served as GeoJSON and JSON-LD by pygeoapi.

## The three views

| Collection | What it shows | Geometry |
|---|---|---|
| `national-source` | Original national CSV fields, unchanged | Null: the national input has no coordinates |
| `emodnet-source` | Original EMODnet CSV fields, unchanged | Source point geometry |
| `harmonized-windfarms` | Target Building Block fields, provenance and mapped locations | EMODnet points for EMODnet records; crosswalk centroid for matched national records; Baltic West has a separately labelled approximate point; null for other unmatched projects |

The target is `ogc.hosted.seadots.emodnet-compliant-windfarm.baltic-project-extension`. Translation rules live beside their source Building Blocks in `translation.json`. The exercise builder reads those blocks' JSON-LD contexts and builds a pygeoapi config from the three contexts. pygeoapi's built-in GeoJSON feature provider serves the generated collections; its linked-data response decorator uses the configured contexts for `f=jsonld`. No custom provider plugin is needed because source translation and location association happen explicitly during the build.

The canonical properties include `name`, `country`, `power_mw`, `status`, `n_turbines`, `year`, `dist_coast`, `developer` and `notes`, plus reporting-time, source provenance and location-match fields. National translations are: `farm` → `name`, `capacity_mw` → `power_mw`, `status_aug2026` → normalized `status` plus preserved `status_detail`, and `first_power_or_completion_year` → `year` with its meaning and assumed status recorded. EMODnet keeps `name`, `power_mw`, `status`, `n_turbines`, `year`, and `updateyear`; `dist_coast_m` maps to `dist_coast` in metres. Fields not available from a source remain null.

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
