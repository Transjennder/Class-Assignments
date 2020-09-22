# -*- coding: utf-8 -*-
"""
@author: Quintan Seyfert

Created on Tue Sep 22 14:29:16 2020

Title: 
"""

import turtle
import random


tt = turtle.Turtle()
sc = turtle.Screen()

tt.speed(0)

def rSquare():
    
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    side = random.randint(20,200)

    aSquare(x,y,side)
    

def aSquare(x, y , length):
    turtle.clear()

    tt.penup()
    tt.setx(x)
    tt.sety(y)
    tt.pendown()
    
    # value between 0 and 1
    # sc.colormode(1)
    # value between 0 and 255
    sc.colormode(255)

    tt.color("red")
    #tt.fillcolor("blue")
    tt.fillcolor(random.randint(0,255),
random.randint(0,255),
random.randint(0,255))

    tt.begin_fill()

    for cntr in range(4):

        tt.forward(length)
        tt.right(90)
        # getPos()

    tt.end_fill()

    tt.pu()



def getPos():

    x = turtle.xcor()
    y = turtle.ycor()

    print(str(x) + ", " + str(y))


def recursiveSquares(x,y, shrink):

    tt.speed(0)

    if  x > -10:
        return

    tt.penup()
    tt.setx(x)
    tt.sety(y)
    tt.pd()

    side = 2 * abs(x)

    for c in range(4):
        tt.forward(side)
        tt.right(90)

    recursiveSquares(x + shrink, y - shrink, shrink)



def main():
    
    ans = "n"

    while ans != "y":

        """
        xpos = int(turtle.numinput("X position", "Enter x coord"))
        ypos = int(turtle.numinput("Y position", "Enter y coord"))
        sidelen = int(turtle.numinput("Side Length", "Enter side length"))

        aSquare(xpos, ypos, sidelen)
        """        

        for c in range(random.randint(2,10)):
            
            rSquare()



        # recursiveSquares(-300, 300, 30)


        ans = turtle.textinput("Quit", "Quit y or n").lower()


    turtle.done() 
    turtle.bye()

    
main()


"""
review recursive square

circles
stars

spirals


- Basic animation


"""


