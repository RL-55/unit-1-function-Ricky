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
def spiralV1(x):
        for i in range(120):
            t.forward(x+i)
            t.left(89)
def spiralV2(x):
    for h in range(80):
         for i in range(4):
              t.forward(x+h)
              t.left(90)
         t.left(5)
spiralV2(50)
turtle.done()
