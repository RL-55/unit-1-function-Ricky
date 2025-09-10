import turtle
from turtle import *
t = Turtle()
t.speed(100)
t.shape('turtle')
def square(x,y):
    for i in range(99):
        for i in range(4):
            t.forward(x)
            t.left(90)
        t.left(y+4)
def spiral(x):
    for i in range(99):
        for i in range(4):
            t.forward(i+5)
            t.left(90)
        t.left(5)
spiral(1)
turtle.done()
