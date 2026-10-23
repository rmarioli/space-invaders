from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.life_score = 3
        self.points = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-230, 240)
        self.write(f"Lifes: {self.life_score}", False, ALIGNMENT, FONT)
        self.goto(0, 240)
        self.write(f"Points: {self.points}", False, ALIGNMENT, FONT)


    def life_subs(self):
        self.life_score -= 1
        self.update_scoreboard()
        if self.life_score == 0:
            return True
        else:
            return False

    def point_up(self):
        self.points += 10
        self.update_scoreboard()
