#05.01.2025
#Kristo Varul
import turtle
import math

def draw_square(size):
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

def move(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

turtle.speed(0)
turtle.pensize(2)
turtle.pencolor("black")
turtle.fillcolor("white")
s = 30

move(0, s)
draw_square(s)

move(-2*s, 0)
draw_square(s)

move(-s, -2*s)
draw_square(s)

move(s, -s)
draw_square(s)

turtle.hideturtle()
turtle.done()
