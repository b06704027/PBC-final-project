import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image


class YoutubeVideoSearch(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create_widgets()
        self.master.title("Special YouTube Recommendation")
        self.master.geometry("800x600")
        self.yt_icon()
    
    def yt_icon(self):
        self.imageYT = ImageTk.PhotoImage(file="D:\\商管程\\final project\\PBC-final-project\\youtube_PNG6.png")
        self.YTlogo = tk.Label(self, image = self.imageYT)
        self.YTlogo.grid(row=0, column=0)
        
    def create_widgets(self):
        f1 = tkFont.Font(size=20, family="王漢宗細黑體繁")  # slant="italic"斜體
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")

        self.scrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        
        
        self.search = tk.Label(self, text="影片搜尋", font=f1, height=2, width=7)  # 搜索詞
        self.search_content = tk.Entry(self, bd=3,font=f2,width=40,
                                       xscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.search_content.xview)
        
        self.selection = tk.Label(self, text="篩選器",
                                  font=f1, height=1, width=10, bg="#FFA07A")
        self.not_search = tk.Label(self, text="不要出現", font=f3, height=2, width=10)  # 不想看到的關鍵字
        self.not_search_content = tk.Entry(self, bd=3, font=f2, width=30)
        
        
        self.order = tk.Label(self, text="排序依據", font=f3, height=1, width=10)
        
        radio_value2 = tk.IntVar()
        self.relevance = tk.Radiobutton(self, text="關聯性", font=f2, 
                                        variable=radio_value2, value=1)
        self.date = tk.Radiobutton(self, text="上傳日期", font=f2,
                                   variable=radio_value2, value=2)
        self.rating = tk.Radiobutton(self, text="喜愛程度", font=f2,
                                         variable=radio_value2, value=3)
        self.view = tk.Radiobutton(self, text="觀看次數", font=f2,
                                   variable=radio_value2, value=4)
        
        self.go = tk.Button(self, command=self.click_go,
                            font=f3, text="GO", bg='#FFFACD',fg='#FF8C00')  # bg背景色；fg字體色
        
        
        self.result = tk.Label(self, text="搜尋結果", font=f1, height=2, width=10)  # result
        self.result_content = tk.Label(self, bd=3,font=f2,width=40)
        
        # 設定每個功能的位置
        
        
        i = 3
        self.search.grid(row=i + 0, column=0)
        self.search_content.grid(row=i + 0, column=1, columnspan=2, ipady=8)
        self.scrollbar.grid(row=i + 1, column=1, sticky='we')
        self.selection.grid(row=i + 2, column=0)
        self.not_search.grid(row=i + 3, column=0)
        self.not_search_content.grid(row=i + 3, column=1, ipady=6, columnspan=2, sticky=tk.W)
        


        
        k = 15
        self.order.grid(row=k + 8, column=0) 
        self.relevance.grid(row=k + 9, column=1, sticky=tk.W)
        self.date.grid(row=k +9, column=2, sticky=tk.W)
        self.view.grid(row=k + 10, column=2, sticky=tk.W)
        self.rating.grid(row=k + 10, column=1, sticky=tk.W)
        self.go.grid(row=k +20, column=0, columnspan=4)
    
        self.result.grid(row=k+30, column=0)
        self.result_content.grid(row=k + 30, column=1, columnspan=2, ipady=8)
        
    def click_go(self):
        # 讀取搜索欄資訊entry
        pass

   
yt_recom1 = YoutubeVideoSearch()
yt_recom1.mainloop()




 
    








