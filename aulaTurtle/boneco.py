from turtle import Turtle

class Boneco(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.Corpo(x,y)
        self.goto(x,y)
        
    def Corpo(self,x,y):
        self.goto(x,y)
        self.pendown()
        self.pensize(4)
        self.goto(x,y-50)
        self.goto(x+20,y-80)
        self.goto(x,y-50)
        self.goto(x-20,y-80)
        self.goto(x,y-50)
        self.goto(x,y-20)
        self.goto(x+20,y-30)
        self.goto(x,y-20)
        self.goto(x-20,y-30)
        self.penup()

