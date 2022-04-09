# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 22:23:42 2021

@author: Admin
"""
def draw(cur_stat):
    for i in cur_stat:
        if i == "":
            return False
    return True

def no_of_time(cur_stat):
    c = 9
    for i in cur_stat:
        if i == "":
            c-=1
    return c
def win(l,pl):
    if l[0] == l[1] == l[2] == pl:
        return True
    if l[3] == l[4] == l[5] == pl:
        return True
    if l[6] == l[7] == l[8] == pl:
        return True
    if l[0] == l[4] == l[8] == pl:
        return True
    if l[2] == l[4] == l[6] == pl:
        return True
    if l[0] == l[3] == l[6] == pl:
        return True
    if l[1] == l[4] == l[7] == pl:
        return True
    if l[2] == l[5] == l[8] == pl:
        return True
    return False

def win_2_way(cur,pl):
    ans = []
    for i in range(9):
        if cur[i] == "":
            cur1 = list(cur)
            cur1[i] = pl
            if win(cur1,pl):
                ans.append(i)
    if len(ans)>=2:
        return True
    return False
    
def next_move(cur_stat):
    
    
    n = no_of_time(cur_stat)
    if n ==1:
        if cur_stat[4] == "":
            return 4
        elif cur_stat[0] == "":
            return 0
    else:
        # check win chance for me also opponent
        
        for i in range(9):
            if cur_stat[i] == "":
                cur = list(cur_stat)
                
                cur[i] = "O"
                if win(cur,"O"):
                    return i
        
        for i in range(9):
            if cur_stat[i] == "":
                cur = list(cur_stat)
                cur[i] = "X"
                if win(cur,"X"):
                    return i
        if n ==3:
            if cur_stat == ["X","","","","O","","","","X"]:
                return 1
            if cur_stat == ["","","X","","O","","X","",""]:
                return 1
        for i in range(9):
            if cur_stat[i] == "":
                cur = list(cur_stat)
                
                cur[i] = "O"
                if win_2_way(cur,"O"):
                    return i
        
        for i in range(9):
            if cur_stat[i] == "":
                cur = list(cur_stat)
                cur[i] = "X"
                if win_2_way(cur,"X"):
                    return i
    
        for i in range(9):
            if cur_stat[i] == "":
                return i
        
        
            
    
    