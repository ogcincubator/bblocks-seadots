#!/bin/sh
set -eu
source_file="$1"
transform_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
output=$(mktemp)
trap 'rm -f "$output"' EXIT
jq -f "$transform_dir/transforms/geojson-to-oim-observation.jq" "$source_file" > "$output"
# Contract: source id, geometry, time, and bwmus are all represented in the output.
jq -e '
  (.features | length) > 0 and
  all(.features[]; .id != null and .geometry.type == "Point" and
      .properties.observedProperty == "https://w3id.org/iliad/property/bwmus" and
      .properties.phenomenonTime != null and .properties.hasResult.value != null)
' "$output" >/dev/null
