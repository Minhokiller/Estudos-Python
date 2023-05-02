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
#obstaculo_1 = turtle.Turtle()
#obstaculo_1.penup()
#obstaculo_1.goto(-150, 35)
#obstaculo_1.color('green')
#obstaculo_1.shape('square')

#obstaculo_2 = turtle.Turtle()
#obstaculo_2.penup()
#obstaculo_2.goto(0, -25)
#obstaculo_2.color('green')
#obstaculo_2.shape('square')

#obstaculo_3 = turtle.Turtle()
#obstaculo_3.penup()
#obstaculo_3.goto(100, 10)
#obstaculo_3.color('green')
#obstaculo_3.shape('square')

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
    
# Define o tamanho da população e dos indivíduos
POP_SIZE = 4
IND_SIZE = 100  # cada indivíduo terá 100 movimentos

# Define os possíveis movimentos (cima, direita, baixo)

#POSSIBLE_MOVES = [(0, 10), (10, 0), (0, -10)]

# Gera a população inicial
population = []
x=-160
y=0
RIGHT = (x+10, y)
UP = (x, y+10)
DOWN = (x , y-10)
for i in range(POP_SIZE):
    # Gera um indivíduo aleatório
    individuo = []
    last_move = None  # armazena o último movimento
    for j in range(IND_SIZE):
        # Escolhe um movimento aleatório que obedeça às limitações
        if last_move is None:  # se for o primeiro movimento, pode ser qualquer um
            move = (RIGHT)
        else:
            possible_moves = [RIGHT]
            if last_move == ("UP"):  # último movimento foi para cima
                possible_moves = [UP, RIGHT]
            elif last_move == ("RIGHT"):  # último movimento foi para a direita
                possible_moves = [UP, RIGHT, DOWN]
            elif last_move == ("DOWN"):  # último movimento foi para baixo
                possible_moves = [DOWN, RIGHT]
            move = random.choice(possible_moves)
        if move == RIGHT:
            x =x+10
            last_move = ("RIGHT") 
            move = (x,y)
        elif move == UP:
            Y = y+10
            last_move = ("UP")
            move = (x,y)
        else:
            y = y-10
            last_move = ('DOWN')  
            move = (x,y)  
        print(f"o move é{move}")
        print(f"x e y = {x} e {y}")    
        individuo.append(move)
        
    #x = 0
    #y = 0
    population.append(individuo)

while not colisao(circulo, quadrado):
    for item in population:
        for indiv in individuo:
                # Loop while para mover o círculo vermelho até o quadrado azul
            #while not colisao(circulo, quadrado):
                # atualiza a direção atual e move o círculo

                
                circulo.pendown()
                circulo.pensize(8)
                
                print(indiv)
                print(item)
                circulo.goto(indiv)
                passos += 1
                janela.title(f"{tentativas}")
                circulo.penup()
                
                # Verificando colisões com as paredes verdes
                if circulo.xcor() > 180 or circulo.xcor() < -180 or circulo.ycor() > 45 or circulo.ycor() < -45:
                    tentativas += 1
                    print('bateu na parede')
                    dist = ((circulo.xcor() - quadrado.xcor())**2 + (circulo.ycor() - quadrado.ycor())**2)**0.5
                    print(int(dist))
                    circulo.clear()
                    passos = 0
                    input()
                    circulo.goto(-160, 0)

                
                # Verificando colisões com os obstáculos verdes
                #elif colisao(circulo, obstaculo_1) or colisao(circulo, obstaculo_2):# or colisao(circulo, obstaculo_3):
                    #tentativas += 1
                    #print('bateu no obstaculo')
                    #dist = ((circulo.xcor() - quadrado.xcor())**2 + (circulo.ycor() - quadrado.ycor())**2)**0.5
                    #print(int(dist))
                    #circulo.clear()
                    #passos = 0
                    #circulo.goto(-160, 0)
                
                else:
                    pass

#Exibindo mensagem de vitória
mensagem = turtle.Turtle()
mensagem.penup()
mensagem.goto(0, 120)
mensagem.color('black')
mensagem.write(f"O circulo chegou usando: ", align='center', font=('Arial', 20, 'bold'))
mensagem.goto(0, 90)
mensagem.write(f"{tentativas} Tentativas.", align='center', font=('Arial', 20, 'bold'))
mensagem.goto(0, 60)
mensagem.write(f"Com {passos} Passos.", align='center', font=('Arial', 20, 'bold'))
mensagem.hideturtle()

#Mantendo a janela aberta até o usuário fechar
janela.mainloop()

#Defina a representação da solução: a solução pode ser representada como uma série de movimentos do círculo. Cada movimento pode ser representado por um vetor de tamanho 2, que indica o deslocamento em x e y. Você precisará definir o tamanho da população, o tamanho dos indivíduos e outros parâmetros para o algoritmo.
#Crie a população inicial: Você precisará criar uma população inicial de soluções candidatas aleatórias, cada uma representando um indivíduo. Cada indivíduo será uma lista de movimentos. Para criar uma solução aleatória, você pode gerar uma lista de movimentos aleatórios para cada indivíduo.
#Avalie a população: Execute cada trajetória do círculo usando os movimentos do indivíduo e calcule a distância entre o círculo e o quadrado azul no final da trajetória. A solução é considerada melhor quanto menor for a distância.
#Selecione os melhores indivíduos: Selecione os melhores indivíduos da população atual com base na sua pontuação de aptidão (distância percorrida). Você pode usar uma estratégia de seleção por torneio ou seleção por roleta para selecionar os indivíduos.
#Aplique operadores genéticos: Use os operadores de crossover e mutação para criar uma nova geração de soluções. Você pode usar uma taxa de crossover e uma taxa de mutação para controlar a diversidade da população. O crossover pode ser realizado selecionando dois pais aleatórios e trocando uma parte dos seus movimentos. A mutação pode ser realizada alterando aleatoriamente um ou mais movimentos de um indivíduo.
#Repita os passos 3 a 5 até que uma solução satisfatória seja encontrada ou um critério de parada seja atingido, como um número máximo de gerações ou um limite de tempo.
#Execute a melhor solução: Depois de encontrar uma solução satisfatória, execute a trajetória do círculo usando os movimentos do indivíduo e observe se o círculo chega ao quadrado azul.
#Lembre-se de que implementar um algoritmo genético é um processo complexo e pode levar tempo e esforço para obter uma solução satisfatória. Se você tiver dificuldades em alguma etapa ou quiser mais ajuda, sinta-se à vontade para me perguntar.
