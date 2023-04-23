# from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView
# from PyQt5.QtGui import QColor, QPen, QBrush
# from osgeo import ogr
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("显示shp文件")
#         self.setGeometry(100, 100, 800, 600)
#         self.scene = QGraphicsScene(self)
#         self.view = QGraphicsView(self.scene, self)
#         self.setCentralWidget(self.view)
#         self.show()
#
#     def show_shapefile(self, shp_path):
#         driver = ogr.GetDriverByName("ESRI Shapefile")
#         datasource = driver.Open(shp_path, 0)
#         layer = datasource.GetLayer()
#         for feature in layer:
#             geometry = feature.GetGeometryRef()
#             if geometry.GetGeometryType() == ogr.wkbPoint:
#                 point = geometry.GetPoint()
#                 brush = QBrush(QColor(255, 0, 0))
#                 pen = QPen(QColor(0, 0, 0))
#                 self.scene.addEllipse(point[0], -point[1], 5, 5, pen, brush)
#             elif geometry.GetGeometryType() == ogr.wkbPolygon:
#                 polygon = geometry.ExportToWkt()
#                 # Do something with the polygon
#         self.view.fitInView(self.scene.itemsBoundingRect(), 0)
#
# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     window.show_shapefile(r"D:\SGDownload\landuse2020\行政区划.shp")
#     app.exec_()


import geopandas as gpd
import matplotlib.pyplot as plt

# 读取shp文件
gdf = gpd.read_file(r"buffered.shp")

# 绘制图层
gdf.plot()

# 显示图形
plt.show()
