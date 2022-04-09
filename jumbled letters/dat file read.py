# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 11:14:47 2021

@author: Admin
"""
import pickle
f_name = "5letter.dat"
with open(f_name,"rb") as fh:
    l = pickle.load(fh)
    print(list(l))
