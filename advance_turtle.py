import turtle as t

#Draw a square
tim = t.Turtle()
tim.shape("turtle")
tim.color("purple")
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)

#Draw a hash line
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()