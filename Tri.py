import colorsys
import turtle

turtle.title('Cool Triangle')

#Init py Graphics
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('Black')

t.penup()
t.goto(-200, -100)
t.pendown()
t.speed(10)

#Logic 
a = 400
h = 0
n = 100

def Triangle():
    global a, n, h
    for i in range(40):
        c = colorsys.hsv_to_rgb(h, 1, 0.6)
        h = h+(1/n)
        t.color(c)
        t.forward(a)
        t.left(120)
        a = a-10


Triangle()
Triangle()

t.hideturtle()
turtle.done()