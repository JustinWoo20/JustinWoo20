from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
NU_CARS = 20
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = random.randint(5, 10)

class CarManager:
    def __init__(self):
        self.all_cars = []


    def generate_cars(self):
        for _ in range(NU_CARS):
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            random_x = random.randint(-300, 300)
            random_y = random.randint(-250, 250)
            new_car.goto(random_x, random_y)
            speed = random.randint(5, 10)
            self.all_cars.append({"turtle": new_car, "speed": speed},)

    def car_movement(self):
        for car_info in self.all_cars:
            car = car_info["turtle"]
            speed = car_info["speed"]
            car.forward(speed)
            if car.xcor() < -300:
                car.goto(300, random.randint(-250, 250))






