from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
    def update_scoreboard(self):
        self.clear()
        self.write(self.score, align="center", font=("Arial",24,"normal"))

