
# import PIL.Image, PIL.ImageDraw
from py_graphics import *
# import math
win = GraphWin('Bresenham Circle  Algortihm ', 800, 800)
xs = 100 
ys = 100

def circle(radius):
    "Bresenham complete circle algorithm in Python"
    # init vars
    p = 3 - (2 * radius)
    points = set()
    x = 100
    y =  radius
    # first quarter/octant starts clockwise at 12 o'clock
    while x <= y:
        # first quarter first octant
        points.add((x,y))
        pt = Point(x,y)
        pt.setOutline(color="red")
        pt.draw(win)
       
        # first quarter 2nd octant
        points.add((y,x))
        pt1 = Point(y,x)
        pt1.setOutline(color="red")
        pt1.draw(win)
        # second quarter 3rd octant
        points.add((y,x))
        pt2 = Point(y,x)
        pt2.setOutline(color="red")
        pt2.draw(win)
        # second quarter 4.octant
        points.add((xs+x,y))
        pt3 = Point(xs+x,y)
        pt3.setOutline(color="blue")
        pt3.draw(win)
        # third quarter 5.octant
        points.add((x,y))
        pt4 = Point(x,y)
        pt4.draw(win)        
       # third quarter 6.octant
        points.add((-y,x))
        pt5 = Point(ys-y,xs+x)
        pt5.draw(win)
        # fourth quarter 7.octant
        points.add((-y,-x))
        pt6 = Point(ys-y,x)
        pt6.draw(win)
        # fourth quarter 8.octant

        points.add((-x,-y))
        pt7 = Point(x,ys-y)
        pt7.draw(win)

        if p < 0:
            p = p + (4 * x) + 6
        else:
            p = p + (4 * (x - y)) + 10
            y = y - 1
        x = x + 1
 
    return points


radius = 200

p = circle(radius)

win.getMouse()
win.close()

