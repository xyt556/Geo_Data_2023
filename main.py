from osgeo import gdal
from osgeo import ogr
# 打开影像文件
dataset = gdal.Open(r"F:\Data\Sentinel-2\L1C_T50SNC_A010883_20190407T025751.tif")

# 获取影像文件中波段的个数
band_count = dataset.RasterCount

# 输出波段个数
print("个数:", band_count)

# 关闭影像文件
dataset = None
