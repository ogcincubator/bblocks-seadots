# EMODnet Human Activities windfarm source snapshot

This source-stage block keeps the EMODnet source property names, including `dist_coast_m`, `updateyear`, `lon`, and `lat`. The exercise snapshot is the Poland-filtered WFS-derived CSV bundled with the Baltic SES exercise; refresh it from the WFS before regenerating if a newer source edition is required.

`translation.json` records how the raw properties map into the canonical target. The raw API collection remains available alongside the harmonized collection so users can inspect what changed.
