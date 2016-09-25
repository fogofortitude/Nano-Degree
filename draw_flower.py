import turtle
import math


def draw_line():
    george = turtle.Turtle()
    george.color("brown")
    george.setpos((47,43))
    #george.pendown()
    george.width(4)
    george.right(90)
    george.forward(200)

def draw_leaf():
    george = turtle.Turtle()
    george.color("green")
    george.setpos((47,-100))
    george.width(3)
    drawFlower(george, 1, 30, 110)


def drawArc(myTurtle, radius, angle):
    arc_length = 2 * math.pi * radius * abs(angle) / 360
    sides = int(arc_length / 4) + 1
    step_length = arc_length / sides
    step_angle = angle / sides

    for side in range(sides):
        myTurtle.forward(step_length)
        myTurtle.left(step_angle)

def drawPetal(myTurtle, radius, angle):
    drawArc(myTurtle, radius, angle)
    myTurtle.left(180-angle)
    drawArc(myTurtle, radius, angle)
    myTurtle.left(180-angle)

def drawFlower(myTurtle, petals, radius, angle):
    for petal in range(petals):
        drawPetal(myTurtle, radius, angle)
        myTurtle.left( 360 / petals )

def drawRandomFlower(myTurtle):
    petals = 24
    radius = 40
    angle = 120
    color = 'orange'
    shape = 'turtle'
    speed = 'fastest'


    # Set new color
    draw_line()
    draw_leaf()
    myTurtle.color(color)
    myTurtle.shape(shape)
    myTurtle.speed(speed)
    drawFlower(myTurtle, petals, radius, angle)
    window.exitonclick()



window = turtle.Screen()
window.bgcolor("black")
george = turtle.Turtle()

# used to generate the number of flowers on the screen.
for i in range(1):
    drawRandomFlower(george)
