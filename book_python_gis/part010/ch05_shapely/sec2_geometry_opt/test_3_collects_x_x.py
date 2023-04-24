#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from shapely.geometry import LineString
a = LineString([(0, 0), (1,1), (1,2), (2,2)])
b = LineString([(0, 0), (1,1), (2,1), (2,2)])
c = a.intersection(b)
len(c)
c.wkt
###############################################################################
for g in c: print(g.wkt)

for g in c.geoms: print(g.wkt)

###############################################################################
c.geoms[0].wkt
c[1].wkt
###############################################################################
from shapely.geometry import MultiPoint
points = MultiPoint([(0.0, 0.0), (1.0, 1.0)])
points.area
points.length
points.bounds
###############################################################################
from shapely.geometry import MultiLineString
coords = [((0, 0), (1, 1)), ((-1, 0), (1, 0))]
lines = MultiLineString(coords)
lines.area
lines.length
lines.bounds
len(lines.geoms)
###############################################################################
polygon = [(0, 0), (1,1), (1,2), (2,2),(0,0)]
s = [(10, 0), (21,1), (31,2), (24,2),(10,0)]
t = [(0, 50), (1,21), (1,22), (32,2),(0,50)]
from shapely.geometry import Polygon
p_a, s_a, t_a = [Polygon(x) for x in  [polygon, s, t]]
from shapely.geometry import MultiPolygon
polygons = MultiPolygon([p_a, s_a, t_a])
len(polygons.geoms)
len(polygons)
polygons.bounds
