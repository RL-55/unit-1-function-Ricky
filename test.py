import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
def triangle(x):
    t.forward(x)
    t.left(90)
    t.forward(x+25)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x+25)
triangle(100)
turtle.done()
