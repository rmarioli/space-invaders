import turtle

class Obstacle(turtle.Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.goto(pos)
        self.life = 3

    def obst_damage(self):
        if self.life == 3:
            self.life -= 1
            self.color("yellow")
            return False
        elif self.life == 2:
            self.life -= 1
            self.color("red")
        else:
            return True