import turtle

class Alien(turtle.Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("turtle")
        self.tilt(-90)
        self.penup()
        self.shapesize(stretch_len=0.76, stretch_wid=0.8)
        self.color("white")
        self.goto(pos)
        self.dir = 1

    def alien_move_x(self, dir_ship):
        self.forward(2*dir_ship)

    def alien_move_y(self):
        self.setheading(90)
        self.forward(-5)
        self.setheading(-90)

    def up(self):
        self.forward(28)

    def down(self):
        self.forward(-28)
