# OBIS MAREANO Checklist

This block captures a raw OBIS checklist response for selected MAREANO dataset
identifiers:

`https://api.obis.org/v3/checklist?size=10&skip=20&datasetid=d556b9d4-7625-4aa2-894d-441eabae47f7,152259dc-9c20-4c1a-9644-8e4b509d4f73,14fa3c3e-259c-4af9-9314-eee1dc3a119b`

The examples intentionally keep the OBIS payloads as-is:

- `examples/mareano_obis_checklist.json` is a checklist of taxa and occurrence
  record counts.
- `examples/mareano_obis_occurrences.json` is an occurrence response with
  per-observation rows like the OBIS `/occurrence/{id}` endpoint.

The transformer in `transforms/to_benthic_biomass_density_mareano.py` creates a
derived MAREANO biomass-density **proxy** example by normalizing checklist
record counts or occurrence rows. The output provenance records that this is
not a physical kg m-2 biomass measurement.
