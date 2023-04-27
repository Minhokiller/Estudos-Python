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

# Define a representação cromossômica
def random_instruction():
    return (random.choice([0, 90, 180, 270]), random.randint(1, 10))

def random_solution(length):
    return [random_instruction() for i in range(length)]

# Define a função de avaliação
def fitness(solution):
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    turtle.setheading(0)
    distance = 0
    for direction, steps in solution:
        turtle.setheading(direction)
        turtle.forward(steps)
        distance += steps
        if turtle.distance(200, 0) < 20:
            return distance
        elif turtle.xcor() < xmin or turtle.xcor() > xmax or turtle.ycor() < ymin or turtle.ycor() > ymax:
            return 0
        else:
            for obstacle in obstacles:
                if turtle.distance(obstacle) < 20:
                    return 0
    return distance

# Define os operadores genéticos
def tournament_selection(population, tournament_size):
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=lambda x: fitness(x))

def crossover(solution1, solution2):
    i1 = random.randint(0, len(solution1) - 1)
    i2 = random.randint(0, len(solution2) - 1)
    sub1 = solution1[:i1] + solution2[i2:]
    sub2 = solution2[:i2] + solution1[i1:]
    return sub1, sub2

def mutation(solution, mutation_rate):
    for i in range(len(solution)):
        if random.random() < mutation_rate:
            solution[i] = random_instruction()
            return solution
        
#Define os parâmetros do algoritmo genético

population_size = 100
solution_length = 20
tournament_size = 5
mutation_rate = 0.1

#Inicializa a população
population = [random_solution(solution_length) for i in range(population_size)]

#Executa o algoritmo genético
for generation in range(100):
# Avalia a população
    fitnesses = [fitness(solution) for solution in population]

# Seleciona os pais
parents = [tournament_selection(population, tournament_size) for i in range(population_size)]

# Realiza o cruzamento
offspring = []
for i in range(0, population_size, 2):
    child1, child2 = crossover(parents[i], parents[i+1])
    offspring.append(child1)
    offspring.append(child2)

# Realiza a mutação
offspring = [mutation(solution, mutation_rate) for solution in offspring]

# Substitui a população antiga pela nova
population = offspring

# Imprime a melhor solução da geração atual
best_solution = max(population, key=lambda x: fitness(x))
print("Generation:", generation, "Fitness:", fitness(best_solution))

# Desenha a melhor solução
turtle.clear()
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.setheading(0)
for direction, steps in best_solution:
    turtle.setheading(direction)
    turtle.forward(steps)
    if turtle.distance(200, 0) < 20:
        break
    elif turtle.xcor() < xmin or turtle.xcor() > xmax or turtle.ycor() < ymin or turtle.ycor() > ymax:
        break
    else:
        for obstacle in obstacles:
            if turtle.distance(obstacle) < 20:
                break
