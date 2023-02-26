from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def refresh(self):
        self.score += 1
        self.clear()
        self.update()
    
    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGN, font=FONT)
        