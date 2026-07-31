
# SeaDOTs Catalog Data Multidimensional (Schema)

`ogc.hosted.seadots.catalog-data-multidim` *v0.1*

OGC API Records profile for catalog records that describe multidimensional gridded or array-oriented data products, reusing the ILIAD STAC/DCAT multidimensional data profile.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# SeaDOTs Catalog Data Multidimensional

OGC API Records profile for catalog records that describe multidimensional gridded or array-oriented data products such as NetCDF, Zarr, or CF-convention datasets.

The profile composes `ogc.hosted.seadots.catalog-data` for shared catalog data semantics and the imported `ogc.hosted.iliad.api.features.stac_multidim_data` building block for multidimensional metadata. It intentionally avoids copying inherited properties, schemas, or JSON-LD context. Local schema constraints only require a profile link that advertises the imported multidimensional data profile.

## Composition

| Concern | Source |
| --- | --- |
| Shared STAC/CF/provenance data record | `bblocks://ogc.hosted.seadots.catalog-data` |
| Multidimensional STAC/DCAT record structure | `bblocks://ogc.hosted.iliad.api.features.stac_multidim_data` |
| SeaDOTs profile advertisement | Local `schema.yaml` profile-link constraint |
| JSON-LD terms | Imported catalog-data and ILIAD multidimensional contexts |

## Usage Notes

Use this block when a SeaDOTs catalog record points to a multidimensional data asset rather than a scalar observation, workflow, or execution record. The actual multidimensional metadata terms remain governed by the imported ILIAD profile so that this block stays a thin OGC Record profile.

## Generator

The `scripts/build_catalog_data_multidim_record.py` helper generates a STAC/OGC Record from a NetCDF file header without loading data arrays. It prefers Python metadata backends (`netCDF4`, `h5netcdf`) when installed, then falls back to CLI metadata inspection (`h5dump`, `ncdump -h`) with a timeout.

Example:

```bash
python3 _sources/catalog-data-multidim/scripts/build_catalog_data_multidim_record.py \
  --href https://example.org/data/example.nc \
  --license https://spdx.org/licenses/CC-BY-4.0.html \
  -o /tmp/catalog-data-multidim-record.json \
  /path/to/example.nc
```

## Examples

### SeaDOTs Catalog Data Multidimensional
#### json
```json
{
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/dataset/north-sea-temperature-forecast",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/datacube/v2.2.0/schema.json",
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          2.0,
          56.0
        ],
        [
          9.0,
          56.0
        ],
        [
          9.0,
          61.0
        ],
        [
          2.0,
          61.0
        ],
        [
          2.0,
          56.0
        ]
      ]
    ]
  },
  "bbox": [
    2.0,
    56.0,
    9.0,
    61.0
  ],
  "properties": {
    "title": "North Sea temperature forecast cube",
    "description": "Synthetic SeaDOTs catalog record for a multidimensional sea-water temperature data cube.",
    "datetime": "2026-06-10T00:00:00Z",
    "start_datetime": "2026-06-10T00:00:00Z",
    "end_datetime": "2026-06-11T00:00:00Z",
    "keywords": [
      "SeaDOTs",
      "multidimensional",
      "NetCDF",
      "CF",
      "temperature"
    ],
    "license": "CC-BY-4.0",
    "formats": [
      {
        "name": "NetCDF",
        "mediaType": "application/x-netcdf"
      }
    ],
    "variables": {
      "sea_water_temperature": {
        "title": "Sea water temperature",
        "description": "Sea water temperature forecast variable.",
        "unit": "K"
      }
    }
  },
  "assets": {
    "netcdf": {
      "href": "https://example.org/seadots/north-sea-temperature-forecast.nc",
      "type": "application/x-netcdf",
      "title": "NetCDF data cube",
      "cf:parameter": [
        {
          "name": "sea_water_temperature",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "K",
          "description": "Sea water temperature forecast variable."
        }
      ],
      "roles": [
        "data"
      ]
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data bblock"
    },
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data-multidim",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data Multidimensional bblock"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.iliad.api.features.stac_multidim_data",
      "type": "application/schema+json",
      "title": "ILIAD STAC/DCAT multidimensional data profile"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data-multidim/context.jsonld",
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/dataset/north-sea-temperature-forecast",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/datacube/v2.2.0/schema.json",
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          2.0,
          56.0
        ],
        [
          9.0,
          56.0
        ],
        [
          9.0,
          61.0
        ],
        [
          2.0,
          61.0
        ],
        [
          2.0,
          56.0
        ]
      ]
    ]
  },
  "bbox": [
    2.0,
    56.0,
    9.0,
    61.0
  ],
  "properties": {
    "title": "North Sea temperature forecast cube",
    "description": "Synthetic SeaDOTs catalog record for a multidimensional sea-water temperature data cube.",
    "datetime": "2026-06-10T00:00:00Z",
    "start_datetime": "2026-06-10T00:00:00Z",
    "end_datetime": "2026-06-11T00:00:00Z",
    "keywords": [
      "SeaDOTs",
      "multidimensional",
      "NetCDF",
      "CF",
      "temperature"
    ],
    "license": "CC-BY-4.0",
    "formats": [
      {
        "name": "NetCDF",
        "mediaType": "application/x-netcdf"
      }
    ],
    "variables": {
      "sea_water_temperature": {
        "title": "Sea water temperature",
        "description": "Sea water temperature forecast variable.",
        "unit": "K"
      }
    }
  },
  "assets": {
    "netcdf": {
      "href": "https://example.org/seadots/north-sea-temperature-forecast.nc",
      "type": "application/x-netcdf",
      "title": "NetCDF data cube",
      "cf:parameter": [
        {
          "name": "sea_water_temperature",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "K",
          "description": "Sea water temperature forecast variable."
        }
      ],
      "roles": [
        "data"
      ]
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data bblock"
    },
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data-multidim",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data Multidimensional bblock"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.iliad.api.features.stac_multidim_data",
      "type": "application/schema+json",
      "title": "ILIAD STAC/DCAT multidimensional data profile"
    }
  ]
}
```

#### ttl
```ttl
@prefix cf: <https://stac-extensions.github.io/cf/v0.2.0/schema.json#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix ns2: <https://w3id.org/ogc/stac/assets/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/ogc/hosted/seadots/catalog/dataset/north-sea-temperature-forecast> a geojson:Feature ;
    dcterms:date "2026-06-10T00:00:00+00:00"^^xsd:dateTime ;
    dcterms:description "Synthetic SeaDOTs catalog record for a multidimensional sea-water temperature data cube." ;
    dcterms:license "CC-BY-4.0" ;
    dcterms:subject "CF",
        "NetCDF",
        "SeaDOTs",
        "multidimensional",
        "temperature" ;
    dcterms:title "North Sea temperature forecast cube" ;
    rdfs:seeAlso [ rdfs:label "SeaDOTs Catalog Data bblock" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-data> ],
        [ rdfs:label "SeaDOTs Catalog Data Multidimensional bblock" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-data-multidim> ],
        [ rdfs:label "ILIAD STAC/DCAT multidimensional data profile" ;
            dcterms:type "application/schema+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/profile> ;
            oa:hasTarget <bblocks://ogc.hosted.iliad.api.features.stac_multidim_data> ] ;
    geojson:bbox ( 2e+00 5.6e+01 9e+00 6.1e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 2e+00 5.6e+01 ) ( 9e+00 5.6e+01 ) ( 9e+00 6.1e+01 ) ( 2e+00 6.1e+01 ) ( 2e+00 5.6e+01 ) ) ) ] ;
    seadots:itemType "record" ;
    stac:end_datetime "2026-06-11T00:00:00+00:00"^^xsd:dateTime ;
    stac:hasAsset [ ns2:netcdf [ dcterms:format "application/x-netcdf" ;
                    dcterms:title "NetCDF data cube" ;
                    oa:hasTarget <https://example.org/seadots/north-sea-temperature-forecast.nc> ;
                    cf:parameter [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
                            dcterms:description "Sea water temperature forecast variable." ;
                            qudt:unit <http://qudt.org/vocab/unit/K> ;
                            foaf:name "sea_water_temperature"^^rdfs:Literal ] ;
                    stac:roles "data" ] ] ;
    stac:hasExtension "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
        "https://stac-extensions.github.io/datacube/v2.2.0/schema.json",
        "https://stac-extensions.github.io/prov/v1.0.0/schema.json" ;
    stac:start_datetime "2026-06-10T00:00:00+00:00"^^xsd:dateTime ;
    stac:version "1.0.0" ;
    rec:format [ dcterms:mediaType "application/x-netcdf" ;
            rec:name "NetCDF" ] ;
    rec:hasVariable <http://example.com/variables/sea_water_temperature> .

<http://example.com/variables/sea_water_temperature> dcterms:description "Sea water temperature forecast variable." ;
    dcterms:title "Sea water temperature" ;
    qudt:unit <http://qudt.org/vocab/unit/K> .


```


### German Case SCHISM NetCDF Catalog Data Multidimensional
#### json
```json
{
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/dataset/german-case-schism-wwm-3dinterp-10",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/datacube/v2.2.0/schema.json",
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "geometry": null,
  "properties": {
    "title": "Dummy data file for OGC from the German Use Case",
    "description": "Header-derived SeaDOTs catalog record for the German Use Case SCHISM NetCDF multidimensional dataset.",
    "datetime": "2026-06-11T09:23:33Z",
    "keywords": [
      "SeaDOTs",
      "multidimensional",
      "NetCDF",
      "CF"
    ],
    "license": "CC-BY-4.0",
    "role": "data",
    "convention": "CF-1.8",
    "formats": [
      {
        "name": "NetCDF",
        "mediaType": "application/x-netcdf"
      }
    ],
    "variables": {
      "v": {
        "title": "Northward Surface Sea Water Velocity (V)",
        "description": "horizontalVelY",
        "unit": "m/s"
      },
      "u": {
        "title": "Eastward Surface Sea Water Velocity (U)",
        "description": "horizontalVelX",
        "unit": "m/s"
      },
      "sst": {
        "title": "Sea Surface Temperature (SST)",
        "description": "temperature",
        "unit": "degC"
      },
      "sss": {
        "title": "Sea Water Salinity (SSS)",
        "description": "salinity",
        "unit": "0.001"
      },
      "oxy": {
        "title": "oxygen concentration in the water",
        "description": "ECO_oxy",
        "unit": "degree"
      },
      "nmus": {
        "title": "number of mussels per qubic meter",
        "description": "ECO_nmus",
        "unit": "m*1e-3"
      },
      "hanmus": {
        "title": "biomass of harvested mussels N",
        "description": "ECO_hanmus",
        "unit": "mol-N/m3"
      },
      "hacmus": {
        "title": "biomass of harvested mussels C",
        "description": "ECO_hacmus",
        "unit": "mol-C/m3"
      },
      "chl": {
        "title": "chlorophyll mass concentration",
        "description": "chlorophyll",
        "unit": "s"
      },
      "SIO4": {
        "title": "silicate in the water",
        "description": "ECO_sil",
        "unit": "s"
      },
      "PO4": {
        "title": "phospate in the water",
        "description": "ECO_pho",
        "unit": "s"
      },
      "NO3": {
        "title": "nitrat in the water",
        "description": "ECO_no3",
        "unit": "m"
      }
    },
    "cf:parameter": [
      {
        "name": "surface_northward_sea_water_velocity",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "m/s",
        "description": "Northward Surface Sea Water Velocity (V)"
      },
      {
        "name": "surface_eastward_sea_water_velocity",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "m/s",
        "description": "Eastward Surface Sea Water Velocity (U)"
      },
      {
        "name": "sea_water_temperature",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "degC",
        "description": "Sea Surface Temperature (SST)"
      },
      {
        "name": "sea_water_salinity",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "0.001",
        "description": "Sea Water Salinity (SSS)"
      },
      {
        "name": "concentration of oxygen in sea_water",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "degree",
        "description": "oxygen concentration in the water"
      },
      {
        "name": "number of mussels per qubic meter",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "m*1e-3",
        "description": "number of mussels per qubic meter"
      },
      {
        "name": "biomass of harvested mussels N",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "mol-N/m3",
        "description": "biomass of harvested mussels N"
      },
      {
        "name": "biomass of harvested mussels C",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "mol-C/m3",
        "description": "biomass of harvested mussels C"
      },
      {
        "name": "total mass concentration of chlorophyll in sea_water",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "s",
        "description": "chlorophyll mass concentration"
      },
      {
        "name": "concentration of sio4 in sea_water",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "s",
        "description": "silicate in the water"
      },
      {
        "name": "concentration of po4 in sea_water",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "s",
        "description": "phospate in the water"
      },
      {
        "name": "concentration of no3 in sea_water",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "m",
        "description": "nitrat in the water"
      }
    ]
  },
  "assets": {
    "netcdf": {
      "href": "https://example.org/seadots/german-case/schism-wwm_3Dinterp_10.nc",
      "type": "application/x-netcdf",
      "title": "NetCDF data cube",
      "roles": [
        "data"
      ],
      "cf:parameter": [
        {
          "name": "surface_northward_sea_water_velocity",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "m/s",
          "description": "Northward Surface Sea Water Velocity (V)"
        },
        {
          "name": "surface_eastward_sea_water_velocity",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "m/s",
          "description": "Eastward Surface Sea Water Velocity (U)"
        },
        {
          "name": "sea_water_temperature",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "degC",
          "description": "Sea Surface Temperature (SST)"
        },
        {
          "name": "sea_water_salinity",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "0.001",
          "description": "Sea Water Salinity (SSS)"
        },
        {
          "name": "concentration of oxygen in sea_water",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "degree",
          "description": "oxygen concentration in the water"
        },
        {
          "name": "number of mussels per qubic meter",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "m*1e-3",
          "description": "number of mussels per qubic meter"
        },
        {
          "name": "biomass of harvested mussels N",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "mol-N/m3",
          "description": "biomass of harvested mussels N"
        },
        {
          "name": "biomass of harvested mussels C",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "mol-C/m3",
          "description": "biomass of harvested mussels C"
        },
        {
          "name": "total mass concentration of chlorophyll in sea_water",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "s",
          "description": "chlorophyll mass concentration"
        },
        {
          "name": "concentration of sio4 in sea_water",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "s",
          "description": "silicate in the water"
        },
        {
          "name": "concentration of po4 in sea_water",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "s",
          "description": "phospate in the water"
        },
        {
          "name": "concentration of no3 in sea_water",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "m",
          "description": "nitrat in the water"
        }
      ]
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data bblock"
    },
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data-multidim",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data Multidimensional bblock"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.iliad.api.features.stac_multidim_data",
      "type": "application/schema+json",
      "title": "ILIAD STAC/DCAT multidimensional data profile"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data-multidim/context.jsonld",
  "id": "https://w3id.org/ogc/hosted/seadots/catalog/dataset/german-case-schism-wwm-3dinterp-10",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/datacube/v2.2.0/schema.json",
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "geometry": null,
  "properties": {
    "title": "Dummy data file for OGC from the German Use Case",
    "description": "Header-derived SeaDOTs catalog record for the German Use Case SCHISM NetCDF multidimensional dataset.",
    "datetime": "2026-06-11T09:23:33Z",
    "keywords": [
      "SeaDOTs",
      "multidimensional",
      "NetCDF",
      "CF"
    ],
    "license": "CC-BY-4.0",
    "role": "data",
    "convention": "CF-1.8",
    "formats": [
      {
        "name": "NetCDF",
        "mediaType": "application/x-netcdf"
      }
    ],
    "variables": {
      "v": {
        "title": "Northward Surface Sea Water Velocity (V)",
        "description": "horizontalVelY",
        "unit": "m/s"
      },
      "u": {
        "title": "Eastward Surface Sea Water Velocity (U)",
        "description": "horizontalVelX",
        "unit": "m/s"
      },
      "sst": {
        "title": "Sea Surface Temperature (SST)",
        "description": "temperature",
        "unit": "degC"
      },
      "sss": {
        "title": "Sea Water Salinity (SSS)",
        "description": "salinity",
        "unit": "0.001"
      },
      "oxy": {
        "title": "oxygen concentration in the water",
        "description": "ECO_oxy",
        "unit": "degree"
      },
      "nmus": {
        "title": "number of mussels per qubic meter",
        "description": "ECO_nmus",
        "unit": "m*1e-3"
      },
      "hanmus": {
        "title": "biomass of harvested mussels N",
        "description": "ECO_hanmus",
        "unit": "mol-N/m3"
      },
      "hacmus": {
        "title": "biomass of harvested mussels C",
        "description": "ECO_hacmus",
        "unit": "mol-C/m3"
      },
      "chl": {
        "title": "chlorophyll mass concentration",
        "description": "chlorophyll",
        "unit": "s"
      },
      "SIO4": {
        "title": "silicate in the water",
        "description": "ECO_sil",
        "unit": "s"
      },
      "PO4": {
        "title": "phospate in the water",
        "description": "ECO_pho",
        "unit": "s"
      },
      "NO3": {
        "title": "nitrat in the water",
        "description": "ECO_no3",
        "unit": "m"
      }
    },
    "cf:parameter": [
      {
        "name": "surface_northward_sea_water_velocity",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "m/s",
        "description": "Northward Surface Sea Water Velocity (V)"
      },
      {
        "name": "surface_eastward_sea_water_velocity",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "m/s",
        "description": "Eastward Surface Sea Water Velocity (U)"
      },
      {
        "name": "sea_water_temperature",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "degC",
        "description": "Sea Surface Temperature (SST)"
      },
      {
        "name": "sea_water_salinity",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "0.001",
        "description": "Sea Water Salinity (SSS)"
      },
      {
        "name": "concentration of oxygen in sea_water",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "degree",
        "description": "oxygen concentration in the water"
      },
      {
        "name": "number of mussels per qubic meter",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "m*1e-3",
        "description": "number of mussels per qubic meter"
      },
      {
        "name": "biomass of harvested mussels N",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "mol-N/m3",
        "description": "biomass of harvested mussels N"
      },
      {
        "name": "biomass of harvested mussels C",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "mol-C/m3",
        "description": "biomass of harvested mussels C"
      },
      {
        "name": "total mass concentration of chlorophyll in sea_water",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "s",
        "description": "chlorophyll mass concentration"
      },
      {
        "name": "concentration of sio4 in sea_water",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "s",
        "description": "silicate in the water"
      },
      {
        "name": "concentration of po4 in sea_water",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "s",
        "description": "phospate in the water"
      },
      {
        "name": "concentration of no3 in sea_water",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "m",
        "description": "nitrat in the water"
      }
    ]
  },
  "assets": {
    "netcdf": {
      "href": "https://example.org/seadots/german-case/schism-wwm_3Dinterp_10.nc",
      "type": "application/x-netcdf",
      "title": "NetCDF data cube",
      "roles": [
        "data"
      ],
      "cf:parameter": [
        {
          "name": "surface_northward_sea_water_velocity",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "m/s",
          "description": "Northward Surface Sea Water Velocity (V)"
        },
        {
          "name": "surface_eastward_sea_water_velocity",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "m/s",
          "description": "Eastward Surface Sea Water Velocity (U)"
        },
        {
          "name": "sea_water_temperature",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "degC",
          "description": "Sea Surface Temperature (SST)"
        },
        {
          "name": "sea_water_salinity",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "0.001",
          "description": "Sea Water Salinity (SSS)"
        },
        {
          "name": "concentration of oxygen in sea_water",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "degree",
          "description": "oxygen concentration in the water"
        },
        {
          "name": "number of mussels per qubic meter",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "m*1e-3",
          "description": "number of mussels per qubic meter"
        },
        {
          "name": "biomass of harvested mussels N",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "mol-N/m3",
          "description": "biomass of harvested mussels N"
        },
        {
          "name": "biomass of harvested mussels C",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "mol-C/m3",
          "description": "biomass of harvested mussels C"
        },
        {
          "name": "total mass concentration of chlorophyll in sea_water",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "s",
          "description": "chlorophyll mass concentration"
        },
        {
          "name": "concentration of sio4 in sea_water",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "s",
          "description": "silicate in the water"
        },
        {
          "name": "concentration of po4 in sea_water",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "s",
          "description": "phospate in the water"
        },
        {
          "name": "concentration of no3 in sea_water",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "m",
          "description": "nitrat in the water"
        }
      ]
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data bblock"
    },
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data-multidim",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data Multidimensional bblock"
    },
    {
      "rel": "profile",
      "href": "bblocks://ogc.hosted.iliad.api.features.stac_multidim_data",
      "type": "application/schema+json",
      "title": "ILIAD STAC/DCAT multidimensional data profile"
    }
  ]
}
```

#### ttl
```ttl
@prefix cf: <https://stac-extensions.github.io/cf/v0.2.0/schema.json#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <https://w3id.org/ogc/stac/assets/> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rec: <https://www.opengis.net/def/ogc-api/records/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/ogc/hosted/seadots/catalog/dataset/german-case-schism-wwm-3dinterp-10> a geojson:Feature ;
    dcterms:date "2026-06-11T09:23:33+00:00"^^xsd:dateTime ;
    dcterms:description "Header-derived SeaDOTs catalog record for the German Use Case SCHISM NetCDF multidimensional dataset." ;
    dcterms:license "CC-BY-4.0" ;
    dcterms:subject "CF",
        "NetCDF",
        "SeaDOTs",
        "multidimensional" ;
    dcterms:title "Dummy data file for OGC from the German Use Case" ;
    rdfs:seeAlso [ rdfs:label "SeaDOTs Catalog Data bblock" ;
            dcterms:type "application/schema+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-data> ],
        [ rdfs:label "SeaDOTs Catalog Data Multidimensional bblock" ;
            dcterms:type "application/schema+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-data-multidim> ],
        [ rdfs:label "ILIAD STAC/DCAT multidimensional data profile" ;
            dcterms:type "application/schema+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/profile> ;
            oa:hasTarget <bblocks://ogc.hosted.iliad.api.features.stac_multidim_data> ] ;
    cf:parameter [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "biomass of harvested mussels C" ;
            qudt:unit <http://qudt.org/vocab/unit/mol-C/m3> ;
            foaf:name "biomass of harvested mussels C"^^rdfs:Literal ],
        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "chlorophyll mass concentration" ;
            qudt:unit <http://qudt.org/vocab/unit/s> ;
            foaf:name "total mass concentration of chlorophyll in sea_water"^^rdfs:Literal ],
        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "biomass of harvested mussels N" ;
            qudt:unit <http://qudt.org/vocab/unit/mol-N/m3> ;
            foaf:name "biomass of harvested mussels N"^^rdfs:Literal ],
        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "Sea Surface Temperature (SST)" ;
            qudt:unit <http://qudt.org/vocab/unit/degC> ;
            foaf:name "sea_water_temperature"^^rdfs:Literal ],
        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "silicate in the water" ;
            qudt:unit <http://qudt.org/vocab/unit/s> ;
            foaf:name "concentration of sio4 in sea_water"^^rdfs:Literal ],
        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "Eastward Surface Sea Water Velocity (U)" ;
            qudt:unit <http://qudt.org/vocab/unit/m/s> ;
            foaf:name "surface_eastward_sea_water_velocity"^^rdfs:Literal ],
        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "Sea Water Salinity (SSS)" ;
            qudt:unit <http://qudt.org/vocab/unit/0.001> ;
            foaf:name "sea_water_salinity"^^rdfs:Literal ],
        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "number of mussels per qubic meter" ;
            qudt:unit <http://qudt.org/vocab/unit/m*1e-3> ;
            foaf:name "number of mussels per qubic meter"^^rdfs:Literal ],
        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "Northward Surface Sea Water Velocity (V)" ;
            qudt:unit <http://qudt.org/vocab/unit/m/s> ;
            foaf:name "surface_northward_sea_water_velocity"^^rdfs:Literal ],
        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "oxygen concentration in the water" ;
            qudt:unit <http://qudt.org/vocab/unit/degree> ;
            foaf:name "concentration of oxygen in sea_water"^^rdfs:Literal ],
        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "phospate in the water" ;
            qudt:unit <http://qudt.org/vocab/unit/s> ;
            foaf:name "concentration of po4 in sea_water"^^rdfs:Literal ],
        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "nitrat in the water" ;
            qudt:unit <http://qudt.org/vocab/unit/m> ;
            foaf:name "concentration of no3 in sea_water"^^rdfs:Literal ] ;
    seadots:itemType "record" ;
    seadots:metadataConvention "CF-1.8" ;
    seadots:role "data" ;
    stac:hasAsset [ ns1:netcdf [ dcterms:format "application/x-netcdf" ;
                    dcterms:title "NetCDF data cube" ;
                    oa:hasTarget <https://example.org/seadots/german-case/schism-wwm_3Dinterp_10.nc> ;
                    cf:parameter [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
                            dcterms:description "Northward Surface Sea Water Velocity (V)" ;
                            qudt:unit <http://qudt.org/vocab/unit/m/s> ;
                            foaf:name "surface_northward_sea_water_velocity"^^rdfs:Literal ],
                        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
                            dcterms:description "number of mussels per qubic meter" ;
                            qudt:unit <http://qudt.org/vocab/unit/m*1e-3> ;
                            foaf:name "number of mussels per qubic meter"^^rdfs:Literal ],
                        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
                            dcterms:description "Eastward Surface Sea Water Velocity (U)" ;
                            qudt:unit <http://qudt.org/vocab/unit/m/s> ;
                            foaf:name "surface_eastward_sea_water_velocity"^^rdfs:Literal ],
                        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
                            dcterms:description "biomass of harvested mussels N" ;
                            qudt:unit <http://qudt.org/vocab/unit/mol-N/m3> ;
                            foaf:name "biomass of harvested mussels N"^^rdfs:Literal ],
                        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
                            dcterms:description "chlorophyll mass concentration" ;
                            qudt:unit <http://qudt.org/vocab/unit/s> ;
                            foaf:name "total mass concentration of chlorophyll in sea_water"^^rdfs:Literal ],
                        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
                            dcterms:description "biomass of harvested mussels C" ;
                            qudt:unit <http://qudt.org/vocab/unit/mol-C/m3> ;
                            foaf:name "biomass of harvested mussels C"^^rdfs:Literal ],
                        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
                            dcterms:description "nitrat in the water" ;
                            qudt:unit <http://qudt.org/vocab/unit/m> ;
                            foaf:name "concentration of no3 in sea_water"^^rdfs:Literal ],
                        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
                            dcterms:description "silicate in the water" ;
                            qudt:unit <http://qudt.org/vocab/unit/s> ;
                            foaf:name "concentration of sio4 in sea_water"^^rdfs:Literal ],
                        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
                            dcterms:description "phospate in the water" ;
                            qudt:unit <http://qudt.org/vocab/unit/s> ;
                            foaf:name "concentration of po4 in sea_water"^^rdfs:Literal ],
                        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
                            dcterms:description "Sea Water Salinity (SSS)" ;
                            qudt:unit <http://qudt.org/vocab/unit/0.001> ;
                            foaf:name "sea_water_salinity"^^rdfs:Literal ],
                        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
                            dcterms:description "oxygen concentration in the water" ;
                            qudt:unit <http://qudt.org/vocab/unit/degree> ;
                            foaf:name "concentration of oxygen in sea_water"^^rdfs:Literal ],
                        [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
                            dcterms:description "Sea Surface Temperature (SST)" ;
                            qudt:unit <http://qudt.org/vocab/unit/degC> ;
                            foaf:name "sea_water_temperature"^^rdfs:Literal ] ;
                    stac:roles "data" ] ] ;
    stac:hasExtension "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
        "https://stac-extensions.github.io/datacube/v2.2.0/schema.json",
        "https://stac-extensions.github.io/prov/v1.0.0/schema.json" ;
    stac:version "1.0.0" ;
    rec:format [ dcterms:mediaType "application/x-netcdf" ;
            rec:name "NetCDF" ] ;
    rec:hasVariable <http://example.com/variables/NO3>,
        <http://example.com/variables/PO4>,
        <http://example.com/variables/SIO4>,
        <http://example.com/variables/chl>,
        <http://example.com/variables/hacmus>,
        <http://example.com/variables/hanmus>,
        <http://example.com/variables/nmus>,
        <http://example.com/variables/oxy>,
        <http://example.com/variables/sss>,
        <http://example.com/variables/sst>,
        <http://example.com/variables/u>,
        <http://example.com/variables/v> .

<http://example.com/variables/NO3> dcterms:description "ECO_no3" ;
    dcterms:title "nitrat in the water" ;
    qudt:unit <http://qudt.org/vocab/unit/m> .

<http://example.com/variables/PO4> dcterms:description "ECO_pho" ;
    dcterms:title "phospate in the water" ;
    qudt:unit <http://qudt.org/vocab/unit/s> .

<http://example.com/variables/SIO4> dcterms:description "ECO_sil" ;
    dcterms:title "silicate in the water" ;
    qudt:unit <http://qudt.org/vocab/unit/s> .

<http://example.com/variables/chl> dcterms:description "chlorophyll" ;
    dcterms:title "chlorophyll mass concentration" ;
    qudt:unit <http://qudt.org/vocab/unit/s> .

<http://example.com/variables/hacmus> dcterms:description "ECO_hacmus" ;
    dcterms:title "biomass of harvested mussels C" ;
    qudt:unit <http://qudt.org/vocab/unit/mol-C/m3> .

<http://example.com/variables/hanmus> dcterms:description "ECO_hanmus" ;
    dcterms:title "biomass of harvested mussels N" ;
    qudt:unit <http://qudt.org/vocab/unit/mol-N/m3> .

<http://example.com/variables/nmus> dcterms:description "ECO_nmus" ;
    dcterms:title "number of mussels per qubic meter" ;
    qudt:unit <http://qudt.org/vocab/unit/m*1e-3> .

<http://example.com/variables/oxy> dcterms:description "ECO_oxy" ;
    dcterms:title "oxygen concentration in the water" ;
    qudt:unit <http://qudt.org/vocab/unit/degree> .

<http://example.com/variables/sss> dcterms:description "salinity" ;
    dcterms:title "Sea Water Salinity (SSS)" ;
    qudt:unit <http://qudt.org/vocab/unit/0.001> .

<http://example.com/variables/sst> dcterms:description "temperature" ;
    dcterms:title "Sea Surface Temperature (SST)" ;
    qudt:unit <http://qudt.org/vocab/unit/degC> .

<http://example.com/variables/u> dcterms:description "horizontalVelX" ;
    dcterms:title "Eastward Surface Sea Water Velocity (U)" ;
    qudt:unit <http://qudt.org/vocab/unit/m/s> .

<http://example.com/variables/v> dcterms:description "horizontalVelY" ;
    dcterms:title "Northward Surface Sea Water Velocity (V)" ;
    qudt:unit <http://qudt.org/vocab/unit/m/s> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SeaDOTs Catalog Data Multidimensional
description: 'OGC API Records profile for records describing multidimensional gridded
  or array-oriented data. The structural contract is inherited from the ILIAD STAC/DCAT
  multidimensional data profile; this block only adds the SeaDOTs profile-link constraint.

  '
allOf:
- $ref: https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data/schema.yaml
- $ref: https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/stac_multidim_data/schema.yaml
type: object
required:
- type
- properties
- links
properties:
  type:
    const: Feature
    x-jsonld-id: '@type'
  properties:
    type: object
    required:
    - title
    - description
    additionalProperties: true
    x-jsonld-id: '@nest'
  links:
    type: array
    contains:
      type: object
      required:
      - rel
      - href
      properties:
        rel:
          const: profile
          x-jsonld-id: http://www.iana.org/assignments/relation
          x-jsonld-type: '@id'
          x-jsonld-base: http://www.iana.org/assignments/relation/
        href:
          const: bblocks://ogc.hosted.iliad.api.features.stac_multidim_data
          x-jsonld-type: '@id'
          x-jsonld-id: http://www.w3.org/ns/oa#hasTarget
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
    x-jsonld-extra-terms:
      type: http://purl.org/dc/terms/type
      hreflang: http://purl.org/dc/terms/language
      title: http://www.w3.org/2000/01/rdf-schema#label
      length: http://purl.org/dc/terms/extent
x-jsonld-extra-terms:
  Feature: https://purl.org/geojson/vocab#Feature
  FeatureCollection: https://purl.org/geojson/vocab#FeatureCollection
  GeometryCollection: https://purl.org/geojson/vocab#GeometryCollection
  LineString: https://purl.org/geojson/vocab#LineString
  MultiLineString: https://purl.org/geojson/vocab#MultiLineString
  MultiPoint: https://purl.org/geojson/vocab#MultiPoint
  MultiPolygon: https://purl.org/geojson/vocab#MultiPolygon
  Point: https://purl.org/geojson/vocab#Point
  Polygon: https://purl.org/geojson/vocab#Polygon
  features:
    x-jsonld-container: '@set'
    x-jsonld-id: https://purl.org/geojson/vocab#features
  id: '@id'
  geometry:
    x-jsonld-context:
      coordinates:
        '@container': '@list'
        '@id': https://purl.org/geojson/vocab#coordinates
    x-jsonld-id: https://purl.org/geojson/vocab#geometry
  bbox:
    x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#bbox
  conformsTo:
    x-jsonld-container: '@set'
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
  time: http://purl.org/dc/terms/temporal
  linkTemplates:
    x-jsonld-context:
      rel:
        '@context':
          '@base': http://www.iana.org/assignments/relation/
        '@id': http://www.iana.org/assignments/relation
        '@type': '@id'
      type: http://purl.org/dc/terms/format
      hreflang: http://purl.org/dc/terms/language
      title: http://www.w3.org/2000/01/rdf-schema#label
      length: http://purl.org/dc/terms/extent
      uriTemplate:
        '@type': http://www.w3.org/2001/XMLSchema#string
        '@id': https://www.opengis.net/def/ogc-api/records/uriTemplate
      varBase: https://www.opengis.net/def/ogc-api/records/varBase
      variables:
        '@id': https://www.opengis.net/def/ogc-api/records/hasVariable
        '@container': '@index'
        '@index': http://purl.org/dc/terms/identifier
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/hasLinkTemplate
  created: http://purl.org/dc/terms/created
  updated: http://purl.org/dc/terms/modified
  title:
    x-jsonld-container: '@set'
    x-jsonld-id: http://purl.org/dc/terms/title
  description:
    x-jsonld-container: '@set'
    x-jsonld-id: http://purl.org/dc/terms/description
  keywords:
    x-jsonld-container: '@set'
    x-jsonld-id: http://www.w3.org/ns/dcat#keyword
  language: https://www.opengis.net/def/ogc-api/records/language
  languages:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/languages
    x-jsonld-context:
      code: https://www.opengis.net/def/ogc-api/records/languageCode
      name: http://www.w3.org/2004/02/skos/core#prefLabel
  resourceLanguages:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/resourceLanguages
    x-jsonld-context:
      code: https://www.opengis.net/def/ogc-api/records/languageCode
      name: http://www.w3.org/2004/02/skos/core#prefLabel
  externalIds:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/scopedIdentifier
    x-jsonld-context:
      scheme: https://www.opengis.net/def/ogc-api/records/scheme
      value: https://www.opengis.net/def/ogc-api/records/id
  themes:
    x-jsonld-container: '@set'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/themes
    x-jsonld-context:
      concepts:
        '@id': https://w3id.org/ogc/stac/themes/concepts
        '@context':
          id: https://w3id.org/ogc/stac/themes/id
          url: '@id'
        '@container': '@set'
      scheme: https://w3id.org/ogc/stac/themes/scheme
  formats:
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/format
    x-jsonld-context:
      name: https://www.opengis.net/def/ogc-api/records/name
      mediaType: https://www.opengis.net/def/ogc-api/records/mediaType
    x-jsonld-container: '@set'
    x-jsonld-type: '@id'
  contacts:
    x-jsonld-container: '@set'
    x-jsonld-id: http://www.w3.org/ns/dcat#contactPoint
    x-jsonld-type: '@id'
  license: http://www.w3.org/ns/dcat#license
  accessrights: http://purl.org/dc/terms/accessRights
  variables:
    x-jsonld-container: '@id'
    x-jsonld-id: https://www.opengis.net/def/ogc-api/records/hasVariable
    x-jsonld-context:
      '@base': http://example.com/variables/
      '@vocab': https://www.opengis.net/def/ogc-api/records/
  stac_extensions: https://w3id.org/ogc/stac/core/hasExtension
  assets:
    x-jsonld-context:
      type: http://purl.org/dc/terms/format
      roles:
        '@id': https://w3id.org/ogc/stac/core/roles
        '@container': '@set'
      '@vocab': https://w3id.org/ogc/stac/assets/
    x-jsonld-id: https://w3id.org/ogc/stac/core/hasAsset
    x-jsonld-container: '@set'
  stac_version: https://w3id.org/ogc/stac/core/version
  start_datetime:
    x-jsonld-id: https://w3id.org/ogc/stac/core/start_datetime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  end_datetime:
    x-jsonld-id: https://w3id.org/ogc/stac/core/end_datetime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  providers: https://w3id.org/ogc/stac/core/hasProvider
  media_type: http://purl.org/dc/terms/format
  extent: http://purl.org/dc/terms/extent
  datetime:
    x-jsonld-id: http://purl.org/dc/terms/date
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  concepts:
    x-jsonld-id: https://w3id.org/ogc/stac/themes/concepts
    x-jsonld-container: '@set'
    x-jsonld-context:
      name: https://w3id.org/ogc/stac/themes/name
      id: https://w3id.org/ogc/stac/themes/id
      url: '@id'
  scheme: https://w3id.org/ogc/stac/themes/scheme
  rights: http://www.w3.org/ns/dcat#rights
  wasInfluencedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasInfluencedBy
    x-jsonld-type: '@id'
  qualifiedInfluence:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInfluence
    x-jsonld-type: '@id'
  hadMember:
    x-jsonld-id: http://www.w3.org/ns/prov#hadMember
    x-jsonld-type: '@id'
  provType: '@type'
  featureType: '@type'
  entityType: '@type'
  has_provenance:
    x-jsonld-id: http://purl.org/dc/terms/provenance
    x-jsonld-type: '@id'
  wasGeneratedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
    x-jsonld-type: '@id'
  wasAttributedTo:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAttributedTo
    x-jsonld-type: '@id'
  wasDerivedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
    x-jsonld-type: '@id'
  alternateOf:
    x-jsonld-id: http://www.w3.org/ns/prov#alternateOf
    x-jsonld-type: '@id'
  hadPrimarySource:
    x-jsonld-id: http://www.w3.org/ns/prov#hadPrimarySource
    x-jsonld-type: '@id'
  specializationOf:
    x-jsonld-id: http://www.w3.org/ns/prov#specializationOf
    x-jsonld-type: '@id'
  wasInvalidatedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasInvalidatedBy
    x-jsonld-type: '@id'
  wasQuotedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasQuotedFrom
    x-jsonld-type: '@id'
  wasRevisionOf:
    x-jsonld-id: http://www.w3.org/ns/prov#wasRevisionOf
    x-jsonld-type: '@id'
  atLocation:
    x-jsonld-id: http://www.w3.org/ns/prov#atLocation
    x-jsonld-type: '@id'
  qualifiedGeneration:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedGeneration
    x-jsonld-type: '@id'
  qualifiedInvalidation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInvalidation
    x-jsonld-type: '@id'
  qualifiedDerivation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedDerivation
    x-jsonld-type: '@id'
  qualifiedAttribution:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedAttribution
    x-jsonld-type: '@id'
  activityType: '@type'
  agentType: '@type'
  Activity: http://www.w3.org/ns/prov#Activity
  ActivityInfluence: http://www.w3.org/ns/prov#ActivityInfluence
  Agent: http://xmlns.com/foaf/0.1/Agent
  AgentInfluence: http://www.w3.org/ns/prov#AgentInfluence
  Association: http://www.w3.org/ns/prov#Association
  Attribution: http://www.w3.org/ns/prov#Attribution
  Bundle: http://www.w3.org/ns/prov#Bundle
  Collection: http://www.w3.org/ns/prov#Collection
  Communication: http://www.w3.org/ns/prov#Communication
  Delegation: http://www.w3.org/ns/prov#Delegation
  Derivation: http://www.w3.org/ns/prov#Derivation
  EmptyCollection: http://www.w3.org/ns/prov#EmptyCollection
  End: http://www.w3.org/ns/prov#End
  Entity: http://www.w3.org/ns/prov#Entity
  EntityInfluence: http://www.w3.org/ns/prov#EntityInfluence
  Generation: http://www.w3.org/ns/prov#Generation
  Influence: http://www.w3.org/ns/prov#Influence
  InstantaneousEvent: http://www.w3.org/ns/prov#InstantaneousEvent
  Invalidation: http://www.w3.org/ns/prov#Invalidation
  Location: http://purl.org/dc/terms/Location
  Organization: https://schema.org/Organization
  Person: http://xmlns.com/foaf/0.1/Person
  Plan: http://www.w3.org/ns/prov#Plan
  PrimarySource: http://www.w3.org/ns/prov#PrimarySource
  Quotation: http://www.w3.org/ns/prov#Quotation
  Revision: http://www.w3.org/ns/prov#Revision
  Role: https://schema.org/Role
  SoftwareAgent: http://www.w3.org/ns/prov#SoftwareAgent
  Start: http://www.w3.org/ns/prov#Start
  Usage: http://www.w3.org/ns/prov#Usage
  ServiceDescription: http://www.w3.org/ns/prov#ServiceDescription
  DirectQueryService: http://www.w3.org/ns/prov#DirectQueryService
  Accept: http://www.w3.org/ns/prov#Accept
  Contribute: http://www.w3.org/ns/prov#Contribute
  Contributor: http://www.w3.org/ns/prov#Contributor
  Copyright: http://www.w3.org/ns/prov#Copyright
  Create: http://www.w3.org/ns/prov#Create
  Creator: http://www.w3.org/ns/prov#Creator
  Modify: http://www.w3.org/ns/prov#Modify
  Publish: http://www.w3.org/ns/prov#Publish
  Publisher: http://www.w3.org/ns/prov#Publisher
  Replace: http://www.w3.org/ns/prov#Replace
  RightsAssignment: http://www.w3.org/ns/prov#RightsAssignment
  RightsHolder: http://www.w3.org/ns/prov#RightsHolder
  Submit: http://www.w3.org/ns/prov#Submit
  Dictionary: http://www.w3.org/ns/prov#Dictionary
  EmptyDictionary: http://www.w3.org/ns/prov#EmptyDictionary
  KeyEntityPair: http://www.w3.org/ns/prov#KeyEntityPair
  Insertion: http://www.w3.org/ns/prov#Insertion
  Removal: http://www.w3.org/ns/prov#Removal
  atTime:
    x-jsonld-id: http://www.w3.org/ns/prov#atTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  endedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#endedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  generatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#generatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  invalidatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#invalidatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  startedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#startedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  value: http://www.opengis.net/cis/1.1/value
  provenanceUriTemplate: http://www.w3.org/ns/prov#provenanceUriTemplate
  pairKey:
    x-jsonld-id: http://www.w3.org/ns/prov#pairKey
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  removedKey:
    x-jsonld-id: http://www.w3.org/ns/prov#removedKey
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  actedOnBehalfOf:
    x-jsonld-id: http://www.w3.org/ns/prov#actedOnBehalfOf
    x-jsonld-type: '@id'
  agent:
    x-jsonld-id: http://www.w3.org/ns/prov#agent
    x-jsonld-type: '@id'
  entity:
    x-jsonld-id: http://www.w3.org/ns/prov#entity
    x-jsonld-type: '@id'
  generated:
    x-jsonld-id: http://www.w3.org/ns/prov#generated
    x-jsonld-type: '@id'
  hadActivity:
    x-jsonld-id: http://www.w3.org/ns/prov#hadActivity
    x-jsonld-type: '@id'
  activity:
    x-jsonld-id: http://www.w3.org/ns/prov#activity
    x-jsonld-type: '@id'
  hadGeneration:
    x-jsonld-id: http://www.w3.org/ns/prov#hadGeneration
    x-jsonld-type: '@id'
  hadPlan:
    x-jsonld-id: http://www.w3.org/ns/prov#hadPlan
    x-jsonld-type: '@id'
  hadRole:
    x-jsonld-id: http://www.w3.org/ns/prov#hadRole
    x-jsonld-type: '@id'
  hadUsage:
    x-jsonld-id: http://www.w3.org/ns/prov#hadUsage
    x-jsonld-type: '@id'
  influenced:
    x-jsonld-id: http://www.w3.org/ns/prov#influenced
    x-jsonld-type: '@id'
  influencer:
    x-jsonld-id: http://www.w3.org/ns/prov#influencer
    x-jsonld-type: '@id'
  invalidated:
    x-jsonld-id: http://www.w3.org/ns/prov#invalidated
    x-jsonld-type: '@id'
  qualifiedAssociation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedAssociation
    x-jsonld-type: '@id'
  qualifiedCommunication:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedCommunication
    x-jsonld-type: '@id'
  qualifiedDelegation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedDelegation
    x-jsonld-type: '@id'
  qualifiedEnd:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedEnd
    x-jsonld-type: '@id'
  qualifiedPrimarySource:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedPrimarySource
    x-jsonld-type: '@id'
  qualifiedQuotation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedQuotation
    x-jsonld-type: '@id'
  qualifiedRevision:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedRevision
    x-jsonld-type: '@id'
  qualifiedStart:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedStart
    x-jsonld-type: '@id'
  qualifiedUsage:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedUsage
    x-jsonld-type: '@id'
  used:
    x-jsonld-id: http://www.w3.org/ns/prov#used
    x-jsonld-type: '@id'
  wasAssociatedWith:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAssociatedWith
    x-jsonld-type: '@id'
  wasEndedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasEndedBy
    x-jsonld-type: '@id'
  wasInformedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasInformedBy
    x-jsonld-type: '@id'
  wasStartedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasStartedBy
    x-jsonld-type: '@id'
  has_anchor:
    x-jsonld-id: http://www.w3.org/ns/prov#has_anchor
    x-jsonld-type: '@id'
  has_query_service:
    x-jsonld-id: http://www.w3.org/ns/prov#has_query_service
    x-jsonld-type: '@id'
  describesService:
    x-jsonld-id: http://www.w3.org/ns/prov#describesService
    x-jsonld-type: '@id'
  pingback:
    x-jsonld-id: http://www.w3.org/ns/prov#pingback
    x-jsonld-type: '@id'
  dictionary:
    x-jsonld-id: http://www.w3.org/ns/prov#dictionary
    x-jsonld-type: '@id'
  derivedByInsertionFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#derivedByInsertionFrom
    x-jsonld-type: '@id'
  derivedByRemovalFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#derivedByRemovalFrom
    x-jsonld-type: '@id'
  insertedKeyEntityPair:
    x-jsonld-id: http://www.w3.org/ns/prov#insertedKeyEntityPair
    x-jsonld-type: '@id'
  hadDictionaryMember:
    x-jsonld-id: http://www.w3.org/ns/prov#hadDictionaryMember
    x-jsonld-type: '@id'
  pairEntity:
    x-jsonld-id: http://www.w3.org/ns/prov#pairEntity
    x-jsonld-type: '@id'
  qualifiedInsertion:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedInsertion
    x-jsonld-type: '@id'
  qualifiedRemoval:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedRemoval
    x-jsonld-type: '@id'
  asInBundle:
    x-jsonld-id: http://www.w3.org/ns/prov#asInBundle
    x-jsonld-type: '@id'
  mentionOf:
    x-jsonld-id: http://www.w3.org/ns/prov#mentionOf
    x-jsonld-type: '@id'
  name: https://w3id.org/ogc/stac/cf/name
  role: https://w3id.org/ogc/hosted/seadots/catalog#role
  convention: https://w3id.org/ogc/hosted/seadots/catalog#metadataConvention
  cf:parameter:
    x-jsonld-id: https://stac-extensions.github.io/cf/v0.2.0/schema.json#parameter
    x-jsonld-container: '@set'
  schema:
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
  derivedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
    x-jsonld-container: '@set'
    x-jsonld-type: '@id'
  IndexAxisType: http://www.opengis.net/cis/1.1/IndexAxisType
  spatial: http://purl.org/dc/terms/spatial
  previewInfo:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/previewInfo
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  hasEmail:
    x-jsonld-id: http://www.w3.org/2006/vcard/ns#hasEmail
    x-jsonld-type: '@id'
  QualityMeasurement: http://www.w3.org/ns/dqv#QualityMeasurement
  coverage:
    x-jsonld-id: http://www.opengis.net/cis/1.1/coverage
    x-jsonld-type: '@id'
  VideoResource: https://w3id.org/idsa/core/VideoResource
  scopeNote: http://www.w3.org/2004/02/skos/core#scopeNote
  endpointDescription:
    x-jsonld-id: http://www.w3.org/ns/dcat#endpointDescription
    x-jsonld-type: '@id'
  DigitalContent: https://w3id.org/idsa/core/DigitalContent
  affiliation: https://schema.org/affiliation
  endpointArtifact:
    x-jsonld-id: https://w3id.org/idsa/core/endpointArtifact
    x-jsonld-type: '@id'
  Unit: http://qudt.org/schema/qudt/Unit
  versionInfo: http://www.w3.org/2002/07/owl#versionInfo
  VDataBlockType: http://www.opengis.net/cis/1.1/VDataBlockType
  ImageRepresentation: https://w3id.org/idsa/core/ImageRepresentation
  lowerBound:
    x-jsonld-id: http://www.opengis.net/cis/1.1/lowerBound
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
  GeoPoint: https://w3id.org/idsa/core/GeoPoint
  Dataset: http://www.w3.org/ns/dcat#Dataset
  EnvelopeByAxisType: http://www.opengis.net/cis/1.1/EnvelopeByAxisType
  width:
    x-jsonld-id: https://w3id.org/idsa/core/width
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  compressFormat:
    x-jsonld-id: http://www.w3.org/ns/dcat#compressFormat
    x-jsonld-type: '@id'
  Relationship: http://www.w3.org/ns/dcat#Relationship
  concept:
    x-jsonld-id: http://purl.org/linked-data/cube#concept
    x-jsonld-type: '@id'
  ProvenanceStatement: http://purl.org/dc/terms/ProvenanceStatement
  accrualPeriodicity: http://purl.org/dc/terms/accrualPeriodicity
  Asset: http://www.w3.org/ns/odrl/2/Asset
  adms.Asset: http://www.w3.org/ns/adms#Asset
  model:
    x-jsonld-id: http://www.opengis.net/cis/1.1/model
    x-jsonld-type: '@id'
  Type: http://www.w3.org/2006/vcard/ns#Type
  MediaType: http://purl.org/dc/terms/MediaType
  vcard.Organization: http://www.w3.org/2006/vcard/ns#Organization
  Distribution: http://www.w3.org/ns/dcat#Distribution
  issued: http://purl.org/dc/terms/issued
  dataset:
    x-jsonld-id: http://www.w3.org/ns/dcat#dataset
    x-jsonld-type: '@id'
  AudioRepresentation: https://w3id.org/idsa/core/AudioRepresentation
  usageNote: http://purl.org/vocab/vann/usageNote
  AxisExtendType: http://www.opengis.net/cis/1.1/AxisExtendType
  height:
    x-jsonld-id: https://w3id.org/idsa/core/height
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  distribution:
    x-jsonld-id: http://www.w3.org/ns/dcat#distribution
    x-jsonld-type: '@id'
  downloadURL:
    x-jsonld-id: http://www.w3.org/ns/dcat#downloadURL
    x-jsonld-type: '@id'
  hasQualityMetadata:
    x-jsonld-id: http://www.w3.org/ns/dqv#hasQualityMetadata
    x-jsonld-type: '@id'
  coordinate:
    x-jsonld-id: http://www.opengis.net/cis/1.1/coordinate
    x-jsonld-type: '@id'
  ComponentProperty: http://purl.org/linked-data/cube#ComponentProperty
  hasVersion: http://purl.org/dc/terms/hasVersion
  dcat.hasVersion:
    x-jsonld-id: http://www.w3.org/ns/dcat#hasVersion
    x-jsonld-type: '@id'
  frameRate:
    x-jsonld-id: https://w3id.org/idsa/core/frameRate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  QualityMetadata: http://www.w3.org/ns/dqv#QualityMetadata
  Geometry: http://www.opengis.net/ont/geosparql#Geometry
  locn.Geometry: http://www.w3.org/ns/locn#Geometry
  GridLimitsType: http://www.opengis.net/cis/1.1/GridLimitsType
  hasValue:
    x-jsonld-id: http://www.w3.org/2006/vcard/ns#hasValue
    x-jsonld-type: '@id'
  temporalResolution: http://www.w3.org/ns/dcat#temporalResolution
  versionNotes:
    x-jsonld-id: http://www.w3.org/ns/adms#versionNotes
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  VideoRepresentation: https://w3id.org/idsa/core/VideoRepresentation
  GeoFeature: https://w3id.org/idsa/core/GeoFeature
  landingPage:
    x-jsonld-id: http://www.w3.org/ns/dcat#landingPage
    x-jsonld-type: '@id'
  maker:
    x-jsonld-id: http://xmlns.com/foaf/0.1/maker
    x-jsonld-type: '@id'
  isPrimaryTopicOf:
    x-jsonld-id: http://xmlns.com/foaf/0.1/isPrimaryTopicOf
    x-jsonld-type: '@id'
  fileReference: http://www.opengis.net/cis/1.1/fileReference
  hasAddress:
    x-jsonld-id: http://www.w3.org/2006/vcard/ns#hasAddress
    x-jsonld-type: '@id'
  DataRepresentation: https://w3id.org/idsa/core/DataRepresentation
  sensorInstanceRef:
    x-jsonld-id: http://www.sensorml.com/sensorML-2.0/sensorInstanceRef
    x-jsonld-type: '@id'
  generalGrid:
    x-jsonld-id: http://www.opengis.net/cis/1.1/generalGrid
    x-jsonld-type: '@id'
  structure:
    x-jsonld-id: http://purl.org/linked-data/cube#structure
    x-jsonld-type: '@id'
  label: http://www.w3.org/2000/01/rdf-schema#label
  positionValuePair:
    x-jsonld-id: http://www.opengis.net/cis/1.1/positionValuePair
    x-jsonld-type: '@id'
  PVPType: http://www.opengis.net/cis/1.1/PVPType
  hasTelephone:
    x-jsonld-id: http://www.w3.org/2006/vcard/ns#hasTelephone
    x-jsonld-type: '@id'
  scaleFactor:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/scaleFactor
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#float
  AllowedValues: http://www.opengis.net/swe/2.0/AllowedValues
  DescribedSemantically: https://w3id.org/idsa/core/DescribedSemantically
  isPartOf: http://purl.org/dc/terms/isPartOf
  filenameExtension:
    x-jsonld-id: https://w3id.org/idsa/core/filenameExtension
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  project: https://w3id.org/iliad/oim/metadata/project
  Concept: http://www.w3.org/2004/02/skos/core#Concept
  component:
    x-jsonld-id: http://purl.org/linked-data/cube#component
    x-jsonld-type: '@id'
  measure:
    x-jsonld-id: http://purl.org/linked-data/cube#measure
    x-jsonld-type: '@id'
  gridLimits:
    x-jsonld-id: http://www.opengis.net/cis/1.1/gridLimits
    x-jsonld-type: '@id'
  user:
    x-jsonld-id: http://data.europa.eu/930/user
    x-jsonld-type: '@id'
  TextRepresentation: https://w3id.org/idsa/core/TextRepresentation
  TextResource: https://w3id.org/idsa/core/TextResource
  DataResource: https://w3id.org/idsa/core/DataResource
  rangeSet:
    x-jsonld-id: http://www.opengis.net/cis/1.1/rangeSet
    x-jsonld-type: '@id'
  idsa.Location: https://w3id.org/idsa/core/Location
  rangeType:
    x-jsonld-id: http://www.opengis.net/cis/1.1/rangeType
    x-jsonld-type: '@id'
  axisLabels:
    x-jsonld-id: http://www.opengis.net/cis/1.1/axisLabels
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  path:
    x-jsonld-id: https://w3id.org/idsa/core/path
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  interpolationRestriction:
    x-jsonld-id: http://www.opengis.net/cis/1.1/interpolationRestriction
    x-jsonld-type: '@id'
  axis:
    x-jsonld-id: http://www.opengis.net/cis/1.1/axis
    x-jsonld-type: '@id'
  ImageResource: https://w3id.org/idsa/core/ImageResource
  spatialResolutionInMeters: http://www.w3.org/ns/dcat#spatialResolutionInMeters
  partition:
    x-jsonld-id: http://www.opengis.net/cis/1.1/partition
    x-jsonld-type: '@id'
  fn:
    x-jsonld-id: http://www.w3.org/2006/vcard/ns#fn
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  CoverageByPartitioningType: http://www.opengis.net/cis/1.1/CoverageByPartitioningType
  GeneralGridCoverageType: http://www.opengis.net/cis/1.1/GeneralGridCoverageType
  homepage:
    x-jsonld-id: http://xmlns.com/foaf/0.1/homepage
    x-jsonld-type: '@id'
  maxValue: https://w3id.org/iliad/oim/metadata/maxValue
  sensorModelRef:
    x-jsonld-id: http://www.sensorml.com/sensorML-2.0/sensorModelRef
    x-jsonld-type: '@id'
  Axis: http://www.opengis.net/cis/1.1/Axis
  appliedModel:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/appliedModel
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  hasQualityMeasurement:
    x-jsonld-id: http://www.w3.org/ns/dqv#hasQualityMeasurement
    x-jsonld-type: '@id'
  Graph: http://www.w3.org/2004/03/trix/rdfg-1/Graph
  unitsDescription:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/unitsDescription
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  Artifact: https://w3id.org/idsa/core/Artifact
  filters:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/filters
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  rightsHolder: http://purl.org/dc/terms/rightsHolder
  noDataValue:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/noDataValue
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  QualityAnnotation: http://www.w3.org/ns/dqv#QualityAnnotation
  searchText:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/searchText
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  notation: http://www.w3.org/2004/02/skos/core#notation
  Participant: https://w3id.org/idsa/core/Participant
  profileSchema:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/profileSchema
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  Described: https://w3id.org/idsa/core/Described
  coverageRef:
    x-jsonld-id: http://www.opengis.net/cis/1.1/coverageRef
    x-jsonld-type: '@id'
  dct.Agent: http://purl.org/dc/terms/Agent
  prov.Agent: http://www.w3.org/ns/prov#Agent
  ContentType: https://w3id.org/idsa/core/ContentType
  creator: http://purl.org/dc/terms/creator
  swe.name: http://www.opengis.net/swe/2.0/name
  dataBlock:
    x-jsonld-id: http://www.opengis.net/cis/1.1/dataBlock
    x-jsonld-type: '@id'
  DataService: http://www.w3.org/ns/dcat#DataService
  Individual: http://www.w3.org/2006/vcard/ns#Individual
  representation:
    x-jsonld-id: https://w3id.org/idsa/core/representation
    x-jsonld-type: '@id'
  minDate:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/minDate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTimeStamp
  interval:
    x-jsonld-id: http://www.opengis.net/swe/2.0/interval
    x-jsonld-type: '@id'
  uomLabel:
    x-jsonld-id: http://www.opengis.net/cis/1.1/uomLabel
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  schemaAgency:
    x-jsonld-id: http://www.w3.org/ns/adms#schemaAgency
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  RangeSetType: http://www.opengis.net/cis/1.1/RangeSetType
  allowedInterpolation:
    x-jsonld-id: http://www.opengis.net/cis/1.1/allowedInterpolation
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  ComponentSpecification: http://purl.org/linked-data/cube#ComponentSpecification
  axisLabel:
    x-jsonld-id: http://www.opengis.net/cis/1.1/axisLabel
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  Work: http://www.w3.org/2006/vcard/ns#Work
  TemporalEntity: http://www.w3.org/2006/time#TemporalEntity
  DataRecordType: http://www.opengis.net/swe/2.0/DataRecordType
  IrregularAxisType: http://www.opengis.net/cis/1.1/IrregularAxisType
  field:
    x-jsonld-id: http://www.opengis.net/swe/2.0/field
    x-jsonld-type: '@id'
  PartitionSetType: http://www.opengis.net/cis/1.1/PartitionSetType
  identifier: http://purl.org/dc/terms/identifier
  adms.identifier:
    x-jsonld-id: http://www.w3.org/ns/adms#identifier
    x-jsonld-type: '@id'
  keyword:
    x-jsonld-id: http://www.w3.org/ns/dcat#keyword
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  envelope:
    x-jsonld-id: http://www.opengis.net/cis/1.1/envelope
    x-jsonld-type: '@id'
  processor:
    x-jsonld-id: http://data.europa.eu/930/processor
    x-jsonld-type: '@id'
  endpointInformation:
    x-jsonld-id: https://w3id.org/idsa/core/endpointInformation
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  subject: http://purl.org/dc/terms/subject
  fileName:
    x-jsonld-id: https://w3id.org/idsa/core/fileName
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  qualifiedRelation:
    x-jsonld-id: http://www.w3.org/ns/dcat#qualifiedRelation
    x-jsonld-type: '@id'
  metadata:
    x-jsonld-id: http://www.opengis.net/cis/1.1/metadata
    x-jsonld-type: '@id'
  byteSize: http://www.w3.org/ns/dcat#byteSize
  idsa.byteSize:
    x-jsonld-id: https://w3id.org/idsa/core/byteSize
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
  instance:
    x-jsonld-id: https://w3id.org/idsa/core/instance
    x-jsonld-type: '@id'
  isDefinedBy: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
  definition: http://www.w3.org/2004/02/skos/core#definition
  swe.definition:
    x-jsonld-id: http://www.opengis.net/swe/2.0/definition
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  RangeSetRefType: http://www.opengis.net/cis/1.1/RangeSetRefType
  srsName:
    x-jsonld-id: http://www.opengis.net/cis/1.1/srsName
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  principalInvestigator:
    x-jsonld-id: http://data.europa.eu/930/principalInvestigator
    x-jsonld-type: '@id'
  QuantityType: http://www.opengis.net/swe/2.0/QuantityType
  technicalManagerInfo:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/technicalManagerInfo
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  colorTable:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/colorTable
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  names:
    x-jsonld-id: http://www.opengis.net/swe/2.0/names
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  Property: http://www.w3.org/1999/02/22-rdf-syntax-ns#Property
  dataType:
    x-jsonld-id: https://w3id.org/idsa/core/dataType
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  source: http://purl.org/dc/terms/source
  MeasureProperty: http://purl.org/linked-data/cube#MeasureProperty
  publisher: http://purl.org/dc/terms/publisher
  mediaType: http://purl.org/dc/terms/mediaType
  uom:
    x-jsonld-id: http://www.opengis.net/swe/2.0/uom
    x-jsonld-type: '@id'
  subDatasetName: https://w3id.org/iliad/oim/metadata/subDatasetName
  upperBound:
    x-jsonld-id: http://www.opengis.net/cis/1.1/upperBound
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
  version: http://www.w3.org/ns/dcat#version
  modified: http://purl.org/dc/terms/modified
  Frequency: http://purl.org/dc/terms/Frequency
  idsa.Frequency: https://w3id.org/idsa/core/Frequency
  Endpoint: https://w3id.org/idsa/core/Endpoint
  endpointURL:
    x-jsonld-id: http://www.w3.org/ns/dcat#endpointURL
    x-jsonld-type: '@id'
  provenance: http://purl.org/dc/terms/provenance
  samplingRate:
    x-jsonld-id: https://w3id.org/idsa/core/samplingRate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  CoverageByDomainAndRangeType: http://www.opengis.net/cis/1.1/CoverageByDomainAndRangeType
  inSeries:
    x-jsonld-id: http://www.w3.org/ns/dcat#inSeries
    x-jsonld-type: '@id'
  endpointDocumentation:
    x-jsonld-id: https://w3id.org/idsa/core/endpointDocumentation
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  distributor:
    x-jsonld-id: http://data.europa.eu/930/distributor
    x-jsonld-type: '@id'
  accessRights: http://purl.org/dc/terms/accessRights
  DCMIType: http://purl.org/dc/terms/DCMIType
  wasUsedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasUsedBy
    x-jsonld-type: '@id'
  checkSum:
    x-jsonld-id: https://w3id.org/idsa/core/checkSum
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  seeAlso: http://www.w3.org/2000/01/rdf-schema#seeAlso
  contentType:
    x-jsonld-id: https://w3id.org/idsa/core/contentType
    x-jsonld-type: '@id'
  RepresentationInstance: https://w3id.org/idsa/core/RepresentationInstance
  partitionSet:
    x-jsonld-id: http://www.opengis.net/cis/1.1/partitionSet
    x-jsonld-type: '@id'
  datasetManagerInfo:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/datasetManagerInfo
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  contentStandard:
    x-jsonld-id: https://w3id.org/idsa/core/contentStandard
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  dataTypeSchema:
    x-jsonld-id: https://w3id.org/idsa/core/dataTypeSchema
    x-jsonld-type: '@id'
  Language: https://w3id.org/idsa/core/Language
  resourceProvider:
    x-jsonld-id: http://data.europa.eu/930/resourceProvider
    x-jsonld-type: '@id'
  contactPoint:
    x-jsonld-id: http://www.w3.org/ns/dcat#contactPoint
    x-jsonld-type: '@id'
  Resource: http://www.w3.org/ns/dcat#Resource
  idsa.Resource: https://w3id.org/idsa/core/Resource
  rdfs.Resource: http://www.w3.org/2000/01/rdf-schema#Resource
  hasQualityAnnotation:
    x-jsonld-id: http://www.w3.org/ns/dqv#hasQualityAnnotation
    x-jsonld-type: '@id'
  domainSet:
    x-jsonld-id: http://www.opengis.net/cis/1.1/domainSet
    x-jsonld-type: '@id'
  SpatialThing: http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing
  theme:
    x-jsonld-id: http://www.w3.org/ns/dcat#theme
    x-jsonld-type: '@id'
  Party: http://www.w3.org/ns/odrl/2/Party
  comment: http://www.w3.org/2000/01/rdf-schema#comment
  custodian:
    x-jsonld-id: http://data.europa.eu/930/custodian
    x-jsonld-type: '@id'
  Document: http://xmlns.com/foaf/0.1/Document
  page:
    x-jsonld-id: http://xmlns.com/foaf/0.1/page
    x-jsonld-type: '@id'
  Group: http://xmlns.com/foaf/0.1/Group
  TransformationBySensorModelType: http://www.opengis.net/cis/1.1/TransformationBySensorModelType
  uomLabels:
    x-jsonld-id: http://www.opengis.net/cis/1.1/uomLabels
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  contributor: http://purl.org/dc/terms/contributor
  originator:
    x-jsonld-id: http://data.europa.eu/930/originator
    x-jsonld-type: '@id'
  resolutionUnit:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/resolutionUnit
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  AudioResource: https://w3id.org/idsa/core/AudioResource
  DisplacementAxisNestType: http://www.opengis.net/cis/1.1/DisplacementAxisNestType
  DomainSetType: http://www.opengis.net/cis/1.1/DomainSetType
  generalizationOf:
    x-jsonld-id: http://www.w3.org/ns/prov#generalizationOf
    x-jsonld-type: '@id'
  displacement:
    x-jsonld-id: http://www.opengis.net/cis/1.1/displacement
    x-jsonld-type: '@id'
  minValue: https://w3id.org/iliad/oim/metadata/minValue
  UnitReference: http://www.opengis.net/swe/2.0/UnitReference
  code:
    x-jsonld-id: http://www.opengis.net/swe/2.0/code
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  Identifier: http://www.w3.org/ns/adms#Identifier
  epsg:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/epsg
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  Home: http://www.w3.org/2006/vcard/ns#Home
  ManagedEntity: https://w3id.org/idsa/core/ManagedEntity
  format: http://purl.org/dc/terms/format
  accessURL:
    x-jsonld-id: http://www.w3.org/ns/dcat#accessURL
    x-jsonld-type: '@id'
  credits:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/credits
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  sample:
    x-jsonld-id: http://www.w3.org/ns/adms#sample
    x-jsonld-type: '@id'
  BoundingPolygon: https://w3id.org/idsa/core/BoundingPolygon
  Kind: http://www.w3.org/2006/vcard/ns#Kind
  relation: http://purl.org/dc/terms/relation
  temporal: http://purl.org/dc/terms/temporal
  accrualPolicy: http://purl.org/dc/terms/accrualPolicy
  resolution:
    x-jsonld-id: http://www.opengis.net/cis/1.1/resolution
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  maxDate:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/maxDate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTimeStamp
  constraint:
    x-jsonld-id: http://www.opengis.net/swe/2.0/constraint
    x-jsonld-type: '@id'
  ConnectorEndpoint: https://w3id.org/idsa/core/ConnectorEndpoint
  DataStructureDefinition: http://purl.org/linked-data/cube#DataStructureDefinition
  numberOfRecords:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/numberOfRecords
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
  RegularAxisType: http://www.opengis.net/cis/1.1/RegularAxisType
  PhotonFluxDensity: http://purl.oclc.org/NET/ssnx/qu/dim#PhotonFluxDensity
  implements:
    x-jsonld-id: http://www.w3.org/ns/ssn/implements
    x-jsonld-type: '@id'
  Attachable: http://purl.org/linked-data/cube#Attachable
  QuantityValue: http://qudt.org/schema/qudt/QuantityValue
  Line: http://www.opengis.net/ont/sf#Line
  member:
    x-jsonld-id: http://xmlns.com/foaf/0.1/member
    x-jsonld-type: '@id'
  example: http://www.w3.org/2004/02/skos/core#example
  Slice: http://purl.org/linked-data/cube#Slice
  Concentration: http://purl.oclc.org/NET/ssnx/qu/dim#Concentration
  dataSet:
    x-jsonld-id: http://purl.org/linked-data/cube#dataSet
    x-jsonld-type: '@id'
  componentAttachment:
    x-jsonld-id: http://purl.org/linked-data/cube#componentAttachment
    x-jsonld-type: '@id'
  Platform: http://www.w3.org/ns/sosa/Platform
  Deployment: http://www.w3.org/ns/ssn/Deployment
  MultiSurface: http://www.opengis.net/ont/sf#MultiSurface
  TemporalDuration: http://www.w3.org/2006/time#TemporalDuration
  Procedure: http://www.w3.org/ns/sosa/Procedure
  DiffusionCoefficient: http://purl.oclc.org/NET/ssnx/qu/dim#DiffusionCoefficient
  asGeoJSON:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#asGeoJSON
    x-jsonld-type: http://www.opengis.net/ont/geosparql#geoJSONLiteral
  Volume: http://purl.oclc.org/NET/ssnx/qu/dim#Volume
  Thing: http://www.w3.org/2002/07/owl#Thing
  GFI_Feature: http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_Feature
  AttributeProperty: http://purl.org/linked-data/cube#AttributeProperty
  quantityValue:
    x-jsonld-id: http://qudt.org/schema/qudt/quantityValue
    x-jsonld-type: '@id'
  TemporalUnit: http://www.w3.org/2006/time#TemporalUnit
  hosts:
    x-jsonld-id: http://www.w3.org/ns/sosa/hosts
    x-jsonld-type: '@id'
  asWKT:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#asWKT
    x-jsonld-type: http://www.opengis.net/ont/geosparql#wktLiteral
  hasOutput:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasOutput
    x-jsonld-type: '@id'
  Angle: http://purl.oclc.org/NET/ssnx/qu/dim#Angle
  TemperatureDrift: http://purl.oclc.org/NET/ssnx/qu/dim#TemperatureDrift
  RotationalSpeed: http://purl.oclc.org/NET/ssnx/qu/dim#RotationalSpeed
  FeatureOfInterest: http://www.w3.org/ns/sosa/FeatureOfInterest
  Class: http://www.w3.org/2000/01/rdf-schema#Class
  ObservationCollection: http://www.w3.org/ns/sosa/ObservationCollection
  NumberPerArea: http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerArea
  depiction: http://xmlns.com/foaf/0.1/depiction
  Curve: http://www.opengis.net/ont/sf#Curve
  Instant: http://www.w3.org/2006/time#Instant
  sfWithin:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#sfWithin
    x-jsonld-type: '@id'
  hasBoundingBox:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#hasBoundingBox
    x-jsonld-type: '@id'
  ThermalConductivity: http://purl.oclc.org/NET/ssnx/qu/dim#ThermalConductivity
  hasUltimateFeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasUltimateFeatureOfInterest
    x-jsonld-type: '@id'
  domainIncludes: https://schema.org/domainIncludes
  madeBySensor:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
    x-jsonld-type: '@id'
  long: http://www.w3.org/2003/01/geo/wgs84_pos#long
  ActuatableProperty: http://www.w3.org/ns/sosa/ActuatableProperty
  numericValue: http://qudt.org/schema/qudt/numericValue
  attribute:
    x-jsonld-id: http://purl.org/linked-data/cube#attribute
    x-jsonld-type: '@id'
  SliceKey: http://purl.org/linked-data/cube#SliceKey
  Result: http://www.w3.org/ns/sosa/Result
  isHostedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isHostedBy
    x-jsonld-type: '@id'
  Compressibility: http://purl.oclc.org/NET/ssnx/qu/dim#Compressibility
  inDeployment:
    x-jsonld-id: http://www.w3.org/ns/ssn/inDeployment
    x-jsonld-type: '@id'
  ComponentSet: http://purl.org/linked-data/cube#ComponentSet
  MassPerTimePerArea: http://purl.oclc.org/NET/ssnx/qu/dim#MassPerTimePerArea
  numericDuration:
    x-jsonld-id: http://www.w3.org/2006/time#numericDuration
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  ElectricConductivity: http://purl.oclc.org/NET/ssnx/qu/dim#ElectricConductivity
  Temperature: http://purl.oclc.org/NET/ssnx/qu/dim#Temperature
  hasProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasProperty
    x-jsonld-type: '@id'
  Measure: http://def.seegrid.csiro.au/isotc211/iso19103/2005/basic#Measure
  Triangle: http://www.opengis.net/ont/sf#Triangle
  note: http://www.w3.org/2004/02/skos/core#note
  observationGroup:
    x-jsonld-id: http://purl.org/linked-data/cube#observationGroup
    x-jsonld-type: '@id'
  Interval: http://www.w3.org/2006/time#Interval
  EnergyFlux: http://purl.oclc.org/NET/ssnx/qu/dim#EnergyFlux
  StressOrPressure: http://purl.oclc.org/NET/ssnx/qu/dim#StressOrPressure
  resultTime:
    x-jsonld-id: http://www.w3.org/ns/sosa/resultTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  VolumeDensityRate: http://purl.oclc.org/NET/ssnx/qu/dim#VolumeDensityRate
  phenomenonTime:
    x-jsonld-id: http://www.w3.org/ns/sosa/phenomenonTime
    x-jsonld-type: '@id'
  Energy: http://purl.oclc.org/NET/ssnx/qu/dim#Energy
  foaf.name: http://xmlns.com/foaf/0.1/name
  hasSerialization:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#hasSerialization
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  hasTime:
    x-jsonld-id: http://www.w3.org/2006/time#hasTime
    x-jsonld-type: '@id'
  SF_SamplingFeature.sampledFeature:
    x-jsonld-id: http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature.sampledFeature
    x-jsonld-type: '@id'
  hasMember:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
    x-jsonld-type: '@id'
  rangeIncludes: https://schema.org/rangeIncludes
  hasInput:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasInput
    x-jsonld-type: '@id'
  Mass: http://purl.oclc.org/NET/ssnx/qu/dim#Mass
  implementedBy:
    x-jsonld-id: http://www.w3.org/ns/ssn/implementedBy
    x-jsonld-type: '@id'
  location:
    x-jsonld-id: http://www.w3.org/2003/01/geo/wgs84_pos#location
    x-jsonld-type: '@id'
  Scheme: http://www.w3.org/2004/02/skos/core#Scheme
  hasEnd:
    x-jsonld-id: http://www.w3.org/2006/time#hasEnd
    x-jsonld-type: '@id'
  hasBeginning:
    x-jsonld-id: http://www.w3.org/2006/time#hasBeginning
    x-jsonld-type: '@id'
  isResultOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isResultOf
    x-jsonld-type: '@id'
  SF_SamplingFeature: http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature
  DimensionProperty: http://purl.org/linked-data/cube#DimensionProperty
  alt: http://www.w3.org/2003/01/geo/wgs84_pos#alt
  Acceleration: http://purl.oclc.org/NET/ssnx/qu/dim#Acceleration
  hasSubSystem:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasSubSystem
    x-jsonld-type: '@id'
  Quantity: http://qudt.org/schema/qudt/Quantity
  MassFlowRate: http://purl.oclc.org/NET/ssnx/qu/dim#MassFlowRate
  qu.QuantityKind: http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind
  SpatialObjectCollection: http://www.opengis.net/ont/geosparql#SpatialObjectCollection
  Distance: http://purl.oclc.org/NET/ssnx/qu/dim#Distance
  deprecated: http://www.w3.org/2002/07/owl#deprecated
  Radiance: http://purl.oclc.org/NET/ssnx/qu/dim#Radiance
  Duration: http://www.w3.org/2006/time#Duration
  TIN: http://www.opengis.net/ont/sf#TIN
  SurfaceDensity: http://purl.oclc.org/NET/ssnx/qu/dim#SurfaceDensity
  wgs84.Point: http://www.w3.org/2003/01/geo/wgs84_pos#Point
  editorialNote: http://www.w3.org/2004/02/skos/core#editorialNote
  observes:
    x-jsonld-id: http://www.w3.org/ns/sosa/observes
    x-jsonld-type: '@id'
  hasDeployment:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasDeployment
    x-jsonld-type: '@id'
  hasResult:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasResult
    x-jsonld-type: '@id'
  order:
    x-jsonld-id: http://purl.org/linked-data/cube#order
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#int
  hasGeometry:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#hasGeometry
    x-jsonld-type: '@id'
  usedProcedure:
    x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
    x-jsonld-type: '@id'
  ssn.Property: http://www.w3.org/ns/ssn/Property
  sfContains:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#sfContains
    x-jsonld-type: '@id'
  Density: http://purl.oclc.org/NET/ssnx/qu/dim#Density
  LinearRing: http://www.opengis.net/ont/sf#LinearRing
  Molality: http://purl.oclc.org/NET/ssnx/qu/dim#Molality
  inXSDDateTimeStamp:
    x-jsonld-id: http://www.w3.org/2006/time#inXSDDateTimeStamp
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTimeStamp
  PropertyKind: http://purl.oclc.org/NET/ssnx/qu/qu#PropertyKind
  SpatialObject: http://www.opengis.net/ont/geosparql#SpatialObject
  sliceStructure:
    x-jsonld-id: http://purl.org/linked-data/cube#sliceStructure
    x-jsonld-type: '@id'
  hasFeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    x-jsonld-type: '@id'
  NumberPerLength: http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerLength
  lat: http://www.w3.org/2003/01/geo/wgs84_pos#lat
  VolumeFlowRate: http://purl.oclc.org/NET/ssnx/qu/dim#VolumeFlowRate
  SpecificEntropy: http://purl.oclc.org/NET/ssnx/qu/dim#SpecificEntropy
  CodedProperty: http://purl.org/linked-data/cube#CodedProperty
  observedProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
    x-jsonld-type: '@id'
  slice:
    x-jsonld-id: http://purl.org/linked-data/cube#slice
    x-jsonld-type: '@id'
  madeObservation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
    x-jsonld-type: '@id'
  date: http://purl.org/dc/terms/date
  isPropertyOf:
    x-jsonld-id: http://www.w3.org/ns/ssn/isPropertyOf
    x-jsonld-type: '@id'
  ObservationGroup: http://purl.org/linked-data/cube#ObservationGroup
  Sample: http://www.w3.org/ns/sosa/Sample
  DataSet: http://purl.org/linked-data/cube#DataSet
  PolyhedralSurface: http://www.opengis.net/ont/sf#PolyhedralSurface
  ObservableProperty: http://www.w3.org/ns/sosa/ObservableProperty
  deployedSystem:
    x-jsonld-id: http://www.w3.org/ns/ssn/deployedSystem
    x-jsonld-type: '@id'
  System: http://www.w3.org/ns/ssn/System
  unitKind:
    x-jsonld-id: http://purl.oclc.org/NET/ssnx/qu/qu#unitKind
    x-jsonld-type: '@id'
  dimension:
    x-jsonld-id: http://purl.org/linked-data/cube#dimension
    x-jsonld-type: '@id'
  RadianceExposure: http://purl.oclc.org/NET/ssnx/qu/dim#RadianceExposure
  VelocityOrSpeed: http://purl.oclc.org/NET/ssnx/qu/dim#VelocityOrSpeed
  deployedOnPlatform:
    x-jsonld-id: http://www.w3.org/ns/ssn/deployedOnPlatform
    x-jsonld-type: '@id'
  inXSDDate:
    x-jsonld-id: http://www.w3.org/2006/time#inXSDDate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
  GFI_DomainFeature: http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_DomainFeature
  Actuation: http://www.w3.org/ns/sosa/Actuation
  observation:
    x-jsonld-id: http://purl.org/linked-data/cube#observation
    x-jsonld-type: '@id'
  Dimensionless: http://purl.oclc.org/NET/ssnx/qu/dim#Dimensionless
  Area: http://purl.oclc.org/NET/ssnx/qu/dim#Area
  Sampling: http://www.w3.org/ns/sosa/Sampling
  Power: http://purl.oclc.org/NET/ssnx/qu/dim#Power
  OM_Observation: http://def.isotc211.org/iso19156/2011/Observation#OM_Observation
  prefLabel: http://www.w3.org/2004/02/skos/core#prefLabel
  Surface: http://www.opengis.net/ont/sf#Surface
  sliceKey:
    x-jsonld-id: http://purl.org/linked-data/cube#sliceKey
    x-jsonld-type: '@id'
  inScheme: http://www.w3.org/2004/02/skos/core#inScheme
  dct.description: http://purl.org/dc/terms/description
  MultiCurve: http://www.opengis.net/ont/sf#MultiCurve
  hasQuantityKind:
    x-jsonld-id: http://qudt.org/schema/qudt/hasQuantityKind
    x-jsonld-type: '@id'
  qb.Observation: http://purl.org/linked-data/cube#Observation
  EnergyDensity: http://purl.oclc.org/NET/ssnx/qu/dim#EnergyDensity
  Sensor: http://www.w3.org/ns/sosa/Sensor
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  unitType:
    x-jsonld-id: http://www.w3.org/2006/time#unitType
    x-jsonld-type: '@id'
  componentProperty:
    x-jsonld-id: http://purl.org/linked-data/cube#componentProperty
    x-jsonld-type: '@id'
  isFeatureOfInterestOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    x-jsonld-type: '@id'
  sf.Geometry: http://www.opengis.net/ont/sf#Geometry
  schema.Person: https://schema.org/Person
  Observation: http://www.w3.org/ns/sosa/Observation
  schema.name: https://schema.org/name
  QuantityKind: http://qudt.org/schema/qudt/QuantityKind
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/catalog#
x-jsonld-prefixes:
  geojson: https://purl.org/geojson/vocab#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  dct: http://purl.org/dc/terms/
  rec: https://www.opengis.net/def/ogc-api/records/
  xsd: http://www.w3.org/2001/XMLSchema#
  dcat: http://www.w3.org/ns/dcat#
  skos: http://www.w3.org/2004/02/skos/core#
  thns: https://w3id.org/ogc/stac/themes/
  stac: https://w3id.org/ogc/stac/core/
  oa: http://www.w3.org/ns/oa#
  prov: http://www.w3.org/ns/prov#
  cf: https://stac-extensions.github.io/cf/v0.2.0/schema.json#
  seadots: https://w3id.org/ogc/hosted/seadots/catalog#
  dcterms: http://purl.org/dc/terms/
  vcard: http://www.w3.org/2006/vcard/ns#
  owl: http://www.w3.org/2002/07/owl#
  foaf: http://xmlns.com/foaf/0.1/
  w3ctime: http://www.w3.org/2006/time#
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  dctype: http://purl.org/dc/dcmitype/
  qudt: http://qudt.org/schema/qudt/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data-multidim/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data-multidim/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/catalog#",
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
      "@id": "geojson:features"
    },
    "type": "@type",
    "id": "@id",
    "properties": "@nest",
    "geometry": {
      "@context": {
        "coordinates": {
          "@container": "@list",
          "@id": "geojson:coordinates"
        }
      },
      "@id": "geojson:geometry"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "links": {
      "@context": {
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
    "conformsTo": {
      "@container": "@set",
      "@id": "dct:conformsTo",
      "@type": "@id"
    },
    "time": "dct:temporal",
    "linkTemplates": {
      "@context": {
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:format",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent",
        "uriTemplate": {
          "@type": "xsd:string",
          "@id": "rec:uriTemplate"
        },
        "varBase": "rec:varBase",
        "variables": {
          "@id": "rec:hasVariable",
          "@container": "@index",
          "@index": "dct:identifier"
        }
      },
      "@id": "rec:hasLinkTemplate"
    },
    "created": "dct:created",
    "updated": "dct:modified",
    "title": {
      "@container": "@set",
      "@id": "dct:title"
    },
    "description": {
      "@container": "@set",
      "@id": "dct:description"
    },
    "keywords": {
      "@container": "@set",
      "@id": "dct:subject"
    },
    "language": {
      "@id": "rec:language",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "languages": {
      "@container": "@set",
      "@id": "rec:languages",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "resourceLanguages": {
      "@container": "@set",
      "@id": "rec:resourceLanguages",
      "@context": {
        "code": "rec:languageCode",
        "name": "skos:prefLabel"
      }
    },
    "externalIds": {
      "@container": "@set",
      "@id": "rec:scopedIdentifier",
      "@context": {
        "scheme": "rec:scheme",
        "value": "rec:id"
      }
    },
    "themes": {
      "@container": "@set",
      "@id": "thns:schemes",
      "@context": {
        "concepts": {
          "@id": "thns:concepts",
          "@context": {
            "id": {
              "@type": "xsd:string",
              "@id": "thns:id"
            },
            "url": {
              "@type": "@id",
              "@id": "@id"
            }
          },
          "@container": "@set"
        }
      }
    },
    "formats": {
      "@id": "rec:format",
      "@context": {
        "name": "rec:name"
      }
    },
    "contacts": {
      "@container": "@set",
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "license": "dct:license",
    "accessrights": "dct:accessRights",
    "variables": {
      "@container": "@id",
      "@id": "rec:hasVariable",
      "@context": {
        "@base": "http://example.com/variables/",
        "@vocab": "https://www.opengis.net/def/ogc-api/records/"
      }
    },
    "stac_extensions": "stac:hasExtension",
    "assets": {
      "@context": {
        "@vocab": "https://w3id.org/ogc/stac/assets/",
        "type": "dct:format",
        "roles": {
          "@id": "stac:roles",
          "@container": "@set"
        }
      },
      "@id": "stac:hasAsset",
      "@container": "@set"
    },
    "stac_version": "stac:version",
    "start_datetime": {
      "@id": "stac:start_datetime",
      "@type": "xsd:dateTime"
    },
    "end_datetime": {
      "@id": "stac:end_datetime",
      "@type": "xsd:dateTime"
    },
    "providers": "stac:hasProvider",
    "media_type": "dct:format",
    "extent": "dct:extent",
    "datetime": {
      "@id": "dct:date",
      "@type": "xsd:dateTime"
    },
    "concepts": {
      "@id": "thns:concepts",
      "@container": "@set",
      "@context": {
        "name": "thns:name",
        "id": "thns:id",
        "url": "@id"
      }
    },
    "scheme": "thns:scheme",
    "wasInfluencedBy": {
      "@context": {
        "Agent": "prov:Agent",
        "Location": "prov:Location",
        "Organization": "prov:Organization",
        "Person": "prov:Person",
        "Role": "prov:Role",
        "value": "prov:value",
        "name": "rdfs:label"
      },
      "@id": "prov:wasInfluencedBy",
      "@type": "@id"
    },
    "qualifiedInfluence": {
      "@context": {
        "influencer": {
          "@context": {
            "Agent": "prov:Agent",
            "Location": "prov:Location",
            "Organization": "prov:Organization",
            "Person": "prov:Person",
            "Role": "prov:Role",
            "value": "prov:value",
            "name": "rdfs:label"
          },
          "@id": "prov:influencer",
          "@type": "@id"
        },
        "activity": {
          "@context": {
            "Agent": "prov:Agent",
            "Location": "prov:Location",
            "Organization": "prov:Organization",
            "Person": "prov:Person",
            "Role": "prov:Role",
            "value": "prov:value",
            "name": "rdfs:label"
          },
          "@id": "prov:activity",
          "@type": "@id"
        },
        "agent": {
          "@context": {
            "name": "rdfs:label",
            "Agent": "prov:Agent",
            "Location": "prov:Location",
            "Organization": "prov:Organization",
            "Person": "prov:Person",
            "Role": "prov:Role",
            "value": "prov:value"
          },
          "@id": "prov:agent",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedInfluence",
      "@type": "@id"
    },
    "hadMember": {
      "@id": "prov:hadMember",
      "@type": "@id"
    },
    "provType": "@type",
    "featureType": "@type",
    "entityType": "@type",
    "has_provenance": {
      "@context": {
        "name": "rdfs:label",
        "Agent": "prov:Agent",
        "Location": "prov:Location",
        "Organization": "prov:Organization",
        "Person": "prov:Person",
        "Role": "prov:Role",
        "value": "prov:value"
      },
      "@id": "dct:provenance",
      "@type": "@id"
    },
    "wasGeneratedBy": {
      "@context": {
        "Agent": "prov:Agent",
        "Location": "prov:Location",
        "Organization": "prov:Organization",
        "Person": "prov:Person",
        "Role": "prov:Role",
        "value": "prov:value",
        "name": "rdfs:label"
      },
      "@id": "prov:wasGeneratedBy",
      "@type": "@id"
    },
    "wasAttributedTo": {
      "@context": {
        "name": "rdfs:label",
        "Agent": "prov:Agent",
        "Location": "prov:Location",
        "Organization": "prov:Organization",
        "Person": "prov:Person",
        "Role": "prov:Role",
        "value": "prov:value"
      },
      "@id": "prov:wasAttributedTo",
      "@type": "@id"
    },
    "wasDerivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@type": "@id"
    },
    "alternateOf": {
      "@id": "prov:alternateOf",
      "@type": "@id"
    },
    "hadPrimarySource": {
      "@id": "prov:hadPrimarySource",
      "@type": "@id"
    },
    "specializationOf": {
      "@id": "prov:specializationOf",
      "@type": "@id"
    },
    "wasInvalidatedBy": {
      "@context": {
        "Agent": "prov:Agent",
        "Location": "prov:Location",
        "Organization": "prov:Organization",
        "Person": "prov:Person",
        "Role": "prov:Role",
        "value": "prov:value",
        "name": "rdfs:label"
      },
      "@id": "prov:wasInvalidatedBy",
      "@type": "@id"
    },
    "wasQuotedFrom": {
      "@id": "prov:wasQuotedFrom",
      "@type": "@id"
    },
    "wasRevisionOf": {
      "@id": "prov:wasRevisionOf",
      "@type": "@id"
    },
    "generatedAtTime": {
      "@id": "prov:generatedAtTime",
      "@type": "xsd:dateTime"
    },
    "invalidatedAtTime": {
      "@id": "prov:invalidatedAtTime",
      "@type": "xsd:dateTime"
    },
    "value": "http://www.opengis.net/cis/1.1/value",
    "qualifiedPrimarySource": {
      "@context": {
        "hadActivity": {
          "@context": {
            "wasAssociatedWith": {
              "@context": {
                "name": "rdfs:label",
                "Agent": "prov:Agent",
                "Location": "prov:Location",
                "Organization": "prov:Organization",
                "Person": "prov:Person",
                "Role": "prov:Role",
                "value": "prov:value"
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "name": "rdfs:label"
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedPrimarySource",
      "@type": "@id"
    },
    "qualifiedQuotation": {
      "@context": {
        "hadActivity": {
          "@context": {
            "wasAssociatedWith": {
              "@context": {
                "name": "rdfs:label",
                "Agent": "prov:Agent",
                "Location": "prov:Location",
                "Organization": "prov:Organization",
                "Person": "prov:Person",
                "Role": "prov:Role",
                "value": "prov:value"
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "name": "rdfs:label"
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedQuotation",
      "@type": "@id"
    },
    "qualifiedRevision": {
      "@context": {
        "hadActivity": {
          "@context": {
            "wasAssociatedWith": {
              "@context": {
                "name": "rdfs:label",
                "Agent": "prov:Agent",
                "Location": "prov:Location",
                "Organization": "prov:Organization",
                "Person": "prov:Person",
                "Role": "prov:Role",
                "value": "prov:value"
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "name": "rdfs:label"
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedRevision",
      "@type": "@id"
    },
    "atLocation": {
      "@id": "prov:atLocation",
      "@type": "@id"
    },
    "qualifiedGeneration": {
      "@id": "prov:qualifiedGeneration",
      "@type": "@id"
    },
    "qualifiedInvalidation": {
      "@id": "prov:qualifiedInvalidation",
      "@type": "@id"
    },
    "qualifiedDerivation": {
      "@context": {
        "hadActivity": {
          "@context": {
            "wasAssociatedWith": {
              "@context": {
                "name": "rdfs:label",
                "Agent": "prov:Agent",
                "Location": "prov:Location",
                "Organization": "prov:Organization",
                "Person": "prov:Person",
                "Role": "prov:Role",
                "value": "prov:value"
              },
              "@id": "prov:wasAssociatedWith",
              "@type": "@id"
            },
            "qualifiedAssociation": {
              "@context": {
                "agent": {
                  "@context": {
                    "name": "rdfs:label"
                  },
                  "@id": "prov:agent",
                  "@type": "@id"
                }
              },
              "@id": "prov:qualifiedAssociation",
              "@type": "@id"
            }
          },
          "@id": "prov:hadActivity",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedDerivation",
      "@type": "@id"
    },
    "qualifiedAttribution": {
      "@context": {
        "agent": {
          "@context": {
            "name": "rdfs:label",
            "Agent": "prov:Agent",
            "Location": "prov:Location",
            "Organization": "prov:Organization",
            "Person": "prov:Person",
            "Role": "prov:Role",
            "value": "prov:value"
          },
          "@id": "prov:agent",
          "@type": "@id"
        }
      },
      "@id": "prov:qualifiedAttribution",
      "@type": "@id"
    },
    "activityType": "@type",
    "agentType": "@type",
    "Activity": "prov:Activity",
    "ActivityInfluence": "prov:ActivityInfluence",
    "Agent": "foaf:Agent",
    "AgentInfluence": "prov:AgentInfluence",
    "Association": "prov:Association",
    "Attribution": "prov:Attribution",
    "Bundle": "prov:Bundle",
    "Collection": "prov:Collection",
    "Communication": "prov:Communication",
    "Delegation": "prov:Delegation",
    "Derivation": "prov:Derivation",
    "EmptyCollection": "prov:EmptyCollection",
    "End": "prov:End",
    "Entity": "prov:Entity",
    "EntityInfluence": "prov:EntityInfluence",
    "Generation": "prov:Generation",
    "Influence": "prov:Influence",
    "InstantaneousEvent": "prov:InstantaneousEvent",
    "Invalidation": "prov:Invalidation",
    "Location": "dct:Location",
    "Organization": "https://schema.org/Organization",
    "Person": "foaf:Person",
    "Plan": "prov:Plan",
    "PrimarySource": "prov:PrimarySource",
    "Quotation": "prov:Quotation",
    "Revision": "prov:Revision",
    "Role": "https://schema.org/Role",
    "SoftwareAgent": "prov:SoftwareAgent",
    "Start": "prov:Start",
    "Usage": "prov:Usage",
    "ServiceDescription": "prov:ServiceDescription",
    "DirectQueryService": "prov:DirectQueryService",
    "Accept": "prov:Accept",
    "Contribute": "prov:Contribute",
    "Contributor": "prov:Contributor",
    "Copyright": "prov:Copyright",
    "Create": "prov:Create",
    "Creator": "prov:Creator",
    "Modify": "prov:Modify",
    "Publish": "prov:Publish",
    "Publisher": "prov:Publisher",
    "Replace": "prov:Replace",
    "RightsAssignment": "prov:RightsAssignment",
    "RightsHolder": "prov:RightsHolder",
    "Submit": "prov:Submit",
    "Dictionary": "prov:Dictionary",
    "EmptyDictionary": "prov:EmptyDictionary",
    "KeyEntityPair": "prov:KeyEntityPair",
    "Insertion": "prov:Insertion",
    "Removal": "prov:Removal",
    "atTime": {
      "@id": "prov:atTime",
      "@type": "xsd:dateTime"
    },
    "endedAtTime": {
      "@id": "prov:endedAtTime",
      "@type": "xsd:dateTime"
    },
    "startedAtTime": {
      "@id": "prov:startedAtTime",
      "@type": "xsd:dateTime"
    },
    "provenanceUriTemplate": "prov:provenanceUriTemplate",
    "pairKey": {
      "@id": "prov:pairKey",
      "@type": "rdfs:Literal"
    },
    "removedKey": {
      "@id": "prov:removedKey",
      "@type": "rdfs:Literal"
    },
    "actedOnBehalfOf": {
      "@id": "prov:actedOnBehalfOf",
      "@type": "@id"
    },
    "agent": {
      "@id": "prov:agent",
      "@type": "@id"
    },
    "entity": {
      "@id": "prov:entity",
      "@type": "@id"
    },
    "generated": {
      "@id": "prov:generated",
      "@type": "@id"
    },
    "hadActivity": {
      "@id": "prov:hadActivity",
      "@type": "@id"
    },
    "activity": {
      "@id": "prov:activity",
      "@type": "@id"
    },
    "hadGeneration": {
      "@id": "prov:hadGeneration",
      "@type": "@id"
    },
    "hadPlan": {
      "@id": "prov:hadPlan",
      "@type": "@id"
    },
    "hadRole": {
      "@id": "prov:hadRole",
      "@type": "@id"
    },
    "hadUsage": {
      "@id": "prov:hadUsage",
      "@type": "@id"
    },
    "influenced": {
      "@id": "prov:influenced",
      "@type": "@id"
    },
    "influencer": {
      "@id": "prov:influencer",
      "@type": "@id"
    },
    "invalidated": {
      "@id": "prov:invalidated",
      "@type": "@id"
    },
    "qualifiedAssociation": {
      "@id": "prov:qualifiedAssociation",
      "@type": "@id"
    },
    "qualifiedCommunication": {
      "@id": "prov:qualifiedCommunication",
      "@type": "@id"
    },
    "qualifiedDelegation": {
      "@id": "prov:qualifiedDelegation",
      "@type": "@id"
    },
    "qualifiedEnd": {
      "@id": "prov:qualifiedEnd",
      "@type": "@id"
    },
    "qualifiedStart": {
      "@id": "prov:qualifiedStart",
      "@type": "@id"
    },
    "qualifiedUsage": {
      "@id": "prov:qualifiedUsage",
      "@type": "@id"
    },
    "used": {
      "@id": "prov:used",
      "@type": "@id"
    },
    "wasAssociatedWith": {
      "@id": "prov:wasAssociatedWith",
      "@type": "@id"
    },
    "wasEndedBy": {
      "@id": "prov:wasEndedBy",
      "@type": "@id"
    },
    "wasInformedBy": {
      "@id": "prov:wasInformedBy",
      "@type": "@id"
    },
    "wasStartedBy": {
      "@id": "prov:wasStartedBy",
      "@type": "@id"
    },
    "has_anchor": {
      "@id": "prov:has_anchor",
      "@type": "@id"
    },
    "has_query_service": {
      "@id": "prov:has_query_service",
      "@type": "@id"
    },
    "describesService": {
      "@id": "prov:describesService",
      "@type": "@id"
    },
    "pingback": {
      "@id": "prov:pingback",
      "@type": "@id"
    },
    "dictionary": {
      "@id": "prov:dictionary",
      "@type": "@id"
    },
    "derivedByInsertionFrom": {
      "@id": "prov:derivedByInsertionFrom",
      "@type": "@id"
    },
    "derivedByRemovalFrom": {
      "@id": "prov:derivedByRemovalFrom",
      "@type": "@id"
    },
    "insertedKeyEntityPair": {
      "@id": "prov:insertedKeyEntityPair",
      "@type": "@id"
    },
    "hadDictionaryMember": {
      "@id": "prov:hadDictionaryMember",
      "@type": "@id"
    },
    "pairEntity": {
      "@id": "prov:pairEntity",
      "@type": "@id"
    },
    "qualifiedInsertion": {
      "@id": "prov:qualifiedInsertion",
      "@type": "@id"
    },
    "qualifiedRemoval": {
      "@id": "prov:qualifiedRemoval",
      "@type": "@id"
    },
    "asInBundle": {
      "@id": "prov:asInBundle",
      "@type": "@id"
    },
    "mentionOf": {
      "@id": "prov:mentionOf",
      "@type": "@id"
    },
    "name": {
      "@id": "foaf:name",
      "@type": "rdfs:Literal"
    },
    "unit": {
      "@id": "qudt:unit",
      "@context": {
        "@base": "http://qudt.org/vocab/unit/"
      },
      "@type": "@id"
    },
    "rights": "dcat:rights",
    "cf:parameter": {
      "@id": "cf:parameter",
      "@container": "@set"
    },
    "schema": {
      "@id": "dct:conformsTo",
      "@type": "@id"
    },
    "IndexAxisType": "http://www.opengis.net/cis/1.1/IndexAxisType",
    "spatial": "dct:spatial",
    "previewInfo": {
      "@id": "https://w3id.org/iliad/oim/metadata/previewInfo",
      "@type": "xsd:string"
    },
    "hasEmail": {
      "@id": "vcard:hasEmail",
      "@type": "@id"
    },
    "QualityMeasurement": "http://www.w3.org/ns/dqv#QualityMeasurement",
    "coverage": {
      "@id": "http://www.opengis.net/cis/1.1/coverage",
      "@type": "@id"
    },
    "VideoResource": "https://w3id.org/idsa/core/VideoResource",
    "scopeNote": "skos:scopeNote",
    "endpointDescription": {
      "@id": "dcat:endpointDescription",
      "@type": "@id"
    },
    "DigitalContent": "https://w3id.org/idsa/core/DigitalContent",
    "affiliation": "https://schema.org/affiliation",
    "endpointArtifact": {
      "@id": "https://w3id.org/idsa/core/endpointArtifact",
      "@type": "@id"
    },
    "Unit": "qudt:Unit",
    "versionInfo": "owl:versionInfo",
    "VDataBlockType": "http://www.opengis.net/cis/1.1/VDataBlockType",
    "ImageRepresentation": "https://w3id.org/idsa/core/ImageRepresentation",
    "lowerBound": {
      "@id": "http://www.opengis.net/cis/1.1/lowerBound",
      "@type": "xsd:integer"
    },
    "GeoPoint": "https://w3id.org/idsa/core/GeoPoint",
    "Dataset": "dcat:Dataset",
    "EnvelopeByAxisType": "http://www.opengis.net/cis/1.1/EnvelopeByAxisType",
    "width": {
      "@id": "https://w3id.org/idsa/core/width",
      "@type": "xsd:decimal"
    },
    "compressFormat": {
      "@id": "dcat:compressFormat",
      "@type": "@id"
    },
    "Relationship": "dcat:Relationship",
    "concept": {
      "@id": "http://purl.org/linked-data/cube#concept",
      "@type": "@id"
    },
    "ProvenanceStatement": "dct:ProvenanceStatement",
    "accrualPeriodicity": "dct:accrualPeriodicity",
    "Asset": "http://www.w3.org/ns/odrl/2/Asset",
    "adms.Asset": "http://www.w3.org/ns/adms#Asset",
    "model": {
      "@id": "http://www.opengis.net/cis/1.1/model",
      "@type": "@id"
    },
    "Type": "vcard:Type",
    "MediaType": "dct:MediaType",
    "vcard.Organization": "vcard:Organization",
    "Distribution": "dcat:Distribution",
    "issued": "dct:issued",
    "dataset": {
      "@id": "dcat:dataset",
      "@type": "@id"
    },
    "AudioRepresentation": "https://w3id.org/idsa/core/AudioRepresentation",
    "usageNote": "http://purl.org/vocab/vann/usageNote",
    "AxisExtendType": "http://www.opengis.net/cis/1.1/AxisExtendType",
    "height": {
      "@id": "https://w3id.org/idsa/core/height",
      "@type": "xsd:decimal"
    },
    "distribution": {
      "@id": "dcat:distribution",
      "@type": "@id"
    },
    "downloadURL": {
      "@id": "dcat:downloadURL",
      "@type": "@id"
    },
    "hasQualityMetadata": {
      "@id": "http://www.w3.org/ns/dqv#hasQualityMetadata",
      "@type": "@id"
    },
    "coordinate": {
      "@id": "http://www.opengis.net/cis/1.1/coordinate",
      "@type": "@id"
    },
    "ComponentProperty": "http://purl.org/linked-data/cube#ComponentProperty",
    "hasVersion": "dct:hasVersion",
    "dcat.hasVersion": {
      "@id": "dcat:hasVersion",
      "@type": "@id"
    },
    "frameRate": {
      "@id": "https://w3id.org/idsa/core/frameRate",
      "@type": "xsd:decimal"
    },
    "QualityMetadata": "http://www.w3.org/ns/dqv#QualityMetadata",
    "Geometry": "http://www.opengis.net/ont/geosparql#Geometry",
    "locn.Geometry": "http://www.w3.org/ns/locn#Geometry",
    "GridLimitsType": "http://www.opengis.net/cis/1.1/GridLimitsType",
    "hasValue": {
      "@id": "vcard:hasValue",
      "@type": "@id"
    },
    "temporalResolution": "dcat:temporalResolution",
    "versionNotes": {
      "@id": "http://www.w3.org/ns/adms#versionNotes",
      "@type": "rdfs:Literal"
    },
    "VideoRepresentation": "https://w3id.org/idsa/core/VideoRepresentation",
    "GeoFeature": "https://w3id.org/idsa/core/GeoFeature",
    "landingPage": {
      "@id": "dcat:landingPage",
      "@type": "@id"
    },
    "maker": {
      "@id": "foaf:maker",
      "@type": "@id"
    },
    "isPrimaryTopicOf": {
      "@id": "foaf:isPrimaryTopicOf",
      "@type": "@id"
    },
    "fileReference": "http://www.opengis.net/cis/1.1/fileReference",
    "hasAddress": {
      "@id": "vcard:hasAddress",
      "@type": "@id"
    },
    "DataRepresentation": "https://w3id.org/idsa/core/DataRepresentation",
    "sensorInstanceRef": {
      "@id": "http://www.sensorml.com/sensorML-2.0/sensorInstanceRef",
      "@type": "@id"
    },
    "generalGrid": {
      "@id": "http://www.opengis.net/cis/1.1/generalGrid",
      "@type": "@id"
    },
    "structure": {
      "@id": "http://purl.org/linked-data/cube#structure",
      "@type": "@id"
    },
    "label": "rdfs:label",
    "positionValuePair": {
      "@id": "http://www.opengis.net/cis/1.1/positionValuePair",
      "@type": "@id"
    },
    "PVPType": "http://www.opengis.net/cis/1.1/PVPType",
    "hasTelephone": {
      "@id": "vcard:hasTelephone",
      "@type": "@id"
    },
    "scaleFactor": {
      "@id": "https://w3id.org/iliad/oim/metadata/scaleFactor",
      "@type": "xsd:float"
    },
    "AllowedValues": "http://www.opengis.net/swe/2.0/AllowedValues",
    "DescribedSemantically": "https://w3id.org/idsa/core/DescribedSemantically",
    "isPartOf": "dct:isPartOf",
    "filenameExtension": {
      "@id": "https://w3id.org/idsa/core/filenameExtension",
      "@type": "xsd:string"
    },
    "project": "https://w3id.org/iliad/oim/metadata/project",
    "Concept": "skos:Concept",
    "component": {
      "@id": "http://purl.org/linked-data/cube#component",
      "@type": "@id"
    },
    "measure": {
      "@id": "http://purl.org/linked-data/cube#measure",
      "@type": "@id"
    },
    "gridLimits": {
      "@id": "http://www.opengis.net/cis/1.1/gridLimits",
      "@type": "@id"
    },
    "user": {
      "@id": "http://data.europa.eu/930/user",
      "@type": "@id"
    },
    "TextRepresentation": "https://w3id.org/idsa/core/TextRepresentation",
    "TextResource": "https://w3id.org/idsa/core/TextResource",
    "DataResource": "https://w3id.org/idsa/core/DataResource",
    "rangeSet": {
      "@id": "http://www.opengis.net/cis/1.1/rangeSet",
      "@type": "@id"
    },
    "idsa.Location": "https://w3id.org/idsa/core/Location",
    "rangeType": {
      "@id": "http://www.opengis.net/cis/1.1/rangeType",
      "@type": "@id"
    },
    "axisLabels": {
      "@id": "http://www.opengis.net/cis/1.1/axisLabels",
      "@type": "xsd:string"
    },
    "path": {
      "@id": "https://w3id.org/idsa/core/path",
      "@type": "xsd:string"
    },
    "interpolationRestriction": {
      "@id": "http://www.opengis.net/cis/1.1/interpolationRestriction",
      "@type": "@id"
    },
    "axis": {
      "@id": "http://www.opengis.net/cis/1.1/axis",
      "@type": "@id"
    },
    "ImageResource": "https://w3id.org/idsa/core/ImageResource",
    "spatialResolutionInMeters": "dcat:spatialResolutionInMeters",
    "partition": {
      "@id": "http://www.opengis.net/cis/1.1/partition",
      "@type": "@id"
    },
    "fn": {
      "@id": "vcard:fn",
      "@type": "xsd:string"
    },
    "CoverageByPartitioningType": "http://www.opengis.net/cis/1.1/CoverageByPartitioningType",
    "GeneralGridCoverageType": "http://www.opengis.net/cis/1.1/GeneralGridCoverageType",
    "homepage": {
      "@id": "foaf:homepage",
      "@type": "@id"
    },
    "maxValue": "https://w3id.org/iliad/oim/metadata/maxValue",
    "sensorModelRef": {
      "@id": "http://www.sensorml.com/sensorML-2.0/sensorModelRef",
      "@type": "@id"
    },
    "Axis": "http://www.opengis.net/cis/1.1/Axis",
    "appliedModel": {
      "@id": "https://w3id.org/iliad/oim/metadata/appliedModel",
      "@type": "xsd:string"
    },
    "hasQualityMeasurement": {
      "@id": "http://www.w3.org/ns/dqv#hasQualityMeasurement",
      "@type": "@id"
    },
    "Graph": "http://www.w3.org/2004/03/trix/rdfg-1/Graph",
    "unitsDescription": {
      "@id": "https://w3id.org/iliad/oim/metadata/unitsDescription",
      "@type": "xsd:string"
    },
    "Artifact": "https://w3id.org/idsa/core/Artifact",
    "filters": {
      "@id": "https://w3id.org/iliad/oim/metadata/filters",
      "@type": "xsd:string"
    },
    "rightsHolder": "dct:rightsHolder",
    "noDataValue": {
      "@id": "https://w3id.org/iliad/oim/metadata/noDataValue",
      "@type": "xsd:string"
    },
    "QualityAnnotation": "http://www.w3.org/ns/dqv#QualityAnnotation",
    "searchText": {
      "@id": "https://w3id.org/iliad/oim/metadata/searchText",
      "@type": "xsd:string"
    },
    "notation": "skos:notation",
    "Participant": "https://w3id.org/idsa/core/Participant",
    "profileSchema": {
      "@id": "https://w3id.org/iliad/oim/metadata/profileSchema",
      "@type": "xsd:string"
    },
    "Described": "https://w3id.org/idsa/core/Described",
    "coverageRef": {
      "@id": "http://www.opengis.net/cis/1.1/coverageRef",
      "@type": "@id"
    },
    "dct.Agent": "dct:Agent",
    "prov.Agent": "prov:Agent",
    "ContentType": "https://w3id.org/idsa/core/ContentType",
    "creator": "dct:creator",
    "swe.name": "http://www.opengis.net/swe/2.0/name",
    "dataBlock": {
      "@id": "http://www.opengis.net/cis/1.1/dataBlock",
      "@type": "@id"
    },
    "DataService": "dcat:DataService",
    "Individual": "vcard:Individual",
    "representation": {
      "@id": "https://w3id.org/idsa/core/representation",
      "@type": "@id"
    },
    "minDate": {
      "@id": "https://w3id.org/iliad/oim/metadata/minDate",
      "@type": "xsd:dateTimeStamp"
    },
    "interval": {
      "@id": "http://www.opengis.net/swe/2.0/interval",
      "@type": "@id"
    },
    "uomLabel": {
      "@id": "http://www.opengis.net/cis/1.1/uomLabel",
      "@type": "xsd:string"
    },
    "schemaAgency": {
      "@id": "http://www.w3.org/ns/adms#schemaAgency",
      "@type": "rdfs:Literal"
    },
    "RangeSetType": "http://www.opengis.net/cis/1.1/RangeSetType",
    "allowedInterpolation": {
      "@id": "http://www.opengis.net/cis/1.1/allowedInterpolation",
      "@type": "xsd:anyURI"
    },
    "ComponentSpecification": "http://purl.org/linked-data/cube#ComponentSpecification",
    "axisLabel": {
      "@id": "http://www.opengis.net/cis/1.1/axisLabel",
      "@type": "xsd:string"
    },
    "Work": "vcard:Work",
    "TemporalEntity": "w3ctime:TemporalEntity",
    "DataRecordType": "http://www.opengis.net/swe/2.0/DataRecordType",
    "IrregularAxisType": "http://www.opengis.net/cis/1.1/IrregularAxisType",
    "field": {
      "@id": "http://www.opengis.net/swe/2.0/field",
      "@type": "@id"
    },
    "PartitionSetType": "http://www.opengis.net/cis/1.1/PartitionSetType",
    "identifier": "dct:identifier",
    "adms.identifier": {
      "@id": "http://www.w3.org/ns/adms#identifier",
      "@type": "@id"
    },
    "keyword": {
      "@id": "dcat:keyword",
      "@type": "rdfs:Literal"
    },
    "envelope": {
      "@id": "http://www.opengis.net/cis/1.1/envelope",
      "@type": "@id"
    },
    "processor": {
      "@id": "http://data.europa.eu/930/processor",
      "@type": "@id"
    },
    "endpointInformation": {
      "@id": "https://w3id.org/idsa/core/endpointInformation",
      "@type": "xsd:string"
    },
    "subject": "dct:subject",
    "fileName": {
      "@id": "https://w3id.org/idsa/core/fileName",
      "@type": "xsd:string"
    },
    "qualifiedRelation": {
      "@id": "dcat:qualifiedRelation",
      "@type": "@id"
    },
    "metadata": {
      "@id": "http://www.opengis.net/cis/1.1/metadata",
      "@type": "@id"
    },
    "byteSize": "dcat:byteSize",
    "idsa.byteSize": {
      "@id": "https://w3id.org/idsa/core/byteSize",
      "@type": "xsd:integer"
    },
    "instance": {
      "@id": "https://w3id.org/idsa/core/instance",
      "@type": "@id"
    },
    "isDefinedBy": "rdfs:isDefinedBy",
    "definition": "skos:definition",
    "swe.definition": {
      "@id": "http://www.opengis.net/swe/2.0/definition",
      "@type": "xsd:string"
    },
    "RangeSetRefType": "http://www.opengis.net/cis/1.1/RangeSetRefType",
    "srsName": {
      "@id": "http://www.opengis.net/cis/1.1/srsName",
      "@type": "xsd:anyURI"
    },
    "principalInvestigator": {
      "@id": "http://data.europa.eu/930/principalInvestigator",
      "@type": "@id"
    },
    "QuantityType": "http://www.opengis.net/swe/2.0/QuantityType",
    "technicalManagerInfo": {
      "@id": "https://w3id.org/iliad/oim/metadata/technicalManagerInfo",
      "@type": "xsd:string"
    },
    "colorTable": {
      "@id": "https://w3id.org/iliad/oim/metadata/colorTable",
      "@type": "xsd:string"
    },
    "names": {
      "@id": "http://www.opengis.net/swe/2.0/names",
      "@type": "xsd:string"
    },
    "Property": "rdf:Property",
    "dataType": {
      "@id": "https://w3id.org/idsa/core/dataType",
      "@type": "xsd:anyURI"
    },
    "source": "dct:source",
    "MeasureProperty": "http://purl.org/linked-data/cube#MeasureProperty",
    "publisher": "dct:publisher",
    "mediaType": "dct:mediaType",
    "uom": {
      "@id": "http://www.opengis.net/swe/2.0/uom",
      "@type": "@id"
    },
    "subDatasetName": "https://w3id.org/iliad/oim/metadata/subDatasetName",
    "upperBound": {
      "@id": "http://www.opengis.net/cis/1.1/upperBound",
      "@type": "xsd:integer"
    },
    "version": "dcat:version",
    "modified": "dct:modified",
    "Frequency": "dct:Frequency",
    "idsa.Frequency": "https://w3id.org/idsa/core/Frequency",
    "Endpoint": "https://w3id.org/idsa/core/Endpoint",
    "endpointURL": {
      "@id": "dcat:endpointURL",
      "@type": "@id"
    },
    "provenance": "dct:provenance",
    "samplingRate": {
      "@id": "https://w3id.org/idsa/core/samplingRate",
      "@type": "xsd:decimal"
    },
    "CoverageByDomainAndRangeType": "http://www.opengis.net/cis/1.1/CoverageByDomainAndRangeType",
    "inSeries": {
      "@id": "dcat:inSeries",
      "@type": "@id"
    },
    "endpointDocumentation": {
      "@id": "https://w3id.org/idsa/core/endpointDocumentation",
      "@type": "xsd:anyURI"
    },
    "distributor": {
      "@id": "http://data.europa.eu/930/distributor",
      "@type": "@id"
    },
    "accessRights": "dct:accessRights",
    "DCMIType": "dct:DCMIType",
    "wasUsedBy": {
      "@id": "prov:wasUsedBy",
      "@type": "@id"
    },
    "checkSum": {
      "@id": "https://w3id.org/idsa/core/checkSum",
      "@type": "xsd:string"
    },
    "seeAlso": "rdfs:seeAlso",
    "contentType": {
      "@id": "https://w3id.org/idsa/core/contentType",
      "@type": "@id"
    },
    "RepresentationInstance": "https://w3id.org/idsa/core/RepresentationInstance",
    "partitionSet": {
      "@id": "http://www.opengis.net/cis/1.1/partitionSet",
      "@type": "@id"
    },
    "datasetManagerInfo": {
      "@id": "https://w3id.org/iliad/oim/metadata/datasetManagerInfo",
      "@type": "xsd:string"
    },
    "contentStandard": {
      "@id": "https://w3id.org/idsa/core/contentStandard",
      "@type": "xsd:anyURI"
    },
    "dataTypeSchema": {
      "@id": "https://w3id.org/idsa/core/dataTypeSchema",
      "@type": "@id"
    },
    "Language": "https://w3id.org/idsa/core/Language",
    "resourceProvider": {
      "@id": "http://data.europa.eu/930/resourceProvider",
      "@type": "@id"
    },
    "contactPoint": {
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "Resource": "dcat:Resource",
    "idsa.Resource": "https://w3id.org/idsa/core/Resource",
    "rdfs.Resource": "rdfs:Resource",
    "hasQualityAnnotation": {
      "@id": "http://www.w3.org/ns/dqv#hasQualityAnnotation",
      "@type": "@id"
    },
    "domainSet": {
      "@id": "http://www.opengis.net/cis/1.1/domainSet",
      "@type": "@id"
    },
    "SpatialThing": "http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing",
    "theme": {
      "@id": "dcat:theme",
      "@type": "@id"
    },
    "Party": "http://www.w3.org/ns/odrl/2/Party",
    "comment": "rdfs:comment",
    "custodian": {
      "@id": "http://data.europa.eu/930/custodian",
      "@type": "@id"
    },
    "Document": "foaf:Document",
    "page": {
      "@id": "foaf:page",
      "@type": "@id"
    },
    "Group": "foaf:Group",
    "TransformationBySensorModelType": "http://www.opengis.net/cis/1.1/TransformationBySensorModelType",
    "uomLabels": {
      "@id": "http://www.opengis.net/cis/1.1/uomLabels",
      "@type": "xsd:string"
    },
    "contributor": "dct:contributor",
    "originator": {
      "@id": "http://data.europa.eu/930/originator",
      "@type": "@id"
    },
    "resolutionUnit": {
      "@id": "https://w3id.org/iliad/oim/metadata/resolutionUnit",
      "@type": "xsd:string"
    },
    "AudioResource": "https://w3id.org/idsa/core/AudioResource",
    "DisplacementAxisNestType": "http://www.opengis.net/cis/1.1/DisplacementAxisNestType",
    "DomainSetType": "http://www.opengis.net/cis/1.1/DomainSetType",
    "generalizationOf": {
      "@id": "prov:generalizationOf",
      "@type": "@id"
    },
    "displacement": {
      "@id": "http://www.opengis.net/cis/1.1/displacement",
      "@type": "@id"
    },
    "minValue": "https://w3id.org/iliad/oim/metadata/minValue",
    "UnitReference": "http://www.opengis.net/swe/2.0/UnitReference",
    "code": {
      "@id": "http://www.opengis.net/swe/2.0/code",
      "@type": "xsd:string"
    },
    "Identifier": "http://www.w3.org/ns/adms#Identifier",
    "epsg": {
      "@id": "https://w3id.org/iliad/oim/metadata/epsg",
      "@type": "xsd:string"
    },
    "Home": "vcard:Home",
    "ManagedEntity": "https://w3id.org/idsa/core/ManagedEntity",
    "format": "dct:format",
    "accessURL": {
      "@id": "dcat:accessURL",
      "@type": "@id"
    },
    "credits": {
      "@id": "https://w3id.org/iliad/oim/metadata/credits",
      "@type": "xsd:string"
    },
    "sample": {
      "@id": "http://www.w3.org/ns/adms#sample",
      "@type": "@id"
    },
    "BoundingPolygon": "https://w3id.org/idsa/core/BoundingPolygon",
    "Kind": "vcard:Kind",
    "relation": "dct:relation",
    "temporal": "dct:temporal",
    "accrualPolicy": "dct:accrualPolicy",
    "resolution": {
      "@id": "http://www.opengis.net/cis/1.1/resolution",
      "@type": "xsd:string"
    },
    "maxDate": {
      "@id": "https://w3id.org/iliad/oim/metadata/maxDate",
      "@type": "xsd:dateTimeStamp"
    },
    "constraint": {
      "@id": "http://www.opengis.net/swe/2.0/constraint",
      "@type": "@id"
    },
    "ConnectorEndpoint": "https://w3id.org/idsa/core/ConnectorEndpoint",
    "DataStructureDefinition": "http://purl.org/linked-data/cube#DataStructureDefinition",
    "numberOfRecords": {
      "@id": "https://w3id.org/iliad/oim/metadata/numberOfRecords",
      "@type": "xsd:integer"
    },
    "RegularAxisType": "http://www.opengis.net/cis/1.1/RegularAxisType",
    "PhotonFluxDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#PhotonFluxDensity",
    "implements": {
      "@id": "http://www.w3.org/ns/ssn/implements",
      "@type": "@id"
    },
    "Attachable": "http://purl.org/linked-data/cube#Attachable",
    "QuantityValue": "qudt:QuantityValue",
    "Line": "http://www.opengis.net/ont/sf#Line",
    "member": {
      "@id": "foaf:member",
      "@type": "@id"
    },
    "example": "skos:example",
    "Slice": "http://purl.org/linked-data/cube#Slice",
    "Concentration": "http://purl.oclc.org/NET/ssnx/qu/dim#Concentration",
    "dataSet": {
      "@id": "http://purl.org/linked-data/cube#dataSet",
      "@type": "@id"
    },
    "componentAttachment": {
      "@id": "http://purl.org/linked-data/cube#componentAttachment",
      "@type": "@id"
    },
    "Platform": "http://www.w3.org/ns/sosa/Platform",
    "Deployment": "http://www.w3.org/ns/ssn/Deployment",
    "MultiSurface": "http://www.opengis.net/ont/sf#MultiSurface",
    "TemporalDuration": "w3ctime:TemporalDuration",
    "Procedure": "http://www.w3.org/ns/sosa/Procedure",
    "DiffusionCoefficient": "http://purl.oclc.org/NET/ssnx/qu/dim#DiffusionCoefficient",
    "asGeoJSON": {
      "@id": "http://www.opengis.net/ont/geosparql#asGeoJSON",
      "@type": "http://www.opengis.net/ont/geosparql#geoJSONLiteral"
    },
    "Volume": "http://purl.oclc.org/NET/ssnx/qu/dim#Volume",
    "Thing": "owl:Thing",
    "GFI_Feature": "http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_Feature",
    "AttributeProperty": "http://purl.org/linked-data/cube#AttributeProperty",
    "quantityValue": {
      "@id": "qudt:quantityValue",
      "@type": "@id"
    },
    "TemporalUnit": "w3ctime:TemporalUnit",
    "hosts": {
      "@id": "http://www.w3.org/ns/sosa/hosts",
      "@type": "@id"
    },
    "asWKT": {
      "@id": "http://www.opengis.net/ont/geosparql#asWKT",
      "@type": "http://www.opengis.net/ont/geosparql#wktLiteral"
    },
    "hasOutput": {
      "@id": "http://www.w3.org/ns/ssn/hasOutput",
      "@type": "@id"
    },
    "Angle": "http://purl.oclc.org/NET/ssnx/qu/dim#Angle",
    "TemperatureDrift": "http://purl.oclc.org/NET/ssnx/qu/dim#TemperatureDrift",
    "RotationalSpeed": "http://purl.oclc.org/NET/ssnx/qu/dim#RotationalSpeed",
    "FeatureOfInterest": "http://www.w3.org/ns/sosa/FeatureOfInterest",
    "Class": "rdfs:Class",
    "ObservationCollection": "http://www.w3.org/ns/sosa/ObservationCollection",
    "NumberPerArea": "http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerArea",
    "depiction": "foaf:depiction",
    "Curve": "http://www.opengis.net/ont/sf#Curve",
    "Instant": "w3ctime:Instant",
    "sfWithin": {
      "@id": "http://www.opengis.net/ont/geosparql#sfWithin",
      "@type": "@id"
    },
    "hasBoundingBox": {
      "@id": "http://www.opengis.net/ont/geosparql#hasBoundingBox",
      "@type": "@id"
    },
    "ThermalConductivity": "http://purl.oclc.org/NET/ssnx/qu/dim#ThermalConductivity",
    "hasUltimateFeatureOfInterest": {
      "@id": "http://www.w3.org/ns/sosa/hasUltimateFeatureOfInterest",
      "@type": "@id"
    },
    "domainIncludes": "https://schema.org/domainIncludes",
    "madeBySensor": {
      "@id": "http://www.w3.org/ns/sosa/madeBySensor",
      "@type": "@id"
    },
    "long": "http://www.w3.org/2003/01/geo/wgs84_pos#long",
    "ActuatableProperty": "http://www.w3.org/ns/sosa/ActuatableProperty",
    "numericValue": "qudt:numericValue",
    "attribute": {
      "@id": "http://purl.org/linked-data/cube#attribute",
      "@type": "@id"
    },
    "SliceKey": "http://purl.org/linked-data/cube#SliceKey",
    "Result": "http://www.w3.org/ns/sosa/Result",
    "isHostedBy": {
      "@id": "http://www.w3.org/ns/sosa/isHostedBy",
      "@type": "@id"
    },
    "Compressibility": "http://purl.oclc.org/NET/ssnx/qu/dim#Compressibility",
    "inDeployment": {
      "@id": "http://www.w3.org/ns/ssn/inDeployment",
      "@type": "@id"
    },
    "ComponentSet": "http://purl.org/linked-data/cube#ComponentSet",
    "MassPerTimePerArea": "http://purl.oclc.org/NET/ssnx/qu/dim#MassPerTimePerArea",
    "numericDuration": {
      "@id": "w3ctime:numericDuration",
      "@type": "xsd:decimal"
    },
    "ElectricConductivity": "http://purl.oclc.org/NET/ssnx/qu/dim#ElectricConductivity",
    "Temperature": "http://purl.oclc.org/NET/ssnx/qu/dim#Temperature",
    "hasProperty": {
      "@id": "http://www.w3.org/ns/ssn/hasProperty",
      "@type": "@id"
    },
    "Measure": "http://def.seegrid.csiro.au/isotc211/iso19103/2005/basic#Measure",
    "Triangle": "http://www.opengis.net/ont/sf#Triangle",
    "note": "skos:note",
    "observationGroup": {
      "@id": "http://purl.org/linked-data/cube#observationGroup",
      "@type": "@id"
    },
    "Interval": "w3ctime:Interval",
    "EnergyFlux": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyFlux",
    "StressOrPressure": "http://purl.oclc.org/NET/ssnx/qu/dim#StressOrPressure",
    "resultTime": {
      "@id": "http://www.w3.org/ns/sosa/resultTime",
      "@type": "xsd:dateTime"
    },
    "VolumeDensityRate": "http://purl.oclc.org/NET/ssnx/qu/dim#VolumeDensityRate",
    "phenomenonTime": {
      "@id": "http://www.w3.org/ns/sosa/phenomenonTime",
      "@type": "@id"
    },
    "Energy": "http://purl.oclc.org/NET/ssnx/qu/dim#Energy",
    "foaf.name": "foaf:name",
    "hasSerialization": {
      "@id": "http://www.opengis.net/ont/geosparql#hasSerialization",
      "@type": "rdfs:Literal"
    },
    "hasTime": {
      "@id": "w3ctime:hasTime",
      "@type": "@id"
    },
    "SF_SamplingFeature.sampledFeature": {
      "@id": "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature.sampledFeature",
      "@type": "@id"
    },
    "hasMember": {
      "@id": "http://www.w3.org/ns/sosa/hasMember",
      "@type": "@id"
    },
    "rangeIncludes": "https://schema.org/rangeIncludes",
    "hasInput": {
      "@id": "http://www.w3.org/ns/ssn/hasInput",
      "@type": "@id"
    },
    "Mass": "http://purl.oclc.org/NET/ssnx/qu/dim#Mass",
    "implementedBy": {
      "@id": "http://www.w3.org/ns/ssn/implementedBy",
      "@type": "@id"
    },
    "location": {
      "@id": "http://www.w3.org/2003/01/geo/wgs84_pos#location",
      "@type": "@id"
    },
    "Scheme": "skos:Scheme",
    "hasEnd": {
      "@id": "w3ctime:hasEnd",
      "@type": "@id"
    },
    "hasBeginning": {
      "@id": "w3ctime:hasBeginning",
      "@type": "@id"
    },
    "isResultOf": {
      "@id": "http://www.w3.org/ns/sosa/isResultOf",
      "@type": "@id"
    },
    "SF_SamplingFeature": "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature",
    "DimensionProperty": "http://purl.org/linked-data/cube#DimensionProperty",
    "alt": "http://www.w3.org/2003/01/geo/wgs84_pos#alt",
    "Acceleration": "http://purl.oclc.org/NET/ssnx/qu/dim#Acceleration",
    "hasSubSystem": {
      "@id": "http://www.w3.org/ns/ssn/hasSubSystem",
      "@type": "@id"
    },
    "Quantity": "qudt:Quantity",
    "MassFlowRate": "http://purl.oclc.org/NET/ssnx/qu/dim#MassFlowRate",
    "qu.QuantityKind": "http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind",
    "SpatialObjectCollection": "http://www.opengis.net/ont/geosparql#SpatialObjectCollection",
    "Distance": "http://purl.oclc.org/NET/ssnx/qu/dim#Distance",
    "deprecated": "owl:deprecated",
    "Radiance": "http://purl.oclc.org/NET/ssnx/qu/dim#Radiance",
    "Duration": "w3ctime:Duration",
    "TIN": "http://www.opengis.net/ont/sf#TIN",
    "SurfaceDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#SurfaceDensity",
    "wgs84.Point": "http://www.w3.org/2003/01/geo/wgs84_pos#Point",
    "editorialNote": "skos:editorialNote",
    "observes": {
      "@id": "http://www.w3.org/ns/sosa/observes",
      "@type": "@id"
    },
    "hasDeployment": {
      "@id": "http://www.w3.org/ns/ssn/hasDeployment",
      "@type": "@id"
    },
    "hasResult": {
      "@id": "http://www.w3.org/ns/sosa/hasResult",
      "@type": "@id"
    },
    "order": {
      "@id": "http://purl.org/linked-data/cube#order",
      "@type": "xsd:int"
    },
    "hasGeometry": {
      "@id": "http://www.opengis.net/ont/geosparql#hasGeometry",
      "@type": "@id"
    },
    "usedProcedure": {
      "@id": "http://www.w3.org/ns/sosa/usedProcedure",
      "@type": "@id"
    },
    "ssn.Property": "http://www.w3.org/ns/ssn/Property",
    "sfContains": {
      "@id": "http://www.opengis.net/ont/geosparql#sfContains",
      "@type": "@id"
    },
    "Density": "http://purl.oclc.org/NET/ssnx/qu/dim#Density",
    "LinearRing": "http://www.opengis.net/ont/sf#LinearRing",
    "Molality": "http://purl.oclc.org/NET/ssnx/qu/dim#Molality",
    "inXSDDateTimeStamp": {
      "@id": "w3ctime:inXSDDateTimeStamp",
      "@type": "xsd:dateTimeStamp"
    },
    "PropertyKind": "http://purl.oclc.org/NET/ssnx/qu/qu#PropertyKind",
    "SpatialObject": "http://www.opengis.net/ont/geosparql#SpatialObject",
    "sliceStructure": {
      "@id": "http://purl.org/linked-data/cube#sliceStructure",
      "@type": "@id"
    },
    "hasFeatureOfInterest": {
      "@id": "http://www.w3.org/ns/sosa/hasFeatureOfInterest",
      "@type": "@id"
    },
    "NumberPerLength": "http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerLength",
    "lat": "http://www.w3.org/2003/01/geo/wgs84_pos#lat",
    "VolumeFlowRate": "http://purl.oclc.org/NET/ssnx/qu/dim#VolumeFlowRate",
    "SpecificEntropy": "http://purl.oclc.org/NET/ssnx/qu/dim#SpecificEntropy",
    "CodedProperty": "http://purl.org/linked-data/cube#CodedProperty",
    "observedProperty": {
      "@id": "http://www.w3.org/ns/sosa/observedProperty",
      "@type": "@id"
    },
    "slice": {
      "@id": "http://purl.org/linked-data/cube#slice",
      "@type": "@id"
    },
    "madeObservation": {
      "@id": "http://www.w3.org/ns/sosa/madeObservation",
      "@type": "@id"
    },
    "date": "dct:date",
    "isPropertyOf": {
      "@id": "http://www.w3.org/ns/ssn/isPropertyOf",
      "@type": "@id"
    },
    "ObservationGroup": "http://purl.org/linked-data/cube#ObservationGroup",
    "Sample": "http://www.w3.org/ns/sosa/Sample",
    "DataSet": "http://purl.org/linked-data/cube#DataSet",
    "PolyhedralSurface": "http://www.opengis.net/ont/sf#PolyhedralSurface",
    "ObservableProperty": "http://www.w3.org/ns/sosa/ObservableProperty",
    "deployedSystem": {
      "@id": "http://www.w3.org/ns/ssn/deployedSystem",
      "@type": "@id"
    },
    "System": "http://www.w3.org/ns/ssn/System",
    "unitKind": {
      "@id": "http://purl.oclc.org/NET/ssnx/qu/qu#unitKind",
      "@type": "@id"
    },
    "dimension": {
      "@id": "http://purl.org/linked-data/cube#dimension",
      "@type": "@id"
    },
    "RadianceExposure": "http://purl.oclc.org/NET/ssnx/qu/dim#RadianceExposure",
    "VelocityOrSpeed": "http://purl.oclc.org/NET/ssnx/qu/dim#VelocityOrSpeed",
    "deployedOnPlatform": {
      "@id": "http://www.w3.org/ns/ssn/deployedOnPlatform",
      "@type": "@id"
    },
    "inXSDDate": {
      "@id": "w3ctime:inXSDDate",
      "@type": "xsd:date"
    },
    "GFI_DomainFeature": "http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_DomainFeature",
    "Actuation": "http://www.w3.org/ns/sosa/Actuation",
    "observation": {
      "@id": "http://purl.org/linked-data/cube#observation",
      "@type": "@id"
    },
    "Dimensionless": "http://purl.oclc.org/NET/ssnx/qu/dim#Dimensionless",
    "Area": "http://purl.oclc.org/NET/ssnx/qu/dim#Area",
    "Sampling": "http://www.w3.org/ns/sosa/Sampling",
    "Power": "http://purl.oclc.org/NET/ssnx/qu/dim#Power",
    "OM_Observation": "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation",
    "prefLabel": "skos:prefLabel",
    "Surface": "http://www.opengis.net/ont/sf#Surface",
    "sliceKey": {
      "@id": "http://purl.org/linked-data/cube#sliceKey",
      "@type": "@id"
    },
    "inScheme": "skos:inScheme",
    "dct.description": "dct:description",
    "MultiCurve": "http://www.opengis.net/ont/sf#MultiCurve",
    "hasQuantityKind": {
      "@id": "qudt:hasQuantityKind",
      "@type": "@id"
    },
    "qb.Observation": "http://purl.org/linked-data/cube#Observation",
    "EnergyDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyDensity",
    "Sensor": "http://www.w3.org/ns/sosa/Sensor",
    "hasSimpleResult": "http://www.w3.org/ns/sosa/hasSimpleResult",
    "unitType": {
      "@id": "w3ctime:unitType",
      "@type": "@id"
    },
    "componentProperty": {
      "@id": "http://purl.org/linked-data/cube#componentProperty",
      "@type": "@id"
    },
    "isFeatureOfInterestOf": {
      "@id": "http://www.w3.org/ns/sosa/isFeatureOfInterestOf",
      "@type": "@id"
    },
    "sf.Geometry": "http://www.opengis.net/ont/sf#Geometry",
    "schema.Person": "https://schema.org/Person",
    "Observation": "http://www.w3.org/ns/sosa/Observation",
    "schema.name": "https://schema.org/name",
    "QuantityKind": "qudt:QuantityKind",
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
    },
    "role": "seadots:role",
    "convention": "seadots:metadataConvention",
    "derivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@container": "@set",
      "@type": "@id"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "rec": "https://www.opengis.net/def/ogc-api/records/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "w3ctime": "http://www.w3.org/2006/time#",
    "dctype": "http://purl.org/dc/dcmitype/",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "prov": "http://www.w3.org/ns/prov#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "thns": "https://w3id.org/ogc/stac/themes/",
    "stac": "https://w3id.org/ogc/stac/core/",
    "cf": "https://stac-extensions.github.io/cf/v0.2.0/schema.json#",
    "seadots": "https://w3id.org/ogc/hosted/seadots/catalog#",
    "dcterms": "http://purl.org/dc/terms/",
    "qudt": "http://qudt.org/schema/qudt/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data-multidim/context.jsonld)

## Sources

* [SeaDOTs Interoperability Framework - Catalog Metadata Model](https://github.com/ogcincubator/bblocks-seadots)
* [ILIAD STAC/DCAT dimensional data building block](https://ogcincubator.github.io/iliad-apis-features/bblock/ogc.hosted.iliad.api.features.stac_multidim_data)
* [OGC API - Records](https://docs.ogc.org/is/20-004/20-004.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/catalog-data-multidim`

