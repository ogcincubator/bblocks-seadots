# EMODnet Human Activities — source-to-block mapping

This mapping turns each source in [the source inventory](data_sources_for_EMODnet_Human_Activities.md) into an interoperable publication profile. A *source profile* validates the data itself; all profiles also use the shared catalogue/metadata profile below. “Proposed” means that the block should be authored in this register; it is not a claim that EMODnet has already adopted that exact profile.

## Shared requirements

Every published dataset shall have:

- **`ogc.hosted.seadots.catalog-data`** (existing), which reuses GeoDCAT/OGC API Records, STAC and provenance metadata.
- ISO 19115-style discovery metadata, including lineage, temporal and spatial extent, responsible organisation, licence/use constraints, update date, distribution links and quality information. EMODnet explicitly harmonises metadata against EU/INSPIRE and international/ISO standards, and requires attribution/use restrictions from the dataset metadata.
- An INSPIRE-compatible metadata record and an EMODnet catalogue/WFS distribution. EMODnet Human Activities currently publishes vector data through WFS; GeoJSON (`application/geo+json`) is the exchange/download representation.
- EPSG:4326 longitude/latitude coordinates in GeoJSON. Preserve the provider's native CRS in the provenance metadata whenever a transformation is made.

## Generalised mapping of EMODnet ingestion requirements to Blocks

The [Marine Data Management Guidelines](https://emodnet.ec.europa.eu/en/data-ingestion#marine-data-management-guidelines) require an archiving format that is software-independent, self-describing enough to process an isolated dataset, exchange-compatible, able to retain history/comments, and consistently structured. They also require information about what, where, when, how, who, processing and quality. The mapping below expresses those requirements as a small reusable stack rather than repeating them in every thematic profile.

| EMODnet requirement | Reusable Block | Status | Minimum contract supplied by the Block | Applied by |
| --- | --- | --- | --- | --- |
| A dataset package, complete discovery metadata and links to data/documentation | `ogc.hosted.seadots.catalog-data` | Existing | GeoDCAT/OGC API Records/STAC catalogue record; title, description, temporal extent, distributions, `describedby` link, source/provenance links and declared convention. | **All** source profiles. |
| Computer-independent, exchange-compatible distribution with required format fields | `ogc.hosted.seadots.marine-distribution` | Proposed | A distribution has media type, encoding, file/schema version, download/access URL, checksum/size where available, CRS and a conformance link. It profiles DCAT distribution metadata; it does not prescribe one file format. | **All** source profiles; GeoJSON, CSV, WFS, WCS and provider APIs. |
| What was measured or counted, plus its unit | `ogc.hosted.seadots.marine-observed-property` | Proposed; may reuse `ogc.hosted.seadots.oim-variable-observation` for numeric observations | Controlled observed-property URI, value type, unit URI and, where applicable, species/taxon and vessel/asset class. Use a profile-specific code list only for values that are genuinely domain-specific. | Fishing measures, AIS density, port metrics, bathymetry and wind-farm capacity/counts. |
| Where and when data were collected or are valid | `ogc.hosted.seadots.marine-spatiotemporal-extent` | Proposed | Geometry or spatial coverage, CRS, vertical datum/reference where relevant, acquisition/validity period, time-zone declaration and spatial/temporal resolution. | **All** profiles; static assets use validity dates, event data use event time, grids use cell geometry and reporting period. |
| How the data were obtained | `ogc.hosted.seadots.marine-acquisition-method` | Proposed | Sampling/derivation method, instrument or source system, platform/processing-system identifier, method version and a documentation link. | AIS/VMS derivatives, logbooks, bathymetry and stakeholder wind-farm data. |
| Persistent references to station, event, vessel, asset, dataset and organisation | `ogc.hosted.seadots.marine-identifier-and-agent` | Proposed | Stable identifiers, identifier scheme, responsible organisation and role (originator, custodian, processor, publisher), and contact/reference link. Personal contact information is excluded from public output. | **All** profiles. |
| Processing, calibration, aggregation or transformations applied to source data | `ogc.hosted.seadots.marine-lineage` | Proposed | Source dataset references, ordered processing steps, software/algorithm and version, parameters, execution time and derived-product relation. This specializes PROV-O relations already available through `catalog-data`. | Derived wind-farm compilation, AIS density, ICES/GFW effort, German intensity and bathymetry derivatives. |
| Quality information, known problems and user-facing comments | `ogc.hosted.seadots.marine-quality-and-notes` | Proposed | Quality measure/result, validation status, positional/temporal uncertainty where available, known limitations, free-text comment/history and confidentiality/generalisation statement. | **All** profiles; mandatory for derived and access-restricted products. |
| Standard terminology instead of unconstrained free text where a vocabulary exists | `ogc.hosted.seadots.marine-vocabulary-binding` | Proposed | A field is bound to a resolvable vocabulary/concept scheme, code and label; allows a documented free-text fallback only when no suitable term exists. | **All** profiles; notably status, designation, gear, species, vessel type and units. |
| CSV that remains intelligible outside its original system | `ogc.hosted.seadots.catalog-data-tabular` + `ogc.hosted.seadots.geoparquet-header` | Existing | Catalogue metadata plus CSVW/table-column semantics; GeoParquet structural metadata when a tabular dataset has geometry. | Fisheries events, vessel register, port traffic and any CSV/grid distribution. |

### Composition rule

Each thematic source Block in the next section shall import `catalog-data`, `marine-distribution`, `marine-spatiotemporal-extent`, `marine-identifier-and-agent`, `marine-quality-and-notes` and `marine-vocabulary-binding`. It shall additionally import:

- `marine-observed-property` when it contains a measured/count/estimated value;
- `marine-acquisition-method` when collection or derivation method affects interpretation;
- `marine-lineage` when it is a harmonised, aggregated or computed product; and
- `catalog-data-tabular` (and `geoparquet-header` when applicable) for CSV or GeoParquet delivery.

This avoids a separate “metadata block” for every thematic dataset while retaining the information EMODnet identifies as necessary for processing, archiving and integration. The source profile only adds its thematic geometry and attributes—for example wind-farm status, fishing gear, AIS vessel class or protected-area designation.

## Building Blocks

| Block | Status | Data model and relevant conventions | Used by |
| --- | --- | --- | --- |
| `ogc.hosted.seadots.emodnet-compliant-windfarm` | Existing | EMODnet Human Activities windfarms WFS/XSD field set; GeoJSON RFC 7946; INSPIRE Energy Resources. Requires `country`, `n_turbines`, `power_mw`, `status`, `type_inst`, year information and geometry. | Unified three-area wind parks; German Bight monopile locations. |
| `ogc.hosted.seadots.emodnet-protected-area` | Proposed | INSPIRE Protected Sites; GeoJSON feature geometry; nationally designated / Natura 2000 designation vocabulary; protected-area identifier, designation, authority, legal status, dates and source licence. | Naturbase protected areas / marine MPAs. |
| `ogc.hosted.seadots.emodnet-fishing-activity-event` | Proposed | Event-level logbook/landing model; ISO 8601 time; FAO 3-alpha species code and scientific-name/AphiaID when available; vessel identifier, landing port/municipality, gear, quantity/unit, spatial unit or geometry, confidentiality flag. CSVW metadata is mandatory for CSV distribution. | Norwegian Fiskeridirektoratet landings linked to vessels; Swedish licensed-fisher logbook data. |
| `ogc.hosted.seadots.emodnet-fishing-effort-grid` | Proposed | Spatiotemporal grid/area product; GeoJSON polygons or a coverage; declared grid CRS/resolution, period, effort measure/unit, gear/fleet/species dimensions, aggregation method, disclosure control and source. CSVW metadata for CSV; use OGC API Coverages/WCS if delivered as a gridded coverage. | ICES VMS/logbook effort products; German Bight fisheries intensity; Global Fishing Watch public fishing effort. |
| `ogc.hosted.seadots.emodnet-fishing-vessel-register` | Proposed | EU Community Fishing Fleet Register semantics; stable CFR/external registration identifier, flag state, vessel characteristics, active dates and register provenance. It is a registry table, not a fishing-event or effort-grid profile. CSVW metadata is mandatory for CSV distribution. | Community Fishing Fleet Register. |
| `ogc.hosted.seadots.emodnet-vessel-density-grid` | Proposed | EMODnet vessel-density methodology; AIS message semantics (ITU-R M.1371 where raw AIS is retained); a regular cell geometry, vessel class, reporting period, statistic/unit, source coverage and aggregation method. GeoJSON for vector grid, or Coverage/WCS for raster output. | Kystverket/BarentsWatch historical AIS-derived density; German Bight monthly AIS vessel-density maps. |
| `ogc.hosted.seadots.emodnet-port-traffic` | Proposed | Port traffic/port-call time series; UN/LOCODE port identifier, ISO 8601 reporting period, vessel class, arrivals/calls/tonnage metric, unit, source and confidentiality. Use geometry for the port and CSVW for tabular observations. | German Bight port traffic (Helgoland, Cuxhaven, etc.). |
| `ogc.hosted.seadots.emodnet-marine-infrastructure-route` | Proposed | INSPIRE Utility and Government Services concepts plus EMODnet Human Activities cables/pipelines conventions; line geometry, infrastructure type, operator/owner where releasable, status, source/update date and positional accuracy. | Kartverket/Geonorge cable and pipeline routes. |
| `ogc.hosted.seadots.emodnet-bathymetry-coverage-reference` | Proposed | EMODnet Bathymetry DTM exchange specification for an interoperable gridded elevation product; use WCS/OGC API Coverages or a referenced provider service. Do **not** apply it to cable/pipeline lines. | Kartverket/Geonorge marine basemap and bathymetry. |

## Source-level assignment

| Demonstrator case | Source from inventory | Required source profile(s) | Why this is the correct level of reuse |
| --- | --- | --- | --- |
| All | Unified wind-park development dataset | `emodnet-compliant-windfarm` | Same feature type and mandatory EMODnet wind-farm fields as the German monopile source. |
| Norwegian North Sea | Naturbase protected areas / marine MPAs | `emodnet-protected-area` | A protected-site designation is not an energy or infrastructure feature. |
| Norwegian North Sea | Fiskeridirektoratet landings linked with vessel data | `emodnet-fishing-activity-event` | Retains event/landing-level measures and potentially sensitive vessel information. |
| Norwegian North Sea | ICES VMS and logbook spatial effort products | `emodnet-fishing-effort-grid` | It is an already aggregated spatial effort product, not raw events. |
| Norwegian North Sea | Kystverket / BarentsWatch historical AIS | `emodnet-vessel-density-grid` | The intended EMODnet contribution is a derived vessel-density product rather than raw AIS tracks. |
| Norwegian North Sea | Kartverket / Geonorge basemap, bathymetry, cable and pipeline routes | `emodnet-bathymetry-coverage-reference` **and** `emodnet-marine-infrastructure-route` | One provider source contains two incompatible data types: gridded bathymetry and linear infrastructure. |
| German Bight | Offshore windfarm monopile locations | `emodnet-compliant-windfarm` | A monopile location is an installation/component of the same wind-farm domain; use `type_inst` and notes/component identifiers instead of a new parallel wind-farm model. |
| German Bight | Monthly AIS vessel-density maps | `emodnet-vessel-density-grid` | Same cell, vessel-class, period and aggregation requirements as the Norwegian AIS product. |
| German Bight | Port traffic | `emodnet-port-traffic` | Port calls/statistics are point/time-series observations, not density cells. |
| German Bight | Fisheries intensity | `emodnet-fishing-effort-grid` | A spatially aggregated intensity map shares the ICES/GFW grid profile. |
| Central Baltic (Gotland) | Swedish licensed-fisher logbook data | `emodnet-fishing-activity-event` | Same event-level model as Norwegian logbook/landings; field mappings may differ but the profile remains the same. |
| Central Baltic (Gotland) | Community Fishing Fleet Register | `emodnet-fishing-vessel-register` | A reference register describes vessels, not fishing activity. |
| Central Baltic (Gotland) | Global Fishing Watch public fishing effort | `emodnet-fishing-effort-grid` | It is a derived spatiotemporal effort product and therefore shares the ICES/German intensity profile. |

## Implementation boundaries

- The existing wind-farm block should be reused unchanged for wind-farm features. If monopiles are supplied as individual asset records rather than farm extents, add an optional component identifier and parent-farm identifier in a small profile extension; do not fork the core schema.
- The Norwegian landings and Swedish logbooks may share a common event schema only after the access-control rule is made explicit. Vessel identifiers and fine spatial positions should be omitted, generalized or access-restricted where required by the source licence or confidentiality policy.
- Do not force raw AIS, VMS, logbook events or bathymetry grids into a single “GeoJSON or CSV” block. Their geometry, time semantics, aggregation and access constraints differ materially.

## Authoritative references

- [EMODnet web-service documentation](https://emodnet.ec.europa.eu/en/emodnet-web-service-documentation) — Human Activities WFS/WCS and catalogue service.
- [EMODnet Human Activities portfolio](https://emodnet.ec.europa.eu/sites/emodnet.ec.europa.eu/files/public/PDF/20210819_EMODnet_Portfolio.pdf) — themes including wind farms, cables, pipelines, fisheries, vessel traffic and ports.
- [EMODnet EU vessel-density method](https://emodnet.ec.europa.eu/en/human-activities-eu-vessel-density-map-detailed-method) — vessel-density cells and reporting periods.
- [EMODnet terms of use](https://emodnet.ec.europa.eu/en/terms-use-emodnet-online-services-data-and-data-products) — provenance, attribution and metadata obligations.
- [GeoJSON RFC 7946](https://datatracker.ietf.org/doc/html/rfc7946), [INSPIRE data specifications](https://inspire.ec.europa.eu/data-specifications/2892), [OGC API — Records](https://docs.ogc.org/is/20-004/20-004.html), and [CSV on the Web](https://www.w3.org/TR/tabular-data-primer/).
