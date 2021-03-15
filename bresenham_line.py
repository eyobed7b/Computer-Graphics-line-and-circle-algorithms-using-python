from py_graphics import *
import math

x0 = float(input("Insert x0 ")) # 1st point x coordinate
y0 = float(input("Insert y0 ")) # 1st point y coordinate 
x1 = float(input("Insert x1 ")) # 2nd point x coordinate
y1 = float(input("Insert y1 ")) # 2nd point y coordinate 

win = GraphWin('Bresenham line Algortihm ', 640, 480)


def sign(a):   # sign function if the starting point is greater than the final point it will assign -1 and vis revers
    if a>0:
        ret = 1
    elif a<0:
        ret = -1
    else:
        ret = 0
    return ret




x = int(x0)
y = int(y0)
dx = int(abs(x1-x))  # change in x 
dy = int(abs(y1-y))  # change in y
s1 = sign(x1-x0)
s2 = sign(y1-y0)
# ln = Line(Point(x0,y0),Point(x1,y1))
txt = Text(Point(abs(x1+100),abs(y0-y1))," Point 1 =  ("+ str(x0)+','+str(y0)+")"+" \n Point 2 = ("+str(x1)+","+str(y1)+" \n The slop is "+str(dy/dx))
txt.draw(win)
if dy>dx:  # if change in y > change in x  we will sweap 
    dx, dy = dy, dx
    interchange = True
else:
    interchange = False


e = 2*dy - dx    # decision parameter for initial    


for i in range(dx):    # for all x value use used x valus if the m > 1 we will sweap and make the y valu to x and do the loop
        pt = Point(x,y)
        pt.draw(win)
        while(e>=0):   # if the next desision parameter is >= 0 we will chose we will chose the lower point so x will incremment by unite
            if interchange:
                x = x +s1
                
            else:       # else we will choose the upper point the y will increment by unite
                y = y + s2
                
            e = e - 2*dx # the next point  decsion maker paramenter using the x value

        if interchange: # if change in y is greater or m >1  we will increment the y value by unite 
            y = y + s2
            
        else:
            x = x + s1
            

        e = e + 2*dy  # the next point  decsion maker paramenter using the y value
       


win.getMouse()
win.close()


