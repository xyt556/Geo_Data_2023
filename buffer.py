from osgeo import ogr
import os


def buffer_analysis(input_shp, output_shp, buffer_size):
    # 1. 打开输入数据源
    in_driver = ogr.GetDriverByName("ESRI Shapefile")
    in_datasource = in_driver.Open(input_shp, 0)
    in_layer = in_datasource.GetLayer()

    # 2. 创建输出数据源
    out_driver = ogr.GetDriverByName("ESRI Shapefile")
    if os.path.exists(output_shp):
        out_driver.DeleteDataSource(output_shp)
    out_datasource = out_driver.CreateDataSource(output_shp)
    out_layer = out_datasource.CreateLayer("buffered", in_layer.GetSpatialRef(), ogr.wkbPolygon)

    # 3. 定义缓冲区参数
    buffer_dist = float(buffer_size)

    # 4. 对每个要素进行缓冲区分析，并将结果添加到输出图层
    for in_feature in in_layer:
        # 获取要素几何体
        geom = in_feature.GetGeometryRef()
        # 进行缓冲区分析
        buffer_geom = geom.Buffer(buffer_dist)
        # 将缓冲区几何体添加到输出图层
        out_feature = ogr.Feature(out_layer.GetLayerDefn())
        out_feature.SetGeometry(buffer_geom)
        out_layer.CreateFeature(out_feature)
        out_feature = None

    # 5. 清理内存
    in_datasource = None
    out_datasource = None


input_shp = r"D:\SGDownload\landuse2020\行政区划.shp"
output_shp = r"buff_output.shp"
buffer_size = 10000  # 缓冲区大小（单位：米）

buffer_analysis(input_shp, output_shp, buffer_size)
