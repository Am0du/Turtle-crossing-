from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", mode='r') as data:
            self.highest_level = int(data.read())
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
        self.goto(280, 260)
        self.write(f'HIGHEST LEVEL: {self.highest_level}', align='right', font=FONT)

    def add_level(self):
        """Adds to the level"""
        self.counter += 1
        self.level()

    def game_over(self):
        """Game Over"""
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)
        if self.counter > self.highest_level:
            with open('data.txt', mode='w') as data:
                self.highest_level = self.counter
                data.write(f'{self.counter}')
