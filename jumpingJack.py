# Name: J. Carter Haley, 20 November 2016
# jumpingJack.py

#Problem: This program will animate a series of line objects to simulate
#jumping jacks. The program will use buttons to allow the user 

#Certification of Authority:
    #I certify that this lab is entirely my own work.


# button determines where the user clicked in relation to
# the button.  The last portion creates a quit button.  This requires a
# while loop to exit only when the user clicks the button.

from graphics import *
import time


def wasClicked(pt, rect):
    #This function gets points pf a rectangle
    rectP1X = rect.getP1().getX()
    rectP1Y = rect.getP1().getY()
    rectP2X = rect.getP2().getX()
    rectP2Y = rect.getP2().getY()

    #These two lines get the (X,Y) values of the user's click
    ptX = pt.getX()
    ptY = pt.getY()
    click = False

    #It uses these points to determine if the user's click falls
    #in the rectangle.
    if (ptX >= rectP1X and ptX <= rectP2X) and (ptY >= rectP1Y and ptY <= rectP2Y):
        click = True
    return click
    

def jumpingJack():
    # Creates a graphic window named, 'Jumping Jack'
    winWidth = 500
    winHeight = 500
    win = GraphWin("Jumping Jack", winWidth, winHeight)

    # Creates a 'Start', 'Stop', and 'Quit'
    startButtonText = Text(Point(125, 425), "Start").draw(win)
    Rectangle(Point(100, 400), Point(150, 450)).draw(win)

    stopButtonText = Text(Point(200, 425), "Stop").draw(win)
    Rectangle(Point(175, 400), Point(225, 450)).draw(win)

    quitButtonText = Text(Point(275, 425), "Quit").draw(win)
    Rectangle(Point(250, 400), Point(300, 450)).draw(win)

    # Creates a text object with instructions for the user   
    instructions= Text(Point(250, 490), "Click Start to make Jack jump, Or click Quit to Close").draw(win)

    # Creates the head of the Jumping Jack
    jackHead = Circle(Point(250, 50), 20)
    jackHead.draw(win)

    # Creates the arms of the Jumping Jack (U: Upper, D: Lower)     
    arm1U = Line(Point(250,120),Point(300,100))
    arm1D = Line(Point(250,120),Point(300,150))

    arm2U = Line(Point(250,120),Point(200,100))
    arm2D = Line(Point(250,120),Point(200,150))

    # Creates the legs of the Jumping Jack
    leg1U = Line(Point(250,200),Point(200,250))
    leg1D = Line(Point(250,200),Point(250,250))

    leg2U = Line(Point(250,200),Point(300,250))
    leg2D = Line(Point(250,200),Point(250,250))

    # Creates the chest of the Jumping Jack
    jackChest = Line(Point(250,70),Point(250,200))
    jackChest.draw(win)
    
    #Draws the arms of the Jumping Jack
    arm1U.draw(win)
    arm2U.draw(win)

    #Draws the legs of the Jumping Jack
    leg1U.draw(win)
    leg2U.draw(win)

    pt = win.getMouse()

    # The next 3 lines use the wasClicked function to determine
    #if each box is clicked
    start = wasClicked(pt, Rectangle(Point(100, 400), Point(150, 450)))
    stop = wasClicked(pt, Rectangle(Point(175, 400), Point(225, 450)))
    quit1 = wasClicked(pt, Rectangle(Point(250, 400), Point(300, 450)))

    click = win.checkMouse()

    #This while loop starts the jumping Jacks by undrawing, moving,
    #then drawing different points of the Jack's arms
    while click == None:
        
        if start == True:
            arm1U.undraw()
            arm2U.undraw()
            leg1U.undraw()
            leg2U.undraw()
            
            arm1D.draw(win)
            arm2D.draw(win)

            leg1D.draw(win)
            leg2D.draw(win)

            time.sleep(.3)

            arm1D.undraw()
            arm2D.undraw()

            leg1D.undraw()
            leg2D.undraw()
            
            arm1U.draw(win)
            arm2U.draw(win)

            leg1U.draw(win)
            leg2U.draw(win)
            time.sleep(.3)
            click = win.checkMouse()

        #This statement should stop the jumping
        #Jacks when the stop button is clicked
        if stop == True:

            arm1U.undraw() 
            arm2U.undraw() 

            leg1U.undraw()
            leg2U.undraw()

            arm1U.draw(win) 
            arm2U.draw(win)

            leg1U.draw(win)
            leg2U.draw(win)
            win.getMouse()

            click = win.checkMouse()
            
        #This statement closes the window, if Quit is clicked.
        elif quit1 == True:
            win.close()
    
            
jumpingJack()
