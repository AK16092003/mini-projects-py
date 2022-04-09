# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 11:04:57 2021

@author: Admin
"""
import pickle
for n in range(2,3):
    print(n)
    f_name = "{}letter.txt".format(n)
    
    f_bin = f_name.replace("txt","dat")
    
    f_handle = open(f_name,"r")
    l = f_handle.readlines()
    l2=  []
    for i in l:
        s = i.lower().replace(" ","").replace("\n","")
        l1 = list(s)
        l1.sort()
        s1=""
        for j in l1:
            s1+=j
        l2.append((s1,s))
    f_handle.close()
    
    l2.sort()
    print(l2)
    with open(f_bin,"wb") as fh:
        pickle.dump(l2,fh)


    