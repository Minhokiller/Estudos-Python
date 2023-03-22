from turtle import Screen
from pista import Pista

tela = Screen()
tela.setup(600,600)
tela.tracer(0)
pista=Pista()
tela.title('Tarturega')
jogo_on= True
while jogo_on == True:
    tela.update()
tela.exitonclick()

