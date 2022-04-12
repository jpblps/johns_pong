import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.x_vector = random.choice([-10, 10])
        self.y_vector = random.choice([-10, 10])
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_vector
        new_y = self.ycor() + self.y_vector
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_vector *= -1

    def bounce_x(self):
        if self.xcor() > 320:
            self.x_vector = -10
        elif self.xcor() < -320:
            self.x_vector = 10

    def reset_position(self):
        self.goto(0, 0)
        self.x_vector *= -1
