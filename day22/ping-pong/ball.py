from turtle import Turtle
import random

MOVE = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = self.y_move = MOVE
    
    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self, x=False, y=False):
        if x:
            self.x_move *= -1 
        if y:
            self.y_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce(x=random.choices([True, False]), y=random.choices([True, False]))