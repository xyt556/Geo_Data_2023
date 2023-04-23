from osgeo import ogr
# 打开shp文件
driver = ogr.GetDriverByName('ESRI Shapefile')
shp_file = driver.Open(r"D:\SGDownload\landuse2020\行政区划.shp", 0)

# 获取第一个图层
layer = shp_file.GetLayer()

# 获取前十条记录并输出
for i in range(5):
    feature = layer.GetNextFeature()
    if feature is None:
        break
    print(f'Record {i+1}:')
    for field in feature.keys():
        value = feature.GetField(field)
        print(f'    {field}: {value}')
