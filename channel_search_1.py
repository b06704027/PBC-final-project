import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image


class YoutubeChannelSearch(tk.Frame):

    def yt_icon(self):
        self.imageYT = ImageTk.PhotoImage(file="D:\\商管程\\final project\\PBC-final-project\\youtube_PNG6.png")
        self.YTlogo = tk.Label(self, image = self.imageYT)
        self.YTlogo.grid(row=0, column=0)
        
    def create_widgets(self):
        f1 = tkFont.Font(size=20, family="王漢宗細黑體繁")  # slant="italic"斜體
        f2 = tkFont.Font(size=14, family="王漢宗細黑體繁")
        f3 = tkFont.Font(size=16, family="王漢宗細黑體繁")
    