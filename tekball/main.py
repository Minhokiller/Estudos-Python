from turtle import Screen
from jogador import Jogador
from bola import Bola
import time



tela = Screen()
tela.tracer(0)
tela.setup(620,600)
tela.title('tekbola')
tela.bgcolor('#66d5aa')
jogador1= Jogador((0,-280))
jogador2= Jogador((0,280))


tela.listen()
#mov jog 1
tela.onkey(jogador1.mover_direita,'Right')
tela.onkey(jogador1.mover_esquerda,'Left')

#mov jog 2
tela.onkey(jogador2.mover_direita,'d')
tela.onkey(jogador2.mover_esquerda,'a')

bola = Bola()

jogo_on = True
while jogo_on:
    bola.mover_bola()
    time.sleep(0.02)
    tela.update()
    if bola.xcor() > 280 or bola.xcor() < -280:
        bola.quicar_pos_x()

tela.exitonclick()