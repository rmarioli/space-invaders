from turtle import Turtle

class ScreenSetUp(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(-400, 290)
        self.pendown()
        self.pensize(20)
        self.forward(800)
