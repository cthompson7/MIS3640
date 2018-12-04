import turtle

jack =turtle.Turtle()

# jack.fd(100)
# jack.lt(90)
# jack.fd(100)
# jack.lt(90)
# jack.fd(100)
# jack.lt(90)
# jack.fd(100)
#
# turtle.mainloop()

# for i in range(4):
#     print('Hello!')
#     print("world")

# Exercise 2.1
# def square(t):
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)
#
# square(jack)
# turtle.mainloop()

# def spiral(t):
#     for i in range(360):
#         square(t)
#         t.rt(1)
#
# spiral(jack)
# turtle.mainloop()
# Exercise 2.2
# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)
#
# square(jack, 1000)
# turtle.mainloop()

# Exercise 2.3
# def polygon(t, length, n):
#     for i in range(n):
#         t.fd(length)
#         t.lt(360/n)
#
# polygon(jack, 100, 6)
# turtle.mainloop()

# Exercise 2.4
# import math

# def circle(t, r):
#     circumference = 2 * math.pi * r
#     n = int(circumference/3) + 1
#     length = circumference / n
#     polygon(t, length, n)
#
# circle(jack, 100)
# turtle.mainloop()

# Exercise 2.5
# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = angle / n
#
#     for i in range(n):
#         t.fd(step_length)
#         t.lt(step_angle)

# def polyline(t, n, length, angle):
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)
#
# def polygon(t, n, length):
#     angle = 360.0 / n
#     polyline(t, n, length, angle)

# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = float(angle) / n
#     polyline(t, n, step_length, step_angle)

# polyline(jack, 3, 100, 30)
# turtle.mainloop()

# def circle(t, r):
#     arc(t, r, 360)
#
# circle(jack, 100)
# turtle.mainloop()

# Exercise #3
# 1. Write an appropriately general set of functions that can draw shapes as below. The third one shape is optional.
def draw_flower(turtle):
    for i in range(6):
        turtle.circle(100, 60)
        turtle.left(120)
        turtle.circle(100, 60)
        turtle.left(60)

    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()
    turtle.circle(100)

# draw_flower(jack)
# turtle.mainloop()

def draw_yinYang(turtle):
    turtle.width(3)
    turtle.left(180)
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.circle(50, 180)

    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.circle(50, 180)

    turtle.penup()
    turtle.goto(0, 75)
    turtle.pendown()
    turtle.circle(15)
    turtle.penup()

    turtle.goto(0, 175)
    turtle.pendown()
    turtle.circle(15)
    turtle.penup()

    turtle.goto(0,200)
    turtle.pendown()
    turtle.circle(100)

# draw_yinYang(jack)
# turtle.mainloop()
