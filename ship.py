import turtle

class Ship(turtle.Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1.5, stretch_wid=0.7)
        self.color("white")
        self.speed("fastest")
        self.goto(pos)

    def rightt(self):
        if not self.xcor() > 275:
            self.forward(14)

    def leftt(self):
        if not self.xcor() < -270:
            self.forward(-14)
