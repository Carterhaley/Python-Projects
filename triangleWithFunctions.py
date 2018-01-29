# Name: J. Carter Haley,  25 October 2016
# triangleWithFunctions.py

##Problem: Modify this program so that it uses a function,
##makeTriangle(p1, p2, p3), to create the triangle. That is, the three
##points are passed to the function, and it returns a Triangle object.
##Make the colors whatever you like. Draw the triangle that the function
##returns in main().


#Certification of Authority:
    #I certify that this lab is entirely my own work.

from graphics import *
import math

"""
makeTriangle(p1, p2, p3), to create the triangle. That is, the three
points are passed to the function, and it returns a Triangle object.
Make the colors whatever you like. Draw the triangle that the function
returns in main().
"""

#The following function accepts three points as parameters
def makeTriangle(p1,p2,p3):
##The following lines set up the graphic window
##    winWidth = 500
##    winHeight= 500
##    win = GraphWin("Triangle", winWidth, winHeight)
    
##The next several lines draw the triangle polygon object
    triangle = Polygon(p1,p2, p3)
    triangle.setFill("blue")
##    triangle.draw(win)
    
##    tri = Polygon(p1, p2, p3)
    return triangle

"""
Write a function, distance(p1, p2), that is passed two points and that
returns the Euclidean distance between the points.

"""

def distance(p1,p2):
##These lines get the X &Y coordinates from the first point 
    p1X= p1.getX()
    p1Y=p1.getY()

##These lines get the X &Y coordinates from the second point 
    p2X=p2.getX()
    p2Y=p2.getY()

##this formula calculates the distance between points
    distance = math.sqrt(((p1X-p2X)**2 +(p1Y-p2Y)**2))

    return distance

def perimeter(triangle):
##    winWidth = 500
##    winHeight= 500
##    win = GraphWin("Triangle", winWidth, winHeight)
##    triangle.setFill("blue")
##    triangle.draw(win)
    
##creates a list of point, which when indexed, can be used to find the
##length of each side
    pointList = triangle.getPoints()

##Indexing the list pointList, and summing the results calculates
##the length of each side
    sideA = distance(pointList[0], pointList[1])
    sideB = distance(pointList[1], pointList[2])
    sideC = distance(pointList[2], pointList[0])

    return sideA
    return sideB
    return sideC

    perimeter = sideA + sideB + sideC

    return perimeter
    
def area(triangle):
    pointList = triangle.getPoints()

    sideA = distance(pointList[0], pointList[1])
    sideB = distance(pointList[1], pointList[2])
    sideC = distance(pointList[2], pointList[0])
    perimeter = sideA + sideB + sideC
    
##Heron's formula for area of a triangle
    p = float(perimeter/2)
    area = math.sqrt(p*(p-sideA)*(p-sideB)*(p-sideC))

    return area

##The following main() tests the work above

def main():
    winWidth = 500
    winHeight= 500
    win = GraphWin("Triangle", winWidth, winHeight)
    win.getMouse()
    tri = makeTriangle(win.getMouse(), win.getMouse(), win.getMouse())

    tri.draw(win)

    instruct = Text(Point(winWidth/2, winHeight-10), "")
    instruct.setText("area: " + str(area(tri)) + " Perimeter: " + str(perimeter(tri)))
    instruct.draw(win)
    time.sleep(5)
    instruct.setText("Close Window.")
    instruct.draw(win)
    win.close()
main()
