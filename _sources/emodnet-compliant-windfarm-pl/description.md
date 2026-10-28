# Polish windfarm extension for EMODnet

This independent Building Block translates Polish national windfarm pipeline records and EMODnet windfarm records into the EMODnet windfarm property vocabulary. The shared fields retain the base block names (`power_mw`, `status`, `year`, `updateyear`, `n_turbines`, `type_inst`, `dist_coast`, and `notes`). It adds generic fields for project name and developer, the reporting date and meaning of a year, and dataset and record provenance.

Input-specific column labels are not carried into the harmonized output. Their values are translated. For example, a national `capacity_mw` value becomes `power_mw`; a source status such as `In planning (auction...)` becomes the normalized controlled status `Planned`, while its full wording is retained in `status_detail`; and `status_aug2026` is represented by generic `status`, `status_detail`, `status_as_of`, and `updateyear` properties.

The schema accepts complete EMODnet base features or sparse harmonized features. This block depends on the base model rather than claiming to be a strict profile: national pipeline sources do not provide every EMODnet attribute. `dist_coast` is expressed in metres, matching the EMODnet input field. Location status and reference terms distinguish source-provided geometry, EMODnet-mapped locations, approximate public-source locations, and unmatched records.


The target also carries `source_type`, `location_status`, `location_method`, and `location_emodnet_ids`. A national location derived from one or more EMODnet sites is represented by that site or their centroid, with the crosswalk IDs and method retained. A national project without an identifiable EMODnet location remains `geometry: null` and `location_status: unmatched`.
