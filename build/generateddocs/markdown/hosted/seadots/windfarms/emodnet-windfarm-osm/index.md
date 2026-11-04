
# EMODnet windfarm OSM extension (Schema)

`ogc.hosted.seadots.windfarms.emodnet-windfarm-osm` *v0.1*

A profile of the EMODnet-compliant windfarm feature that harmonizes explicit OpenStreetMap name, installed capacity, status, installation type, and year tags while preserving the source OSM element identity, complete tag dictionary, relation members, geometry, and null geometry.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# EMODnet windfarm OSM extension

This block profiles `ogc.hosted.seadots.windfarms.windfarm-designated-area-emodnet` and adds source-specific OSM identity, tags, and relation members. The base block remains unchanged. Each transformed feature retains its original GeoJSON geometry—including a null relation geometry—and its original `id`, `osm_type`, `osm_id`, complete `tags` object, and optional `members` array. Mapped properties are additive; they do not replace the source tags.

## Source-property coverage gaps

| OSM source property | EMODnet/profile property | Mapping |
|---|---|---|
| `tags.name`, otherwise `tags.seamark:name` | `name` | Copy first available value |
| `tags.plant:output:electricity`, otherwise `tags.generator:output:electricity` | `power_mw` | Parse a numeric value only when the explicit unit is MW; raw value remains in `tags` |
| `tags.status` | `status` | Copy source text without normalization |
| `tags.plant:type` | `type_inst` | Copy source text |
| `tags.start_date` | `year` | Copy source string; raw tag remains available to interpret the date meaning |
| `tags.turbines` | `n_turbines` | Parse only an integer count |
| Polygon or multipolygon relation plus `tags.industrial=windfarm`, `tags.seamark:landmark:production_area=wind_farm`, or `tags.plant:source=wind` and `tags.plant:type=offshore` | `category_of_offshore_production_area` | Add IHO enumerated code `1` (“Wind Farm”) only when area geometry/type and source tags support it |
| Point node with `tags.generator:method=wind_turbine` | `iho_feature_role` | Link to the local Wind Turbine concept, aligned to IHO S-32 and the S-101 Wind Turbine (LNDMRK) label |
| Polygon or multipolygon relation with explicit wind-farm area tags (above) | `iho_feature_role` | Link to the local Offshore Production Area concept, aligned to the S-101 Offshore Production Area (OSPARE) label |

No value is inferred for `country`, `dist_coast`, `notes`, `updateyear`, or area. The snapshot's geographic filter does not constitute per-feature country evidence. The transform does not normalize OSM statuses or assume an absent tag. For an electricity-output tag expressed in a unit other than MW or with an unparseable value, `power_mw` is omitted.

### Explicitly unmapped EMODnet properties

The source has no per-feature country code/name, coastal distance, source notes field, update year, or area measurement, so `country`, `dist_coast`, `notes`, `updateyear`, and `area_sqkm` remain absent. A bounding filter is not evidence that every feature lies within a national boundary. No OSM property maps to these fields without additional authoritative data.

The IHO Geospatial Information Registry defines Data Dictionary item 42, “Category of Offshore Production Area,” as classification of an area at sea within which production facilities exist; code `1` is “Wind Farm.” The local predicate `categoryOfOffshoreProductionArea` is linked to item 42 in `ontology.ttl`, and the data stores the registry's numeric code. The property is only attached to area features when OSM tags explicitly support it. `iho_feature_role` points to local concepts with SKOS close-match links to the cited IHO material; the transform does not invent an IHO registry IRI for a feature class. This follows the distinction in IHO S-101 between offshore production areas and individual wind turbines. See the [IHO registry item](https://registry.iho.int/fdd/view3.do?idx=42&type=3), [IHO S-101 Annex A](https://metanorma.github.io/iho-s-101/documents/2.0.0/annex-a/document.html), and the [IHO S-32 wind turbine definition](https://portal.iho.int/iho-ohi/S32/engView.php?page=303).

The source is a dated OpenStreetMap extract, not an authoritative national inventory. Its attribution and ODbL license are retained with the source representation and example. See [OpenStreetMap copyright](https://www.openstreetmap.org/copyright).

## Examples

### Polish Baltic OSM features harmonized to the EMODnet model
The source tags remain present alongside mapped properties. This sample includes turbine nodes, farm-area ways, and a relation whose geometry is null. Source: [OpenStreetMap contributors](https://www.openstreetmap.org/copyright); retrieved from the [OSM API](https://api.openstreetmap.org/api/0.6/map) on 2026-10-27 under the [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/).
#### json
```json
{
  "type": "FeatureCollection",
  "source": "OpenStreetMap contributors (ODbL 1.0), api.openstreetmap.org/api/0.6/map, fetched 2026-10-27; offshore Polish Baltic, lat > 54.85",
  "features": [
    {
      "type": "Feature",
      "id": "node/14191571016",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.884117,
          55.09105
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571016,
        "tags": {
          "name": "MFW Bałtyk II Offshore Substation",
          "operator": "Equinor;Polenergia",
          "power": "substation",
          "ref": "BK2 OSS",
          "status": "construction",
          "substation": "transmission",
          "voltage": "220000;66000"
        },
        "name": "MFW Bałtyk II Offshore Substation",
        "status": "construction"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571018",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.803137,
          55.086865
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571018,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 H04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571019",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.80055,
          55.097815
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571019,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 H03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571021",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.825374,
          55.076584
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571021,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 G05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571022",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.822962,
          55.087942
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571022,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 G04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571023",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.820724,
          55.099058
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571023,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 G03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571026",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.84783,
          55.066841
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571026,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 F06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571027",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.845752,
          55.077734
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571027,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 F05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571028",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.843453,
          55.088887
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571028,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 F04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571032",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.867979,
          55.067973
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571032,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 E06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571033",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.865872,
          55.078913
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571033,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 E05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571034",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.86363,
          55.090107
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571034,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 E04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571037",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.891036,
          55.057788
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571037,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 D07",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571038",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.888075,
          55.068803
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571038,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 D06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571039",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.886259,
          55.079969
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571039,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 D05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571017",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.7776,
          55.108004
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571017,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 J02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571020",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.798163,
          55.108933
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571020,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 H02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571024",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.818688,
          55.109898
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571024,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 G02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571025",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.816035,
          55.121208
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571025,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 G01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571029",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.841109,
          55.10004
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571029,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 F03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571030",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.83836,
          55.111032
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571030,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 F02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571031",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.836498,
          55.122311
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571031,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 F01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571035",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.858692,
          55.112335
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571035,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 E02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571036",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.855997,
          55.12346
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571036,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 E01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571040",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.881528,
          55.102278
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571040,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 D03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571041",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.878947,
          55.113625
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571041,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 D02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571042",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.876683,
          55.124524
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571042,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 D01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571047",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.898713,
          55.113625
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571047,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 C02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571048",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.897143,
          55.125586
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571048,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 C01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537539",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.353556,
          54.997069
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537539,
        "tags": {
          "name": "MFW Bałtyk III Offshore Substation",
          "operator": "Equinor;Polenergia",
          "power": "substation",
          "ref": "BK3 OSS",
          "status": "construction",
          "substation": "transmission",
          "voltage": "220000;66000"
        },
        "name": "MFW Bałtyk III Offshore Substation",
        "status": "construction"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537540",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.270053,
          54.998782
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537540,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 M04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537541",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.275409,
          55.010672
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537541,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 M03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537542",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.281049,
          55.022455
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537542,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 M02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537543",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.283813,
          54.983888
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537543,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 L05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537544",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.289463,
          54.99559
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537544,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 L04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537545",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.29541,
          55.007347
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537545,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 L03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537546",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.30046,
          55.019018
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537546,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 L02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537547",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.306081,
          55.030645
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537547,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 L01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537548",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.292501,
          54.957068
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537548,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 K07",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537549",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.298174,
          54.968722
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537549,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 K06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537550",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.303485,
          54.980528
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537550,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 K05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537551",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.308958,
          54.992256
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537551,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 K04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537552",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.314493,
          55.003671
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537552,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 K03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537553",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.319906,
          55.015593
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537553,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 K02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537554",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.325594,
          55.027275
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537554,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 K01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537555",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.311847,
          54.953732
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537555,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 J07",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537556",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.31743,
          54.965356
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537556,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 J06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537557",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.322872,
          54.977064
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537557,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 J05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537558",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.328485,
          54.988852
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537558,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 J04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537559",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.333772,
          55.000446
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537559,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 J03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537560",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.339309,
          55.012201
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537560,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 J02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537561",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.344812,
          55.023919
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537561,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 J01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537562",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.336774,
          54.962085
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537562,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 H06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537563",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.342261,
          54.973665
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537563,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 H05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537564",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.347981,
          54.985377
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537564,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 H04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537565",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.364254,
          55.020548
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537565,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 H01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537566",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.356131,
          54.958498
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537566,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 G06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537567",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.361697,
          54.970311
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537567,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 G05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537568",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.372896,
          54.993769
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537568,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 G03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537569",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.378069,
          55.005452
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537569,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 G02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537570",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.383622,
          55.017118
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537570,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 G01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537571",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.381244,
          54.966888
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537571,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 F05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537572",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.386526,
          54.978579
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537572,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 F04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537573",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.392011,
          54.990222
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537573,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 F03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571043",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.913676,
          55.047667
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571043,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 C08",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571044",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.911206,
          55.058512
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571044,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 C07",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571045",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.908728,
          55.070153
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571045,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 C06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571046",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.90412,
          55.092218
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571046,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 C04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571049",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.936386,
          55.037346
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571049,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B09",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571050",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.933612,
          55.048736
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571050,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B08",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571051",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.931603,
          55.059844
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571051,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B07",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571052",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.929119,
          55.07094
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571052,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571053",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.927012,
          55.082075
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571053,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571054",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.924474,
          55.093338
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571054,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571058",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.956572,
          55.038679
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571058,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A09",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571059",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.954215,
          55.049798
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571059,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A08",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571060",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.951729,
          55.060982
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571060,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A07",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571061",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.949152,
          55.07234
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571061,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571062",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.947122,
          55.08304
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571062,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571063",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.944589,
          55.094174
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571063,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911456",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.056763,
          55.05042
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911456,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "G16",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911457",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.162282,
          55.074338
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911457,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "F24",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911458",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.055145,
          55.059105
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911458,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "F16",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911459",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.99413,
          55.048522
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911459,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "F12",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911460",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.081364,
          55.084846
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911460,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "F04",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911461",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.207586,
          55.084077
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911461,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "F03",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911462",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.145807,
          55.077702
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911462,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E24",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911463",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.179149,
          55.048452
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911463,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E23",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911464",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.268651,
          55.097706
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911464,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E21",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911465",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.205919,
          55.092437
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911465,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E19",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911466",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.975856,
          55.060168
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911466,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E17",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911467",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.023082,
          55.060883
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911467,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E16",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911468",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.008841,
          55.053637
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911468,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E12",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911469",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.979361,
          55.04307
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911469,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E11",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911470",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.086985,
          55.02731
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911470,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E08",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911472",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.064853,
          55.088226
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911472,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E05",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911473",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.130153,
          55.077241
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911473,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E04",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911474",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.190976,
          55.08831
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911474,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E03",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911476",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.14781,
          55.067721
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911476,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D24",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911477",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.149906,
          55.057281
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911477,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D23",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911478",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.26886,
          55.089294
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911478,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D21",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911480",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.230169,
          55.098839
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911480,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D19",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911481",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.973176,
          55.074731
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911481,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D18",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911482",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.97761,
          55.051614
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911482,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D17",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911483",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.036973,
          55.070254
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911483,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D16",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911484",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.104782,
          55.070156
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911484,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D15",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911487",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.981071,
          55.034558
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911487,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D11",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911488",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.025106,
          55.023296
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911488,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D10",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911489",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.071411,
          55.011944
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911489,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D09",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911490",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.093759,
          55.044184
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911490,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D08",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911491",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.069453,
          55.065543
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911491,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D07",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911493",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.062657,
          55.099052
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911493,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D05",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911494",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.097696,
          55.081766
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911494,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D04",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911495",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.214603,
          55.099971
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911495,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D02",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911497",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.16454,
          55.062874
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911497,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C24",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911498",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.164608,
          55.053155
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911498,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C23",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911499",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.194778,
          55.045129
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911499,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C22",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911500",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.258598,
          55.082456
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911500,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C21",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968202",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.222,
          55.090479
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968202,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C19",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968203",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.969432,
          55.092967
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968203,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C18",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968204",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.992375,
          55.057103
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968204,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C17",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968205",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.040301,
          55.053899
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968205,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C16",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968206",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.09799,
          55.061375
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968206,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C15",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968208",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.99589,
          55.039917
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968208,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C12",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968209",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.995765,
          55.030763
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968209,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C11",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968210",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.055382,
          55.015581
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968210,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C10",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968211",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.083366,
          55.018663
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968211,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C09",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968212",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.090342,
          55.035582
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968212,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C08",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968213",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.07118,
          55.05702
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968213,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C07",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968216",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.133411,
          55.061459
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968216,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C04",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968217",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.193193,
          55.077005
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968217,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C03",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968220",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.178971,
          55.069725
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968220,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B24",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968221",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.18146,
          55.057054
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968221,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B23",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968222",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.208481,
          55.049657
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968222,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B22",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968223",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.248456,
          55.075696
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968223,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B21",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968224",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.253148,
          55.092131
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968224,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B20",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968225",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.224122,
          55.080196
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968225,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B19",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968226",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.97121,
          55.084309
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968226,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B18",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968227",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.006922,
          55.063323
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968227,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B17",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968228",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.053257,
          55.067689
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968228,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B16",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968229",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.083621,
          55.073235
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968229,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B15",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968230",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.983897,
          55.098499
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968230,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B13",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968231",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.012418,
          55.036384
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968231,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B12",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968232",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.010713,
          55.02696
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968232,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B11",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968233",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.040156,
          55.019463
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968233,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B10",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968234",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.062187,
          55.022912
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968234,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B09",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968235",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.075053,
          55.03843
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968235,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B08",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968236",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.094808,
          55.053163
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968236,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B07",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968238",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.094169,
          55.099211
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968238,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B05",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968239",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.124449,
          55.068642
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968239,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B04",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968240",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.176601,
          55.081355
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968240,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B03",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968242",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.195457,
          55.065972
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968242,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A24",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968243",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.197291,
          55.056037
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968243,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A23",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968244",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.219233,
          55.056198
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968244,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A22",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968245",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.238066,
          55.068821
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968245,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A21",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968246",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.238679,
          55.086173
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968246,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A20",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968247",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.209739,
          55.073448
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968247,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A19",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968248",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.98806,
          55.077498
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968248,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A18",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968249",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.034935,
          55.080421
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968249,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A17",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968250",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.051198,
          55.077823
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968250,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A16",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968252",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.001586,
          55.088828
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968252,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A13",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968253",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.027126,
          55.041354
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968253,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A12",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968254",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.028885,
          55.032584
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968254,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A11",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968255",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.045469,
          55.02911
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968255,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A10",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968256",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.06063,
          55.031352
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968256,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A09",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968257",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.059088,
          55.03974
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968257,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A08",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968258",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.110114,
          55.098179
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968258,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A06",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968259",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.095895,
          55.090675
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968259,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A05",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968260",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.159819,
          55.085684
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968260,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A03",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968262",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.126551,
          55.095199
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968262,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A01",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571055",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.922397,
          55.104129
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571055,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571056",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.919539,
          55.115594
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571056,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571057",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.917253,
          55.126734
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571057,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571064",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.942171,
          55.105568
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571064,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571065",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.940286,
          55.116807
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571065,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571066",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.937141,
          55.127815
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571066,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911471",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.043432,
          55.111741
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911471,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E06",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911475",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.105549,
          55.107152
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911475,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E01",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911479",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.245112,
          55.101796
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911479,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D20",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911485",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.996363,
          55.112844
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911485,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D14",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911486",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.964826,
          55.112794
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911486,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D13",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911492",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.058962,
          55.110838
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911492,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D06",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911496",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.121066,
          55.106389
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911496,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D01",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968201",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.260012,
          55.104459
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968201,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C20",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968207",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.967247,
          55.1036
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968207,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C13",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968214",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.074569,
          55.109736
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968214,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C06",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968215",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.07807,
          55.100793
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968215,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C05",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968218",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.19918,
          55.101056
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968218,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C02",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968219",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.152316,
          55.104254
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968219,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C01",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968237",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.090128,
          55.108254
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968237,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B06",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968241",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.183421,
          55.102147
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968241,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B02",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968251",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.046488,
          55.101279
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968251,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A14",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968261",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.16785,
          55.103191
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968261,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A02",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128570",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.66812,
          55.10027
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128570,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "71",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128582",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.67817,
          55.109397
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128582,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "59",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128592",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.701642,
          55.10965
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128592,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "49",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129402",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.638176,
          55.102896
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129402,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "39",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129403",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.654604,
          55.109176
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129403,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "38",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129404",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.722445,
          55.10092
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129404,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "37",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129405",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.724589,
          55.109811
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129405,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "36",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129406",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.747051,
          55.108198
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129406,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "35",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129408",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.769843,
          55.108576
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129408,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "33",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129426",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.621821,
          55.108774
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129426,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "15",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128563",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.624929,
          55.031379
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128563,
        "tags": {
          "location": "sea",
          "name": "Baltic Power OSS West",
          "power": "substation",
          "seamark:platform:category": "production",
          "seamark:type": "platform",
          "substation": "generation",
          "voltage": "230000;66000"
        },
        "name": "Baltic Power OSS West"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128566",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.63486,
          55.020635
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128566,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "75",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128568",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.64328,
          55.060358
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128568,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "73",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128569",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.64,
          55.049375
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128569,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "72",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128571",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.610119,
          55.043869
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128571,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "70",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128575",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.640016,
          55.039663
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128575,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "66",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128576",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.635311,
          55.029823
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128576,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "65",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128577",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.628869,
          55.00997
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128577,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "64",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128578",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.626832,
          55.000814
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128578,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "63",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128593",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.594355,
          55.003223
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128593,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "48",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128594",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.602226,
          55.014896
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128594,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "47",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128595",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.604322,
          55.024106
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128595,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "46",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128596",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.606384,
          55.034685
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128596,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "45",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128597",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.616112,
          55.052976
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128597,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "44",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128598",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.61844,
          55.063799
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128598,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "43",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128599",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.624618,
          55.074478
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128599,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "42",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128600",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.632259,
          55.083729
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128600,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "41",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129401",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.636667,
          55.092805
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129401,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "40",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129427",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.616341,
          55.099549
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129427,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "14",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129428",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.612253,
          55.088796
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129428,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "13",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129429",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.603759,
          55.079589
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129429,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "12",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129430",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.595467,
          55.070586
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129430,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "11",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129431",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.587049,
          55.061441
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129431,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "10",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129432",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.583794,
          55.05254
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129432,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "9",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129433",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.581526,
          55.043584
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129433,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "8",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129434",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.579247,
          55.034576
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129434,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "7",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129435",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.576959,
          55.025528
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129435,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "6",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129436",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.57467,
          55.016476
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129436,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "5",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129437",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.572366,
          55.007357
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129437,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "4",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537574",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.403106,
          55.013742
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537574,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 F01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537579",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.42238,
          55.010324
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537579,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 E01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537583",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.441772,
          55.006915
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537583,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 D01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537586",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.461272,
          55.003525
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537586,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 C01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128564",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.68719,
          55.051187
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128564,
        "tags": {
          "location": "sea",
          "name": "Baltic Power OSS East",
          "power": "substation",
          "seamark:platform:category": "production",
          "seamark:type": "platform",
          "substation": "generation",
          "voltage": "230000;66000"
        },
        "name": "Baltic Power OSS East"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128565",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.653582,
          55.006667
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128565,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "76",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128567",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.661072,
          55.080457
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128567,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "74",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128572",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.683461,
          55.066143
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128572,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "69",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128573",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.747624,
          55.099235
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128573,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "68",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128574",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.654354,
          55.071385
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128574,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "67",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128580",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.716839,
          55.090599
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128580,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "61",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128581",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.663009,
          55.091074
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128581,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "60",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128583",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.672281,
          55.0146
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128583,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "58",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128584",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.672183,
          55.023284
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128584,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "57",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128585",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.675452,
          55.031888
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128585,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "56",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128586",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.675065,
          55.040864
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128586,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "55",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128587",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.673089,
          55.049809
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128587,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "54",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128588",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.668436,
          55.058796
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128588,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "53",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128589",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.685713,
          55.076469
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128589,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "52",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128590",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.689498,
          55.087969
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128590,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "51",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128591",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.694919,
          55.098781
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128591,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "50",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129407",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.743457,
          55.090149
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129407,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "34",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129409",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.771604,
          55.098788
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129409,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "32",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129410",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.76571,
          55.088551
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129410,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "31",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129411",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708551,
          55.080982
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129411,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "30",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129412",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708551,
          55.071803
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129412,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "29",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129413",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.70855,
          55.06282
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129413,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "28",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129414",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708564,
          55.053803
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129414,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "27",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129415",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.70858,
          55.044819
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129415,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "26",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129416",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708615,
          55.035834
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129416,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "25",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129417",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708638,
          55.023444
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129417,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "24",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129418",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708593,
          55.014232
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129418,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "23",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129419",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708956,
          55.005267
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129419,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "22",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129420",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.688873,
          55.008866
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129420,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "21",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129421",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.673768,
          55.001274
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129421,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "20",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129422",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.650697,
          54.995819
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129422,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "19",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128579",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.589261,
          54.993376
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128579,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "62",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129423",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.628481,
          54.991824
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129423,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "18",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129424",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.607432,
          54.987943
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129424,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "17",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129425",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.58752,
          54.982886
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129425,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "16",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129438",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.570083,
          54.998319
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129438,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "3",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129439",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.567802,
          54.989286
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129439,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "2",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129440",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.565519,
          54.980271
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129440,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "1",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537575",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.400523,
          54.96347
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537575,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 E05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537576",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.405782,
          54.975308
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537576,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 E04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537577",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.411684,
          54.98702
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537577,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 E03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537578",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.416964,
          54.998604
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537578,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 E02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537580",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.425285,
          54.971758
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537580,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 D04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537581",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.430813,
          54.983522
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537581,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 D03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537582",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.436202,
          54.995205
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537582,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 D02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537584",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.450155,
          54.980018
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537584,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 C03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537585",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.455675,
          54.99177
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537585,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 C02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537587",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.47507,
          54.988381
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537587,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 B02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537588",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.480568,
          54.999961
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537588,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 B01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537589",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.499785,
          54.996564
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537589,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 A01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "way/1560132096",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              16.97519,
              55.01403
            ],
            [
              16.85987,
              55.03507
            ],
            [
              16.84804,
              55.03533
            ],
            [
              16.77326,
              55.10242
            ],
            [
              16.77199,
              55.10329
            ],
            [
              16.74361,
              55.11839
            ],
            [
              16.78563,
              55.12361
            ],
            [
              16.8413,
              55.13174
            ],
            [
              16.8929,
              55.13481
            ],
            [
              16.92212,
              55.13824
            ],
            [
              16.94999,
              55.13669
            ],
            [
              16.97519,
              55.01403
            ]
          ]
        ]
      },
      "properties": {
        "osm_type": "way",
        "osm_id": 1560132096,
        "tags": {
          "boundary": "industrial",
          "construction:power": "plant",
          "name": "MFW Bałtyk II Offshore Wind Farm",
          "operator": "Equinor;Polenergia",
          "plant:output:electricity": "720 MW",
          "plant:source": "wind",
          "plant:type": "offshore",
          "start_date": "2027",
          "status": "construction",
          "turbines": "50"
        },
        "name": "MFW Bałtyk II Offshore Wind Farm",
        "power_mw": 720.0,
        "status": "construction",
        "type_inst": "offshore",
        "year": "2027",
        "n_turbines": 50,
        "category_of_offshore_production_area": 1,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#OffshoreProductionArea"
      }
    },
    {
      "type": "Feature",
      "id": "way/1560193204",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              17.30485,
              55.04237
            ],
            [
              17.32097,
              55.0531
            ],
            [
              17.3392,
              55.05365
            ],
            [
              17.3393,
              55.05369
            ],
            [
              17.38446,
              55.055
            ],
            [
              17.38475,
              55.05501
            ],
            [
              17.38526,
              55.05505
            ],
            [
              17.38576,
              55.0551
            ],
            [
              17.38626,
              55.05517
            ],
            [
              17.38674,
              55.05527
            ],
            [
              17.38722,
              55.05538
            ],
            [
              17.38768,
              55.0555
            ],
            [
              17.38812,
              55.05565
            ],
            [
              17.38855,
              55.05581
            ],
            [
              17.38896,
              55.05599
            ],
            [
              17.38935,
              55.05618
            ],
            [
              17.38972,
              55.05638
            ],
            [
              17.39006,
              55.0566
            ],
            [
              17.39037,
              55.05683
            ],
            [
              17.39066,
              55.05708
            ],
            [
              17.39092,
              55.05733
            ],
            [
              17.39115,
              55.05759
            ],
            [
              17.39136,
              55.05786
            ],
            [
              17.39122,
              55.05814
            ],
            [
              17.39166,
              55.05842
            ],
            [
              17.39177,
              55.05871
            ],
            [
              17.39184,
              55.059
            ],
            [
              17.39188,
              55.0593
            ],
            [
              17.39187,
              55.05972
            ],
            [
              17.38848,
              55.09758
            ],
            [
              17.45562,
              55.09956
            ],
            [
              17.45563,
              55.09956
            ],
            [
              17.55269,
              55.10238
            ],
            [
              17.54074,
              55.06522
            ],
            [
              17.54073,
              55.06521
            ],
            [
              17.53442,
              55.0452
            ],
            [
              17.52893,
              55.03915
            ],
            [
              17.52878,
              55.03898
            ],
            [
              17.52858,
              55.03871
            ],
            [
              17.52841,
              55.03843
            ],
            [
              17.52827,
              55.03815
            ],
            [
              17.52816,
              55.03786
            ],
            [
              17.52809,
              55.03757
            ],
            [
              17.52805,
              55.03727
            ],
            [
              17.52804,
              55.03698
            ],
            [
              17.52807,
              55.03669
            ],
            [
              17.5281,
              55.03655
            ],
            [
              17.53513,
              55.00209
            ],
            [
              17.3133,
              55.0409
            ],
            [
              17.30485,
              55.04237
            ]
          ]
        ]
      },
      "properties": {
        "osm_type": "way",
        "osm_id": 1560193204,
        "tags": {
          "boundary": "maritime",
          "industrial": "windfarm",
          "name": "Baltica 3 OWF",
          "operator": "PGE / Ørsted",
          "plant:source": "wind",
          "seamark:name": "Baltica 3",
          "seamark:production_area:product": "power",
          "seamark:type": "production_area"
        },
        "name": "Baltica 3 OWF",
        "category_of_offshore_production_area": 1,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#OffshoreProductionArea"
      }
    },
    {
      "type": "Feature",
      "id": "way/1560193205",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              17.04888,
              55.0159
            ],
            [
              16.97915,
              55.03365
            ],
            [
              16.96261,
              55.11424
            ],
            [
              17.03059,
              55.11418
            ],
            [
              17.09057,
              55.10969
            ],
            [
              17.09066,
              55.10968
            ],
            [
              17.16009,
              55.10494
            ],
            [
              17.16009,
              55.10494
            ],
            [
              17.22777,
              55.10031
            ],
            [
              17.22788,
              55.10031
            ],
            [
              17.22839,
              55.10029
            ],
            [
              17.2289,
              55.10028
            ],
            [
              17.22941,
              55.1003
            ],
            [
              17.22992,
              55.10034
            ],
            [
              17.23043,
              55.10039
            ],
            [
              17.23092,
              55.10047
            ],
            [
              17.23109,
              55.1005
            ],
            [
              17.26984,
              55.1076
            ],
            [
              17.27155,
              55.08923
            ],
            [
              17.25706,
              55.07957
            ],
            [
              17.24396,
              55.07084
            ],
            [
              17.22737,
              55.05977
            ],
            [
              17.20123,
              55.04231
            ],
            [
              17.18645,
              55.04306
            ],
            [
              17.17902,
              55.04545
            ],
            [
              17.12825,
              55.06174
            ],
            [
              17.1201,
              55.06952
            ],
            [
              17.12007,
              55.06956
            ],
            [
              17.11978,
              55.0698
            ],
            [
              17.11947,
              55.07004
            ],
            [
              17.11914,
              55.07026
            ],
            [
              17.11878,
              55.07047
            ],
            [
              17.11839,
              55.07066
            ],
            [
              17.11799,
              55.07084
            ],
            [
              17.11757,
              55.07101
            ],
            [
              17.11712,
              55.07116
            ],
            [
              17.11667,
              55.07129
            ],
            [
              17.11619,
              55.0714
            ],
            [
              17.11571,
              55.0715
            ],
            [
              17.11521,
              55.07158
            ],
            [
              17.11471,
              55.07163
            ],
            [
              17.1142,
              55.07167
            ],
            [
              17.11382,
              55.0717
            ],
            [
              17.11267,
              55.07168
            ],
            [
              17.11216,
              55.07164
            ],
            [
              17.11166,
              55.07159
            ],
            [
              17.11062,
              55.04174
            ],
            [
              17.11064,
              55.04171
            ],
            [
              17.11001,
              55.04167
            ],
            [
              17.10974,
              55.04162
            ],
            [
              17.1093,
              55.04157
            ],
            [
              17.10887,
              55.04151
            ],
            [
              17.10846,
              55.04145
            ],
            [
              17.10807,
              55.04138
            ],
            [
              17.10771,
              55.04131
            ],
            [
              17.10737,
              55.04123
            ],
            [
              17.10702,
              55.04114
            ],
            [
              17.10676,
              55.04106
            ],
            [
              17.10651,
              55.04096
            ],
            [
              17.1061,
              55.04087
            ],
            [
              17.10608,
              55.04077
            ],
            [
              17.10591,
              55.04067
            ],
            [
              17.10578,
              55.04057
            ],
            [
              17.10577,
              55.04056
            ],
            [
              17.08831,
              55.02524
            ],
            [
              17.08222,
              55.00972
            ],
            [
              17.08218,
              55.00873
            ],
            [
              17.04888,
              55.0159
            ]
          ]
        ]
      },
      "properties": {
        "osm_type": "way",
        "osm_id": 1560193205,
        "tags": {
          "boundary": "maritime",
          "construction:power": "plant",
          "industrial": "windfarm",
          "name": "Baltica 2 OWF",
          "operator": "PGE / Ørsted",
          "plant:source": "wind",
          "seamark:name": "Baltica 2",
          "seamark:production_area:product": "power",
          "seamark:type": "production_area"
        },
        "name": "Baltica 2 OWF",
        "category_of_offshore_production_area": 1,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#OffshoreProductionArea"
      }
    },
    {
      "type": "Feature",
      "id": "way/1532855580",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              17.56412,
              54.9776
            ],
            [
              17.65142,
              54.99505
            ],
            [
              17.71816,
              55.00498
            ],
            [
              17.71614,
              55.08525
            ],
            [
              17.76867,
              55.08348
            ],
            [
              17.78045,
              55.11133
            ],
            [
              17.6207,
              55.11137
            ],
            [
              17.58828,
              55.07482
            ],
            [
              17.56412,
              54.9776
            ]
          ]
        ]
      },
      "properties": {
        "osm_type": "way",
        "osm_id": 1532855580,
        "tags": {
          "boundary": "maritime",
          "industrial": "windfarm",
          "seamark:name": "Baltic Power",
          "seamark:production_area:product": "power",
          "seamark:type": "production_area"
        },
        "name": "Baltic Power",
        "category_of_offshore_production_area": 1,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#OffshoreProductionArea"
      }
    },
    {
      "type": "Feature",
      "id": "relation/21402440",
      "geometry": null,
      "properties": {
        "osm_type": "relation",
        "osm_id": 21402440,
        "tags": {
          "name": "Baltic Power",
          "offshore": "yes",
          "operator": "Baltic Power",
          "plant:method": "wind_turbine",
          "plant:output:electricity": "1200 MW",
          "plant:source": "wind",
          "power": "plant",
          "seamark:landmark:production_area": "wind_farm",
          "seamark:type": "production_area",
          "type": "multipolygon"
        },
        "members": [
          "node/14185128592:generator",
          "node/14185129403:generator",
          "node/14185129406:generator",
          "node/14185129405:generator",
          "node/14185128582:generator",
          "node/14185129426:generator",
          "node/14185129408:generator",
          "node/14185129410:generator",
          "node/14185129409:generator",
          "node/14185128600:generator",
          "node/14185129401:generator",
          "node/14185129428:generator",
          "node/14185129427:generator",
          "node/14185128599:generator",
          "node/14185128567:generator",
          "node/14185129430:generator",
          "node/14185129429:generator",
          "node/14185128574:generator",
          "node/14185128581:generator",
          "node/14185128598:generator",
          "node/14185129402:generator",
          "node/14185129412:generator",
          "node/14185128591:generator",
          "node/14185128573:generator",
          "node/14185129411:generator",
          "node/14185129404:generator",
          "node/14185128570:generator",
          "node/14185128580:generator",
          "node/14185128590:generator",
          "node/14185128572:generator",
          "node/14185128589:generator",
          "node/14185129407:generator",
          "node/14185128586:generator",
          "node/14185129414:generator",
          "node/14185128585:generator",
          "node/14185129416:generator",
          "node/14185129413:generator",
          "node/14185128588:generator",
          "node/14185128587:generator",
          "node/14185129415:generator",
          "node/14185129417:generator",
          "node/14185128564:substation",
          "node/14185128584:generator",
          "node/14185128576:generator",
          "node/14185128566:generator",
          "node/14185128568:generator",
          "node/14185128597:generator",
          "node/14185128575:generator",
          "node/14185128569:generator",
          "node/14185129432:generator",
          "node/14185128571:generator",
          "node/14185128596:generator",
          "node/14185129434:generator",
          "node/14185128595:generator",
          "node/14185129431:generator",
          "node/14185128563:substation",
          "node/14185129433:generator",
          "node/14185129425:generator",
          "node/14185129422:generator",
          "node/14185128583:generator",
          "node/14185128565:generator",
          "node/14185128578:generator",
          "node/14185129421:generator",
          "node/14185128577:generator",
          "node/14185128594:generator",
          "node/14185129423:generator",
          "node/14185128593:generator",
          "node/14185129418:generator",
          "node/14185128579:generator",
          "node/14185129424:generator",
          "node/14185129420:generator",
          "node/14185129419:generator",
          "node/14185129435:generator",
          "node/14185129436:generator",
          "node/14185129438:generator",
          "node/14185129437:generator",
          "node/14185129439:generator",
          "node/14185129440:generator",
          "way/1532855580:outer"
        ],
        "name": "Baltic Power",
        "power_mw": 1200.0,
        "category_of_offshore_production_area": 1,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#OffshoreProductionArea"
      }
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/emodnet-windfarm-osm/context.jsonld",
  "type": "FeatureCollection",
  "source": "OpenStreetMap contributors (ODbL 1.0), api.openstreetmap.org/api/0.6/map, fetched 2026-10-27; offshore Polish Baltic, lat > 54.85",
  "features": [
    {
      "type": "Feature",
      "id": "node/14191571016",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.884117,
          55.09105
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571016,
        "tags": {
          "name": "MFW Ba\u0142tyk II Offshore Substation",
          "operator": "Equinor;Polenergia",
          "power": "substation",
          "ref": "BK2 OSS",
          "status": "construction",
          "substation": "transmission",
          "voltage": "220000;66000"
        },
        "name": "MFW Ba\u0142tyk II Offshore Substation",
        "status": "construction"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571018",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.803137,
          55.086865
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571018,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 H04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571019",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.80055,
          55.097815
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571019,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 H03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571021",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.825374,
          55.076584
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571021,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 G05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571022",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.822962,
          55.087942
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571022,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 G04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571023",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.820724,
          55.099058
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571023,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 G03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571026",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.84783,
          55.066841
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571026,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 F06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571027",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.845752,
          55.077734
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571027,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 F05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571028",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.843453,
          55.088887
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571028,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 F04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571032",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.867979,
          55.067973
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571032,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 E06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571033",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.865872,
          55.078913
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571033,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 E05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571034",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.86363,
          55.090107
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571034,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 E04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571037",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.891036,
          55.057788
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571037,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 D07",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571038",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.888075,
          55.068803
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571038,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 D06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571039",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.886259,
          55.079969
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571039,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 D05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571017",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.7776,
          55.108004
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571017,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 J02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571020",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.798163,
          55.108933
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571020,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 H02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571024",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.818688,
          55.109898
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571024,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 G02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571025",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.816035,
          55.121208
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571025,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 G01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571029",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.841109,
          55.10004
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571029,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 F03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571030",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.83836,
          55.111032
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571030,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 F02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571031",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.836498,
          55.122311
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571031,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 F01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571035",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.858692,
          55.112335
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571035,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 E02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571036",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.855997,
          55.12346
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571036,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 E01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571040",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.881528,
          55.102278
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571040,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 D03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571041",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.878947,
          55.113625
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571041,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 D02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571042",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.876683,
          55.124524
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571042,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 D01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571047",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.898713,
          55.113625
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571047,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 C02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571048",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.897143,
          55.125586
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571048,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 C01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537539",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.353556,
          54.997069
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537539,
        "tags": {
          "name": "MFW Ba\u0142tyk III Offshore Substation",
          "operator": "Equinor;Polenergia",
          "power": "substation",
          "ref": "BK3 OSS",
          "status": "construction",
          "substation": "transmission",
          "voltage": "220000;66000"
        },
        "name": "MFW Ba\u0142tyk III Offshore Substation",
        "status": "construction"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537540",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.270053,
          54.998782
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537540,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 M04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537541",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.275409,
          55.010672
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537541,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 M03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537542",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.281049,
          55.022455
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537542,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 M02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537543",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.283813,
          54.983888
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537543,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 L05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537544",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.289463,
          54.99559
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537544,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 L04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537545",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.29541,
          55.007347
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537545,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 L03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537546",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.30046,
          55.019018
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537546,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 L02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537547",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.306081,
          55.030645
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537547,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 L01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537548",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.292501,
          54.957068
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537548,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 K07",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537549",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.298174,
          54.968722
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537549,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 K06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537550",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.303485,
          54.980528
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537550,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 K05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537551",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.308958,
          54.992256
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537551,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 K04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537552",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.314493,
          55.003671
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537552,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 K03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537553",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.319906,
          55.015593
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537553,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 K02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537554",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.325594,
          55.027275
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537554,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 K01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537555",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.311847,
          54.953732
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537555,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 J07",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537556",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.31743,
          54.965356
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537556,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 J06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537557",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.322872,
          54.977064
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537557,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 J05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537558",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.328485,
          54.988852
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537558,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 J04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537559",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.333772,
          55.000446
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537559,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 J03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537560",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.339309,
          55.012201
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537560,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 J02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537561",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.344812,
          55.023919
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537561,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 J01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537562",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.336774,
          54.962085
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537562,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 H06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537563",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.342261,
          54.973665
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537563,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 H05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537564",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.347981,
          54.985377
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537564,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 H04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537565",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.364254,
          55.020548
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537565,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 H01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537566",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.356131,
          54.958498
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537566,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 G06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537567",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.361697,
          54.970311
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537567,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 G05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537568",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.372896,
          54.993769
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537568,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 G03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537569",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.378069,
          55.005452
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537569,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 G02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537570",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.383622,
          55.017118
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537570,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 G01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537571",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.381244,
          54.966888
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537571,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 F05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537572",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.386526,
          54.978579
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537572,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 F04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537573",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.392011,
          54.990222
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537573,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 F03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571043",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.913676,
          55.047667
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571043,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 C08",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571044",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.911206,
          55.058512
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571044,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 C07",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571045",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.908728,
          55.070153
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571045,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 C06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571046",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.90412,
          55.092218
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571046,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 C04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571049",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.936386,
          55.037346
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571049,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B09",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571050",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.933612,
          55.048736
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571050,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B08",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571051",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.931603,
          55.059844
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571051,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B07",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571052",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.929119,
          55.07094
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571052,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571053",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.927012,
          55.082075
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571053,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571054",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.924474,
          55.093338
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571054,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571058",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.956572,
          55.038679
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571058,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A09",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571059",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.954215,
          55.049798
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571059,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A08",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571060",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.951729,
          55.060982
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571060,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A07",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571061",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.949152,
          55.07234
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571061,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A06",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571062",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.947122,
          55.08304
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571062,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571063",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.944589,
          55.094174
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571063,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911456",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.056763,
          55.05042
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911456,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "G16",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911457",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.162282,
          55.074338
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911457,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "F24",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911458",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.055145,
          55.059105
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911458,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "F16",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911459",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.99413,
          55.048522
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911459,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "F12",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911460",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.081364,
          55.084846
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911460,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "F04",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911461",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.207586,
          55.084077
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911461,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "F03",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911462",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.145807,
          55.077702
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911462,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E24",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911463",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.179149,
          55.048452
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911463,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E23",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911464",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.268651,
          55.097706
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911464,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E21",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911465",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.205919,
          55.092437
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911465,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E19",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911466",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.975856,
          55.060168
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911466,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E17",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911467",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.023082,
          55.060883
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911467,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E16",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911468",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.008841,
          55.053637
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911468,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E12",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911469",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.979361,
          55.04307
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911469,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E11",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911470",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.086985,
          55.02731
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911470,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E08",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911472",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.064853,
          55.088226
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911472,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E05",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911473",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.130153,
          55.077241
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911473,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E04",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911474",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.190976,
          55.08831
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911474,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E03",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911476",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.14781,
          55.067721
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911476,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D24",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911477",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.149906,
          55.057281
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911477,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D23",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911478",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.26886,
          55.089294
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911478,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D21",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911480",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.230169,
          55.098839
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911480,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D19",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911481",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.973176,
          55.074731
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911481,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D18",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911482",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.97761,
          55.051614
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911482,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D17",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911483",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.036973,
          55.070254
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911483,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D16",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911484",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.104782,
          55.070156
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911484,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D15",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911487",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.981071,
          55.034558
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911487,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D11",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911488",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.025106,
          55.023296
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911488,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D10",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911489",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.071411,
          55.011944
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911489,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D09",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911490",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.093759,
          55.044184
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911490,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D08",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911491",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.069453,
          55.065543
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911491,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D07",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911493",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.062657,
          55.099052
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911493,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D05",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911494",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.097696,
          55.081766
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911494,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D04",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911495",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.214603,
          55.099971
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911495,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D02",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911497",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.16454,
          55.062874
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911497,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C24",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911498",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.164608,
          55.053155
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911498,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C23",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911499",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.194778,
          55.045129
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911499,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C22",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911500",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.258598,
          55.082456
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911500,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C21",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968202",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.222,
          55.090479
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968202,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C19",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968203",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.969432,
          55.092967
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968203,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C18",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968204",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.992375,
          55.057103
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968204,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C17",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968205",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.040301,
          55.053899
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968205,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C16",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968206",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.09799,
          55.061375
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968206,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C15",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968208",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.99589,
          55.039917
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968208,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C12",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968209",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.995765,
          55.030763
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968209,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C11",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968210",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.055382,
          55.015581
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968210,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C10",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968211",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.083366,
          55.018663
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968211,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C09",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968212",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.090342,
          55.035582
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968212,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C08",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968213",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.07118,
          55.05702
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968213,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C07",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968216",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.133411,
          55.061459
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968216,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C04",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968217",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.193193,
          55.077005
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968217,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C03",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968220",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.178971,
          55.069725
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968220,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B24",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968221",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.18146,
          55.057054
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968221,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B23",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968222",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.208481,
          55.049657
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968222,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B22",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968223",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.248456,
          55.075696
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968223,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B21",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968224",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.253148,
          55.092131
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968224,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B20",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968225",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.224122,
          55.080196
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968225,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B19",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968226",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.97121,
          55.084309
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968226,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B18",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968227",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.006922,
          55.063323
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968227,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B17",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968228",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.053257,
          55.067689
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968228,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B16",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968229",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.083621,
          55.073235
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968229,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B15",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968230",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.983897,
          55.098499
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968230,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B13",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968231",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.012418,
          55.036384
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968231,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B12",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968232",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.010713,
          55.02696
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968232,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B11",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968233",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.040156,
          55.019463
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968233,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B10",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968234",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.062187,
          55.022912
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968234,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B09",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968235",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.075053,
          55.03843
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968235,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B08",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968236",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.094808,
          55.053163
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968236,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B07",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968238",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.094169,
          55.099211
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968238,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B05",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968239",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.124449,
          55.068642
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968239,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B04",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968240",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.176601,
          55.081355
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968240,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B03",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968242",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.195457,
          55.065972
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968242,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A24",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968243",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.197291,
          55.056037
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968243,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A23",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968244",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.219233,
          55.056198
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968244,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A22",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968245",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.238066,
          55.068821
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968245,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A21",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968246",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.238679,
          55.086173
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968246,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A20",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968247",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.209739,
          55.073448
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968247,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A19",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968248",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.98806,
          55.077498
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968248,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A18",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968249",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.034935,
          55.080421
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968249,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A17",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968250",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.051198,
          55.077823
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968250,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A16",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968252",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.001586,
          55.088828
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968252,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A13",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968253",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.027126,
          55.041354
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968253,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A12",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968254",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.028885,
          55.032584
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968254,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A11",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968255",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.045469,
          55.02911
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968255,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A10",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968256",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.06063,
          55.031352
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968256,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A09",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968257",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.059088,
          55.03974
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968257,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A08",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968258",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.110114,
          55.098179
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968258,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A06",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968259",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.095895,
          55.090675
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968259,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A05",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968260",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.159819,
          55.085684
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968260,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A03",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968262",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.126551,
          55.095199
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968262,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A01",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571055",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.922397,
          55.104129
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571055,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571056",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.919539,
          55.115594
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571056,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571057",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.917253,
          55.126734
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571057,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 B01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571064",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.942171,
          55.105568
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571064,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571065",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.940286,
          55.116807
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571065,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191571066",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.937141,
          55.127815
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191571066,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK2 A01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911471",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.043432,
          55.111741
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911471,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E06",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911475",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.105549,
          55.107152
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911475,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "E01",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911479",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.245112,
          55.101796
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911479,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D20",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911485",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.996363,
          55.112844
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911485,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D14",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911486",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.964826,
          55.112794
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911486,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D13",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911492",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.058962,
          55.110838
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911492,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D06",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191911496",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.121066,
          55.106389
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191911496,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "D01",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968201",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.260012,
          55.104459
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968201,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C20",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968207",
      "geometry": {
        "type": "Point",
        "coordinates": [
          16.967247,
          55.1036
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968207,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C13",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968214",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.074569,
          55.109736
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968214,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C06",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968215",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.07807,
          55.100793
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968215,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C05",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968218",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.19918,
          55.101056
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968218,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C02",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968219",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.152316,
          55.104254
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968219,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "C01",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968237",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.090128,
          55.108254
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968237,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B06",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968241",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.183421,
          55.102147
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968241,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "B02",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968251",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.046488,
          55.101279
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968251,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A14",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191968261",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.16785,
          55.103191
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191968261,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "14 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-222 DD",
          "operator": "PGE; Orsted",
          "power": "generator",
          "ref": "A02",
          "rotor:diameter": "222"
        },
        "power_mw": 14.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128570",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.66812,
          55.10027
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128570,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "71",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128582",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.67817,
          55.109397
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128582,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "59",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128592",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.701642,
          55.10965
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128592,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "49",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129402",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.638176,
          55.102896
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129402,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "39",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129403",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.654604,
          55.109176
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129403,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "38",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129404",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.722445,
          55.10092
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129404,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "37",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129405",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.724589,
          55.109811
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129405,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "36",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129406",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.747051,
          55.108198
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129406,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "35",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129408",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.769843,
          55.108576
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129408,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "33",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129426",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.621821,
          55.108774
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129426,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "15",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128563",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.624929,
          55.031379
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128563,
        "tags": {
          "location": "sea",
          "name": "Baltic Power OSS West",
          "power": "substation",
          "seamark:platform:category": "production",
          "seamark:type": "platform",
          "substation": "generation",
          "voltage": "230000;66000"
        },
        "name": "Baltic Power OSS West"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128566",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.63486,
          55.020635
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128566,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "75",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128568",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.64328,
          55.060358
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128568,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "73",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128569",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.64,
          55.049375
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128569,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "72",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128571",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.610119,
          55.043869
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128571,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "70",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128575",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.640016,
          55.039663
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128575,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "66",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128576",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.635311,
          55.029823
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128576,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "65",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128577",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.628869,
          55.00997
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128577,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "64",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128578",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.626832,
          55.000814
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128578,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "63",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128593",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.594355,
          55.003223
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128593,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "48",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128594",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.602226,
          55.014896
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128594,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "47",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128595",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.604322,
          55.024106
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128595,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "46",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128596",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.606384,
          55.034685
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128596,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "45",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128597",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.616112,
          55.052976
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128597,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "44",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128598",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.61844,
          55.063799
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128598,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "43",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128599",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.624618,
          55.074478
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128599,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "42",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128600",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.632259,
          55.083729
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128600,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "41",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129401",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.636667,
          55.092805
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129401,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "40",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129427",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.616341,
          55.099549
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129427,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "14",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129428",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.612253,
          55.088796
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129428,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "13",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129429",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.603759,
          55.079589
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129429,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "12",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129430",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.595467,
          55.070586
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129430,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "11",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129431",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.587049,
          55.061441
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129431,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "10",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129432",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.583794,
          55.05254
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129432,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "9",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129433",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.581526,
          55.043584
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129433,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "8",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129434",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.579247,
          55.034576
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129434,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "7",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129435",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.576959,
          55.025528
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129435,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "6",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129436",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.57467,
          55.016476
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129436,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "5",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129437",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.572366,
          55.007357
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129437,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "4",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537574",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.403106,
          55.013742
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537574,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 F01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537579",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.42238,
          55.010324
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537579,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 E01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537583",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.441772,
          55.006915
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537583,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 D01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537586",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.461272,
          55.003525
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537586,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 C01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128564",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.68719,
          55.051187
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128564,
        "tags": {
          "location": "sea",
          "name": "Baltic Power OSS East",
          "power": "substation",
          "seamark:platform:category": "production",
          "seamark:type": "platform",
          "substation": "generation",
          "voltage": "230000;66000"
        },
        "name": "Baltic Power OSS East"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128565",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.653582,
          55.006667
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128565,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "76",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128567",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.661072,
          55.080457
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128567,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "74",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128572",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.683461,
          55.066143
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128572,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "69",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128573",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.747624,
          55.099235
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128573,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "68",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128574",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.654354,
          55.071385
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128574,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "67",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128580",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.716839,
          55.090599
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128580,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "61",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128581",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.663009,
          55.091074
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128581,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "60",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128583",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.672281,
          55.0146
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128583,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "58",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128584",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.672183,
          55.023284
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128584,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "57",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128585",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.675452,
          55.031888
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128585,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "56",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128586",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.675065,
          55.040864
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128586,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "55",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128587",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.673089,
          55.049809
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128587,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "54",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128588",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.668436,
          55.058796
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128588,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "53",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128589",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.685713,
          55.076469
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128589,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "52",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128590",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.689498,
          55.087969
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128590,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "51",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128591",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.694919,
          55.098781
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128591,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "50",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129407",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.743457,
          55.090149
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129407,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "34",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129409",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.771604,
          55.098788
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129409,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "32",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129410",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.76571,
          55.088551
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129410,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "31",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129411",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708551,
          55.080982
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129411,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "30",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129412",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708551,
          55.071803
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129412,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "29",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129413",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.70855,
          55.06282
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129413,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "28",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129414",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708564,
          55.053803
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129414,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "27",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129415",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.70858,
          55.044819
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129415,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "26",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129416",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708615,
          55.035834
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129416,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "25",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129417",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708638,
          55.023444
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129417,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "24",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129418",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708593,
          55.014232
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129418,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "23",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129419",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.708956,
          55.005267
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129419,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "22",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129420",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.688873,
          55.008866
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129420,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "21",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129421",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.673768,
          55.001274
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129421,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "20",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129422",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.650697,
          54.995819
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129422,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "19",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185128579",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.589261,
          54.993376
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185128579,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "62",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129423",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.628481,
          54.991824
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129423,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "18",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129424",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.607432,
          54.987943
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129424,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "17",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129425",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.58752,
          54.982886
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129425,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "16",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129438",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.570083,
          54.998319
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129438,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "3",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129439",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.567802,
          54.989286
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129439,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "2",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14185129440",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.565519,
          54.980271
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14185129440,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:output:electricity": "15 MW",
          "generator:source": "wind",
          "generator:type": "horizontal_axis",
          "height:hub": "141",
          "manufacturer": "Vestas",
          "model": "V236-15.0 MW",
          "offshore": "yes",
          "power": "generator",
          "ref": "1",
          "rotor:diameter": "236"
        },
        "power_mw": 15.0,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537575",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.400523,
          54.96347
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537575,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 E05",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537576",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.405782,
          54.975308
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537576,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 E04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537577",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.411684,
          54.98702
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537577,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 E03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537578",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.416964,
          54.998604
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537578,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 E02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537580",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.425285,
          54.971758
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537580,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 D04",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537581",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.430813,
          54.983522
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537581,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 D03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537582",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.436202,
          54.995205
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537582,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 D02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537584",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.450155,
          54.980018
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537584,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 C03",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537585",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.455675,
          54.99177
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537585,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 C02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537587",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.47507,
          54.988381
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537587,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 B02",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537588",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.480568,
          54.999961
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537588,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 B01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "node/14191537589",
      "geometry": {
        "type": "Point",
        "coordinates": [
          17.499785,
          54.996564
        ]
      },
      "properties": {
        "osm_type": "node",
        "osm_id": 14191537589,
        "tags": {
          "generator:method": "wind_turbine",
          "generator:source": "wind",
          "generator:type": "offshore",
          "manufacturer": "Siemens Gamesa",
          "model": "SG 14-236 DD",
          "operator": "Equinor;Polenergia",
          "power": "generator",
          "ref": "BK3 A01",
          "rotor:diameter": "236",
          "status": "construction"
        },
        "status": "construction",
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine"
      }
    },
    {
      "type": "Feature",
      "id": "way/1560132096",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              16.97519,
              55.01403
            ],
            [
              16.85987,
              55.03507
            ],
            [
              16.84804,
              55.03533
            ],
            [
              16.77326,
              55.10242
            ],
            [
              16.77199,
              55.10329
            ],
            [
              16.74361,
              55.11839
            ],
            [
              16.78563,
              55.12361
            ],
            [
              16.8413,
              55.13174
            ],
            [
              16.8929,
              55.13481
            ],
            [
              16.92212,
              55.13824
            ],
            [
              16.94999,
              55.13669
            ],
            [
              16.97519,
              55.01403
            ]
          ]
        ]
      },
      "properties": {
        "osm_type": "way",
        "osm_id": 1560132096,
        "tags": {
          "boundary": "industrial",
          "construction:power": "plant",
          "name": "MFW Ba\u0142tyk II Offshore Wind Farm",
          "operator": "Equinor;Polenergia",
          "plant:output:electricity": "720 MW",
          "plant:source": "wind",
          "plant:type": "offshore",
          "start_date": "2027",
          "status": "construction",
          "turbines": "50"
        },
        "name": "MFW Ba\u0142tyk II Offshore Wind Farm",
        "power_mw": 720.0,
        "status": "construction",
        "type_inst": "offshore",
        "year": "2027",
        "n_turbines": 50,
        "category_of_offshore_production_area": 1,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#OffshoreProductionArea"
      }
    },
    {
      "type": "Feature",
      "id": "way/1560193204",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              17.30485,
              55.04237
            ],
            [
              17.32097,
              55.0531
            ],
            [
              17.3392,
              55.05365
            ],
            [
              17.3393,
              55.05369
            ],
            [
              17.38446,
              55.055
            ],
            [
              17.38475,
              55.05501
            ],
            [
              17.38526,
              55.05505
            ],
            [
              17.38576,
              55.0551
            ],
            [
              17.38626,
              55.05517
            ],
            [
              17.38674,
              55.05527
            ],
            [
              17.38722,
              55.05538
            ],
            [
              17.38768,
              55.0555
            ],
            [
              17.38812,
              55.05565
            ],
            [
              17.38855,
              55.05581
            ],
            [
              17.38896,
              55.05599
            ],
            [
              17.38935,
              55.05618
            ],
            [
              17.38972,
              55.05638
            ],
            [
              17.39006,
              55.0566
            ],
            [
              17.39037,
              55.05683
            ],
            [
              17.39066,
              55.05708
            ],
            [
              17.39092,
              55.05733
            ],
            [
              17.39115,
              55.05759
            ],
            [
              17.39136,
              55.05786
            ],
            [
              17.39122,
              55.05814
            ],
            [
              17.39166,
              55.05842
            ],
            [
              17.39177,
              55.05871
            ],
            [
              17.39184,
              55.059
            ],
            [
              17.39188,
              55.0593
            ],
            [
              17.39187,
              55.05972
            ],
            [
              17.38848,
              55.09758
            ],
            [
              17.45562,
              55.09956
            ],
            [
              17.45563,
              55.09956
            ],
            [
              17.55269,
              55.10238
            ],
            [
              17.54074,
              55.06522
            ],
            [
              17.54073,
              55.06521
            ],
            [
              17.53442,
              55.0452
            ],
            [
              17.52893,
              55.03915
            ],
            [
              17.52878,
              55.03898
            ],
            [
              17.52858,
              55.03871
            ],
            [
              17.52841,
              55.03843
            ],
            [
              17.52827,
              55.03815
            ],
            [
              17.52816,
              55.03786
            ],
            [
              17.52809,
              55.03757
            ],
            [
              17.52805,
              55.03727
            ],
            [
              17.52804,
              55.03698
            ],
            [
              17.52807,
              55.03669
            ],
            [
              17.5281,
              55.03655
            ],
            [
              17.53513,
              55.00209
            ],
            [
              17.3133,
              55.0409
            ],
            [
              17.30485,
              55.04237
            ]
          ]
        ]
      },
      "properties": {
        "osm_type": "way",
        "osm_id": 1560193204,
        "tags": {
          "boundary": "maritime",
          "industrial": "windfarm",
          "name": "Baltica 3 OWF",
          "operator": "PGE / \u00d8rsted",
          "plant:source": "wind",
          "seamark:name": "Baltica 3",
          "seamark:production_area:product": "power",
          "seamark:type": "production_area"
        },
        "name": "Baltica 3 OWF",
        "category_of_offshore_production_area": 1,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#OffshoreProductionArea"
      }
    },
    {
      "type": "Feature",
      "id": "way/1560193205",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              17.04888,
              55.0159
            ],
            [
              16.97915,
              55.03365
            ],
            [
              16.96261,
              55.11424
            ],
            [
              17.03059,
              55.11418
            ],
            [
              17.09057,
              55.10969
            ],
            [
              17.09066,
              55.10968
            ],
            [
              17.16009,
              55.10494
            ],
            [
              17.16009,
              55.10494
            ],
            [
              17.22777,
              55.10031
            ],
            [
              17.22788,
              55.10031
            ],
            [
              17.22839,
              55.10029
            ],
            [
              17.2289,
              55.10028
            ],
            [
              17.22941,
              55.1003
            ],
            [
              17.22992,
              55.10034
            ],
            [
              17.23043,
              55.10039
            ],
            [
              17.23092,
              55.10047
            ],
            [
              17.23109,
              55.1005
            ],
            [
              17.26984,
              55.1076
            ],
            [
              17.27155,
              55.08923
            ],
            [
              17.25706,
              55.07957
            ],
            [
              17.24396,
              55.07084
            ],
            [
              17.22737,
              55.05977
            ],
            [
              17.20123,
              55.04231
            ],
            [
              17.18645,
              55.04306
            ],
            [
              17.17902,
              55.04545
            ],
            [
              17.12825,
              55.06174
            ],
            [
              17.1201,
              55.06952
            ],
            [
              17.12007,
              55.06956
            ],
            [
              17.11978,
              55.0698
            ],
            [
              17.11947,
              55.07004
            ],
            [
              17.11914,
              55.07026
            ],
            [
              17.11878,
              55.07047
            ],
            [
              17.11839,
              55.07066
            ],
            [
              17.11799,
              55.07084
            ],
            [
              17.11757,
              55.07101
            ],
            [
              17.11712,
              55.07116
            ],
            [
              17.11667,
              55.07129
            ],
            [
              17.11619,
              55.0714
            ],
            [
              17.11571,
              55.0715
            ],
            [
              17.11521,
              55.07158
            ],
            [
              17.11471,
              55.07163
            ],
            [
              17.1142,
              55.07167
            ],
            [
              17.11382,
              55.0717
            ],
            [
              17.11267,
              55.07168
            ],
            [
              17.11216,
              55.07164
            ],
            [
              17.11166,
              55.07159
            ],
            [
              17.11062,
              55.04174
            ],
            [
              17.11064,
              55.04171
            ],
            [
              17.11001,
              55.04167
            ],
            [
              17.10974,
              55.04162
            ],
            [
              17.1093,
              55.04157
            ],
            [
              17.10887,
              55.04151
            ],
            [
              17.10846,
              55.04145
            ],
            [
              17.10807,
              55.04138
            ],
            [
              17.10771,
              55.04131
            ],
            [
              17.10737,
              55.04123
            ],
            [
              17.10702,
              55.04114
            ],
            [
              17.10676,
              55.04106
            ],
            [
              17.10651,
              55.04096
            ],
            [
              17.1061,
              55.04087
            ],
            [
              17.10608,
              55.04077
            ],
            [
              17.10591,
              55.04067
            ],
            [
              17.10578,
              55.04057
            ],
            [
              17.10577,
              55.04056
            ],
            [
              17.08831,
              55.02524
            ],
            [
              17.08222,
              55.00972
            ],
            [
              17.08218,
              55.00873
            ],
            [
              17.04888,
              55.0159
            ]
          ]
        ]
      },
      "properties": {
        "osm_type": "way",
        "osm_id": 1560193205,
        "tags": {
          "boundary": "maritime",
          "construction:power": "plant",
          "industrial": "windfarm",
          "name": "Baltica 2 OWF",
          "operator": "PGE / \u00d8rsted",
          "plant:source": "wind",
          "seamark:name": "Baltica 2",
          "seamark:production_area:product": "power",
          "seamark:type": "production_area"
        },
        "name": "Baltica 2 OWF",
        "category_of_offshore_production_area": 1,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#OffshoreProductionArea"
      }
    },
    {
      "type": "Feature",
      "id": "way/1532855580",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              17.56412,
              54.9776
            ],
            [
              17.65142,
              54.99505
            ],
            [
              17.71816,
              55.00498
            ],
            [
              17.71614,
              55.08525
            ],
            [
              17.76867,
              55.08348
            ],
            [
              17.78045,
              55.11133
            ],
            [
              17.6207,
              55.11137
            ],
            [
              17.58828,
              55.07482
            ],
            [
              17.56412,
              54.9776
            ]
          ]
        ]
      },
      "properties": {
        "osm_type": "way",
        "osm_id": 1532855580,
        "tags": {
          "boundary": "maritime",
          "industrial": "windfarm",
          "seamark:name": "Baltic Power",
          "seamark:production_area:product": "power",
          "seamark:type": "production_area"
        },
        "name": "Baltic Power",
        "category_of_offshore_production_area": 1,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#OffshoreProductionArea"
      }
    },
    {
      "type": "Feature",
      "id": "relation/21402440",
      "geometry": null,
      "properties": {
        "osm_type": "relation",
        "osm_id": 21402440,
        "tags": {
          "name": "Baltic Power",
          "offshore": "yes",
          "operator": "Baltic Power",
          "plant:method": "wind_turbine",
          "plant:output:electricity": "1200 MW",
          "plant:source": "wind",
          "power": "plant",
          "seamark:landmark:production_area": "wind_farm",
          "seamark:type": "production_area",
          "type": "multipolygon"
        },
        "members": [
          "node/14185128592:generator",
          "node/14185129403:generator",
          "node/14185129406:generator",
          "node/14185129405:generator",
          "node/14185128582:generator",
          "node/14185129426:generator",
          "node/14185129408:generator",
          "node/14185129410:generator",
          "node/14185129409:generator",
          "node/14185128600:generator",
          "node/14185129401:generator",
          "node/14185129428:generator",
          "node/14185129427:generator",
          "node/14185128599:generator",
          "node/14185128567:generator",
          "node/14185129430:generator",
          "node/14185129429:generator",
          "node/14185128574:generator",
          "node/14185128581:generator",
          "node/14185128598:generator",
          "node/14185129402:generator",
          "node/14185129412:generator",
          "node/14185128591:generator",
          "node/14185128573:generator",
          "node/14185129411:generator",
          "node/14185129404:generator",
          "node/14185128570:generator",
          "node/14185128580:generator",
          "node/14185128590:generator",
          "node/14185128572:generator",
          "node/14185128589:generator",
          "node/14185129407:generator",
          "node/14185128586:generator",
          "node/14185129414:generator",
          "node/14185128585:generator",
          "node/14185129416:generator",
          "node/14185129413:generator",
          "node/14185128588:generator",
          "node/14185128587:generator",
          "node/14185129415:generator",
          "node/14185129417:generator",
          "node/14185128564:substation",
          "node/14185128584:generator",
          "node/14185128576:generator",
          "node/14185128566:generator",
          "node/14185128568:generator",
          "node/14185128597:generator",
          "node/14185128575:generator",
          "node/14185128569:generator",
          "node/14185129432:generator",
          "node/14185128571:generator",
          "node/14185128596:generator",
          "node/14185129434:generator",
          "node/14185128595:generator",
          "node/14185129431:generator",
          "node/14185128563:substation",
          "node/14185129433:generator",
          "node/14185129425:generator",
          "node/14185129422:generator",
          "node/14185128583:generator",
          "node/14185128565:generator",
          "node/14185128578:generator",
          "node/14185129421:generator",
          "node/14185128577:generator",
          "node/14185128594:generator",
          "node/14185129423:generator",
          "node/14185128593:generator",
          "node/14185129418:generator",
          "node/14185128579:generator",
          "node/14185129424:generator",
          "node/14185129420:generator",
          "node/14185129419:generator",
          "node/14185129435:generator",
          "node/14185129436:generator",
          "node/14185129438:generator",
          "node/14185129437:generator",
          "node/14185129439:generator",
          "node/14185129440:generator",
          "way/1532855580:outer"
        ],
        "name": "Baltic Power",
        "power_mw": 1200.0,
        "category_of_offshore_production_area": 1,
        "iho_feature_role": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#OffshoreProductionArea"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix em: <https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix iho: <https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#> .
@prefix ns1: <generator:> .
@prefix ns10: <seamark:platform:> .
@prefix ns11: <seamark:landmark:> .
@prefix ns2: <rotor:> .
@prefix ns3: <height:> .
@prefix ns4: <generator:output:> .
@prefix ns5: <plant:> .
@prefix ns6: <construction:> .
@prefix ns7: <seamark:> .
@prefix ns8: <plant:output:> .
@prefix ns9: <seamark:production_area:> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix seadots-emodnet: <https://w3id.org/ogc/hosted/seadots/emodnet/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/node/14185128563> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.762493e+01 5.503138e+01 ) ] ;
    geojson:properties [ seadots-emodnet:name "Baltic Power OSS West" ;
            seadots-emodnet:osm_id 14185128563 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ seadots-emodnet:location "sea" ;
                    seadots-emodnet:name "Baltic Power OSS West" ;
                    seadots-emodnet:power "substation" ;
                    seadots-emodnet:substation "generation" ;
                    seadots-emodnet:voltage "230000;66000" ;
                    ns10:category "production" ;
                    ns7:type "platform" ] ] .

<file:///github/workspace/node/14185128564> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.768719e+01 5.505119e+01 ) ] ;
    geojson:properties [ seadots-emodnet:name "Baltic Power OSS East" ;
            seadots-emodnet:osm_id 14185128564 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ seadots-emodnet:location "sea" ;
                    seadots-emodnet:name "Baltic Power OSS East" ;
                    seadots-emodnet:power "substation" ;
                    seadots-emodnet:substation "generation" ;
                    seadots-emodnet:voltage "230000;66000" ;
                    ns10:category "production" ;
                    ns7:type "platform" ] ] .

<file:///github/workspace/node/14185128565> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.765358e+01 5.500667e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128565 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "76" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128566> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.763486e+01 5.502063e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128566 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "75" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128567> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.766107e+01 5.508046e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128567 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "74" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128568> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.764328e+01 5.506036e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128568 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "73" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128569> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.764e+01 5.504937e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128569 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "72" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128570> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.766812e+01 5.510027e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128570 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "71" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128571> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.761012e+01 5.504387e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128571 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "70" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128572> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.768346e+01 5.506614e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128572 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "69" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128573> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.774762e+01 5.509924e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128573 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "68" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128574> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.765435e+01 5.507138e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128574 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "67" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128575> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.764002e+01 5.503966e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128575 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "66" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128576> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.763531e+01 5.502982e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128576 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "65" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128577> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.762887e+01 5.500997e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128577 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "64" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128578> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.762683e+01 5.500081e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128578 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "63" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128579> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.758926e+01 5.499338e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128579 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "62" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128580> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.771684e+01 5.50906e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128580 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "61" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128581> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.766301e+01 5.509107e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128581 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "60" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128582> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.767817e+01 5.51094e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128582 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "59" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128583> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.767228e+01 5.50146e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128583 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "58" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128584> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.767218e+01 5.502328e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128584 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "57" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128585> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.767545e+01 5.503189e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128585 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "56" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128586> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.767507e+01 5.504086e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128586 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "55" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128587> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.767309e+01 5.504981e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128587 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "54" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128588> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.766844e+01 5.50588e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128588 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "53" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128589> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.768571e+01 5.507647e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128589 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "52" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128590> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.76895e+01 5.508797e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128590 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "51" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128591> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.769492e+01 5.509878e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128591 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "50" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128592> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770164e+01 5.510965e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128592 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "49" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128593> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.759436e+01 5.500322e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128593 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "48" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128594> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.760223e+01 5.50149e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128594 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "47" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128595> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.760432e+01 5.502411e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128595 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "46" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128596> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.760638e+01 5.503469e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128596 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "45" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128597> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.761611e+01 5.505298e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128597 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "44" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128598> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.761844e+01 5.50638e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128598 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "43" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128599> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.762462e+01 5.507448e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128599 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "42" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185128600> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.763226e+01 5.508373e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185128600 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "41" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129401> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.763667e+01 5.50928e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129401 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "40" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129402> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.763818e+01 5.51029e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129402 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "39" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129403> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.76546e+01 5.510918e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129403 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "38" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129404> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.772245e+01 5.510092e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129404 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "37" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129405> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.772459e+01 5.510981e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129405 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "36" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129406> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.774705e+01 5.51082e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129406 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "35" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129407> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.774346e+01 5.509015e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129407 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "34" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129408> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.776984e+01 5.510858e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129408 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "33" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129409> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.77716e+01 5.509879e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129409 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "32" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129410> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.776571e+01 5.508855e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129410 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "31" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129411> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770855e+01 5.508098e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129411 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "30" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129412> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770855e+01 5.50718e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129412 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "29" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129413> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770855e+01 5.506282e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129413 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "28" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129414> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770856e+01 5.50538e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129414 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "27" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129415> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770858e+01 5.504482e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129415 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "26" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129416> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770862e+01 5.503583e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129416 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "25" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129417> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770864e+01 5.502344e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129417 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "24" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129418> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770859e+01 5.501423e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129418 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "23" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129419> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.770896e+01 5.500527e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129419 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "22" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129420> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.768887e+01 5.500887e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129420 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "21" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129421> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.767377e+01 5.500127e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129421 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "20" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129422> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.76507e+01 5.499582e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129422 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "19" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129423> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.762848e+01 5.499182e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129423 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "18" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129424> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.760743e+01 5.498794e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129424 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "17" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129425> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.758752e+01 5.498289e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129425 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "16" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129426> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.762182e+01 5.510877e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129426 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "15" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129427> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.761634e+01 5.509955e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129427 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "14" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129428> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.761225e+01 5.50888e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129428 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "13" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129429> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.760376e+01 5.507959e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129429 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "12" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129430> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.759547e+01 5.507059e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129430 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "11" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129431> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.758705e+01 5.506144e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129431 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "10" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129432> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.758379e+01 5.505254e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129432 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "9" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129433> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.758153e+01 5.504358e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129433 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "8" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129434> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.757925e+01 5.503458e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129434 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "7" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129435> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.757696e+01 5.502553e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129435 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "6" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129436> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.757467e+01 5.501648e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129436 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "5" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129437> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.757237e+01 5.500736e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129437 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "4" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129438> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.757008e+01 5.499832e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129438 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "3" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129439> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.75678e+01 5.498929e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129439 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "2" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14185129440> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.756552e+01 5.498027e+01 ) ] ;
    geojson:properties [ em:powerMW 1.5e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14185129440 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "15 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    ns3:hub "141" ;
                    seadots-emodnet:manufacturer "Vestas" ;
                    seadots-emodnet:model "V236-15.0 MW" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "1" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537539> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.735356e+01 5.499707e+01 ) ] ;
    geojson:properties [ seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:name "MFW Bałtyk III Offshore Substation" ;
            seadots-emodnet:osm_id 14191537539 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:name "MFW Bałtyk III Offshore Substation" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "substation" ;
                    seadots-emodnet:ref "BK3 OSS" ;
                    seadots-emodnet:substation "transmission" ;
                    seadots-emodnet:voltage "220000;66000" ] ] .

<file:///github/workspace/node/14191537540> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.727005e+01 5.499878e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537540 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 M04" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537541> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.727541e+01 5.501067e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537541 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 M03" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537542> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.728105e+01 5.502246e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537542 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 M02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537543> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.728381e+01 5.498389e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537543 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 L05" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537544> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.728946e+01 5.499559e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537544 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 L04" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537545> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.729541e+01 5.500735e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537545 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 L03" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537546> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.730046e+01 5.501902e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537546 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 L02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537547> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.730608e+01 5.503064e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537547 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 L01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537548> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.72925e+01 5.495707e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537548 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 K07" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537549> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.729817e+01 5.496872e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537549 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 K06" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537550> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.730348e+01 5.498053e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537550 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 K05" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537551> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.730896e+01 5.499226e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537551 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 K04" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537552> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.731449e+01 5.500367e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537552 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 K03" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537553> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.731991e+01 5.501559e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537553 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 K02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537554> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.732559e+01 5.502728e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537554 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 K01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537555> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.731185e+01 5.495373e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537555 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 J07" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537556> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.731743e+01 5.496536e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537556 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 J06" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537557> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.732287e+01 5.497706e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537557 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 J05" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537558> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.732849e+01 5.498885e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537558 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 J04" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537559> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.733377e+01 5.500045e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537559 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 J03" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537560> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.733931e+01 5.50122e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537560 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 J02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537561> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.734481e+01 5.502392e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537561 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 J01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537562> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.733677e+01 5.496209e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537562 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 H06" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537563> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.734226e+01 5.497366e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537563 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 H05" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537564> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.734798e+01 5.498538e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537564 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 H04" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537565> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.736425e+01 5.502055e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537565 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 H01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537566> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.735613e+01 5.49585e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537566 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 G06" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537567> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.73617e+01 5.497031e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537567 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 G05" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537568> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.73729e+01 5.499377e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537568 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 G03" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537569> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.737807e+01 5.500545e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537569 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 G02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537570> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.738362e+01 5.501712e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537570 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 G01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537571> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.738124e+01 5.496689e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537571 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 F05" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537572> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.738653e+01 5.497858e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537572 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 F04" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537573> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.739201e+01 5.499022e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537573 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 F03" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537574> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.740311e+01 5.501374e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537574 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 F01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537575> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.740052e+01 5.496347e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537575 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 E05" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537576> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.740578e+01 5.497531e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537576 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 E04" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537577> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.741168e+01 5.498702e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537577 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 E03" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537578> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.741696e+01 5.49986e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537578 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 E02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537579> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.742238e+01 5.501032e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537579 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 E01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537580> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.742528e+01 5.497176e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537580 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 D04" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537581> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.743081e+01 5.498352e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537581 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 D03" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537582> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.74362e+01 5.49952e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537582 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 D02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537583> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.744177e+01 5.500691e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537583 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 D01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537584> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.745015e+01 5.498002e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537584 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 C03" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537585> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.745567e+01 5.499177e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537585 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 C02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537586> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.746127e+01 5.500353e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537586 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 C01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537587> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.747507e+01 5.498838e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537587 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 B02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537588> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.748057e+01 5.499996e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537588 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 B01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191537589> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.749978e+01 5.499656e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191537589 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK3 A01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571016> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.688412e+01 5.509105e+01 ) ] ;
    geojson:properties [ seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:name "MFW Bałtyk II Offshore Substation" ;
            seadots-emodnet:osm_id 14191571016 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:name "MFW Bałtyk II Offshore Substation" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "substation" ;
                    seadots-emodnet:ref "BK2 OSS" ;
                    seadots-emodnet:substation "transmission" ;
                    seadots-emodnet:voltage "220000;66000" ] ] .

<file:///github/workspace/node/14191571017> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.67776e+01 5.5108e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571017 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 J02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571018> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.680314e+01 5.508687e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571018 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 H04" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571019> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.680055e+01 5.509781e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571019 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 H03" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571020> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.679816e+01 5.510893e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571020 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 H02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571021> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.682537e+01 5.507658e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571021 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 G05" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571022> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.682296e+01 5.508794e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571022 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 G04" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571023> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.682072e+01 5.509906e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571023 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 G03" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571024> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.681869e+01 5.51099e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571024 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 G02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571025> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.681603e+01 5.512121e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571025 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 G01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571026> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.684783e+01 5.506684e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571026 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 F06" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571027> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.684575e+01 5.507773e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571027 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 F05" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571028> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.684345e+01 5.508889e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571028 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 F04" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571029> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.684111e+01 5.510004e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571029 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 F03" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571030> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.683836e+01 5.511103e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571030 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 F02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571031> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.68365e+01 5.512231e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571031 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 F01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571032> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.686798e+01 5.506797e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571032 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 E06" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571033> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.686587e+01 5.507891e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571033 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 E05" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571034> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.686363e+01 5.509011e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571034 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 E04" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571035> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.685869e+01 5.511234e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571035 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 E02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571036> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.6856e+01 5.512346e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571036 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 E01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571037> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.689104e+01 5.505779e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571037 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 D07" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571038> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.688808e+01 5.50688e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571038 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 D06" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571039> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.688626e+01 5.507997e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571039 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 D05" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571040> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.688153e+01 5.510228e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571040 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 D03" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571041> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.687895e+01 5.511362e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571041 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 D02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571042> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.687668e+01 5.512452e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571042 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 D01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571043> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.691368e+01 5.504767e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571043 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 C08" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571044> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.691121e+01 5.505851e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571044 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 C07" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571045> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.690873e+01 5.507015e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571045 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 C06" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571046> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.690412e+01 5.509222e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571046 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 C04" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571047> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.689871e+01 5.511362e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571047 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 C02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571048> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.689714e+01 5.512559e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571048 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 C01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571049> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.693639e+01 5.503735e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571049 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 B09" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571050> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.693361e+01 5.504874e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571050 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 B08" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571051> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.69316e+01 5.505984e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571051 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 B07" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571052> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.692912e+01 5.507094e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571052 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 B06" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571053> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.692701e+01 5.508208e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571053 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 B05" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571054> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.692447e+01 5.509334e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571054 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 B04" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571055> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.69224e+01 5.510413e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571055 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 B03" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571056> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.691954e+01 5.511559e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571056 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 B02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571057> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.691725e+01 5.512673e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571057 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 B01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571058> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.695657e+01 5.503868e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571058 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 A09" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571059> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.695422e+01 5.50498e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571059 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 A08" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571060> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.695173e+01 5.506098e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571060 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 A07" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571061> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.694915e+01 5.507234e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571061 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 A06" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571062> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.694712e+01 5.508304e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571062 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 A05" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571063> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.694459e+01 5.509417e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571063 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 A04" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571064> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.694217e+01 5.510557e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571064 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 A03" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571065> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.694029e+01 5.511681e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571065 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 A02" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191571066> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.693714e+01 5.512781e+01 ) ] ;
    geojson:properties [ iho:featureRole iho:WindTurbine ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:osm_id 14191571066 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns1:source "wind" ;
                    ns1:type "offshore" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-236 DD" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "BK2 A01" ;
                    ns2:diameter "236" ] ] .

<file:///github/workspace/node/14191911456> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.705676e+01 5.505042e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911456 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "G16" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911457> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.716228e+01 5.507434e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911457 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "F24" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911458> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.705514e+01 5.505911e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911458 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "F16" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911459> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.699413e+01 5.504852e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911459 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "F12" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911460> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.708136e+01 5.508485e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911460 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "F04" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911461> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.720759e+01 5.508408e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911461 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "F03" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911462> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.714581e+01 5.50777e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911462 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "E24" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911463> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.717915e+01 5.504845e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911463 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "E23" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911464> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.726865e+01 5.509771e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911464 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "E21" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911465> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.720592e+01 5.509244e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911465 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "E19" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911466> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.697586e+01 5.506017e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911466 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "E17" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911467> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.702308e+01 5.506088e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911467 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "E16" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911468> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.700884e+01 5.505364e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911468 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "E12" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911469> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.697936e+01 5.504307e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911469 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "E11" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911470> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.708698e+01 5.502731e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911470 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "E08" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911471> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.704343e+01 5.511174e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911471 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "E06" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911472> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.706485e+01 5.508823e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911472 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "E05" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911473> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.713015e+01 5.507724e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911473 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "E04" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911474> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.719098e+01 5.508831e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911474 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "E03" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911475> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.710555e+01 5.510715e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911475 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "E01" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911476> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.714781e+01 5.506772e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911476 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D24" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911477> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.714991e+01 5.505728e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911477 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D23" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911478> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.726886e+01 5.508929e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911478 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D21" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911479> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.724511e+01 5.51018e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911479 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D20" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911480> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.723017e+01 5.509884e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911480 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D19" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911481> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.697318e+01 5.507473e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911481 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D18" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911482> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.697761e+01 5.505161e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911482 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D17" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911483> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.703697e+01 5.507025e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911483 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D16" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911484> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.710478e+01 5.507016e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911484 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D15" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911485> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.699636e+01 5.511284e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911485 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D14" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911486> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.696483e+01 5.511279e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911486 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D13" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911487> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.698107e+01 5.503456e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911487 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D11" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911488> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.702511e+01 5.50233e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911488 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D10" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911489> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.707141e+01 5.501194e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911489 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D09" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911490> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.709376e+01 5.504418e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911490 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D08" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911491> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.706945e+01 5.506554e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911491 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D07" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911492> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.705896e+01 5.511084e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911492 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D06" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911493> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.706266e+01 5.509905e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911493 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D05" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911494> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.70977e+01 5.508177e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911494 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D04" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911495> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.72146e+01 5.509997e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911495 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D02" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911496> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.712107e+01 5.510639e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911496 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "D01" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911497> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.716454e+01 5.506287e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911497 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C24" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911498> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.716461e+01 5.505315e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911498 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C23" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911499> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.719478e+01 5.504513e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911499 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C22" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191911500> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.72586e+01 5.508246e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191911500 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C21" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968201> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.726001e+01 5.510446e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968201 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C20" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968202> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.7222e+01 5.509048e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968202 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C19" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968203> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.696943e+01 5.509297e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968203 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C18" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968204> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.699237e+01 5.50571e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968204 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C17" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968205> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.70403e+01 5.50539e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968205 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C16" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968206> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.709799e+01 5.506137e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968206 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C15" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968207> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.696725e+01 5.51036e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968207 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C13" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968208> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.699589e+01 5.503992e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968208 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C12" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968209> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.699576e+01 5.503076e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968209 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C11" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968210> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.705538e+01 5.501558e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968210 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C10" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968211> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.708337e+01 5.501866e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968211 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C09" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968212> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.709034e+01 5.503558e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968212 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C08" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968213> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.707118e+01 5.505702e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968213 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C07" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968214> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.707457e+01 5.510974e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968214 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C06" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968215> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.707807e+01 5.510079e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968215 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C05" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968216> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.713341e+01 5.506146e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968216 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C04" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968217> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.719319e+01 5.5077e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968217 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C03" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968218> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.719918e+01 5.510106e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968218 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C02" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968219> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.715232e+01 5.510425e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968219 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "C01" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968220> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.717897e+01 5.506972e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968220 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B24" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968221> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.718146e+01 5.505705e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968221 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B23" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968222> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.720848e+01 5.504966e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968222 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B22" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968223> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.724846e+01 5.50757e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968223 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B21" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968224> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.725315e+01 5.509213e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968224 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B20" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968225> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.722412e+01 5.50802e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968225 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B19" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968226> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.697121e+01 5.508431e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968226 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B18" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968227> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.700692e+01 5.506332e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968227 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B17" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968228> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.705326e+01 5.506769e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968228 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B16" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968229> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.708362e+01 5.507323e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968229 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B15" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968230> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.69839e+01 5.50985e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968230 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B13" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968231> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.701242e+01 5.503638e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968231 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B12" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968232> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.701071e+01 5.502696e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968232 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B11" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968233> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.704016e+01 5.501946e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968233 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B10" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968234> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.706219e+01 5.502291e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968234 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B09" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968235> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.707505e+01 5.503843e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968235 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B08" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968236> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.709481e+01 5.505316e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968236 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B07" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968237> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.709013e+01 5.510825e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968237 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B06" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968238> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.709417e+01 5.509921e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968238 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B05" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968239> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.712445e+01 5.506864e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968239 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B04" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968240> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.71766e+01 5.508136e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968240 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B03" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968241> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.718342e+01 5.510215e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968241 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "B02" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968242> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.719546e+01 5.506597e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968242 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A24" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968243> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.719729e+01 5.505604e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968243 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A23" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968244> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.721923e+01 5.50562e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968244 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A22" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968245> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.723807e+01 5.506882e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968245 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A21" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968246> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.723868e+01 5.508617e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968246 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A20" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968247> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.720974e+01 5.507345e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968247 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A19" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968248> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.698806e+01 5.50775e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968248 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A18" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968249> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.703494e+01 5.508042e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968249 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A17" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968250> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.70512e+01 5.507782e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968250 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A16" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968251> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.704649e+01 5.510128e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968251 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A14" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968252> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.700159e+01 5.508883e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968252 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A13" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968253> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.702713e+01 5.504135e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968253 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A12" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968254> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.702888e+01 5.503258e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968254 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A11" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968255> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.704547e+01 5.502911e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968255 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A10" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968256> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.706063e+01 5.503135e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968256 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A09" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968257> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.705909e+01 5.503974e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968257 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A08" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968258> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.711011e+01 5.509818e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968258 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A06" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968259> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.709589e+01 5.509067e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968259 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A05" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968260> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.715982e+01 5.508568e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968260 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A03" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968261> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.716785e+01 5.510319e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968261 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A02" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/node/14191968262> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.712655e+01 5.50952e+01 ) ] ;
    geojson:properties [ em:powerMW 1.4e+01 ;
            iho:featureRole iho:WindTurbine ;
            seadots-emodnet:osm_id 14191968262 ;
            seadots-emodnet:osm_type "node" ;
            seadots-emodnet:tags [ ns1:method "wind_turbine" ;
                    ns4:electricity "14 MW" ;
                    ns1:source "wind" ;
                    ns1:type "horizontal_axis" ;
                    seadots-emodnet:manufacturer "Siemens Gamesa" ;
                    seadots-emodnet:model "SG 14-222 DD" ;
                    seadots-emodnet:operator "PGE; Orsted" ;
                    seadots-emodnet:power "generator" ;
                    seadots-emodnet:ref "A01" ;
                    ns2:diameter "222" ] ] .

<file:///github/workspace/relation/21402440> a geojson:Feature ;
    geojson:properties [ em:powerMW 1.2e+03 ;
            iho:categoryOfOffshoreProductionArea 1 ;
            iho:featureRole iho:OffshoreProductionArea ;
            seadots-emodnet:members "node/14185128563:substation",
                "node/14185128564:substation",
                "node/14185128565:generator",
                "node/14185128566:generator",
                "node/14185128567:generator",
                "node/14185128568:generator",
                "node/14185128569:generator",
                "node/14185128570:generator",
                "node/14185128571:generator",
                "node/14185128572:generator",
                "node/14185128573:generator",
                "node/14185128574:generator",
                "node/14185128575:generator",
                "node/14185128576:generator",
                "node/14185128577:generator",
                "node/14185128578:generator",
                "node/14185128579:generator",
                "node/14185128580:generator",
                "node/14185128581:generator",
                "node/14185128582:generator",
                "node/14185128583:generator",
                "node/14185128584:generator",
                "node/14185128585:generator",
                "node/14185128586:generator",
                "node/14185128587:generator",
                "node/14185128588:generator",
                "node/14185128589:generator",
                "node/14185128590:generator",
                "node/14185128591:generator",
                "node/14185128592:generator",
                "node/14185128593:generator",
                "node/14185128594:generator",
                "node/14185128595:generator",
                "node/14185128596:generator",
                "node/14185128597:generator",
                "node/14185128598:generator",
                "node/14185128599:generator",
                "node/14185128600:generator",
                "node/14185129401:generator",
                "node/14185129402:generator",
                "node/14185129403:generator",
                "node/14185129404:generator",
                "node/14185129405:generator",
                "node/14185129406:generator",
                "node/14185129407:generator",
                "node/14185129408:generator",
                "node/14185129409:generator",
                "node/14185129410:generator",
                "node/14185129411:generator",
                "node/14185129412:generator",
                "node/14185129413:generator",
                "node/14185129414:generator",
                "node/14185129415:generator",
                "node/14185129416:generator",
                "node/14185129417:generator",
                "node/14185129418:generator",
                "node/14185129419:generator",
                "node/14185129420:generator",
                "node/14185129421:generator",
                "node/14185129422:generator",
                "node/14185129423:generator",
                "node/14185129424:generator",
                "node/14185129425:generator",
                "node/14185129426:generator",
                "node/14185129427:generator",
                "node/14185129428:generator",
                "node/14185129429:generator",
                "node/14185129430:generator",
                "node/14185129431:generator",
                "node/14185129432:generator",
                "node/14185129433:generator",
                "node/14185129434:generator",
                "node/14185129435:generator",
                "node/14185129436:generator",
                "node/14185129437:generator",
                "node/14185129438:generator",
                "node/14185129439:generator",
                "node/14185129440:generator",
                "way/1532855580:outer" ;
            seadots-emodnet:name "Baltic Power" ;
            seadots-emodnet:osm_id 21402440 ;
            seadots-emodnet:osm_type "relation" ;
            seadots-emodnet:tags [ a seadots-emodnet:multipolygon ;
                    seadots-emodnet:name "Baltic Power" ;
                    seadots-emodnet:offshore "yes" ;
                    seadots-emodnet:operator "Baltic Power" ;
                    seadots-emodnet:power "plant" ;
                    ns5:method "wind_turbine" ;
                    ns8:electricity "1200 MW" ;
                    ns5:source "wind" ;
                    ns11:production_area "wind_farm" ;
                    ns7:type "production_area" ] ] .

<file:///github/workspace/way/1532855580> a geojson:Feature ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.756412e+01 5.49776e+01 ) ( 1.765142e+01 5.499505e+01 ) ( 1.771816e+01 5.500498e+01 ) ( 1.771614e+01 5.508525e+01 ) ( 1.776867e+01 5.508348e+01 ) ( 1.778045e+01 5.511133e+01 ) ( 1.76207e+01 5.511137e+01 ) ( 1.758828e+01 5.507482e+01 ) ( 1.756412e+01 5.49776e+01 ) ) ) ] ;
    geojson:properties [ iho:categoryOfOffshoreProductionArea 1 ;
            iho:featureRole iho:OffshoreProductionArea ;
            seadots-emodnet:name "Baltic Power" ;
            seadots-emodnet:osm_id 1532855580 ;
            seadots-emodnet:osm_type "way" ;
            seadots-emodnet:tags [ seadots-emodnet:boundary "maritime" ;
                    seadots-emodnet:industrial "windfarm" ;
                    ns7:name "Baltic Power" ;
                    ns9:product "power" ;
                    ns7:type "production_area" ] ] .

<file:///github/workspace/way/1560132096> a geojson:Feature ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.697519e+01 5.501403e+01 ) ( 1.685987e+01 5.503507e+01 ) ( 1.684804e+01 5.503533e+01 ) ( 1.677326e+01 5.510242e+01 ) ( 1.677199e+01 5.510329e+01 ) ( 1.674361e+01 5.511839e+01 ) ( 1.678563e+01 5.512361e+01 ) ( 1.68413e+01 5.513174e+01 ) ( 1.68929e+01 5.513481e+01 ) ( 1.692212e+01 5.513824e+01 ) ( 1.694999e+01 5.513669e+01 ) ( 1.697519e+01 5.501403e+01 ) ) ) ] ;
    geojson:properties [ schema:additionalType "offshore" ;
            em:nTurbines 50 ;
            em:powerMW 7.2e+02 ;
            em:year "2027" ;
            iho:categoryOfOffshoreProductionArea 1 ;
            iho:featureRole iho:OffshoreProductionArea ;
            seadots-emodnet: seadots-emodnet:construction ;
            seadots-emodnet:name "MFW Bałtyk II Offshore Wind Farm" ;
            seadots-emodnet:osm_id 1560132096 ;
            seadots-emodnet:osm_type "way" ;
            seadots-emodnet:tags [ ns6:power "plant" ;
                    seadots-emodnet: seadots-emodnet:construction ;
                    seadots-emodnet:boundary "industrial" ;
                    seadots-emodnet:name "MFW Bałtyk II Offshore Wind Farm" ;
                    seadots-emodnet:operator "Equinor;Polenergia" ;
                    seadots-emodnet:start_date "2027" ;
                    seadots-emodnet:turbines "50" ;
                    ns8:electricity "720 MW" ;
                    ns5:source "wind" ;
                    ns5:type "offshore" ] ] .

<file:///github/workspace/way/1560193204> a geojson:Feature ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.730485e+01 5.504237e+01 ) ( 1.732097e+01 5.50531e+01 ) ( 1.73392e+01 5.505365e+01 ) ( 1.73393e+01 5.505369e+01 ) ( 1.738446e+01 5.5055e+01 ) ( 1.738475e+01 5.505501e+01 ) ( 1.738526e+01 5.505505e+01 ) ( 1.738576e+01 5.50551e+01 ) ( 1.738626e+01 5.505517e+01 ) ( 1.738674e+01 5.505527e+01 ) ( 1.738722e+01 5.505538e+01 ) ( 1.738768e+01 5.50555e+01 ) ( 1.738812e+01 5.505565e+01 ) ( 1.738855e+01 5.505581e+01 ) ( 1.738896e+01 5.505599e+01 ) ( 1.738935e+01 5.505618e+01 ) ( 1.738972e+01 5.505638e+01 ) ( 1.739006e+01 5.50566e+01 ) ( 1.739037e+01 5.505683e+01 ) ( 1.739066e+01 5.505708e+01 ) ( 1.739092e+01 5.505733e+01 ) ( 1.739115e+01 5.505759e+01 ) ( 1.739136e+01 5.505786e+01 ) ( 1.739122e+01 5.505814e+01 ) ( 1.739166e+01 5.505842e+01 ) ( 1.739177e+01 5.505871e+01 ) ( 1.739184e+01 5.5059e+01 ) ( 1.739188e+01 5.50593e+01 ) ( 1.739187e+01 5.505972e+01 ) ( 1.738848e+01 5.509758e+01 ) ( 1.745562e+01 5.509956e+01 ) ( 1.745563e+01 5.509956e+01 ) ( 1.755269e+01 5.510238e+01 ) ( 1.754074e+01 5.506522e+01 ) ( 1.754073e+01 5.506521e+01 ) ( 1.753442e+01 5.50452e+01 ) ( 1.752893e+01 5.503915e+01 ) ( 1.752878e+01 5.503898e+01 ) ( 1.752858e+01 5.503871e+01 ) ( 1.752841e+01 5.503843e+01 ) ( 1.752827e+01 5.503815e+01 ) ( 1.752816e+01 5.503786e+01 ) ( 1.752809e+01 5.503757e+01 ) ( 1.752805e+01 5.503727e+01 ) ( 1.752804e+01 5.503698e+01 ) ( 1.752807e+01 5.503669e+01 ) ( 1.75281e+01 5.503655e+01 ) ( 1.753513e+01 5.500209e+01 ) ( 1.73133e+01 5.50409e+01 ) ( 1.730485e+01 5.504237e+01 ) ) ) ] ;
    geojson:properties [ iho:categoryOfOffshoreProductionArea 1 ;
            iho:featureRole iho:OffshoreProductionArea ;
            seadots-emodnet:name "Baltica 3 OWF" ;
            seadots-emodnet:osm_id 1560193204 ;
            seadots-emodnet:osm_type "way" ;
            seadots-emodnet:tags [ seadots-emodnet:boundary "maritime" ;
                    seadots-emodnet:industrial "windfarm" ;
                    seadots-emodnet:name "Baltica 3 OWF" ;
                    seadots-emodnet:operator "PGE / Ørsted" ;
                    ns5:source "wind" ;
                    ns7:name "Baltica 3" ;
                    ns9:product "power" ;
                    ns7:type "production_area" ] ] .

<file:///github/workspace/way/1560193205> a geojson:Feature ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 1.704888e+01 5.50159e+01 ) ( 1.697915e+01 5.503365e+01 ) ( 1.696261e+01 5.511424e+01 ) ( 1.703059e+01 5.511418e+01 ) ( 1.709057e+01 5.510969e+01 ) ( 1.709066e+01 5.510968e+01 ) ( 1.716009e+01 5.510494e+01 ) ( 1.716009e+01 5.510494e+01 ) ( 1.722777e+01 5.510031e+01 ) ( 1.722788e+01 5.510031e+01 ) ( 1.722839e+01 5.510029e+01 ) ( 1.72289e+01 5.510028e+01 ) ( 1.722941e+01 5.51003e+01 ) ( 1.722992e+01 5.510034e+01 ) ( 1.723043e+01 5.510039e+01 ) ( 1.723092e+01 5.510047e+01 ) ( 1.723109e+01 5.51005e+01 ) ( 1.726984e+01 5.51076e+01 ) ( 1.727155e+01 5.508923e+01 ) ( 1.725706e+01 5.507957e+01 ) ( 1.724396e+01 5.507084e+01 ) ( 1.722737e+01 5.505977e+01 ) ( 1.720123e+01 5.504231e+01 ) ( 1.718645e+01 5.504306e+01 ) ( 1.717902e+01 5.504545e+01 ) ( 1.712825e+01 5.506174e+01 ) ( 1.71201e+01 5.506952e+01 ) ( 1.712007e+01 5.506956e+01 ) ( 1.711978e+01 5.50698e+01 ) ( 1.711947e+01 5.507004e+01 ) ( 1.711914e+01 5.507026e+01 ) ( 1.711878e+01 5.507047e+01 ) ( 1.711839e+01 5.507066e+01 ) ( 1.711799e+01 5.507084e+01 ) ( 1.711757e+01 5.507101e+01 ) ( 1.711712e+01 5.507116e+01 ) ( 1.711667e+01 5.507129e+01 ) ( 1.711619e+01 5.50714e+01 ) ( 1.711571e+01 5.50715e+01 ) ( 1.711521e+01 5.507158e+01 ) ( 1.711471e+01 5.507163e+01 ) ( 1.71142e+01 5.507167e+01 ) ( 1.711382e+01 5.50717e+01 ) ( 1.711267e+01 5.507168e+01 ) ( 1.711216e+01 5.507164e+01 ) ( 1.711166e+01 5.507159e+01 ) ( 1.711062e+01 5.504174e+01 ) ( 1.711064e+01 5.504171e+01 ) ( 1.711001e+01 5.504167e+01 ) ( 1.710974e+01 5.504162e+01 ) ( 1.71093e+01 5.504157e+01 ) ( 1.710887e+01 5.504151e+01 ) ( 1.710846e+01 5.504145e+01 ) ( 1.710807e+01 5.504138e+01 ) ( 1.710771e+01 5.504131e+01 ) ( 1.710737e+01 5.504123e+01 ) ( 1.710702e+01 5.504114e+01 ) ( 1.710676e+01 5.504106e+01 ) ( 1.710651e+01 5.504096e+01 ) ( 1.71061e+01 5.504087e+01 ) ( 1.710608e+01 5.504077e+01 ) ( 1.710591e+01 5.504067e+01 ) ( 1.710578e+01 5.504057e+01 ) ( 1.710577e+01 5.504056e+01 ) ( 1.708831e+01 5.502524e+01 ) ( 1.708222e+01 5.500972e+01 ) ( 1.708218e+01 5.500873e+01 ) ( 1.704888e+01 5.50159e+01 ) ) ) ] ;
    geojson:properties [ iho:categoryOfOffshoreProductionArea 1 ;
            iho:featureRole iho:OffshoreProductionArea ;
            seadots-emodnet:name "Baltica 2 OWF" ;
            seadots-emodnet:osm_id 1560193205 ;
            seadots-emodnet:osm_type "way" ;
            seadots-emodnet:tags [ ns6:power "plant" ;
                    seadots-emodnet:boundary "maritime" ;
                    seadots-emodnet:industrial "windfarm" ;
                    seadots-emodnet:name "Baltica 2 OWF" ;
                    seadots-emodnet:operator "PGE / Ørsted" ;
                    ns5:source "wind" ;
                    ns7:name "Baltica 2" ;
                    ns9:product "power" ;
                    ns7:type "production_area" ] ] .

[] a geojson:FeatureCollection ;
    geojson:features <file:///github/workspace/node/14185128563>,
        <file:///github/workspace/node/14185128564>,
        <file:///github/workspace/node/14185128565>,
        <file:///github/workspace/node/14185128566>,
        <file:///github/workspace/node/14185128567>,
        <file:///github/workspace/node/14185128568>,
        <file:///github/workspace/node/14185128569>,
        <file:///github/workspace/node/14185128570>,
        <file:///github/workspace/node/14185128571>,
        <file:///github/workspace/node/14185128572>,
        <file:///github/workspace/node/14185128573>,
        <file:///github/workspace/node/14185128574>,
        <file:///github/workspace/node/14185128575>,
        <file:///github/workspace/node/14185128576>,
        <file:///github/workspace/node/14185128577>,
        <file:///github/workspace/node/14185128578>,
        <file:///github/workspace/node/14185128579>,
        <file:///github/workspace/node/14185128580>,
        <file:///github/workspace/node/14185128581>,
        <file:///github/workspace/node/14185128582>,
        <file:///github/workspace/node/14185128583>,
        <file:///github/workspace/node/14185128584>,
        <file:///github/workspace/node/14185128585>,
        <file:///github/workspace/node/14185128586>,
        <file:///github/workspace/node/14185128587>,
        <file:///github/workspace/node/14185128588>,
        <file:///github/workspace/node/14185128589>,
        <file:///github/workspace/node/14185128590>,
        <file:///github/workspace/node/14185128591>,
        <file:///github/workspace/node/14185128592>,
        <file:///github/workspace/node/14185128593>,
        <file:///github/workspace/node/14185128594>,
        <file:///github/workspace/node/14185128595>,
        <file:///github/workspace/node/14185128596>,
        <file:///github/workspace/node/14185128597>,
        <file:///github/workspace/node/14185128598>,
        <file:///github/workspace/node/14185128599>,
        <file:///github/workspace/node/14185128600>,
        <file:///github/workspace/node/14185129401>,
        <file:///github/workspace/node/14185129402>,
        <file:///github/workspace/node/14185129403>,
        <file:///github/workspace/node/14185129404>,
        <file:///github/workspace/node/14185129405>,
        <file:///github/workspace/node/14185129406>,
        <file:///github/workspace/node/14185129407>,
        <file:///github/workspace/node/14185129408>,
        <file:///github/workspace/node/14185129409>,
        <file:///github/workspace/node/14185129410>,
        <file:///github/workspace/node/14185129411>,
        <file:///github/workspace/node/14185129412>,
        <file:///github/workspace/node/14185129413>,
        <file:///github/workspace/node/14185129414>,
        <file:///github/workspace/node/14185129415>,
        <file:///github/workspace/node/14185129416>,
        <file:///github/workspace/node/14185129417>,
        <file:///github/workspace/node/14185129418>,
        <file:///github/workspace/node/14185129419>,
        <file:///github/workspace/node/14185129420>,
        <file:///github/workspace/node/14185129421>,
        <file:///github/workspace/node/14185129422>,
        <file:///github/workspace/node/14185129423>,
        <file:///github/workspace/node/14185129424>,
        <file:///github/workspace/node/14185129425>,
        <file:///github/workspace/node/14185129426>,
        <file:///github/workspace/node/14185129427>,
        <file:///github/workspace/node/14185129428>,
        <file:///github/workspace/node/14185129429>,
        <file:///github/workspace/node/14185129430>,
        <file:///github/workspace/node/14185129431>,
        <file:///github/workspace/node/14185129432>,
        <file:///github/workspace/node/14185129433>,
        <file:///github/workspace/node/14185129434>,
        <file:///github/workspace/node/14185129435>,
        <file:///github/workspace/node/14185129436>,
        <file:///github/workspace/node/14185129437>,
        <file:///github/workspace/node/14185129438>,
        <file:///github/workspace/node/14185129439>,
        <file:///github/workspace/node/14185129440>,
        <file:///github/workspace/node/14191537539>,
        <file:///github/workspace/node/14191537540>,
        <file:///github/workspace/node/14191537541>,
        <file:///github/workspace/node/14191537542>,
        <file:///github/workspace/node/14191537543>,
        <file:///github/workspace/node/14191537544>,
        <file:///github/workspace/node/14191537545>,
        <file:///github/workspace/node/14191537546>,
        <file:///github/workspace/node/14191537547>,
        <file:///github/workspace/node/14191537548>,
        <file:///github/workspace/node/14191537549>,
        <file:///github/workspace/node/14191537550>,
        <file:///github/workspace/node/14191537551>,
        <file:///github/workspace/node/14191537552>,
        <file:///github/workspace/node/14191537553>,
        <file:///github/workspace/node/14191537554>,
        <file:///github/workspace/node/14191537555>,
        <file:///github/workspace/node/14191537556>,
        <file:///github/workspace/node/14191537557>,
        <file:///github/workspace/node/14191537558>,
        <file:///github/workspace/node/14191537559>,
        <file:///github/workspace/node/14191537560>,
        <file:///github/workspace/node/14191537561>,
        <file:///github/workspace/node/14191537562>,
        <file:///github/workspace/node/14191537563>,
        <file:///github/workspace/node/14191537564>,
        <file:///github/workspace/node/14191537565>,
        <file:///github/workspace/node/14191537566>,
        <file:///github/workspace/node/14191537567>,
        <file:///github/workspace/node/14191537568>,
        <file:///github/workspace/node/14191537569>,
        <file:///github/workspace/node/14191537570>,
        <file:///github/workspace/node/14191537571>,
        <file:///github/workspace/node/14191537572>,
        <file:///github/workspace/node/14191537573>,
        <file:///github/workspace/node/14191537574>,
        <file:///github/workspace/node/14191537575>,
        <file:///github/workspace/node/14191537576>,
        <file:///github/workspace/node/14191537577>,
        <file:///github/workspace/node/14191537578>,
        <file:///github/workspace/node/14191537579>,
        <file:///github/workspace/node/14191537580>,
        <file:///github/workspace/node/14191537581>,
        <file:///github/workspace/node/14191537582>,
        <file:///github/workspace/node/14191537583>,
        <file:///github/workspace/node/14191537584>,
        <file:///github/workspace/node/14191537585>,
        <file:///github/workspace/node/14191537586>,
        <file:///github/workspace/node/14191537587>,
        <file:///github/workspace/node/14191537588>,
        <file:///github/workspace/node/14191537589>,
        <file:///github/workspace/node/14191571016>,
        <file:///github/workspace/node/14191571017>,
        <file:///github/workspace/node/14191571018>,
        <file:///github/workspace/node/14191571019>,
        <file:///github/workspace/node/14191571020>,
        <file:///github/workspace/node/14191571021>,
        <file:///github/workspace/node/14191571022>,
        <file:///github/workspace/node/14191571023>,
        <file:///github/workspace/node/14191571024>,
        <file:///github/workspace/node/14191571025>,
        <file:///github/workspace/node/14191571026>,
        <file:///github/workspace/node/14191571027>,
        <file:///github/workspace/node/14191571028>,
        <file:///github/workspace/node/14191571029>,
        <file:///github/workspace/node/14191571030>,
        <file:///github/workspace/node/14191571031>,
        <file:///github/workspace/node/14191571032>,
        <file:///github/workspace/node/14191571033>,
        <file:///github/workspace/node/14191571034>,
        <file:///github/workspace/node/14191571035>,
        <file:///github/workspace/node/14191571036>,
        <file:///github/workspace/node/14191571037>,
        <file:///github/workspace/node/14191571038>,
        <file:///github/workspace/node/14191571039>,
        <file:///github/workspace/node/14191571040>,
        <file:///github/workspace/node/14191571041>,
        <file:///github/workspace/node/14191571042>,
        <file:///github/workspace/node/14191571043>,
        <file:///github/workspace/node/14191571044>,
        <file:///github/workspace/node/14191571045>,
        <file:///github/workspace/node/14191571046>,
        <file:///github/workspace/node/14191571047>,
        <file:///github/workspace/node/14191571048>,
        <file:///github/workspace/node/14191571049>,
        <file:///github/workspace/node/14191571050>,
        <file:///github/workspace/node/14191571051>,
        <file:///github/workspace/node/14191571052>,
        <file:///github/workspace/node/14191571053>,
        <file:///github/workspace/node/14191571054>,
        <file:///github/workspace/node/14191571055>,
        <file:///github/workspace/node/14191571056>,
        <file:///github/workspace/node/14191571057>,
        <file:///github/workspace/node/14191571058>,
        <file:///github/workspace/node/14191571059>,
        <file:///github/workspace/node/14191571060>,
        <file:///github/workspace/node/14191571061>,
        <file:///github/workspace/node/14191571062>,
        <file:///github/workspace/node/14191571063>,
        <file:///github/workspace/node/14191571064>,
        <file:///github/workspace/node/14191571065>,
        <file:///github/workspace/node/14191571066>,
        <file:///github/workspace/node/14191911456>,
        <file:///github/workspace/node/14191911457>,
        <file:///github/workspace/node/14191911458>,
        <file:///github/workspace/node/14191911459>,
        <file:///github/workspace/node/14191911460>,
        <file:///github/workspace/node/14191911461>,
        <file:///github/workspace/node/14191911462>,
        <file:///github/workspace/node/14191911463>,
        <file:///github/workspace/node/14191911464>,
        <file:///github/workspace/node/14191911465>,
        <file:///github/workspace/node/14191911466>,
        <file:///github/workspace/node/14191911467>,
        <file:///github/workspace/node/14191911468>,
        <file:///github/workspace/node/14191911469>,
        <file:///github/workspace/node/14191911470>,
        <file:///github/workspace/node/14191911471>,
        <file:///github/workspace/node/14191911472>,
        <file:///github/workspace/node/14191911473>,
        <file:///github/workspace/node/14191911474>,
        <file:///github/workspace/node/14191911475>,
        <file:///github/workspace/node/14191911476>,
        <file:///github/workspace/node/14191911477>,
        <file:///github/workspace/node/14191911478>,
        <file:///github/workspace/node/14191911479>,
        <file:///github/workspace/node/14191911480>,
        <file:///github/workspace/node/14191911481>,
        <file:///github/workspace/node/14191911482>,
        <file:///github/workspace/node/14191911483>,
        <file:///github/workspace/node/14191911484>,
        <file:///github/workspace/node/14191911485>,
        <file:///github/workspace/node/14191911486>,
        <file:///github/workspace/node/14191911487>,
        <file:///github/workspace/node/14191911488>,
        <file:///github/workspace/node/14191911489>,
        <file:///github/workspace/node/14191911490>,
        <file:///github/workspace/node/14191911491>,
        <file:///github/workspace/node/14191911492>,
        <file:///github/workspace/node/14191911493>,
        <file:///github/workspace/node/14191911494>,
        <file:///github/workspace/node/14191911495>,
        <file:///github/workspace/node/14191911496>,
        <file:///github/workspace/node/14191911497>,
        <file:///github/workspace/node/14191911498>,
        <file:///github/workspace/node/14191911499>,
        <file:///github/workspace/node/14191911500>,
        <file:///github/workspace/node/14191968201>,
        <file:///github/workspace/node/14191968202>,
        <file:///github/workspace/node/14191968203>,
        <file:///github/workspace/node/14191968204>,
        <file:///github/workspace/node/14191968205>,
        <file:///github/workspace/node/14191968206>,
        <file:///github/workspace/node/14191968207>,
        <file:///github/workspace/node/14191968208>,
        <file:///github/workspace/node/14191968209>,
        <file:///github/workspace/node/14191968210>,
        <file:///github/workspace/node/14191968211>,
        <file:///github/workspace/node/14191968212>,
        <file:///github/workspace/node/14191968213>,
        <file:///github/workspace/node/14191968214>,
        <file:///github/workspace/node/14191968215>,
        <file:///github/workspace/node/14191968216>,
        <file:///github/workspace/node/14191968217>,
        <file:///github/workspace/node/14191968218>,
        <file:///github/workspace/node/14191968219>,
        <file:///github/workspace/node/14191968220>,
        <file:///github/workspace/node/14191968221>,
        <file:///github/workspace/node/14191968222>,
        <file:///github/workspace/node/14191968223>,
        <file:///github/workspace/node/14191968224>,
        <file:///github/workspace/node/14191968225>,
        <file:///github/workspace/node/14191968226>,
        <file:///github/workspace/node/14191968227>,
        <file:///github/workspace/node/14191968228>,
        <file:///github/workspace/node/14191968229>,
        <file:///github/workspace/node/14191968230>,
        <file:///github/workspace/node/14191968231>,
        <file:///github/workspace/node/14191968232>,
        <file:///github/workspace/node/14191968233>,
        <file:///github/workspace/node/14191968234>,
        <file:///github/workspace/node/14191968235>,
        <file:///github/workspace/node/14191968236>,
        <file:///github/workspace/node/14191968237>,
        <file:///github/workspace/node/14191968238>,
        <file:///github/workspace/node/14191968239>,
        <file:///github/workspace/node/14191968240>,
        <file:///github/workspace/node/14191968241>,
        <file:///github/workspace/node/14191968242>,
        <file:///github/workspace/node/14191968243>,
        <file:///github/workspace/node/14191968244>,
        <file:///github/workspace/node/14191968245>,
        <file:///github/workspace/node/14191968246>,
        <file:///github/workspace/node/14191968247>,
        <file:///github/workspace/node/14191968248>,
        <file:///github/workspace/node/14191968249>,
        <file:///github/workspace/node/14191968250>,
        <file:///github/workspace/node/14191968251>,
        <file:///github/workspace/node/14191968252>,
        <file:///github/workspace/node/14191968253>,
        <file:///github/workspace/node/14191968254>,
        <file:///github/workspace/node/14191968255>,
        <file:///github/workspace/node/14191968256>,
        <file:///github/workspace/node/14191968257>,
        <file:///github/workspace/node/14191968258>,
        <file:///github/workspace/node/14191968259>,
        <file:///github/workspace/node/14191968260>,
        <file:///github/workspace/node/14191968261>,
        <file:///github/workspace/node/14191968262>,
        <file:///github/workspace/relation/21402440>,
        <file:///github/workspace/way/1532855580>,
        <file:///github/workspace/way/1560132096>,
        <file:///github/workspace/way/1560193204>,
        <file:///github/workspace/way/1560193205> ;
    seadots-emodnet:source "OpenStreetMap contributors (ODbL 1.0), api.openstreetmap.org/api/0.6/map, fetched 2026-10-27; offshore Polish Baltic, lat > 54.85" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EMODnet windfarm feature with preserved OSM source properties
description: An extension of the EMODnet windfarm model. It keeps the source OSM properties
  and adds EMODnet vocabulary properties only where explicit tags permit a defensible
  mapping. Missing EMODnet properties remain absent; no country or geometry is inferred.
oneOf:
- allOf:
  - $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/windfarm-designated-area-emodnet/schema.yaml
  - $ref: '#/$defs/osmExtensionFeature'
- type: object
  required:
  - type
  - features
  properties:
    type:
      const: FeatureCollection
      x-jsonld-id: '@type'
    source:
      type: string
    features:
      type: array
      items:
        allOf:
        - $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/windfarm-designated-area-emodnet/schema.yaml
        - $ref: '#/$defs/osmExtensionFeature'
  additionalProperties: true
$defs:
  osmExtensionFeature:
    type: object
    required:
    - id
    - type
    - geometry
    - properties
    properties:
      id:
        type: string
        description: Original OSM type/id feature identifier, retained as a source
          reference.
        x-jsonld-id: '@id'
      type:
        const: Feature
        x-jsonld-id: '@type'
      geometry:
        oneOf:
        - type: 'null'
        - type: object
          required:
          - type
          - coordinates
          properties:
            type:
              enum:
              - Point
              - MultiPoint
              - LineString
              - MultiLineString
              - Polygon
              - MultiPolygon
              x-jsonld-id: '@type'
            coordinates:
              x-jsonld-id: https://purl.org/geojson/vocab#coordinates
              x-jsonld-container: '@list'
          additionalProperties: true
        x-jsonld-id: https://purl.org/geojson/vocab#geometry
      properties:
        type: object
        required:
        - osm_type
        - osm_id
        - tags
        properties:
          country:
            type:
            - string
            - 'null'
            x-jsonld-id: https://schema.org/addressCountry
            x-jsonld-type: '@vocab'
          n_turbines:
            type:
            - number
            - 'null'
            minimum: 0
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#nTurbines
          power_mw:
            type:
            - number
            - 'null'
            minimum: 0
            description: Numeric installed capacity parsed from an explicit OSM electricity-output
              tag whose unit is MW.
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#powerMW
          status:
            type:
            - string
            - 'null'
            description: Source status text, copied without normalization.
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet/
            x-jsonld-type: '@vocab'
          type_inst:
            type:
            - string
            - 'null'
            description: Installation type copied from an explicit plant:type tag.
            x-jsonld-id: https://schema.org/additionalType
          year:
            type:
            - string
            - 'null'
            description: Source year copied from an explicit start_date tag; its source
              meaning is retained in tags.
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#year
          updateyear:
            type:
            - string
            - 'null'
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#updateYear
          dist_coast:
            type:
            - number
            - 'null'
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#distanceToCoast
          notes:
            type:
            - string
            - 'null'
            x-jsonld-id: http://purl.org/dc/terms/description
          name:
            type:
            - string
            - 'null'
            description: Name copied from the OSM name tag, falling back to seamark:name.
          area_sqkm:
            type:
            - number
            - 'null'
          osm_type:
            type: string
            enum:
            - node
            - way
            - relation
          osm_id:
            type: integer
            minimum: 0
          tags:
            type: object
            description: Unmodified source OSM tag dictionary, kept in addition to
              normalized EMODnet properties.
            additionalProperties:
              type: string
          members:
            type: array
            description: Original relation member references and roles, preserved
              in source order.
            items:
              type: string
          category_of_offshore_production_area:
            const: 1
            description: IHO enumerated code 1 (Wind Farm), populated only where OSM
              explicitly tags a wind-farm production area.
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#categoryOfOffshoreProductionArea
            x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
          iho_feature_role:
            type: string
            format: uri
            enum:
            - https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#WindTurbine
            - https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#OffshoreProductionArea
            description: Local concept aligned to the cited IHO feature label; raw
              OSM tags remain the source evidence.
            x-jsonld-id: https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#featureRole
            x-jsonld-type: '@id'
        additionalProperties: true
        x-jsonld-id: https://purl.org/geojson/vocab#properties
    additionalProperties: true
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
  Point: https://purl.org/geojson/vocab#Point
  Polygon: https://purl.org/geojson/vocab#Polygon
  MultiPolygon: https://purl.org/geojson/vocab#MultiPolygon
  MapResponse: https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#MapResponse
  Bounds: https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#Bounds
  Element: https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#Element
  TagSet: https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#TagSet
  RelationMember: https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#RelationMember
  version: https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#apiVersion
  generator: https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#generator
  copyright: http://purl.org/dc/terms/rights
  attribution:
    x-jsonld-id: http://creativecommons.org/ns#attributionURL
    x-jsonld-type: '@id'
  license:
    x-jsonld-id: http://purl.org/dc/terms/license
    x-jsonld-type: '@id'
  bounds:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#bounds
    x-jsonld-context:
      minlat:
        '@id': https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#minlat
        '@type': http://www.w3.org/2001/XMLSchema#decimal
      minlon:
        '@id': https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#minlon
        '@type': http://www.w3.org/2001/XMLSchema#decimal
      maxlat:
        '@id': https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#maxlat
        '@type': http://www.w3.org/2001/XMLSchema#decimal
      maxlon:
        '@id': https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#maxlon
        '@type': http://www.w3.org/2001/XMLSchema#decimal
  elements:
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#element
    x-jsonld-container: '@set'
    x-jsonld-context:
      type: '@type'
      node: https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#Node
      way: https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#Way
      relation: https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#Relation
      id:
        '@id': https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#elementIdentifier
        '@type': http://www.w3.org/2001/XMLSchema#integer
      timestamp:
        '@id': http://purl.org/dc/terms/modified
        '@type': http://www.w3.org/2001/XMLSchema#dateTime
      version:
        '@id': https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#elementVersion
        '@type': http://www.w3.org/2001/XMLSchema#integer
      changeset:
        '@id': https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#changeset
        '@type': http://www.w3.org/2001/XMLSchema#integer
      user: https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#user
      uid:
        '@id': https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#uid
        '@type': http://www.w3.org/2001/XMLSchema#integer
      tags:
        '@id': https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#tagSet
        '@context':
          '@version': 1.1
          osmkey: 'https://www.openstreetmap.org/wiki/Key:'
          '@vocab': 'https://www.openstreetmap.org/wiki/Key:'
          ISO3166-1: 'https://www.openstreetmap.org/wiki/Key:ISO3166-1:'
          TMC: 'https://www.openstreetmap.org/wiki/Key:TMC:'
          alt_name: 'https://www.openstreetmap.org/wiki/Key:alt_name:'
          construction: 'https://www.openstreetmap.org/wiki/Key:construction:'
          contact: 'https://www.openstreetmap.org/wiki/Key:contact:'
          description: 'https://www.openstreetmap.org/wiki/Key:description:'
          generator: 'https://www.openstreetmap.org/wiki/Key:generator:'
          height: 'https://www.openstreetmap.org/wiki/Key:height:'
          long_name: 'https://www.openstreetmap.org/wiki/Key:long_name:'
          name: 'https://www.openstreetmap.org/wiki/Key:name:'
          note: 'https://www.openstreetmap.org/wiki/Key:note:'
          official_name: 'https://www.openstreetmap.org/wiki/Key:official_name:'
          old_name: 'https://www.openstreetmap.org/wiki/Key:old_name:'
          plant: 'https://www.openstreetmap.org/wiki/Key:plant:'
          population: 'https://www.openstreetmap.org/wiki/Key:population:'
          rotor: 'https://www.openstreetmap.org/wiki/Key:rotor:'
          seamark: 'https://www.openstreetmap.org/wiki/Key:seamark:'
          short_name: 'https://www.openstreetmap.org/wiki/Key:short_name:'
          source: 'https://www.openstreetmap.org/wiki/Key:source:'
          teryt: 'https://www.openstreetmap.org/wiki/Key:teryt:'
          wreck: 'https://www.openstreetmap.org/wiki/Key:wreck:'
      lat:
        '@id': http://www.w3.org/2003/01/geo/wgs84_pos#lat
        '@type': http://www.w3.org/2001/XMLSchema#decimal
      lon:
        '@id': http://www.w3.org/2003/01/geo/wgs84_pos#long
        '@type': http://www.w3.org/2001/XMLSchema#decimal
      nodes:
        '@id': https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#nodeReference
        '@container': '@list'
        '@type': http://www.w3.org/2001/XMLSchema#integer
      members:
        '@id': https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#relationMember
        '@container': '@list'
        '@context':
          type:
            '@id': https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#memberType
            '@type': '@vocab'
          ref:
            '@id': https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#memberReference
            '@type': http://www.w3.org/2001/XMLSchema#integer
          role: https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#memberRole
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  schema: https://schema.org/
  seadots: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#
  dcterms: http://purl.org/dc/terms/
  osmdata: https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#
  cc: http://creativecommons.org/ns#
  xsd: http://www.w3.org/2001/XMLSchema#
  geo: http://www.w3.org/2003/01/geo/wgs84_pos#
  iho: https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#
  seadots-emodnet: https://w3id.org/ogc/hosted/seadots/emodnet/
  inspire-cofv: http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/
  em: https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#
x-bblocks-metadata:
  itemIdentifier: ogc.hosted.seadots.windfarms.emodnet-windfarm-osm
  register: https://ogcincubator.github.io/bblocks-seadots/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-27'

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/emodnet-windfarm-osm/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/emodnet-windfarm-osm/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/emodnet/",
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "features": {
      "@container": "@set",
      "@id": "geojson:features",
      "@context": {
        "@vocab": "https://w3id.org/ogc/hosted/seadots/emodnet/"
      }
    },
    "type": "@type",
    "id": "@id",
    "properties": {
      "@context": {
        "country": {
          "@id": "schema:addressCountry",
          "@type": "@vocab"
        },
        "n_turbines": "seadots:nTurbines",
        "power_mw": "seadots:powerMW",
        "status": {
          "@id": "https://w3id.org/ogc/hosted/seadots/emodnet/",
          "@type": "@vocab"
        },
        "type_inst": "schema:additionalType",
        "updateyear": "seadots:updateYear",
        "year": "seadots:year",
        "dist_coast": "seadots:distanceToCoast",
        "notes": "dct:description",
        "category_of_offshore_production_area": {
          "@id": "iho:categoryOfOffshoreProductionArea",
          "@type": "xsd:integer"
        },
        "iho_feature_role": {
          "@id": "iho:featureRole",
          "@type": "@id"
        }
      },
      "@id": "geojson:properties"
    },
    "geometry": "geojson:geometry",
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "links": {
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "coordinates": {
      "@id": "geojson:coordinates",
      "@container": "@list"
    },
    "MapResponse": "osmdata:MapResponse",
    "Bounds": "osmdata:Bounds",
    "Element": "osmdata:Element",
    "TagSet": "osmdata:TagSet",
    "RelationMember": "osmdata:RelationMember",
    "version": "osmdata:apiVersion",
    "generator": "osmdata:generator",
    "copyright": "dct:rights",
    "attribution": {
      "@id": "cc:attributionURL",
      "@type": "@id"
    },
    "license": {
      "@id": "dct:license",
      "@type": "@id"
    },
    "bounds": {
      "@id": "osmdata:bounds",
      "@context": {
        "minlat": {
          "@id": "osmdata:minlat",
          "@type": "xsd:decimal"
        },
        "minlon": {
          "@id": "osmdata:minlon",
          "@type": "xsd:decimal"
        },
        "maxlat": {
          "@id": "osmdata:maxlat",
          "@type": "xsd:decimal"
        },
        "maxlon": {
          "@id": "osmdata:maxlon",
          "@type": "xsd:decimal"
        }
      }
    },
    "elements": {
      "@id": "osmdata:element",
      "@container": "@set",
      "@context": {
        "node": "osmdata:Node",
        "way": "osmdata:Way",
        "relation": "osmdata:Relation",
        "id": {
          "@id": "osmdata:elementIdentifier",
          "@type": "xsd:integer"
        },
        "timestamp": {
          "@id": "dct:modified",
          "@type": "xsd:dateTime"
        },
        "version": {
          "@id": "osmdata:elementVersion",
          "@type": "xsd:integer"
        },
        "changeset": {
          "@id": "osmdata:changeset",
          "@type": "xsd:integer"
        },
        "user": "osmdata:user",
        "uid": {
          "@id": "osmdata:uid",
          "@type": "xsd:integer"
        },
        "tags": {
          "@id": "osmdata:tagSet",
          "@context": {
            "@version": 1.1,
            "osmkey": "https://www.openstreetmap.org/wiki/Key:",
            "@vocab": "https://www.openstreetmap.org/wiki/Key:",
            "ISO3166-1": "https://www.openstreetmap.org/wiki/Key:ISO3166-1:",
            "TMC": "https://www.openstreetmap.org/wiki/Key:TMC:",
            "alt_name": "https://www.openstreetmap.org/wiki/Key:alt_name:",
            "construction": "https://www.openstreetmap.org/wiki/Key:construction:",
            "contact": "https://www.openstreetmap.org/wiki/Key:contact:",
            "description": "https://www.openstreetmap.org/wiki/Key:description:",
            "generator": "https://www.openstreetmap.org/wiki/Key:generator:",
            "height": "https://www.openstreetmap.org/wiki/Key:height:",
            "long_name": "https://www.openstreetmap.org/wiki/Key:long_name:",
            "name": "https://www.openstreetmap.org/wiki/Key:name:",
            "note": "https://www.openstreetmap.org/wiki/Key:note:",
            "official_name": "https://www.openstreetmap.org/wiki/Key:official_name:",
            "old_name": "https://www.openstreetmap.org/wiki/Key:old_name:",
            "plant": "https://www.openstreetmap.org/wiki/Key:plant:",
            "population": "https://www.openstreetmap.org/wiki/Key:population:",
            "rotor": "https://www.openstreetmap.org/wiki/Key:rotor:",
            "seamark": "https://www.openstreetmap.org/wiki/Key:seamark:",
            "short_name": "https://www.openstreetmap.org/wiki/Key:short_name:",
            "source": "https://www.openstreetmap.org/wiki/Key:source:",
            "teryt": "https://www.openstreetmap.org/wiki/Key:teryt:",
            "wreck": "https://www.openstreetmap.org/wiki/Key:wreck:"
          }
        },
        "lat": {
          "@id": "geo:lat",
          "@type": "xsd:decimal"
        },
        "lon": {
          "@id": "geo:long",
          "@type": "xsd:decimal"
        },
        "nodes": {
          "@id": "osmdata:nodeReference",
          "@container": "@list",
          "@type": "xsd:integer"
        },
        "members": {
          "@id": "osmdata:relationMember",
          "@container": "@list",
          "@context": {
            "type": {
              "@id": "osmdata:memberType",
              "@type": "@vocab"
            },
            "ref": {
              "@id": "osmdata:memberReference",
              "@type": "xsd:integer"
            },
            "role": "osmdata:memberRole"
          }
        }
      }
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "schema": "https://schema.org/",
    "seadots": "https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#",
    "dcterms": "http://purl.org/dc/terms/",
    "seadots-emodnet": "https://w3id.org/ogc/hosted/seadots/emodnet/",
    "inspire-cofv": "http://inspire.ec.europa.eu/codelist/ConditionOfFacilityValue/",
    "osmdata": "https://w3id.org/ogc/hosted/seadots/osm-offshore-wind-source#",
    "cc": "http://creativecommons.org/ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "iho": "https://w3id.org/ogc/hosted/seadots/emodnet-windfarm-osm#",
    "em": "https://w3id.org/ogc/hosted/seadots/emodnet-compliant-windfarm#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/windfarms/emodnet-windfarm-osm/context.jsonld)

## Sources

* [EMODnet-compliant windfarm Building Block](https://w3id.org/ogc/hosted/seadots/windfarms/windfarm-designated-area-emodnet)
* [OpenStreetMap copyright and ODbL attribution](https://www.openstreetmap.org/copyright)
* [OpenStreetMap API map endpoint used for the source snapshot](https://api.openstreetmap.org/api/0.6/map)
* [IHO S-100 Registry: Category of Offshore Production Area](https://registry.iho.int/fdd/view3.do?idx=42&type=3)
* [IHO S-101 Electronic Navigational Chart Product Specification](https://metanorma.github.io/iho-s-101/documents/2.0.0/annex-a/document.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/windfarms/emodnet-windfarm-osm`

