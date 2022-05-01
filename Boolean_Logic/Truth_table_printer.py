from tabulate import *

"""
        ALL LOGICAL GATES HERE !
"""

def _xor(a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0):
    return a^b^c^d^e^f^g^h

def _or(a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0):
    return a|b|c|d|e|f|g|h

def _not(a):
    return 1-a

def _and(a=1,b=1,c=1,d=1,e=1,f=1,g=1,h=1):
    return a&b&c&d&e&f&g&h

def _xnor(a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0):
    return _not(_xor(a,b,c,d,e,f,g,h))

def _nor(a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0):
    return _not(_or(a,b,c,d,e,f,g,h))

def _nand(a=1,b=1,c=1,d=1,e=1,f=1,g=1,h=1):
    return _not(_and(a,b,c,d,e,f,g,h))

def inputs_lst(exp):                      # figures out list of input variables in user input
    l = set()
    count = 0
    for i in exp:
        if i.isupper():
            count += 1
            l.add(i)
    return list(l)

def generate_inputs(c):                   # generates all possible input combinations = 2^n
    
    l = []
    for n in range(2**c):
        s = str(bin(n))[2:]
        s = "0"*(c - len(s)) + s
        l.append(list(map(int,list(s))))
    return l

def evaluate(l,inp,exp):                  # evaluates the output with a combination of input 
    n = len(l)
    for i in range(n):
        exp = exp.replace(inp[i] ,str(l[i]))    # replaces the user typed expression input variables with 0 / 1
    
    return eval(exp)                            # eval(exp) - calls the respective logic gate function above
    
    
exp = input("(give input variables in upper case , gates in lower case)\nEnter expression:  ")

exp = exp.replace("xnor","_xnor")
exp = exp.replace("nand","_nand")
exp = exp.replace("nor","_nor")
exp = exp.replace("or","_or")
exp = exp.replace("xor","_xor")
exp = exp.replace("and","_and")
exp = exp.replace("not","_not")
exp = exp.replace("xn_or","xnor")
exp = exp.replace("n_or","nor")
exp = exp.replace("n_and","nand")
exp = exp.replace("x_nor","xnor")
exp = exp.replace("x_or","_xor")

inputs = inputs_lst(exp)
inputs.sort()

inp_count = len(inputs)
all_inputs = generate_inputs(inp_count)

headers = inputs+["OUTPUT"]
body = []

for l in all_inputs:
    ans = evaluate(l,inputs,exp)
    body.append(l + [ans])

print(tabulate(body , headers , tablefmt = "grid"))
