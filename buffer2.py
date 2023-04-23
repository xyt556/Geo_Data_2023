from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import matplotlib.pyplot as plt
import geopandas as gpd
import os
import sys

# 创建GUI界面
root = Tk()
root.title('缓冲区分析')
root.geometry('400x200')


# 创建“打开”按钮
def open_file():
    filepath = filedialog.askopenfilename(filetypes=[('Shapefile', '*.shp')])
    if filepath:
        txt_filepath.delete(0, END)
        txt_filepath.insert(END, filepath)


btn_open = Button(root, text='打开', command=open_file)
btn_open.pack(pady=10)

# 创建文本框和标签
Label(root, text='缓冲区半径：').pack()
txt_radius = Entry(root)
txt_radius.pack()

Label(root, text='文件路径：').pack()
txt_filepath = Entry(root)
txt_filepath.pack()


# 创建“保存”按钮
def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension='.shp', filetypes=[('Shapefile', '*.shp')])
    if filepath:
        txt_output.delete(0, END)
        txt_output.insert(END, filepath)


btn_save = Button(root, text='保存', command=save_file)
btn_save.pack(pady=10)


# 创建“分析”按钮
def buffer_analysis():
    # 获取文件路径和缓冲区半径
    filepath = txt_filepath.get()
    radius = float(txt_radius.get())

    if not os.path.isfile(filepath):
        messagebox.showerror('错误', '无效的文件路径')
        return

    try:
        # 打开文件
        gdf = gpd.read_file(filepath)

        # 进行缓冲区分析
        buffered = gdf.copy()
        buffered.geometry = gdf.geometry.buffer(radius)

        # 保存缓冲区分析结果
        output_filepath = txt_output.get()
        if not output_filepath:
            messagebox.showerror('错误', '无效的输出路径')
            return
        buffered.to_file(output_filepath)

        # 显示结果
        fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 4))
        gdf.plot(ax=ax1)
        buffered.plot(ax=ax2)
        ax1.set_title('原始数据')
        ax2.set_title('缓冲区分析结果')
        plt.show()

    except Exception as e:
        messagebox.showerror('错误', str(e))
        return


btn_analyze = Button(root, text='分析', command=buffer_analysis)
btn_analyze.pack(pady=10)

# 创建文本框和标签
Label(root, text='输出路径：').pack()
txt_output = Entry(root)
txt_output.pack()

root.mainloop()
