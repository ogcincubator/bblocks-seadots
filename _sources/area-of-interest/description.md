# Marine Area of Interest

Simple GeoJSON Feature profile for a polygon delimiting a marine area of
interest.

The AOI polygon is carried only by the top-level GeoJSON `geometry` member.
The `properties` object carries only a human-readable `title` and
`description`. Derived values such as bbox, centroid, area, CRS, and provenance
are intentionally omitted to avoid duplicating information that can be computed
from the geometry or managed by a separate metadata record.
