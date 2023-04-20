from turtle import Turtle

class Jogador(Turtle):
    def __init__(self,pos):
        super(Jogador, self).__init__()
        self.shape('square')
        self.shapesize(0.5,2)
        self.penup()
        self.goto(pos)

    def mover_direita(self):
        nova_pos = self.xcor() +30
        self.goto(nova_pos, self.ycor() )
    def mover_esquerda(self):
        nova_pos = self.xcor() -30
        self.goto(nova_pos, self.ycor() )
