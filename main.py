# sample: https://typing-speed-test.aoeu.eu/?lang=en

from tkinter import *
import ttkbootstrap
from ttkbootstrap.constants import *
from PIL import ImageTk, Image
from config import *
# from test_area import *
from test_area_ver2 import *

# ====================================================================================
app = ttkbootstrap.Window('darkly')
app.title('Typing Speed Test')
screen_width = app.winfo_screenwidth() # 1440
screen_height = app.winfo_screenheight() # 900
app.geometry(f'{screen_width}x{screen_height}+0+5')

#------------------------------------------------
photo = ImageTk.PhotoImage(LOGO_IM)
logo_lb = ttkbootstrap.Label(app, image=photo)
logo_lb.grid(row=0, column=0, columnspan=6, padx=int((screen_width - logo_lb.winfo_reqwidth())/2), pady=(30,10), sticky=EW)


current_lan = LANGUAGES[0]

main_frm = MainFrame(app, current_lan)
main_frm.grid(row=1, column=0, sticky='nsew')
# ====================================================================================
app.mainloop()


# TODO:
# 1. switch keyboard according to the current_lan
# 2. update colors of each current typing character
