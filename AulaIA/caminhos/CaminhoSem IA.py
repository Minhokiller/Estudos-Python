import turtle
import random

# Criando a janela de jogo
janela = turtle.Screen()
janela.setup(420, 420)
tentativas = 0
janela.title(f"{tentativas}")
janela.tracer(10)

# Criando a parede verde
parede = turtle.Turtle()
parede.penup()
parede.pencolor('green')
parede.pensize(4)
parede.goto(200, 50)
parede.pendown()
parede.goto(200, -50)
parede.goto(-200, -50)
parede.goto(-200, 50)
parede.goto(200, 50)

# Criando o quadrado azul
quadrado = turtle.Turtle()
quadrado.shape('square')
quadrado.color('blue')
quadrado.penup()
quadrado.goto(180, 0)

# Criando os obstáculos verdes
obstaculo_1 = turtle.Turtle()
obstaculo_1.penup()
obstaculo_1.goto(-150, 35)
obstaculo_1.color('green')
obstaculo_1.shape('square')

obstaculo_2 = turtle.Turtle()
obstaculo_2.penup()
obstaculo_2.goto(0, -25)
obstaculo_2.color('green')
obstaculo_2.shape('square')

obstaculo_3 = turtle.Turtle()
obstaculo_3.penup()
obstaculo_3.goto(100, 10)
obstaculo_3.color('green')
obstaculo_3.shape('square')

# Criando o círculo vermelho
circulo = turtle.Turtle()
circulo.penup()
circulo.shape('circle')
circulo.color('red')
circulo.goto(-160, 0)

# Criando um conjunto para armazenar as posições por onde o círculo já passou
posicoes = set()

# Função para verificar colisões
def colisao(turtle, objeto):
    if turtle.distance(objeto) < 20:
        return True
    else:
        return False
    
# define as direções permitidas para cada direção atual
direcoes_permitidas = {
    "direita": ["direita", "cima", "baixo"],
    "cima": ["cima", "direita"],
    "baixo": ["baixo", "direita"]
}

# define a direção inicial do círculo
direcao_atual = "direita"


# Loop while para mover o círculo vermelho até o quadrado azul
while not colisao(circulo, quadrado):

    # escolhe uma direção aleatória permitida com base na direção atual
    direcoes_possiveis = direcoes_permitidas[direcao_atual]
    direcao_aleatoria = random.choice(direcoes_possiveis)

    # atualiza a direção atual e move o círculo
    circulo.pendown()
    circulo.pensize(8)
    if direcao_aleatoria == "direita":
        circulo.right(circulo.heading())
        direcao_atual = "direita"
    elif direcao_aleatoria == "cima":
        circulo.setheading(90)
        direcao_atual = "cima"
    elif direcao_aleatoria == "baixo":
        circulo.setheading(270)
        direcao_atual = "baixo"
    circulo.forward(10)
    janela.title(f"{tentativas}")
    circulo.penup()
    
    # Verificando colisões com as paredes verdes
    if circulo.xcor() > 180 or circulo.xcor() < -180 or circulo.ycor() > 45 or circulo.ycor() < -45:
        tentativas += 1
        print('bateu na parede')
        dist = ((circulo.xcor() - quadrado.xcor())**2 + (circulo.ycor() - quadrado.ycor())**2)**0.5
        print(int(dist))
        circulo.clear()
        circulo.goto(-160, 0)

    
    # Verificando colisões com os obstáculos verdes
    elif colisao(circulo, obstaculo_1) or colisao(circulo, obstaculo_2) or colisao(circulo, obstaculo_3):
        tentativas += 1
        print('bateu no obstaculo')
        dist = ((circulo.xcor() - quadrado.xcor())**2 + (circulo.ycor() - quadrado.ycor())**2)**0.5
        print(int(dist))
        circulo.clear()
        circulo.goto(-160, 0)
    
    else:
        posicoes.add((circulo.xcor(), circulo.ycor()))

#Exibindo mensagem de vitória
mensagem = turtle.Turtle()
mensagem.penup()
mensagem.goto(0, 80)
mensagem.color('black')
mensagem.write(f"O circulo chegou usando {tentativas}", align='center', font=('Arial', 14, 'bold'))
mensagem.hideturtle()

#Mantendo a janela aberta até o usuário fechar
janela.mainloop()


