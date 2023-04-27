import turtle
import random

# Define a janela do turtle
janela = turtle.Screen()
janela.title("Círculo até o Quadrado")
janela.bgcolor("white")
janela.setup(width=600, height=600)

# Define as paredes do mapa
parede_esquerda = -200
parede_direita = 200
parede_superior = 50
parede_inferior = -50

# Define os obstáculos do mapa
obstaculos = [(50, 50), (-50, 50), (0, 0)]

# Cria o círculo
circulo = turtle.Turtle()
circulo.shape("circle")
circulo.color("blue")
circulo.penup()

# Cria o quadrado
quadrado = turtle.Turtle()
quadrado.shape("square")
quadrado.color("red")
quadrado.penup()
quadrado.goto(200, 0)

# Define uma lista para armazenar as posições visitadas pelo círculo
posicoes_visitadas = []

# Loop para fazer o círculo se mover aleatoriamente até chegar ao quadrado
while True:
    # Gera um novo movimento aleatório para o círculo
    dx = random.randint(-10, 10)
    dy = random.randint(-10, 10)
    circulo.goto(circulo.xcor() + dx, circulo.ycor() + dy)
    
    # Verifica se o círculo colidiu com uma parede ou um obstáculo
    if (circulo.xcor(), circulo.ycor()) in posicoes_visitadas or \
        circulo.xcor() < parede_esquerda or circulo.xcor() > parede_direita or \
        circulo.ycor() < parede_inferior or circulo.ycor() > parede_superior or \
        (circulo.xcor(), circulo.ycor()) in obstaculos:
        
        # Desfaz o último movimento e gera um novo aleatório
        circulo.goto(circulo.xcor() - dx, circulo.ycor() - dy)
        continue
    
    # Adiciona a posição atual do círculo à lista de posições visitadas
    posicoes_visitadas.append((circulo.xcor(), circulo.ycor()))
    
    # Verifica se o círculo chegou ao quadrado
    if circulo.distance(quadrado) < 20:
        break

# Espera o usuário clicar para fechar a janela
janela.exitonclick()
