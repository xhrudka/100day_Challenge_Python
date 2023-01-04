import turtle as t
import random

tim = t.Turtle()

colors = ["medium aquamarine", "DeepSkyBlue", "DarkOrchid"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed(10)

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))