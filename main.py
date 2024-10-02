import turtle
import random

wn=turtle.Screen().bgcolor("orange")
t=turtle.Turtle()
t.pensize(2)

def pdraw():
 t.right(90)
 for _ in range(90):
    t.forward(1)
    t.right(2)
def idraw():
    t.forward(20)
    t.backward(10)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(10)
    t.backward(20)


t.penup()
t.goto(-500,0)
t.pendown()
t.left(90)
t.forward(100)
t.goto(-500,0)
t.penup()
t.right(90)
t.forward(70)
t.pendown()
t.left(90)
t.forward(100)
t.backward(50) #h
t.left(90)
t.forward(70)

t.penup()
t.goto(-400,0)
t.pendown()
t.left(250)
t.forward(110) #a
t.right(140)
t.forward(110)
t.penup()
t.goto(-385,40)
t.pendown()
t.left(70)
t.forward(45)

t.penup()
t.goto(-300,0)
t.pendown()
t.left(90)
t.forward(100)
pdraw()
t.penup()
t.goto(-250,0)
t.pendown()
t.right(90)
t.forward(100)
pdraw()
t.penup()
t.goto(-180,0)
t.pendown()
t.right(90)
t.forward(60)
t.left(45)
t.forward(50)
t.backward(50)
t.right(90)
t.forward(50)
t.penup() 

t.goto(-50,0) #H letter
t.pendown()
t.left(45)
t.forward(100)
t.goto(-50,0)
t.penup()
t.right(90)
t.forward(70)
t.pendown()
t.left(90)
t.forward(100)
t.backward(50) #h
t.left(90)
t.forward(70) 

t.penup()
t.goto(90,90)
t.pendown()
t.right(180)
for _ in range(180):
    t.forward(1.7)
    t.right(2)

t.penup()
t.goto(160,100)
t.pendown()
t.right(90)
t.forward(100)
t.left(90)
t.forward(70)

t.penup()
t.goto(260,100)
t.pendown()
t.forward(40)
t.backward(20)
t.right(90)
t.forward(100)
t.left(90)
t.forward(20)
t.backward(40)


t=turtle.Turtle()

def pen(colour):
    t.color(colour)

def fireworks(distance):
    for _ in range(20):
        t.forward(distance)
        t.right(180-(360/20))

def move():
    t.penup()
    x=random.randint(-700,700)
    y=random.randint(-700,700)
    t.goto(x,y)
    t.pendown()

t.speed(0)
colors = ['red','purple','green','blue','orange','yellow','cyan']
for i in range(30):
    color=random.choice(colors)
    pen(color)
    fireworks(random.randint(50,100))
    move()
turtle.done()