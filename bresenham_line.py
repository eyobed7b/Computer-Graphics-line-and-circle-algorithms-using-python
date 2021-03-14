from py_graphics import *
import math

win = GraphWin('Bresenham Algortihm ', 640, 480)

def sign(a):   # sign function if the starting point is greater than the final point it will assign -1 and vis revers
    if a>0:
        ret = 1
    elif a<0:
        ret = -1
    else:
        ret = 0
    return ret


x0 =50   # starting point on x
y0 = 50   # starting point on y
x1 = 200    # end point on x
y1 = 200     # end point in y

x = x0
y = y0
dx = abs(x1-x)  # change in x 
dy = abs(y1-y)  # change in y
s1 = sign(x1-x0)
s2 = sign(y1-y0)
# ln = Line(Point(x0,y0),Point(x1,y1))

if dy>dx:  # if change in y > change in x  we will sweap 
    dx, dy = dy, dx
    interchange = True
else:
    interchange = False


e = 2*dy - dx      


for i in range(dx):
        pt = Point(x,y)
        pt.draw(win)
        while(e>=0):   
            if interchange:
                x = x +s1
                
            else:
                y = y + s2
                
            e = e - 2*dx

        if interchange:
            y = y + s2
            
        else:
            x = x + s1
            

        e = e + 2*dy
       


win.getMouse()
win.close()


