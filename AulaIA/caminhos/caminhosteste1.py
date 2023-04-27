import turtle
import random

# Configurações iniciais
turtle.speed(0)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.color("blue")
turtle.shape("circle")

# Define os limites do ambiente
xmin, xmax = -200, 200
ymin, ymax = -200, 200

# Define os obstáculos
obstacles = []
for i in range(5):
    obstacle = turtle.Turtle()
    obstacle.penup()
    obstacle.goto(random.randint(xmin, xmax), random.randint(ymin, ymax))
    obstacle.pendown()
    obstacle.color("red")
    obstacle.shape("triangle")
    obstacles.append(obstacle)

# Define a função de movimento aleatório
def move():
    directions = [0, 90, 180, 270]  # direções possíveis
    direction = random.choice(directions)  # escolhe uma direção aleatória
    turtle.setheading(direction)
    turtle.forward(10)

    # Verifica se o círculo colidiu com a parede
    x, y = turtle.position()
    if x < xmin or x > xmax or y < ymin or y > ymax:
        turtle.goto(-200, 0)  # retorna o círculo à posição inicial

    # Verifica se o círculo colidiu com um obstáculo
    for obstacle in obstacles:
        if turtle.distance(obstacle) < 20:
            turtle.goto(-200, 0)  # retorna o círculo à posição inicial

    # Verifica se o círculo chegou ao quadrado
    if turtle.distance(200, 0) < 20:
        return True
    else:
        return False

# Executa o movimento aleatório até chegar ao quadrado
while not move():
    pass

turtle.done()
