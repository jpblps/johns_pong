from turtle import Turtle

NET = """
|

|

|

|

|

|

|

|

|
"""


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        net = Turtle()
        net.color("white")
        net.hideturtle()
        net.pu()
        net.goto(0, -315)
        net.write(NET, False, "center", ("courier", 24, "normal"))

        self.color("white")
        self.pu()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 190)
        self.write(f"{self.p1_score} {self.p2_score}", False, "center", ("courier", 70, "normal"))

    # def scored(self):
    #     self.goto(0, 0)
    #     self.write("SCORE!", False, "center", ("courier", 28, "normal"))

    def p1_point(self):
        self.clear()
        self.p1_score += 1
        self.update_scoreboard()

    def p2_point(self):
        self.clear()
        self.p2_score += 1
        self.update_scoreboard()
