

# Loop while para mover o círculo vermelho até o quadrado azul
class Roda():
    def __init__(self) -> None:
        pass
        while not colisao(circulo, quadrado):
            for pop in population:
                print(f"o population é :{pop}")
                for ind in individuo:
                    print(f"o individuo é :{ind}")
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
                        
                        #Exibindo mensagem de vitória
                        mensagem = turtle.Turtle()
                        mensagem.penup()
                        mensagem.goto(0, 80)
                        mensagem.color('black')
                        mensagem.write(f"O circulo chegou depois de: {tentativas} tentativas", align='center', font=('Arial', 14, 'bold'))
                        mensagem.hideturtle()
            def mutate(individuo, mutation_rate):
                mutated_individuo = individuo.copy()
                for i in range(len(mutated_individuo)):
                    if random.random() <= mutation_rate:
                        directions = ['direita', 'esquerda', 'cima', 'baixo']
                        new_direction = random.choice(directions)
                        mutated_individuo[i] = new_direction
                    print(mutated_individuo)
                        return mutated_individuo