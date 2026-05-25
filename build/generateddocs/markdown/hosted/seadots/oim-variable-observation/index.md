
# OIM Variable Observation (Schema)

`ogc.hosted.seadots.oim-variable-observation` *v0.1*

Schema profile for OIM/SOSA observations of SEADOTS variables and indicators, including numeric values mapped to observed-property IRIs from the OIM Variables building block.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# OIM Variable Observation

This building block profiles OIM/SOSA observations for SEADOTS variables and
indicators. It follows the generic OIM/SOSA observation pattern and adds a small
numeric result object for variable values.

The observed variable is carried by `observedProperty`. For reef-effect
demonstrators, a reef aggregation index value is represented by setting:

```json
"observedProperty": "indo:reef-aggregation-index"
```

The example in this block is a compact observation for a dimensionless reef
aggregation index at Utsira Nord. The numeric value is illustrative because no
source data payload was provided with the generation request.

## Examples

### Reef aggregation index variable observation
examples/reef-aggregation-index-observation.json

### Utsira reef aggregation index observation features
examples/utsira-reef-aggregation-index-observations.json
## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: OIM Variable Observation
description: 'OIM/SOSA observation profile for numeric variable and indicator values.
  The observedProperty field identifies the variable concept, such as indo:reef-aggregation-index,
  while hasResult carries the numeric value.

  '
$defs:
  GeoJSONPoint:
    type: object
    required:
    - type
    - coordinates
    properties:
      type:
        type: string
        const: Point
        x-jsonld-id: '@type'
      coordinates:
        type: array
        minItems: 2
        items:
          type: number
        x-jsonld-id: https://purl.org/geojson/vocab#coordinates
        x-jsonld-container: '@list'
      bbox:
        type: array
        items:
          type: number
  VariableObservationResult:
    type: object
    required:
    - value
    properties:
      type:
        oneOf:
        - type: string
        - type: array
          items:
            type: string
        x-jsonld-id: '@type'
      value:
        type: number
        x-jsonld-id: http://qudt.org/schema/qudt/numericValue
      unit:
        type: string
        format: uri-reference
        x-jsonld-id: http://qudt.org/schema/qudt/unit
        x-jsonld-type: '@id'
      taxon:
        type: string
        x-jsonld-id: https://schema.org/taxon
      taxonConcept:
        type: string
        format: uri-reference
        x-jsonld-id: https://schema.org/taxon
        x-jsonld-type: '@id'
      method:
        type: string
        x-jsonld-id: https://schema.org/measurementTechnique
      evidence:
        type: string
        format: uri-reference
        x-jsonld-id: https://schema.org/citation
        x-jsonld-type: '@id'
    additionalProperties: true
  OIMVariableObservationProps:
    type: object
    required:
    - observedProperty
    - hasResult
    properties:
      label:
        oneOf:
        - type: string
        - type: object
        x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#label
        x-jsonld-container: '@language'
      observedProperty:
        type: string
        format: uri-reference
        x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
        x-jsonld-type: '@id'
      hasResult:
        $ref: '#/$defs/VariableObservationResult'
        x-jsonld-id: http://www.w3.org/ns/sosa/hasResult
        x-jsonld-type: '@id'
      phenomenonTime:
        type: string
        format: date-time
        x-jsonld-id: http://www.w3.org/ns/sosa/phenomenonTime
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
      resultTime:
        type: string
        format: date-time
        x-jsonld-id: http://www.w3.org/ns/sosa/resultTime
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
    additionalProperties: true
  OIMVariableObservationFeature:
    type: object
    required:
    - type
    - geometry
    - properties
    properties:
      '@context': true
      '@id':
        type: string
        format: uri-reference
      id:
        type: string
        format: uri-reference
        x-jsonld-id: '@id'
      type:
        type: string
        const: Feature
        x-jsonld-id: '@type'
      geometry:
        oneOf:
        - type: 'null'
        - $ref: '#/$defs/GeoJSONPoint'
        x-jsonld-id: https://purl.org/geojson/vocab#geometry
      properties:
        $ref: '#/$defs/OIMVariableObservationProps'
        x-jsonld-id: '@nest'
      links:
        type: array
    additionalProperties: true
  OIMVariableObservationCollection:
    type: object
    required:
    - type
    - features
    properties:
      '@context': true
      '@id':
        type: string
        format: uri-reference
      id:
        type: string
        format: uri-reference
        x-jsonld-id: '@id'
      type:
        type: string
        const: FeatureCollection
        x-jsonld-id: '@type'
      features:
        type: array
        items:
          $ref: '#/$defs/OIMVariableObservationFeature'
      links:
        type: array
    additionalProperties: true
anyOf:
- $ref: '#/$defs/OIMVariableObservationProps'
- $ref: '#/$defs/OIMVariableObservationFeature'
- $ref: '#/$defs/OIMVariableObservationCollection'
x-jsonld-extra-terms:
  PhotonFluxDensity: http://purl.oclc.org/NET/ssnx/qu/dim#PhotonFluxDensity
  implements:
    x-jsonld-id: http://www.w3.org/ns/ssn/implements
    x-jsonld-type: '@id'
  invalidatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#invalidatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  MultiLineString: http://www.opengis.net/ont/sf#MultiLineString
  Attachable: http://purl.org/linked-data/cube#Attachable
  QuantityValue: http://qudt.org/schema/qudt/QuantityValue
  affiliation: https://schema.org/affiliation
  Unit: http://qudt.org/schema/qudt/Unit
  Line: http://www.opengis.net/ont/sf#Line
  member:
    x-jsonld-id: http://xmlns.com/foaf/0.1/member
    x-jsonld-type: '@id'
  versionInfo: http://www.w3.org/2002/07/owl#versionInfo
  generatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#generatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
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
  concept:
    x-jsonld-id: http://purl.org/linked-data/cube#concept
    x-jsonld-type: '@id'
  Deployment: http://www.w3.org/ns/ssn/Deployment
  MultiSurface: http://www.opengis.net/ont/sf#MultiSurface
  TemporalDuration: http://www.w3.org/2006/time#TemporalDuration
  Procedure: http://www.w3.org/ns/sosa/Procedure
  DiffusionCoefficient: http://purl.oclc.org/NET/ssnx/qu/dim#DiffusionCoefficient
  asGeoJSON:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#asGeoJSON
    x-jsonld-type: http://www.opengis.net/ont/geosparql#geoJSONLiteral
  Organization: https://schema.org/Organization
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
  ComponentProperty: http://purl.org/linked-data/cube#ComponentProperty
  Class: http://www.w3.org/2000/01/rdf-schema#Class
  ObservationCollection: http://www.w3.org/ns/sosa/ObservationCollection
  Geometry: http://www.opengis.net/ont/geosparql#Geometry
  NumberPerArea: http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerArea
  depiction: http://xmlns.com/foaf/0.1/depiction
  Curve: http://www.opengis.net/ont/sf#Curve
  Instant: http://www.w3.org/2006/time#Instant
  maker: http://xmlns.com/foaf/0.1/maker
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
  Feature: https://purl.org/geojson/vocab#Feature
  LineString: http://www.opengis.net/ont/sf#LineString
  numericValue: http://qudt.org/schema/qudt/numericValue
  Concept: http://www.w3.org/2004/02/skos/core#Concept
  component:
    x-jsonld-id: http://purl.org/linked-data/cube#component
    x-jsonld-type: '@id'
  measure:
    x-jsonld-id: http://purl.org/linked-data/cube#measure
    x-jsonld-type: '@id'
  attribute:
    x-jsonld-id: http://purl.org/linked-data/cube#attribute
    x-jsonld-type: '@id'
  structure:
    x-jsonld-id: http://purl.org/linked-data/cube#structure
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
  homepage: http://xmlns.com/foaf/0.1/homepage
  hasProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasProperty
    x-jsonld-type: '@id'
  Measure: http://def.seegrid.csiro.au/isotc211/iso19103/2005/basic#Measure
  Person: http://xmlns.com/foaf/0.1/Person
  Triangle: http://www.opengis.net/ont/sf#Triangle
  note: http://www.w3.org/2004/02/skos/core#note
  observationGroup:
    x-jsonld-id: http://purl.org/linked-data/cube#observationGroup
    x-jsonld-type: '@id'
  Interval: http://www.w3.org/2006/time#Interval
  EnergyFlux: http://purl.oclc.org/NET/ssnx/qu/dim#EnergyFlux
  StressOrPressure: http://purl.oclc.org/NET/ssnx/qu/dim#StressOrPressure
  VolumeDensityRate: http://purl.oclc.org/NET/ssnx/qu/dim#VolumeDensityRate
  Agent: http://xmlns.com/foaf/0.1/Agent
  creator: http://purl.org/dc/terms/creator
  Energy: http://purl.oclc.org/NET/ssnx/qu/dim#Energy
  foaf.name: http://xmlns.com/foaf/0.1/name
  Role: https://schema.org/Role
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
  ComponentSpecification: http://purl.org/linked-data/cube#ComponentSpecification
  Scheme: http://www.w3.org/2004/02/skos/core#Scheme
  hasEnd:
    x-jsonld-id: http://www.w3.org/2006/time#hasEnd
    x-jsonld-type: '@id'
  GeometryCollection: http://www.opengis.net/ont/sf#GeometryCollection
  rights: http://purl.org/dc/terms/rights
  TemporalEntity: http://www.w3.org/2006/time#TemporalEntity
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
  identifier: http://purl.org/dc/terms/identifier
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
  isDefinedBy: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
  wgs84.Point: http://www.w3.org/2003/01/geo/wgs84_pos#Point
  definition: http://www.w3.org/2004/02/skos/core#definition
  editorialNote: http://www.w3.org/2004/02/skos/core#editorialNote
  observes:
    x-jsonld-id: http://www.w3.org/ns/sosa/observes
    x-jsonld-type: '@id'
  hasDeployment:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasDeployment
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
  title: http://purl.org/dc/terms/title
  Density: http://purl.oclc.org/NET/ssnx/qu/dim#Density
  LinearRing: http://www.opengis.net/ont/sf#LinearRing
  Molality: http://purl.oclc.org/NET/ssnx/qu/dim#Molality
  inXSDDateTimeStamp:
    x-jsonld-id: http://www.w3.org/2006/time#inXSDDateTimeStamp
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTimeStamp
  MeasureProperty: http://purl.org/linked-data/cube#MeasureProperty
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
  slice:
    x-jsonld-id: http://purl.org/linked-data/cube#slice
    x-jsonld-type: '@id'
  madeObservation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
    x-jsonld-type: '@id'
  FeatureCollection: https://purl.org/geojson/vocab#FeatureCollection
  unit:
    x-jsonld-id: http://qudt.org/schema/qudt/unit
    x-jsonld-type: '@id'
  date: http://purl.org/dc/terms/date
  isPropertyOf:
    x-jsonld-id: http://www.w3.org/ns/ssn/isPropertyOf
    x-jsonld-type: '@id'
  seeAlso: http://www.w3.org/2000/01/rdf-schema#seeAlso
  ObservationGroup: http://purl.org/linked-data/cube#ObservationGroup
  Sample: http://www.w3.org/ns/sosa/Sample
  DataSet: http://purl.org/linked-data/cube#DataSet
  comment: http://www.w3.org/2000/01/rdf-schema#comment
  PolyhedralSurface: http://www.opengis.net/ont/sf#PolyhedralSurface
  Polygon: http://www.opengis.net/ont/sf#Polygon
  MultiPolygon: http://www.opengis.net/ont/sf#MultiPolygon
  ObservableProperty: http://www.w3.org/ns/sosa/ObservableProperty
  contributor: http://purl.org/dc/terms/contributor
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
  DataStructureDefinition: http://purl.org/linked-data/cube#DataStructureDefinition
  MultiPoint: http://www.opengis.net/ont/sf#MultiPoint
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
  Point: https://purl.org/geojson/vocab#Point
  schema.name: https://schema.org/name
  QuantityKind: http://qudt.org/schema/qudt/QuantityKind
  VariableObservationResult: https://w3id.org/iliad/oim/ext/variable-observation/VariableObservationResult
  coordinates:
    x-jsonld-id: https://purl.org/geojson/vocab#coordinates
    x-jsonld-container: '@list'
  value: http://qudt.org/schema/qudt/numericValue
  taxon: https://schema.org/taxon
  taxonConcept:
    x-jsonld-id: https://schema.org/taxon
    x-jsonld-type: '@id'
  method: https://schema.org/measurementTechnique
  evidence:
    x-jsonld-id: https://schema.org/citation
    x-jsonld-type: '@id'
x-jsonld-prefixes:
  qudt: http://qudt.org/schema/qudt/
  geojson: https://purl.org/geojson/vocab#
  sosa: http://www.w3.org/ns/sosa/
  schema: https://schema.org/
  indo: https://w3id.org/indicators/marine/obs/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/oim-variable-observation/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/oim-variable-observation/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "label": {
      "@id": "http://www.w3.org/2000/01/rdf-schema#label",
      "@container": "@language"
    },
    "observedProperty": {
      "@id": "sosa:observedProperty",
      "@type": "@id"
    },
    "hasResult": {
      "@id": "sosa:hasResult",
      "@type": "@id"
    },
    "phenomenonTime": {
      "@id": "sosa:phenomenonTime",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "resultTime": {
      "@id": "sosa:resultTime",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "id": "@id",
    "type": "@type",
    "geometry": "geojson:geometry",
    "properties": "@nest",
    "PhotonFluxDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#PhotonFluxDensity",
    "implements": {
      "@id": "http://www.w3.org/ns/ssn/implements",
      "@type": "@id"
    },
    "invalidatedAtTime": {
      "@id": "http://www.w3.org/ns/prov#invalidatedAtTime",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "MultiLineString": "http://www.opengis.net/ont/sf#MultiLineString",
    "Attachable": "http://purl.org/linked-data/cube#Attachable",
    "QuantityValue": "qudt:QuantityValue",
    "affiliation": "schema:affiliation",
    "Unit": "qudt:Unit",
    "Line": "http://www.opengis.net/ont/sf#Line",
    "member": {
      "@id": "http://xmlns.com/foaf/0.1/member",
      "@type": "@id"
    },
    "versionInfo": "http://www.w3.org/2002/07/owl#versionInfo",
    "generatedAtTime": {
      "@id": "http://www.w3.org/ns/prov#generatedAtTime",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "example": "http://www.w3.org/2004/02/skos/core#example",
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
    "Platform": "sosa:Platform",
    "concept": {
      "@id": "http://purl.org/linked-data/cube#concept",
      "@type": "@id"
    },
    "Deployment": "http://www.w3.org/ns/ssn/Deployment",
    "MultiSurface": "http://www.opengis.net/ont/sf#MultiSurface",
    "TemporalDuration": "http://www.w3.org/2006/time#TemporalDuration",
    "Procedure": "sosa:Procedure",
    "DiffusionCoefficient": "http://purl.oclc.org/NET/ssnx/qu/dim#DiffusionCoefficient",
    "asGeoJSON": {
      "@id": "http://www.opengis.net/ont/geosparql#asGeoJSON",
      "@type": "http://www.opengis.net/ont/geosparql#geoJSONLiteral"
    },
    "Organization": "schema:Organization",
    "Volume": "http://purl.oclc.org/NET/ssnx/qu/dim#Volume",
    "Thing": "http://www.w3.org/2002/07/owl#Thing",
    "GFI_Feature": "http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_Feature",
    "AttributeProperty": "http://purl.org/linked-data/cube#AttributeProperty",
    "quantityValue": {
      "@id": "qudt:quantityValue",
      "@type": "@id"
    },
    "TemporalUnit": "http://www.w3.org/2006/time#TemporalUnit",
    "hosts": {
      "@id": "sosa:hosts",
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
    "FeatureOfInterest": "sosa:FeatureOfInterest",
    "ComponentProperty": "http://purl.org/linked-data/cube#ComponentProperty",
    "Class": "http://www.w3.org/2000/01/rdf-schema#Class",
    "ObservationCollection": "sosa:ObservationCollection",
    "Geometry": "http://www.opengis.net/ont/geosparql#Geometry",
    "NumberPerArea": "http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerArea",
    "depiction": "http://xmlns.com/foaf/0.1/depiction",
    "Curve": "http://www.opengis.net/ont/sf#Curve",
    "Instant": "http://www.w3.org/2006/time#Instant",
    "maker": "http://xmlns.com/foaf/0.1/maker",
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
      "@id": "sosa:hasUltimateFeatureOfInterest",
      "@type": "@id"
    },
    "domainIncludes": "schema:domainIncludes",
    "madeBySensor": {
      "@id": "sosa:madeBySensor",
      "@type": "@id"
    },
    "long": "http://www.w3.org/2003/01/geo/wgs84_pos#long",
    "ActuatableProperty": "sosa:ActuatableProperty",
    "Feature": "geojson:Feature",
    "LineString": "http://www.opengis.net/ont/sf#LineString",
    "numericValue": "qudt:numericValue",
    "Concept": "http://www.w3.org/2004/02/skos/core#Concept",
    "component": {
      "@id": "http://purl.org/linked-data/cube#component",
      "@type": "@id"
    },
    "measure": {
      "@id": "http://purl.org/linked-data/cube#measure",
      "@type": "@id"
    },
    "attribute": {
      "@id": "http://purl.org/linked-data/cube#attribute",
      "@type": "@id"
    },
    "structure": {
      "@id": "http://purl.org/linked-data/cube#structure",
      "@type": "@id"
    },
    "SliceKey": "http://purl.org/linked-data/cube#SliceKey",
    "Result": "sosa:Result",
    "isHostedBy": {
      "@id": "sosa:isHostedBy",
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
      "@id": "http://www.w3.org/2006/time#numericDuration",
      "@type": "http://www.w3.org/2001/XMLSchema#decimal"
    },
    "ElectricConductivity": "http://purl.oclc.org/NET/ssnx/qu/dim#ElectricConductivity",
    "Temperature": "http://purl.oclc.org/NET/ssnx/qu/dim#Temperature",
    "homepage": "http://xmlns.com/foaf/0.1/homepage",
    "hasProperty": {
      "@id": "http://www.w3.org/ns/ssn/hasProperty",
      "@type": "@id"
    },
    "Measure": "http://def.seegrid.csiro.au/isotc211/iso19103/2005/basic#Measure",
    "Person": "http://xmlns.com/foaf/0.1/Person",
    "Triangle": "http://www.opengis.net/ont/sf#Triangle",
    "note": "http://www.w3.org/2004/02/skos/core#note",
    "observationGroup": {
      "@id": "http://purl.org/linked-data/cube#observationGroup",
      "@type": "@id"
    },
    "Interval": "http://www.w3.org/2006/time#Interval",
    "EnergyFlux": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyFlux",
    "StressOrPressure": "http://purl.oclc.org/NET/ssnx/qu/dim#StressOrPressure",
    "VolumeDensityRate": "http://purl.oclc.org/NET/ssnx/qu/dim#VolumeDensityRate",
    "Agent": "http://xmlns.com/foaf/0.1/Agent",
    "creator": "http://purl.org/dc/terms/creator",
    "Energy": "http://purl.oclc.org/NET/ssnx/qu/dim#Energy",
    "foaf.name": "http://xmlns.com/foaf/0.1/name",
    "Role": "schema:Role",
    "hasSerialization": {
      "@id": "http://www.opengis.net/ont/geosparql#hasSerialization",
      "@type": "http://www.w3.org/2000/01/rdf-schema#Literal"
    },
    "hasTime": {
      "@id": "http://www.w3.org/2006/time#hasTime",
      "@type": "@id"
    },
    "SF_SamplingFeature.sampledFeature": {
      "@id": "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature.sampledFeature",
      "@type": "@id"
    },
    "hasMember": {
      "@id": "sosa:hasMember",
      "@type": "@id"
    },
    "rangeIncludes": "schema:rangeIncludes",
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
    "ComponentSpecification": "http://purl.org/linked-data/cube#ComponentSpecification",
    "Scheme": "http://www.w3.org/2004/02/skos/core#Scheme",
    "hasEnd": {
      "@id": "http://www.w3.org/2006/time#hasEnd",
      "@type": "@id"
    },
    "GeometryCollection": "http://www.opengis.net/ont/sf#GeometryCollection",
    "rights": "http://purl.org/dc/terms/rights",
    "TemporalEntity": "http://www.w3.org/2006/time#TemporalEntity",
    "hasBeginning": {
      "@id": "http://www.w3.org/2006/time#hasBeginning",
      "@type": "@id"
    },
    "isResultOf": {
      "@id": "sosa:isResultOf",
      "@type": "@id"
    },
    "SF_SamplingFeature": "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature",
    "DimensionProperty": "http://purl.org/linked-data/cube#DimensionProperty",
    "alt": "http://www.w3.org/2003/01/geo/wgs84_pos#alt",
    "Acceleration": "http://purl.oclc.org/NET/ssnx/qu/dim#Acceleration",
    "identifier": "http://purl.org/dc/terms/identifier",
    "hasSubSystem": {
      "@id": "http://www.w3.org/ns/ssn/hasSubSystem",
      "@type": "@id"
    },
    "Quantity": "qudt:Quantity",
    "MassFlowRate": "http://purl.oclc.org/NET/ssnx/qu/dim#MassFlowRate",
    "qu.QuantityKind": "http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind",
    "SpatialObjectCollection": "http://www.opengis.net/ont/geosparql#SpatialObjectCollection",
    "Distance": "http://purl.oclc.org/NET/ssnx/qu/dim#Distance",
    "deprecated": "http://www.w3.org/2002/07/owl#deprecated",
    "Radiance": "http://purl.oclc.org/NET/ssnx/qu/dim#Radiance",
    "Duration": "http://www.w3.org/2006/time#Duration",
    "TIN": "http://www.opengis.net/ont/sf#TIN",
    "SurfaceDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#SurfaceDensity",
    "isDefinedBy": "http://www.w3.org/2000/01/rdf-schema#isDefinedBy",
    "wgs84.Point": "http://www.w3.org/2003/01/geo/wgs84_pos#Point",
    "definition": "http://www.w3.org/2004/02/skos/core#definition",
    "editorialNote": "http://www.w3.org/2004/02/skos/core#editorialNote",
    "observes": {
      "@id": "sosa:observes",
      "@type": "@id"
    },
    "hasDeployment": {
      "@id": "http://www.w3.org/ns/ssn/hasDeployment",
      "@type": "@id"
    },
    "order": {
      "@id": "http://purl.org/linked-data/cube#order",
      "@type": "http://www.w3.org/2001/XMLSchema#int"
    },
    "hasGeometry": {
      "@id": "http://www.opengis.net/ont/geosparql#hasGeometry",
      "@type": "@id"
    },
    "usedProcedure": {
      "@id": "sosa:usedProcedure",
      "@type": "@id"
    },
    "ssn.Property": "http://www.w3.org/ns/ssn/Property",
    "sfContains": {
      "@id": "http://www.opengis.net/ont/geosparql#sfContains",
      "@type": "@id"
    },
    "title": "http://purl.org/dc/terms/title",
    "Density": "http://purl.oclc.org/NET/ssnx/qu/dim#Density",
    "LinearRing": "http://www.opengis.net/ont/sf#LinearRing",
    "Molality": "http://purl.oclc.org/NET/ssnx/qu/dim#Molality",
    "inXSDDateTimeStamp": {
      "@id": "http://www.w3.org/2006/time#inXSDDateTimeStamp",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTimeStamp"
    },
    "MeasureProperty": "http://purl.org/linked-data/cube#MeasureProperty",
    "PropertyKind": "http://purl.oclc.org/NET/ssnx/qu/qu#PropertyKind",
    "SpatialObject": "http://www.opengis.net/ont/geosparql#SpatialObject",
    "sliceStructure": {
      "@id": "http://purl.org/linked-data/cube#sliceStructure",
      "@type": "@id"
    },
    "hasFeatureOfInterest": {
      "@id": "sosa:hasFeatureOfInterest",
      "@type": "@id"
    },
    "NumberPerLength": "http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerLength",
    "lat": "http://www.w3.org/2003/01/geo/wgs84_pos#lat",
    "VolumeFlowRate": "http://purl.oclc.org/NET/ssnx/qu/dim#VolumeFlowRate",
    "SpecificEntropy": "http://purl.oclc.org/NET/ssnx/qu/dim#SpecificEntropy",
    "CodedProperty": "http://purl.org/linked-data/cube#CodedProperty",
    "slice": {
      "@id": "http://purl.org/linked-data/cube#slice",
      "@type": "@id"
    },
    "madeObservation": {
      "@id": "sosa:madeObservation",
      "@type": "@id"
    },
    "FeatureCollection": "geojson:FeatureCollection",
    "unit": {
      "@id": "qudt:unit",
      "@type": "@id"
    },
    "date": "http://purl.org/dc/terms/date",
    "isPropertyOf": {
      "@id": "http://www.w3.org/ns/ssn/isPropertyOf",
      "@type": "@id"
    },
    "seeAlso": "http://www.w3.org/2000/01/rdf-schema#seeAlso",
    "ObservationGroup": "http://purl.org/linked-data/cube#ObservationGroup",
    "Sample": "sosa:Sample",
    "DataSet": "http://purl.org/linked-data/cube#DataSet",
    "comment": "http://www.w3.org/2000/01/rdf-schema#comment",
    "PolyhedralSurface": "http://www.opengis.net/ont/sf#PolyhedralSurface",
    "Polygon": "http://www.opengis.net/ont/sf#Polygon",
    "MultiPolygon": "http://www.opengis.net/ont/sf#MultiPolygon",
    "ObservableProperty": "sosa:ObservableProperty",
    "contributor": "http://purl.org/dc/terms/contributor",
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
      "@id": "http://www.w3.org/2006/time#inXSDDate",
      "@type": "http://www.w3.org/2001/XMLSchema#date"
    },
    "GFI_DomainFeature": "http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_DomainFeature",
    "Actuation": "sosa:Actuation",
    "observation": {
      "@id": "http://purl.org/linked-data/cube#observation",
      "@type": "@id"
    },
    "Dimensionless": "http://purl.oclc.org/NET/ssnx/qu/dim#Dimensionless",
    "Area": "http://purl.oclc.org/NET/ssnx/qu/dim#Area",
    "Sampling": "sosa:Sampling",
    "Power": "http://purl.oclc.org/NET/ssnx/qu/dim#Power",
    "OM_Observation": "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation",
    "prefLabel": "http://www.w3.org/2004/02/skos/core#prefLabel",
    "Surface": "http://www.opengis.net/ont/sf#Surface",
    "sliceKey": {
      "@id": "http://purl.org/linked-data/cube#sliceKey",
      "@type": "@id"
    },
    "inScheme": "http://www.w3.org/2004/02/skos/core#inScheme",
    "dct.description": "http://purl.org/dc/terms/description",
    "MultiCurve": "http://www.opengis.net/ont/sf#MultiCurve",
    "hasQuantityKind": {
      "@id": "qudt:hasQuantityKind",
      "@type": "@id"
    },
    "DataStructureDefinition": "http://purl.org/linked-data/cube#DataStructureDefinition",
    "MultiPoint": "http://www.opengis.net/ont/sf#MultiPoint",
    "qb.Observation": "http://purl.org/linked-data/cube#Observation",
    "EnergyDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyDensity",
    "Sensor": "sosa:Sensor",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "unitType": {
      "@id": "http://www.w3.org/2006/time#unitType",
      "@type": "@id"
    },
    "componentProperty": {
      "@id": "http://purl.org/linked-data/cube#componentProperty",
      "@type": "@id"
    },
    "isFeatureOfInterestOf": {
      "@id": "sosa:isFeatureOfInterestOf",
      "@type": "@id"
    },
    "sf.Geometry": "http://www.opengis.net/ont/sf#Geometry",
    "schema.Person": "schema:Person",
    "Observation": "sosa:Observation",
    "Point": "geojson:Point",
    "schema.name": "schema:name",
    "QuantityKind": "qudt:QuantityKind",
    "VariableObservationResult": "https://w3id.org/iliad/oim/ext/variable-observation/VariableObservationResult",
    "coordinates": {
      "@id": "geojson:coordinates",
      "@container": "@list"
    },
    "value": "qudt:numericValue",
    "taxon": "schema:taxon",
    "taxonConcept": {
      "@id": "schema:taxon",
      "@type": "@id"
    },
    "method": "schema:measurementTechnique",
    "evidence": {
      "@id": "schema:citation",
      "@type": "@id"
    },
    "qudt": "http://qudt.org/schema/qudt/",
    "geojson": "https://purl.org/geojson/vocab#",
    "sosa": "http://www.w3.org/ns/sosa/",
    "schema": "https://schema.org/",
    "indo": "https://w3id.org/indicators/marine/obs/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/oim-variable-observation/context.jsonld)

## Sources

* [OIM master repository](https://github.com/ILIAD-ocean-twin/OIM)
* [SEADOTS OIM Variables](bblocks://ogc.hosted.seadots.api.features.oim-variables)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/oim-variable-observation`

