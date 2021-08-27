import turtle
from turtle import *

window = turtle.Screen()
window.bgcolor("#363636")
flw = turtle.Turtle()
flw.speed(14)

def shape(size,side):
 for i in range(side):
     flw.forward(size)
     flw.left(360/side)

def draw_petal(turtle, radius):
    heading = turtle.heading()
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.setheading(heading)


flw.up()
flw.goto(0,-300)
flw.down()
flw.color('orange')
flw.begin_fill()
flw.circle(300)
flw.end_fill()


flw.goto(0,-280)
flw.color('#FFD700')
flw.begin_fill()
flw.circle(280)
flw.end_fill()


flw.goto(0,-260)
flw.color('#FFFFE0')
flw.begin_fill()
flw.circle(260)
flw.end_fill()

flw.goto(0,-240)
flw.color('#006400')
flw.begin_fill()
flw.circle(240)
flw.end_fill()

flw.up()
flw.goto(0,5)
flw.down()



for j in range(45):
    flw.color("#660000")
    flw.begin_fill()
    shape(160,4)
    flw.left(8)
    flw.end_fill()

for k in range(36):
    flw.color("#EEE8AA")
    flw.begin_fill()
    shape(140,4)
    flw.left(10)
    flw.end_fill()

for n in range(36):
    flw.color("#FF8C00")
    flw.begin_fill()
    shape(130,4)
    flw.left(10)
    flw.end_fill()

flw.goto(0,-150)
flw.color("#FFD700")
flw.begin_fill()
flw.circle(150)
flw.end_fill()


my_radius = int(150)
my_petals = int(16)
bob = Turtle()
bob.speed(30)
bob.color("#FFFFE0")
bob.begin_fill()
for _ in range(my_petals):
    draw_petal(bob, my_radius)
    bob.left(360 / my_petals)
bob.hideturtle()
bob.end_fill()


flw.goto(0,-80)
flw.color("#800000")
flw.begin_fill()
flw.circle(80)
flw.end_fill()


bob.color("orange")
bob.begin_fill()
my_radius = int(80)
my_petals = int(18)
bob = Turtle()
bob.speed(20)
bob.color("orange")
bob.begin_fill()
for _ in range(my_petals):
    draw_petal(bob, my_radius)
    bob.left(360 / my_petals)
bob.hideturtle()
bob.end_fill()


flw.goto(0,-50)
flw.color("#FFD700")
flw.begin_fill()
flw.circle(50)
flw.end_fill()


flw.goto(0,-40)
flw.color("#006400")
flw.begin_fill()
flw.circle(40)
flw.end_fill()


flw.goto(0,-30)
flw.color("#FFF8DC")
flw.begin_fill()
flw.circle(30)
flw.end_fill()


flw.goto(0,-20)
flw.color("#FFF8DC")
flw.begin_fill()
flw.circle(20)
flw.end_fill()

bob.color("#660000")
bob.begin_fill()
my_radius = int(30)
my_petals = int(14)
for _ in range(my_petals):
    draw_petal(bob, my_radius)
    bob.left(360 / my_petals)
bob.end_fill()


flw.goto(0,-10)
flw.color("#FFF8DC")
flw.begin_fill()
flw.circle(10)
flw.end_fill()
flw.hideturtle()

screen = Screen()
screen.exitonclick()
turtle.done()

