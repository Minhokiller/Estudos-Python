from turtle import Turtle
import random

class Maca(Turtle):
    def __init__(self):
        super(Maca, self).__init__()
        self.color('red')
        self.shape('circle')
        self.nova_maca()
    def nova_maca(self):
        self.penup()
        x,y = random.randint(-280, 280), random.randint(-280, 280)
        self.goto(x,y)