# IMR Benthic Biomass Observations

This block contains the raw IMR / MAREANO Marbunn catch-sample point features
used as the source material for aggregate benthic biomass summaries.

The example is a GeoJSON `FeatureCollection`. Each feature is an individual
Marbunn sample point, carrying the source species query, cruise identifier,
gear/equipment, count and weight fields where present in the upstream payload.

The companion block `benthic-biomass-density-imr` keeps the aggregate
SOSA/OIM observation derived from these raw features.

## Transform

`transforms/to_benthic_biomass_density_mareano.py` converts this raw
FeatureCollection into the `benthic-biomass-density-mareano` aggregate
observation profile. The transform is declared in `transforms.yaml`, converts
sample weights in kg into point densities using explicit gear-area assumptions,
then extrapolates each taxon over the AOI with inverse distance weighting
(IDW). The output provenance records the assumptions and notes that Ordinary
Kriging or Regression-Kriging would be preferable once variograms and covariates
are available.
