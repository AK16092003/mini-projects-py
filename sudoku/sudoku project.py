import time
from tkinter import *
from tkinter import messagebox
from sudokusolver import *

top = Tk()
top.geometry("1000x500")
top.title("Sudoku Solver")

n1=StringVar()
n2=StringVar()
n3=StringVar()
n4=StringVar()
n5=StringVar()
n6=StringVar()
n7=StringVar()
n8=StringVar()
n9=StringVar()
n11=StringVar()
n12=StringVar()
n13=StringVar()
n14=StringVar()
n15=StringVar()
n16=StringVar()
n17=StringVar()
n18=StringVar()
n19=StringVar()
n21=StringVar()
n22=StringVar()
n23=StringVar()
n24=StringVar()
n25=StringVar()
n26=StringVar()
n27=StringVar()
n28=StringVar()
n29=StringVar()
n31=StringVar()
n32=StringVar()
n33=StringVar()
n34=StringVar()
n35=StringVar()
n36=StringVar()
n37=StringVar()
n38=StringVar()
n39=StringVar()
n41=StringVar()
n42=StringVar()
n43=StringVar()
n44=StringVar()
n45=StringVar()
n46=StringVar()
n47=StringVar()
n48=StringVar()
n49=StringVar()
n51=StringVar()
n52=StringVar()
n53=StringVar()
n54=StringVar()
n55=StringVar()
n56=StringVar()
n57=StringVar()
n58=StringVar()
n59=StringVar()
n61=StringVar()
n62=StringVar()
n63=StringVar()
n64=StringVar()
n65=StringVar()
n66=StringVar()
n67=StringVar()
n68=StringVar()
n69=StringVar()
n71=StringVar()
n72=StringVar()
n73=StringVar()
n74=StringVar()
n75=StringVar()
n76=StringVar()
n77=StringVar()
n78=StringVar()
n79=StringVar()
n81=StringVar()
n82=StringVar()
n83=StringVar()
n84=StringVar()
n85=StringVar()
n86=StringVar()
n87=StringVar()
n88=StringVar()
n89=StringVar()
def reset():
    
    global n1,n2,n3,n4,n5,n6,n7,n8,n9
    global n11,n12,n13,n14,n15,n16,n17,n18,n19
    global n21,n22,n23,n24,n25,n26,n27,n28,n29
    global n31,n32,n33,n34,n35,n36,n37,n38,n39
    global n41,n42,n43,n44,n45,n46,n47,n48,n49
    global n51,n52,n53,n54,n55,n56,n57,n58,n59
    global n61,n62,n63,n64,n65,n66,n67,n68,n69
    global n71,n72,n73,n74,n75,n76,n77,n78,n79
    global n81,n82,n83,n84,n85,n86,n87,n88,n89
    n1.set("")
    n2.set("")
    n3.set("")
    n4.set("")
    n5.set("")
    n6.set("")
    n7.set("")
    n8.set("")
    n9.set("")
    n11.set("")
    n12.set("")
    n13.set("")
    n14.set("")
    n15.set("")
    n16.set("")
    n17.set("")
    n18.set("")
    n19.set("")
    n21.set("")
    n22.set("")
    n23.set("")
    n24.set("")
    n25.set("")
    n26.set("")
    n27.set("")
    n28.set("")
    n29.set("")
    n31.set("")
    n32.set("")
    n33.set("")
    n34.set("")
    n35.set("")
    n36.set("")
    n37.set("")
    n38.set("")
    n39.set("")
    n41.set("")
    n42.set("")
    n43.set("")
    n44.set("")
    n45.set("")
    n46.set("")
    n47.set("")
    n48.set("")
    n49.set("")
    n51.set("")
    n52.set("")
    n53.set("")
    n54.set("")
    n55.set("")
    n56.set("")
    n57.set("")
    n58.set("")
    n59.set("")
    n61.set("")
    n62.set("")
    n63.set("")
    n64.set("")
    n65.set("")
    n66.set("")
    n67.set("")
    n68.set("")
    n69.set("")
    n71.set("")
    n72.set("")
    n73.set("")
    n74.set("")
    n75.set("")
    n76.set("")
    n77.set("")
    n78.set("")
    n79.set("")
    n81.set("")
    n82.set("")
    n83.set("")
    n84.set("")
    n85.set("")
    n86.set("")
    n87.set("")
    n88.set("")
    n89.set("")


def process():
    t1 = n1.get()
    t2 = n2.get()
    t3 = n3.get()
    t4 = n4.get()
    t5 = n5.get()
    t6 = n6.get()
    t7 = n7.get()
    t8 = n8.get()
    t9 = n9.get()
    t11 = n11.get()
    t12 = n12.get()
    t13 = n13.get()
    t14 = n14.get()
    t15 = n15.get()
    t16 = n16.get()
    t17 = n17.get()
    t18 = n18.get()
    t19 = n19.get()
    t21 = n21.get()
    t22 = n22.get()
    t23 = n23.get()
    t24 = n24.get()
    t25 = n25.get()
    t26 = n26.get()
    t27 = n27.get()
    t28 = n28.get()
    t29 = n29.get()
    t31 = n31.get()
    t32 = n32.get()
    t33 = n33.get()
    t34 = n34.get()
    t35 = n35.get()
    t36 = n36.get()
    t37 = n37.get()
    t38 = n38.get()
    t39 = n39.get()
    t41 = n41.get()
    t42 = n42.get()
    t43 = n43.get()
    t44 = n44.get()
    t45 = n45.get()
    t46 = n46.get()
    t47 = n47.get()
    t48 = n48.get()
    t49 = n49.get()
    t51 = n51.get()
    t52 = n52.get()
    t53 = n53.get()
    t54 = n54.get()
    t55 = n55.get()
    t56 = n56.get()
    t57 = n57.get()
    t58 = n58.get()
    t59 = n59.get()
    t61 = n61.get()
    t62 = n62.get()
    t63 = n63.get()
    t64 = n64.get()
    t65 = n65.get()
    t66 = n66.get()
    t67 = n67.get()
    t68 = n68.get()
    t69 = n69.get()
    t71 = n71.get()
    t72 = n72.get()
    t73 = n73.get()
    t74 = n74.get()
    t75 = n75.get()
    t76 = n76.get()
    t77 = n77.get()
    t78 = n78.get()
    t79 = n79.get()
    t81 = n81.get()
    t82 = n82.get()
    t83 = n83.get()
    t84 = n84.get()
    t85 = n85.get()
    t86 = n86.get()
    t87 = n87.get()
    t88 = n88.get()
    t89 = n89.get()
    
    puzzle = [[t1,t2,t3,t4,t5,t6,t7,t8,t9] ,
    [t11,t12,t13,t14,t15,t16,t17,t18,t19] ,
    [t21,t22,t23,t24,t25,t26,t27,t28,t29] ,
    [t31,t32,t33,t34,t35,t36,t37,t38,t39] ,
    [t41,t42,t43,t44,t45,t46,t47,t48,t49] ,
    [t51,t52,t53,t54,t55,t56,t57,t58,t59] ,
    [t61,t62,t63,t64,t65,t66,t67,t68,t69] ,
    [t71,t72,t73,t74,t75,t76,t77,t78,t79] ,
    [t81,t82,t83,t84,t85,t86,t87,t88,t89]]
    
    
    for i in range(9):
        for j in range(9):
            if "1"<=puzzle[i][j]<="9" and len(puzzle[i][j]) == 1:
                puzzle[i][j] = int(puzzle[i][j])
            elif puzzle[i][j] == "":
                puzzle[i][j] = 0
            else:
                messagebox.showwarning("Invalid Input","All input data should be within 1 to 9")
                return 
    
    
    inp_val = []
    for i in range(9):
        for j in range(9):
            if puzzle[i][j]!=0:
                inp_val.append((i,j))
    
    if not valid(puzzle):
        messagebox.showwarning("Invalid Puzzle","The given puzzle does not follow the rules of sudoku , The number should be unique in each row,column as well as within grids")
        return
    ans = []
    try:
        ans = solve(puzzle,time.time(),10)
    except:
        ans = []
    if ans:
        st = 50
        padx = 500
        w = 2
        for i in range(9):
            for j in range(9):
                if (i,j) in inp_val:
                    if 0<=i<3 and 0<=j<3:
                        Label(top,bg="aqua",fg = "red",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st ,x = j*st+padx)
                    if 0<=i<3 and 3<=j<6:
                        Label(top,bg="pink",fg = "red",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st,x = j*st+padx)
                    if 0<=i<3 and 6<=j<9:
                        Label(top,bg="light green",fg = "red",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st ,x = j*st+padx)
                    if 3<=i<6 and 0<=j<3:
                        Label(top,bg="yellow",fg = "red",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st ,x = j*st+padx)
                    if 3<=i<6 and 3<=j<6:
                        Label(top,bg="white",fg = "red",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st ,x = j*st+padx)
                    if 3<=i<6 and 6<=j<9:
                        Label(top,bg="brown",fg = "red",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st ,x = j*st+padx)
                    if 6<=i<9 and 0<=j<3:
                        Label(top,bg="blue",fg = "red",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st,x = j*st+padx)
                    if 6<=i<9 and 3<=j<6:
                        Label(top,bg="orange",fg = "red",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st,x = j*st+padx)
                    if 6<=i<9 and 6<=j<9:
                        Label(top,bg="violet",fg = "red",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st,x = j*st+padx)
                    
                    continue
                if 0<=i<3 and 0<=j<3:
                    Label(top,bg="aqua",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st ,x = j*st+padx)
                if 0<=i<3 and 3<=j<6:
                    Label(top,bg="pink",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st,x = j*st+padx)
                if 0<=i<3 and 6<=j<9:
                    Label(top,bg="light green",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st ,x = j*st+padx)
                if 3<=i<6 and 0<=j<3:
                    Label(top,bg="yellow",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st ,x = j*st+padx)
                if 3<=i<6 and 3<=j<6:
                    Label(top,bg="white",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st ,x = j*st+padx)
                if 3<=i<6 and 6<=j<9:
                    Label(top,bg="brown",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st ,x = j*st+padx)
                if 6<=i<9 and 0<=j<3:
                    Label(top,bg="blue",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st,x = j*st+padx)
                if 6<=i<9 and 3<=j<6:
                    Label(top,bg="orange",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st,x = j*st+padx)
                if 6<=i<9 and 6<=j<9:
                    Label(top,bg="violet",text = ans[i][j],font = ("Arial",30),width=w,borderwidth = 1,relief = "solid").place(y = i*st,x = j*st+padx)
                
        top.mainloop()
                
    else:
        messagebox.showwarning("No Solution","The computer program cannot find a solution for this puzzle, kindly check your values")
heading = Label(top,text = "SUDOKU SOLVER",font=("Arial",25)).place(x = 100,y = 10)
sub_heading = Label(top,text = "Enter the values below:",font=("Arial",15)).place(x = 10,y = 70)
reset()
x1=30
y1 = 200
space_y = 25
e1 = Entry(top,width = 2,textvariable = n1).place(x = x1,y = y1); x1+=20
e2 = Entry(top,width = 2,textvariable = n2).place(x = x1,y = y1); x1+=20
e3 = Entry(top,width = 2,textvariable = n3).place(x = x1,y = y1); x1+=40
e4 = Entry(top,width = 2,textvariable = n4).place(x = x1,y = y1); x1+=20
e5 = Entry(top,width = 2,textvariable = n5).place(x = x1,y = y1); x1+=20
e6 = Entry(top,width = 2,textvariable = n6).place(x = x1,y = y1); x1+=40
e7 = Entry(top,width = 2,textvariable = n7).place(x = x1,y = y1); x1+=20
e8 = Entry(top,width = 2,textvariable = n8).place(x = x1,y = y1); x1+=20
e9 = Entry(top,width = 2,textvariable = n9).place(x = x1,y = y1); x1-=200
y1+=space_y
e11 = Entry(top,width = 2,textvariable = n11).place(x = x1,y = y1); x1+=20
e12 = Entry(top,width = 2,textvariable = n12).place(x = x1,y = y1); x1+=20
e13 = Entry(top,width = 2,textvariable = n13).place(x = x1,y = y1); x1+=40
e14 = Entry(top,width = 2,textvariable = n14).place(x = x1,y = y1); x1+=20
e15 = Entry(top,width = 2,textvariable = n15).place(x = x1,y = y1); x1+=20
e16 = Entry(top,width = 2,textvariable = n16).place(x = x1,y = y1); x1+=40
e17 = Entry(top,width = 2,textvariable = n17).place(x = x1,y = y1); x1+=20
e18 = Entry(top,width = 2,textvariable = n18).place(x = x1,y = y1); x1+=20
e19 = Entry(top,width = 2,textvariable = n19).place(x = x1,y = y1); x1-=200
y1+=space_y
e21 = Entry(top,width = 2,textvariable = n21).place(x = x1,y = y1); x1+=20
e22 = Entry(top,width = 2,textvariable = n22).place(x = x1,y = y1); x1+=20
e23 = Entry(top,width = 2,textvariable = n23).place(x = x1,y = y1); x1+=40
e24 = Entry(top,width = 2,textvariable = n24).place(x = x1,y = y1); x1+=20
e25 = Entry(top,width = 2,textvariable = n25).place(x = x1,y = y1); x1+=20
e26 = Entry(top,width = 2,textvariable = n26).place(x = x1,y = y1); x1+=40
e27 = Entry(top,width = 2,textvariable = n27).place(x = x1,y = y1); x1+=20
e28 = Entry(top,width = 2,textvariable = n28).place(x = x1,y = y1); x1+=20
e29 = Entry(top,width = 2,textvariable = n29).place(x = x1,y = y1); x1-=200
y1+=space_y+10
e31 = Entry(top,width = 2,textvariable = n31).place(x = x1,y = y1); x1+=20
e32 = Entry(top,width = 2,textvariable = n32).place(x = x1,y = y1); x1+=20
e33 = Entry(top,width = 2,textvariable = n33).place(x = x1,y = y1); x1+=40
e34 = Entry(top,width = 2,textvariable = n34).place(x = x1,y = y1); x1+=20
e35 = Entry(top,width = 2,textvariable = n35).place(x = x1,y = y1); x1+=20
e36 = Entry(top,width = 2,textvariable = n36).place(x = x1,y = y1); x1+=40
e37 = Entry(top,width = 2,textvariable = n37).place(x = x1,y = y1); x1+=20
e38 = Entry(top,width = 2,textvariable = n38).place(x = x1,y = y1); x1+=20
e39 = Entry(top,width = 2,textvariable = n39).place(x = x1,y = y1); x1-=200
y1+=space_y
e41 = Entry(top,width = 2,textvariable = n41).place(x = x1,y = y1); x1+=20
e42 = Entry(top,width = 2,textvariable = n42).place(x = x1,y = y1); x1+=20
e43 = Entry(top,width = 2,textvariable = n43).place(x = x1,y = y1); x1+=40
e44 = Entry(top,width = 2,textvariable = n44).place(x = x1,y = y1); x1+=20
e45 = Entry(top,width = 2,textvariable = n45).place(x = x1,y = y1); x1+=20
e46 = Entry(top,width = 2,textvariable = n46).place(x = x1,y = y1); x1+=40
e47 = Entry(top,width = 2,textvariable = n47).place(x = x1,y = y1); x1+=20
e48 = Entry(top,width = 2,textvariable = n48).place(x = x1,y = y1); x1+=20
e49 = Entry(top,width = 2,textvariable = n49).place(x = x1,y = y1); x1-=200
y1+=space_y
e51 = Entry(top,width = 2,textvariable = n51).place(x = x1,y = y1); x1+=20
e52 = Entry(top,width = 2,textvariable = n52).place(x = x1,y = y1); x1+=20
e53 = Entry(top,width = 2,textvariable = n53).place(x = x1,y = y1); x1+=40
e54 = Entry(top,width = 2,textvariable = n54).place(x = x1,y = y1); x1+=20
e55 = Entry(top,width = 2,textvariable = n55).place(x = x1,y = y1); x1+=20
e56 = Entry(top,width = 2,textvariable = n56).place(x = x1,y = y1); x1+=40
e57 = Entry(top,width = 2,textvariable = n57).place(x = x1,y = y1); x1+=20
e58 = Entry(top,width = 2,textvariable = n58).place(x = x1,y = y1); x1+=20
e59 = Entry(top,width = 2,textvariable = n59).place(x = x1,y = y1); x1-=200
y1+=space_y+10
e61 = Entry(top,width = 2,textvariable = n61).place(x = x1,y = y1); x1+=20
e62 = Entry(top,width = 2,textvariable = n62).place(x = x1,y = y1); x1+=20
e63 = Entry(top,width = 2,textvariable = n63).place(x = x1,y = y1); x1+=40
e64 = Entry(top,width = 2,textvariable = n64).place(x = x1,y = y1); x1+=20
e65 = Entry(top,width = 2,textvariable = n65).place(x = x1,y = y1); x1+=20
e66 = Entry(top,width = 2,textvariable = n66).place(x = x1,y = y1); x1+=40
e67 = Entry(top,width = 2,textvariable = n67).place(x = x1,y = y1); x1+=20
e68 = Entry(top,width = 2,textvariable = n68).place(x = x1,y = y1); x1+=20
e69 = Entry(top,width = 2,textvariable = n69).place(x = x1,y = y1); x1-=200
y1+=space_y
e71 = Entry(top,width = 2,textvariable = n71).place(x = x1,y = y1); x1+=20
e72 = Entry(top,width = 2,textvariable = n72).place(x = x1,y = y1); x1+=20
e73 = Entry(top,width = 2,textvariable = n73).place(x = x1,y = y1); x1+=40
e74 = Entry(top,width = 2,textvariable = n74).place(x = x1,y = y1); x1+=20
e75 = Entry(top,width = 2,textvariable = n75).place(x = x1,y = y1); x1+=20
e76 = Entry(top,width = 2,textvariable = n76).place(x = x1,y = y1); x1+=40
e77 = Entry(top,width = 2,textvariable = n77).place(x = x1,y = y1); x1+=20
e78 = Entry(top,width = 2,textvariable = n78).place(x = x1,y = y1); x1+=20
e79 = Entry(top,width = 2,textvariable = n79).place(x = x1,y = y1); x1-=200
y1+=space_y
e81 = Entry(top,width = 2,textvariable = n81).place(x = x1,y = y1); x1+=20
e82 = Entry(top,width = 2,textvariable = n82).place(x = x1,y = y1); x1+=20
e83 = Entry(top,width = 2,textvariable = n83).place(x = x1,y = y1); x1+=40
e84 = Entry(top,width = 2,textvariable = n84).place(x = x1,y = y1); x1+=20
e85 = Entry(top,width = 2,textvariable = n85).place(x = x1,y = y1); x1+=20
e86 = Entry(top,width = 2,textvariable = n86).place(x = x1,y = y1); x1+=40
e87 = Entry(top,width = 2,textvariable = n87).place(x = x1,y = y1); x1+=20
e88 = Entry(top,width = 2,textvariable = n88).place(x = x1,y = y1); x1+=20
e89 = Entry(top,width = 2,textvariable = n89).place(x = x1,y = y1); x1-=200
y1+=space_y
bt = Button(top,text = "Submit" ,font=("Arial",17), command = process).place(x = 300,y = 200)
bt = Button(top,text = "Reset" ,font=("Arial",17), command = reset).place(x = 300,y = 250)
top.mainloop()
