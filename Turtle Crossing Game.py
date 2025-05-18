from turtle import Screen, Turtle
from player import Player
import time
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height= 600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkeypress(fun=player.move_up, key="Up")

car_manager.generate_cars()


game_is_on = True

while game_is_on:
    time.sleep(player.move_speed)
    screen.update()
    car_manager.car_movement()
    if player.ycor() > 280:
        player.back_to_start()
        scoreboard.add_score()
    #Detect Collisions
    for car_info in car_manager.all_cars:
        car = car_info["turtle"]
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
