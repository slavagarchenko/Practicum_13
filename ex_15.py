import turtle
import random

turtle.setup(800, 600)
turtle.bgcolor("navy")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

t.penup()
t.goto(-400, -300)
t.pendown()
t.color("darkgreen")
t.goto(400, -300)

t.penup()
t.goto(0, -280)
t.pendown()
t.color("gray")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

t.color("white")
for _ in range(10):
    x = -400 + 800 * random.random()
    y = -250 + 550 * random.random()
    t.penup()
    t.goto(x, y)
    t.dot(2)

turtle.done()
