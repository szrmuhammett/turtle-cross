import random
from turtle import Turtle
from random import Random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.CARS=[]
        self.car_distance = STARTING_MOVE_DISTANCE


    def car_move(self):
        for car in self.CARS:
            car.forward(self.car_distance)

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car=Turtle()
            new_car.color(random.choice(COLORS))  # change
            new_car.shape("square")
            new_car.turtlesize(stretch_wid=1, stretch_len=3)
            new_car.penup()
            new_car.goto(x=300, y=random.randint(-250, 250))
            new_car.left(180)
            self.CARS.append(new_car)

    def increment_car_speed(self):
        self.car_distance += MOVE_INCREMENT




