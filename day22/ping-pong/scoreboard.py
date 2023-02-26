from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 50, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()
        
    def update(self):
        self.clear()
        self.goto(-50, 220)
        self.write(f"{self.l_score}", align=ALIGN, font=FONT)
        self.goto(50, 220)
        self.write(f"{self.r_score}", align=ALIGN, font=FONT)
    
    def l_point(self):
        self.l_score += 1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()