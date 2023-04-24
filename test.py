from osgeo import gdal
drv_count = gdal.GetDriverCount()
print(drv_count)
for idx in range(drv_count):
    driver = gdal.GetDriver(idx)
    print("%10s: %s" % (driver.ShortName, driver.LongName))