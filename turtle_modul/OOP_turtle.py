# Graphic module for Python
import turtle

# A new object, created from Turtle
from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("purple")
timmy.forward(50)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()