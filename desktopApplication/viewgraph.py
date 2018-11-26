# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties

# 参照ボタンのイベント
def reference_clicked():

    filepath = filedialog.askopenfilename()
    file1.set(filepath)

# グラフ描画ボタンのイベント
def drawing_clicked():

    df = pd.read_excel(file1.get(), index_col=0)
    x = df.index.values
    y_label = df.columns.values[0]
    y = df.iloc[:, 0].values
    fp = FontProperties(fname=r'C:/WINDOWS/Fonts/msgothic.ttc')
    fig = Figure(figsize=(8, 6), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.set_ylabel(y_label, fontproperties=fp)

    sub_win = tk.Toplevel()
    canvas = FigureCanvasTkAgg(fig, master=sub_win)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, expand=0)
    canvas._tkcanvas.pack(side=tk.BOTTOM, expand=0)

if __name__ == '__main__':

    # rootの作成
    root = tk.Tk()
    root.title('ViewGraph')
    root.resizable(False, False)

    # root に紐付いた Frame1 の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # frame1 に紐付いた参照ボタンの作成
    button1 = ttk.Button(frame1, text=u'参照', command=reference_clicked)
    button1.grid(row=0, column=3)

    # frame1 に紐付いた「ファイル」ラベルの作成
    s = tk.StringVar()
    s.set('ファイル>>')
    label1 = ttk.Label(frame1, textvariable=s)
    label1.grid(row=0, column=0)

    # frame1 に紐付いた参照ファイルパス表示ラベルの作成
    file1 = tk.StringVar()
    file1_entry = ttk.Entry(frame1, textvariable=file1, width=50)
    file1_entry.grid(row=0, column=2)

    # root に紐付いた Frame2 の作成
    frame2 = ttk.Frame(root, padding=(0,5))
    frame2.grid(row=1)

    # frame2 に紐付いたグラフ描画ボタンの作成
    button2 = ttk.Button(frame2, text='グラフ描画', command=drawing_clicked)
    button2.pack(side=tk.LEFT)

    # frame2 に紐付いたキャンセルボタンの作成
    button3 = ttk.Button(frame2, text='キャンセル', command=quit)
    button3.pack(side=tk.LEFT)

    root.mainloop()
