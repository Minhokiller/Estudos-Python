from turtle import Turtle

class Bola(Turtle):
    def __init__(self):
        super(Bola, self).__init__()
        self.shape('circle')
        self.shapesize(1)
        self.penup()
        self.move_x = 1
        self.move_y = 2
        self.penup()

    def mover_bola(self):
        novo_x = self.xcor() + self.move_x
        novo_y = self.ycor() + self.move_y
        self.goto(novo_x,novo_y)

    def quicar_pos_x(self):
        self.move_x*=1
    def quicar_pos_y(self):
        self.move_y*=1
