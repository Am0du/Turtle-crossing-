from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.counter = 1
        self.level()

    def level(self):
        """Show the Current level of the player"""
        self.clear()
        self.goto(-300, 260)
        self.write(f'LEVEL: {self.counter}', align='left', font=FONT)

    def add_level(self):
        """Adds to the level"""
        self.counter += 1
        self.level()

    def game_over(self):
        """Game Over"""
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)
