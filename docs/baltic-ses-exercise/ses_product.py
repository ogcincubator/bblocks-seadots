"""Write the Baltic production exercise outputs as a GeoPackage and STAC/ODD records."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import geopandas as gpd
import pandas as pd
from shapely.geometry import MultiPoint, mapping


INPUTS = [
    ("ICES sprat assessment summary, 2025", "ices_sprat_spr.27.22-32_2025_summary.csv", "Columns Year, SSB, Catches, Recruitment and assessment ranges; Year selects the annual sequence, SSB and Catches are divided by 1,000,000 to Mt for the stock equation and growth fit."),
    ("ICES sprat reference points, 2025", "ices_sprat_spr.27.22-32_2025_refpoints.csv", "Columns StockKeyLabel, AssessmentKey, AssessmentYear, Blim, Bpa, MSYBtrigger, FMSY and Fpa; biomass reference points are converted from tonnes to Mt and feed the ICES harvest rule."),
    ("Economic inputs", "economic_inputs.csv", "Columns parameter, value, unit, status, source; parameter/value supply fish price and costs, wind auction price, discount rate, and SES benefit parameters. Status distinguishes DATA from ASSUMPTION; source records provenance."),
    ("Polish offshore wind pipeline (common-windfarm-designated-area)", "polish_offshore_wind_pipeline_windfarm_areas.geojson", "GeoJSON FeatureCollection in the common-windfarm-designated-area block, produced by the crowdsourced-designated-area-pl transform from polish_offshore_wind_pipeline.csv (gramwzielone.pl, 26 Aug 2026); properties name, power_mw and year define the contracted investment path and capacity weights, same_as links each project to its EMODnet records. Baltic West is excluded from that path."),
    ("Farm and turbine assignment", "farm_turbine_assignment.csv", "Columns project, wind_site, share_of_project, turbine_model, unit_mw, hub_m, layout, status, note; assigns sites to projects and sets turbine/hub-height inputs."),
    ("Turbine specifications", "turbine_specs.csv", "Columns model, manufacturer, rated_kw, rotor_d_m, swept_area_m2, cut_in_ms, rated_speed_ms, cut_out_ms, power_curve, status, source; defines turbine power/thrust curve bounds and rotor geometry."),
    ("OpenStreetMap wind turbines (common-windfarm-turbine)", "osm_polish_offshore_wind_turbines.geojson", "GeoJSON FeatureCollection in the common-windfarm-turbine block, produced by the windfarm-openstreetmap to-windfarm-turbine transform from the OSM API map response of 27 Oct 2026; properties ref, model, rotor_diameter_m, hub_height_m and windfarm assign turbines to wind sites and drive the wake calculation. ODbL 1.0."),
    ("OpenStreetMap wind farm areas (common-windfarm-designated-area)", "osm_polish_offshore_wind_windfarm_areas.geojson", "GeoJSON FeatureCollection in the common-windfarm-designated-area block, produced by the windfarm-openstreetmap to-windfarm-designated-area transform from the same OSM response; farm outlines shown on the layout map. ODbL 1.0."),
    ("EMODnet wind farm points (common-windfarm-designated-area)", "emodnet_windfarms_PL_windfarm_areas.geojson", "GeoJSON FeatureCollection in the common-windfarm-designated-area block, produced by the windfarm-designated-area-emodnet transform from the EMODnet WFS emodnet:windfarms response of 30 Oct 2026; compared with the national projects through their same_as links and shown on the layout map."),
    ("EMODnet wind farm zones (common-windfarm-designated-area)", "emodnet_windfarmspoly_PL_windfarm_areas.geojson", "GeoJSON FeatureCollection in the common-windfarm-designated-area block, produced by the windfarm-designated-area-emodnet transform from the EMODnet WFS emodnet:windfarmspoly response of 30 Oct 2026; planning zones shown on the layout map."),
    ("Wind-speed histograms by height", "wind_speed_hist_by_height_2023-2025.csv", "Columns site, lon, lat, source, height_m, n_hours, mean_ms, counts_0_to_30ms; each count is hours in a 1 m/s speed bin, by source (ICON-EU, DMI HARMONIE-AROME, ERA5), height and site. Drives gross production."),
    ("ICON-EU hub-height wind roses", "wind_rose_hubheight_icon_eu_2023-2025.csv", "Columns site, source, height_m, sector_deg, counts_0_to_30ms; binned hours by wind direction and speed at hub height, used for directional Jensen wake losses."),
    ("IEA 15 MW reference power curve", "iea15mw_reference_power_curve.csv", "Columns wind_speed_ms, power_kw, cp, thrust_kn, ct; supplies reference curve shape for commercial turbine curve reconstructions."),
]


def write_product(*, data_dir, output_dir, turbines, assignment, summary, gross,
                  wakes, projects, scenario_results, cf_grid, pv_grid,
                  contracted_cf, availability, electrical, wake_k):
    """Persist computed data and create a STAC Item with an ODD protocol record."""
    data_dir, output_dir = Path(data_dir), Path(output_dir)
    missing = [filename for _, filename, _ in INPUTS if not (data_dir / filename).is_file()]
    if missing:
        raise FileNotFoundError(f"Model input snapshots not found under {data_dir}: {', '.join(missing)}")
    output_dir.mkdir(parents=True, exist_ok=True)
    gpkg = output_dir / "baltic-production.gpkg"
    for path in (gpkg, output_dir / "odd-model-description.json"):
        if path.exists():
            path.unlink()

    # Attach farm-level model estimates and the gross CF estimate to each turbine.
    turbine_results = turbines.copy()
    site_to_project = assignment.set_index("wind_site")["project"]
    turbine_results["project"] = turbine_results["wind_site"].map(site_to_project)
    turbine_results["wake_efficiency"] = turbine_results.wind_site.map(wakes["in the cluster"])
    turbine_results["gross_capacity_factor"] = turbine_results.wind_site.map(gross["turbine curve, ICON hub"])
    turbine_results["net_capacity_factor"] = turbine_results["project"].map(projects["net_cf"])
    turbine_results["project_capacity_mw"] = turbine_results["project"].map(projects["MW"])
    turbine_results["availability_assumption"] = availability
    turbine_results["electrical_efficiency_assumption"] = electrical
    turbine_results["wake_decay_assumption"] = wake_k
    turbine_results.to_file(gpkg, layer="turbines", driver="GPKG", index=False)

    # A MultiPoint geometry makes the farm-level summary spatial while retaining its project metrics.
    farm_rows = []
    for project, result in projects.iterrows():
        site_names = assignment.loc[assignment.project == project, "wind_site"]
        points = turbine_results.loc[turbine_results.wind_site.isin(site_names), "geometry"]
        farm_rows.append({"project": project, **result.to_dict(),
                          "geometry": MultiPoint(list(points)) if len(points) else None})
    farms = gpd.GeoDataFrame(farm_rows, geometry="geometry", crs=turbines.crs)
    farms.to_file(gpkg, layer="farm_model_results", driver="GPKG", index=False)

    # Preserve detailed, non-spatial scenario and sensitivity tables as machine-readable CSV assets.
    scenarios_path = output_dir / "scenario_present_values.csv"
    scenario_results.to_csv(scenarios_path, index_label="scenario")
    cf_path = output_dir / "capacity_factor_sensitivity.csv"
    cf_grid.to_csv(cf_path, index_label="wind data / curve")
    pv_path = output_dir / "wind_present_value_sensitivity.csv"
    pv_grid.to_csv(pv_path, index_label="wind data / curve")
    gross_path = output_dir / "gross_capacity_factors.csv"
    gross.to_csv(gross_path, index_label="wind site")
    summary_path = output_dir / "layout_summary.csv"
    summary.to_csv(summary_path, index_label="wind site")

    odd = {
        "id": "urn:baltic-ses:odd:baltic-production-extension-v1",
        "type": "Feature",
        "geometry": None,
        "time": {"date": datetime.now(timezone.utc).date().isoformat()},
        "properties": {
            "type": "SoftwareSourceCode",
            "title": "Baltic SES production extension — ODD model description",
            "description": "ODD Protocol record for the Baltic offshore-wind production extension and its coupling to the fishery–wind–public SES model.",
            "language": {"code": "en"},
            "license": "https://creativecommons.org/licenses/by/4.0/",
            "keywords": ["Baltic Sea", "offshore wind", "surplus production", "ODD", "STAC", "GeoPackage"],
            "odd": {
                "purpose": "Estimate turbine- and farm-level offshore wind energy production for the Polish Baltic project pipeline, account for wake losses, and pass the capacity-weighted capacity factor into the coupled fishery–wind–public model to compare present values.",
                "patterns": [
                    {"name": "ICES sprat stock history", "description": "ICES SSB, catches and recruitment time series used to fit the logistic surplus-production curve.", "reference": "https://www.ices.dk/data/data-portals/Pages/Stock-Assessment-Graphs.aspx"},
                    {"name": "Mapped wind turbine layouts", "description": "OSM locations and turbine tags for mapped projects; layout geometry determines directional Jensen wake losses.", "reference": "https://www.openstreetmap.org/copyright"}
                ],
                "entities": [
                    {"name": "Offshore wind turbine", "entityType": "agent", "stateVariables": [
                        {"name": "location", "type": "Point", "unit": "WGS 84", "description": "OpenStreetMap turbine foundation location."},
                        {"name": "ratedPower", "type": "real", "unit": "MW", "description": "Turbine rated electrical power."},
                        {"name": "grossCapacityFactor", "type": "real", "unit": "1", "range": "[0,1]", "description": "Energy yield before wakes, availability and electrical losses."},
                        {"name": "wakeEfficiency", "type": "real", "unit": "1", "range": "[0,1]", "description": "Energy remaining after modeled wake losses."},
                        {"name": "netCapacityFactor", "type": "real", "unit": "1", "range": "[0,1]", "description": "Capacity factor after wake, availability and electrical losses."}
                    ], "scales": {"spatial": "individual turbine points and farm clusters in the Polish Baltic Sea", "temporal": "annual model inputs and 2025–2050 SES horizon"}},
                    {"name": "Sprat stock and fishery", "entityType": "resource", "stateVariables": [
                        {"name": "SSB", "type": "real", "unit": "Mt", "description": "Spawning-stock biomass, converted from ICES tonnes."},
                        {"name": "catch", "type": "real", "unit": "Mt yr-1", "description": "Annual catch, converted from ICES tonnes."}
                    ], "scales": {"spatial": "ICES spr.27.22-32 stock area", "temporal": "annual; calibrated on 1974 onward data"}}
                ],
                "processOverview": {"scheduling": "Deterministic annual SES simulation; wind-resource and wake calculations are deterministic aggregations over supplied histograms and turbine layouts.", "processes": [
                    {"name": "Reconstruct turbine layouts", "executedBy": "production extension", "description": "Select generator nodes from OSM and assign them to wind sites with explicit reference/relation/model rules."},
                    {"name": "Estimate wind production", "executedBy": "production extension", "description": "Apply reconstructed power curves to wind-speed histograms at turbine hub height to estimate gross capacity factors."},
                    {"name": "Estimate wakes and net output", "executedBy": "production extension", "description": "Use directional wind roses and Jensen/Park wake geometry, then multiply by availability and electrical efficiency."},
                    {"name": "Run coupled SES model", "executedBy": "SES model", "description": "Feed contracted-pipeline capacity-weighted capacity factor and investment path into the fishery, wind-benefit and passive-use model; calculate discounted present values."}
                ]},
                "designConcepts": {
                    "basicPrinciples": "Logistic surplus production for fish stock; wind power curves applied to hourly-frequency histograms; Jensen/Park engineering wake model; capacity-factor weighted energy and discounted SES benefits.",
                    "emergence": "Farm output and cluster losses emerge from turbine locations, turbine specifications, wind distributions and directional interactions.",
                    "adaptation": "None. Turbines, fisheries rule and investment pathway do not adapt during a run.",
                    "objectives": "Compare discounted wind, fishery and passive-use benefits under the contracted wind pipeline and harvest rule.",
                    "learning": "None.",
                    "prediction": "No forecasting by agents; supplied wind histograms represent 2020–2025 weather-model periods and are used as production climatologies.",
                    "sensing": "No agents sense the environment.",
                    "interaction": "Turbines interact through directional wakes; wind investment affects fish growth and fishing costs in the coupled SES equations.",
                    "stochasticity": "None within a run. Uncertainty is explored through alternative wind datasets and power-curve reconstructions.",
                    "collectives": "Turbines are grouped by wind site and national project; mapped sites form a cluster for wake analysis.",
                    "observation": "GeoPackage turbine and farm layers; layout, gross/net capacity-factor tables; scenario present values; capacity-factor and present-value sensitivity tables."
                },
                "initialization": {"description": "The fish stock starts from the 2025 ICES assessment state; investment follows the contracted Polish offshore pipeline, excluding Baltic West. Turbine positions and specifications come from the bundled OSM snapshot, assignment table and turbine-specification table.", "links": [{"href": "../../data/ices_sprat_spr.27.22-32_2025_summary.csv", "title": "ICES 2025 sprat summary", "type": "text/csv"}]},
                "inputData": [
                    {"name": name, "description": description, "source": f"../../data/{filename}", "format": "application/geo+json" if filename.endswith(".geojson") else "text/csv"}
                    for name, filename, description in INPUTS
                ],
                "outputData": [
                    {"name": "Baltic production GeoPackage", "description": "Turbine point layer with modeled wake and capacity-factor attributes, and farm MultiPoint layer with model output.", "source": "baltic-production.gpkg", "format": "application/geopackage+sqlite3"},
                    {"name": "Scenario and sensitivity tables", "description": "Present-value comparisons, gross capacity factors, and capacity-factor/PV sensitivity grids.", "source": "scenario_present_values.csv", "format": "text/csv"}
                ],
                "submodels": [
                    {"name": "Wind production and wakes", "equations": "CF_gross = sum_bin(hours_bin × power(speed_bin)) / (sum_bin(hours_bin) × rated_power); wake deficit follows Jensen/Park geometry; CF_net = CF_gross × wake_efficiency × availability × electrical_efficiency.", "parameterization": f"Power curves are bounded reconstructions anchored to the IEA 15 MW reference curve and commercial turbine specifications. Jensen wake decay k={wake_k}; availability={availability}; electrical efficiency={electrical}. Wind distributions are bundled ICON-EU/DMI HARMONIE-AROME/ERA5 histograms and ICON-EU direction roses. Baltic West receives a proxy average modeled wake efficiency because no turbine layout is assigned. This run's capacity-weighted CF for the contracted pipeline is {contracted_cf:.4f}.", "links": [{"href": "../../ses_production.py", "rel": "describedby", "title": "Wind production and wake calculation source"}]},
                    {"name": "Coupled fishery–wind–public SES", "equations": "G(x,w)=(alpha-epsilon_1*w)*x-beta*x^2; x_(t+1)=x_t+G(x_t,w_t)-q_t; w_(t+1)=w_t+I_(w,t)-delta*w_t; PV=sum_t (b_f+b_w+b_p)_t/(1+r)^(t+1).", "parameterization": "Fish growth is fitted to ICES 2025 sprat SSB and catch data. Harvest follows ICES reference points. Investment follows the national contracted pipeline excluding Baltic West. Economic values and their status/source are in economic_inputs.csv. The extension capacity factor is capacity weighted over the contracted projects; compare the notebook scenario table for present values.", "links": [{"href": "../../ses_model.py", "rel": "describedby", "title": "Coupled SES equations and simulation source"}]}
                ]
            }
        },
        "links": [{"rel": "describedby", "href": "bblocks://ogc.hosted.seadots.odd-protocol", "type": "application/schema+json", "title": "ODD Protocol record schema"}]
    }
    odd_sections = odd["properties"]["odd"]
    odd_description = [
        "ODD Protocol model description — Overview, Design concepts and Details.",
        "PURPOSE: " + odd_sections["purpose"],
        "PATTERNS: " + " ".join(f"{p['name']}: {p['description']} Reference: {p['reference']}" for p in odd_sections["patterns"]),
        "ENTITIES: " + " ".join(
            f"{entity['name']} ({entity['entityType']}): " + "; ".join(
                f"{v['name']} [{v.get('unit', 'unit not specified')}]: {v['description']}" for v in entity["stateVariables"]
            ) + f" Scales: {entity['scales']['spatial']}; {entity['scales']['temporal']}."
            for entity in odd_sections["entities"]
        ),
        "PROCESS OVERVIEW: " + odd_sections["processOverview"]["scheduling"] + " " + " ".join(
            f"{p['name']}: {p['description']}" for p in odd_sections["processOverview"]["processes"]
        ),
        "DESIGN CONCEPTS: " + " ".join(f"{key}: {value}" for key, value in odd_sections["designConcepts"].items()),
        "INITIALIZATION: " + odd_sections["initialization"]["description"],
        "INPUT DATA: " + " ".join(
            f"{item['name']} ({item['source']}): {item['description']}" for item in odd_sections["inputData"]
        ),
        "OUTPUT DATA: " + " ".join(
            f"{item['name']} ({item['source']}): {item['description']}" for item in odd_sections["outputData"]
        ),
        "SUBMODELS: " + " ".join(
            f"{item['name']}. Equation: {item['equations']} Parameterization: {item['parameterization']} References: " +
            ", ".join(link["href"] for link in item.get("links", []))
            for item in odd_sections["submodels"]
        ),
    ]

    bounds = turbines.total_bounds
    geometry = mapping(turbines.unary_union.convex_hull)
    stac = {
        "type": "Feature", "stac_version": "1.0.0", "stac_extensions": [],
        "id": "baltic-ses-production-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "geometry": geometry, "bbox": [float(v) for v in bounds],
        "properties": {
            "title": "Baltic SES offshore-wind production model output",
            "description": "\n\n".join(odd_description + ["PROVENANCE AND LICENSING: Source licenses vary by dataset; OpenStreetMap-derived geometry is ODbL 1.0. The linked assets contain every input snapshot, spatial model output, scenario result and sensitivity table for this run."]),
            "datetime": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "start_datetime": "2020-01-01T00:00:00Z", "end_datetime": "2050-12-31T23:59:59Z",
            "license": "various"
        },
        "assets": {
            "data": {"href": "baltic-production.gpkg", "type": "application/geopackage+sqlite3", "title": "Spatial turbine and farm model outputs", "roles": ["data", "result"]},
            "scenario_results": {"href": scenarios_path.name, "type": "text/csv", "title": "Scenario present-value comparison", "roles": ["data", "result"]},
            "capacity_factor_sensitivity": {"href": cf_path.name, "type": "text/csv", "title": "Capacity-factor sensitivity grid", "roles": ["data", "result"]},
            "wind_pv_sensitivity": {"href": pv_path.name, "type": "text/csv", "title": "Wind present-value sensitivity grid", "roles": ["data", "result"]},
            "gross_capacity_factors": {"href": gross_path.name, "type": "text/csv", "title": "Gross capacity factors by site and curve/wind dataset", "roles": ["data", "result"]},
            "layout_summary": {"href": summary_path.name, "type": "text/csv", "title": "Turbine layout and reported capacity comparison", "roles": ["data", "result"]}
        },
        "links": [
            {"rel": "via", "href": "../../baltic_ses_production_extension.ipynb", "type": "application/x-ipynb+json", "title": "Notebook execution"},
            {"rel": "related", "href": "../../ses_production.py", "type": "text/x-python", "title": "Wind production and wake model source"},
            {"rel": "related", "href": "../../ses_model.py", "type": "text/x-python", "title": "Coupled SES model source"},
            {"rel": "describedby", "href": "bblocks://ogc.hosted.seadots.odd-protocol", "type": "application/schema+json", "title": "ODD Protocol record profile; description is embedded in this STAC Item"}
        ]
    }
    for _, filename, description in INPUTS:
        stac["assets"]["input_" + filename.rsplit(".", 1)[0].replace("-", "_").replace(".", "_")] = {
            "href": f"../../data/{filename}", "type": "application/geo+json" if filename.endswith(".geojson") else "text/csv",
            "title": filename, "description": description, "roles": ["input", "metadata"]
        }
    stac_path = output_dir / "stac-item.json"
    stac_path.write_text(json.dumps(stac, indent=2, ensure_ascii=False) + "\n")
    return {"gpkg": gpkg, "stac": stac_path,
            "scenario_results": scenarios_path, "cf_sensitivity": cf_path, "pv_sensitivity": pv_path}
