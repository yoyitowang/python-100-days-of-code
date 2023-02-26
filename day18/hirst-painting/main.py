###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import random
from turtle import Turtle, Screen

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

t = Turtle()
s = Screen()
s.colormode(255)
t.setheading(0)
t.pensize(10)
t.penup()
t.goto(-225, -225)

def draw_hirst_painting(n):
    gap = 50
    for i in range(1, n+1):
        t.penup()
        t.forward(gap)
        t.dot(30, tuple(random.choice(rgb_colors)))
        if i % 10 == 0:
            t.goto(-225, t.ycor()+gap)
    t.hideturtle()

draw_hirst_painting(100)
s.exitonclick()