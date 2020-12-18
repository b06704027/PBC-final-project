import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from  tkinter import ttk
import textwrap

def wrap(string, length=30):  # 自動換列！！
    return '\n'.join(textwrap.wrap(string, length))


answer = 'abc'  # 之後要替代掉
like_ratio = 234
video_view = 34354554
video_name = [1,3,4,5]
video_value = "https://clay-atlas.com/blog/2019/11/07/python-chinese-tutorial-map-function/ , 234, 2324, 333, 222"
list_value = video_value.split(',')
list_value = list(map(str, list_value))
# print(list_value)
# list_value = list(map(wrap, list_value))
new_video_value = tuple(list_value)



class YoutubeVideoResult(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("Special YouTube Result")
        self.master.geometry("800x600")
        self.master.configure(background='white')
        self.create_video_result('搜索詞：'+ answer)  # 應該補放入變數(搜索詞的總和)！！
        self.click()

    
    
    def create_video_result(self, words):
        f1 = tkFont.Font(size=20, family="王漢宗細黑體繁")  # slant="italic"斜體
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")
        
        self.result = tk.Label(self, text=words, font=f3, height=1, width=10)
        
        self.table = ttk.Treeview(self, height=18, show="headings")
        self.table["columns"]=("影片名稱","影片連結","觀看次數", "讚踩比", "留言數量", "上傳時間")
        
        self.table.column("影片名稱", width=200, anchor='center')
        self.table.column("影片連結", width=200, anchor='center')
        self.table.column("觀看次數", width=80, anchor='center')
        self.table.column("讚踩比", width=80, anchor='center')
        # self.table.column("頻道追蹤人數", width=100, anchor='center')
        self.table.column("留言數量", width=80, anchor='center')
        self.table.column("上傳時間", width=200, anchor='center')
        
        self.table.heading("影片名稱", text="影片名稱")
        self.table.heading("影片連結", text="影片連結")
        self.table.heading("觀看次數", text="觀看次數")
        self.table.heading("讚踩比", text="讚踩比")
        # self.table.heading("頻道追蹤人數", text="頻道追蹤人數")
        self.table.heading("留言數量", text="留言數量")
        self.table.heading("上傳時間", text="上傳時間")
        
        self.table.insert("", 0, text=str(video_name[0]), values= tuple(str(video_name[0]))+new_video_value)
        
        
        self.result.grid(row=0, column=0, sticky = tk.W+tk.N)
        self.table.grid(row = 2, column = 0)
        
        

    def select_item(self, event):  # 點選表格內文字
        cur_item = self.table.item(self.table.focus())
        col = self.table.identify_column(event.x)
        # print ('curItem = ', cur_item)
        # print ('col = ', col)

        if col in '#1#2#3#4#5#6':
            cell_value = cur_item['values'][1]
        print(cur_item['text'])  # 印出影片名稱
        print ('cell_value = ', cell_value)  # 印出網址
    
    def click(self):
        self.table.bind('<ButtonRelease-1>', self.select_item)
    

    
yt_recom = YoutubeVideoResult()
yt_recom.mainloop()
     