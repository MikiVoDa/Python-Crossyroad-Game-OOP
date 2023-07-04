import time
from turtle import Screen
from player import Player, FINISH_LINE_Y, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
score = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()

            game_is_on = False

    if player.ycor() == FINISH_LINE_Y:
        player.goto(STARTING_POSITION)
        scoreboard.point()
        car_manager.increment += 1
        scoreboard.update()

screen.exitonclick()
