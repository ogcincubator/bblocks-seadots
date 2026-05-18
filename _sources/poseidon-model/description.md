# POSEIDON Fisheries Model ODD Record

This building block profiles the local [ODD Protocol Description Record](bblocks://ogc.hosted.seadots.odd-protocol) for the implemented POSEIDON model of ocean fisheries described by Bailey et al. in Sustainability Science and maintained at <https://github.com/poseidon-fisheries/POSEIDON>.

POSEIDON is a coupled human-environment simulation for fisheries policy design. It represents fishing boats as adaptive agents coupled to a spatial fish biomass model, then uses repeated simulation runs and Bayesian optimization to search policy parameter spaces against user-defined objectives.

The implementation is a Java fishery agent-based model licensed under GPL-3.0-or-later. Its current repository README notes that the code is being refactored under the SURIMI project, and points users who want the old tutorial or GUI workflow to the `poseidon-gui` repository. This block therefore records both the published model description and the executable implementation lineage.

The schema keeps the ODD sections as the primary description:

- Overview: purpose, empirical or stylized patterns, entities, and process scheduling.
- Design concepts: adaptation, objectives, sensing, interaction, stochasticity, observation, and the other ODD concepts.
- Details: initialization, input data, and submodels.

The profile adds POSEIDON-specific metadata for:

- explicit input blocks consumed by the implementation;
- policy optimization method, objective function, decision variables, and outputs;
- STAC collections or items used as spatial support assets, using imported STAC building blocks;
- Open Science workflows, experiments, products, and application packages, using imported Open Science building blocks;
- reproducibility notes for run protocols, random seeds, calibration, and implementation status.

## Model Inputs

The implemented model consumes a scenario and related configuration inputs. These are represented as separate building blocks so they can be reused by workflows and validation pipelines:

- `ogc.hosted.seadots.poseidon-input-run-control`: scenario file, policy file, random seed, run length, replicates, and output directory.
- `ogc.hosted.seadots.poseidon-input-scenario`: scenario YAML composition layer.
- `ogc.hosted.seadots.poseidon-input-map`: generated or file-backed spatial map, grid, bathymetry/depth, and STAC spatial assets.
- `ogc.hosted.seadots.poseidon-input-biology`: biomass, abundance, recruitment, growth, mortality, diffusion, OSMOSE, and species parameter inputs.
- `ogc.hosted.seadots.poseidon-input-fleet`: fishers, vessels, gear, behavioural strategies, social network, logbook, and adaptation inputs.
- `ogc.hosted.seadots.poseidon-input-port-market`: ports, landing infrastructure, market prices, and fuel or gas prices.
- `ogc.hosted.seadots.poseidon-input-regulation-policy`: regulations, closures, quotas, gear restrictions, and shocks.
- `ogc.hosted.seadots.poseidon-input-optimization`: base scenario, tunable parameters, objective function, simulation budget, seeds, and replicate strategy.
- `ogc.hosted.seadots.poseidon-input-observation-output`: indicators, output columns, output cadence, and logger selection.

## Imported Building Blocks

The schema is based on `ogc.hosted.seadots.odd-protocol` and imports the following external blocks:

- `ogc.contrib.stac.item`, `ogc.contrib.stac.collection`, and `ogc.contrib.stac.item-prov` for spatial catalog assets and provenance-bearing STAC items.
- `ogc.osc.geodcat-stac-earthcode.workflows`, `ogc.osc.geodcat-stac-earthcode.experiments`, and `ogc.osc.geodcat-stac-earthcode.products` for Open Science catalog metadata.
- `ogc.osc.application-package` for workflow packaging.

## Source

Bailey, R. M., Carrella, E., Axtell, R. et al. (2019). *A computational approach to managing coupled human-environmental systems: the POSEIDON model of ocean fisheries*. Sustainability Science, 14, 259-275. <https://doi.org/10.1007/s11625-018-0579-9>

Implementation repository: <https://github.com/poseidon-fisheries/POSEIDON>
