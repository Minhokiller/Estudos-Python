import time
import turtle
from turtle import Screen
from pista import Pista
from jogador import Jogador
from carro import CarroConfig

tela = Screen()
tela.setup(600,600)
tela.tracer(0)
tela.bgcolor('green')
pista=Pista()
tela.listen()
jogador=Jogador()
carro_config=CarroConfig()
tela.onkey(jogador.mover_direita,'Right')
tela.onkey(jogador.mover_esquerda,'Left')
tela.title('Tarturega')
jogo_on= True
while jogo_on == True:
    time.sleep(0.1)
    carro_config.aparecer_carro()
    carro_config.mover_carro()
    if jogador.xcor() > 120 or jogador.xcor() < -120:
        turtle.write(f"Game Over", align='center', font=('arial',40,'bold'))
        jogo_on = False
    for carrinho in carro_config.carros:
        if abs(jogador.xcor() - carrinho.xcor()) <1 and jogador.distance(carrinho) < 65:
            turtle.write(f"Game Over", align='center', font=('arial',40,'bold'))
            jogo_on = False
    tela.update()
tela.exitonclick()

