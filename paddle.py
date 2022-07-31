from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color('white')
        self.penup()
        self.reset_position(position)
        self.speed('fastest')

    def reset_position(self, position):
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 35
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 35
        self.goto(self.xcor(), new_y)
