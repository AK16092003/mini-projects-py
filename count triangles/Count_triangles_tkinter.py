# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 13:15:18 2022
@author: Admin
"""

from tkinter import *
from tkinter import messagebox
import time

def clear():
    
    global c ,cur_event ,  lines , list_of_points
    c.delete("all")
    lines = []
    list_of_points = []
    cur_event = "stop"
    e["text"] = "Number of triangles : 0"
    

class Point:
    x = 0
    y = 0
    def __init__(self , x , y):
        self.x = x
        self.y = y
        
    def draw(self):
        r = 10     #radius of the circle
        c.create_oval(self.x-r,self.y-r,self.x+r,self.y+r)
        
        c.create_text(self.x , self.y , text = str(len(list_of_points)))
        
    def equals(self , pt):
        x1 = pt.x
        y1 = pt.y
        if self.x == x1 and self.y == y1:
            return True
        else:
            return False
        
class Line:
    
    p1 = Point(0,0)
    p2 = Point(0,0)
    
    def __init__(self , p1 , p2):
        self.p1 = p1
        self.p2 = p2
        
    def draw(self):
        c.create_line(self.p1.x , self.p1.y , self.p2.x , self.p2.y)
        
    def slope(self):
        del_x = self.p1.x - self.p2.x
        del_y = self.p1.y - self.p2.y
        return del_y / (del_x + 10**-8)
    
    def intercept(self):
        del_x = self.p1.x - self.p2.x
        del_y = self.p1.y - self.p2.y
        m = del_y / (del_x+10**-8)
        return ((self.p1.y - m*self.p1.x) + (self.p2.y - m*self.p2.x))/ 2
    
    

list_of_points = []

lines = []
start_point = Point(0, 0)



def search(line):
    
    start_point = line.p1
    end_point = line.p2
    required_slope = line.slope()
    #print("__"*10)
    for search_line in lines:
        
        if lies_in(start_point , search_line) and (lies_in(end_point , search_line)):
            return True
        else:
            continue
            
                
def lies_in(point , line):
    d = distance_lp(point , line)
    
    if d<=1:
        
        return True
    
    return False


cur_event = "stop"



def submit():
    
    tot_points = len(list_of_points)
    print("Total points = " , tot_points)
    
    for i in range(tot_points):
        for j in range(i+1 , tot_points):
            p1 = list_of_points[i]
            p2 = list_of_points[j]
            l = Line(p1, p2)
            if search(l) == True:
                print(i+1 , j+1 , end = "")
                print("yes")
    
    
    tot_points = len(list_of_points)
    print("Total points = " , tot_points)
    
    ans = 0
    
    for i in range(tot_points):
        for j in range(i+1 , tot_points):
            for k in range(j+1 , tot_points):
                
                pt1 = list_of_points[i]
                pt2 = list_of_points[j]
                pt3 = list_of_points[k]
                if triangle(pt1 , pt2 , pt3):
                    
                    print(i+1 , j+1 , k+1 , end = " ")
                    print("triangle ")
                    ans += 1
                    line1 = c.create_line(pt1.x , pt1.y , pt2.x , pt2.y , fill = "green" , width = 5)
                    line2 = c.create_line(pt1.x , pt1.y , pt3.x , pt3.y , fill = "green" , width = 5)
                    line3 = c.create_line(pt3.x , pt3.y , pt2.x , pt2.y , fill = "green" , width = 5)
                    e["text"] = "Number of triangles : "+str(ans)                    
                    top.update()
                    time.sleep(1)
                    c.delete(line1)
                    c.delete(line2)
                    c.delete(line3)
                    
                #else:
                   # print("not triangle")
                    
                    
                    
    print("triangles : ",ans)
    messagebox.showinfo("Hurray!","We have counted "+str(ans)+" triangles till now")
def triangle(pt1 , pt2 , pt3):
    
    line_1 = Line(pt1, pt2)
    line_2 = Line(pt2, pt3)
    line_3 = Line(pt1, pt3)
    
    if search(line_1) and search(line_2) and search(line_3):
        if equals_line(line_1 , line_2) or equals_line(line_3 , line_2) or equals_line(line_1 , line_3):
            return False
        else:
            return True
    return False
    

def equals_line(line_1 , line_2):
    
    if (line_1.p1 == line_2.p1 and line_1.p2 == line_2.p2) or  (line_1.p1 == line_2.p2 and line_1.p2 == line_2.p1) :
        return True
    
    
    m1 = line_1.slope()
    m2 = line_2.slope()
    
    c1 = line_1.intercept()
    c2 = line_2.intercept()
    
    if comp_slope(m1 , m2) and abs(c1 - c2)<15:
        return True
    return False


def comp_slope(m1 , m2):
    md = abs(m1 - m2)
    p =  100*(md / (m1+10**-8))
    if p<1:
        return True
    return False

def distance(p1,p2):
    
    return (((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**(0.5))

def  bet(a,b,c):
    if a<=c<=b or b<=c<=a:
        return True
    return False

def intersects(line_1 , line_2):
    
    p1 = line_1.p1
    p2 = line_1.p2
    
    p3 = line_2.p1
    p4 = line_2.p2
    
    m1 = line_1.slope()
    m2 = line_2.slope()
    
    c1 = p1.y - m1*p1.x
    c2 = p3.y - m2*p3.x
    
    
    if abs(m1-m2)<0.5:
        print("Parallel points")
        return False
    
    x_ins = (c2 - c1)/(m1 - m2)
    y_ins = (m1*c2 - m2*c1)/(m1 - m2)
    
    if bet(p1.x , p2.x , x_ins) and bet(p3.x , p4.x , x_ins) and bet(p1.y , p2.y , y_ins) and bet(p3.y , p4.y , y_ins):
        new_point = Point(x_ins , y_ins)
        return new_point
    else:
        print("Intersection at external")
        return False
    
    
def get_point_closer_to_line(point):
    
    for line in lines:
        if distance_lp(point,line)<10:
            return near_point(point , line)
    return point

def near_point(point , line):
    
    
    m1 = line.slope()
    m2 = -1/m1
    c1 = line.intercept()
    c2 = (point.y - m2*point.x)
    x_ins = (c2 - c1)/(m1 - m2+10**-10)
    y_ins = (m1*c2 - m2*c1)/(m1 - m2+10**-10)    
    pt = Point(x_ins, y_ins)
    
    return pt

def distance_lp(point , line):
    m = line.slope()
    x = point.x
    y = point.y
    p1 = line.p1
    p2 = line.p2
    d1 = distance(p1, p2)
    d2 = distance(p1 , point)
    d3 = distance(p2, point)

    c = line.intercept()
    if d2**2 > d1**2 + d3**2:
        return 100
    if d3**2 > d1**2 + d2**2:
        return 100
    
    return abs((y - m*x - c) / ((1 + m**2)**(0.5)))
        
def new_point(event):

    global list_of_points,cur_event,start_point , lines
    
    x = event.x
    y = event.y
    
    cur_point = Point(x, y)
    
    print("Point clicked : " ,(x,y))
    
    # check whether new point or not
    tot_points = len(list_of_points)

    counter = 0
    for old_point in list_of_points:
        dist = distance(cur_point,old_point)
        counter += 1
        if dist <= 10:
            print("Point already choosen :distance = {} , point number {}".format(dist,counter))
            cur_point = old_point
            break
    else:
        print("New Point choosen !")
        cur_point = get_point_closer_to_line(cur_point)        
        # change current mode
        list_of_points.append(cur_point)
        # draw a circle around the point
        
        # check for nearby line 
        
        cur_point.draw()
        
    
    # change the current event ->  start / stop of the line
    
    if cur_event == "start":
        cur_event = "stop"
    else:
        cur_event = "start"
        
    if cur_event == "stop":
        if start_point.equals(cur_point):
            print("Same Point Cannot be choosen")
            cur_event = "start"
            return 
        new_line = Line(cur_point , start_point)
        new_line.draw()
        
        # draw a new line
        
        line_1 = new_line
        
        # check for intersection
        
        
        for line_2 in lines:
            
            if intersects(line_1 , line_2):
                pt = intersects(line_1 , line_2)
                
                # check for overlapping of existing points
                
                counter = 0
                for old_point in list_of_points:
                    dist = distance(pt,old_point)
                    counter += 1
                    if dist <= 10:
                        print("Point already choosen :distance = {} , point number {}".format(dist,counter))
                        break
                else:
                    print("New Point choosen !")
                    
                    list_of_points.append(pt)
                    pt.draw()
                
        
        lines.append(new_line)
        # store this new line
        
        
        
    else:
        
        #record the point
        start_point = cur_point
    
        
def debug():
    
    a,b = list(map(int,input("Enter points : ").split()))
    l = Line(list_of_points[a-1] , list_of_points[b-1])
    print("Search function : ",search(l))
    
    start_point = l.p1
    end_point = l.p2
    required_slope = l.slope()
    #print("__"*10)
    for search_line in lines:
        
        d1 = distance_lp(start_point , search_line) 
        d2 = distance_lp(end_point , search_line)
        p1 = search_line.p1
        p2 = search_line.p2
        i1 = list_of_points.index(p1)+1
        i2 = list_of_points.index(p2)+1
        print("Line: {} {} dist = {} {}" . format(i1,i2,d1,d2))
    
    

top = Tk()
top.title("Count Lines And Shapes")
top.geometry("1000x500")

c = Canvas(top , bg = "white" , height = 500 , width = 500)
c.bind("<Button-1>",new_point)
c.place(x = 0 , y = 0)

clear_button = Button(top,text = "CLEAR" , command = clear ,bg = "red",font = ('Arial' , 20 , "bold"))
clear_button.place(x = 600 , y = 250)

submit_button = Button(top,text = "SUBMIT" , command = submit , bg = "green" , font = ('Arial' , 20 , "bold"))
submit_button.place(x = 600 , y = 350)

e = Label(top , text = "Number of triangles : 0" , font = ('Arial' , 20 , "bold"))
e.place(x = 550 , y = 450)

Label(top , text = "Instructions:",font=("TimesNewRoman" , 20 , "bold")).place(x = 550 , y = 50)
Label(top , text = "1) Click on the canvas to draw a point").place(x = 550 , y = 100)
Label(top , text = "2) To draw a line , click on canvas to create another point").place(x = 550 , y = 150)
Label(top , text = "3) The 2 points which are recently selected form a line").place(x = 550 , y = 200)

top.mainloop()