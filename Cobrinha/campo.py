from turtle import Turtle

class Campo(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pensize(4)
        self.goto(200,200)
        self.pendown()
        self.goto(200,-200)
        self.goto(-200,-200)
        self.goto(-200,200)
        self.goto(200,200)
        self.hideturtle()
