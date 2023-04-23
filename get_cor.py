import fiona
from shapely.geometry import shape

with fiona.open(r"D:\SGDownload\landuse2020\行政区划.shp") as src:
    for row in src:
        geom = shape(row['geometry'])
        if geom.geom_type == 'Polygon' and not geom.is_valid:
            geom = geom.buffer(0)
        for point in geom.exterior.coords:
            print(point)
