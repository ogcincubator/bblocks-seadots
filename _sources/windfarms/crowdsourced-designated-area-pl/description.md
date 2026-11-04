# Polish national offshore windfarm source

This block describes the source-stage record exactly as delivered in the exercise CSV: `farm`, `developer`, `capacity_mw`, `status_aug2026`, `first_power_or_completion_year`, and `source`. Its source rows do **not** contain coordinates. Their geometry therefore remains null in the national-source collection.

The exercise applies the separate `location-mapping.json` crosswalk when it builds the harmonized service. Crosswalked locations are explicitly marked as derived from the listed EMODnet records; a project without a defensible EMODnet match remains unlocated.
