from turtle import Screen
from campo import Campo
from cobra import Cobra
from maca import Maca
from pontuacao import Pontuacao
import time


tela = Screen()
tela.title('Jogo da cobrinha')
tela.setup(600,620)
tela.bgcolor('beige')
jogo_on = True
tela.tracer(0)
cobra = Cobra()
maca = Maca()
tela.listen()
tela.onkey(cobra.mover_direita,'Right')
tela.onkey(cobra.mover_esquerda,'Left')
tela.onkey(cobra.mover_cima,'Up')
tela.onkey(cobra.mover_baixo,'Down')
campo = Campo()
pontuacao = Pontuacao()
while jogo_on:
    maca.nova_maca
    time.sleep(0.01)
     
    if cobra.cabeca.distance(maca)<20:
        print('comeu a maca')
        pontuacao.marca_ponto()
        maca.nova_maca()
        cobra.crecer_cobra()
        
    cobra.mover() 
    if cobra.cabeca.xcor() > 285 or cobra.cabeca.xcor() < -285 or cobra.cabeca.ycor() < -285 or cobra.cabeca.ycor() > 285:
        jogo_on = False
        print('faleceu')
    tela.update()
tela.exitonclick()
