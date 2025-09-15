import turtle
from turtle import *
t = Turtle()
t.speed(5000)
t.shape('turtle')
def square(x,y):
    for i in range(99):
        for i in range(4):
            t.forward(x)
            t.left(90)
        t.left(y+4)
def spiralV1(x):
        for i in range(150):
            t.forward(x+i)
            t.left(88)
def spiralV2(x):
    t.left(180)
    for h in range(60):
         for i in range(4):
              t.left(90)
              t.forward(h*5)
         t.left(-5)
def spiralV3(x):
    for h in range(100):
         for i in range(5):
              t.forward(x+h*2)
              t.left(144)
         t.left(-5)
def Triple(x):
     t.forward(-x)
     for h in range(3):
          for i in range(3):
            t.forward(x)
            t.left(120)
          t.forward(x)
spiralV2(50)
turtle.done()