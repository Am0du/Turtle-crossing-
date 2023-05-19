from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280
MOVE_INCREMENT = 5


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('black')
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.move_distance = 10

    def move(self):
        """Moves the player forward"""
        self.forward(self.move_distance)

    def reset_turtle(self):
        """Moves the player back to the starting position"""
        self.goto(STARTING_POSITION)

    def player_speed(self):
        """Increases the player move distance"""
        self.move_distance += MOVE_INCREMENT
