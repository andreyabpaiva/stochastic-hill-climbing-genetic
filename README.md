## Resolvendo o problema das Oito Rainhas 
### Com Stochastic Hill Climbing

1. Implementação do código em [`eight_queen_problem_hillClimbing.py`](https://github.com/andreyabpaiva/stochastic-hill-climbing-genetic/blob/main/eight_queen_problem_hillClimbing.py)
2. Fluxograma
  ```mermaid
  graph LR
      A[INÍCIO: COM ESTADO S0] --> B[GERA UM SUCESSOR ALEATÓRIO S' A PARTIR  DE S ATUAL]
      B --> C[s' AVALIA O VALOR DA FUNÇÃO OBJETIVO PARA S']
      C --> D{QUAL FUNÇÃO OBJETIVO É MELHOR? S OU S'?}
      D --> E[SUBSTITUI S POR S']
      D -->F[MANTÉM S ATUAL]
      E --> G{CRITÉRIO DE PARADA ATINGIDO?}
      F --> G
      G -->|SIM| H[FIM: RETORNA ATUAL SOLUÇÃO]
      G --> |NÃO|B
  ```
3. Resultado da execução e cinco melhores resultados 
   
   ```python
   def run_experiments(num_experiments: int = 50) -> tuple:
    """
    Executes the algorithm 50 times and computes statistical references

    args: 
        number of experiments to be executed

    return:
        (float: mean of the number iterations, float: standart deviation of the number of iterations, float: mean of the time of executions of the function, float: standart deviation of the number of executions of the function)
    """

    iterations = []
    executions_times = []
    best_solutions = []

    for i in range(num_experiments):
        if i % 10 == 0:
            print('.')
        start_time = time.time()
        result, collisions, number_of_iterations = stochastic_hill_climbing()
        end_time = time.time()

        executions_times.append(end_time - start_time)
        iterations.append(number_of_iterations)
        if collisions == 0 and result not in best_solutions:
            best_solutions.append(result)

        mean_iterations = np.mean(iterations)
        std_iterations = np.std(iterations)
        mean_time = np.mean(executions_times)
        std_time = np.std(executions_times)


    return mean_iterations, std_iterations, mean_time, std_time, best_solutions
   ```
### Com algoritmo genético
1. Implementação do código em [`eight_queen_problem_genetic.py`](https://github.com/andreyabpaiva/stochastic-hill-climbing-genetic/blob/main/eight_queen_problem_genetic.py)
2. Fluxograma
  ```mermaid
  flowchart LR
      A[INÍCIO] -->B[INICIAR POPULAÇÃO]
      B --> C[CALCULA FITNESS DA POPULAÇÃO]
  
      D[MUTAÇÃO 3% - BIT FLIP] --> E[SELECIONAR SOBREVIVENTES - ELITISMO] 
      E-->C
      C--> F{VERIFICAR SE O CRITÉRIO DE PARADA FOI ATINGIDO}
      F-->|NÃO| G[SELEÇÃO DOS PAIS - ESTRATÉGIA DE ROLETA]
      G-->H[CRUZAMENTO - PONTO DE CORTE]
      H-->D
      F--> |SIM| I[FIM]
  ```
3. Resultado da execução
   
   ```python
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
        
        # print(f"Tentativa {i+1}:")
        # print(f"Solução: {queens_solution}")
        # if generations < 1000:
        #     print(f"Solução ótima encontrada em {generations} gerações.")
        # else:
        #     print("Solução ótima não encontrada. Melhor solução após 1000 gerações.")
        # print(f"Tempo de execução: {time_taken:.4f} segundos\n")
    
    return solutions, generations_list, times
   ```
4. Média e Desvio Padrão
   ```python
   def calculate_statistics(generations_list, times):
    avg_generations = np.mean(generations_list)
    std_generations = np.std(generations_list)
    avg_time = np.mean(times)
    std_time = np.std(times)
    
    print(f"Média do número de gerações: {avg_generations:.2f}")
    print(f"Desvio padrão do número de gerações: {std_generations:.2f}")
    print(f"Média do tempo de execução: {avg_time:.4f} segundos")
    print(f"Desvio padrão do tempo de execução: {std_time:.4f} segundos")
   ```

6. Cinco melhores resultados
   ```python
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
   ```



#
Alunos: 
`Andreya Paiva`
`Andrey Oliveira`
`Alexandre Moraes`
