# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 21:45:00 2022
@author: Ashwanth K
"""

import os
import random

def get_file_parts(filename):
    
    n = len(filename)
    flag = 0
    extension = ""
    name = ""
    for i in range(n):
        if flag == 1:
            extension += filename[i]
        elif filename[i] != ".":
            name += filename[i]
        if filename[i] == ".":
            flag = 1
    return (name , extension)

def get_theme():
    
    cur_path = os.getcwd()    
    list_files = os.listdir(cur_path)
    
    themes = []
    total_themes = 0
    for file in list_files:
        f_name , f_extn = get_file_parts(file)
        
        # theme is stored in txt format
        if f_extn == "txt":
            themes.append(f_name)
            total_themes += 1
    if total_themes == 0:
        return  -1
    else:
        index = random.randint(1 , total_themes) - 1
        return themes[index]

def get_list_of_words(theme):
    
    file_name = theme + ".txt"
    list_words = []
    with open(file_name , "r") as fhandle:
        for word in fhandle.readlines():
            
            word = word.replace("\n", "")
            word = word.upper()

            if check_valid_word(word):
                list_words.append(word)
            else:
                #reject word
                pass
            
    fhandle.close()
    return list_words

def check_valid_word(word):
    
    n = len(word)
    alpha = 0
    open_bracket = 0
    closed_bracket = 0
    space = 0
    for i in range(n):
        if word[i].isalpha():
            alpha += 1
        elif word[i] == " ":
            space += 1
        elif word[i] == "(":
            open_bracket += 1
        elif word[i] == ")":
            closed_bracket += 1
        else:
            return False
    else:
        if open_bracket == closed_bracket and open_bracket in [0,1]:
            if alpha>space>=0:
                if alpha >= 3:
                    # allowed 
                    return True
    return False
                    
def random_word_choose(l):
    
    n = len(l)
    rand_num = random.randint(0,n-1)
    return l[rand_num].upper()

def edit_word(word):
   
    edit = []
    n = len(word)
    alpha = 0
    for i in range(n):
        if word[i].isalpha():
            alpha += 1
            edit+=["_"]
        else:
            edit += [word[i]]
    
    for i in range(n//3):
    
        r = random.randint(1,alpha)
        c = 0
        for i in range(n):
            if word[i].isalpha():
                c += 1
                if c == r:
                    edit[i] = word[i]
    return edit
        
        
        
        
        
    
    
    
    
    
    