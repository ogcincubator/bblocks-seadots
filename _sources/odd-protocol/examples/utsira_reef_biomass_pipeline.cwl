cwlVersion: v1.2
$namespaces:
  s: https://schema.org/
  odd: https://w3id.org/ogc/hosted/seadots/odd-protocol#
  eqrel: https://w3id.org/ogc/hosted/seadots/equation-property-relationship#
  indo: https://id3.seadots.eu/indicator/
s:softwareVersion: 0.1.0
s:identifier: https://example.org/norwegian-ses/cwl/utsira-reef-biomass-pipeline-v1
s:name: Utsira reef-biomass pipeline
s:description: >-
  Executable realisation of the one-submodel ODD demonstrator
  `utsira_reef_biomass_demonstrator.json`. Implements the equation
  B_reef = sum_i (A_sub . D_pre,i . AF_i . C_t) by composing one CWL step per
  symbol (A_sub, D_pre,i, AF_i, C_t) plus IO bookends. Default inputs reproduce
  the Utsira Nord licence-polygon run; supplying a different AOI polygon and a
  different infrastructure layout re-targets the pipeline to the surroundings
  of Utsira island without code changes.
s:citation:
  - https://w3id.org/ogc/hosted/seadots/odd-protocol/examples/utsira_reef_biomass_demonstrator
  - https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation
  - https://doi.org/10.5670/oceanog.2020.405
schemas:
  - http://schema.org/version/latest/schemaorg-current-https.rdf

$graph:
  - class: Workflow
    id: utsira_reef_biomass
    label: Utsira reef-associated biomass estimator
    doc: >-
      Sum-over-taxa reef-biomass estimator parameterised by the linked
      equation-property-relationship record. Scatter axis: TaxonGroup index `i`.
    requirements:
      - class: ScatterFeatureRequirement
      - class: SubworkflowFeatureRequirement
      - class: StepInputExpressionRequirement

    inputs:
      aoi:
        label: Area of interest (GeoJSON polygon)
        doc: >-
          Polygon delimiting the study area. Default is the Utsira Nord licence
          polygon used by the ODD demonstrator. Replace with a surroundings
          polygon (e.g. ring around Utsira island, ICES SD 27/29-adjacent
          waters) to re-run for the broader area.
        type: File
        format: https://www.iana.org/assignments/media-types/application/geo+json
        default:
          class: File
          location: aoi/utsira_nord_licence_polygon.geojson
      infrastructure_layout:
        label: Submerged infrastructure layout
        doc: >-
          Per-unit geometry of submerged surfaces (hull + mooring + anchor) for
          the floating-wind units intersecting the AOI. Drives the A_sub
          calculation.
        type: File
        format: https://www.iana.org/assignments/media-types/application/geo+json
        default:
          class: File
          location: infrastructure/utsira_nord_60x15mw.geojson
      equation_record:
        label: Equation-property-relationship record
        doc: >-
          Canonical reef-biomass equation record carrying the symbol table and
          bindings for A_sub, D_pre,i, AF_i, C_t.
        type: string
        default: https://w3id.org/ogc/hosted/seadots/equation-property-relationship/examples/reef-biomass-equation
      taxon_groups:
        label: TaxonGroup index values
        doc: Scientific names iterated by index i in the reef-biomass equation.
        type: string[]
        default:
          - "Mytilus edulis"
          - "Buccinum undatum"
          - "Asterias rubens"
      baseline_density_primary:
        label: Primary baseline benthic biomass density source (MAREANO)
        type: string
        default: https://mareano.no/api/benthic-biomass-density
      baseline_density_fallback:
        label: Fallback baseline benthic biomass density source (IMR)
        type: string
        default: https://www.hi.no/api/benthic-biomass-baseline
      scenario_t0:
        label: Scenario start date (ISO 8601)
        type: string
        default: "2026-05-13"
      colonisation_months:
        label: Months since installation (drives C_t sigmoid)
        type: int
        default: 24

    outputs:
      - id: reef_biomass_geoparquet
        label: Reef-associated biomass — per-cell GeoParquet
        outputSource: step_package/reef_biomass_geoparquet
        type: File
        format: https://geoparquet.org/
      - id: stac_catalog
        label: STAC catalog for the run
        outputSource: step_package/stac_catalog
        type: Directory
      - id: prov_record
        label: PROV-O provenance (JSON-LD) — links to ODD record and equation record
        outputSource: step_package/prov_record
        type: File
        format: https://www.w3.org/TR/json-ld11/

    steps:
      step_compute_a_sub:
        label: Compute A_sub from infrastructure layout
        doc: Symbol A_{sub} — featureOfInterest, quantitykind:Area.
        run: "#compute_submerged_area"
        in:
          aoi: aoi
          infrastructure_layout: infrastructure_layout
        out:
          - a_sub_value

      step_fetch_d_pre:
        label: Fetch D_pre,i per taxon (scatter over i)
        doc: Symbol D_{pre,i} — intensiveQuantity, kg m-2. MAREANO primary, IMR fallback.
        run: "#fetch_baseline_density"
        scatter: taxon
        scatterMethod: dotproduct
        in:
          aoi: aoi
          taxon: taxon_groups
          primary_source: baseline_density_primary
          fallback_source: baseline_density_fallback
        out:
          - d_pre_i

      step_resolve_af:
        label: Resolve AF_i per taxon from the equation record
        doc: Symbol AF_i — adjustmentFactor, dimensionless.
        run: "#resolve_aggregation_index"
        scatter: taxon
        scatterMethod: dotproduct
        in:
          equation_record: equation_record
          taxon: taxon_groups
        out:
          - af_i

      step_compute_c_t:
        label: Compute C_t (default sigmoid saturating at 24 months)
        doc: Symbol C_t — timeCoefficient, dimensionless.
        run: "#compute_colonisation_factor"
        in:
          equation_record: equation_record
          t0: scenario_t0
          months: colonisation_months
        out:
          - c_t_value

      step_apply_equation:
        label: Apply B_reef = sum_i (A_sub . D_pre,i . AF_i . C_t)
        run: "#apply_reef_equation"
        in:
          a_sub: step_compute_a_sub/a_sub_value
          d_pre_i: step_fetch_d_pre/d_pre_i
          af_i: step_resolve_af/af_i
          c_t: step_compute_c_t/c_t_value
          taxa: taxon_groups
        out:
          - b_reef_per_taxon
          - b_reef_total

      step_package:
        label: Package outputs (GeoParquet + STAC + PROV)
        run: "#package_outputs"
        in:
          aoi: aoi
          b_reef_per_taxon: step_apply_equation/b_reef_per_taxon
          b_reef_total: step_apply_equation/b_reef_total
          odd_record: { default: "https://w3id.org/ogc/hosted/seadots/odd-protocol/examples/utsira_reef_biomass_demonstrator" }
          equation_record: equation_record
        out:
          - reef_biomass_geoparquet
          - stac_catalog
          - prov_record

  - class: CommandLineTool
    id: compute_submerged_area
    requirements:
      DockerRequirement:
        dockerPull: ghcr.io/seadots/reef-biomass-tools:0.1.0
      ResourceRequirement:
        coresMax: 2
        ramMax: 2048
    baseCommand: ["compute-submerged-area"]
    inputs:
      aoi: { type: File, inputBinding: { prefix: --aoi } }
      infrastructure_layout: { type: File, inputBinding: { prefix: --layout } }
    outputs:
      a_sub_value:
        type: File
        format: application/json
        outputBinding: { glob: a_sub.json }

  - class: CommandLineTool
    id: fetch_baseline_density
    requirements:
      DockerRequirement:
        dockerPull: ghcr.io/seadots/reef-biomass-tools:0.1.0
      NetworkAccess: { networkAccess: true }
    baseCommand: ["fetch-baseline-density"]
    inputs:
      aoi: { type: File, inputBinding: { prefix: --aoi } }
      taxon: { type: string, inputBinding: { prefix: --taxon } }
      primary_source: { type: string, inputBinding: { prefix: --primary } }
      fallback_source: { type: string, inputBinding: { prefix: --fallback } }
    outputs:
      d_pre_i:
        type: File
        format: application/json
        outputBinding: { glob: d_pre_*.json }

  - class: CommandLineTool
    id: resolve_aggregation_index
    requirements:
      DockerRequirement:
        dockerPull: ghcr.io/seadots/reef-biomass-tools:0.1.0
      NetworkAccess: { networkAccess: true }
    baseCommand: ["resolve-af"]
    inputs:
      equation_record: { type: string, inputBinding: { prefix: --equation } }
      taxon: { type: string, inputBinding: { prefix: --taxon } }
    outputs:
      af_i:
        type: File
        format: application/json
        outputBinding: { glob: af_*.json }

  - class: CommandLineTool
    id: compute_colonisation_factor
    requirements:
      DockerRequirement:
        dockerPull: ghcr.io/seadots/reef-biomass-tools:0.1.0
    baseCommand: ["compute-ct"]
    inputs:
      equation_record: { type: string, inputBinding: { prefix: --equation } }
      t0: { type: string, inputBinding: { prefix: --t0 } }
      months: { type: int, inputBinding: { prefix: --months } }
    outputs:
      c_t_value:
        type: File
        format: application/json
        outputBinding: { glob: c_t.json }

  - class: CommandLineTool
    id: apply_reef_equation
    requirements:
      DockerRequirement:
        dockerPull: ghcr.io/seadots/reef-biomass-tools:0.1.0
    baseCommand: ["apply-reef-equation"]
    inputs:
      a_sub: { type: File, inputBinding: { prefix: --a-sub } }
      d_pre_i: { type: "File[]", inputBinding: { prefix: --d-pre } }
      af_i: { type: "File[]", inputBinding: { prefix: --af } }
      c_t: { type: File, inputBinding: { prefix: --c-t } }
      taxa: { type: "string[]", inputBinding: { prefix: --taxa } }
    outputs:
      b_reef_per_taxon:
        type: File
        format: https://geoparquet.org/
        outputBinding: { glob: b_reef_per_taxon.parquet }
      b_reef_total:
        type: File
        format: application/json
        outputBinding: { glob: b_reef_total.json }

  - class: CommandLineTool
    id: package_outputs
    requirements:
      DockerRequirement:
        dockerPull: ghcr.io/seadots/reef-biomass-tools:0.1.0
    baseCommand: ["package-outputs"]
    inputs:
      aoi: { type: File, inputBinding: { prefix: --aoi } }
      b_reef_per_taxon: { type: File, inputBinding: { prefix: --per-taxon } }
      b_reef_total: { type: File, inputBinding: { prefix: --total } }
      odd_record: { type: string, inputBinding: { prefix: --odd } }
      equation_record: { type: string, inputBinding: { prefix: --equation } }
    outputs:
      reef_biomass_geoparquet:
        type: File
        format: https://geoparquet.org/
        outputBinding: { glob: reef_biomass.parquet }
      stac_catalog:
        type: Directory
        outputBinding: { glob: stac/ }
      prov_record:
        type: File
        format: https://www.w3.org/TR/json-ld11/
        outputBinding: { glob: prov.jsonld }
