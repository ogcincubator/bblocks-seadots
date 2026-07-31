# Run with: jq -f extract-representative-sample.jq /path/to/harvest_timeseries_scenario_Scen_M3[539974].geojson
{
  type: "FeatureCollection",
  features: [
    .features[] |
    select((.id == 1 or .id == 42 or .id == 83) and
           (.properties.time == "2020-04-30 00:00:00" or .properties.time == "2020-12-25 00:00:00"))
  ]
}
