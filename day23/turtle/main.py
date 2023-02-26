import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

difficulty = screen.textinput("Difficulty: ", "Normal=0, Hard=1, Expert=2:")
screen.listen()
screen.onkey(player.left, 'Left')
screen.onkey(player.right, 'Right')
screen.onkey(player.up, 'Up')

game_is_on = True
counter = 0
while game_is_on:
    counter += 1
    time.sleep(0.1)
    screen.update()
    carManager.move()
    if counter % 6 == 0:
        carManager.create_car()

    for car in carManager.cars:
        if car.distance(player) < 20.:
            game_is_on = False
            scoreboard.game_over()
    
    if player.finish_line():
        carManager.speed_up()
        player.reset_pos()
        scoreboard.level_up()