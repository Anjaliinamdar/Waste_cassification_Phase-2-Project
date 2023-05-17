import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import time
import os
from PIL import Image
from tkinter import *
import tkinter as ttk
from tkinter.filedialog import askopenfilename
import shutil

window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("SAMPLE")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
#answer = messagebox.askquestion(dialog_title, dialog_text)
 
window.geometry('1200x600')
##window.configure(background='Grey')
from PIL import Image, ImageTk
img=Image.open('download.jpg')
img=img.resize((1400,800))
bg=ImageTk.PhotoImage(img)
label=Label(window,image=bg)
label.place(x=0,y=0)

def Start():
    os.system('python detect.py')

Button4 = tk.Label(window,fg="Black"  ,bg="white"  ,width=20  ,height=2, activebackground = "green" ,font=('times', 30, ' bold '))


Button4 = tk.Button(window, text="Detect Image", command=Start  ,fg="Black"  ,bg="white"  ,width=15  ,height=2, activebackground = "green" ,font=('times', 15, ' bold '))
Button4.place(x=590, y=580)

window.mainloop()
