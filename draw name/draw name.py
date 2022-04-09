from tkinter import *

a_pattern = """
############### ###############
##############   ##############
#############     #############
############   #   ############
###########   ###   ###########
##########   #####   ##########
#########   #######   #########
########               ########
#######                 #######
######                   ######
#####   ###############   #####
####   #################   ####
###   ###################   ###
##   #####################   ##
#   #######################   #
###############################
"""

i,j = 0,0
cap_a= []
for s in a_pattern:
    if s == " ":
        cap_a.append((i,j))
    i+=1
    if s == "\n":
        i=0
        j=j+1
        

def submit():
    c.delete("all")
    s = int(t1.get())
    w = int(t2.get())
    c["bg"] = t4.get()
    color_lst = list(t3.get().split(","))
    for (x,y) in cap_a:
        color_ind = cap_a.index((x,y))%len(color_lst)
        c.create_oval(s*x,s*y,s*x+w,s*y+w,fill = color_lst[color_ind])



top = Tk()
top.geometry("700x600")
top.title("Style Your Name")


t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()

Label(top,text = "Size:",font = ("Arial",15)).place(x = 50,y = 40)
e1 = Entry(top,width = 10 ,textvariable = t1, font = ("Arial",15))
e1.place(x = 190,y = 40)
Label(top,text = "Bg-color:",font = ("Arial",15)).place(x = 50,y = 160)
e4 = Entry(top,width = 10 ,textvariable = t4, font = ("Arial",15))
e4.place(x = 190,y = 160)
Label(top,text = "Width:",font = ("Arial",15)).place(x = 50,y = 80)
e2 = Entry(top,width = 10 , textvariable = t2,font = ("Arial",15))
e2.place(x = 190,y = 80)
Label(top,text = "Color List:",font = ("Arial",15)).place(x = 50,y = 120)
e3 = Entry(top,width = 20 , textvariable = t3,font = ("Arial",15))
e3.place(x = 190,y = 120)
b = Button(top,text="SUBMIT",font = ("Arial",20),command = submit)
b.place(x =500 , y = 100)
c = Canvas(top,width = 2000,height = 2000)
c.place(x = 0 , y = 200)

t1.set("20")
t2.set("40")
t3.set("blue,red,green,orange")
t4.set("black")


top.mainloop()