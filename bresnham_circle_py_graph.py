

from py_graphics import *

xs = (float(input("Enter X coordinate of the circle \n: ")))   # x coordinate input from the user
ys = (float(input("Enter Y coordinate of the circle \n: ")))   # y coordinate input from the user
radius  = (float(input("Enter the radius of the cicle ")))
win = GraphWin('Bresenham Circle  Algortihm ', 800, 800)


def circle(radius):
    "Bresenham complete circle algorithm in Python"
    # init vars
    p = 3 - (2 * radius) # decision parameter of the initial point
   
    x = 0
    y =  radius
    # first ysuarter/octant starts clockwise at 12 o'clock
    while x <= y:  # when x = with y mean as x increse y will decrese
        # first ysuarter first octant
        pt1 = Point(x + xs, y + ys)       # first quarter 1st octant
        pt1.setOutline(color="green")     
        pt1.draw(win)                   

        pt2 = Point(x + xs, -y + ys)      # first quarter 2nd octant
        pt2.setOutline(color="yellow")
        pt2.draw(win)                    

        pt3 = Point(-x + xs, -y + ys)     # ssecond quarter 3rd octanta
        pt3.setOutline(color="red")
        pt3.draw(win)                

        pt4 = Point(-x + xs, y + ys)      # second quarter 4.octant
        pt4.setOutline(color="blue")
        pt4.draw(win)                   

        pt5 = Point(y + xs, x + ys)        #  third quarter 5.octant
        pt5.setOutline(color="black")
        pt5.draw(win)    

        pt6 = Point(y + xs, -x + ys)      # third quarter 6.octant
        pt6.setOutline(color="green")
        pt6.draw(win)                    

        pt7 = Point(-y + xs, -x + ys)       # fourth quarter 7.octant
        pt7.setOutline(color="yellow")
        pt7.draw(win)                    

        pt8 = Point(-y + xs, x + ys)       # fourth quarter 7.octant
        pt8.setOutline(color="red")
        pt8.draw(win)
  

        if p <= 0:
            p = p + (4 * x) + 6
            x=x+1
        else:
            p = p + (4 * (x - y)) + 10
            y = y - 1
            x = x + 1
 
txt = Text(Point(xs+radius,ys+radius+20),"The circle  radius is "+str(radius)) # text which tells the radius in GUI 
txt.draw(win)

circle(radius)




win.getMouse()
win.close()

