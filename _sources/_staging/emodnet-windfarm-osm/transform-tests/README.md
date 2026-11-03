From the repository root, run:

```sh
python3 _sources/_staging/emodnet-windfarm-osm/transform-tests/test_transform.py
```

The test runs the declared transform on the complete BB1 source example, compares
the result with the checked-in BB2 example, and checks preservation of each
source feature field and property as well as key mappings and the null-geometry
relation.
