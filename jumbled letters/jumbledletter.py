"""
Created on Tue Dec 14 10:43:37 2021
@author: Admin
"""

import pickle
from tkinter import messagebox
def sort_str(s):
    l = list(s)
    l.sort()
    s1 = ""
    for i in l:
        s1+=i
    return s1

def solve(inp):
    
    f_name = str(len(inp))+"letter.dat"
    try:
        f_handle = open(f_name,"rb")
    except:
        messagebox.showwarning("Sorry User","{} letter words are not updated in the search dictionary of this program".format(len(inp)))
    dictionary = pickle.load(f_handle)
    search_el = sort_str(inp)
    low = 0
    high = len(dictionary) - 1
    while low<=high:
        mid = (low+high)//2
        if dictionary[mid][0] == search_el:
            answers = set()
            for ind in range(mid-10,mid+10):
                if dictionary[ind][0] == search_el:
                    answers.add(dictionary[ind][1].upper())
            return answers
        elif dictionary[mid][0] > search_el:
            high = mid - 1
        else:
            low = mid + 1
    return -1


