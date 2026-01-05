#02.01.2025
#Kristo Varul

import turtle
import math

t = turtle.Turtle()
t.speed(0)
side = 100

t.penup()
t.goto(-side/2, -side*math.sqrt(3)/2)
t.setheading(0)
t.pendown()

for _ in range(6):
    t.forward(side)
    t.left(60)

t.penup()
t.goto(0, 0)
t.setheading(0)
t.pendown()

for _ in range(6):
    t.forward(side)
    t.backward(side)
    t.left(60)

turtle.done()
