# Source GeoJSON FeatureCollection -> OIM observation-shaped GeoJSON FeatureCollection.
# The semantic IRI remains provisional until the owner defines bwmus and its unit.
{
  type: "FeatureCollection",
  features: [
    .features[] |
    {
      type: "Feature",
      id: (.id | tostring),
      geometry: .geometry,
      properties: {
        observedProperty: "https://w3id.org/iliad/property/bwmus",
        phenomenonTime: (.properties.time | sub(" "; "T") + "Z"),
        hasResult: {value: .properties.bwmus}
      }
    }
  ]
}
