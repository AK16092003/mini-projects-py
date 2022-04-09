# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 21:54:20 2021
@author: Admin
"""

from tkinter import *
from tkinter import messagebox
import time
from tictactoelogic import *

top = Tk()
top.geometry("500x500") 
top.title("Tic Tac Toe")
top.iconbitmap("icon.ico")
cur_stat = ["","","","","","","","",""]

def reset():
    global cur_stat
    cur_turn.set("Its Your Turn")
    cur_stat = ["","","","","","","","",""]
    for i in range(9):
        update_game(i)

def update_game(x):
        
    x_color = "red"
    o_color = "blue"
    
    if x == 0:
        if cur_stat[0] == "X":
            Button(top,text="X",bg="white",fg= x_color,width=3,font=("Arial",30),command = enter1).place(x = 100,y = 100)
        elif cur_stat[0] == "O":
            Button(top,text="O",bg="white",fg = o_color,width=3,font=("Arial",30),command = enter1).place(x = 100,y = 100)
        else:
            Button(top,text="",bg="white",fg = x_color,width=3,font=("Arial",30),command = enter1).place(x = 100,y = 100)
        
    if x == 1:   
        if cur_stat[1] == "X":
            Button(top,text="X",bg="white",fg= x_color,width=3,font=("Arial",30),command = enter2).place(x = 200,y = 100)
        elif cur_stat[1] == "O":
            Button(top,text="O",bg="white",fg = o_color,width=3,font=("Arial",30),command = enter2).place(x = 200,y = 100)
        else:
            Button(top,text="",bg="white",fg = x_color,width=3,font=("Arial",30),command = enter2).place(x = 200,y = 100)
    
    if x == 2:
        if cur_stat[2] == "X":
            Button(top,text="X",bg="white",fg= x_color,width=3,font=("Arial",30),command = enter3).place(x = 300,y = 100)
        elif cur_stat[2] == "O":
            Button(top,text="O",bg="white",fg = o_color,width=3,font=("Arial",30),command = enter3).place(x = 300,y = 100)
        else:
            Button(top,text="",bg="white",fg = x_color,width=3,font=("Arial",30),command = enter3).place(x = 300,y = 100)
    
    if x == 3: 
        if cur_stat[3] == "X":
            Button(top,text="X",bg="white",fg= x_color,width=3,font=("Arial",30),command = enter4).place(x = 100,y = 200)
        elif cur_stat[3] == "O":
            Button(top,text="O",bg="white",fg = o_color,width=3,font=("Arial",30),command = enter4).place(x = 100,y = 200)
        else:
            Button(top,text="",bg="white",fg = x_color,width=3,font=("Arial",30),command = enter4).place(x = 100,y = 200)
    
    if x == 4:  
        if cur_stat[4] == "X":
            Button(top,text="X",bg="white",fg= x_color,width=3,font=("Arial",30),command = enter5).place(x = 200,y = 200)
        elif cur_stat[4] == "O":
            Button(top,text="O",bg="white",fg = o_color,width=3,font=("Arial",30),command = enter5).place(x = 200,y = 200)
        else:
            Button(top,text="",bg="white",fg = x_color,width=3,font=("Arial",30),command = enter5).place(x = 200,y = 200)
    
    if x == 5:
        if cur_stat[5] == "X":
            Button(top,text="X",bg="white",fg= x_color,width=3,font=("Arial",30),command = enter6).place(x = 300,y = 200)
        elif cur_stat[5] == "O":
            Button(top,text="O",bg="white",fg = o_color,width=3,font=("Arial",30),command = enter6).place(x = 300,y = 200)
        else:
            Button(top,text="",bg="white",fg = x_color,width=3,font=("Arial",30),command = enter6).place(x = 300,y = 200)
    
    if x == 6:
        if cur_stat[6] == "X":
            Button(top,text="X",bg="white",fg= x_color,width=3,font=("Arial",30),command = enter7).place(x = 100,y = 300)
        elif cur_stat[6] == "O":
            Button(top,text="O",bg="white",fg = o_color,width=3,font=("Arial",30),command = enter7).place(x = 100,y = 300)
        else:
            Button(top,text="",bg="white",fg = x_color,width=3,font=("Arial",30),command = enter7).place(x = 100,y = 300)
    
    if x == 7:  
        if cur_stat[7] == "X":
            Button(top,text="X",bg="white",fg= x_color,width=3,font=("Arial",30),command = enter8).place(x = 200,y = 300)
        elif cur_stat[7] == "O":
            Button(top,text="O",bg="white",fg = o_color,width=3,font=("Arial",30),command = enter8).place(x = 200,y = 300)
        else:
            Button(top,text="",bg="white",fg = x_color,width=3,font=("Arial",30),command = enter8).place(x = 200,y = 300)
    
    if x == 8: 
        if cur_stat[8] == "X":
            Button(top,text="X",bg="white",fg= x_color,width=3,font=("Arial",30),command = enter9).place(x = 300,y = 300)
        elif cur_stat[8] == "O":
            Button(top,text="O",bg="white",fg = o_color,width=3,font=("Arial",30),command = enter9).place(x = 300,y = 300)
        else:
            Button(top,text="",bg="white",fg = x_color,width=3,font=("Arial",30),command = enter9).place(x = 300,y = 300)
    
    
    

def process(n):
    
    global cur_stat
    if cur_turn.get() in ["You Win","Computer Wins","Its a draw"]:
        messagebox.showwarning("Game Over","Game is already over , restart to play a new game")
        return
    if cur_stat[n-1] == "":
        cur_stat[n-1] = "X"
        update_game(n-1)
    else:
        messagebox.showwarning("Invalid","Place Already Occupied")
        return
    
    if win(cur_stat,"X"):
        cur_turn.set("You Win")
        return
    if draw(cur_stat):
        cur_turn.set("Its a draw")
        return
    cur_turn.set("Computer's Turn")
    top.update()
    time.sleep(1)
    n1 = next_move(cur_stat)
    cur_stat[n1] = "O"
    update_game(n1)
    
    if win(cur_stat,"O"):
        cur_turn.set("Computer Wins")
        return
    cur_turn.set("Its Your Turn")
    
    
def enter1():
    process(1)
def enter2():
    process(2)
def enter3():
    process(3)
def enter4():
    process(4)
def enter5():
    process(5)
def enter6():
    process(6)
def enter7():
    process(7)
def enter8():
    process(8)
def enter9():
    process(9)
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()
t8 = StringVar()
t9 = StringVar()
cur_turn= StringVar()

Label(top,text = "TIC",fg = "blue" , font = ("Arial",20)).place(x = 150,y=10)
Label(top,text = "TAC",fg = "green" , font = ("Arial",20)).place(x = 200,y=10)
Label(top,text = "TOE",fg = "red" , font = ("Arial",20)).place(x = 260,y=10)
Label(top,textvariable = cur_turn , font = ("Arial",15) ).place(x = 180,y=50)
cur_turn.set("Its Your Turn")
reset()
rst = Button(top,text="RESET",font=("Arial",20),command = reset).place(x = 180,y = 400)

top.mainloop()
