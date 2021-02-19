import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from tkinter import ttk
import textwrap
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import pandas as pd
import webbrowser
import matplotlib.pyplot as py
from matplotlib.font_manager import FontProperties
import urllib.request
import json
import sys
import re


def wrap(string, length):  # 自動換列
    return '\n'.join(textwrap.wrap(string, length))


class YoutubePlaylistResult(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.design()
        self.master.title("Special YouTube Result")
        self.master.geometry("1080x1080")
        self.master.configure(background='white')
        self.create_playlist_result('播放清單ID：' + pl_id,
                                    '清單影片數量：' + vid_num,
                                    '影片總時長：' + vid_time)

        self.X_axis()
        self.Y_axis()
        self.click_web()
        self.bar_icon()
        self.home_widget()

    def home_widget(self):
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")
        self.home = tk.Button(self, command=self.return_home,
                              font=f3, text="回首頁", bg='white', fg='black')
        self.home.grid(row=0, column=0, sticky=tk.E, padx=(0, 30))

    def return_home(self):
        self.destroy()
        enter_search = SearchType()
        enter_search.mainloop()

    def design(self):
        self.img = Image.open(
            "D:\\商管程\\final project\\PBC-final-project\\bg8.png")
        self.image2 = ImageTk.PhotoImage(self.img)
        self.design1 = tk.Canvas(self, width=1080, height=1080, bg="black")
        self.design1.create_image(540, 300, image=self.image2, anchor="center")
        self.design1.grid(
            row=0,
            column=0,
            columnspan=5,
            rowspan=50,
            sticky="nw")

    def create_playlist_result(self, words, vid_num, vid_time):  # playlist 資訊欄
        f1 = tkFont.Font(size=20, family="王漢宗細黑體繁")
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")

        self.result = tk.Label(
            self,
            text=words,
            font=f3,
            height=1,
            width=60,
            anchor='nw',
            bg='#f8f8ee')
        self.vid_num_1 = tk.Label(
            self,
            text=vid_num,
            font=f3,
            height=1,
            width=60,
            anchor='nw',
            bg='#f8f8ee')
        self.vid_time_1 = tk.Label(
            self,
            text=vid_time,
            font=f3,
            height=1,
            width=60,
            anchor='nw',
            bg='#f8f8ee')

        self.table = ttk.Treeview(self, height=10, show="headings")
        self.table["columns"] = ("影片名稱", "觀看次數", "讚踩比", "留言數量", "影片連結")

        self.table.column("影片名稱", width=300, anchor='center')
        self.table.column("影片連結", width=300, anchor='center')
        self.table.column("觀看次數", width=80, anchor='center')
        self.table.column("讚踩比", width=80, anchor='center')
        self.table.column("留言數量", width=80, anchor='center')

        self.table.heading("影片名稱", text="影片名稱")
        self.table.heading("影片連結", text="影片連結")
        self.table.heading("觀看次數", text="觀看次數")
        self.table.heading("讚踩比", text="讚踩比")
        self.table.heading("留言數量", text="留言數量")

        for i in range(len(videos_list)):
            video_name = videos_list[i][0]
            list_value = list(map(str, videos_list[i]))
            new_video_value = tuple(list_value)
            self.table.insert(
                "",
                i,
                text=str(video_name),
                values=new_video_value)

        self.result.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky=tk.W +
            tk.N,
            padx=(
                20,
                0))
        self.vid_num_1.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=tk.W +
            tk.N,
            padx=(
                20,
                0))
        self.vid_time_1.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky=tk.W +
            tk.N,
            padx=(
                20,
                0))

        self.table.grid(row=4, column=0, padx=(20, 20))

    def sel_1(self):
        global sel_x
        sel_x = radio_value3.get()

    def sel_2(self):
        global sel_y
        sel_y = radio_value4.get()

    def X_axis(self):
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")

        self.x_ = tk.Label(self, text='X軸類別', font=f3, bg='#f8f8ee',
                           height=1, width=15, anchor='nw')

        global radio_value3
        radio_value3 = tk.IntVar()
        radio_value3.set(0)

        self.name = tk.Radiobutton(
            self,
            text="影片名稱",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value3,
            command=self.sel_1,
            value=1)
        self.view = tk.Radiobutton(
            self,
            text="觀看次數",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value3,
            command=self.sel_1,
            value=2)
        self.like_ratio = tk.Radiobutton(
            self,
            text="讚踩比",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value3,
            command=self.sel_1,
            value=3)
        self.comment = tk.Radiobutton(
            self,
            text="留言數量",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value3,
            command=self.sel_1,
            value=4)

        i = 3
        self.x_.grid(
            row=i + 2,
            column=0,
            sticky=tk.W,
            padx=(
                20,
                20),
            pady=(
                20,
                10))
        self.name.grid(row=i + 3, column=0, sticky=tk.W, padx=(20, 20))
        self.view.grid(row=i + 3, column=0, sticky=tk.W, padx=(150, 20))
        self.like_ratio.grid(row=i + 3, column=0, sticky=tk.W, padx=(300, 20))
        self.comment.grid(row=i + 3, column=0, sticky=tk.W, padx=(450, 20))

    def Y_axis(self):
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")

        self.y_ = tk.Label(self, text='Y軸類別', font=f3, bg='#f8f8ee',
                           height=1, width=15, anchor='nw')
        global radio_value4
        radio_value4 = tk.IntVar()
        radio_value4.set(0)

        self.name = tk.Radiobutton(
            self,
            text="影片名稱",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value4,
            command=self.sel_2,
            value=1)
        self.view = tk.Radiobutton(
            self,
            text="觀看次數",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value4,
            command=self.sel_2,
            value=2)
        self.like_ratio = tk.Radiobutton(
            self,
            text="讚踩比",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value4,
            command=self.sel_2,
            value=3)
        self.comment = tk.Radiobutton(
            self,
            text="留言數量",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value4,
            command=self.sel_2,
            value=4)

        i = 6
        self.y_.grid(
            row=i + 2,
            column=0,
            sticky=tk.W,
            padx=(
                20,
                20),
            pady=(
                20,
                10))
        self.name.grid(row=i + 3, column=0, sticky=tk.W, padx=(20, 20))
        self.view.grid(row=i + 3, column=0, sticky=tk.W, padx=(150, 20))
        self.like_ratio.grid(row=i + 3, column=0, sticky=tk.W, padx=(300, 20))
        self.comment.grid(row=i + 3, column=0, sticky=tk.W, padx=(450, 20))

    def select_item(self, event):  # 點選表格內文字
        cur_item = self.table.item(self.table.focus())
        col = self.table.identify_column(event.x)
        if col in '#1#2#3#4#5#6':
            cell_value = cur_item['values'][4]  # 影片網址
            url = cell_value
            webbrowser.open(cell_value, new=2)

    def click_web(self):
        self.table.bind('<ButtonRelease-1>', self.select_item)

    def bar_icon(self):
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")
        self.bar = tk.Button(
            self,
            command=self.click_bar,
            font=f3,
            text="產生圖表",
            bg='#FFFACD',
            fg="black")  # 按下home鍵 回到首頁
        i = 10
        self.bar.grid(
            row=i, column=0, sticky=tk.W, padx=(
                300, 50), pady=(
                20, 0))

    def click_bar(self):
        new_list1 = []
        new_list2 = []
        if sel_x == 1:
            for i in videos_list:
                new_list1.append(i[0])
            py.ylabel("影片名稱")
        elif sel_x == 2:
            for i in videos_list:
                new_list1.append(i[1])
            py.ylabel("觀看次數")
        elif sel_x == 3:
            for i in videos_list:
                new_list1.append(i[2])
            py.ylabel("讚踩比")
        elif sel_x == 4:
            for i in videos_list:
                new_list1.append(i[3])
            py.ylabel("留言數量")

        if sel_y == 1:
            for i in videos_list:
                new_list2.append(i[0])
            py.xlabel("影片名稱")
        elif sel_y == 2:
            for i in videos_list:
                new_list2.append(i[1])
            py.xlabel("觀看次數")
        elif sel_y == 3:
            for i in videos_list:
                new_list2.append(i[2])
            py.xlabel("讚踩比")
        elif sel_y == 4:
            for i in videos_list:
                new_list2.append(i[3])
            py.xlabel("留言數量")

        if sel_x != sel_y:
            py.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
            py.barh(new_list1, new_list2, color="#ffcccc", alpha=0.7)
            py.show()
        else:
            self.wrong_message = tk.messagebox.showwarning(
                title="小提醒", message="請選擇不同的X、Y軸類別")


class YoutubeChannelResult(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.design()
        self.master.title("Special YouTube Result")
        self.master.geometry("1080x1080")
        self.master.configure(background='white')
        self.create_channel_result('頻道ID：' + wanted_channel_id)
        self.video_result('點讚數前十名影片資訊')
        self.X_axis()
        self.Y_axis()
        self.click_web()
        self.bar_icon()
        self.home_widget()

    def home_widget(self):
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")
        self.home = tk.Button(self, command=self.return_home,
                              font=f3, text="回首頁", bg='white', fg='black')
        self.home.grid(row=0, column=0, sticky=tk.E, padx=(0, 30))

    def design(self):
        self.img = Image.open(
            "D:\\商管程\\final project\\PBC-final-project\\bg8.png")
        self.image2 = ImageTk.PhotoImage(self.img)
        self.design1 = tk.Canvas(self, width=1080, height=1080, bg="black")
        self.design1.create_image(540, 300, image=self.image2, anchor="center")
        self.design1.grid(
            row=0,
            column=0,
            columnspan=5,
            rowspan=50,
            sticky="nw")

    def return_home(self):
        self.destroy()
        enter_search = SearchType()
        enter_search.mainloop()

    def create_channel_result(self, words):
        f1 = tkFont.Font(size=20, family="王漢宗細黑體繁")
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")

        self.result = tk.Label(
            self,
            text=words,
            font=f3,
            height=1,
            width=35,
            bg='#f8f8ee')

        ttk.Style().configure('MyStyle1.Treeview', rowheight=90)
        self.table = ttk.Treeview(self, height=1, show="headings",
                                  selectmode='none', style='MyStyle1.Treeview')

        self.table["columns"] = ("頻道名稱", "總觀看人數", "頻道訂閱人數", "簡介")

        self.table.column("頻道名稱", width=150, anchor='center')
        self.table.column("總觀看人數", width=100, anchor='center')
        self.table.column("頻道訂閱人數", width=100, anchor='center')
        self.table.column("簡介", width=670, anchor='center')

        self.table.heading("頻道名稱", text="頻道名稱")  # 显示表头
        self.table.heading("總觀看人數", text="總觀看人數")
        self.table.heading("頻道訂閱人數", text="頻道訂閱人數")
        self.table.heading("總觀看人數", text="總觀看人數")
        self.table.heading("簡介", text="簡介")

        name_wrap = wrap(channel_name, 115)
        description_wrap = wrap(channel_descrip, 115)

        self.table.insert(
            "",
            "0",
            values=(
                name_wrap,
                channel_views,
                channel_sub,
                description_wrap))

        self.result.grid(row=0, column=0, sticky=tk.W)
        self.table.grid(row=1, column=0, rowspan=5, sticky=tk.W, padx=(20, 0))

    def video_result(self, words):
        f1 = tkFont.Font(size=20, family="王漢宗細黑體繁")
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")

        self.result = tk.Label(
            self,
            text=words,
            font=f3,
            height=1,
            width=60,
            anchor='nw',
            bg='#f8f8ee')

        self.table = ttk.Treeview(
            self,
            height=10,
            show="headings",
            selectmode='browse')

        self.table["columns"] = ("影片名稱", "觀看次數", "讚踩比", "留言數量", "影片連結")

        self.table.column("影片名稱", width=450, anchor='center')
        self.table.column("影片連結", width=300, anchor='center')
        self.table.column("觀看次數", width=90, anchor='center')
        self.table.column("讚踩比", width=90, anchor='center')
        self.table.column("留言數量", width=90, anchor='center')

        self.table.heading("影片名稱", text="影片名稱")
        self.table.heading("影片連結", text="影片連結")
        self.table.heading("觀看次數", text="觀看次數")
        self.table.heading("讚踩比", text="讚踩比")
        self.table.heading("留言數量", text="留言數量")

        for i in range(len(videos_list)):
            video_name = videos_list[i][0]
            list_value = list(map(str, videos_list[i]))
            new_video_value = tuple(list_value)
            self.table.insert(
                "",
                i,
                text=str(
                    video_name[i][0]),
                values=new_video_value)

        self.result.grid(
            row=2,
            column=0,
            columnspan=3,
            sticky=tk.W +
            tk.N,
            padx=(
                20,
                0),
            pady=(
                10,
                0))
        self.table.grid(row=3, column=0, padx=(20, 20))

    def sel_1(self):
        global sel_x
        sel_x = radio_value1.get()

    def sel_2(self):
        global sel_y
        sel_y = radio_value2.get()

    def X_axis(self):
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")

        self.x_ = tk.Label(self, text='X軸類別', font=f3, bg='#f8f8ee',
                           height=1, width=15, anchor='nw')

        global radio_value1
        radio_value1 = tk.IntVar()
        radio_value1.set(0)

        self.name = tk.Radiobutton(
            self,
            text="影片名稱",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value1,
            command=self.sel_1,
            value=1)
        self.view = tk.Radiobutton(
            self,
            text="觀看次數",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value1,
            command=self.sel_1,
            value=2)
        self.like_ratio = tk.Radiobutton(
            self,
            text="讚踩比",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value1,
            command=self.sel_1,
            value=3)
        self.comment = tk.Radiobutton(
            self,
            text="留言數量",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value1,
            command=self.sel_1,
            value=4)

        i = 2
        self.x_.grid(
            row=i + 2,
            column=0,
            sticky=tk.W,
            padx=(
                20,
                20),
            pady=(
                20,
                10))
        self.name.grid(row=i + 3, column=0, sticky=tk.W, padx=(20, 20))
        self.view.grid(row=i + 3, column=0, sticky=tk.W, padx=(150, 20))
        self.like_ratio.grid(row=i + 3, column=0, sticky=tk.W, padx=(300, 20))
        self.comment.grid(row=i + 3, column=0, sticky=tk.W, padx=(450, 20))

    def Y_axis(self):
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")

        self.y_ = tk.Label(self, text='Y軸類別', font=f3, bg='#f8f8ee',
                           height=1, width=15, anchor='nw')

        global radio_value2
        radio_value2 = tk.IntVar()
        radio_value2.set(0)

        self.name = tk.Radiobutton(
            self,
            text="影片名稱",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value2,
            command=self.sel_2,
            value=1)
        self.view = tk.Radiobutton(
            self,
            text="觀看次數",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value2,
            command=self.sel_2,
            value=2)
        self.like_ratio = tk.Radiobutton(
            self,
            text="讚踩比",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value2,
            command=self.sel_2,
            value=3)
        self.comment = tk.Radiobutton(
            self,
            text="留言數量",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value2,
            command=self.sel_2,
            value=4)

        i = 4
        self.y_.grid(
            row=i + 2,
            column=0,
            sticky=tk.W,
            padx=(
                20,
                20),
            pady=(
                20,
                10))
        self.name.grid(row=i + 3, column=0, sticky=tk.W, padx=(20, 20))
        self.view.grid(row=i + 3, column=0, sticky=tk.W, padx=(150, 20))
        self.like_ratio.grid(row=i + 3, column=0, sticky=tk.W, padx=(300, 20))
        self.comment.grid(row=i + 3, column=0, sticky=tk.W, padx=(450, 20))

    def select_item(self, event):  # 點選表格內文字
        cur_item = self.table.item(self.table.focus())
        col = self.table.identify_column(event.x)
        if col in '#1#2#3#4#5':
            cell_value = cur_item['values'][4]  # 影片網址
            url = cell_value
            webbrowser.open(cell_value, new=2)
        # print ('cell_value = ', cell_value)  # 印出網址

    def click_web(self):
        self.table.bind('<ButtonRelease-1>', self.select_item)

    def bar_icon(self):
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")
        self.bar = tk.Button(
            self,
            command=self.click_bar,
            font=f3,
            text="產生圖表",
            bg='#FFFACD',
            fg="black")  # 按下home鍵 回到首頁
        i = 8
        self.bar.grid(
            row=i, column=0, sticky=tk.W, padx=(
                300, 50), pady=(
                0, 40))

    def click_bar(self):
        new_list1 = []
        new_list2 = []
        if sel_x == 1:
            for i in videos_list:
                new_list1.append(i[0])
            py.ylabel("影片名稱")
        elif sel_x == 2:
            for i in videos_list:
                new_list1.append(i[1])
            py.ylabel("觀看次數")
        elif sel_x == 3:
            for i in videos_list:
                new_list1.append(i[2])
            py.ylabel("讚踩比")
        elif sel_x == 4:
            for i in videos_list:
                new_list1.append(i[3])
            py.ylabel("留言數量")

        if sel_y == 1:
            for i in videos_list:
                new_list2.append(i[0])
            py.xlabel("影片名稱")
        elif sel_y == 2:
            for i in videos_list:
                new_list2.append(i[1])
            py.xlabel("觀看次數")
        elif sel_y == 3:
            for i in videos_list:
                new_list2.append(i[2])
            py.xlabel("讚踩比")
        elif sel_y == 4:
            for i in videos_list:
                new_list2.append(i[3])
            py.xlabel("留言數量")

        if sel_x != sel_y:
            py.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
            py.barh(new_list1, new_list2, color="#ffcccc", alpha=0.7)
            py.show()
        else:
            self.wrong_message = tk.messagebox.showwarning(
                title="小提醒", message="請選擇不同的X、Y軸類別")


class YoutubeVideoResult(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.design()
        self.master.title("Special YouTube Result")
        self.master.geometry("1080x1080")
        self.master.configure(background='#f8f8ee')
        self.create_video_result('搜索詞：' + answer)  # 應該補放入變數(搜索詞的總和)！！
        self.X_axis()
        self.Y_axis()
        self.click_web()
        self.bar_icon()
        self.home_widget()

    def home_widget(self):
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")
        self.home = tk.Button(self, command=self.return_home,
                              font=f3, text="回首頁", bg='white', fg='black')
        self.home.grid(row=0, column=0, sticky=tk.E, padx=(0, 30))

    def design(self):
        self.img = Image.open(
            "D:\\商管程\\final project\\PBC-final-project\\bg8.png")
        self.image2 = ImageTk.PhotoImage(self.img)
        self.design1 = tk.Canvas(self, width=1080, height=1080, bg="black")
        self.design1.create_image(540, 300, image=self.image2, anchor="center")
        self.design1.grid(
            row=0,
            column=0,
            columnspan=5,
            rowspan=30,
            sticky="nw")

    def return_home(self):
        self.destroy()
        enter_search = SearchType()
        enter_search.mainloop()

    def create_video_result(self, words):
        f1 = tkFont.Font(size=20, family="王漢宗細黑體繁")
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")

        self.result = tk.Label(
            self,
            text=words,
            font=f3,
            height=2,
            width=40,
            anchor='nw',
            bg='#f8f8ee')

        self.table = ttk.Treeview(self, height=10, show="headings")
        self.table["columns"] = ("影片名稱", "觀看次數", "讚踩比", "留言數量", "影片連結")

        self.table.column("影片名稱", width=200, anchor='center')
        self.table.column("影片連結", width=300, anchor='center')
        self.table.column("觀看次數", width=80, anchor='center')
        self.table.column("讚踩比", width=80, anchor='center')
        self.table.column("留言數量", width=80, anchor='center')

        self.table.heading("影片名稱", text="影片名稱")
        self.table.heading("影片連結", text="影片連結")
        self.table.heading("觀看次數", text="觀看次數")
        self.table.heading("讚踩比", text="讚踩比")
        self.table.heading("留言數量", text="留言數量")

        for i in range(len(videos_list)):
            video_name = videos_list[i][0]
            list_value = list(map(str, videos_list[i]))
            new_video_value = tuple(list_value)
            self.table.insert(
                "",
                i,
                text=str(video_name),
                values=new_video_value)

        self.result.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky=tk.W +
            tk.N,
            padx=(
                20,
                0))
        self.table.grid(row=2, column=0, padx=(20, 20))

    def sel_1(self):
        global sel_x
        sel_x = radio_value1.get()

    def sel_2(self):
        global sel_y
        sel_y = radio_value2.get()

    def X_axis(self):
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")

        self.x_ = tk.Label(self, text='X軸類別', font=f3, bg='#f8f8ee',
                           height=1, width=15, anchor='nw')

        global radio_value1
        radio_value1 = tk.IntVar()
        radio_value1.set(0)

        self.name = tk.Radiobutton(
            self,
            text="影片名稱",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value1,
            command=self.sel_1,
            value=1)
        self.view = tk.Radiobutton(
            self,
            text="觀看次數",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value1,
            command=self.sel_1,
            value=2)
        self.like_ratio = tk.Radiobutton(
            self,
            text="讚踩比",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value1,
            command=self.sel_1,
            value=3)
        self.comment = tk.Radiobutton(
            self,
            text="留言數量",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value1,
            command=self.sel_1,
            value=4)

        i = 1
        self.x_.grid(
            row=i + 2,
            column=0,
            sticky=tk.W,
            padx=(
                20,
                20),
            pady=(
                20,
                10))
        self.name.grid(row=i + 3, column=0, sticky=tk.W, padx=(20, 20))
        self.view.grid(row=i + 3, column=0, sticky=tk.W, padx=(150, 20))
        self.like_ratio.grid(row=i + 3, column=0, sticky=tk.W, padx=(300, 20))
        self.comment.grid(row=i + 3, column=0, sticky=tk.W, padx=(450, 20))

    def Y_axis(self):
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")

        self.y_ = tk.Label(self, text='Y軸類別', font=f3, bg='#f8f8ee',
                           height=1, width=15, anchor='nw')

        global radio_value2
        radio_value2 = tk.IntVar()
        radio_value2.set(0)

        self.name = tk.Radiobutton(
            self,
            text="影片名稱",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value2,
            command=self.sel_2,
            value=1)
        self.view = tk.Radiobutton(
            self,
            text="觀看次數",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value2,
            command=self.sel_2,
            value=2)
        self.like_ratio = tk.Radiobutton(
            self,
            text="讚踩比",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value2,
            command=self.sel_2,
            value=3)
        self.comment = tk.Radiobutton(
            self,
            text="留言數量",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value2,
            command=self.sel_2,
            value=4)

        i = 3
        self.y_.grid(
            row=i + 2,
            column=0,
            sticky=tk.W,
            padx=(
                20,
                20),
            pady=(
                20,
                10))
        self.name.grid(row=i + 3, column=0, sticky=tk.W, padx=(20, 20))
        self.view.grid(row=i + 3, column=0, sticky=tk.W, padx=(150, 20))
        self.like_ratio.grid(row=i + 3, column=0, sticky=tk.W, padx=(300, 20))
        self.comment.grid(row=i + 3, column=0, sticky=tk.W, padx=(450, 20))

    def select_item(self, event):  # 點選表格內文字
        cur_item = self.table.item(self.table.focus())
        col = self.table.identify_column(event.x)
        if col in '#1#2#3#4#5':
            cell_value = cur_item['values'][4]  # 影片網址
            url = cell_value
            webbrowser.open(cell_value, new=2)
        # print ('cell_value = ', cell_value)  # 印出網址

    def click_web(self):
        self.table.bind('<ButtonRelease-1>', self.select_item)

    def bar_icon(self):
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")
        self.bar = tk.Button(
            self,
            command=self.click_bar,
            font=f3,
            text="產生圖表",
            bg='#FFFACD',
            fg="black")  # 按下home鍵 回到首頁
        i = 7
        self.bar.grid(
            row=i, column=0, sticky=tk.W, padx=(
                300, 50), pady=(
                20, 0))

    def click_bar(self):
        new_list1 = []
        new_list2 = []
        if sel_x == 1:
            for i in videos_list:
                new_list1.append(i[0])
            py.ylabel("影片名稱")
        elif sel_x == 2:
            for i in videos_list:
                new_list1.append(i[1])
            py.ylabel("觀看次數")
        elif sel_x == 3:
            for i in videos_list:
                new_list1.append(i[2])
            py.ylabel("讚踩比")
        elif sel_x == 4:
            for i in videos_list:
                new_list1.append(i[3])
            py.ylabel("留言數量")

        if sel_y == 1:
            for i in videos_list:
                new_list2.append(i[0])
            py.xlabel("影片名稱")
        elif sel_y == 2:
            for i in videos_list:
                new_list2.append(i[1])
            py.xlabel("觀看次數")
        elif sel_y == 3:
            for i in videos_list:
                new_list2.append(i[2])
            py.xlabel("讚踩比")
        elif sel_y == 4:
            for i in videos_list:
                new_list2.append(i[3])
            py.xlabel("留言數量")

        if sel_x != sel_y:
            py.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

            py.barh(new_list1, new_list2, color="#ffcccc", alpha=0.7)
            py.show()
        else:
            self.wrong_message = tk.messagebox.showwarning(
                title="小提醒", message="請選擇不同的X、Y軸類別")


class YoutubeVideoSearch(tk.Frame):  # 影片搜尋頁
    def __init__(self):  # 基礎畫面設定
        tk.Frame.__init__(self)
        self.grid()
        self.design()
        self.create_widgets()
        self.master.title("Special YouTube Recommendation")
        self.master.geometry("800x600")
        self.yt_icon()

    def design(self):
        self.img = Image.open(
            "D:\\商管程\\final project\\PBC-final-project\\bg6.png")
        self.image2 = ImageTk.PhotoImage(self.img)
        self.design1 = tk.Canvas(self, width=800, height=600, bg="black")
        self.design1.create_image(400, 300, image=self.image2, anchor="center")
        self.design1.grid(
            row=0,
            column=0,
            columnspan=6,
            rowspan=40,
            sticky="nw")

    def yt_icon(self):  # 首頁鍵
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁", weight="bold")
        self.home = tk.Button(
            self,
            command=self.return_home,
            font=f3,
            text="回首頁",
            bg='white',
            fg='black')  # 按下home鍵 回到首頁
        self.home.grid(row=0, column=1, sticky=tk.W, pady=(60, 0))

    def return_home(self):  # 回到首頁
        self.destroy()  # 清空畫面
        enter_search = SearchType()
        enter_search.mainloop()

    def sel(self):
        global selection
        global words_1
        global words_2

        selection = radio_value2.get()
        words_1 = self.search_content.get()
        words_2 = self.not_search_content.get()

    def create_widgets(self):
        f1 = tkFont.Font(size=20, family="王漢宗細黑體繁")
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")

        self.scrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)

        self.search = tk.Label(
            self,
            text="影片搜尋",
            font=f1,
            height=1,
            width=10,
            bg="#ffcccc")  # 搜索詞
        self.search_content = tk.Entry(self, bd=3, font=f2, width=40,
                                       xscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.search_content.xview)

        self.selection = tk.Label(self, text="篩選器",
                                  font=f1, height=1, width=10, bg="#FFA07A")
        self.not_search = tk.Label(
            self,
            text="不要出現",
            font=f1,
            height=1,
            width=10,
            bg="#ffcccc")  # 不想看到的關鍵字
        self.not_search_content = tk.Entry(self, bd=3, font=f2, width=30)

        self.order = tk.Label(
            self,
            text="排序依據",
            font=f1,
            height=1,
            width=10,
            bg="#ffcccc")

        global radio_value2
        radio_value2 = tk.IntVar()
        radio_value2.set(0)

        self.relevance = tk.Radiobutton(
            self,
            text="關聯性",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value2,
            command=self.sel,
            value=1)
        self.date = tk.Radiobutton(
            self,
            text="上傳日期",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value2,
            command=self.sel,
            value=2)
        self.rating = tk.Radiobutton(
            self,
            text="喜愛程度",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value2,
            command=self.sel,
            value=3)
        self.view = tk.Radiobutton(
            self,
            text="觀看次數",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value2,
            command=self.sel,
            value=4)
        self.title = tk.Radiobutton(
            self,
            text="依筆畫/字母排序",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value2,
            command=self.sel,
            value=5)

        self.go = tk.Button(
            self,
            command=self.click_go,
            font=f3,
            text="GO",
            bg='#FFFACD',
            fg='black')  # bg背景色；fg字體色

        # 設定每個功能的位置
        i = 15
        self.search.grid(row=i + 0, column=0)
        self.search_content.grid(row=i + 0, column=1, columnspan=2, ipady=8)
        self.scrollbar.grid(row=i + 1, column=1, sticky='we')
        self.selection.grid(row=i + 2, column=0)
        self.not_search.grid(row=i + 3, column=0)
        self.not_search_content.grid(
            row=i + 3,
            column=1,
            ipady=6,
            columnspan=2,
            sticky=tk.W)

        k = 10
        self.order.grid(row=k + 8, column=0)
        self.relevance.grid(row=k + 9, column=1, sticky=tk.W)
        self.date.grid(row=k + 9, column=2, sticky=tk.W)
        self.view.grid(row=k + 10, column=2, sticky=tk.W)
        self.rating.grid(row=k + 10, column=1, sticky=tk.W)
        self.title.grid(row=k + 11, column=1, sticky=tk.W)

        self.go.grid(
            row=k + 20,
            column=0,
            columnspan=4,
            padx=(
                80,
                0),
            pady=(
                40,
                0))

    def video_search(
            self,
            query,
            order,
            max_results=50,
            token=None,
            location=None,
            location_radius=None):

        # search upto max 50 videos based on query
        search_response = youtube_api.search().list(
            q=query,
            type="video",
            pageToken=token,
            order=order,
            part="id, snippet",
            maxResults=max_results,
            location=location,
            locationRadius=location_radius).execute()
        items = search_response['items']

        if len(items) == 0:
            print('Find Nothing')
        else:
            # assign values
            title = items[0]['snippet']['title']
            channelId = items[0]['snippet']['channelId']
            datePublished = items[0]['snippet']['publishedAt']

        return search_response

    def store_results(self, response):

        # create variables to store your values
        title = []
        channelId = []
        channelTitle = []
        categoryId = []
        videoId = []
        viewCount = []
        likeCount = []
        dislikeCount = []
        like_dislike_ratio = []
        commentCount = []
        category = []
        tags = []
        videos = []
        datePublished = []
        url = []

        for search_result in response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":

                # append title, video and published date for each item
                title.append(search_result['snippet']['title'])
                videoId.append(search_result['id']['videoId'])
                url.append(
                    'https://www.youtube.com/watch?v=' +
                    search_result['id']['videoId'])
                datePublished.append(search_result['snippet']['publishedAt'])

                # then collect stats on each video using videoId
                stats = youtube_api.videos().list(
                    part='statistics, snippet',
                    id=search_result['id']['videoId']).execute()

                channelId.append(stats['items'][0]['snippet']['channelId'])
                channelTitle.append(
                    stats['items'][0]['snippet']['channelTitle'])
                categoryId.append(stats['items'][0]['snippet']['categoryId'])
                viewCount.append(
                    int(stats['items'][0]['statistics']['viewCount']))

                # not every video has likes/dislikes enabled so they won't
                # appear in JSON response
                try:
                    likeCount.append(
                        int(stats['items'][0]['statistics']['likeCount']))
                except BaseException:
                    # good to be aware of Channels that turn off their Likes
                    # appends "Not Available" to keep dictionary values aligned
                    likeCount.append("Not available")

                try:
                    dislikeCount.append(
                        int(stats['items'][0]['statistics']['dislikeCount']))
                except BaseException:
                    # good to be aware of Channels that turn off their Likes
                    dislikeCount.append("Not available")

                try:
                    like = int(stats['items'][0]['statistics']['likeCount'])
                    dislike = int(
                        stats['items'][0]['statistics']['dislikeCount'])
                    # if dislike is zero, append its value
                    if dislike == 0:
                        dislike = 0.5
                    like_dislike_ratio.append(
                        '{:.0f}'.format(like / dislike))  # 四捨五入取到整數
                except BaseException:
                    like_dislike_ratio.append("Not available")

                # sometimes comments are disabled so if they exist append, if not append nothing...
                # it's not uncommon to disable comments, so no need to wrap in
                # try and except
                if 'commentCount' in stats['items'][0]['statistics'].keys():
                    commentCount.append(
                        int(stats['items'][0]['statistics']['commentCount']))
                else:
                    commentCount.append(0)

                if 'tags' in stats['items'][0]['snippet'].keys():
                    tags.append(stats['items'][0]['snippet']['tags'])
                else:
                    # I'm not a fan of empty fields
                    tags.append("No Tags")

        # break out of for-loop and if statement and store lists of values in
        # list
        youtube_list = [
            tags,
            channelId,
            channelTitle,
            categoryId,
            title,
            videoId,
            viewCount,
            likeCount,
            dislikeCount,
            like_dislike_ratio,
            commentCount,
            datePublished,
            url]

        return youtube_list

    # 只挑選前10個
    def ten_videos(self, result):
        portfolio = []
        # print(result)

        for i in range(50):
            if result[9][i] != 'Not available':
                portfolio += [[result[4][i], result[6][i],
                               result[9][i], result[10][i], result[12][i]]]
        return portfolio[0:10]
        # just list the top 10

    def click_go(self):
        # 讀取搜索欄資訊entry
        api_key = 'AIzaSyABgOEaH7Y49Ns-qPk5d8BBRwUeuZMs-Rw'
        global youtube_api
        youtube_api = build('youtube', 'v3', developerKey=api_key)

        # searching keywords
        search_items = words_1
        # excluding keywords
        if words_2 != "":
            exclude_items = ' -' + words_2
            # query
            query = search_items + exclude_items
        else:
            query = search_items
        # specifies the method that will be used to order resources
        # order：'date', 'rating', 'relevance', 'viewCount', 'title',
        # 'videoCount'

        global answer
        answer = words_1
        global videos_list

        if selection == 1:
            self.destroy()
            videos_list = self.ten_videos(
                self.store_results(
                    self.video_search(
                        query, 'relevance')))

            yt_result1 = YoutubeVideoResult()
            yt_result1.mainloop()

        elif selection == 2:
            self.destroy()
            videos_list = self.ten_videos(
                self.store_results(
                    self.video_search(
                        query, 'date')))

            yt_result1 = YoutubeVideoResult()
            yt_result1.mainloop()

        elif selection == 3:
            self.destroy()
            videos_list = self.ten_videos(
                self.store_results(
                    self.video_search(
                        query, 'rating')))

            yt_result1 = YoutubeVideoResult()
            yt_result1.mainloop()

        elif selection == 4:
            self.destroy()
            videos_list = self.ten_videos(
                self.store_results(
                    self.video_search(
                        query, 'viewCount')))

            yt_result1 = YoutubeVideoResult()
            yt_result1.mainloop()

        elif selection == 5:
            self.destroy()
            videos_list = self.ten_videos(
                self.store_results(
                    self.video_search(
                        query, 'title')))

            yt_result1 = YoutubeVideoResult()
            yt_result1.mainloop()


class YoutubeChannelSearch(tk.Frame):  # 頻道搜尋頁
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.design()
        self.create_widgets()
        self.master.title("Special YouTube Recommendation")
        self.master.geometry("800x600")
        self.yt_icon()

    def yt_icon(self):
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁", weight="bold")

        self.home = tk.Button(self, command=self.return_home,
                              font=f3, text="回首頁", bg='white', fg='black')
        self.home.grid(
            row=0, column=1, sticky=tk.W, pady=(
                60, 0), padx=(
                0, 20))

    def design(self):
        self.img = Image.open(
            "D:\\商管程\\final project\\PBC-final-project\\bg6.png")
        self.image2 = ImageTk.PhotoImage(self.img)
        self.design1 = tk.Canvas(self, width=800, height=600, bg="black")
        self.design1.create_image(400, 300, image=self.image2, anchor="center")
        self.design1.grid(
            row=0,
            column=0,
            columnspan=5,
            rowspan=16,
            sticky="nw")

    def return_home(self):
        self.destroy()
        enter_search = SearchType()
        enter_search.mainloop()

    def sel(self):
        global link
        link = self.v.get()

    def create_widgets(self):
        f1 = tkFont.Font(size=20, family="王漢宗細黑體繁")
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")

        self.ch_ID = tk.Label(
            self,
            text="輸入頻道網址",
            font=f1,
            height=1,
            width=15,
            bg="#ffcccc")

        self.v = tk.StringVar()
        self.scrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.ch_ID_content = tk.Entry(
            self,
            bd=3,
            font=f2,
            xscrollcommand=self.scrollbar.set,
            width=40,
            textvariable=self.v)
        self.scrollbar.config(command=self.ch_ID_content.xview)

        self.go = tk.Button(
            self,
            command=self.click_go,
            font=f3,
            text="GO",
            bg='#FFFACD',
            fg='black')  # bg背景色；fg字體色

        i = 3
        self.ch_ID.grid(row=i, column=0, sticky=tk.W, padx=(20, 0))
        self.ch_ID_content.grid(row=i, column=1, columnspan=2, ipady=8)
        self.go.grid(row=i, column=3, columnspan=2)
        self.scrollbar.grid(
            row=i + 1,
            column=1,
            sticky=tk.E + tk.W,
            columnspan=2)

    def get_channel_ID(self, url):
        global wanted_channel_id
        website_link = url
        if website_link[0:26] == "https://www.youtube.com/c/":  # 若連結為該形式，告訴使用者輸入錯誤
            wanted_channel_id = "No channel ID"
            sys.exit()

        if website_link[0:29] == "https://www.youtube.com/user/":
            wanted_channel_id = "No channel ID"
            sys.exit()

        else:

            wanted_channel_id = website_link[32:]
            api_key = 'AIzaSyABgOEaH7Y49Ns-qPk5d8BBRwUeuZMs-Rw'
            youtube = build('youtube', 'v3', developerKey=api_key)
            res = youtube.channels().list(
                id=wanted_channel_id,
                part='contentDetails').execute()
        return wanted_channel_id

    def channel_name(self, wanted_channel_id):
        api_key = 'AIzaSyABgOEaH7Y49Ns-qPk5d8BBRwUeuZMs-Rw'
        youtube = build('youtube', 'v3', developerKey=api_key)
        res = youtube.channels().list(id=wanted_channel_id,
                                      part='brandingSettings').execute()
        name = res['items'][0]['brandingSettings']['channel']['title']
        return name

    def total_view_time(self, wanted_channel_id):  # 輸入頻道ID獲取該頻道的總觀看次數
        key = 'AIzaSyABgOEaH7Y49Ns-qPk5d8BBRwUeuZMs-Rw'
        data = urllib.request.urlopen(
            "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" +
            wanted_channel_id +
            "&key=" +
            key).read()  # 讀取資料
        total_view = json.loads(data)['items'][0]['statistics']['viewCount']
        return total_view

    def total_subscribers(self, wanted_channel_id):  # 輸入頻道ID獲取該頻道的總訂閱數
        key = 'AIzaSyABgOEaH7Y49Ns-qPk5d8BBRwUeuZMs-Rw'
        data = urllib.request.urlopen(
            "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" +
            wanted_channel_id +
            "&key=" +
            key).read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        return subs

    def channel_description(self, wanted_channel_id):  # 輸入頻道ID獲取頻道簡介
        api_key = 'AIzaSyABgOEaH7Y49Ns-qPk5d8BBRwUeuZMs-Rw'
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        res = self.youtube.channels().list(id=wanted_channel_id,
                                           part='brandingSettings').execute()
        try:
            description = res['items'][0]['brandingSettings']['channel']['description']

        except BaseException:
            description = "沒有資料"
        return description

    def get_channel_videos(self, channel_id):  # 找出頻道的所有影片
        # get Uploads playlist id
        res = self.youtube.channels().list(id=channel_id,
                                           part='contentDetails').execute()
        playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        videos = []
        next_page_token = None  # 如果沒有下一頁(已找到最後一頁)

        while True:
            res = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                    part='snippet',
                                                    maxResults=50,
                                                    pageToken=next_page_token).execute()
            videos += res['items']
            next_page_token = res.get('nextPageToken')

            if next_page_token is None:
                break

        return videos

    def get_video_stats(self, video_ids):
        videos = self.get_channel_videos(wanted_channel_id)
        res = self.youtube.videos().list(
            id=videos[0]['snippet']['resourceId']['videoId'],
            part='statistics').execute()
        stats = []
        for i in range(0, len(video_ids), 50):
            res = self.youtube.videos().list(id=','.join(
                video_ids[i:i + 50]), part='snippet,contentDetails,statistics').execute()
            stats += res['items']
        return stats

    def ten_videos(self):
        videos = self.get_channel_videos(wanted_channel_id)
        video_ids = list(
            map(lambda x: x['snippet']['resourceId']['videoId'], videos))
        stats = self.get_video_stats(video_ids)
        count = 0
        most_liked = sorted(
            stats,
            key=lambda x: int(
                x['statistics']['likeCount']),
            reverse=True)
        temporary_list = []  # 暫存的列表
        final_list = []

        for video in most_liked:
            temporary_list.append(video['snippet']['title'])  # 影片名稱
            temporary_list.append(video['statistics']['viewCount'])  # 該影片觀看數
            a = int(video['statistics']['likeCount'])
            b = int(video['statistics']['dislikeCount'])
            temporary_list.append(format(a / b, '0.0f'))  # 讚踩比
            temporary_list.append(video['statistics']['commentCount'])  # 評論數
            temporary_list.append("https://www.youtube.com/watch?v=" +
                                  video['id'])  # 影片連結
            final_list.append(temporary_list)
            temporary_list = []
            count += 1
            if count == 10:
                break
        return final_list

    def click_go(self):
        global channel_name
        global channel_views
        global channel_descrip
        global channel_sub
        global wanted_channel_id
        global videos_list

        try:
            self.destroy()
            self.sel()
            channel_url = link
            wanted_channel_id = self.get_channel_ID(channel_url)
            channel_name = self.channel_name(wanted_channel_id)
            channel_views = self.total_view_time(wanted_channel_id)
            channel_sub = self.total_subscribers(wanted_channel_id)
            channel_descrip = self.channel_description(wanted_channel_id)

            videos_list = self.ten_videos()
            yt_result3 = YoutubeChannelResult()
            yt_result3.mainloop()
        except BaseException:
            self.wrong_message = tk.messagebox.showwarning(
                title="小提醒", message="請輸入正確的頻道連結")
            tk.Frame.__init__(self)
            self.grid()
            self.design()
            self.create_widgets()
            self.master.title("Special YouTube Recommendation")
            self.master.geometry("800x600")
            self.yt_icon()


class YoutubePlaylistSearch(tk.Frame):  # 播放清單搜尋頁
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.design()
        self.create_widgets()
        self.master.title("Special YouTube Recommendation")
        self.master.geometry("800x600")
        self.yt_icon()

    def design(self):
        self.img = Image.open(
            "D:\\商管程\\final project\\PBC-final-project\\bg6.png")
        self.image2 = ImageTk.PhotoImage(self.img)
        self.design1 = tk.Canvas(self, width=800, height=600, bg="black")
        self.design1.create_image(400, 300, image=self.image2, anchor="center")
        self.design1.grid(
            row=0,
            column=0,
            columnspan=5,
            rowspan=26,
            sticky="nw")

    def yt_icon(self):
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁", weight="bold")
        self.home = tk.Button(self, command=self.return_home,
                              font=f3, text="回首頁", bg='white', fg='black')
        self.home.grid(row=0, column=1, sticky=tk.W, pady=(60, 0))

    def return_home(self):
        self.destroy()
        enter_search = SearchType()
        enter_search.mainloop()

    def sel(self):
        global selection
        global pl_url
        pl_url = self.playlist_ID_content.get()
        selection = radio_value5.get()

    def create_widgets(self):
        f1 = tkFont.Font(size=20, family="王漢宗細黑體繁")
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")
        self.scrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)

        self.playlist_ID = tk.Label(
            self,
            text="輸入播放清單網址",
            font=f1,
            height=1,
            width=15,
            bg="#ffcccc")
        self.playlist_ID_content = tk.Entry(
            self, bd=3, font=f2, width=40, xscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.playlist_ID_content.xview)
        self.selection = tk.Label(self, text="篩選器",
                                  font=f1, height=1, width=15, bg="#FFA07A")

        self.order = tk.Label(
            self,
            text="排序依據",
            font=f1,
            height=1,
            width=15,
            bg="#ffcccc")

        global radio_value5
        radio_value5 = tk.IntVar()
        radio_value5.set(0)

        global selection
        selection = radio_value5.get()

        self.comment = tk.Radiobutton(
            self,
            text="留言數量",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value5,
            command=self.sel,
            value=1)
        self.date = tk.Radiobutton(
            self,
            text="上傳日期",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value5,
            command=self.sel,
            value=2)
        self.rating = tk.Radiobutton(
            self,
            text="喜愛程度",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value5,
            command=self.sel,
            value=3)
        self.view = tk.Radiobutton(
            self,
            text="觀看次數",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value5,
            command=self.sel,
            value=4)
        self.title = tk.Radiobutton(
            self,
            text="依筆畫/字母排序",
            font=f2,
            bg='#f8f8ee',
            variable=radio_value5,
            command=self.sel,
            value=5)
        self.go = tk.Button(
            self,
            command=self.click_go,
            font=f3,
            text="GO",
            bg='#FFFACD',
            fg='#FF8C00')  # bg背景色；fg字體色

        i = 3
        self.playlist_ID.grid(row=i + 0, column=0)
        self.playlist_ID_content.grid(
            row=i + 0, column=1, columnspan=2, ipady=8)
        self.selection.grid(row=i + 2, column=0, pady=(20, 20))

        k = 0
        self.order.grid(row=k + 8, column=0)
        self.comment.grid(row=k + 9, column=1, sticky=tk.W)
        self.date.grid(row=k + 9, column=2, sticky=tk.W)
        self.view.grid(row=k + 10, column=2, sticky=tk.W)
        self.rating.grid(row=k + 10, column=1, sticky=tk.W)
        self.title.grid(row=k + 11, column=1, sticky=tk.W)

        self.go.grid(
            row=k + 15,
            column=0,
            columnspan=4,
            padx=(
                80,
                0),
            pady=(
                40,
                0))

    def playlist_time(self, pl_id):
        hours_pattern = re.compile(r'(\d+)H')
        minutes_pattern = re.compile(r'(\d+)M')
        seconds_pattern = re.compile(r'(\d+)S')
        total_seconds = 0

        nextPageToken = None
        try:
            while True:
                api_key = 'AIzaSyABgOEaH7Y49Ns-qPk5d8BBRwUeuZMs-Rw'
                youtube = build('youtube', 'v3', developerKey=api_key)
                pl_request = youtube.playlistItems().list(
                    part='contentDetails',
                    playlistId=pl_id,
                    maxResults=50,  # 一個清單裡有多個video，且總影片數目大過於五
                    pageToken=nextPageToken
                )

                pl_response = pl_request.execute()

                vid_ids = []
                for item in pl_response['items']:
                    vid_ids.append(item['contentDetails']['videoId'])

                vid_request = youtube.videos().list(
                    part="contentDetails",
                    id=','.join(vid_ids)
                )

                vid_response = vid_request.execute()

                for item in vid_response['items']:
                    duration = item['contentDetails']['duration']

                    hours = hours_pattern.search(duration)
                    minutes = minutes_pattern.search(duration)
                    seconds = seconds_pattern.search(duration)

                    hours = int(hours.group(1)) if hours else 0
                    minutes = int(minutes.group(1)) if minutes else 0
                    seconds = int(seconds.group(1)) if seconds else 0

                    video_seconds = timedelta(
                        hours=hours,
                        minutes=minutes,
                        seconds=seconds
                    ).total_seconds()

                    total_seconds += video_seconds

                nextPageToken = pl_response.get('nextPageToken')

                if not nextPageToken:
                    break

            total_seconds = int(total_seconds)

            minutes, seconds = divmod(total_seconds, 60)
            hours, minutes = divmod(minutes, 60)

            num = str(len(vid_ids))  # 影片數量
            time = f'{hours}:{minutes}:{seconds}'  # 清單總時長

            return num, time

        except BaseException:
            num = "Sorry...Something went wrong"
            time = "Sorry...Something went wrong"
            return num, time

    # playlist 排序
    def playlist_search(self, pl_id, order):
        videos = []

        nextPageToken = None

        while True:
            api_key = 'AIzaSyABgOEaH7Y49Ns-qPk5d8BBRwUeuZMs-Rw'
            youtube = build('youtube', 'v3', developerKey=api_key)
            pl_request = youtube.playlistItems().list(
                part='contentDetails,snippet',
                playlistId=pl_id,
                maxResults=50,  # 一個清單裡有多個video，且總影片數目大過於五
                pageToken=nextPageToken)

            pl_response = pl_request.execute()
            #########
            vid_ids = []
            for item in pl_response['items']:
                vid_ids.append(item['contentDetails']['videoId'])

            vid_request = youtube.videos().list(
                part="statistics, snippet",
                id=','.join(vid_ids))

            vid_response = vid_request.execute()

            for item in vid_response['items']:
                vid_views = item['statistics']['viewCount']
                if int(item['statistics']['likeCount']) == 0:
                    vid_like = 1
                else:
                    vid_like = int(item['statistics']['likeCount'])
                if int(item['statistics']['dislikeCount']) == 0:
                    vid_dislike = 1
                else:
                    vid_dislike = int(item['statistics']['dislikeCount'])
                like_dislike_ratio = '%.3f' % (
                    int(vid_like) / int(vid_dislike))
                vid_favorite = item['statistics']['favoriteCount']
                vid_comment = item['statistics']['commentCount']
                vid_title = item['snippet']['title']
                date = item['snippet']['publishedAt']

                vid_id = item["id"]
                yt_link = f'http://youtu.be/{vid_id}'
                # date = item

                videos.append(
                    {
                        "title": vid_title,
                        "views": int(vid_views),
                        "like": int(vid_like),
                        "dislike": int(vid_dislike),
                        "like_dislike_ratio": float(like_dislike_ratio),
                        "favorite": int(vid_favorite),
                        "comment": int(vid_comment),
                        "date": date,
                        "url": yt_link,

                    }
                )

            nextPageToken = pl_response.get('nextPageToken')

            if not nextPageToken:
                break

        videos.sort(key=lambda vid: vid[order], reverse=True)

        video_list_before = []
        for video in videos[:10]:  # 前十名關鎧次數清單
            video_list_before.append([video["title"],
                                      video["views"],
                                      video["like_dislike_ratio"],
                                      video["comment"],
                                      video["url"]])
            # print(video_list_before)
        return video_list_before

    def click_go(self):
        pl_url = self.playlist_ID_content.get()
        api_key = 'AIzaSyABgOEaH7Y49Ns-qPk5d8BBRwUeuZMs-Rw'
        youtube = build('youtube', 'v3', developerKey=api_key)
        try:
            global pl_id
            pl_id = pl_url[(pl_url.find("list=") + 5)                           :pl_url.find("&ab_channel=")]  # 抓取playlist id

            global vid_num
            global vid_time
            vid_num, vid_time = self.playlist_time(pl_id)

            global videos_list

            if selection == 1:
                self.destroy()
                videos_list = self.playlist_search(pl_id, "comment")

                yt_result3 = YoutubePlaylistResult()
                yt_result3.mainloop()

            elif selection == 2:
                self.destroy()
                videos_list = self.playlist_search(pl_id, "date")
                yt_result3 = YoutubePlaylistResult()
                yt_result3.mainloop()

            elif selection == 3:
                self.destroy()
                videos_list = self.playlist_search(pl_id, "favorite")
                yt_result3 = YoutubePlaylistResult()
                yt_result3.mainloop()

            elif selection == 4:
                self.destroy()
                videos_list = self.playlist_search(pl_id, "views")
                print(videos_list)
                yt_result3 = YoutubePlaylistResult()
                yt_result3.mainloop()

            elif selection == 5:
                self.destroy()
                videos_list = self.playlist_search(pl_id, "title")
                yt_result3 = YoutubePlaylistResult()
                yt_result3.mainloop()
        except BaseException:
            self.wrong_message = tk.messagebox.showwarning(
                title="小提醒", message="請輸入正確的播放清單連結")
            tk.Frame.__init__(self)
            self.grid()
            self.design()
            self.create_widgets()
            self.master.title("Special YouTube Recommendation")
            self.master.geometry("800x600")
            self.yt_icon()


class SearchType(tk.Frame):  # 首頁(選擇搜尋類型)
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("Special YouTube Recommendation")
        self.master.geometry("800x600")
        self.design()
        self.type_button()

    def type_button(self):
        f1 = tkFont.Font(size=20, family="王漢宗細黑體繁", weight="bold")
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")
        self.type_ = tk.Label(
            self,
            text="請選擇搜尋類型",
            font=f1,
            height=1,
            width=14,
            bg="#ffcccc")

        self.video = tk.Button(
            self,
            text="影片",
            font=f3,
            height=5,
            padx=30,
            command=self.fun1,
            bg='#FFFACD')  # 按下影片鍵 跑到影片搜尋頁
        self.channel = tk.Button(
            self,
            text="頻道",
            font=f3,
            height=5,
            padx=30,
            command=self.fun2,
            bg='#FFFACD')  # 按下頻道鍵 跑到頻道搜尋頁
        self.playlist = tk.Button(
            self,
            text="播放清單",
            font=f3,
            height=5,
            padx=15,
            command=self.fun3,
            bg='#FFFACD')  # 按下播放清單鍵 跑到播放清單搜尋頁
        j = 1
        self.type_.grid(
            row=j + 4,
            column=0,
            columnspan=3,
            sticky="we",
            pady=(
                20,
                30),
            padx=(
                80,
                0))
        self.video.grid(row=j + 5, column=0, sticky=tk.E, padx=(0, 20))
        self.channel.grid(row=j + 5, column=1, sticky=tk.E, padx=(0, 20))
        self.playlist.grid(row=j + 5, column=2, sticky=tk.E)

    def design(self):
        self.img = Image.open(
            "D:\\商管程\\final project\\PBC-final-project\\bg6.png")
        self.image2 = ImageTk.PhotoImage(self.img)
        self.design1 = tk.Canvas(self, width=800, height=600, bg="black")
        self.design1.create_image(400, 300, image=self.image2, anchor="center")
        self.design1.grid(
            row=0,
            column=0,
            columnspan=5,
            rowspan=16,
            sticky="nw")

    def video_go(self):
        yt_recom1 = YoutubeVideoSearch()
        yt_recom1.mainloop()

    def channel_go(self):
        yt_recom2 = YoutubeChannelSearch()
        yt_recom2.mainloop()

    def playlist_go(self):
        yt_recom3 = YoutubePlaylistSearch()
        yt_recom3.mainloop()

    def quit_(self):
        self.destroy()

    def fun1(self):  # 清除畫面與前往影片搜尋頁
        self.quit_()
        self.video_go()

    def fun2(self):
        self.quit_()
        self.channel_go()

    def fun3(self):
        self.quit_()
        self.playlist_go()


enter_search = SearchType()
enter_search.mainloop()
