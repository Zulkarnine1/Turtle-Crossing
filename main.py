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
score = Scoreboard()

screen.listen()
screen.onkey(player.move_forward,"Up")
screen.onkey(player.move_down,"Down")

game_is_on = True

while game_is_on:
    time.sleep(0.08)
    screen.update()
    carManager.make_car()
    carManager.move_cars(player,score)
    if player.dead:
        game_is_on = False
    if (player.ycor()>=280):
        player.relocate()
        # Reset player
        # Delete existing cars and increase speed
        carManager.level_up()
        # Update score
        score.update_score()

screen.exitonclick()
