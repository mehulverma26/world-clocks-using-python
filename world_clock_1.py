from tkinter import *
import tkinter as tk
from time import strftime 
import time
from datetime import datetime
import pytz
root = Tk()
root.title("World Clock")
zone='Asia/kolkata'
#manu bar
def India():
    global zone
    zone="Asia/kolkata"
def ADDIS():
    global zone
    zone="Africa/Addis_Ababa"
def Johannesburg():
    global zone
    zone="Africa/Johannesburg"
def London():
    global zone
    zone="Europe/London"
def San_Francisco():
    global zone
    zone="America/Los_Angeles"
cal=Frame(root)
Menubar=Menu(cal)
filemenu=Menu(Menubar,tearoff=0)
Menubar.add_cascade(label="Countries",menu=filemenu)
filemenu.add_command(label="India",command=India)
filemenu.add_command(label="ADDIS",command=ADDIS)
filemenu.add_command(label="Johannesburg",command=Johannesburg)
filemenu.add_command(label="London",command=London)
filemenu.add_command(label="San Francisco",command=San_Francisco)
root.config(menu=Menubar)
lbl = Label(root, font = ('Lucida Handwriting', 100, 'bold'), 
            background = 'black', 
            foreground = 'red')
lbl.pack()
def time():
    global lbl
    world=pytz.timezone(zone)
    datetime_India=datetime.now(world)
    timee=datetime_India.strftime("%H:%M:%S")
    sring = timee
    lbl.config(text=sring)
    lbl.after(1000, time)
time()
root.mainloop()