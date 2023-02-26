from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
snake = Snake()
food = Food()
scorebaord = ScoreBoard()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_on = True

def game_over():
    global game_on
    game_on = False
    scorebaord.gameover()

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food.pos()) < 15.:
        food.refresh()
        scorebaord.refresh()
        snake.extend()
    
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10.:
            game_over()


screen.exitonclick()