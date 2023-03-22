from turtle import Screen
from pista import Pista
from jogador import Jogador
from carro import CarroConfig

tela = Screen()
tela.setup(600,600)
tela.tracer(0)
pista=Pista()
tela.listen()
jogador=Jogador()
carro_config=CarroConfig()
tela.onkey(jogador.mover_direita,'Right')
tela.onkey(jogador.mover_esquerda,'Left')
tela.title('Tarturega')
jogo_on= True
while jogo_on == True:
    tela.update()
tela.exitonclick()

