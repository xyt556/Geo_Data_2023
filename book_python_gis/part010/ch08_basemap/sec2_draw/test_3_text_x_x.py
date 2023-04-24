#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import matplotlib
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['STKaiti']
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
para = {'projection': 'merc', 'lat_0': 0, 'lon_0': 120,
    'resolution': 'h', 'area_thresh': .1,
    'llcrnrlon': 116,  'llcrnrlat': 36.6,
    'urcrnrlon': 124,  'urcrnrlat': 40.2 }
my_map = Basemap(**para)
my_map.drawcoastlines(); my_map.drawmapboundary()
###############################################################################
lon =  121.60001; lat = 38.91027
x, y = my_map(lon, lat)
plt.text(x, y, '大连',fontsize=12,fontweight='bold',
    ha='left',va='bottom',color='k')
lon = 121.38617; lat = 37.53042
x, y = my_map(lon, lat)
plt.text(x, y, '烟台',fontsize=12,fontweight='bold',
    ha='left',va='center',color='k',
    bbox=dict(facecolor='b', alpha=0.2))
plt.show()
