
# OBIS MAREANO Checklist (Schema)

`ogc.hosted.seadots.obis-mareano-checklist` *v0.1*

Raw OBIS checklist response for selected MAREANO dataset identifiers. The example preserves the OBIS API payload as returned by the checklist endpoint and is used as source material for derived SeaDOTs biomass-density proxy examples.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### OBIS checklist for selected MAREANO datasets
#### json
```json
{"total":3196,"results":[{"scientificName":"Sipuncula","scientificNameAuthorship":"Stephen, 1965","taxonID":1268,"ncbi_id":6433,"wrims":true,"taxonRank":"Order","taxonomicStatus":"accepted","acceptedNameUsage":"Sipuncula","acceptedNameUsageID":1268,"is_marine":true,"is_brackish":true,"is_freshwater":false,"is_terrestrial":false,"kingdom":"Animalia","phylum":"Annelida","order":"Sipuncula","kingdomid":2,"phylumid":882,"orderid":1268,"records":459},{"scientificName":"Amphipoda","scientificNameAuthorship":"Latreille, 1816","taxonID":1135,"ncbi_id":6821,"wrims":true,"taxonRank":"Order","taxonomicStatus":"accepted","acceptedNameUsage":"Amphipoda","acceptedNameUsageID":1135,"is_marine":true,"is_brackish":true,"is_freshwater":true,"is_terrestrial":true,"kingdom":"Animalia","phylum":"Arthropoda","subphylum":"Crustacea","superclass":"Multicrustacea","class":"Malacostraca","subclass":"Eumalacostraca","superorder":"Peracarida","order":"Amphipoda","kingdomid":2,"phylumid":1065,"subphylumid":1066,"superclassid":845959,"classid":1071,"subclassid":1086,"superorderid":1090,"orderid":1135,"records":452},{"scientificName":"Aphelochaeta","scientificNameAuthorship":"Blake, 1991","taxonID":129240,"ncbi_id":394740,"wrims":true,"taxonRank":"Genus","taxonomicStatus":"accepted","acceptedNameUsage":"Aphelochaeta","acceptedNameUsageID":129240,"is_marine":true,"is_brackish":false,"is_freshwater":false,"is_terrestrial":false,"kingdom":"Animalia","phylum":"Annelida","class":"Polychaeta","subclass":"Sedentaria","infraclass":"Canalipalpata","order":"Terebellida","suborder":"Cirratuliformia","family":"Cirratulidae","genus":"Aphelochaeta","kingdomid":2,"phylumid":882,"classid":883,"subclassid":754175,"infraclassid":154974,"orderid":900,"suborderid":155087,"familyid":919,"genusid":129240,"records":432},{"scientificName":"Hydrozoa","scientificNameAuthorship":"Owen, 1843","taxonID":1337,"ncbi_id":6074,"wrims":true,"taxonRank":"Class","taxonomicStatus":"accepted","acceptedNameUsage":"Hydrozoa","acceptedNameUsageID":1337,"is_marine":true,"is_brackish":true,"is_freshwater":true,"is_terrestrial":false,"kingdom":"Animalia","phylum":"Cnidaria","subphylum":"Medusozoa","class":"Hydrozoa","kingdomid":2,"phylumid":1267,"subphylumid":1740301,"classid":1337,"records":429},{"scientificName":"Oedicerotidae","scientificNameAuthorship":"Lilljeborg, 1865","taxonID":101400,"ncbi_id":181113,"wrims":true,"taxonRank":"Family","taxonomicStatus":"accepted","acceptedNameUsage":"Oedicerotidae","acceptedNameUsageID":101400,"is_marine":true,"is_brackish":false,"is_freshwater":false,"is_terrestrial":false,"kingdom":"Animalia","phylum":"Arthropoda","subphylum":"Crustacea","superclass":"Multicrustacea","class":"Malacostraca","subclass":"Eumalacostraca","superorder":"Peracarida","order":"Amphipoda","suborder":"Amphilochidea","infraorder":"Amphilochida","parvorder":"Oedicerotidira","superfamily":"Oedicerotoidea","family":"Oedicerotidae","kingdomid":2,"phylumid":1065,"subphylumid":1066,"superclassid":845959,"classid":1071,"subclassid":1086,"superorderid":1090,"orderid":1135,"suborderid":1055678,"infraorderid":1055679,"parvorderid":1055682,"superfamilyid":1055683,"familyid":101400,"records":417},{"scientificName":"Notomastus latericeus","scientificNameAuthorship":"Sars, 1851","taxonID":129898,"ncbi_id":167831,"taxonRank":"Species","taxonomicStatus":"accepted","acceptedNameUsage":"Notomastus latericeus","acceptedNameUsageID":129898,"is_marine":true,"is_brackish":false,"is_freshwater":false,"is_terrestrial":false,"kingdom":"Animalia","phylum":"Annelida","class":"Polychaeta","subclass":"Sedentaria","infraclass":"Scolecida","family":"Capitellidae","genus":"Notomastus","species":"Notomastus latericeus","kingdomid":2,"phylumid":882,"classid":883,"subclassid":754175,"infraclassid":183607,"familyid":921,"genusid":129220,"speciesid":129898,"records":413},{"scientificName":"Cephalaspidea","scientificNameAuthorship":"P. Fischer, 1883","taxonID":154,"ncbi_id":69554,"wrims":true,"taxonRank":"Order","taxonomicStatus":"accepted","acceptedNameUsage":"Cephalaspidea","acceptedNameUsageID":154,"is_marine":true,"is_brackish":true,"is_freshwater":true,"kingdom":"Animalia","phylum":"Mollusca","class":"Gastropoda","subclass":"Heterobranchia","infraclass":"Euthyneura","subterclass":"Tectipleura","order":"Cephalaspidea","kingdomid":2,"phylumid":51,"classid":101,"subclassid":14712,"infraclassid":1057247,"subterclassid":1057250,"orderid":154,"records":410},{"scientificName":"Harpinia","scientificNameAuthorship":"Boeck, 1876","taxonID":101716,"ncbi_id":1732150,"taxonRank":"Genus","taxonomicStatus":"accepted","acceptedNameUsage":"Harpinia","acceptedNameUsageID":101716,"is_marine":true,"is_brackish":false,"is_freshwater":false,"is_terrestrial":false,"kingdom":"Animalia","phylum":"Arthropoda","subphylum":"Crustacea","superclass":"Multicrustacea","class":"Malacostraca","subclass":"Eumalacostraca","superorder":"Peracarida","order":"Amphipoda","suborder":"Amphilochidea","infraorder":"Lysianassida","parvorder":"Haustoriidira","superfamily":"Haustorioidea","family":"Phoxocephalidae","subfamily":"Harpiniinae","genus":"Harpinia","kingdomid":2,"phylumid":1065,"subphylumid":1066,"superclassid":845959,"classid":1071,"subclassid":1086,"superorderid":1090,"orderid":1135,"suborderid":1055678,"infraorderid":1055690,"parvorderid":1055694,"superfamilyid":1055695,"familyid":101403,"subfamilyid":176844,"genusid":101716,"records":403},{"scientificName":"Astarte sulcata","scientificNameAuthorship":"(da Costa, 1778)","taxonID":138824,"ncbi_id":462886,"taxonRank":"Species","taxonomicStatus":"accepted","acceptedNameUsage":"Astarte sulcata","acceptedNameUsageID":138824,"is_marine":true,"kingdom":"Animalia","phylum":"Mollusca","class":"Bivalvia","subclass":"Autobranchia","infraclass":"Heteroconchia","subterclass":"Archiheterodonta","order":"Carditida","superfamily":"Crassatelloidea","family":"Astartidae","subfamily":"Astartinae","genus":"Astarte","species":"Astarte sulcata","kingdomid":2,"phylumid":51,"classid":105,"subclassid":1424948,"infraclassid":1424949,"subterclassid":382255,"orderid":382256,"superfamilyid":23014,"familyid":228,"subfamilyid":1817149,"genusid":137683,"speciesid":138824,"records":388},{"scientificName":"Chone","scientificNameAuthorship":"Krøyer, 1856","taxonID":129525,"wrims":true,"taxonRank":"Genus","taxonomicStatus":"accepted","acceptedNameUsage":"Chone","acceptedNameUsageID":129525,"is_marine":true,"is_brackish":false,"is_freshwater":false,"is_terrestrial":false,"kingdom":"Animalia","phylum":"Annelida","class":"Polychaeta","subclass":"Sedentaria","infraclass":"Canalipalpata","order":"Sabellida","family":"Sabellidae","subfamily":"Myxicolinae","tribe":"Myxicolini","genus":"Chone","kingdomid":2,"phylumid":882,"classid":883,"subclassid":754175,"infraclassid":154974,"orderid":901,"familyid":985,"subfamilyid":1470421,"tribeid":1470460,"genusid":129525,"records":386}]}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/obis-mareano-checklist/context.jsonld",
  "total": 3196,
  "results": [
    {
      "scientificName": "Sipuncula",
      "scientificNameAuthorship": "Stephen, 1965",
      "taxonID": 1268,
      "ncbi_id": 6433,
      "wrims": true,
      "taxonRank": "Order",
      "taxonomicStatus": "accepted",
      "acceptedNameUsage": "Sipuncula",
      "acceptedNameUsageID": 1268,
      "is_marine": true,
      "is_brackish": true,
      "is_freshwater": false,
      "is_terrestrial": false,
      "kingdom": "Animalia",
      "phylum": "Annelida",
      "order": "Sipuncula",
      "kingdomid": 2,
      "phylumid": 882,
      "orderid": 1268,
      "records": 459
    },
    {
      "scientificName": "Amphipoda",
      "scientificNameAuthorship": "Latreille, 1816",
      "taxonID": 1135,
      "ncbi_id": 6821,
      "wrims": true,
      "taxonRank": "Order",
      "taxonomicStatus": "accepted",
      "acceptedNameUsage": "Amphipoda",
      "acceptedNameUsageID": 1135,
      "is_marine": true,
      "is_brackish": true,
      "is_freshwater": true,
      "is_terrestrial": true,
      "kingdom": "Animalia",
      "phylum": "Arthropoda",
      "subphylum": "Crustacea",
      "superclass": "Multicrustacea",
      "class": "Malacostraca",
      "subclass": "Eumalacostraca",
      "superorder": "Peracarida",
      "order": "Amphipoda",
      "kingdomid": 2,
      "phylumid": 1065,
      "subphylumid": 1066,
      "superclassid": 845959,
      "classid": 1071,
      "subclassid": 1086,
      "superorderid": 1090,
      "orderid": 1135,
      "records": 452
    },
    {
      "scientificName": "Aphelochaeta",
      "scientificNameAuthorship": "Blake, 1991",
      "taxonID": 129240,
      "ncbi_id": 394740,
      "wrims": true,
      "taxonRank": "Genus",
      "taxonomicStatus": "accepted",
      "acceptedNameUsage": "Aphelochaeta",
      "acceptedNameUsageID": 129240,
      "is_marine": true,
      "is_brackish": false,
      "is_freshwater": false,
      "is_terrestrial": false,
      "kingdom": "Animalia",
      "phylum": "Annelida",
      "class": "Polychaeta",
      "subclass": "Sedentaria",
      "infraclass": "Canalipalpata",
      "order": "Terebellida",
      "suborder": "Cirratuliformia",
      "family": "Cirratulidae",
      "genus": "Aphelochaeta",
      "kingdomid": 2,
      "phylumid": 882,
      "classid": 883,
      "subclassid": 754175,
      "infraclassid": 154974,
      "orderid": 900,
      "suborderid": 155087,
      "familyid": 919,
      "genusid": 129240,
      "records": 432
    },
    {
      "scientificName": "Hydrozoa",
      "scientificNameAuthorship": "Owen, 1843",
      "taxonID": 1337,
      "ncbi_id": 6074,
      "wrims": true,
      "taxonRank": "Class",
      "taxonomicStatus": "accepted",
      "acceptedNameUsage": "Hydrozoa",
      "acceptedNameUsageID": 1337,
      "is_marine": true,
      "is_brackish": true,
      "is_freshwater": true,
      "is_terrestrial": false,
      "kingdom": "Animalia",
      "phylum": "Cnidaria",
      "subphylum": "Medusozoa",
      "class": "Hydrozoa",
      "kingdomid": 2,
      "phylumid": 1267,
      "subphylumid": 1740301,
      "classid": 1337,
      "records": 429
    },
    {
      "scientificName": "Oedicerotidae",
      "scientificNameAuthorship": "Lilljeborg, 1865",
      "taxonID": 101400,
      "ncbi_id": 181113,
      "wrims": true,
      "taxonRank": "Family",
      "taxonomicStatus": "accepted",
      "acceptedNameUsage": "Oedicerotidae",
      "acceptedNameUsageID": 101400,
      "is_marine": true,
      "is_brackish": false,
      "is_freshwater": false,
      "is_terrestrial": false,
      "kingdom": "Animalia",
      "phylum": "Arthropoda",
      "subphylum": "Crustacea",
      "superclass": "Multicrustacea",
      "class": "Malacostraca",
      "subclass": "Eumalacostraca",
      "superorder": "Peracarida",
      "order": "Amphipoda",
      "suborder": "Amphilochidea",
      "infraorder": "Amphilochida",
      "parvorder": "Oedicerotidira",
      "superfamily": "Oedicerotoidea",
      "family": "Oedicerotidae",
      "kingdomid": 2,
      "phylumid": 1065,
      "subphylumid": 1066,
      "superclassid": 845959,
      "classid": 1071,
      "subclassid": 1086,
      "superorderid": 1090,
      "orderid": 1135,
      "suborderid": 1055678,
      "infraorderid": 1055679,
      "parvorderid": 1055682,
      "superfamilyid": 1055683,
      "familyid": 101400,
      "records": 417
    },
    {
      "scientificName": "Notomastus latericeus",
      "scientificNameAuthorship": "Sars, 1851",
      "taxonID": 129898,
      "ncbi_id": 167831,
      "taxonRank": "Species",
      "taxonomicStatus": "accepted",
      "acceptedNameUsage": "Notomastus latericeus",
      "acceptedNameUsageID": 129898,
      "is_marine": true,
      "is_brackish": false,
      "is_freshwater": false,
      "is_terrestrial": false,
      "kingdom": "Animalia",
      "phylum": "Annelida",
      "class": "Polychaeta",
      "subclass": "Sedentaria",
      "infraclass": "Scolecida",
      "family": "Capitellidae",
      "genus": "Notomastus",
      "species": "Notomastus latericeus",
      "kingdomid": 2,
      "phylumid": 882,
      "classid": 883,
      "subclassid": 754175,
      "infraclassid": 183607,
      "familyid": 921,
      "genusid": 129220,
      "speciesid": 129898,
      "records": 413
    },
    {
      "scientificName": "Cephalaspidea",
      "scientificNameAuthorship": "P. Fischer, 1883",
      "taxonID": 154,
      "ncbi_id": 69554,
      "wrims": true,
      "taxonRank": "Order",
      "taxonomicStatus": "accepted",
      "acceptedNameUsage": "Cephalaspidea",
      "acceptedNameUsageID": 154,
      "is_marine": true,
      "is_brackish": true,
      "is_freshwater": true,
      "kingdom": "Animalia",
      "phylum": "Mollusca",
      "class": "Gastropoda",
      "subclass": "Heterobranchia",
      "infraclass": "Euthyneura",
      "subterclass": "Tectipleura",
      "order": "Cephalaspidea",
      "kingdomid": 2,
      "phylumid": 51,
      "classid": 101,
      "subclassid": 14712,
      "infraclassid": 1057247,
      "subterclassid": 1057250,
      "orderid": 154,
      "records": 410
    },
    {
      "scientificName": "Harpinia",
      "scientificNameAuthorship": "Boeck, 1876",
      "taxonID": 101716,
      "ncbi_id": 1732150,
      "taxonRank": "Genus",
      "taxonomicStatus": "accepted",
      "acceptedNameUsage": "Harpinia",
      "acceptedNameUsageID": 101716,
      "is_marine": true,
      "is_brackish": false,
      "is_freshwater": false,
      "is_terrestrial": false,
      "kingdom": "Animalia",
      "phylum": "Arthropoda",
      "subphylum": "Crustacea",
      "superclass": "Multicrustacea",
      "class": "Malacostraca",
      "subclass": "Eumalacostraca",
      "superorder": "Peracarida",
      "order": "Amphipoda",
      "suborder": "Amphilochidea",
      "infraorder": "Lysianassida",
      "parvorder": "Haustoriidira",
      "superfamily": "Haustorioidea",
      "family": "Phoxocephalidae",
      "subfamily": "Harpiniinae",
      "genus": "Harpinia",
      "kingdomid": 2,
      "phylumid": 1065,
      "subphylumid": 1066,
      "superclassid": 845959,
      "classid": 1071,
      "subclassid": 1086,
      "superorderid": 1090,
      "orderid": 1135,
      "suborderid": 1055678,
      "infraorderid": 1055690,
      "parvorderid": 1055694,
      "superfamilyid": 1055695,
      "familyid": 101403,
      "subfamilyid": 176844,
      "genusid": 101716,
      "records": 403
    },
    {
      "scientificName": "Astarte sulcata",
      "scientificNameAuthorship": "(da Costa, 1778)",
      "taxonID": 138824,
      "ncbi_id": 462886,
      "taxonRank": "Species",
      "taxonomicStatus": "accepted",
      "acceptedNameUsage": "Astarte sulcata",
      "acceptedNameUsageID": 138824,
      "is_marine": true,
      "kingdom": "Animalia",
      "phylum": "Mollusca",
      "class": "Bivalvia",
      "subclass": "Autobranchia",
      "infraclass": "Heteroconchia",
      "subterclass": "Archiheterodonta",
      "order": "Carditida",
      "superfamily": "Crassatelloidea",
      "family": "Astartidae",
      "subfamily": "Astartinae",
      "genus": "Astarte",
      "species": "Astarte sulcata",
      "kingdomid": 2,
      "phylumid": 51,
      "classid": 105,
      "subclassid": 1424948,
      "infraclassid": 1424949,
      "subterclassid": 382255,
      "orderid": 382256,
      "superfamilyid": 23014,
      "familyid": 228,
      "subfamilyid": 1817149,
      "genusid": 137683,
      "speciesid": 138824,
      "records": 388
    },
    {
      "scientificName": "Chone",
      "scientificNameAuthorship": "Kr\u00f8yer, 1856",
      "taxonID": 129525,
      "wrims": true,
      "taxonRank": "Genus",
      "taxonomicStatus": "accepted",
      "acceptedNameUsage": "Chone",
      "acceptedNameUsageID": 129525,
      "is_marine": true,
      "is_brackish": false,
      "is_freshwater": false,
      "is_terrestrial": false,
      "kingdom": "Animalia",
      "phylum": "Annelida",
      "class": "Polychaeta",
      "subclass": "Sedentaria",
      "infraclass": "Canalipalpata",
      "order": "Sabellida",
      "family": "Sabellidae",
      "subfamily": "Myxicolinae",
      "tribe": "Myxicolini",
      "genus": "Chone",
      "kingdomid": 2,
      "phylumid": 882,
      "classid": 883,
      "subclassid": 754175,
      "infraclassid": 154974,
      "orderid": 901,
      "familyid": 985,
      "subfamilyid": 1470421,
      "tribeid": 1470460,
      "genusid": 129525,
      "records": 386
    }
  ]
}
```

#### ttl
```ttl
@prefix dwc: <http://rs.tdwg.org/dwc/terms/> .
@prefix obis: <https://api.obis.org/v3/terms/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/obis-mareano-checklist#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] seadots:checklistResult [ dwc:acceptedNameUsage "Oedicerotidae" ;
            dwc:acceptedNameUsageID 101400 ;
            dwc:class "Malacostraca" ;
            dwc:family "Oedicerotidae" ;
            dwc:kingdom "Animalia" ;
            dwc:marine true ;
            dwc:order "Amphipoda" ;
            dwc:phylum "Arthropoda" ;
            dwc:scientificName "Oedicerotidae" ;
            dwc:scientificNameAuthorship "Lilljeborg, 1865" ;
            dwc:taxonID 101400 ;
            dwc:taxonRank "Family" ;
            dwc:taxonomicStatus "accepted" ;
            obis:records 417 ;
            seadots:classid 1071 ;
            seadots:familyid 101400 ;
            seadots:infraorder "Amphilochida" ;
            seadots:infraorderid 1055679 ;
            seadots:isBrackish false ;
            seadots:isFreshwater false ;
            seadots:isTerrestrial false ;
            seadots:kingdomid 2 ;
            seadots:ncbiId 181113 ;
            seadots:orderid 1135 ;
            seadots:parvorder "Oedicerotidira" ;
            seadots:parvorderid 1055682 ;
            seadots:phylumid 1065 ;
            seadots:subclass "Eumalacostraca" ;
            seadots:subclassid 1086 ;
            seadots:suborder "Amphilochidea" ;
            seadots:suborderid 1055678 ;
            seadots:subphylum "Crustacea" ;
            seadots:subphylumid 1066 ;
            seadots:superclass "Multicrustacea" ;
            seadots:superclassid 845959 ;
            seadots:superfamily "Oedicerotoidea" ;
            seadots:superfamilyid 1055683 ;
            seadots:superorder "Peracarida" ;
            seadots:superorderid 1090 ;
            seadots:wrims true ],
        [ dwc:acceptedNameUsage "Hydrozoa" ;
            dwc:acceptedNameUsageID 1337 ;
            dwc:class "Hydrozoa" ;
            dwc:kingdom "Animalia" ;
            dwc:marine true ;
            dwc:phylum "Cnidaria" ;
            dwc:scientificName "Hydrozoa" ;
            dwc:scientificNameAuthorship "Owen, 1843" ;
            dwc:taxonID 1337 ;
            dwc:taxonRank "Class" ;
            dwc:taxonomicStatus "accepted" ;
            obis:records 429 ;
            seadots:classid 1337 ;
            seadots:isBrackish true ;
            seadots:isFreshwater true ;
            seadots:isTerrestrial false ;
            seadots:kingdomid 2 ;
            seadots:ncbiId 6074 ;
            seadots:phylumid 1267 ;
            seadots:subphylum "Medusozoa" ;
            seadots:subphylumid 1740301 ;
            seadots:wrims true ],
        [ dwc:acceptedNameUsage "Astarte sulcata" ;
            dwc:acceptedNameUsageID 138824 ;
            dwc:class "Bivalvia" ;
            dwc:family "Astartidae" ;
            dwc:genus "Astarte" ;
            dwc:kingdom "Animalia" ;
            dwc:marine true ;
            dwc:order "Carditida" ;
            dwc:phylum "Mollusca" ;
            dwc:scientificName "Astarte sulcata" ;
            dwc:scientificNameAuthorship "(da Costa, 1778)" ;
            dwc:specificEpithet "Astarte sulcata" ;
            dwc:taxonID 138824 ;
            dwc:taxonRank "Species" ;
            dwc:taxonomicStatus "accepted" ;
            obis:records 388 ;
            seadots:classid 105 ;
            seadots:familyid 228 ;
            seadots:genusid 137683 ;
            seadots:infraclass "Heteroconchia" ;
            seadots:infraclassid 1424949 ;
            seadots:kingdomid 2 ;
            seadots:ncbiId 462886 ;
            seadots:orderid 382256 ;
            seadots:phylumid 51 ;
            seadots:speciesid 138824 ;
            seadots:subclass "Autobranchia" ;
            seadots:subclassid 1424948 ;
            seadots:subfamily "Astartinae" ;
            seadots:subfamilyid 1817149 ;
            seadots:subterclass "Archiheterodonta" ;
            seadots:subterclassid 382255 ;
            seadots:superfamily "Crassatelloidea" ;
            seadots:superfamilyid 23014 ],
        [ dwc:acceptedNameUsage "Notomastus latericeus" ;
            dwc:acceptedNameUsageID 129898 ;
            dwc:class "Polychaeta" ;
            dwc:family "Capitellidae" ;
            dwc:genus "Notomastus" ;
            dwc:kingdom "Animalia" ;
            dwc:marine true ;
            dwc:phylum "Annelida" ;
            dwc:scientificName "Notomastus latericeus" ;
            dwc:scientificNameAuthorship "Sars, 1851" ;
            dwc:specificEpithet "Notomastus latericeus" ;
            dwc:taxonID 129898 ;
            dwc:taxonRank "Species" ;
            dwc:taxonomicStatus "accepted" ;
            obis:records 413 ;
            seadots:classid 883 ;
            seadots:familyid 921 ;
            seadots:genusid 129220 ;
            seadots:infraclass "Scolecida" ;
            seadots:infraclassid 183607 ;
            seadots:isBrackish false ;
            seadots:isFreshwater false ;
            seadots:isTerrestrial false ;
            seadots:kingdomid 2 ;
            seadots:ncbiId 167831 ;
            seadots:phylumid 882 ;
            seadots:speciesid 129898 ;
            seadots:subclass "Sedentaria" ;
            seadots:subclassid 754175 ],
        [ dwc:acceptedNameUsage "Chone" ;
            dwc:acceptedNameUsageID 129525 ;
            dwc:class "Polychaeta" ;
            dwc:family "Sabellidae" ;
            dwc:genus "Chone" ;
            dwc:kingdom "Animalia" ;
            dwc:marine true ;
            dwc:order "Sabellida" ;
            dwc:phylum "Annelida" ;
            dwc:scientificName "Chone" ;
            dwc:scientificNameAuthorship "Krøyer, 1856" ;
            dwc:taxonID 129525 ;
            dwc:taxonRank "Genus" ;
            dwc:taxonomicStatus "accepted" ;
            obis:records 386 ;
            seadots:classid 883 ;
            seadots:familyid 985 ;
            seadots:genusid 129525 ;
            seadots:infraclass "Canalipalpata" ;
            seadots:infraclassid 154974 ;
            seadots:isBrackish false ;
            seadots:isFreshwater false ;
            seadots:isTerrestrial false ;
            seadots:kingdomid 2 ;
            seadots:orderid 901 ;
            seadots:phylumid 882 ;
            seadots:subclass "Sedentaria" ;
            seadots:subclassid 754175 ;
            seadots:subfamily "Myxicolinae" ;
            seadots:subfamilyid 1470421 ;
            seadots:tribe "Myxicolini" ;
            seadots:tribeid 1470460 ;
            seadots:wrims true ],
        [ dwc:acceptedNameUsage "Sipuncula" ;
            dwc:acceptedNameUsageID 1268 ;
            dwc:kingdom "Animalia" ;
            dwc:marine true ;
            dwc:order "Sipuncula" ;
            dwc:phylum "Annelida" ;
            dwc:scientificName "Sipuncula" ;
            dwc:scientificNameAuthorship "Stephen, 1965" ;
            dwc:taxonID 1268 ;
            dwc:taxonRank "Order" ;
            dwc:taxonomicStatus "accepted" ;
            obis:records 459 ;
            seadots:isBrackish true ;
            seadots:isFreshwater false ;
            seadots:isTerrestrial false ;
            seadots:kingdomid 2 ;
            seadots:ncbiId 6433 ;
            seadots:orderid 1268 ;
            seadots:phylumid 882 ;
            seadots:wrims true ],
        [ dwc:acceptedNameUsage "Amphipoda" ;
            dwc:acceptedNameUsageID 1135 ;
            dwc:class "Malacostraca" ;
            dwc:kingdom "Animalia" ;
            dwc:marine true ;
            dwc:order "Amphipoda" ;
            dwc:phylum "Arthropoda" ;
            dwc:scientificName "Amphipoda" ;
            dwc:scientificNameAuthorship "Latreille, 1816" ;
            dwc:taxonID 1135 ;
            dwc:taxonRank "Order" ;
            dwc:taxonomicStatus "accepted" ;
            obis:records 452 ;
            seadots:classid 1071 ;
            seadots:isBrackish true ;
            seadots:isFreshwater true ;
            seadots:isTerrestrial true ;
            seadots:kingdomid 2 ;
            seadots:ncbiId 6821 ;
            seadots:orderid 1135 ;
            seadots:phylumid 1065 ;
            seadots:subclass "Eumalacostraca" ;
            seadots:subclassid 1086 ;
            seadots:subphylum "Crustacea" ;
            seadots:subphylumid 1066 ;
            seadots:superclass "Multicrustacea" ;
            seadots:superclassid 845959 ;
            seadots:superorder "Peracarida" ;
            seadots:superorderid 1090 ;
            seadots:wrims true ],
        [ dwc:acceptedNameUsage "Harpinia" ;
            dwc:acceptedNameUsageID 101716 ;
            dwc:class "Malacostraca" ;
            dwc:family "Phoxocephalidae" ;
            dwc:genus "Harpinia" ;
            dwc:kingdom "Animalia" ;
            dwc:marine true ;
            dwc:order "Amphipoda" ;
            dwc:phylum "Arthropoda" ;
            dwc:scientificName "Harpinia" ;
            dwc:scientificNameAuthorship "Boeck, 1876" ;
            dwc:taxonID 101716 ;
            dwc:taxonRank "Genus" ;
            dwc:taxonomicStatus "accepted" ;
            obis:records 403 ;
            seadots:classid 1071 ;
            seadots:familyid 101403 ;
            seadots:genusid 101716 ;
            seadots:infraorder "Lysianassida" ;
            seadots:infraorderid 1055690 ;
            seadots:isBrackish false ;
            seadots:isFreshwater false ;
            seadots:isTerrestrial false ;
            seadots:kingdomid 2 ;
            seadots:ncbiId 1732150 ;
            seadots:orderid 1135 ;
            seadots:parvorder "Haustoriidira" ;
            seadots:parvorderid 1055694 ;
            seadots:phylumid 1065 ;
            seadots:subclass "Eumalacostraca" ;
            seadots:subclassid 1086 ;
            seadots:subfamily "Harpiniinae" ;
            seadots:subfamilyid 176844 ;
            seadots:suborder "Amphilochidea" ;
            seadots:suborderid 1055678 ;
            seadots:subphylum "Crustacea" ;
            seadots:subphylumid 1066 ;
            seadots:superclass "Multicrustacea" ;
            seadots:superclassid 845959 ;
            seadots:superfamily "Haustorioidea" ;
            seadots:superfamilyid 1055695 ;
            seadots:superorder "Peracarida" ;
            seadots:superorderid 1090 ],
        [ dwc:acceptedNameUsage "Aphelochaeta" ;
            dwc:acceptedNameUsageID 129240 ;
            dwc:class "Polychaeta" ;
            dwc:family "Cirratulidae" ;
            dwc:genus "Aphelochaeta" ;
            dwc:kingdom "Animalia" ;
            dwc:marine true ;
            dwc:order "Terebellida" ;
            dwc:phylum "Annelida" ;
            dwc:scientificName "Aphelochaeta" ;
            dwc:scientificNameAuthorship "Blake, 1991" ;
            dwc:taxonID 129240 ;
            dwc:taxonRank "Genus" ;
            dwc:taxonomicStatus "accepted" ;
            obis:records 432 ;
            seadots:classid 883 ;
            seadots:familyid 919 ;
            seadots:genusid 129240 ;
            seadots:infraclass "Canalipalpata" ;
            seadots:infraclassid 154974 ;
            seadots:isBrackish false ;
            seadots:isFreshwater false ;
            seadots:isTerrestrial false ;
            seadots:kingdomid 2 ;
            seadots:ncbiId 394740 ;
            seadots:orderid 900 ;
            seadots:phylumid 882 ;
            seadots:subclass "Sedentaria" ;
            seadots:subclassid 754175 ;
            seadots:suborder "Cirratuliformia" ;
            seadots:suborderid 155087 ;
            seadots:wrims true ],
        [ dwc:acceptedNameUsage "Cephalaspidea" ;
            dwc:acceptedNameUsageID 154 ;
            dwc:class "Gastropoda" ;
            dwc:kingdom "Animalia" ;
            dwc:marine true ;
            dwc:order "Cephalaspidea" ;
            dwc:phylum "Mollusca" ;
            dwc:scientificName "Cephalaspidea" ;
            dwc:scientificNameAuthorship "P. Fischer, 1883" ;
            dwc:taxonID 154 ;
            dwc:taxonRank "Order" ;
            dwc:taxonomicStatus "accepted" ;
            obis:records 410 ;
            seadots:classid 101 ;
            seadots:infraclass "Euthyneura" ;
            seadots:infraclassid 1057247 ;
            seadots:isBrackish true ;
            seadots:isFreshwater true ;
            seadots:kingdomid 2 ;
            seadots:ncbiId 69554 ;
            seadots:orderid 154 ;
            seadots:phylumid 51 ;
            seadots:subclass "Heterobranchia" ;
            seadots:subclassid 14712 ;
            seadots:subterclass "Tectipleura" ;
            seadots:subterclassid 1057250 ;
            seadots:wrims true ] ;
    seadots:totalChecklistRows 3196 .


```


### OBIS occurrences for selected MAREANO datasets
#### json
```json
{"total":105687,"results":[{"basisOfRecord":"Occurrence","brackish":false,"catalogNumber":"143680821001060","class":"Polychaeta","classid":883,"collectionCode":"IMRMarbunnBenthos","continent":"Barents Sea","datasetID":"https://marineinfo.org/id/dataset/4539","datasetName":"grab_2006-2022","date_end":1409356800000,"date_mid":1409356800000,"date_start":1409356800000,"date_year":2014,"day":"30","decimalLatitude":73.130833,"decimalLongitude":33.378167,"depth":228.98000000000002,"eventDate":"2014-08-30T18:04:00+00:00/2014-08-30T18:17:00+00:00","eventID":"Cruise: 58GS-2014115 Sample: 821","eventTime":"18:04:00+00:00/18:17:00+00:00","family":"Maldanidae","familyid":923,"fieldNumber":"catchId: 60","genus":"Praxillura","genusid":129361,"infraclass":"Scolecida","infraclassid":183607,"institutionCode":"IMR","kingdom":"Animalia","kingdomid":2,"locality":"MAREANO Reference Station: 1436","marine":true,"maximumDepthInMeters":229.11,"minimumDepthInMeters":228.85,"modified":"2024-05-23 10:35:05","month":"8","occurrenceID":"143680821001060","occurrenceStatus":"present","phylum":"Annelida","phylumid":882,"samplingProtocol":"Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0","scientificName":"Praxillura longissima","scientificNameAuthorship":"Arwidsson, 1906","scientificNameID":"urn:lsid:marinespecies.org:taxname:130327","species":"Praxillura longissima","speciesid":130327,"subclass":"Sedentaria","subclassid":754175,"subfamily":"Lumbriclymeninae","subfamilyid":154919,"year":"2014","id":"00014e73-67d6-40ce-919f-0ca40089c1e6","dataset_id":"d556b9d4-7625-4aa2-894d-441eabae47f7","node_id":["4bf79a01-65a9-4db6-b37b-18434f26ddfc"],"dropped":false,"absence":false,"originalScientificName":"Praxillura longissima","aphiaID":130327,"flags":[],"bathymetry":236.2,"shoredistance":286893,"sst":4.99,"sss":35},{"basisOfRecord":"Occurrence","brackish":false,"catalogNumber":"078650010010013","class":"Malacostraca","classid":1071,"collectionCode":"IMRMarbunnBenthos","continent":"Norwegian Sea","datasetID":"https://marineinfo.org/id/dataset/4541","datasetName":"rp-sledge_2006-2022","date_end":1336176000000,"date_mid":1336176000000,"date_start":1336176000000,"date_year":2012,"day":"5","decimalLatitude":67.955607,"decimalLongitude":9.5926,"depth":1307.4250000000002,"eventDate":"2012-05-05T23:09:00+00:00/2012-05-05T23:24:00+00:00","eventID":"Cruise: 58GS-2012106 Sample: 10","eventTime":"23:09:00+00:00/23:24:00+00:00","fieldNumber":"catchId: 13","footprintWKT":"LINESTRING(9.5926 67.955607,9.600935 67.958358)","infraorder":"Lysianassida","infraorderid":1055690,"institutionCode":"IMR","kingdom":"Animalia","kingdomid":2,"locality":"MAREANO Reference Station: 786","marine":true,"maximumDepthInMeters":1315.39,"minimumDepthInMeters":1299.46,"modified":"2024-05-23 10:35:05","month":"5","occurrenceID":"078650010010013","occurrenceStatus":"present","order":"Amphipoda","orderid":1135,"parvorder":"Lysianassidira","parvorderid":1055696,"phylum":"Arthropoda","phylumid":1065,"samplingProtocol":"RP-sledge,Subsample method: Decanted - Mesh size (mm): 0.5","scientificName":"Lysianassoidea","scientificNameAuthorship":"Dana, 1849","scientificNameID":"urn:lsid:marinespecies.org:taxname:176788","subclass":"Eumalacostraca","subclassid":1086,"suborder":"Amphilochidea","suborderid":1055678,"subphylum":"Crustacea","subphylumid":1066,"superclass":"Multicrustacea","superclassid":845959,"superfamily":"Lysianassoidea","superfamilyid":176788,"superorder":"Peracarida","superorderid":1090,"wrims":true,"year":"2012","id":"0001e2dc-e4c7-4fd0-9214-7c643a7d7c4a","dataset_id":"152259dc-9c20-4c1a-9644-8e4b509d4f73","node_id":["4bf79a01-65a9-4db6-b37b-18434f26ddfc"],"dropped":false,"absence":false,"originalScientificName":"Lysianassoidea","aphiaID":176788,"flags":[],"bathymetry":1320.8,"shoredistance":109497,"sst":8.81,"sss":34.99},{"basisOfRecord":"Occurrence","brackish":false,"catalogNumber":"081880066019034","class":"Polychaeta","classid":883,"collectionCode":"IMRMarbunnBenthos","continent":"Norwegian Sea","datasetID":"https://marineinfo.org/id/dataset/4539","datasetName":"grab_2006-2022","date_end":1336089600000,"date_mid":1336089600000,"date_start":1336089600000,"date_year":2012,"day":"4","decimalLatitude":67.595283,"decimalLongitude":9.307715,"depth":913.03,"eventDate":"2012-05-04T23:33:00+00:00","eventID":"Cruise: 58GS-2012106 Sample: 66","eventTime":"23:33:00+00:00","family":"Acrocirridae","familyid":920,"fieldNumber":"catchId: 34","genus":"Actaedrilus","genusid":1473424,"infraclass":"Canalipalpata","infraclassid":154974,"institutionCode":"IMR","kingdom":"Animalia","kingdomid":2,"locality":"MAREANO Reference Station: 818","marine":true,"maximumDepthInMeters":913.03,"minimumDepthInMeters":913.03,"modified":"2024-05-23 10:35:05","month":"5","occurrenceID":"081880066019034","occurrenceStatus":"present","order":"Terebellida","orderid":900,"phylum":"Annelida","phylumid":882,"samplingProtocol":"Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0","scientificName":"Actaedrilus polyonyx","scientificNameAuthorship":"Eliason, 1962","scientificNameID":"urn:lsid:marinespecies.org:taxname:1473437","species":"Actaedrilus polyonyx","speciesid":1473437,"subclass":"Sedentaria","subclassid":754175,"suborder":"Cirratuliformia","suborderid":155087,"year":"2012","id":"0002100b-ad82-4d11-be10-c47f18f30c21","dataset_id":"d556b9d4-7625-4aa2-894d-441eabae47f7","node_id":["4bf79a01-65a9-4db6-b37b-18434f26ddfc"],"dropped":false,"absence":false,"originalScientificName":"Actaedrilus polyonyx","aphiaID":1473437,"flags":[],"bathymetry":916.8,"shoredistance":109430,"sst":8.94,"sss":34.99},{"basisOfRecord":"Occurrence","brackish":false,"catalogNumber":"164910018001034","class":"Calcarea","classid":559,"collectionCode":"IMRMarbunnBenthos","continent":"Barents Sea","datasetID":"https://marineinfo.org/id/dataset/4540","datasetName":"beamtrawl_2006-2022","date_end":1475020800000,"date_mid":1475020800000,"date_start":1475020800000,"date_year":2016,"day":"28","decimalLatitude":74.997,"decimalLongitude":25.9995,"depth":208.005,"eventDate":"2016-09-28T00:41:00+00:00/2016-09-28T00:46:00+00:00","eventID":"Cruise: 58GS-2016113 Sample: 18","eventTime":"00:41:00+00:00/00:46:00+00:00","fieldNumber":"catchId: 34","footprintWKT":"LINESTRING(25.9995 74.997,25.9995 74.994833)","institutionCode":"IMR","kingdom":"Animalia","kingdomid":2,"locality":"MAREANO Reference Station: 1649","marine":true,"maximumDepthInMeters":208.45,"minimumDepthInMeters":207.56,"modified":"2024-05-23 10:35:05","month":"9","occurrenceID":"164910018001034","occurrenceStatus":"present","order":"Leucosolenida","orderid":131591,"phylum":"Porifera","phylumid":558,"samplingProtocol":"Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0","scientificName":"Leucosolenida","scientificNameID":"urn:lsid:marinespecies.org:taxname:131591","subclass":"Calcaronea","subclassid":131584,"wrims":true,"year":"2016","id":"00029056-f56d-45f4-a1db-f6bbd2350903","dataset_id":"14fa3c3e-259c-4af9-9314-eee1dc3a119b","node_id":["4bf79a01-65a9-4db6-b37b-18434f26ddfc"],"dropped":false,"absence":false,"originalScientificName":"Leucosolenida","aphiaID":131591,"flags":[],"bathymetry":219,"shoredistance":163319,"sst":3.35,"sss":34.68},{"basisOfRecord":"Occurrence","brackish":false,"catalogNumber":"171710009001042","class":"Polychaeta","classid":883,"collectionCode":"IMRMarbunnBenthos","continent":"Barents Sea","datasetID":"https://marineinfo.org/id/dataset/4540","datasetName":"beamtrawl_2006-2022","date_end":1491436800000,"date_mid":1491436800000,"date_start":1491436800000,"date_year":2017,"day":"6","decimalLatitude":73.5475,"decimalLongitude":23.913167,"depth":448.975,"eventDate":"2017-04-06T03:41:00+00:00/2017-04-06T03:46:00+00:00","eventID":"Cruise: 58GS-2017103 Sample: 9","eventTime":"03:41:00+00:00/03:46:00+00:00","family":"Sabellidae","familyid":985,"fieldNumber":"catchId: 42","footprintWKT":"LINESTRING(23.913167 73.5475,23.909547 73.54935)","genus":"Chone","genusid":129525,"infraclass":"Canalipalpata","infraclassid":154974,"institutionCode":"IMR","kingdom":"Animalia","kingdomid":2,"locality":"MAREANO Reference Station: 1717","marine":true,"maximumDepthInMeters":449.1,"minimumDepthInMeters":448.85,"modified":"2024-05-23 10:35:05","month":"4","occurrenceID":"171710009001042","occurrenceStatus":"present","order":"Sabellida","orderid":901,"phylum":"Annelida","phylumid":882,"samplingProtocol":"Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0","scientificName":"Chone","scientificNameAuthorship":"Krøyer, 1856","scientificNameID":"urn:lsid:marinespecies.org:taxname:129525","subclass":"Sedentaria","subclassid":754175,"subfamily":"Myxicolinae","subfamilyid":1470421,"tribe":"Myxicolini","tribeid":1470460,"wrims":true,"year":"2017","id":"0002e38c-8260-4f5d-9bc4-1895860fbcb8","dataset_id":"14fa3c3e-259c-4af9-9314-eee1dc3a119b","node_id":["4bf79a01-65a9-4db6-b37b-18434f26ddfc"],"dropped":false,"absence":false,"originalScientificName":"Chone","aphiaID":129525,"flags":[],"bathymetry":453.4,"shoredistance":171175,"sst":5.67,"sss":35.03},{"basisOfRecord":"Occurrence","brackish":false,"catalogNumber":"059290417049111","class":"Gastropoda","classid":101,"collectionCode":"IMRMarbunnBenthos","continent":"Norwegian Sea","datasetID":"https://marineinfo.org/id/dataset/4539","datasetName":"grab_2006-2022","date_end":1281484800000,"date_mid":1281484800000,"date_start":1281484800000,"date_year":2010,"day":"11","decimalLatitude":70.411833,"decimalLongitude":18.704333,"depth":100.47,"eventDate":"2010-08-11T00:40:00+00:00","eventID":"Cruise: 58GS-2010110 Sample: 417","eventTime":"00:40:00+00:00","family":"Buccinidae","familyid":149,"fieldNumber":"catchId: 111","genus":"Buccinum","genusid":137701,"institutionCode":"IMR","kingdom":"Animalia","kingdomid":2,"locality":"MAREANO Reference Station: 592","marine":true,"maximumDepthInMeters":100.47,"minimumDepthInMeters":100.47,"modified":"2024-05-23 10:35:05","month":"8","occurrenceID":"059290417049111","occurrenceStatus":"present","order":"Neogastropoda","orderid":146,"phylum":"Mollusca","phylumid":51,"samplingProtocol":"VVgrab020,Subsample method: Sieve content - Mesh size (mm): 1.0","scientificName":"Buccinum finmarkianum","scientificNameAuthorship":"Verkrüzen, 1875","scientificNameID":"urn:lsid:marinespecies.org:taxname:160143","species":"Buccinum finmarkianum","speciesid":160143,"subclass":"Caenogastropoda","subclassid":224570,"subfamily":"Buccininae","subfamilyid":225649,"superfamily":"Buccinoidea","superfamilyid":382214,"year":"2010","id":"00054ffb-17c9-46eb-9aeb-72252a6b90d8","dataset_id":"d556b9d4-7625-4aa2-894d-441eabae47f7","node_id":["4bf79a01-65a9-4db6-b37b-18434f26ddfc"],"dropped":false,"absence":false,"originalScientificName":"Buccinum finmarkianum","aphiaID":160143,"flags":[],"bathymetry":96.6,"shoredistance":21556,"sst":7.26,"sss":34.46},{"basisOfRecord":"Occurrence","brackish":false,"catalogNumber":"253740119001007","class":"Echinoidea","classid":123082,"collectionCode":"IMRMarbunnBenthos","continent":"Norwegian Sea","datasetID":"https://marineinfo.org/id/dataset/4539","datasetName":"grab_2006-2022","date_end":1620000000000,"date_mid":1620000000000,"date_start":1620000000000,"date_year":2021,"day":"3","decimalLatitude":62.060718,"decimalLongitude":1.414981,"depth":369,"eventDate":"2021-05-03T12:22:00+00:00","eventID":"Cruise: 58GS-2021104 Sample: 119","eventTime":"12:22:00+00:00","family":"Brissidae","familyid":123173,"fieldNumber":"catchId: 7","genus":"Brissopsis","genusid":123418,"infraclass":"Irregularia","infraclassid":510499,"institutionCode":"IMR","kingdom":"Animalia","kingdomid":2,"locality":"MAREANO Reference Station: 2537","marine":true,"maximumDepthInMeters":369,"minimumDepthInMeters":369,"modified":"2024-05-23 10:35:05","month":"5","occurrenceID":"253740119001007","occurrenceStatus":"present","order":"Spatangoida","orderid":123106,"phylum":"Echinodermata","phylumid":1806,"samplingProtocol":"Small VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0","scientificName":"Brissopsis lyrifera","scientificNameAuthorship":"(Forbes, 1841)","scientificNameID":"urn:lsid:marinespecies.org:taxname:124373","species":"Brissopsis lyrifera","speciesid":124373,"subclass":"Euechinoidea","subclassid":149854,"subfamily":"Brissopsinae","subfamilyid":510878,"suborder":"Brissidina","suborderid":510538,"subphylum":"Echinozoa","subphylumid":148744,"subterclass":"Atelostomata","subterclassid":149864,"year":"2021","id":"0007423f-403a-44d2-9565-281acbe343ce","dataset_id":"d556b9d4-7625-4aa2-894d-441eabae47f7","node_id":["4bf79a01-65a9-4db6-b37b-18434f26ddfc"],"dropped":false,"absence":false,"originalScientificName":"Brissopsis lyrifera","aphiaID":124373,"flags":[],"bathymetry":362.4,"shoredistance":171442,"sst":10.07,"sss":35.3},{"basisOfRecord":"Occurrence","brackish":false,"catalogNumber":"227940090001039","class":"Holothuroidea","classid":123083,"collectionCode":"IMRMarbunnBenthos","continent":"Norwegian Sea","datasetID":"https://marineinfo.org/id/dataset/4539","datasetName":"grab_2006-2022","date_end":1595462400000,"date_mid":1595462400000,"date_start":1595462400000,"date_year":2020,"day":"23","decimalLatitude":65.629713,"decimalLongitude":10.611012,"depth":376.78,"eventDate":"2020-07-23T20:38:00+00:00","eventID":"Cruise: 58GS-2020110 Sample: 90","eventTime":"20:38:00+00:00","family":"Ypsilothuriidae","familyid":123186,"fieldNumber":"catchId: 39","genus":"Echinocucumis","genusid":123473,"institutionCode":"IMR","kingdom":"Animalia","kingdomid":2,"locality":"MAREANO Reference Station: 2279","marine":true,"maximumDepthInMeters":376.78,"minimumDepthInMeters":376.78,"modified":"2024-05-23 10:35:05","month":"7","occurrenceID":"227940090001039","occurrenceStatus":"present","order":"Dendrochirotida","orderid":123111,"phylum":"Echinodermata","phylumid":1806,"samplingProtocol":"Small VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0","scientificName":"Echinocucumis hispida","scientificNameAuthorship":"(Barrett, 1857)","scientificNameID":"urn:lsid:marinespecies.org:taxname:124593","species":"Echinocucumis hispida","speciesid":124593,"subclass":"Actinopoda","subclassid":1393249,"subphylum":"Echinozoa","subphylumid":148744,"year":"2020","id":"0007ec71-87e5-4701-8474-ac409618ed43","dataset_id":"d556b9d4-7625-4aa2-894d-441eabae47f7","node_id":["4bf79a01-65a9-4db6-b37b-18434f26ddfc"],"dropped":false,"absence":false,"originalScientificName":"Echinocucumis hispida","aphiaID":124593,"flags":[],"bathymetry":393.8,"shoredistance":30052,"sst":9.36,"sss":34.32},{"basisOfRecord":"Occurrence","brackish":false,"catalogNumber":"000810008002016","class":"Malacostraca","classid":1071,"collectionCode":"IMRMarbunnBenthos","continent":"Barents Sea","datasetID":"https://marineinfo.org/id/dataset/4540","datasetName":"beamtrawl_2006-2022","date_end":1148774400000,"date_mid":1148774400000,"date_start":1148774400000,"date_year":2006,"day":"28","decimalLatitude":71.287677,"decimalLongitude":22.133255,"depth":321.15,"eventDate":"2006-05-28T02:33:00+00:00/2006-05-28T02:39:00+00:00","eventID":"Cruise: 58AA-2006612 Sample: 8","eventTime":"02:33:00+00:00/02:39:00+00:00","family":"Munididae","familyid":562645,"fieldNumber":"catchId: 16","footprintWKT":"LINESTRING(22.133255 71.287677,22.13529 71.289484)","genus":"Munida","genusid":106835,"infraorder":"Anomura","infraorderid":106671,"institutionCode":"IMR","kingdom":"Animalia","kingdomid":2,"locality":"MAREANO Reference Station: 8","marine":true,"maximumDepthInMeters":321.8,"minimumDepthInMeters":320.5,"modified":"2024-05-23 10:35:05","month":"5","occurrenceID":"000810008002016","occurrenceStatus":"present","order":"Decapoda","orderid":1130,"phylum":"Arthropoda","phylumid":1065,"samplingProtocol":"Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0","scientificName":"Munida sarsi","scientificNameAuthorship":"Huus, 1935","scientificNameID":"urn:lsid:marinespecies.org:taxname:107163","species":"Munida sarsi","speciesid":107163,"subclass":"Eumalacostraca","subclassid":1086,"suborder":"Pleocyemata","suborderid":106670,"subphylum":"Crustacea","subphylumid":1066,"superclass":"Multicrustacea","superclassid":845959,"superfamily":"Galatheoidea","superfamilyid":106685,"superorder":"Eucarida","superorderid":1089,"year":"2006","id":"00087d31-412d-48ce-bed8-9ade8d5b80f5","dataset_id":"14fa3c3e-259c-4af9-9314-eee1dc3a119b","node_id":["4bf79a01-65a9-4db6-b37b-18434f26ddfc"],"dropped":false,"absence":false,"originalScientificName":"Munida sarsi","aphiaID":107163,"flags":[],"bathymetry":319.6,"shoredistance":53735,"sst":7.06,"sss":34.91},{"basisOfRecord":"Occurrence","brackish":true,"catalogNumber":"000380058031020","class":"Ophiuroidea","classid":123084,"collectionCode":"IMRMarbunnBenthos","continent":"Barents Sea","datasetID":"https://marineinfo.org/id/dataset/4539","datasetName":"grab_2006-2022","date_end":1149552000000,"date_mid":1149552000000,"date_start":1149552000000,"date_year":2006,"day":"6","decimalLatitude":71.329727,"decimalLongitude":22.415298,"depth":434.62,"eventDate":"2006-06-06T00:19:00+00:00","eventID":"Cruise: 58AA-2006612 Sample: 58","eventTime":"00:19:00+00:00","fieldNumber":"catchId: 20","institutionCode":"IMR","kingdom":"Animalia","kingdomid":2,"locality":"MAREANO Reference Station: 3","marine":true,"maximumDepthInMeters":434.62,"minimumDepthInMeters":434.62,"modified":"2024-05-23 10:35:05","month":"6","occurrenceID":"000380058031020","occurrenceStatus":"present","phylum":"Echinodermata","phylumid":1806,"samplingProtocol":"Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0","scientificName":"Ophiuroidea","scientificNameAuthorship":"Gray, 1840","scientificNameID":"urn:lsid:marinespecies.org:taxname:123084","subphylum":"Asterozoa","subphylumid":148743,"wrims":true,"year":"2006","id":"0009bf51-340c-4fa4-ba3d-ce3300291d9c","dataset_id":"d556b9d4-7625-4aa2-894d-441eabae47f7","node_id":["4bf79a01-65a9-4db6-b37b-18434f26ddfc"],"dropped":false,"absence":false,"originalScientificName":"Ophiuroidea","aphiaID":123084,"flags":[],"bathymetry":436.4,"shoredistance":53639,"sst":7.04,"sss":34.91}]}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/obis-mareano-checklist/context.jsonld",
  "total": 105687,
  "results": [
    {
      "basisOfRecord": "Occurrence",
      "brackish": false,
      "catalogNumber": "143680821001060",
      "class": "Polychaeta",
      "classid": 883,
      "collectionCode": "IMRMarbunnBenthos",
      "continent": "Barents Sea",
      "datasetID": "https://marineinfo.org/id/dataset/4539",
      "datasetName": "grab_2006-2022",
      "date_end": 1409356800000,
      "date_mid": 1409356800000,
      "date_start": 1409356800000,
      "date_year": 2014,
      "day": "30",
      "decimalLatitude": 73.130833,
      "decimalLongitude": 33.378167,
      "depth": 228.98000000000002,
      "eventDate": "2014-08-30T18:04:00+00:00/2014-08-30T18:17:00+00:00",
      "eventID": "Cruise: 58GS-2014115 Sample: 821",
      "eventTime": "18:04:00+00:00/18:17:00+00:00",
      "family": "Maldanidae",
      "familyid": 923,
      "fieldNumber": "catchId: 60",
      "genus": "Praxillura",
      "genusid": 129361,
      "infraclass": "Scolecida",
      "infraclassid": 183607,
      "institutionCode": "IMR",
      "kingdom": "Animalia",
      "kingdomid": 2,
      "locality": "MAREANO Reference Station: 1436",
      "marine": true,
      "maximumDepthInMeters": 229.11,
      "minimumDepthInMeters": 228.85,
      "modified": "2024-05-23 10:35:05",
      "month": "8",
      "occurrenceID": "143680821001060",
      "occurrenceStatus": "present",
      "phylum": "Annelida",
      "phylumid": 882,
      "samplingProtocol": "Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0",
      "scientificName": "Praxillura longissima",
      "scientificNameAuthorship": "Arwidsson, 1906",
      "scientificNameID": "urn:lsid:marinespecies.org:taxname:130327",
      "species": "Praxillura longissima",
      "speciesid": 130327,
      "subclass": "Sedentaria",
      "subclassid": 754175,
      "subfamily": "Lumbriclymeninae",
      "subfamilyid": 154919,
      "year": "2014",
      "id": "00014e73-67d6-40ce-919f-0ca40089c1e6",
      "dataset_id": "d556b9d4-7625-4aa2-894d-441eabae47f7",
      "node_id": [
        "4bf79a01-65a9-4db6-b37b-18434f26ddfc"
      ],
      "dropped": false,
      "absence": false,
      "originalScientificName": "Praxillura longissima",
      "aphiaID": 130327,
      "flags": [],
      "bathymetry": 236.2,
      "shoredistance": 286893,
      "sst": 4.99,
      "sss": 35
    },
    {
      "basisOfRecord": "Occurrence",
      "brackish": false,
      "catalogNumber": "078650010010013",
      "class": "Malacostraca",
      "classid": 1071,
      "collectionCode": "IMRMarbunnBenthos",
      "continent": "Norwegian Sea",
      "datasetID": "https://marineinfo.org/id/dataset/4541",
      "datasetName": "rp-sledge_2006-2022",
      "date_end": 1336176000000,
      "date_mid": 1336176000000,
      "date_start": 1336176000000,
      "date_year": 2012,
      "day": "5",
      "decimalLatitude": 67.955607,
      "decimalLongitude": 9.5926,
      "depth": 1307.4250000000002,
      "eventDate": "2012-05-05T23:09:00+00:00/2012-05-05T23:24:00+00:00",
      "eventID": "Cruise: 58GS-2012106 Sample: 10",
      "eventTime": "23:09:00+00:00/23:24:00+00:00",
      "fieldNumber": "catchId: 13",
      "footprintWKT": "LINESTRING(9.5926 67.955607,9.600935 67.958358)",
      "infraorder": "Lysianassida",
      "infraorderid": 1055690,
      "institutionCode": "IMR",
      "kingdom": "Animalia",
      "kingdomid": 2,
      "locality": "MAREANO Reference Station: 786",
      "marine": true,
      "maximumDepthInMeters": 1315.39,
      "minimumDepthInMeters": 1299.46,
      "modified": "2024-05-23 10:35:05",
      "month": "5",
      "occurrenceID": "078650010010013",
      "occurrenceStatus": "present",
      "order": "Amphipoda",
      "orderid": 1135,
      "parvorder": "Lysianassidira",
      "parvorderid": 1055696,
      "phylum": "Arthropoda",
      "phylumid": 1065,
      "samplingProtocol": "RP-sledge,Subsample method: Decanted - Mesh size (mm): 0.5",
      "scientificName": "Lysianassoidea",
      "scientificNameAuthorship": "Dana, 1849",
      "scientificNameID": "urn:lsid:marinespecies.org:taxname:176788",
      "subclass": "Eumalacostraca",
      "subclassid": 1086,
      "suborder": "Amphilochidea",
      "suborderid": 1055678,
      "subphylum": "Crustacea",
      "subphylumid": 1066,
      "superclass": "Multicrustacea",
      "superclassid": 845959,
      "superfamily": "Lysianassoidea",
      "superfamilyid": 176788,
      "superorder": "Peracarida",
      "superorderid": 1090,
      "wrims": true,
      "year": "2012",
      "id": "0001e2dc-e4c7-4fd0-9214-7c643a7d7c4a",
      "dataset_id": "152259dc-9c20-4c1a-9644-8e4b509d4f73",
      "node_id": [
        "4bf79a01-65a9-4db6-b37b-18434f26ddfc"
      ],
      "dropped": false,
      "absence": false,
      "originalScientificName": "Lysianassoidea",
      "aphiaID": 176788,
      "flags": [],
      "bathymetry": 1320.8,
      "shoredistance": 109497,
      "sst": 8.81,
      "sss": 34.99
    },
    {
      "basisOfRecord": "Occurrence",
      "brackish": false,
      "catalogNumber": "081880066019034",
      "class": "Polychaeta",
      "classid": 883,
      "collectionCode": "IMRMarbunnBenthos",
      "continent": "Norwegian Sea",
      "datasetID": "https://marineinfo.org/id/dataset/4539",
      "datasetName": "grab_2006-2022",
      "date_end": 1336089600000,
      "date_mid": 1336089600000,
      "date_start": 1336089600000,
      "date_year": 2012,
      "day": "4",
      "decimalLatitude": 67.595283,
      "decimalLongitude": 9.307715,
      "depth": 913.03,
      "eventDate": "2012-05-04T23:33:00+00:00",
      "eventID": "Cruise: 58GS-2012106 Sample: 66",
      "eventTime": "23:33:00+00:00",
      "family": "Acrocirridae",
      "familyid": 920,
      "fieldNumber": "catchId: 34",
      "genus": "Actaedrilus",
      "genusid": 1473424,
      "infraclass": "Canalipalpata",
      "infraclassid": 154974,
      "institutionCode": "IMR",
      "kingdom": "Animalia",
      "kingdomid": 2,
      "locality": "MAREANO Reference Station: 818",
      "marine": true,
      "maximumDepthInMeters": 913.03,
      "minimumDepthInMeters": 913.03,
      "modified": "2024-05-23 10:35:05",
      "month": "5",
      "occurrenceID": "081880066019034",
      "occurrenceStatus": "present",
      "order": "Terebellida",
      "orderid": 900,
      "phylum": "Annelida",
      "phylumid": 882,
      "samplingProtocol": "Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0",
      "scientificName": "Actaedrilus polyonyx",
      "scientificNameAuthorship": "Eliason, 1962",
      "scientificNameID": "urn:lsid:marinespecies.org:taxname:1473437",
      "species": "Actaedrilus polyonyx",
      "speciesid": 1473437,
      "subclass": "Sedentaria",
      "subclassid": 754175,
      "suborder": "Cirratuliformia",
      "suborderid": 155087,
      "year": "2012",
      "id": "0002100b-ad82-4d11-be10-c47f18f30c21",
      "dataset_id": "d556b9d4-7625-4aa2-894d-441eabae47f7",
      "node_id": [
        "4bf79a01-65a9-4db6-b37b-18434f26ddfc"
      ],
      "dropped": false,
      "absence": false,
      "originalScientificName": "Actaedrilus polyonyx",
      "aphiaID": 1473437,
      "flags": [],
      "bathymetry": 916.8,
      "shoredistance": 109430,
      "sst": 8.94,
      "sss": 34.99
    },
    {
      "basisOfRecord": "Occurrence",
      "brackish": false,
      "catalogNumber": "164910018001034",
      "class": "Calcarea",
      "classid": 559,
      "collectionCode": "IMRMarbunnBenthos",
      "continent": "Barents Sea",
      "datasetID": "https://marineinfo.org/id/dataset/4540",
      "datasetName": "beamtrawl_2006-2022",
      "date_end": 1475020800000,
      "date_mid": 1475020800000,
      "date_start": 1475020800000,
      "date_year": 2016,
      "day": "28",
      "decimalLatitude": 74.997,
      "decimalLongitude": 25.9995,
      "depth": 208.005,
      "eventDate": "2016-09-28T00:41:00+00:00/2016-09-28T00:46:00+00:00",
      "eventID": "Cruise: 58GS-2016113 Sample: 18",
      "eventTime": "00:41:00+00:00/00:46:00+00:00",
      "fieldNumber": "catchId: 34",
      "footprintWKT": "LINESTRING(25.9995 74.997,25.9995 74.994833)",
      "institutionCode": "IMR",
      "kingdom": "Animalia",
      "kingdomid": 2,
      "locality": "MAREANO Reference Station: 1649",
      "marine": true,
      "maximumDepthInMeters": 208.45,
      "minimumDepthInMeters": 207.56,
      "modified": "2024-05-23 10:35:05",
      "month": "9",
      "occurrenceID": "164910018001034",
      "occurrenceStatus": "present",
      "order": "Leucosolenida",
      "orderid": 131591,
      "phylum": "Porifera",
      "phylumid": 558,
      "samplingProtocol": "Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0",
      "scientificName": "Leucosolenida",
      "scientificNameID": "urn:lsid:marinespecies.org:taxname:131591",
      "subclass": "Calcaronea",
      "subclassid": 131584,
      "wrims": true,
      "year": "2016",
      "id": "00029056-f56d-45f4-a1db-f6bbd2350903",
      "dataset_id": "14fa3c3e-259c-4af9-9314-eee1dc3a119b",
      "node_id": [
        "4bf79a01-65a9-4db6-b37b-18434f26ddfc"
      ],
      "dropped": false,
      "absence": false,
      "originalScientificName": "Leucosolenida",
      "aphiaID": 131591,
      "flags": [],
      "bathymetry": 219,
      "shoredistance": 163319,
      "sst": 3.35,
      "sss": 34.68
    },
    {
      "basisOfRecord": "Occurrence",
      "brackish": false,
      "catalogNumber": "171710009001042",
      "class": "Polychaeta",
      "classid": 883,
      "collectionCode": "IMRMarbunnBenthos",
      "continent": "Barents Sea",
      "datasetID": "https://marineinfo.org/id/dataset/4540",
      "datasetName": "beamtrawl_2006-2022",
      "date_end": 1491436800000,
      "date_mid": 1491436800000,
      "date_start": 1491436800000,
      "date_year": 2017,
      "day": "6",
      "decimalLatitude": 73.5475,
      "decimalLongitude": 23.913167,
      "depth": 448.975,
      "eventDate": "2017-04-06T03:41:00+00:00/2017-04-06T03:46:00+00:00",
      "eventID": "Cruise: 58GS-2017103 Sample: 9",
      "eventTime": "03:41:00+00:00/03:46:00+00:00",
      "family": "Sabellidae",
      "familyid": 985,
      "fieldNumber": "catchId: 42",
      "footprintWKT": "LINESTRING(23.913167 73.5475,23.909547 73.54935)",
      "genus": "Chone",
      "genusid": 129525,
      "infraclass": "Canalipalpata",
      "infraclassid": 154974,
      "institutionCode": "IMR",
      "kingdom": "Animalia",
      "kingdomid": 2,
      "locality": "MAREANO Reference Station: 1717",
      "marine": true,
      "maximumDepthInMeters": 449.1,
      "minimumDepthInMeters": 448.85,
      "modified": "2024-05-23 10:35:05",
      "month": "4",
      "occurrenceID": "171710009001042",
      "occurrenceStatus": "present",
      "order": "Sabellida",
      "orderid": 901,
      "phylum": "Annelida",
      "phylumid": 882,
      "samplingProtocol": "Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0",
      "scientificName": "Chone",
      "scientificNameAuthorship": "Kr\u00f8yer, 1856",
      "scientificNameID": "urn:lsid:marinespecies.org:taxname:129525",
      "subclass": "Sedentaria",
      "subclassid": 754175,
      "subfamily": "Myxicolinae",
      "subfamilyid": 1470421,
      "tribe": "Myxicolini",
      "tribeid": 1470460,
      "wrims": true,
      "year": "2017",
      "id": "0002e38c-8260-4f5d-9bc4-1895860fbcb8",
      "dataset_id": "14fa3c3e-259c-4af9-9314-eee1dc3a119b",
      "node_id": [
        "4bf79a01-65a9-4db6-b37b-18434f26ddfc"
      ],
      "dropped": false,
      "absence": false,
      "originalScientificName": "Chone",
      "aphiaID": 129525,
      "flags": [],
      "bathymetry": 453.4,
      "shoredistance": 171175,
      "sst": 5.67,
      "sss": 35.03
    },
    {
      "basisOfRecord": "Occurrence",
      "brackish": false,
      "catalogNumber": "059290417049111",
      "class": "Gastropoda",
      "classid": 101,
      "collectionCode": "IMRMarbunnBenthos",
      "continent": "Norwegian Sea",
      "datasetID": "https://marineinfo.org/id/dataset/4539",
      "datasetName": "grab_2006-2022",
      "date_end": 1281484800000,
      "date_mid": 1281484800000,
      "date_start": 1281484800000,
      "date_year": 2010,
      "day": "11",
      "decimalLatitude": 70.411833,
      "decimalLongitude": 18.704333,
      "depth": 100.47,
      "eventDate": "2010-08-11T00:40:00+00:00",
      "eventID": "Cruise: 58GS-2010110 Sample: 417",
      "eventTime": "00:40:00+00:00",
      "family": "Buccinidae",
      "familyid": 149,
      "fieldNumber": "catchId: 111",
      "genus": "Buccinum",
      "genusid": 137701,
      "institutionCode": "IMR",
      "kingdom": "Animalia",
      "kingdomid": 2,
      "locality": "MAREANO Reference Station: 592",
      "marine": true,
      "maximumDepthInMeters": 100.47,
      "minimumDepthInMeters": 100.47,
      "modified": "2024-05-23 10:35:05",
      "month": "8",
      "occurrenceID": "059290417049111",
      "occurrenceStatus": "present",
      "order": "Neogastropoda",
      "orderid": 146,
      "phylum": "Mollusca",
      "phylumid": 51,
      "samplingProtocol": "VVgrab020,Subsample method: Sieve content - Mesh size (mm): 1.0",
      "scientificName": "Buccinum finmarkianum",
      "scientificNameAuthorship": "Verkr\u00fczen, 1875",
      "scientificNameID": "urn:lsid:marinespecies.org:taxname:160143",
      "species": "Buccinum finmarkianum",
      "speciesid": 160143,
      "subclass": "Caenogastropoda",
      "subclassid": 224570,
      "subfamily": "Buccininae",
      "subfamilyid": 225649,
      "superfamily": "Buccinoidea",
      "superfamilyid": 382214,
      "year": "2010",
      "id": "00054ffb-17c9-46eb-9aeb-72252a6b90d8",
      "dataset_id": "d556b9d4-7625-4aa2-894d-441eabae47f7",
      "node_id": [
        "4bf79a01-65a9-4db6-b37b-18434f26ddfc"
      ],
      "dropped": false,
      "absence": false,
      "originalScientificName": "Buccinum finmarkianum",
      "aphiaID": 160143,
      "flags": [],
      "bathymetry": 96.6,
      "shoredistance": 21556,
      "sst": 7.26,
      "sss": 34.46
    },
    {
      "basisOfRecord": "Occurrence",
      "brackish": false,
      "catalogNumber": "253740119001007",
      "class": "Echinoidea",
      "classid": 123082,
      "collectionCode": "IMRMarbunnBenthos",
      "continent": "Norwegian Sea",
      "datasetID": "https://marineinfo.org/id/dataset/4539",
      "datasetName": "grab_2006-2022",
      "date_end": 1620000000000,
      "date_mid": 1620000000000,
      "date_start": 1620000000000,
      "date_year": 2021,
      "day": "3",
      "decimalLatitude": 62.060718,
      "decimalLongitude": 1.414981,
      "depth": 369,
      "eventDate": "2021-05-03T12:22:00+00:00",
      "eventID": "Cruise: 58GS-2021104 Sample: 119",
      "eventTime": "12:22:00+00:00",
      "family": "Brissidae",
      "familyid": 123173,
      "fieldNumber": "catchId: 7",
      "genus": "Brissopsis",
      "genusid": 123418,
      "infraclass": "Irregularia",
      "infraclassid": 510499,
      "institutionCode": "IMR",
      "kingdom": "Animalia",
      "kingdomid": 2,
      "locality": "MAREANO Reference Station: 2537",
      "marine": true,
      "maximumDepthInMeters": 369,
      "minimumDepthInMeters": 369,
      "modified": "2024-05-23 10:35:05",
      "month": "5",
      "occurrenceID": "253740119001007",
      "occurrenceStatus": "present",
      "order": "Spatangoida",
      "orderid": 123106,
      "phylum": "Echinodermata",
      "phylumid": 1806,
      "samplingProtocol": "Small VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0",
      "scientificName": "Brissopsis lyrifera",
      "scientificNameAuthorship": "(Forbes, 1841)",
      "scientificNameID": "urn:lsid:marinespecies.org:taxname:124373",
      "species": "Brissopsis lyrifera",
      "speciesid": 124373,
      "subclass": "Euechinoidea",
      "subclassid": 149854,
      "subfamily": "Brissopsinae",
      "subfamilyid": 510878,
      "suborder": "Brissidina",
      "suborderid": 510538,
      "subphylum": "Echinozoa",
      "subphylumid": 148744,
      "subterclass": "Atelostomata",
      "subterclassid": 149864,
      "year": "2021",
      "id": "0007423f-403a-44d2-9565-281acbe343ce",
      "dataset_id": "d556b9d4-7625-4aa2-894d-441eabae47f7",
      "node_id": [
        "4bf79a01-65a9-4db6-b37b-18434f26ddfc"
      ],
      "dropped": false,
      "absence": false,
      "originalScientificName": "Brissopsis lyrifera",
      "aphiaID": 124373,
      "flags": [],
      "bathymetry": 362.4,
      "shoredistance": 171442,
      "sst": 10.07,
      "sss": 35.3
    },
    {
      "basisOfRecord": "Occurrence",
      "brackish": false,
      "catalogNumber": "227940090001039",
      "class": "Holothuroidea",
      "classid": 123083,
      "collectionCode": "IMRMarbunnBenthos",
      "continent": "Norwegian Sea",
      "datasetID": "https://marineinfo.org/id/dataset/4539",
      "datasetName": "grab_2006-2022",
      "date_end": 1595462400000,
      "date_mid": 1595462400000,
      "date_start": 1595462400000,
      "date_year": 2020,
      "day": "23",
      "decimalLatitude": 65.629713,
      "decimalLongitude": 10.611012,
      "depth": 376.78,
      "eventDate": "2020-07-23T20:38:00+00:00",
      "eventID": "Cruise: 58GS-2020110 Sample: 90",
      "eventTime": "20:38:00+00:00",
      "family": "Ypsilothuriidae",
      "familyid": 123186,
      "fieldNumber": "catchId: 39",
      "genus": "Echinocucumis",
      "genusid": 123473,
      "institutionCode": "IMR",
      "kingdom": "Animalia",
      "kingdomid": 2,
      "locality": "MAREANO Reference Station: 2279",
      "marine": true,
      "maximumDepthInMeters": 376.78,
      "minimumDepthInMeters": 376.78,
      "modified": "2024-05-23 10:35:05",
      "month": "7",
      "occurrenceID": "227940090001039",
      "occurrenceStatus": "present",
      "order": "Dendrochirotida",
      "orderid": 123111,
      "phylum": "Echinodermata",
      "phylumid": 1806,
      "samplingProtocol": "Small VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0",
      "scientificName": "Echinocucumis hispida",
      "scientificNameAuthorship": "(Barrett, 1857)",
      "scientificNameID": "urn:lsid:marinespecies.org:taxname:124593",
      "species": "Echinocucumis hispida",
      "speciesid": 124593,
      "subclass": "Actinopoda",
      "subclassid": 1393249,
      "subphylum": "Echinozoa",
      "subphylumid": 148744,
      "year": "2020",
      "id": "0007ec71-87e5-4701-8474-ac409618ed43",
      "dataset_id": "d556b9d4-7625-4aa2-894d-441eabae47f7",
      "node_id": [
        "4bf79a01-65a9-4db6-b37b-18434f26ddfc"
      ],
      "dropped": false,
      "absence": false,
      "originalScientificName": "Echinocucumis hispida",
      "aphiaID": 124593,
      "flags": [],
      "bathymetry": 393.8,
      "shoredistance": 30052,
      "sst": 9.36,
      "sss": 34.32
    },
    {
      "basisOfRecord": "Occurrence",
      "brackish": false,
      "catalogNumber": "000810008002016",
      "class": "Malacostraca",
      "classid": 1071,
      "collectionCode": "IMRMarbunnBenthos",
      "continent": "Barents Sea",
      "datasetID": "https://marineinfo.org/id/dataset/4540",
      "datasetName": "beamtrawl_2006-2022",
      "date_end": 1148774400000,
      "date_mid": 1148774400000,
      "date_start": 1148774400000,
      "date_year": 2006,
      "day": "28",
      "decimalLatitude": 71.287677,
      "decimalLongitude": 22.133255,
      "depth": 321.15,
      "eventDate": "2006-05-28T02:33:00+00:00/2006-05-28T02:39:00+00:00",
      "eventID": "Cruise: 58AA-2006612 Sample: 8",
      "eventTime": "02:33:00+00:00/02:39:00+00:00",
      "family": "Munididae",
      "familyid": 562645,
      "fieldNumber": "catchId: 16",
      "footprintWKT": "LINESTRING(22.133255 71.287677,22.13529 71.289484)",
      "genus": "Munida",
      "genusid": 106835,
      "infraorder": "Anomura",
      "infraorderid": 106671,
      "institutionCode": "IMR",
      "kingdom": "Animalia",
      "kingdomid": 2,
      "locality": "MAREANO Reference Station: 8",
      "marine": true,
      "maximumDepthInMeters": 321.8,
      "minimumDepthInMeters": 320.5,
      "modified": "2024-05-23 10:35:05",
      "month": "5",
      "occurrenceID": "000810008002016",
      "occurrenceStatus": "present",
      "order": "Decapoda",
      "orderid": 1130,
      "phylum": "Arthropoda",
      "phylumid": 1065,
      "samplingProtocol": "Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0",
      "scientificName": "Munida sarsi",
      "scientificNameAuthorship": "Huus, 1935",
      "scientificNameID": "urn:lsid:marinespecies.org:taxname:107163",
      "species": "Munida sarsi",
      "speciesid": 107163,
      "subclass": "Eumalacostraca",
      "subclassid": 1086,
      "suborder": "Pleocyemata",
      "suborderid": 106670,
      "subphylum": "Crustacea",
      "subphylumid": 1066,
      "superclass": "Multicrustacea",
      "superclassid": 845959,
      "superfamily": "Galatheoidea",
      "superfamilyid": 106685,
      "superorder": "Eucarida",
      "superorderid": 1089,
      "year": "2006",
      "id": "00087d31-412d-48ce-bed8-9ade8d5b80f5",
      "dataset_id": "14fa3c3e-259c-4af9-9314-eee1dc3a119b",
      "node_id": [
        "4bf79a01-65a9-4db6-b37b-18434f26ddfc"
      ],
      "dropped": false,
      "absence": false,
      "originalScientificName": "Munida sarsi",
      "aphiaID": 107163,
      "flags": [],
      "bathymetry": 319.6,
      "shoredistance": 53735,
      "sst": 7.06,
      "sss": 34.91
    },
    {
      "basisOfRecord": "Occurrence",
      "brackish": true,
      "catalogNumber": "000380058031020",
      "class": "Ophiuroidea",
      "classid": 123084,
      "collectionCode": "IMRMarbunnBenthos",
      "continent": "Barents Sea",
      "datasetID": "https://marineinfo.org/id/dataset/4539",
      "datasetName": "grab_2006-2022",
      "date_end": 1149552000000,
      "date_mid": 1149552000000,
      "date_start": 1149552000000,
      "date_year": 2006,
      "day": "6",
      "decimalLatitude": 71.329727,
      "decimalLongitude": 22.415298,
      "depth": 434.62,
      "eventDate": "2006-06-06T00:19:00+00:00",
      "eventID": "Cruise: 58AA-2006612 Sample: 58",
      "eventTime": "00:19:00+00:00",
      "fieldNumber": "catchId: 20",
      "institutionCode": "IMR",
      "kingdom": "Animalia",
      "kingdomid": 2,
      "locality": "MAREANO Reference Station: 3",
      "marine": true,
      "maximumDepthInMeters": 434.62,
      "minimumDepthInMeters": 434.62,
      "modified": "2024-05-23 10:35:05",
      "month": "6",
      "occurrenceID": "000380058031020",
      "occurrenceStatus": "present",
      "phylum": "Echinodermata",
      "phylumid": 1806,
      "samplingProtocol": "Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0",
      "scientificName": "Ophiuroidea",
      "scientificNameAuthorship": "Gray, 1840",
      "scientificNameID": "urn:lsid:marinespecies.org:taxname:123084",
      "subphylum": "Asterozoa",
      "subphylumid": 148743,
      "wrims": true,
      "year": "2006",
      "id": "0009bf51-340c-4fa4-ba3d-ce3300291d9c",
      "dataset_id": "d556b9d4-7625-4aa2-894d-441eabae47f7",
      "node_id": [
        "4bf79a01-65a9-4db6-b37b-18434f26ddfc"
      ],
      "dropped": false,
      "absence": false,
      "originalScientificName": "Ophiuroidea",
      "aphiaID": 123084,
      "flags": [],
      "bathymetry": 436.4,
      "shoredistance": 53639,
      "sst": 7.04,
      "sss": 34.91
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix dwc: <http://rs.tdwg.org/dwc/terms/> .
@prefix seadots: <https://w3id.org/ogc/hosted/seadots/obis-mareano-checklist#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/00014e73-67d6-40ce-919f-0ca40089c1e6> dcterms:isPartOf "d556b9d4-7625-4aa2-894d-441eabae47f7",
        "https://marineinfo.org/id/dataset/4539" ;
    dcterms:title "grab_2006-2022" ;
    dwc:basisOfRecord "Occurrence" ;
    dwc:class "Polychaeta" ;
    dwc:decimalLatitude 7.313083e+01 ;
    dwc:decimalLongitude 3.337817e+01 ;
    dwc:eventDate "2014-08-30T18:04:00+00:00/2014-08-30T18:17:00+00:00" ;
    dwc:eventID "Cruise: 58GS-2014115 Sample: 821" ;
    dwc:family "Maldanidae" ;
    dwc:genus "Praxillura" ;
    dwc:kingdom "Animalia" ;
    dwc:maximumDepthInMeters 2.2911e+02 ;
    dwc:minimumDepthInMeters 2.2885e+02,
        2.2898e+02 ;
    dwc:occurrenceID "143680821001060" ;
    dwc:phylum "Annelida" ;
    dwc:samplingProtocol "Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0" ;
    dwc:scientificName "Praxillura longissima" ;
    dwc:scientificNameAuthorship "Arwidsson, 1906" ;
    dwc:specificEpithet "Praxillura longissima" ;
    dwc:taxonID 130327 ;
    seadots:absence false ;
    seadots:bathymetry 2.362e+02 ;
    seadots:brackish false ;
    seadots:catalogNumber "143680821001060" ;
    seadots:classid 883 ;
    seadots:collectionCode "IMRMarbunnBenthos" ;
    seadots:continent "Barents Sea" ;
    seadots:date_end 1409356800000 ;
    seadots:date_mid 1409356800000 ;
    seadots:date_start 1409356800000 ;
    seadots:date_year 2014 ;
    seadots:day "30" ;
    seadots:dropped false ;
    seadots:eventTime "18:04:00+00:00/18:17:00+00:00" ;
    seadots:familyid 923 ;
    seadots:fieldNumber "catchId: 60" ;
    seadots:genusid 129361 ;
    seadots:infraclass "Scolecida" ;
    seadots:infraclassid 183607 ;
    seadots:institutionCode "IMR" ;
    seadots:kingdomid 2 ;
    seadots:locality "MAREANO Reference Station: 1436" ;
    seadots:marine true ;
    seadots:modified "2024-05-23 10:35:05" ;
    seadots:month "8" ;
    seadots:node_id "4bf79a01-65a9-4db6-b37b-18434f26ddfc" ;
    seadots:occurrenceStatus "present" ;
    seadots:originalScientificName "Praxillura longissima" ;
    seadots:phylumid 882 ;
    seadots:scientificNameID "urn:lsid:marinespecies.org:taxname:130327" ;
    seadots:shoredistance 286893 ;
    seadots:speciesid 130327 ;
    seadots:sss 35 ;
    seadots:sst 4.99e+00 ;
    seadots:subclass "Sedentaria" ;
    seadots:subclassid 754175 ;
    seadots:subfamily "Lumbriclymeninae" ;
    seadots:subfamilyid 154919 ;
    seadots:year "2014" .

<file:///github/workspace/0001e2dc-e4c7-4fd0-9214-7c643a7d7c4a> dcterms:isPartOf "152259dc-9c20-4c1a-9644-8e4b509d4f73",
        "https://marineinfo.org/id/dataset/4541" ;
    dcterms:title "rp-sledge_2006-2022" ;
    dwc:basisOfRecord "Occurrence" ;
    dwc:class "Malacostraca" ;
    dwc:decimalLatitude 6.795561e+01 ;
    dwc:decimalLongitude 9.5926e+00 ;
    dwc:eventDate "2012-05-05T23:09:00+00:00/2012-05-05T23:24:00+00:00" ;
    dwc:eventID "Cruise: 58GS-2012106 Sample: 10" ;
    dwc:kingdom "Animalia" ;
    dwc:maximumDepthInMeters 1.31539e+03 ;
    dwc:minimumDepthInMeters 1.29946e+03,
        1.307425e+03 ;
    dwc:occurrenceID "078650010010013" ;
    dwc:order "Amphipoda" ;
    dwc:phylum "Arthropoda" ;
    dwc:samplingProtocol "RP-sledge,Subsample method: Decanted - Mesh size (mm): 0.5" ;
    dwc:scientificName "Lysianassoidea" ;
    dwc:scientificNameAuthorship "Dana, 1849" ;
    dwc:taxonID 176788 ;
    seadots:absence false ;
    seadots:bathymetry 1.3208e+03 ;
    seadots:brackish false ;
    seadots:catalogNumber "078650010010013" ;
    seadots:classid 1071 ;
    seadots:collectionCode "IMRMarbunnBenthos" ;
    seadots:continent "Norwegian Sea" ;
    seadots:date_end 1336176000000 ;
    seadots:date_mid 1336176000000 ;
    seadots:date_start 1336176000000 ;
    seadots:date_year 2012 ;
    seadots:day "5" ;
    seadots:dropped false ;
    seadots:eventTime "23:09:00+00:00/23:24:00+00:00" ;
    seadots:fieldNumber "catchId: 13" ;
    seadots:footprintWKT "LINESTRING(9.5926 67.955607,9.600935 67.958358)" ;
    seadots:infraorder "Lysianassida" ;
    seadots:infraorderid 1055690 ;
    seadots:institutionCode "IMR" ;
    seadots:kingdomid 2 ;
    seadots:locality "MAREANO Reference Station: 786" ;
    seadots:marine true ;
    seadots:modified "2024-05-23 10:35:05" ;
    seadots:month "5" ;
    seadots:node_id "4bf79a01-65a9-4db6-b37b-18434f26ddfc" ;
    seadots:occurrenceStatus "present" ;
    seadots:orderid 1135 ;
    seadots:originalScientificName "Lysianassoidea" ;
    seadots:parvorder "Lysianassidira" ;
    seadots:parvorderid 1055696 ;
    seadots:phylumid 1065 ;
    seadots:scientificNameID "urn:lsid:marinespecies.org:taxname:176788" ;
    seadots:shoredistance 109497 ;
    seadots:sss 3.499e+01 ;
    seadots:sst 8.81e+00 ;
    seadots:subclass "Eumalacostraca" ;
    seadots:subclassid 1086 ;
    seadots:suborder "Amphilochidea" ;
    seadots:suborderid 1055678 ;
    seadots:subphylum "Crustacea" ;
    seadots:subphylumid 1066 ;
    seadots:superclass "Multicrustacea" ;
    seadots:superclassid 845959 ;
    seadots:superfamily "Lysianassoidea" ;
    seadots:superfamilyid 176788 ;
    seadots:superorder "Peracarida" ;
    seadots:superorderid 1090 ;
    seadots:wrims true ;
    seadots:year "2012" .

<file:///github/workspace/0002100b-ad82-4d11-be10-c47f18f30c21> dcterms:isPartOf "d556b9d4-7625-4aa2-894d-441eabae47f7",
        "https://marineinfo.org/id/dataset/4539" ;
    dcterms:title "grab_2006-2022" ;
    dwc:basisOfRecord "Occurrence" ;
    dwc:class "Polychaeta" ;
    dwc:decimalLatitude 6.759528e+01 ;
    dwc:decimalLongitude 9.307715e+00 ;
    dwc:eventDate "2012-05-04T23:33:00+00:00" ;
    dwc:eventID "Cruise: 58GS-2012106 Sample: 66" ;
    dwc:family "Acrocirridae" ;
    dwc:genus "Actaedrilus" ;
    dwc:kingdom "Animalia" ;
    dwc:maximumDepthInMeters 9.1303e+02 ;
    dwc:minimumDepthInMeters 9.1303e+02 ;
    dwc:occurrenceID "081880066019034" ;
    dwc:order "Terebellida" ;
    dwc:phylum "Annelida" ;
    dwc:samplingProtocol "Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0" ;
    dwc:scientificName "Actaedrilus polyonyx" ;
    dwc:scientificNameAuthorship "Eliason, 1962" ;
    dwc:specificEpithet "Actaedrilus polyonyx" ;
    dwc:taxonID 1473437 ;
    seadots:absence false ;
    seadots:bathymetry 9.168e+02 ;
    seadots:brackish false ;
    seadots:catalogNumber "081880066019034" ;
    seadots:classid 883 ;
    seadots:collectionCode "IMRMarbunnBenthos" ;
    seadots:continent "Norwegian Sea" ;
    seadots:date_end 1336089600000 ;
    seadots:date_mid 1336089600000 ;
    seadots:date_start 1336089600000 ;
    seadots:date_year 2012 ;
    seadots:day "4" ;
    seadots:dropped false ;
    seadots:eventTime "23:33:00+00:00" ;
    seadots:familyid 920 ;
    seadots:fieldNumber "catchId: 34" ;
    seadots:genusid 1473424 ;
    seadots:infraclass "Canalipalpata" ;
    seadots:infraclassid 154974 ;
    seadots:institutionCode "IMR" ;
    seadots:kingdomid 2 ;
    seadots:locality "MAREANO Reference Station: 818" ;
    seadots:marine true ;
    seadots:modified "2024-05-23 10:35:05" ;
    seadots:month "5" ;
    seadots:node_id "4bf79a01-65a9-4db6-b37b-18434f26ddfc" ;
    seadots:occurrenceStatus "present" ;
    seadots:orderid 900 ;
    seadots:originalScientificName "Actaedrilus polyonyx" ;
    seadots:phylumid 882 ;
    seadots:scientificNameID "urn:lsid:marinespecies.org:taxname:1473437" ;
    seadots:shoredistance 109430 ;
    seadots:speciesid 1473437 ;
    seadots:sss 3.499e+01 ;
    seadots:sst 8.94e+00 ;
    seadots:subclass "Sedentaria" ;
    seadots:subclassid 754175 ;
    seadots:suborder "Cirratuliformia" ;
    seadots:suborderid 155087 ;
    seadots:year "2012" .

<file:///github/workspace/00029056-f56d-45f4-a1db-f6bbd2350903> dcterms:isPartOf "14fa3c3e-259c-4af9-9314-eee1dc3a119b",
        "https://marineinfo.org/id/dataset/4540" ;
    dcterms:title "beamtrawl_2006-2022" ;
    dwc:basisOfRecord "Occurrence" ;
    dwc:class "Calcarea" ;
    dwc:decimalLatitude 7.4997e+01 ;
    dwc:decimalLongitude 2.59995e+01 ;
    dwc:eventDate "2016-09-28T00:41:00+00:00/2016-09-28T00:46:00+00:00" ;
    dwc:eventID "Cruise: 58GS-2016113 Sample: 18" ;
    dwc:kingdom "Animalia" ;
    dwc:maximumDepthInMeters 2.0845e+02 ;
    dwc:minimumDepthInMeters 2.0756e+02,
        2.08005e+02 ;
    dwc:occurrenceID "164910018001034" ;
    dwc:order "Leucosolenida" ;
    dwc:phylum "Porifera" ;
    dwc:samplingProtocol "Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0" ;
    dwc:scientificName "Leucosolenida" ;
    dwc:taxonID 131591 ;
    seadots:absence false ;
    seadots:bathymetry 219 ;
    seadots:brackish false ;
    seadots:catalogNumber "164910018001034" ;
    seadots:classid 559 ;
    seadots:collectionCode "IMRMarbunnBenthos" ;
    seadots:continent "Barents Sea" ;
    seadots:date_end 1475020800000 ;
    seadots:date_mid 1475020800000 ;
    seadots:date_start 1475020800000 ;
    seadots:date_year 2016 ;
    seadots:day "28" ;
    seadots:dropped false ;
    seadots:eventTime "00:41:00+00:00/00:46:00+00:00" ;
    seadots:fieldNumber "catchId: 34" ;
    seadots:footprintWKT "LINESTRING(25.9995 74.997,25.9995 74.994833)" ;
    seadots:institutionCode "IMR" ;
    seadots:kingdomid 2 ;
    seadots:locality "MAREANO Reference Station: 1649" ;
    seadots:marine true ;
    seadots:modified "2024-05-23 10:35:05" ;
    seadots:month "9" ;
    seadots:node_id "4bf79a01-65a9-4db6-b37b-18434f26ddfc" ;
    seadots:occurrenceStatus "present" ;
    seadots:orderid 131591 ;
    seadots:originalScientificName "Leucosolenida" ;
    seadots:phylumid 558 ;
    seadots:scientificNameID "urn:lsid:marinespecies.org:taxname:131591" ;
    seadots:shoredistance 163319 ;
    seadots:sss 3.468e+01 ;
    seadots:sst 3.35e+00 ;
    seadots:subclass "Calcaronea" ;
    seadots:subclassid 131584 ;
    seadots:wrims true ;
    seadots:year "2016" .

<file:///github/workspace/0002e38c-8260-4f5d-9bc4-1895860fbcb8> dcterms:isPartOf "14fa3c3e-259c-4af9-9314-eee1dc3a119b",
        "https://marineinfo.org/id/dataset/4540" ;
    dcterms:title "beamtrawl_2006-2022" ;
    dwc:basisOfRecord "Occurrence" ;
    dwc:class "Polychaeta" ;
    dwc:decimalLatitude 7.35475e+01 ;
    dwc:decimalLongitude 2.391317e+01 ;
    dwc:eventDate "2017-04-06T03:41:00+00:00/2017-04-06T03:46:00+00:00" ;
    dwc:eventID "Cruise: 58GS-2017103 Sample: 9" ;
    dwc:family "Sabellidae" ;
    dwc:genus "Chone" ;
    dwc:kingdom "Animalia" ;
    dwc:maximumDepthInMeters 4.491e+02 ;
    dwc:minimumDepthInMeters 4.4885e+02,
        4.48975e+02 ;
    dwc:occurrenceID "171710009001042" ;
    dwc:order "Sabellida" ;
    dwc:phylum "Annelida" ;
    dwc:samplingProtocol "Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0" ;
    dwc:scientificName "Chone" ;
    dwc:scientificNameAuthorship "Krøyer, 1856" ;
    dwc:taxonID 129525 ;
    seadots:absence false ;
    seadots:bathymetry 4.534e+02 ;
    seadots:brackish false ;
    seadots:catalogNumber "171710009001042" ;
    seadots:classid 883 ;
    seadots:collectionCode "IMRMarbunnBenthos" ;
    seadots:continent "Barents Sea" ;
    seadots:date_end 1491436800000 ;
    seadots:date_mid 1491436800000 ;
    seadots:date_start 1491436800000 ;
    seadots:date_year 2017 ;
    seadots:day "6" ;
    seadots:dropped false ;
    seadots:eventTime "03:41:00+00:00/03:46:00+00:00" ;
    seadots:familyid 985 ;
    seadots:fieldNumber "catchId: 42" ;
    seadots:footprintWKT "LINESTRING(23.913167 73.5475,23.909547 73.54935)" ;
    seadots:genusid 129525 ;
    seadots:infraclass "Canalipalpata" ;
    seadots:infraclassid 154974 ;
    seadots:institutionCode "IMR" ;
    seadots:kingdomid 2 ;
    seadots:locality "MAREANO Reference Station: 1717" ;
    seadots:marine true ;
    seadots:modified "2024-05-23 10:35:05" ;
    seadots:month "4" ;
    seadots:node_id "4bf79a01-65a9-4db6-b37b-18434f26ddfc" ;
    seadots:occurrenceStatus "present" ;
    seadots:orderid 901 ;
    seadots:originalScientificName "Chone" ;
    seadots:phylumid 882 ;
    seadots:scientificNameID "urn:lsid:marinespecies.org:taxname:129525" ;
    seadots:shoredistance 171175 ;
    seadots:sss 3.503e+01 ;
    seadots:sst 5.67e+00 ;
    seadots:subclass "Sedentaria" ;
    seadots:subclassid 754175 ;
    seadots:subfamily "Myxicolinae" ;
    seadots:subfamilyid 1470421 ;
    seadots:tribe "Myxicolini" ;
    seadots:tribeid 1470460 ;
    seadots:wrims true ;
    seadots:year "2017" .

<file:///github/workspace/00054ffb-17c9-46eb-9aeb-72252a6b90d8> dcterms:isPartOf "d556b9d4-7625-4aa2-894d-441eabae47f7",
        "https://marineinfo.org/id/dataset/4539" ;
    dcterms:title "grab_2006-2022" ;
    dwc:basisOfRecord "Occurrence" ;
    dwc:class "Gastropoda" ;
    dwc:decimalLatitude 7.041183e+01 ;
    dwc:decimalLongitude 1.870433e+01 ;
    dwc:eventDate "2010-08-11T00:40:00+00:00" ;
    dwc:eventID "Cruise: 58GS-2010110 Sample: 417" ;
    dwc:family "Buccinidae" ;
    dwc:genus "Buccinum" ;
    dwc:kingdom "Animalia" ;
    dwc:maximumDepthInMeters 1.0047e+02 ;
    dwc:minimumDepthInMeters 1.0047e+02 ;
    dwc:occurrenceID "059290417049111" ;
    dwc:order "Neogastropoda" ;
    dwc:phylum "Mollusca" ;
    dwc:samplingProtocol "VVgrab020,Subsample method: Sieve content - Mesh size (mm): 1.0" ;
    dwc:scientificName "Buccinum finmarkianum" ;
    dwc:scientificNameAuthorship "Verkrüzen, 1875" ;
    dwc:specificEpithet "Buccinum finmarkianum" ;
    dwc:taxonID 160143 ;
    seadots:absence false ;
    seadots:bathymetry 9.66e+01 ;
    seadots:brackish false ;
    seadots:catalogNumber "059290417049111" ;
    seadots:classid 101 ;
    seadots:collectionCode "IMRMarbunnBenthos" ;
    seadots:continent "Norwegian Sea" ;
    seadots:date_end 1281484800000 ;
    seadots:date_mid 1281484800000 ;
    seadots:date_start 1281484800000 ;
    seadots:date_year 2010 ;
    seadots:day "11" ;
    seadots:dropped false ;
    seadots:eventTime "00:40:00+00:00" ;
    seadots:familyid 149 ;
    seadots:fieldNumber "catchId: 111" ;
    seadots:genusid 137701 ;
    seadots:institutionCode "IMR" ;
    seadots:kingdomid 2 ;
    seadots:locality "MAREANO Reference Station: 592" ;
    seadots:marine true ;
    seadots:modified "2024-05-23 10:35:05" ;
    seadots:month "8" ;
    seadots:node_id "4bf79a01-65a9-4db6-b37b-18434f26ddfc" ;
    seadots:occurrenceStatus "present" ;
    seadots:orderid 146 ;
    seadots:originalScientificName "Buccinum finmarkianum" ;
    seadots:phylumid 51 ;
    seadots:scientificNameID "urn:lsid:marinespecies.org:taxname:160143" ;
    seadots:shoredistance 21556 ;
    seadots:speciesid 160143 ;
    seadots:sss 3.446e+01 ;
    seadots:sst 7.26e+00 ;
    seadots:subclass "Caenogastropoda" ;
    seadots:subclassid 224570 ;
    seadots:subfamily "Buccininae" ;
    seadots:subfamilyid 225649 ;
    seadots:superfamily "Buccinoidea" ;
    seadots:superfamilyid 382214 ;
    seadots:year "2010" .

<file:///github/workspace/0007423f-403a-44d2-9565-281acbe343ce> dcterms:isPartOf "d556b9d4-7625-4aa2-894d-441eabae47f7",
        "https://marineinfo.org/id/dataset/4539" ;
    dcterms:title "grab_2006-2022" ;
    dwc:basisOfRecord "Occurrence" ;
    dwc:class "Echinoidea" ;
    dwc:decimalLatitude 6.206072e+01 ;
    dwc:decimalLongitude 1.414981e+00 ;
    dwc:eventDate "2021-05-03T12:22:00+00:00" ;
    dwc:eventID "Cruise: 58GS-2021104 Sample: 119" ;
    dwc:family "Brissidae" ;
    dwc:genus "Brissopsis" ;
    dwc:kingdom "Animalia" ;
    dwc:maximumDepthInMeters 369 ;
    dwc:minimumDepthInMeters 369 ;
    dwc:occurrenceID "253740119001007" ;
    dwc:order "Spatangoida" ;
    dwc:phylum "Echinodermata" ;
    dwc:samplingProtocol "Small VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0" ;
    dwc:scientificName "Brissopsis lyrifera" ;
    dwc:scientificNameAuthorship "(Forbes, 1841)" ;
    dwc:specificEpithet "Brissopsis lyrifera" ;
    dwc:taxonID 124373 ;
    seadots:absence false ;
    seadots:bathymetry 3.624e+02 ;
    seadots:brackish false ;
    seadots:catalogNumber "253740119001007" ;
    seadots:classid 123082 ;
    seadots:collectionCode "IMRMarbunnBenthos" ;
    seadots:continent "Norwegian Sea" ;
    seadots:date_end 1620000000000 ;
    seadots:date_mid 1620000000000 ;
    seadots:date_start 1620000000000 ;
    seadots:date_year 2021 ;
    seadots:day "3" ;
    seadots:dropped false ;
    seadots:eventTime "12:22:00+00:00" ;
    seadots:familyid 123173 ;
    seadots:fieldNumber "catchId: 7" ;
    seadots:genusid 123418 ;
    seadots:infraclass "Irregularia" ;
    seadots:infraclassid 510499 ;
    seadots:institutionCode "IMR" ;
    seadots:kingdomid 2 ;
    seadots:locality "MAREANO Reference Station: 2537" ;
    seadots:marine true ;
    seadots:modified "2024-05-23 10:35:05" ;
    seadots:month "5" ;
    seadots:node_id "4bf79a01-65a9-4db6-b37b-18434f26ddfc" ;
    seadots:occurrenceStatus "present" ;
    seadots:orderid 123106 ;
    seadots:originalScientificName "Brissopsis lyrifera" ;
    seadots:phylumid 1806 ;
    seadots:scientificNameID "urn:lsid:marinespecies.org:taxname:124373" ;
    seadots:shoredistance 171442 ;
    seadots:speciesid 124373 ;
    seadots:sss 3.53e+01 ;
    seadots:sst 1.007e+01 ;
    seadots:subclass "Euechinoidea" ;
    seadots:subclassid 149854 ;
    seadots:subfamily "Brissopsinae" ;
    seadots:subfamilyid 510878 ;
    seadots:suborder "Brissidina" ;
    seadots:suborderid 510538 ;
    seadots:subphylum "Echinozoa" ;
    seadots:subphylumid 148744 ;
    seadots:subterclass "Atelostomata" ;
    seadots:subterclassid 149864 ;
    seadots:year "2021" .

<file:///github/workspace/0007ec71-87e5-4701-8474-ac409618ed43> dcterms:isPartOf "d556b9d4-7625-4aa2-894d-441eabae47f7",
        "https://marineinfo.org/id/dataset/4539" ;
    dcterms:title "grab_2006-2022" ;
    dwc:basisOfRecord "Occurrence" ;
    dwc:class "Holothuroidea" ;
    dwc:decimalLatitude 6.562971e+01 ;
    dwc:decimalLongitude 1.061101e+01 ;
    dwc:eventDate "2020-07-23T20:38:00+00:00" ;
    dwc:eventID "Cruise: 58GS-2020110 Sample: 90" ;
    dwc:family "Ypsilothuriidae" ;
    dwc:genus "Echinocucumis" ;
    dwc:kingdom "Animalia" ;
    dwc:maximumDepthInMeters 3.7678e+02 ;
    dwc:minimumDepthInMeters 3.7678e+02 ;
    dwc:occurrenceID "227940090001039" ;
    dwc:order "Dendrochirotida" ;
    dwc:phylum "Echinodermata" ;
    dwc:samplingProtocol "Small VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0" ;
    dwc:scientificName "Echinocucumis hispida" ;
    dwc:scientificNameAuthorship "(Barrett, 1857)" ;
    dwc:specificEpithet "Echinocucumis hispida" ;
    dwc:taxonID 124593 ;
    seadots:absence false ;
    seadots:bathymetry 3.938e+02 ;
    seadots:brackish false ;
    seadots:catalogNumber "227940090001039" ;
    seadots:classid 123083 ;
    seadots:collectionCode "IMRMarbunnBenthos" ;
    seadots:continent "Norwegian Sea" ;
    seadots:date_end 1595462400000 ;
    seadots:date_mid 1595462400000 ;
    seadots:date_start 1595462400000 ;
    seadots:date_year 2020 ;
    seadots:day "23" ;
    seadots:dropped false ;
    seadots:eventTime "20:38:00+00:00" ;
    seadots:familyid 123186 ;
    seadots:fieldNumber "catchId: 39" ;
    seadots:genusid 123473 ;
    seadots:institutionCode "IMR" ;
    seadots:kingdomid 2 ;
    seadots:locality "MAREANO Reference Station: 2279" ;
    seadots:marine true ;
    seadots:modified "2024-05-23 10:35:05" ;
    seadots:month "7" ;
    seadots:node_id "4bf79a01-65a9-4db6-b37b-18434f26ddfc" ;
    seadots:occurrenceStatus "present" ;
    seadots:orderid 123111 ;
    seadots:originalScientificName "Echinocucumis hispida" ;
    seadots:phylumid 1806 ;
    seadots:scientificNameID "urn:lsid:marinespecies.org:taxname:124593" ;
    seadots:shoredistance 30052 ;
    seadots:speciesid 124593 ;
    seadots:sss 3.432e+01 ;
    seadots:sst 9.36e+00 ;
    seadots:subclass "Actinopoda" ;
    seadots:subclassid 1393249 ;
    seadots:subphylum "Echinozoa" ;
    seadots:subphylumid 148744 ;
    seadots:year "2020" .

<file:///github/workspace/00087d31-412d-48ce-bed8-9ade8d5b80f5> dcterms:isPartOf "14fa3c3e-259c-4af9-9314-eee1dc3a119b",
        "https://marineinfo.org/id/dataset/4540" ;
    dcterms:title "beamtrawl_2006-2022" ;
    dwc:basisOfRecord "Occurrence" ;
    dwc:class "Malacostraca" ;
    dwc:decimalLatitude 7.128768e+01 ;
    dwc:decimalLongitude 2.213325e+01 ;
    dwc:eventDate "2006-05-28T02:33:00+00:00/2006-05-28T02:39:00+00:00" ;
    dwc:eventID "Cruise: 58AA-2006612 Sample: 8" ;
    dwc:family "Munididae" ;
    dwc:genus "Munida" ;
    dwc:kingdom "Animalia" ;
    dwc:maximumDepthInMeters 3.218e+02 ;
    dwc:minimumDepthInMeters 3.205e+02,
        3.2115e+02 ;
    dwc:occurrenceID "000810008002016" ;
    dwc:order "Decapoda" ;
    dwc:phylum "Arthropoda" ;
    dwc:samplingProtocol "Beamtrawl,Subsample method: Sieve content - Mesh size (mm): 5.0" ;
    dwc:scientificName "Munida sarsi" ;
    dwc:scientificNameAuthorship "Huus, 1935" ;
    dwc:specificEpithet "Munida sarsi" ;
    dwc:taxonID 107163 ;
    seadots:absence false ;
    seadots:bathymetry 3.196e+02 ;
    seadots:brackish false ;
    seadots:catalogNumber "000810008002016" ;
    seadots:classid 1071 ;
    seadots:collectionCode "IMRMarbunnBenthos" ;
    seadots:continent "Barents Sea" ;
    seadots:date_end 1148774400000 ;
    seadots:date_mid 1148774400000 ;
    seadots:date_start 1148774400000 ;
    seadots:date_year 2006 ;
    seadots:day "28" ;
    seadots:dropped false ;
    seadots:eventTime "02:33:00+00:00/02:39:00+00:00" ;
    seadots:familyid 562645 ;
    seadots:fieldNumber "catchId: 16" ;
    seadots:footprintWKT "LINESTRING(22.133255 71.287677,22.13529 71.289484)" ;
    seadots:genusid 106835 ;
    seadots:infraorder "Anomura" ;
    seadots:infraorderid 106671 ;
    seadots:institutionCode "IMR" ;
    seadots:kingdomid 2 ;
    seadots:locality "MAREANO Reference Station: 8" ;
    seadots:marine true ;
    seadots:modified "2024-05-23 10:35:05" ;
    seadots:month "5" ;
    seadots:node_id "4bf79a01-65a9-4db6-b37b-18434f26ddfc" ;
    seadots:occurrenceStatus "present" ;
    seadots:orderid 1130 ;
    seadots:originalScientificName "Munida sarsi" ;
    seadots:phylumid 1065 ;
    seadots:scientificNameID "urn:lsid:marinespecies.org:taxname:107163" ;
    seadots:shoredistance 53735 ;
    seadots:speciesid 107163 ;
    seadots:sss 3.491e+01 ;
    seadots:sst 7.06e+00 ;
    seadots:subclass "Eumalacostraca" ;
    seadots:subclassid 1086 ;
    seadots:suborder "Pleocyemata" ;
    seadots:suborderid 106670 ;
    seadots:subphylum "Crustacea" ;
    seadots:subphylumid 1066 ;
    seadots:superclass "Multicrustacea" ;
    seadots:superclassid 845959 ;
    seadots:superfamily "Galatheoidea" ;
    seadots:superfamilyid 106685 ;
    seadots:superorder "Eucarida" ;
    seadots:superorderid 1089 ;
    seadots:year "2006" .

<file:///github/workspace/0009bf51-340c-4fa4-ba3d-ce3300291d9c> dcterms:isPartOf "d556b9d4-7625-4aa2-894d-441eabae47f7",
        "https://marineinfo.org/id/dataset/4539" ;
    dcterms:title "grab_2006-2022" ;
    dwc:basisOfRecord "Occurrence" ;
    dwc:class "Ophiuroidea" ;
    dwc:decimalLatitude 7.132973e+01 ;
    dwc:decimalLongitude 2.24153e+01 ;
    dwc:eventDate "2006-06-06T00:19:00+00:00" ;
    dwc:eventID "Cruise: 58AA-2006612 Sample: 58" ;
    dwc:kingdom "Animalia" ;
    dwc:maximumDepthInMeters 4.3462e+02 ;
    dwc:minimumDepthInMeters 4.3462e+02 ;
    dwc:occurrenceID "000380058031020" ;
    dwc:phylum "Echinodermata" ;
    dwc:samplingProtocol "Large VV grab,Subsample method: Sieve content - Mesh size (mm): 1.0" ;
    dwc:scientificName "Ophiuroidea" ;
    dwc:scientificNameAuthorship "Gray, 1840" ;
    dwc:taxonID 123084 ;
    seadots:absence false ;
    seadots:bathymetry 4.364e+02 ;
    seadots:brackish true ;
    seadots:catalogNumber "000380058031020" ;
    seadots:classid 123084 ;
    seadots:collectionCode "IMRMarbunnBenthos" ;
    seadots:continent "Barents Sea" ;
    seadots:date_end 1149552000000 ;
    seadots:date_mid 1149552000000 ;
    seadots:date_start 1149552000000 ;
    seadots:date_year 2006 ;
    seadots:day "6" ;
    seadots:dropped false ;
    seadots:eventTime "00:19:00+00:00" ;
    seadots:fieldNumber "catchId: 20" ;
    seadots:institutionCode "IMR" ;
    seadots:kingdomid 2 ;
    seadots:locality "MAREANO Reference Station: 3" ;
    seadots:marine true ;
    seadots:modified "2024-05-23 10:35:05" ;
    seadots:month "6" ;
    seadots:node_id "4bf79a01-65a9-4db6-b37b-18434f26ddfc" ;
    seadots:occurrenceStatus "present" ;
    seadots:originalScientificName "Ophiuroidea" ;
    seadots:phylumid 1806 ;
    seadots:scientificNameID "urn:lsid:marinespecies.org:taxname:123084" ;
    seadots:shoredistance 53639 ;
    seadots:sss 3.491e+01 ;
    seadots:sst 7.04e+00 ;
    seadots:subphylum "Asterozoa" ;
    seadots:subphylumid 148743 ;
    seadots:wrims true ;
    seadots:year "2006" .

[] seadots:checklistResult <file:///github/workspace/00014e73-67d6-40ce-919f-0ca40089c1e6>,
        <file:///github/workspace/0001e2dc-e4c7-4fd0-9214-7c643a7d7c4a>,
        <file:///github/workspace/0002100b-ad82-4d11-be10-c47f18f30c21>,
        <file:///github/workspace/00029056-f56d-45f4-a1db-f6bbd2350903>,
        <file:///github/workspace/0002e38c-8260-4f5d-9bc4-1895860fbcb8>,
        <file:///github/workspace/00054ffb-17c9-46eb-9aeb-72252a6b90d8>,
        <file:///github/workspace/0007423f-403a-44d2-9565-281acbe343ce>,
        <file:///github/workspace/0007ec71-87e5-4701-8474-ac409618ed43>,
        <file:///github/workspace/00087d31-412d-48ce-bed8-9ade8d5b80f5>,
        <file:///github/workspace/0009bf51-340c-4fa4-ba3d-ce3300291d9c> ;
    seadots:totalChecklistRows 105687 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: OBIS MAREANO Checklist
description: 'Raw OBIS checklist or occurrence response for selected MAREANO dataset
  identifiers. The payload is intentionally kept in the OBIS API shape: a total count
  and a `results` array of checklist rows or occurrence records.

  '
type: object
required:
- total
- results
properties:
  total:
    type: integer
    minimum: 0
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/obis-mareano-checklist#totalChecklistRows
  results:
    type: array
    items:
      type: object
      required:
      - scientificName
      properties:
        scientificName:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/scientificName
        scientificNameAuthorship:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/scientificNameAuthorship
        taxonID:
          type: integer
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/taxonID
        aphiaID:
          type: integer
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/taxonID
        acceptedNameUsage:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/acceptedNameUsage
        acceptedNameUsageID:
          type: integer
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/acceptedNameUsageID
        taxonRank:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/taxonRank
        taxonomicStatus:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/taxonomicStatus
        records:
          type: integer
          minimum: 0
          x-jsonld-id: https://api.obis.org/v3/terms/records
        id:
          type: string
          x-jsonld-id: '@id'
        occurrenceID:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/occurrenceID
        basisOfRecord:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/basisOfRecord
        dataset_id:
          type: string
          x-jsonld-id: http://purl.org/dc/terms/isPartOf
        datasetID:
          type: string
          x-jsonld-id: http://purl.org/dc/terms/isPartOf
        datasetName:
          type: string
          x-jsonld-id: http://purl.org/dc/terms/title
        decimalLatitude:
          type: number
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/decimalLatitude
        decimalLongitude:
          type: number
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/decimalLongitude
        eventDate:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/eventDate
        eventID:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/eventID
        samplingProtocol:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/samplingProtocol
        depth:
          type: number
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/minimumDepthInMeters
        minimumDepthInMeters:
          type: number
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/minimumDepthInMeters
        maximumDepthInMeters:
          type: number
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/maximumDepthInMeters
        ncbi_id:
          type: integer
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/obis-mareano-checklist#ncbiId
        wrims:
          type: boolean
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/obis-mareano-checklist#wrims
        is_marine:
          type: boolean
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/marine
        is_brackish:
          type: boolean
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/obis-mareano-checklist#isBrackish
        is_freshwater:
          type: boolean
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/obis-mareano-checklist#isFreshwater
        is_terrestrial:
          type: boolean
          x-jsonld-id: https://w3id.org/ogc/hosted/seadots/obis-mareano-checklist#isTerrestrial
        kingdom:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/kingdom
        phylum:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/phylum
        class:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/class
        order:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/order
        family:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/family
        genus:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/genus
        species:
          type: string
          x-jsonld-id: http://rs.tdwg.org/dwc/terms/specificEpithet
      additionalProperties: true
    x-jsonld-id: https://w3id.org/ogc/hosted/seadots/obis-mareano-checklist#checklistResult
    x-jsonld-container: '@set'
additionalProperties: true
x-jsonld-vocab: https://w3id.org/ogc/hosted/seadots/obis-mareano-checklist#
x-jsonld-prefixes:
  seadots: https://w3id.org/ogc/hosted/seadots/obis-mareano-checklist#
  dwc: http://rs.tdwg.org/dwc/terms/
  obis: https://api.obis.org/v3/terms/
  dcterms: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/obis-mareano-checklist/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/obis-mareano-checklist/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/ogc/hosted/seadots/obis-mareano-checklist#",
    "total": "seadots:totalChecklistRows",
    "results": {
      "@context": {
        "scientificName": "dwc:scientificName",
        "scientificNameAuthorship": "dwc:scientificNameAuthorship",
        "taxonID": "dwc:taxonID",
        "aphiaID": "dwc:taxonID",
        "acceptedNameUsage": "dwc:acceptedNameUsage",
        "acceptedNameUsageID": "dwc:acceptedNameUsageID",
        "taxonRank": "dwc:taxonRank",
        "taxonomicStatus": "dwc:taxonomicStatus",
        "records": "obis:records",
        "id": "@id",
        "occurrenceID": "dwc:occurrenceID",
        "basisOfRecord": "dwc:basisOfRecord",
        "dataset_id": "dcterms:isPartOf",
        "datasetID": "dcterms:isPartOf",
        "datasetName": "dcterms:title",
        "decimalLatitude": "dwc:decimalLatitude",
        "decimalLongitude": "dwc:decimalLongitude",
        "eventDate": "dwc:eventDate",
        "eventID": "dwc:eventID",
        "samplingProtocol": "dwc:samplingProtocol",
        "depth": "dwc:minimumDepthInMeters",
        "minimumDepthInMeters": "dwc:minimumDepthInMeters",
        "maximumDepthInMeters": "dwc:maximumDepthInMeters",
        "ncbi_id": "seadots:ncbiId",
        "wrims": "seadots:wrims",
        "is_marine": "dwc:marine",
        "is_brackish": "seadots:isBrackish",
        "is_freshwater": "seadots:isFreshwater",
        "is_terrestrial": "seadots:isTerrestrial",
        "kingdom": "dwc:kingdom",
        "phylum": "dwc:phylum",
        "class": "dwc:class",
        "order": "dwc:order",
        "family": "dwc:family",
        "genus": "dwc:genus",
        "species": "dwc:specificEpithet"
      },
      "@id": "seadots:checklistResult",
      "@container": "@set"
    },
    "seadots": "https://w3id.org/ogc/hosted/seadots/obis-mareano-checklist#",
    "dwc": "http://rs.tdwg.org/dwc/terms/",
    "obis": "https://api.obis.org/v3/terms/",
    "dcterms": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-seadots/build/annotated/hosted/seadots/obis-mareano-checklist/context.jsonld)

## Sources

* [OBIS checklist API](https://api.obis.org/v3/checklist)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-seadots](https://github.com/ogcincubator/bblocks-seadots)
* Path: `_sources/obis-mareano-checklist`

