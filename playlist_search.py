import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image


class YoutubePlaylistSearch(tk.Frame):  # 頻道搜尋頁
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create_widgets()
        self.master.title("Special YouTube Recommendation")
        self.master.geometry("800x600")
        self.yt_icon()
    
    def yt_icon(self):
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁", weight="bold")
        self.imageYT = ImageTk.PhotoImage(file="D:\\商管程\\final project\\PBC-final-project\\youtube_PNG6.png")
        self.YTlogo = tk.Label(self, image = self.imageYT)
        self.YTlogo.grid(row=0, column=0)
        self.home = tk.Button(self, command=self.return_home,
                              font=f3, text="回首頁", bg='white',fg='black')
        self.home.grid(row=0, column=1, sticky=tk.W)
        
    def return_home(self):
        self.destroy()
        enter_search = SearchType()
        enter_search.mainloop()
    
    
    def create_widgets(self):
        f1 = tkFont.Font(size=20, family="王漢宗細黑體繁")  
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")
    
        self.playlist_ID =  tk.Label(self, text="輸入播放清單網址", font=f1, height=2, width=15) 
        self.playlist_ID_content = tk.Entry(self, bd=3,font=f2,width=40)
        
        self.go = tk.Button(self, command=self.click_go,
                            font=f3, text="GO", bg='#FFFACD',fg='#FF8C00')  # bg背景色；fg字體色
        
        
        i = 3
        self.playlist_ID.grid(row=i + 0, column=0, sticky= tk.W)
        self.playlist_ID_content.grid(row=i + 0, column=1, columnspan=2, ipady=8)
        self.go.grid(row=i , column=3, columnspan=2)
    
    def click_go(self):
        pass