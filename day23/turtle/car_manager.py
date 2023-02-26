from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE
        

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.penup()
        car.color(random.choices(COLORS))
        car.goto(300, random.randint(-260, 260))
        self.cars.append(car)

    def move(self):
        tmp = []
        for car in self.cars:
            car.backward(self.car_speed)
            if car.xcor() > -300.:                
                tmp.append(car)
            else:
                car.hideturtle()

        self.cars = tmp

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
