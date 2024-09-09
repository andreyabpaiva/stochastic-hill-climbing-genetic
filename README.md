## Resolvendo o problema das Oito Rainhas com Stochastic Hill Climbing

1. Implementação do código em [`eight_queen_problem_hillClimbing.py`](https://github.com/andreyabpaiva/stochastic-hill-climbing-genetic/blob/main/eight_queen_problem_hillClimbing.py)
2. Fluxograma
  ```mermaid
  ```
3. Resultado da execução em
   
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
   

**Tasks**
- [ ] Stochastic Hill Climbing;
  - [x] Implementar o algoritmo 
  - [ ] Fazer fluxograma do Stochastic Hill [progress]
  - [x] Análise estatística
- [ ] Implementar o algoritmo genético para resolver o problema das Sete Rainhas.
  - [x] Implementar o algoritmo 
  - [ ] Fazer fluxograma da implementação genética [progress]
  - [x] Análise estatística

**Fluxograma 2**
```mermaid
```
#
Alunos: 
`Andreya Paiva`
`Andrey Oliveira`
`Alexandre Moraes`
