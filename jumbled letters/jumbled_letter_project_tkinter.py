# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:44:26 2021

@author: Admin
"""

from tkinter import *
from tkinter import messagebox
from jumbledletter import *
def submit():
    global ans_l
    txt = inp.get()
    txt = txt.lower()
    if txt == "":
        messagebox.showwarning("No Input","Please Enter some input to proceed for unscambling!")
    for i in txt:
        if i.isalpha():
            continue
        else:
            messagebox.showwarning("Invalid Input","All characters of input should be alphabets.")
            return
    if len(txt) == 1:
        messagebox.showwarning("Invalid Input","No word can be formed with 1 letter!")
        return
    
    ans = solve(txt)
    
    if ans == -1:
        messagebox.showwarning("No Solution","A meaningful word cannot be formed with given letters")
        return
    else:
        c = 1
        txt = ""
        for i in ans:
            txt += "{}) {}\n".format(c,i)
            c+=1
        ansv.set(txt)
        
top = Tk()
inp = StringVar()
ansv = StringVar()
top.geometry("500x300")
top.title("Jumbled letters")
l1 = Label(top,text="Enter the unscrambled letters below:",font = ("Arial",20)).place(x = 20,y = 10)
e1 = Entry(top,width = 15,textvariable = inp,font=("Arial",20)).place(x = 70,y = 80)
b1 = Button(top,text="SUBMIT",font = ("Arial",15),command = submit).place(x = 320,y = 75)
ans_l = Label(top,font = ("Arial",15),textvariable = ansv).place(x = 100,y = 180)
top.mainloop()
