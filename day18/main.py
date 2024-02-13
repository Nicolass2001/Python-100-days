import turtle as t
import random as r
import colorgram


timmy = t.Turtle()
timmy.shape('turtle')
t.colormode(255)

colors = colorgram.extract('spots.jpg', 20)
print(colors[0].rgb)

t.screensize(500,500)

t.setworldcoordinates(-10, -10, 100, 100)

timmy.speed(0)
timmy.hideturtle()

for x in range(0, 10):
    for y in range(0, 10):
        timmy.penup()
        timmy.setpos(x*10, y*10)
        timmy.pendown()
        timmy.dot(20, colors[r.randint(0, 19)].rgb)

timmy.penup()
timmy.setpos(-10, -10)

# for x in range(4):
#     timmy.rt(90)
#     timmy.fd(100)

# for x in range(15):
#     timmy.fd(10)
#     timmy.pu()
#     timmy.fd(10)
#     timmy.pd()

# for x in range(3, 10):
#     timmy.color(r.random(), r.random(), r.random())
#     for y in range(x):
#         timmy.rt(360/x)
#         timmy.fd(100)

# timmy.speed(10)
# timmy.pensize(8)

# while True:
#     timmy.rt(90*r.randint(0,3))
#     timmy.fd(20)
#     timmy.color(r.random(), r.random(), r.random())



t.exitonclick()