from py_graphics import *
import math

win = GraphWin('DDA Algorithm', 640, 480)
 

 

def Scanne_convert(x1,y1,x2,y2):

    dx = x2-x1  # change in x
    dy = y2-y1   # change in y 

    m = dy/dx   # slop
    b = y1 - (m*x1)  # y intercept
    tB = Text(Point(400,30),'[.] String point ('+str(x1)+','+str(y1)+')')
    tB.draw(win)
 
    tB = Text(Point(400,50),'[.]  end point ('+str(x2)+','+str(y2)+')')
    tB.draw(win)
 
    tB = Text(Point(368,70),'[.]  Slop = '+str(m))
    tB.draw(win)
 
    tB = Text(Point(390,90),'[.]  Y intercep = '+str(b))
    tB.draw(win)

    if dx<0:  # x2 is < x1 we will make x1 end point and x2 starting point

        x=x2
        y=y2
        xe = x1  # x1 is end point 
    else :
        x = x1 
        y = y1
        xe = x2    # x2 is end point 

    while x<xe :   # from starting point up to the end point 
        p = Point(x,y) 
        p.draw(win)
        x+=1   # x++
        y=m*x + b  # finding the y value 

x1 = 100
y1 = 20
x2 = 250
y2 = 140



Scanne_convert(x1,y1,x2,y2)




win.getMouse()
win.close()