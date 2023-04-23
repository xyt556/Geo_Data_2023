from osgeo import ogr

# 输入文件路径
input_file = r"D:\SGDownload\landuse2020\行政区划.shp"

# 输出文件路径
output_file = r"buffered.shp"

# 缓冲区距离
buffer_distance = 1000  # 单位：米

# 缓冲区分辨率
buffer_resolution = 30  # 单位：度

# 要素编号
feature_id = 1

# 打开输入文件
input_ds = ogr.Open(input_file)

# 获取第一个图层
layer = input_ds.GetLayer()

# 选定要素
feature = layer.GetFeature(feature_id)

# 获取要素的几何对象
geometry = feature.GetGeometryRef()

# 创建缓冲区
buffered_geometry = geometry.Buffer(buffer_distance, buffer_resolution)

# 创建输出数据源
output_driver = ogr.GetDriverByName('ESRI Shapefile')
output_ds = output_driver.CreateDataSource(output_file)

# 创建输出图层
output_layer = output_ds.CreateLayer('buffered', geom_type=ogr.wkbPolygon)

# 创建输出要素
output_feature = ogr.Feature(output_layer.GetLayerDefn())

# 设置输出要素的几何对象
output_feature.SetGeometry(buffered_geometry)

# 写入输出要素
output_layer.CreateFeature(output_feature)

# 释放资源
input_ds = None
output_ds = None
