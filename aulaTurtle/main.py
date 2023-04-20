from turtle import Screen
from boneco import Boneco
from campo import Campo

tela = Screen()
tela.tracer(0)

tela.setup(440,840)
tela.title('Boneco')
tela.bgcolor('#66d5aa')
campo = Campo()
#boneco1 = Boneco(0,0)
#boneco2 = Boneco(80,0)
#boneco3 = Boneco(40,-40)

game_on = True
while game_on:
    tela.update()
    tela.exitonclick()
