import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from  tkinter import ttk
import textwrap

def wrap(string, length=30):  # 自動換列！！
    return '\n'.join(textwrap.wrap(string, length))


answer = 'PLWdTJ5KBaxRbcm6lcLKuTi8ZmKbItKEpi'  # playlist_ID 之後要替代掉

num = str(12)  # 影片數量 之後要替代掉
time = str(234)  # 清單總時長 之後要替代掉


like_ratio = 234
video_view = 34354554
video_name = [1,3,4,5]
video_value = "234, 2324, 333, 222, https://clay-atlas.com/blog/2019/11/07/python-chinese-tutorial-map-function/"
list_value = video_value.split(',')
list_value = list(map(str, list_value))
# print(list_value)
# list_value = list(map(wrap, list_value))
new_video_value = tuple(list_value)  # 之後要替代掉



class YoutubePlaylistResult(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("Special YouTube Result")
        self.master.geometry("1000x800")
        self.master.configure(background='white')
        self.create_playlist_result('播放清單ID：'+ answer,
                                    '清單影片數量：' + num,
                                    '影片總時長：' + time)  # 應該補放入變數！！
        self.playlist_video()
        self.X_axis()
        self.Y_axis()
        self.click()
    
    
    def create_playlist_result(self, words, num, time):  # playlist 資訊欄
        f1 = tkFont.Font(size=20, family="王漢宗細黑體繁")
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")
        
        self.result = tk.Label(self, text=words, font=f3, bg='#C8DAAE',
                               height=1, width=78, anchor='nw')  # 查詢的 playlist_ID
        self.video_num = tk.Label(self, text=num, font=f2,
                                  height=1, width=15, anchor='nw')
                                  
        self.video_time = tk.Label(self, text=time, font=f2,
                                  height=1, width=15, anchor='nw')
        
        self.result.grid(row=0, column=0, sticky = tk.W+tk.N, padx=(20,10))
        self.video_num.grid(row=1, column=0, sticky = tk.W, padx=(20,10))
        self.video_time.grid(row=1, column=0, sticky = tk.W, padx=(300,0))
        
    def playlist_video(self):  # playlist中的影片資訊欄
        f1 = tkFont.Font(size=20, family="王漢宗細黑體繁")
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")
        
        self.table = ttk.Treeview(self, height=15, show="headings", selectmode='browse')
        self.table["columns"]=("影片名稱","觀看次數", "讚踩比",
                               "留言數量", "上傳時間","影片連結")
        
        self.scrollbar = ttk.Scrollbar(orient="vertical",command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar.set)
        
        self.table.column("影片名稱", width=200, anchor='center')
        self.table.column("影片連結", width=300, anchor='center')
        self.table.column("觀看次數", width=80, anchor='center')
        self.table.column("讚踩比", width=80, anchor='center')
        self.table.column("留言數量", width=80, anchor='center')
        self.table.column("上傳時間", width=200, anchor='center')
        
        self.table.heading("影片名稱", text="影片名稱")
        self.table.heading("影片連結", text="影片連結")
        self.table.heading("觀看次數", text="觀看次數")
        self.table.heading("讚踩比", text="讚踩比")
        self.table.heading("留言數量", text="留言數量")
        self.table.heading("上傳時間", text="上傳時間")
        
        self.table.insert("", 0, text=str(video_name[0]),
                          values= tuple(str(video_name[0]))+new_video_value)
             
        
        self.table.grid(row=5, column=0, sticky=tk.W, padx=(20,20))
        self.scrollbar.grid(row=5, column=1)

    def X_axis(self):
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")
        
        self.x_ = tk.Label(self, text='X軸類別', font=f3,
                           height=1, width=15, anchor='nw')
        
        radio_value1 = tk.IntVar()
        self.name = tk.Radiobutton(self, text="影片名稱", font=f2,
                                   variable=radio_value1, value=1)
        self.view = tk.Radiobutton(self, text="觀看次數", font=f2,
                                   variable=radio_value1, value=2)                                
        self.like_ratio = tk.Radiobutton(self, text="讚踩比", font=f2,
                                   variable=radio_value1, value=3)
        self.comment = tk.Radiobutton(self, text="留言數量", font=f2,
                                   variable=radio_value1, value=4)
        self.day = tk.Radiobutton(self, text="上傳天數", font=f2,  # 值需轉換
                                   variable=radio_value1, value=5)                         
        i = 6
        self.x_.grid(row=i + 2, column=0, sticky=tk.W, padx=(20,20), pady=(20,10))
        self.name.grid(row=i + 3, column=0, sticky=tk.W, padx=(20,20))
        self.view.grid(row=i + 3, column=0, sticky=tk.W, padx=(150,20))
        self.like_ratio.grid(row=i + 3, column=0, sticky=tk.W, padx=(300,20))
        self.comment.grid(row=i + 3, column=0, sticky=tk.W, padx=(450,20))
        self.day.grid(row=i + 3, column=0, sticky=tk.W, padx=(600,20))
        
        
    def Y_axis(self):
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")
        
        self.y_ = tk.Label(self, text='Y軸類別', font=f3,
                           height=1, width=15, anchor='nw')
        
        radio_value2 = tk.IntVar()
        self.name = tk.Radiobutton(self, text="影片名稱", font=f2,
                                   variable=radio_value2, value=1)
        self.view = tk.Radiobutton(self, text="觀看次數", font=f2,
                                   variable=radio_value2, value=2)                                
        self.like_ratio = tk.Radiobutton(self, text="讚踩比", font=f2,
                                   variable=radio_value2, value=3)
        self.comment = tk.Radiobutton(self, text="留言數量", font=f2,
                                   variable=radio_value2, value=4)
        self.day = tk.Radiobutton(self, text="上傳天數", font=f2,
                                   variable=radio_value2, value=5)  
        
        
        i = 20
        self.y_.grid(row=i + 2, column=0, sticky=tk.W, padx=(20,20), pady=(20,10))
        self.name.grid(row=i + 3, column=0, sticky=tk.W, padx=(20,20))
        self.view.grid(row=i + 3, column=0, sticky=tk.W, padx=(150,20))
        self.like_ratio.grid(row=i + 3, column=0, sticky=tk.W, padx=(300,20))
        self.comment.grid(row=i + 3, column=0, sticky=tk.W, padx=(450,20))
        self.day.grid(row=i + 3, column=0, sticky=tk.W, padx=(600,20))
        

    def select_item(self, event):  # 點選表格內文字
        cur_item = self.table.item(self.table.focus())
        col = self.table.identify_column(event.x)
        # print ('curItem = ', cur_item)
        # print ('col = ', col)

        if col in '#1#2#3#4#5#6':
            cell_value = cur_item['values'][5]
        # print(cur_item['text'])  # 印出影片名稱
        print ('cell_value = ', cell_value)  # 印出網址
    
    def click(self):
        self.table.bind('<ButtonRelease-1>', self.select_item)


yt_result2 = YoutubePlaylistResult()
yt_result2.mainloop()
     