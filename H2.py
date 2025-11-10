#Kristo Varul
#10.11.2025

from turtle import *
aken = Screen()
aken.setup(width=500, height=400)
speed(0)
penup()
#Sinine
goto(-110,0)
pendown()
pensize(6)
pencolor("Blue")
circle(50)
#must
penup()
goto(0,0)
pendown()
pencolor("black")
circle(50)
#punane
penup()
goto(110,0)
pendown()
pencolor("red")
circle(50)
#kollane
penup()
goto(-55,-55)
pendown()
pencolor("yellow")
circle(50)
#roheline
penup()
goto(55,-55)
pendown()
pencolor("green")
circle(50)

turtle.done()
