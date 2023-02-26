from turtle import Turtle, Screen
import random
import numpy as np

t = Turtle()
screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# # ----------------
# # Draw dashed line
# for _ in range(10):
#     t.forward(10)
#     pen = t.pen().get('pendown')
#     if pen:
#         t.penup()
#     else:
#         t.pendown()

# # ----------------
# # Draw different shapes
# def draw_shape(num_sides):
#     degree = 360 / num_sides
#     for _ in range(num_sides):
#         t.forward(100)
#         t.right(degree)

# for shape_side in range(3, 11):
#     draw_shape(shape_side)

# # ----------------
# # Random walk
# t.speed("fastest")
# direct = [0, 90, 270]
# for i in range(100):
#     t.color(tuple(np.random.randint(256, size=3)))
#     t.forward(30)
#     t.setheading(random.choice(direct))
#     t.pensize(i)

# Draw a spirograph
t.speed("fastest") 
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        t.circle(50)
        t.color(random_color())
        t.setheading(i*size_of_gap)

draw_spirograph(10)
screen.exitonclick()