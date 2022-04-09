# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 20:34:14 2021

@author: Admin
"""
from tkinter import *
import time
l = ["00:00:00.0"]
def reset():
    global a,state,c,l
    l = ["00:00:00.0"]
    c = 0
    a.set("00:00:00.0")
    b.set("")
    state = "reset"
 
def process(x):
    hr = x//(60*60)
    x %= 3600
    mi = x//60
    x%=60
    se = x//1
    x%=1
    ml = x//0.1
    hr = str(int(hr))
    mi = str(int(mi))
    se = str(int(se))
    ml = str(int(ml))
    while len(hr)!=2:
        hr = "0"+hr
    while len(mi)!=2:
        mi = "0"+mi
    while len(se)!=2:
        se = "0"+se
    while len(ml)!=1:
        ml = "0"+ml
    return hr+":"+mi+":"+se+"."+ml
    
def stop():
    
    global a,state
    state = "stop"
    
def start():
    global c,state
    interv = 0.1
    state = "start"
    while True:
        if state == "reset" or state == "stop":
            break
        c += interv
        _str = process(round(c,1))
        a.set(_str)
        
        if state == "reset" or state == "stop":
            break
        top.update()
        if state == "reset" or state == "stop":
            break
        time.sleep(interv)
        
def sub(a1,a2):
    hr1 = int(a1[:2])
    min1 =int(a1[3:5])
    sec1 =int(a1[6:8])
    mil1 =int(a1[9])
    t1 = hr1*60*60 + min1*60 + sec1 + mil1*0.1
    
    hr2 = int(a2[:2])
    min2 =int(a2[3:5])
    sec2 =int(a2[6:8])
    mil2 =int(a2[9])
    t2 = hr2*60*60 + min2*60 + sec2 + mil2*0.1
    return process(round(abs(t2-t1),1))
    
    
def lap():
    
    global c,state,l
    state = "lap"
    s = b.get()
    x = "0"
    if len(l)>=10:
        x = ""
    s += "\n"+x+str(len(l))+") "+" "*30
    s += a.get()
    l.append(a.get())
    if len(l) >1:
        s +=" "*35+ sub(l[-1],l[-2])
    b.set(s)
    
state = ""
c = 0
top = Tk()
top.geometry("700x400")
top.title("Stop Watch")
top["bg"] = "white"
a = StringVar()
b = StringVar()
l1= Label(top,textvariable = a ,bg = "white", font = ("Arial",30)).place(x = 250,y = 40)
b1= Button(top,text = "Start" ,bg = "yellow" , command = start, font = ("Arial",20)).place(x = 150,y = 90)
b2= Button(top,text = "Stop" ,bg = "orange" ,command = stop, font = ("Arial",20)).place(x = 240,y = 90)
b3= Button(top,text = "Reset" ,bg = "violet" , command = reset, font = ("Arial",20)).place(x = 330,y = 90)
b4= Button(top,text = "Lap" ,bg = "aqua" ,command = lap, font = ("Arial",20)).place(x = 435,y = 90)

l1= Label(top,textvariable = b ,bg = "white" , fg = "red", font = ("Arial",12)).place(x = 100,y = 180)

a.set("00:00:00.0")
start = time.time()
top.mainloop()




