from py_graphics import *
import math




x0 = float(input("Insert x0 ")) # 1st point x coordinate
y0 = float(input("Insert y0 ")) # 1st point y coordinate 
x1 = float(input("Insert x1 ")) # 2nd point x coordinate
y1 = float(input("Insert y1 ")) # 2nd point y coordinate 

win = GraphWin('DDA Algorithm', 640, 480)



def slop(x1,y1,x2,y2):
    return((y2-y1)/(x2-x1))


a1 = int(x0)
b1 = int(y0)
a2 = int(x1)
b2 = int(y1)


 

def dda(x1,y1,x2,y2):
    m = slop(x1,y1,x2,y2)

    if(abs(y2-y1)>abs(x2-x1)): # if m > 1 where m is slop ; y will incriment by 1 
        while  y1<y2:  
            x1 += 1/m          # x1 = x1+1/m 
            y1 +=1 
            pl = Point(x1,y1)
            pl.draw(win)
            tx1 = Text(Point(280,170)," m is > 1 so y will incriment by one  ")
            tx1.draw(win)
        
    elif(abs(x2-x1)-abs(y2-y1)): # if m < 1 where m is slop;  y will incriment by 1.
         while  x1<x2:
            y1 += 1/m            # y1 = y1 + 1/m 
            x1 +=1
            pl = Point(x1,y1)
            pl.draw(win)
            tx1 = Text(Point(360,260)," m is < 1 so x will incriment by one  ")
            tx1.draw(win)
           
        
    elif (abs(y2-y1) == abs(x2-x1) ): # if m = 1 both y and x will inncriment by 1
        while x1<x2 & y1<y2:
            x1+=1                #x1 = x1 + 1
            y1+=1                #y1 = y1 + 1
            pl = Point(x1,y1)
            pl.draw(win)
            tx1 = Text(Point(240,100)," m is = 1  both y and x will incriment by one  ")
            tx1.draw(win)





dda(a1,b1,a2,b2) 







# ln.draw(win)
# text.draw(win)



win.getMouse()
win.close()