from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
steps = 10
angle = 10

def move_forward():
    t.forward(steps)

def move_backward():
    t.backward(steps)

def move_left():
    t.left(angle)

def move_right():
    t.right(angle)

def reset():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(move_left, 'a')
screen.onkey(move_right, 'd')
screen.onkey(reset, 'c')
screen.exitonclick()