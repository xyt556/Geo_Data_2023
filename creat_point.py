import geopandas as gpd
from shapely.geometry import Point

# 创建一个空的 GeoDataFrame，指定坐标系为 WGS84
crs = "EPSG:4326"
geometry = []
gdf = gpd.GeoDataFrame(geometry=geometry, crs=crs)

# 添加多个点
gdf.loc[0, 'geometry'] = Point(116, 39)
gdf.loc[1, 'geometry'] = Point(117, 40)

# 保存为 shapefile
gdf.to_file("points.shp")
