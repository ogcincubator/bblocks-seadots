#!/bin/sh
# Contract test for to-emodnet-rsc-mpa.
set -eu
here=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
t="$here/transforms/to_emodnet_rsc_mpa.py"; ref="$here/../../emodnet-protected-area/rsc-mpa/examples/emodnet-reference-helcom.geojson"
a=$(mktemp); b=$(mktemp); trap 'rm -f "$a" "$b"' EXIT
python3 "$t" "$here/examples/helcom-mpas-layer54.geojson" > "$a"
python3 "$t" "$here/examples/helcom-mpa-network-2026-layer190.geojson" --mpa-register "$here/examples/helcom-mpas-layer54.geojson" > "$b"

# 1. Layer 54 output equals the EMODnet records on every non-geometric attribute.
jq -e --slurpfile r "$ref" '
  [.features[] | .properties | del(.shape_leng, .shape_area)] ==
  [$r[0].features[] | .properties | del(.shape_leng, .shape_area)]' "$a" >/dev/null
# 2. Layer 190: only the HELCOM MPA id is published; the other two code schemes are routed.
jq -e '[.features[].id] == [239]
       and (.seadotsTransformReport.routedToNatura2000 | map(.code)) == ["LTSIU0012"]
       and (.seadotsTransformReport.routedToNationallyDesignatedAreas | map(.code)) == ["555638668"]
       and .features[0].properties.status == "Designated and managed" and .features[0].properties.status_yr == 1996' "$b" >/dev/null
# 3. Without the layer-54 register, a layer-190 HELCOM id cannot get a status and is not published.
python3 "$t" "$here/examples/helcom-mpa-network-2026-layer190.geojson" \
  | jq -e '(.features | length) == 0 and (.seadotsTransformReport.noStatusInRegister | map(.code)) == [239]' >/dev/null
echo "ok"
