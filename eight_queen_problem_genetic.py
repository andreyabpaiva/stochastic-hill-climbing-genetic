import random
import numpy as np
import time

# Função para converter binário em posição das rainhas
def binary_to_queens(binary):
    queens = []
    for i in range(0, len(binary), 3):  # 3 bits para representar uma posição de 0 a 7
        queens.append(int(''.join(map(str, binary[i:i+3])), 2))
    return queens

# Função para calcular aptidão (fitness) - quanto menor, melhor
def fitness(queens):
    non_attacking = 28  # Máximo de pares não se atacando
    attacking = 0
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == j - i:
                attacking += 1
    return non_attacking - attacking

# Inicializa a população
def initialize_population(size):
    population = []
    for _ in range(size):
        individual = [random.randint(0, 1) for _ in range(24)]  # 8 rainhas em 24 bits (3 bits por rainha)
        population.append(individual)
    return population

# Função para seleção via roleta
def roulette_selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for individual, fitness in zip(population, fitnesses):
        current += fitness
        if current > pick:
            return individual

# Função para o cruzamento de um ponto
def crossover(parent1, parent2):
    if random.random() < 0.8:  # 80% de chance de cruzamento
        point = random.randint(1, len(parent1) - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1, parent2

# Função para mutação por flip de bit
def mutate(individual):
    for i in range(len(individual)):
        if random.random() < 0.03:  # 3% de chance de mutação
            individual[i] = 1 - individual[i]
    return individual

# Algoritmo genético
def genetic_algorithm():
    population_size = 20
    max_generations = 1000
    elite_size = 2

    population = initialize_population(population_size)
    
    for generation in range(max_generations):
        fitnesses = [fitness(binary_to_queens(ind)) for ind in population]
        
        if max(fitnesses) == 28:  # Solução ótima encontrada
            return population[fitnesses.index(max(fitnesses))], generation

        # Seleção dos pais
        new_population = []
        for _ in range(population_size // 2):
            parent1 = roulette_selection(population, fitnesses)
            parent2 = roulette_selection(population, fitnesses)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.append(mutate(offspring1))
            new_population.append(mutate(offspring2))
        
        # Seleção de sobreviventes (elitismo)
        elites = [x for _, x in sorted(zip(fitnesses, population), reverse=True)][:elite_size]
        population = elites + new_population[:population_size - elite_size]

    # Retorna o melhor indivíduo após as gerações
    best_fitness = max(fitnesses)
    best_individual = population[fitnesses.index(best_fitness)]
    return best_individual, max_generations

# Função para executar múltiplas execuções e mostrar soluções e métricas
def run_multiple_executions():
    num_executions = 50
    solutions = []
    generations_list = []
    times = []
    
    for i in range(num_executions):
        start_time = time.time()
        best_individual, generations = genetic_algorithm()
        end_time = time.time()
        
        queens_solution = binary_to_queens(best_individual)
        time_taken = end_time - start_time
        
        solutions.append(queens_solution)
        generations_list.append(generations)
        times.append(time_taken)
        
        print(f"Tentativa {i+1}:")
        print(f"Solução: {queens_solution}")
        if generations < 1000:
            print(f"Solução ótima encontrada em {generations} gerações.")
        else:
            print("Solução ótima não encontrada. Melhor solução após 1000 gerações.")
        print(f"Tempo de execução: {time_taken:.4f} segundos\n")
    
    return solutions, generations_list, times

# Função para exibir as cinco melhores soluções distintas
def display_best_solutions(solutions):
    unique_solutions = []
    for sol in solutions:
        if sol not in unique_solutions:
            unique_solutions.append(sol)
        if len(unique_solutions) == 5:  # Pegar as cinco primeiras soluções únicas
            break
    
    print("Cinco melhores soluções distintas encontradas:")
    for solution in unique_solutions:
        print(solution)

# Função para calcular média e desvio padrão
def calculate_statistics(generations_list, times):
    avg_generations = np.mean(generations_list)
    std_generations = np.std(generations_list)
    avg_time = np.mean(times)
    std_time = np.std(times)
    
    print(f"Média do número de gerações: {avg_generations:.2f}")
    print(f"Desvio padrão do número de gerações: {std_generations:.2f}")
    print(f"Média do tempo de execução: {avg_time:.4f} segundos")
    print(f"Desvio padrão do tempo de execução: {std_time:.4f} segundos")


# ========================= MAIN ======================================
solutions, generations_list, times = run_multiple_executions()
display_best_solutions(solutions)
calculate_statistics(generations_list, times)
