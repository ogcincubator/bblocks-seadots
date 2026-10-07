# EMODnet-view collection description

Profile of the OGC API - Features collection description (`/collections/{collectionId}`) for a
collection that serves an **EMODnet-compliant view** of a national or regional source, next to the
unchanged source collection on the same API.

A client must be able to find out from the collection description alone which EMODnet profile the
items follow, where they came from and how they were derived. The profile therefore requires these
links in addition to the standard members:

| `rel` | Target | Why |
|---|---|---|
| `profile` | the EMODnet target building block (`nationally-designated-area` or `rsc-mpa`) | RFC 6906: the items conform to it |
| `describedby` (`application/schema+json`) | the annotated item schema of that block | OGC API - Features Part 5 style schema |
| `http://www.opengis.net/def/rel/ogc/1.0/queryables` | the collection's queryables | filters use EMODnet attribute names, so `designatio=NO05` works on both services |
| `derived-from` | the source collection on the same API | provenance of every item |
| `related` | the corresponding EMODnet Human Activities layer | where the same sites are published by EMODnet |
| `license` | the source licence | the view inherits the source's terms |

The collection id must start with `emodnet-view-`, `itemType` is `feature` and CRS84 must be offered.
A link to the transform report (`seadotsTransformReport`, see `protected-area.transform-report`) is
recommended, so clients can see which sites were excluded, routed or differ from EMODnet.

pygeoapi provides all of these through the per-resource `links:` setting.

The examples are **illustrative target designs**: the two views are specified but not yet deployed.
