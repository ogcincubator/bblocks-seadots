# Baltic SES hands-on exercise (1 hour)

Jupyter notebook for the SEAtwins Symposium SES modelling training (SEADOTs).
It runs the fisheries + windmills + public model from *Case-example II.xlsx* on real data:
Baltic sprat (ICES spr.27.22-32, 2025 assessment) and the Polish offshore wind pipeline.

## Run
    pip install numpy pandas matplotlib requests jupyterlab
    jupyter lab baltic_ses_exercise.ipynb

The notebook first tries the live ICES SAG API and the EMODnet Human Activities WFS.
Without internet set `LIVE = False` in part 0; the snapshot in `data/` (fetched 26 Oct 2026) is used.
The wind-farm map uses a clipped Natural Earth coastline snapshot, so it also works offline. The delivered notebook is already executed, so every figure is visible before running (run the map cell to refresh its updated coastline plot).

## Optional extension (about 30 min): `baltic_ses_spatial_extension.ipynb`
Joins geographically distributed data to the individual wind farm sites:
ERA5 hourly 100 m wind 2020-2024 (Open-Meteo) gives a capacity factor per site,
marine Natura 2000 sites (EMODnet) and OBIS records of seaducks, divers and harbour porpoise give a sensitivity index,
and three siting portfolios of the same capacity are run through the SES model.
It imports model calculations from `ses_model.py`; the notebook loads its own input files and runs those calculations explicitly. `LIVE = False` by default because
Open-Meteo rate-limits per IP address, which a training room shares.

## Separate data integration exercise: `windfarm-data-integration/`
Compare the national and EMODnet windfarm source collections with a harmonized pygeoapi/JSON-LD service. The exercise includes source and target Building Blocks, explicit field translations, and a location crosswalk for national records that have no coordinates. See [the exercise guide](windfarm-data-integration/README.md).

## Files
- `baltic_ses_exercise.ipynb` - the exercise (executed)
- `baltic_ses_spatial_extension.ipynb` - the spatial extension (executed)
- `ses_model.py` - shared SES equations, calibration transformations, scenario rules, and present-value calculations; it does not load calibration datasets
- `ses_spatial.py` - pure site-level wind, biodiversity, and portfolio calculations; the spatial notebook loads the underlying datasets
- `data/era5_wind100m_hist_2020-2024.csv` - hourly wind speed histograms (1 m/s bins) for 26 farm sites and 133 sea cells
- `data/obis_sensitive_species_grid025_2026-10-26.csv` - OBIS records of 5 species per 0.25 degree cell
- `data/emodnet_natura2000_PL_marine_2026-10-26.geojson` - 5 marine Natura 2000 sites (simplified outlines)
- `data/ices_sprat_spr.27.22-32_2025_summary.csv` - ICES SAG SummaryTable, assessment key 20915
- `data/ices_sprat_spr.27.22-32_2025_refpoints.csv` - ICES reference points
- `data/emodnet_windfarms_poland_2026-10-26.csv` - EMODnet `emodnet:windfarms`, Poland
- `data/ne_10m_coastline_PL_Baltic.geojson` - Natural Earth 1:10m coastline, clipped to the Polish Baltic map extent (public domain)
- `data/polish_offshore_wind_pipeline.csv` - national reporting, gramwzielone.pl 26 Aug 2026
- `data/economic_inputs.csv` - prices, costs and assumptions, each tagged data / assumption with its source

## Check
Part 1 asserts that the Python model reproduces the Excel present value (9.2208) exactly.

## Bonus section 6: semantic annotation of the model inputs
`data/model_inputs.jsonld` describes every model parameter with DCAT, PROV-O, SKOS, I-ADOPT and QUDT terms
(namespace `urn:baltic-ses:`, as in the GeoJSON-LD wind-farm cell). Section 6 of the main notebook uses it to
re-derive the unit conversions, check species and spatial-scope joins, and detect newer source editions.
It writes `data/model_run_provenance.jsonld`. `rdflib` is optional (only for the SPARQL view).
- `data/ices_sprat_spr.27.22-32_2026_summary.csv`, `..._2026_refpoints.csv` - ICES 2026 assessment (key 22378),
  used only in section 6 to show what the newer edition changes; parts 1-5 still use the 2025 assessment.
