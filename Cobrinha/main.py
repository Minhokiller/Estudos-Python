from turtle import Screen
from campo import Campo
from cobra import Cobra
import time


tela = Screen()
tela.title('Jogo da cobrinha')
tela.setup(600,620)
tela.bgcolor('beige')
jogo_on = True
tela.tracer(0)
cobra = Cobra()
tela.listen()
tela.onkey(cobra.mover_direita,'Right')
tela.onkey(cobra.mover_esquerda,'Left')
tela.onkey(cobra.mover_cima,'Up')
tela.onkey(cobra.mover_baixo,'Down')
campo = Campo()
while jogo_on:
    time.sleep(0.01) 
    cobra.mover() 
    tela.update()
tela.exitonclick()
