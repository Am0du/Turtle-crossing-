import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard()

game_play = True
game_on = True


def stop():
    """Stops the while loop"""
    global game_on
    game_on = False
    return game_on


screen.onkey(player.move, 'Up')
screen.onkey(stop, 's')


def stop():
    """Stops the while loop"""
    global game_on
    game_on = False
    return game_on


while game_on:
    time.sleep(0.1)
    screen.update()

    if game_play:
        car.move()

        # Detects contacts with car
        for j in car.all_cars:
            if j.distance(player) < 32:
                game_play = False

        # When Player crosses over
        if player.ycor() > 280:
            score.add_level()
            car.car_speed()
            player.reset_turtle()
            player.player_speed()
    else:
        score.game_over()
