# Norwegian NVE windfarm extension for EMODnet

This block profiles the [EMODnet windfarm model](../emodnet-compliant-windfarm/)
for an example record from the Norwegian Water Resources and Energy Directorate
(NVE) wind power plant dataset. It demonstrates mapping national fields into the
shared EMODnet properties while keeping useful Norwegian source details.

The NVE dataset covers licensed wind power plants and facilities that have been
or are being processed by NVE. It is a **land-based wind power dataset**. This
example therefore shows reuse of the EMODnet windfarm vocabulary for Norwegian
national data; it does not claim that the Smøla facility is an offshore
EMODnet record.

## Mapping in the example

The example uses NVE's Smøla facility detail page and its associated licensing
case. NVE reports 66 operative turbines, maximum power of 145.8 MW, mean annual
production of 316.9 GWh, the owner, administrative areas, price area, and
turbine models. These map to EMODnet `n_turbines`, `power_mw`, `status`,
`country`, and `year` where the source has a comparable value. NVE's original
licensing status (`Konsesjon gitt`) is retained separately from the mapped
operating status (`Production`), since a licence decision and a facility's
operating state describe different things.

The NVE facility page provides details but not a GeoJSON geometry. Accordingly,
the worked example has `geometry: null`; the NVE windfarm GIS distribution must
provide the geometry for a mapped feature. `dist_coast` and `type_inst` are also
null because this onshore source does not provide equivalent EMODnet offshore
values.

The extension fields retain NVE's facility identifier, licence status,
operational date, owner, counties, municipalities, price area, mean annual
production, turbine details, and links to the facility and licensing records.

## Sources

- [NVE Windkraftverk dataset](https://data.norge.no/nb/datasets/363af211-1914-3814-a365-8439d12466cf/vindkraftverk)
- [NVE Smøla windfarm details](https://www.nve.no/energi/energisystem/vindkraft-paa-land/data-for-utbygde-vindkraftverk-i-norge/vindkraftverk-sider/vindkraftverk/?id=9591)
- [NVE Smøla licensing case](https://www.nve.no/konsesjon/konsesjonssaker/konsesjonssak?id=3&type=A)
