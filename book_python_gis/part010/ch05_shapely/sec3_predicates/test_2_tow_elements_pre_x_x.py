#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from shapely.geometry import Point, LineString
coords = [(0, 0), (1, 1)]
LineString(coords).contains(Point(0.5, 0.5))
Point(0.5, 0.5).within(LineString(coords))
###############################################################################
LineString(coords).contains(Point(1.0, 1.0))
###############################################################################
line = LineString(coords)
contained = filter(line.contains, [Point(), Point(0.5, 0.5)])
for g in contained: print(g.wkt)

###############################################################################
LineString(coords).crosses(LineString([(0, 1), (1, 0)]))
###############################################################################
LineString(coords).crosses(Point(0.5, 0.5))
###############################################################################
Point(0, 0).disjoint(Point(1, 1))
###############################################################################
a = LineString([(0, 0), (1, 1)])
b = LineString([(0, 0), (0.5, 0.5), (1, 1)])
c = LineString([(0, 0), (0, 0), (1, 1)])
a.equals(b)
b.equals(c)
###############################################################################
a = LineString([(0, 0), (1, 1)])
b = LineString([(1, 1), (2, 2)])
a.touches(b)
