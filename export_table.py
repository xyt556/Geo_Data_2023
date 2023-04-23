import os
import pandas as pd
import geopandas as gpd
from tkinter import filedialog, messagebox, ttk
from tkinter import *

# 创建 GUI 界面
root = Tk()
root.title('导出属性表')
root.geometry('400x200')

# 设置程序图标
# root.iconbitmap(os.path.join(os.path.dirname(__file__), 'icon.ico'))


# 创建“打开”按钮
def open_file():
    filepath = filedialog.askopenfilename(filetypes=[('Shapefile', '*.shp')])
    if filepath:
        txt_filepath.delete(0, END)
        txt_filepath.insert(END, filepath)
        lbl_filename.config(text=filepath.split('/')[-1])  # 添加文件名标签


btn_open = Button(root, text='打开', command=open_file)
btn_open.pack(side=LEFT, padx=20, pady=10)


# 创建“导出”按钮
def export_table():
    # 获取文件路径
    filepath = txt_filepath.get()

    if not filepath:
        messagebox.showerror('错误', '无效的文件路径')
        return

    try:
        # 读取 shp 文件
        gdf = gpd.read_file(filepath, encoding='cp936')

        # 将属性表保存到 Excel 文件中
        output_filepath = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel', '*.xlsx')])
        if output_filepath:
            gdf.to_excel(output_filepath, index=False)
            messagebox.showinfo('提示', '属性表导出成功！')  # 添加导出成功的提示框

    except Exception as e:
        messagebox.showerror('错误', str(e))
        return


btn_export = Button(root, text='导出', command=export_table)
btn_export.pack(side=LEFT, padx=20, pady=10)

# 创建菜单栏
menubar = Menu(root)

# 创建“文件”菜单
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="退出", command=root.quit)
menubar.add_cascade(label="文件", menu=filemenu)

# 创建“帮助”菜单
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="关于")
menubar.add_cascade(label="帮助", menu=helpmenu)

root.config(menu=menubar)

# 创建文本框和标签
frm_filepath = Frame(root)
frm_filepath.pack()
Label(frm_filepath, text='文件路径：').grid(row=0, column=0, padx=5, pady=5, sticky=W)
txt_filepath = Entry(frm_filepath)
txt_filepath.grid(row=0, column=1, padx=5, pady=5, sticky=W + E)
lbl_filename = Label(frm_filepath, text='')
lbl_filename.grid(row=1, column=1, padx=5, pady=5, sticky=W)

root.mainloop()
