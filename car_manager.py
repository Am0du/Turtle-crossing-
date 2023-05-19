from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.start()
        self.starting_move_distance = 5
        self.move_increment = 10
        self.movement_speed = 0.1

    def start(self):
        for _ in range(20):
            """Creates the initial cars"""
            random_xcor = random.randint(-300, 300)
            self.generate_cars(random_xcor)

    def generate_cars(self, x_cor):
        """Generates the car"""
        random_color = random.choice(COLORS)
        random_ycor = random.randint(-220, 250)
        turtle = Turtle('square')
        turtle.penup()
        turtle.setheading(180)
        turtle.turtlesize(stretch_wid=1.5, stretch_len=3)
        turtle.color(random_color)
        turtle.goto(x_cor, random_ycor)
        self.all_cars.append(turtle)

    def move(self):
        """Moves the car forward and add more cars """
        for i in self.all_cars:
            i.forward(self.starting_move_distance)

            if i.xcor() < -340:
                self.all_cars.remove(i)

        if len(self.all_cars) < 17:
            self.generate_cars(240)

    def car_speed(self):
        """Increases the speed of the car"""
        self.starting_move_distance += self.move_increment
        self.movement_speed *= 0.9

