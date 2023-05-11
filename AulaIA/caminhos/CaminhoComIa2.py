import turtle
import random

# Criando a janela de jogo
janela = turtle.Screen()
janela.setup(420, 420)
tentativas = 0
passos = 0
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
obstaculo_1.shapesize(1)

obstaculo_2 = turtle.Turtle()
obstaculo_2.penup()
obstaculo_2.goto(0, -25)
obstaculo_2.color('green')
obstaculo_2.shape('square')
obstaculo_2.shapesize(1)

obstaculo_3 = turtle.Turtle()
obstaculo_3.penup()
obstaculo_3.goto(100, 10)
obstaculo_3.color('green')
obstaculo_3.shape('square')
obstaculo_3.shapesize(1)

# Criando o círculo vermelho
circulo = turtle.Turtle()
circulo.penup()
circulo.shape('circle')
circulo.color('red')
circulo.goto(-160, 0)

# Função para verificar colisões
def colisao(turtle, objeto):
    if turtle.distance(objeto) < 30:
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

POP_SIZE = 10 
IND_SIZE = 50
#mutation_rate = 1

population = []
for i in range(POP_SIZE):
    # Gera um indivíduo aleatório
    individuo = []
    last_move = None  # armazena o último movimento
    for j in range(IND_SIZE):
        # Escolhe um movimento aleatório que obedeça às limitações
        if last_move is None:  # se for o primeiro movimento, pode ser qualquer um
            move = ("direita")
        else:
            possible_moves = ["direita"]
            if last_move == ("cima"):  # último movimento foi para cima
                possible_moves = ["cima", "direita"]
            elif last_move == ("direita"):  # último movimento foi para a direita
                possible_moves = ["cima", "direita", "baixo"]
            elif last_move == ("baixo"):  # último movimento foi para baixo
                possible_moves = ["baixo", "direita"]
            move = random.choice(possible_moves)
        last_move = move 

        individuo.append(move)
    population.append(individuo)
janela.tracer(10)
game = True
while game:   
    for pop in population:
        tentativas += 1
        janela.title(f"tentativas:{tentativas} passos:{passos}")
        print(f"o population é :{population}")
        circulo.goto(-160, 0)
        circulo.clear()

        for ind in pop:
            passos += 1
            janela.title(f"tentativas:{tentativas} passos:{passos}")
            print(f"o individuo é :{ind}")
            direcao_aleatoria = ind
            

            # atualiza a direção atual e move o círculo
            circulo.pendown()
            circulo.pensize(8)
            if direcao_aleatoria == "direita":
                circulo.right(circulo.heading())
            elif direcao_aleatoria == "cima":
                circulo.setheading(90)
            elif direcao_aleatoria == "baixo":
                circulo.setheading(270)
            circulo.pencolor("red")
            circulo.forward(10)
            circulo.penup()
            
            
            #Verificando colisões com as paredes verdes
            if circulo.xcor() > 190 or circulo.xcor() < -180 or circulo.ycor() > 35 or circulo.ycor() < -35:
                print('bateu na parede')
                dist = ((circulo.xcor() - quadrado.xcor())**2 + (circulo.ycor() - quadrado.ycor())**2)**0.5
                print(int(dist))       
                
                break
                            
            #Verificando colisões com os obstáculos verdes
            elif colisao(circulo, obstaculo_1) or colisao(circulo, obstaculo_2) or colisao(circulo, obstaculo_3):
                print('bateu no obstaculo')
                dist = ((circulo.xcor() - quadrado.xcor())**2 + (circulo.ycor() - quadrado.ycor())**2)**0.5
                print(int(dist))
                break

            if colisao (circulo, quadrado):
                #Exibindo mensagem de vitória
                mensagem = turtle.Turtle()
                mensagem.penup()
                mensagem.goto(0, 80)
                mensagem.color('black')
                mensagem.write(f"O circulo chegou depois de: {tentativas} tentativas", align='center', font=('Arial', 14, 'bold'))
                mensagem.hideturtle()
                game == False
                break  
        # ordena a população por distância em ordem crescente
    populacao_ordenada = [x for _, x in sorted(zip(distancias, population))]
    # seleciona os 5 melhores indivíduos
    melhores_individuos = populacao_ordenada[:5]

    # cria nova população
    nova_populacao = []
    for i in range(POP_SIZE):
        if i < len(melhores_individuos):
            # insere os melhores indivíduos na nova população sem mutação
            nova_populacao.append(melhores_individuos[i])
        else:
            # seleciona um indivíduo aleatório dos 5 melhores
            individuo_base = random.choice(melhores_individuos)
            # realiza a mutação
            novo_individuo = individuo_base[:IND_SIZE//2] + [random.choice(["cima", "direita", "baixo"]) for j in range(IND_SIZE//2)]
            # insere o novo indivíduo na nova população
            nova_populacao.append(novo_individuo)

    # atualiza a população
    population = nova_populacao


print("fim")

janela.mainloop()


