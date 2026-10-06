#!/bin/sh
# Contract test for to-emodnet-nationally-designated-area.
set -eu
here=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
out=$(mktemp); trap 'rm -f "$out"' EXIT
python3 "$here/transforms/to_emodnet_nda.py" "$here/examples/naturvern-omrade-source.geojson" \
  --retrieved 2026-09-30 --emodnet-reference "$here/../../emodnet-protected-area/nationally-designated-area/examples/emodnet-reference-no.geojson" > "$out"
ref="$here/../../emodnet-protected-area/nationally-designated-area/examples/emodnet-reference-no.geojson"

# 1. Every feature carries exactly the 34 EMODnet attributes (+ none of the source's own fields).
jq -e 'all(.features[]; (.properties|keys|length) == 34 and (.properties|has("verneform")|not))' "$out" >/dev/null
# 2. Tauterryggen equals the EMODnet record on every field the source can supply.
jq -e --slurpfile r "$ref" '
  (.features[] | select(.properties.nationalid=="VV00003080") | .properties) as $o
  | ($r[0].features[] | select(.properties.nationalid=="VV00003080") | .properties) as $e
  | all(["natdaid","countrycod","country","regioncode","sitename","legalfound","localid","namespace","geomtype",
         "coast_mar","nationalid","designated","designatio","iucncatego","iucndesc","sitearea","majorecosy",
         "marinearea","spatialdat","spatialres","pslocalid","psnamespac"][]; $o[.] == $e[.])' "$out" >/dev/null
# 3. The known EMODnet error for Møysalen is reported, with the source values kept in the view.
jq -e '.seadotsTransformReport.differsFromEMODnet
       | any(.nationalid=="VV00002196" and .fields.designatio.source=="NO01" and .fields.designatio.emodnet=="NO02"
             and .fields.iucncatego.source=="II" and .fields.natdaid.source==183154)' "$out" >/dev/null
# 4. The CSV crosswalk and the published SKOS crosswalk agree.
for vf in $(tail -n +2 "$here/crosswalk/verneform-designation.csv" | cut -d, -f1); do
  grep -q "^vf:$vf a skos:Concept" "$here/crosswalk/crosswalk.ttl"
done
echo "ok"
