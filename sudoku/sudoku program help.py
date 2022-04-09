# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:33:19 2021

@author: Admin
"""

for i in range(9):
    print("[",end="")
    for j in range(1,10):
        if i == 0:
            print("n{}".format(j),end="") 
        else:
            print("n{}{}".format(i,j),end="") 
        if j !=9:
            print(",",end="")
    print("] ,")