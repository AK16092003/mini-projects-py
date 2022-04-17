# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 21:22:50 2022
@author: Ashwanth K
"""

from help_module import *
from tkinter import *
from tkinter import messagebox
import time

real_word = ""
edited_word = ""
theme = ""
hang_level = 0

def start():
    
    global real_word , edited_word,theme , text_displ,hang_level , canvas
    hang_level = 0
    canvas["bg"] = "white"
    canvas.create_line(50,50,50,450)
    canvas.create_line(50,50,330,50)
    
    theme = get_theme()
    text_head2["text"] = "Clue : "+theme
    words_list = get_list_of_words(theme)
    real_word = random_word_choose(words_list)
    edited_word = edit_word(real_word)
    real_word = list(real_word)
    text_displ["text"] = " ".join(edited_word)
    print(real_word)
    if len(edited_word) > 7:
        root.geometry("{}x500".format(750 + (20)*(len(edited_word)-7)))
        root.update()

    
def message(s , heading = "Message :"):
    # display alert message with message_box in tk
    messagebox.showinfo(heading,s)
    pass

def check_hangman():
    # hangman update content 
    global hang_level
    
    if hang_level == 1:
        canvas.create_line(250,50,250,100)
    elif hang_level == 2:
        canvas.create_oval(200,100,300,200)
    elif hang_level == 3:
        canvas.create_line(250,200,250,400)
    elif hang_level == 4:
        canvas.create_line(250,280,300,250)
    elif hang_level == 5:
        canvas.create_line(250,280,200,250)
    elif hang_level == 6:
        canvas.create_line(250,400,300,450)
    elif hang_level == 7:
        canvas.create_line(250,400,200,450)
        root.update()
        
        for i in range(10):
            time.sleep(0.2)
            canvas["bg"] = "#ff"+"00"+2*str((9-i))
            root.update()
            
    if hang_level == 7:
        # out of game
        message("Sorry You Lost the game !")
    else:
        message("Be Carefull ! You are much closer to the shark there!")
        

def check_input(char):
    
    global real_word , edited_word,hang_level
    char=char.upper()
    if hang_level == 7:
        return
    count = 0
    n = len(real_word)
    for i in range(n):
        if edited_word[i] == "_" and real_word[i] == char:
            edited_word[i] = char.upper()
            count += 1
    if count == 0:
        # update our hangman
        hang_level = hang_level + 1
        check_hangman()
    else:
        
        missing_words = edited_word.count("_")
        text_displ["text"] = " ".join(edited_word)
        root.update()
        if missing_words == 0:
            # win the game !!!
            message("You won the game ! Congratulations !, But the shark is very hungry ")
            
            for i in range(9):
                time.sleep(0.2)
                canvas["bg"] = "#00"+str((i))+"000"
                root.update()
        else:
            # correct choice
            message("Great ! , Your choice was right !")
                
        
    
def process():
    s = char.get()
    if len(s)!=1 or not s.isalpha():
        message("Please give a proper input : Only a alphabet")
    else:
        check_input(s)
        char.set("")

def restart():
    canvas.delete("all")
    start()


root = Tk()
root.title("HANGMAN")
root.geometry("750x500")
canvas =  Canvas(root , height = 500,width = 350 , bg = "white")
canvas.place(x = 0 , y =  0)

message("You need to find out the missing letters in the given word within 7 trials ,\nIf you failed to do so , then you will be the prey for our shark! \nBe carefull!"
        ,"Welcome to Hangman!")


text_displ = Label(root , font = ("Times", "24", "bold"))
text_displ.place(x = 400 , y = 50)

text_head = Label(root ,text = "Missing Word :" , font = ("Times", "20", "underline"))
text_head.place(x = 400 , y = 10)


text_head1 = Label(root ,text = "Enter a Character :" , font = ("Times", "20", ""))
text_head1.place(x = 400 , y = 250)
text_head2 = Label(root ,text = "Clue : " , font = ("Arial", "20", ""))
text_head2.place(x = 400 , y = 110)

char = StringVar()

entry = Entry(root ,textvariable = char , font = ("Arial", "25", "normal") , width = 3)
entry.place(x = 650 , y = 250)


submit =  Button(root , text = "SUBMIT" ,  font = ("Times", "20", "") , bg = "lightgreen" , command = process)
submit.place(x = 500 , y = 350)
reset =  Button(root , text = "RESTART" ,  font = ("Times", "20", "") , bg = "lightyellow" , command = restart)
reset.place(x = 490 , y = 420)




start()

root.mainloop()


