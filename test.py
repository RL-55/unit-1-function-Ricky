import turtle
from turtle import *
t = Turtle()
t.speed(20)
t.shape('turtle')
def square(x,y):
    for i in range(99):
        for i in range(4):
            t.forward(x)
            t.left(90)
        t.left(y+4)
def spiralV2(x):
    t.left(180)
    for h in range(60):
         for i in range(4):
              t.left(90)
              t.forward(h*5)
         t.left(-5)
def spiralV3(x):
    t.left(320)
    for h in range(60):
         for i in range(5):
              t.forward(x+h*5)
              t.left(144)
         t.left(-5)
spiralV3(100)
turtle.done()