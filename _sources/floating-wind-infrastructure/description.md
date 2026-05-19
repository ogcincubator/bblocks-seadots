# Floating-Wind Submerged Infrastructure

OGC API Records / OGC Feature profile describing the submerged geometry of a floating-wind farm layout.

The record carries:
- a top-level GeoJSON Polygon delimiting the farm's licence footprint;
- a `floatingWindInfrastructure.data` block carrying per-unit surface areas (hull, mooring, anchor), the unit count, an aggregate submerged area, and a small sample of per-unit coordinates with submerged area;
- mandatory `data.provenance` distinguishing the values that come from a real engineering source (e.g. NVE assessment for `nUnits` and `unitDesign`) from illustrative values for per-unit areas.

The aggregate `submerged_area_total_m2` is the variable consumed as `A_sub` in the reef-biomass equation `B_reef = sum_i (A_sub · D_pre,i · AF_i · C_t)`.

## Dependency

Inherits the OIM feature shape from `ogc.hosted.iliad.api.features.oim`.

## Required fields for script consumption

The accompanying calculator script (`_sources/experiment/scripts/utsira_reef_biomass.py`) reads `data.aggregate.submerged_area_total_m2`. That field is marked `required` in the schema.
