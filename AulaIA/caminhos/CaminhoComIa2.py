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

POP_SIZE = 1
IND_SIZE = 20
mutation_rate = 1
directions = ['direita']


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
        if move == ("direita"):
            last_move = ("direita") 
        elif move == ("cima"):
            last_move = ("cima")
        else:
            last_move = ('baixo') 
            #print('a') 
        individuo.append(move)
    population.append(individuo)

#print(population)

while not colisao(circulo, quadrado):
    for pop in population:
        #print(f"o population é :{pop}")
        for ind in individuo:
            #print(f"o individuo é :{ind}")
            # escolhe uma direção aleatória permitida com base na direção atual
            #direcoes_possiveis = direcoes_permitidas[direcao_atual]
            direcao_aleatoria = ind

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
                #print('bateu na parede')
                dist = ((circulo.xcor() - quadrado.xcor())**2 + (circulo.ycor() - quadrado.ycor())**2)**0.5
                #print(int(dist))
                circulo.clear()
                circulo.goto(-160, 0)

            
            # Verificando colisões com os obstáculos verdes
            elif colisao(circulo, obstaculo_1) or colisao(circulo, obstaculo_2) or colisao(circulo, obstaculo_3):
                tentativas += 1
                #print('bateu no obstaculo')
                dist = ((circulo.xcor() - quadrado.xcor())**2 + (circulo.ycor() - quadrado.ycor())**2)**0.5
                #print(int(dist))
                circulo.clear()
                circulo.goto(-160, 0)
    mutated_individuo = individuo
    for kik in population:
        for i in individuo:
            if random.random() <= mutation_rate:
                print(f"Nesse momento o i é {i}")
                if i == "cima":  # último movimento foi para cima
                    directions = ["cima", "direita"]
                    last_move = ("cima")
                elif i == "direita":  # último movimento foi para a direita
                    directions = ["cima", "direita", "baixo"]
                    last_move = ("direita")
                elif i == "baixo":  # último movimento foi para baixo
                    directions = ["baixo", "direita"]
                    last_move = "baixo"
                else:
                    directions = ["crash"]
                    last_move = ("crash")

                new_direction = random.choice(directions)
                mutated_individuo = new_direction
            individuo.append(mutated_individuo)
            print(f"Nesse momento foi apendado o  {mutated_individuo}")
            
        population.append(individuo)
        print(f"Nesse momento foi apendado o population  {individuo}")
    print(f"restart")
        #print(mutated_individuo)
            
             
            #else:
                
                #Exibindo mensagem de vitória
                #mensagem = turtle.Turtle()
                #mensagem.penup()
                #mensagem.goto(0, 80)
                #mensagem.color('black')
                #mensagem.write(f"O circulo chegou depois de: {tentativas} tentativas", align='center', font=('Arial', 14, 'bold'))
                #mensagem.hideturtle()

    #def mutate(individuo, mutation_rate):
                       




#Mantendo a janela aberta até o usuário fechar
#mutate(individuo,0)
janela.mainloop()


