from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)

user = screen.textinput("Turtle Racing", "Which color will win the game?")

turtle_list = []
colors = ["red", "orange", "blue", "black", "pink", "green"]
y = [-100, -60, -20, 20, 60, 100]
game_on = True

def init_turtle():
    for i in range(6):
        t = Turtle(shape="turtle")
        t.penup()
        t.color(colors[i])
        t.goto(-240, y=y[i])
        turtle_list.append(t)

def start_racing():
    global game_on
    while game_on:
        for t in turtle_list:
            t.forward(random.randint(1, 20))
            if t.xcor() > 240:
                game_on = False
                if user == t.pencolor():
                    print('You win!')
                else:
                    print('You lose!')
        

init_turtle()
start_racing()
screen.exitonclick()