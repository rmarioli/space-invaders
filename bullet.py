import turtle


class Bullet(turtle.Turtle):
    def __init__(self, pos, bullet_direction):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=0.8, stretch_wid=0.175)
        self.penup()
        self.color("white")
        self.speed(0)
        self.setheading(90)
        self.goto(pos)
        self.bullet_direction = bullet_direction

    def bullet_move(self):
        self.forward(10*self.bullet_direction)

    def reset_pos(self):
        self.goto(0, 50)
        self.change_movement_x()

