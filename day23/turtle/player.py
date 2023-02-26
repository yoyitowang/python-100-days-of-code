from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.reset_pos()

    def left(self):
        self.goto(self.xcor()-MOVE_DISTANCE, self.ycor())

    def right(self):
        self.goto(self.xcor()+MOVE_DISTANCE, self.ycor())

    def up(self):
        self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def finish_line(self):
        return self.ycor() >= FINISH_LINE_Y

    def reset_pos(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)