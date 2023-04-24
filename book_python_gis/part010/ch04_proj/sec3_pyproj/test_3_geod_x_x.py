#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from pyproj import Geod
g=Geod(ellps='krass')
###############################################################################
miniearth=Geod(a=2,b=1.97)
###############################################################################
###############################################################################
g.fwd(91, 29.6, 52.88778703659133,3419167.0426993747)
###############################################################################
###############################################################################
g.inv(91, 29.6, 125.35, 43.88333)
###############################################################################
###############################################################################
g = Geod(ellps='krass')
lasa_lat = 29.6; lasa_lon = 91
cc_lat = 43.88333; cc_lon = 125.35
###############################################################################
lonlats = g.npts(lasa_lon,lasa_lat,cc_lon,cc_lat,4)
for lon,lat in lonlats: print('%6.3f  %7.3f' % (lat, lon))

