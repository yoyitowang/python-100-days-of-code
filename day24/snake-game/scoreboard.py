from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 20, 'normal')
RECORD = 'records.txt'

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.load_highest_score()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highest_score}", align=ALIGN, font=FONT)

    def refresh(self):
        self.score += 1
        self.update()
    
    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open(RECORD, 'w') as f:
                f.write(f'{self.highest_score}')
        self.score = 0
        self.update()
    
    def load_highest_score(self):
        try:
            with open(RECORD, 'r') as f:
                self.highest_score = eval(f.read())
        except:
            self.highest_score = 0