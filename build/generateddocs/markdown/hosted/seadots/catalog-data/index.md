
# SeaDOTs Catalog Data (Schema)

`ogc.hosted.seadots.catalog-data` *v0.1*

Generic Records/DCAT, STAC Item, CF, and provenance profile for SeaDOTs catalog records that describe data artefacts independent of their workflow role or data type.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# SeaDOTs Catalog Data

Generic Records/DCAT and STAC Item profile for SeaDOTs catalog records that describe data artefacts. It composes the EarthCODE common GeoDCAT/STAC profile, the STAC CF extension, and the STAC Item provenance profile, then adds only SeaDOTs terms that are shared by data records regardless of workflow role or data type.

This block is the shared base for catalog input records, catalog output records, and data-type-specific records such as multidimensional data. Input/output status is represented by `properties.role` (`input` or `output`) and provenance links such as `derived_from` or `via`, not by separate building blocks.

`ogc.osc.geodcat-stac-earthcode.products` was considered as a single import, but it constrains `type` to `Collection`. SeaDOTs catalog input and output records are STAC Items (`type: Feature`), so this block imports `ogc.osc.geodcat-stac-earthcode.common` instead and adds the Item/CF/provenance contracts explicitly.

## Composition

| Concern | Source |
| --- | --- |
| Records/DCAT and GeoDCAT-STAC common profile | `bblocks://ogc.osc.geodcat-stac-earthcode.common` |
| STAC Item plus PROV-O provenance | `bblocks://ogc.contrib.stac.item-prov` |
| CF metadata extension | `bblocks://ogc.contrib.stac.extensions.cf` |
| SeaDOTs shared data-record terms | Local `schema.yaml` |

## Roles

| Role | Meaning |
| --- | --- |
| `data` | Generic data artefact without a workflow-specific role. |
| `input` | Data artefact consumed by an execution or workflow. |
| `output` | Data artefact produced by an execution or workflow. |

## Examples

### SeaDOTs Catalog Data
#### json
```json
{
  "id": "seadots-generic-data-item",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          4.7,
          59.1
        ],
        [
          5.0,
          59.1
        ],
        [
          5.0,
          59.4
        ],
        [
          4.7,
          59.4
        ],
        [
          4.7,
          59.1
        ]
      ]
    ]
  },
  "bbox": [
    4.7,
    59.1,
    5.0,
    59.4
  ],
  "properties": {
    "title": "SeaDOTs generic data item",
    "description": "Generic catalog data item used to demonstrate the shared SeaDOTs data profile.",
    "datetime": "2026-06-10T00:00:00Z",
    "role": "data",
    "convention": "CF-1.10",
    "license": "CC-BY-4.0",
    "cf:parameter": [
      {
        "name": "sea_water_temperature",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "K",
        "description": "Example CF-style parameter declaration."
      }
    ]
  },
  "assets": {
    "data": {
      "href": "https://example.org/seadots/catalog-data.nc",
      "type": "application/x-netcdf",
      "title": "Generic data asset",
      "cf:parameter": [
        {
          "name": "sea_water_temperature",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "K",
          "description": "Example CF-style parameter declaration."
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
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data/context.jsonld",
  "id": "seadots-generic-data-item",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          4.7,
          59.1
        ],
        [
          5.0,
          59.1
        ],
        [
          5.0,
          59.4
        ],
        [
          4.7,
          59.4
        ],
        [
          4.7,
          59.1
        ]
      ]
    ]
  },
  "bbox": [
    4.7,
    59.1,
    5.0,
    59.4
  ],
  "properties": {
    "title": "SeaDOTs generic data item",
    "description": "Generic catalog data item used to demonstrate the shared SeaDOTs data profile.",
    "datetime": "2026-06-10T00:00:00Z",
    "role": "data",
    "convention": "CF-1.10",
    "license": "CC-BY-4.0",
    "cf:parameter": [
      {
        "name": "sea_water_temperature",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "K",
        "description": "Example CF-style parameter declaration."
      }
    ]
  },
  "assets": {
    "data": {
      "href": "https://example.org/seadots/catalog-data.nc",
      "type": "application/x-netcdf",
      "title": "Generic data asset",
      "cf:parameter": [
        {
          "name": "sea_water_temperature",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "K",
          "description": "Example CF-style parameter declaration."
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
    }
  ]
}
```

#### ttl
```ttl
@prefix cf: <https://stac-extensions.github.io/cf/v0.2.0/schema.json#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <https://w3id.org/ogc/stac/cf/> .
@prefix ns2: <https://w3id.org/ogc/stac/assets/> .
@prefix ns3: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/seadots-generic-data-item> a geojson:Feature ;
    dcterms:date "2026-06-10T00:00:00+00:00"^^xsd:dateTime ;
    dcterms:description "Generic catalog data item used to demonstrate the shared SeaDOTs data profile." ;
    dcterms:license "CC-BY-4.0" ;
    dcterms:title "SeaDOTs generic data item" ;
    rdfs:seeAlso [ rdfs:label "SeaDOTs Catalog Data bblock" ;
            dcterms:type "application/schema+json" ;
            ns3:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-data> ] ;
    geojson:bbox ( 4.7e+00 5.91e+01 5e+00 5.94e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 4.7e+00 5.91e+01 ) ( 5e+00 5.91e+01 ) ( 5e+00 5.94e+01 ) ( 4.7e+00 5.94e+01 ) ( 4.7e+00 5.91e+01 ) ) ) ] ;
    cf:parameter [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "Example CF-style parameter declaration." ;
            qudt:hasUnit "K" ;
            ns1:name "sea_water_temperature" ] ;
    seadots:itemType "record" ;
    seadots:metadataConvention "CF-1.10" ;
    seadots:role "data" ;
    stac:hasAsset [ ns2:data <https://example.org/seadots/catalog-data.nc> ] ;
    stac:hasExtension "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
        "https://stac-extensions.github.io/prov/v1.0.0/schema.json" ;
    stac:version "1.0.0" .

<https://example.org/seadots/catalog-data.nc> dcterms:format "application/x-netcdf" ;
    dcterms:title "Generic data asset" ;
    cf:parameter [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "Example CF-style parameter declaration." ;
            qudt:hasUnit "K" ;
            ns1:name "sea_water_temperature" ] ;
    stac:hasAssetroles "data"^^xsd:string .


```


### SeaDOTs Catalog Data Input
#### json
```json
{
  "id": "aoi-utsira",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "collection": "seadots-inputs",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [4.7, 59.1],
        [5.0, 59.1],
        [5.0, 59.4],
        [4.7, 59.4],
        [4.7, 59.1]
      ]
    ]
  },
  "bbox": [4.7, 59.1, 5.0, 59.4],
  "properties": {
    "title": "Utsira area of interest",
    "description": "Example area-of-interest input for a SeaDOTs execution.",
    "datetime": "2026-05-26T00:00:00Z",
    "role": "input",
    "convention": "CF-1.10",
    "cf:parameter": [
      {
        "name": "area",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "m2",
        "description": "Optional CF-style parameter declaration for spatial input extent."
      }
    ]
  },
  "assets": {
    "data": {
      "href": "../../area-of-interest/examples/utsira_surroundings_aoi.json",
      "type": "application/geo+json",
      "title": "Utsira surroundings AOI",
      "cf:parameter": [
        {
          "name": "area",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "m2",
          "description": "Optional CF-style parameter declaration for spatial input extent."
        }
      ],
      "roles": ["data", "input"]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "https://w3id.org/ogc/hosted/seadots/catalog/collections/seadots-inputs",
      "type": "application/json",
      "title": "SeaDOTs inputs"
    },
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data",
      "type": "application/schema+json"
    },
    {
      "rel": "item",
      "href": "bblocks://ogc.hosted.seadots.area-of-interest/examples/utsira_surroundings_aoi.json",
      "type": "application/geo+json",
      "title": "Utsira surroundings AOI"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data/context.jsonld",
  "id": "aoi-utsira",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "collection": "seadots-inputs",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          4.7,
          59.1
        ],
        [
          5.0,
          59.1
        ],
        [
          5.0,
          59.4
        ],
        [
          4.7,
          59.4
        ],
        [
          4.7,
          59.1
        ]
      ]
    ]
  },
  "bbox": [
    4.7,
    59.1,
    5.0,
    59.4
  ],
  "properties": {
    "title": "Utsira area of interest",
    "description": "Example area-of-interest input for a SeaDOTs execution.",
    "datetime": "2026-05-26T00:00:00Z",
    "role": "input",
    "convention": "CF-1.10",
    "cf:parameter": [
      {
        "name": "area",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "m2",
        "description": "Optional CF-style parameter declaration for spatial input extent."
      }
    ]
  },
  "assets": {
    "data": {
      "href": "../../area-of-interest/examples/utsira_surroundings_aoi.json",
      "type": "application/geo+json",
      "title": "Utsira surroundings AOI",
      "cf:parameter": [
        {
          "name": "area",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "m2",
          "description": "Optional CF-style parameter declaration for spatial input extent."
        }
      ],
      "roles": [
        "data",
        "input"
      ]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "https://w3id.org/ogc/hosted/seadots/catalog/collections/seadots-inputs",
      "type": "application/json",
      "title": "SeaDOTs inputs"
    },
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data",
      "type": "application/schema+json"
    },
    {
      "rel": "item",
      "href": "bblocks://ogc.hosted.seadots.area-of-interest/examples/utsira_surroundings_aoi.json",
      "type": "application/geo+json",
      "title": "Utsira surroundings AOI"
    }
  ]
}
```

#### ttl
```ttl
@prefix cf: <https://stac-extensions.github.io/cf/v0.2.0/schema.json#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <https://w3id.org/ogc/stac/assets/> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix ns3: <https://w3id.org/ogc/stac/cf/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/aoi-utsira> a geojson:Feature ;
    dcterms:date "2026-05-26T00:00:00+00:00"^^xsd:dateTime ;
    dcterms:description "Example area-of-interest input for a SeaDOTs execution." ;
    dcterms:title "Utsira area of interest" ;
    rdfs:seeAlso [ rdfs:label "Utsira surroundings AOI" ;
            dcterms:type "application/geo+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.area-of-interest/examples/utsira_surroundings_aoi.json> ],
        [ rdfs:label "SeaDOTs inputs" ;
            dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://w3id.org/ogc/hosted/seadots/catalog/collections/seadots-inputs> ],
        [ dcterms:type "application/schema+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-data> ] ;
    geojson:bbox ( 4.7e+00 5.91e+01 5e+00 5.94e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 4.7e+00 5.91e+01 ) ( 5e+00 5.91e+01 ) ( 5e+00 5.94e+01 ) ( 4.7e+00 5.94e+01 ) ( 4.7e+00 5.91e+01 ) ) ) ] ;
    cf:parameter [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "Optional CF-style parameter declaration for spatial input extent." ;
            qudt:hasUnit "m2" ;
            ns3:name "area" ] ;
    seadots:collection "seadots-inputs" ;
    seadots:itemType "record" ;
    seadots:metadataConvention "CF-1.10" ;
    seadots:role "input" ;
    stac:hasAsset [ ns1:data <file:///area-of-interest/examples/utsira_surroundings_aoi.json> ] ;
    stac:hasExtension "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
        "https://stac-extensions.github.io/prov/v1.0.0/schema.json" ;
    stac:version "1.0.0" .

<file:///area-of-interest/examples/utsira_surroundings_aoi.json> dcterms:format "application/geo+json" ;
    dcterms:title "Utsira surroundings AOI" ;
    cf:parameter [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "Optional CF-style parameter declaration for spatial input extent." ;
            qudt:hasUnit "m2" ;
            ns3:name "area" ] ;
    stac:hasAssetroles "data"^^xsd:string,
        "input"^^xsd:string .


```


### SeaDOTs Catalog Data Output
#### json
```json
{
  "id": "reef-biomass-result",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "collection": "seadots-outputs",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [4.7, 59.1],
        [5.0, 59.1],
        [5.0, 59.4],
        [4.7, 59.4],
        [4.7, 59.1]
      ]
    ]
  },
  "bbox": [4.7, 59.1, 5.0, 59.4],
  "properties": {
    "title": "Reef biomass result",
    "description": "Example output product generated by a SeaDOTs execution.",
    "datetime": "2026-05-26T09:03:00Z",
    "role": "output",
    "convention": "CF-1.10",
    "cf:parameter": [
      {
        "name": "biomass",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "kg",
        "description": "Optional CF-style parameter declaration for the output quantity."
      }
    ],
    "derivedFrom": [
      "https://w3id.org/ogc/hosted/seadots/catalog/input/aoi-utsira"
    ]
  },
  "assets": {
    "data": {
      "href": "../../reef-effect-output/examples/reef_biomass_result.json",
      "type": "application/geo+json",
      "title": "Reef biomass structured result",
      "cf:parameter": [
        {
          "name": "biomass",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "kg",
          "description": "Optional CF-style parameter declaration for the output quantity."
        }
      ],
      "roles": ["data", "result"]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "https://w3id.org/ogc/hosted/seadots/catalog/collections/seadots-outputs",
      "type": "application/json",
      "title": "SeaDOTs outputs"
    },
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data",
      "type": "application/schema+json"
    },
    {
      "rel": "item",
      "href": "bblocks://ogc.hosted.seadots.reef-effect-output/examples/reef_biomass_result.json",
      "type": "application/geo+json",
      "title": "Reef biomass structured result"
    },
    {
      "rel": "derived_from",
      "href": "https://w3id.org/ogc/hosted/seadots/catalog/input/aoi-utsira"
    },
    {
      "rel": "via",
      "href": "https://w3id.org/ogc/hosted/seadots/catalog/execution/reef-effect-run-001"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data/context.jsonld",
  "id": "reef-biomass-result",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "collection": "seadots-outputs",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          4.7,
          59.1
        ],
        [
          5.0,
          59.1
        ],
        [
          5.0,
          59.4
        ],
        [
          4.7,
          59.4
        ],
        [
          4.7,
          59.1
        ]
      ]
    ]
  },
  "bbox": [
    4.7,
    59.1,
    5.0,
    59.4
  ],
  "properties": {
    "title": "Reef biomass result",
    "description": "Example output product generated by a SeaDOTs execution.",
    "datetime": "2026-05-26T09:03:00Z",
    "role": "output",
    "convention": "CF-1.10",
    "cf:parameter": [
      {
        "name": "biomass",
        "schema": "http://vocab.nerc.ac.uk/standard_name/",
        "unit": "kg",
        "description": "Optional CF-style parameter declaration for the output quantity."
      }
    ],
    "derivedFrom": [
      "https://w3id.org/ogc/hosted/seadots/catalog/input/aoi-utsira"
    ]
  },
  "assets": {
    "data": {
      "href": "../../reef-effect-output/examples/reef_biomass_result.json",
      "type": "application/geo+json",
      "title": "Reef biomass structured result",
      "cf:parameter": [
        {
          "name": "biomass",
          "schema": "http://vocab.nerc.ac.uk/standard_name/",
          "unit": "kg",
          "description": "Optional CF-style parameter declaration for the output quantity."
        }
      ],
      "roles": [
        "data",
        "result"
      ]
    }
  },
  "links": [
    {
      "rel": "collection",
      "href": "https://w3id.org/ogc/hosted/seadots/catalog/collections/seadots-outputs",
      "type": "application/json",
      "title": "SeaDOTs outputs"
    },
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data",
      "type": "application/schema+json"
    },
    {
      "rel": "item",
      "href": "bblocks://ogc.hosted.seadots.reef-effect-output/examples/reef_biomass_result.json",
      "type": "application/geo+json",
      "title": "Reef biomass structured result"
    },
    {
      "rel": "derived_from",
      "href": "https://w3id.org/ogc/hosted/seadots/catalog/input/aoi-utsira"
    },
    {
      "rel": "via",
      "href": "https://w3id.org/ogc/hosted/seadots/catalog/execution/reef-effect-run-001"
    }
  ]
}
```

#### ttl
```ttl
@prefix cf: <https://stac-extensions.github.io/cf/v0.2.0/schema.json#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <https://w3id.org/ogc/stac/cf/> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix ns3: <https://w3id.org/ogc/stac/assets/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/reef-biomass-result> a geojson:Feature ;
    dcterms:date "2026-05-26T09:03:00+00:00"^^xsd:dateTime ;
    dcterms:description "Example output product generated by a SeaDOTs execution." ;
    dcterms:title "Reef biomass result" ;
    rdfs:seeAlso [ ns2:relation <http://www.iana.org/assignments/relation/derived_from> ;
            oa:hasTarget <https://w3id.org/ogc/hosted/seadots/catalog/input/aoi-utsira> ],
        [ ns2:relation <http://www.iana.org/assignments/relation/via> ;
            oa:hasTarget <https://w3id.org/ogc/hosted/seadots/catalog/execution/reef-effect-run-001> ],
        [ dcterms:type "application/schema+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-data> ],
        [ rdfs:label "Reef biomass structured result" ;
            dcterms:type "application/geo+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.reef-effect-output/examples/reef_biomass_result.json> ],
        [ rdfs:label "SeaDOTs outputs" ;
            dcterms:type "application/json" ;
            ns2:relation <http://www.iana.org/assignments/relation/collection> ;
            oa:hasTarget <https://w3id.org/ogc/hosted/seadots/catalog/collections/seadots-outputs> ] ;
    prov:wasDerivedFrom <https://w3id.org/ogc/hosted/seadots/catalog/input/aoi-utsira> ;
    geojson:bbox ( 4.7e+00 5.91e+01 5e+00 5.94e+01 ) ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 4.7e+00 5.91e+01 ) ( 5e+00 5.91e+01 ) ( 5e+00 5.94e+01 ) ( 4.7e+00 5.94e+01 ) ( 4.7e+00 5.91e+01 ) ) ) ] ;
    cf:parameter [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "Optional CF-style parameter declaration for the output quantity." ;
            qudt:hasUnit "kg" ;
            ns1:name "biomass" ] ;
    seadots:collection "seadots-outputs" ;
    seadots:itemType "record" ;
    seadots:metadataConvention "CF-1.10" ;
    seadots:role "output" ;
    stac:hasAsset [ ns3:data <file:///reef-effect-output/examples/reef_biomass_result.json> ] ;
    stac:hasExtension "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
        "https://stac-extensions.github.io/prov/v1.0.0/schema.json" ;
    stac:version "1.0.0" .

<file:///reef-effect-output/examples/reef_biomass_result.json> dcterms:format "application/geo+json" ;
    dcterms:title "Reef biomass structured result" ;
    cf:parameter [ dcterms:conformsTo <http://vocab.nerc.ac.uk/standard_name/> ;
            dcterms:description "Optional CF-style parameter declaration for the output quantity." ;
            qudt:hasUnit "kg" ;
            ns1:name "biomass" ] ;
    stac:hasAssetroles "data"^^xsd:string,
        "result"^^xsd:string .


```


### Harvest time-series scenario catalog example
#### json
```json
{
  "id": "harvest-timeseries-scen-m3-catalog-item",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      [7.64260227, 54.39245755],
      [7.6640575066666665, 54.399025196666663],
      [7.6800021166666665, 54.39909727]
    ]
  },
  "bbox": [
    7.64260227,
    54.39245755,
    7.6800021166666665,
    54.39909727
  ],
  "properties": {
    "title": "Harvest time series scenario Scen M3 sample catalog record",
    "description": "Catalog record for a SeaDOTs harvest scenario time-series sample containing point-based bwmus values over multiple timestamps.",
    "datetime": "2020-04-30T00:00:00Z",
    "role": "data",
    "convention": "CF-1.10",
    "license": "Not supplied",
    "keywords": [
      "harvest",
      "time-series",
      "scenario",
      "geojson"
    ]
  },
  "assets": {
    "data": {
      "href": "../../harvest-timeseries-scen-m3-source/examples/harvest-timeseries-scen-m3-sample.geojson",
      "type": "application/geo+json",
      "title": "Harvest time-series sample GeoJSON"
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data bblock"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data/context.jsonld",
  "id": "harvest-timeseries-scen-m3-catalog-item",
  "type": "Feature",
  "itemType": "record",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
    "https://stac-extensions.github.io/prov/v1.0.0/schema.json"
  ],
  "geometry": {
    "type": "MultiPoint",
    "coordinates": [
      [
        7.64260227,
        54.39245755
      ],
      [
        7.6640575066666665,
        54.39902519666666
      ],
      [
        7.6800021166666665,
        54.39909727
      ]
    ]
  },
  "bbox": [
    7.64260227,
    54.39245755,
    7.6800021166666665,
    54.39909727
  ],
  "properties": {
    "title": "Harvest time series scenario Scen M3 sample catalog record",
    "description": "Catalog record for a SeaDOTs harvest scenario time-series sample containing point-based bwmus values over multiple timestamps.",
    "datetime": "2020-04-30T00:00:00Z",
    "role": "data",
    "convention": "CF-1.10",
    "license": "Not supplied",
    "keywords": [
      "harvest",
      "time-series",
      "scenario",
      "geojson"
    ]
  },
  "assets": {
    "data": {
      "href": "../../harvest-timeseries-scen-m3-source/examples/harvest-timeseries-scen-m3-sample.geojson",
      "type": "application/geo+json",
      "title": "Harvest time-series sample GeoJSON"
    }
  },
  "links": [
    {
      "rel": "describedby",
      "href": "bblocks://ogc.hosted.seadots.catalog-data",
      "type": "application/schema+json",
      "title": "SeaDOTs Catalog Data bblock"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <https://w3id.org/ogc/stac/assets/> .
@prefix ns2: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/catalog#> .
@prefix stac: <https://w3id.org/ogc/stac/core/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/harvest-timeseries-scen-m3-catalog-item> a geojson:Feature ;
    dcterms:date "2020-04-30T00:00:00+00:00"^^xsd:dateTime ;
    dcterms:description "Catalog record for a SeaDOTs harvest scenario time-series sample containing point-based bwmus values over multiple timestamps." ;
    dcterms:license "Not supplied" ;
    dcterms:subject "geojson",
        "harvest",
        "scenario",
        "time-series" ;
    dcterms:title "Harvest time series scenario Scen M3 sample catalog record" ;
    rdfs:seeAlso [ rdfs:label "SeaDOTs Catalog Data bblock" ;
            dcterms:type "application/schema+json" ;
            ns2:relation <http://www.iana.org/assignments/relation/describedby> ;
            oa:hasTarget <bblocks://ogc.hosted.seadots.catalog-data> ] ;
    geojson:bbox ( 7.642602e+00 5.439246e+01 7.680002e+00 5.43991e+01 ) ;
    geojson:geometry [ a geojson:MultiPoint ;
            geojson:coordinates ( ( 7.642602e+00 5.439246e+01 ) ( 7.664058e+00 5.439903e+01 ) ( 7.680002e+00 5.43991e+01 ) ) ] ;
    seadots:itemType "record" ;
    seadots:metadataConvention "CF-1.10" ;
    seadots:role "data" ;
    stac:hasAsset [ ns1:data <file:///harvest-timeseries-scen-m3-source/examples/harvest-timeseries-scen-m3-sample.geojson> ] ;
    stac:hasExtension "https://stac-extensions.github.io/cf/v0.2.0/schema.json",
        "https://stac-extensions.github.io/prov/v1.0.0/schema.json" ;
    stac:version "1.0.0" .

<file:///harvest-timeseries-scen-m3-source/examples/harvest-timeseries-scen-m3-sample.geojson> dcterms:format "application/geo+json" ;
    dcterms:title "Harvest time-series sample GeoJSON" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SeaDOTs Catalog Data
description: 'Generic SeaDOTs catalog data profile. It composes the EarthCODE common
  GeoDCAT/STAC/Records profile, STAC Item provenance, and CF metadata support, then
  adds only SeaDOTs data-record terms shared by inputs, outputs, and data-type-specific
  profiles.

  '
allOf:
- $ref: https://ogcincubator.github.io/bblocks-openscience/build/annotated/osc/geodcat-stac-earthcode/common/schema.yaml
- $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/item-prov/schema.yaml
- $ref: https://ogcincubator.github.io/bblocks-stac/build/annotated/contrib/stac/extensions/cf/schema.yaml
type: object
required:
- type
- itemType
- properties
properties:
  type:
    const: Feature
    x-jsonld-id: '@type'
  itemType:
    const: record
  properties:
    type: object
    required:
    - title
    - description
    - datetime
    properties:
      role:
        type: string
        enum:
        - data
        - input
        - output
        description: Data role in a SeaDOTs catalog or workflow context.
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#role
      convention:
        type: string
        description: Optional metadata convention declaration, e.g. CF-1.10.
        x-jsonld-id: https://w3id.org/ogc/hosted/seadots/catalog#metadataConvention
      derivedFrom:
        type: array
        description: Source data records or artefacts from which this data item was
          derived.
        items:
          type: string
          format: uri-reference
        x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
        x-jsonld-container: '@set'
        x-jsonld-type: '@id'
    additionalProperties: true
    x-jsonld-id: '@nest'
  links:
    type: array
    items:
      type: object
      properties:
        rel:
          type: string
          description: Link relation, including workflow-neutral data links and role-specific
            input/output provenance links.
          x-jsonld-id: http://www.iana.org/assignments/relation
          x-jsonld-type: '@id'
          x-jsonld-base: http://www.iana.org/assignments/relation/
        href:
          type: string
          format: uri-reference
          x-jsonld-type: '@id'
          x-jsonld-id: http://www.w3.org/ns/oa#hasTarget
    contains:
      type: object
      required:
      - rel
      - href
      properties:
        rel:
          const: describedby
          x-jsonld-id: http://www.iana.org/assignments/relation
          x-jsonld-type: '@id'
          x-jsonld-base: http://www.iana.org/assignments/relation/
        href:
          const: bblocks://ogc.hosted.seadots.catalog-data
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
      '@vocab': https://w3id.org/ogc/stac/assets/
      href: '@id'
      type: http://purl.org/dc/terms/format
      roles:
        '@id': https://w3id.org/ogc/stac/core/hasAssetroles
        '@type': http://www.w3.org/2001/XMLSchema#string
        '@container': '@set'
    x-jsonld-id: https://w3id.org/ogc/stac/core/hasAsset
    x-jsonld-container: '@set'
  datetime:
    x-jsonld-id: http://purl.org/dc/terms/date
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  start_datetime:
    x-jsonld-id: https://w3id.org/ogc/stac/core/start_datetime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  end_datetime:
    x-jsonld-id: https://w3id.org/ogc/stac/core/end_datetime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  providers: https://w3id.org/ogc/stac/core/hasProvider
  stac_version: https://w3id.org/ogc/stac/core/version
  media_type: http://purl.org/dc/terms/format
  extent: http://purl.org/dc/terms/extent
  concepts:
    x-jsonld-id: https://w3id.org/ogc/stac/themes/concepts
    x-jsonld-container: '@set'
    x-jsonld-context:
      id: https://w3id.org/ogc/stac/themes/id
      title: https://w3id.org/ogc/stac/themes/name
      description: https://w3id.org/ogc/stac/themes/description
      url: '@id'
  scheme: https://w3id.org/ogc/stac/themes/scheme
  osc:type:
    x-jsonld-id: https://w3id.org/ogc/stac/osc/type
    x-jsonld-type: '@vocab'
    x-jsonld-context:
      project: https://w3id.org/ogc/stac/osc/project-type
      product: https://w3id.org/ogc/stac/osc/product-type
  osc:status:
    x-jsonld-id: https://w3id.org/ogc/stac/osc/status
    x-jsonld-type: '@vocab'
    x-jsonld-context:
      planned: https://w3id.org/ogc/stac/osc/planned
      ongoing: https://w3id.org/ogc/stac/osc/ongoing
      completed: https://w3id.org/ogc/stac/osc/completed
  osc:project:
    x-jsonld-id: https://w3id.org/ogc/stac/osc/project
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  osc:region:
    x-jsonld-id: https://w3id.org/ogc/stac/osc/region
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  osc:variables:
    x-jsonld-id: https://w3id.org/ogc/stac/osc/variables
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
    x-jsonld-container: '@set'
  osc:missions:
    x-jsonld-id: https://w3id.org/ogc/stac/osc/missions
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
    x-jsonld-container: '@set'
  osc:experiment:
    x-jsonld-id: https://w3id.org/ogc/stac/osc/experiment
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  osc:workflows:
    x-jsonld-id: https://w3id.org/ogc/stac/osc/workflows
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
    x-jsonld-container: '@set'
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
  generatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#generatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  invalidatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#invalidatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  value: http://www.w3.org/ns/prov#value
  qualifiedPrimarySource:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedPrimarySource
    x-jsonld-type: '@id'
  qualifiedQuotation:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedQuotation
    x-jsonld-type: '@id'
  qualifiedRevision:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedRevision
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
  Agent: http://www.w3.org/ns/prov#Agent
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
  Location: http://www.w3.org/ns/prov#Location
  Organization: http://www.w3.org/ns/prov#Organization
  Person: http://www.w3.org/ns/prov#Person
  Plan: http://www.w3.org/ns/prov#Plan
  PrimarySource: http://www.w3.org/ns/prov#PrimarySource
  Quotation: http://www.w3.org/ns/prov#Quotation
  Revision: http://www.w3.org/ns/prov#Revision
  Role: http://www.w3.org/ns/prov#Role
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
  startedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#startedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
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
  unit:
    x-jsonld-id: http://qudt.org/schema/qudt/hasUnit
    x-jsonld-context:
      '@base': http://qudt.org/vocab/unit/
  cf:parameter:
    x-jsonld-id: https://stac-extensions.github.io/cf/v0.2.0/schema.json#parameter
    x-jsonld-container: '@set'
  schema:
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
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
  osc: https://w3id.org/ogc/stac/osc/
  oa: http://www.w3.org/ns/oa#
  prov: http://www.w3.org/ns/prov#
  qudt: http://qudt.org/schema/qudt/
  cf: https://stac-extensions.github.io/cf/v0.2.0/schema.json#
  seadots: https://w3id.org/ogc/hosted/seadots/catalog#
  dcterms: http://purl.org/dc/terms/
  owl: http://www.w3.org/2002/07/owl#
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  w3ctime: http://www.w3.org/2006/time#
  dctype: http://purl.org/dc/dcmitype/
  vcard: http://www.w3.org/2006/vcard/ns#
  foaf: http://xmlns.com/foaf/0.1/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data/schema.yaml)


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
        "href": "@id",
        "type": "dct:format",
        "roles": {
          "@id": "stac:hasAssetroles",
          "@type": "xsd:string",
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
        "id": "thns:id",
        "title": "thns:name",
        "description": "thns:description",
        "url": "@id"
      }
    },
    "scheme": "thns:scheme",
    "osc:type": {
      "@id": "osc:type",
      "@type": "@vocab",
      "@context": {
        "project": "osc:project-type",
        "product": "osc:product-type"
      }
    },
    "osc:status": {
      "@id": "osc:status",
      "@type": "@vocab",
      "@context": {
        "planned": "osc:planned",
        "ongoing": "osc:ongoing",
        "completed": "osc:completed"
      }
    },
    "osc:project": {
      "@id": "osc:project",
      "@type": "xsd:string"
    },
    "osc:region": {
      "@id": "osc:region",
      "@type": "xsd:string"
    },
    "osc:variables": {
      "@id": "osc:variables",
      "@type": "xsd:string",
      "@container": "@set"
    },
    "osc:missions": {
      "@id": "osc:missions",
      "@type": "xsd:string",
      "@container": "@set"
    },
    "osc:experiment": {
      "@id": "osc:experiment",
      "@type": "xsd:string"
    },
    "osc:workflows": {
      "@id": "osc:workflows",
      "@type": "xsd:string",
      "@container": "@set"
    },
    "wasInfluencedBy": {
      "@context": {
        "name": "rdfs:label"
      },
      "@id": "prov:wasInfluencedBy",
      "@type": "@id"
    },
    "qualifiedInfluence": {
      "@context": {
        "influencer": {
          "@context": {
            "name": "rdfs:label"
          },
          "@id": "prov:influencer",
          "@type": "@id"
        },
        "activity": {
          "@context": {
            "name": "rdfs:label"
          },
          "@id": "prov:activity",
          "@type": "@id"
        },
        "agent": {
          "@context": {
            "name": "rdfs:label"
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
        "name": "rdfs:label"
      },
      "@id": "dct:provenance",
      "@type": "@id"
    },
    "wasGeneratedBy": {
      "@context": {
        "name": "rdfs:label"
      },
      "@id": "prov:wasGeneratedBy",
      "@type": "@id"
    },
    "wasAttributedTo": {
      "@context": {
        "name": "rdfs:label"
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
    "value": "prov:value",
    "qualifiedPrimarySource": {
      "@context": {
        "hadActivity": {
          "@context": {
            "wasAssociatedWith": {
              "@context": {
                "name": "rdfs:label"
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
                "name": "rdfs:label"
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
                "name": "rdfs:label"
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
                "name": "rdfs:label"
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
            "name": "rdfs:label"
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
    "Agent": "prov:Agent",
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
    "Location": "prov:Location",
    "Organization": "prov:Organization",
    "Person": "prov:Person",
    "Plan": "prov:Plan",
    "PrimarySource": "prov:PrimarySource",
    "Quotation": "prov:Quotation",
    "Revision": "prov:Revision",
    "Role": "prov:Role",
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
    "name": "https://w3id.org/ogc/stac/cf/name",
    "unit": {
      "@id": "qudt:hasUnit",
      "@context": {
        "@base": "http://qudt.org/vocab/unit/"
      }
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
    "href": {
      "@type": "@id",
      "@id": "oa:hasTarget"
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
    "osc": "https://w3id.org/ogc/stac/osc/",
    "qudt": "http://qudt.org/schema/qudt/",
    "cf": "https://stac-extensions.github.io/cf/v0.2.0/schema.json#",
    "seadots": "https://w3id.org/ogc/hosted/seadots/catalog#",
    "dcterms": "http://purl.org/dc/terms/",
    "role": "seadots:role",
    "convention": "seadots:metadataConvention",
    "derivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@container": "@set",
      "@type": "@id"
    },
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/catalog-data/context.jsonld)

## Sources

* [SeaDOTs Interoperability Framework - Catalog Metadata Model](https://github.com/ogcincubator/bblocks-seadots)
* [STAC CF extension building block](https://ogcincubator.github.io/bblocks-stac/bblock/ogc.contrib.stac.extensions.cf)
* [STAC Item provenance building block](https://ogcincubator.github.io/bblocks-stac/bblock/ogc.contrib.stac.item-prov)
* [EarthCODE common GeoDCAT/STAC profile](https://ogcincubator.github.io/bblocks-openscience/bblock/ogc.osc.geodcat-stac-earthcode.common)
* [EarthCODE products profile](https://ogcincubator.github.io/bblocks-openscience/bblock/ogc.osc.geodcat-stac-earthcode.products)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/catalog-data`

