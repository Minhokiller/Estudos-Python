from turtle import Turtle

class Pontuacao(Turtle):
    def __init__(self):
        super(Pontuacao,self).__init__()
        self.penup()
        self.goto(0,285)
        self.hideturtle()
        self.pontuacao=0
        self.marca_ponto()
    def marca_ponto(self):
        self.mostra_ponto()
        self.pontuacao+=10
    def mostra_ponto(self,nome ='Andre'):
        self.clear()
        self.write(f'{self.pontuacao}|{nome}',font=('arial',20,'bold'),align='center')