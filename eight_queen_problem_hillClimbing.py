import random
import time
import numpy as np
import pandas as pd
import os


def calculate_collisions(state: list) -> int:
    """
    Compute the number of collisions beetween queens in the board

    args:
        list: list of queen positions

    returns:
        int: number of collisions
    """
    collisions = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                collisions += 1
        
    return collisions


def stochastic_hill_climbing(max_no_improve: int = 500) -> tuple:
    """
        Implementation of the Stochastic Hill Climbing algorithm for the 8 queen problem

        args:
            int: max number of iterations
        
        returns:
            tuple: (list: final state reached, int: number of colisions of the final state, int: number of iterations until the final state)
    """

    state = [random.randint(0, 7) for _ in range(8)] # Initial Solution
    current_collisions = calculate_collisions(state) # Initial Collisions count
    no_improvement = 0 # No Improvements Count
    iterations = 0

    while no_improvement < max_no_improve:
        iterations += 1
        # Choose a random column to modify
        col = random.randint(0, 7)
        best_state = state[:]
        min_collisions = current_collisions

        for row in range(8):
            if state[col] == row: # Verify if the queen is already in this row
                continue
            new_state = state[:]
            new_state[col] = row
            new_collisions = calculate_collisions(new_state)
            # print(best_state, min_collisions, new_state, new_collisions)
            if new_collisions < min_collisions:
                min_collisions = new_collisions
                best_state = new_state
        
        if min_collisions < current_collisions: # There is a improvement
            state = best_state
            current_collisions = min_collisions
            no_improvement = 0
        else: 
            no_improvement += 1
        

    return state, current_collisions, iterations


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
    results_data = []
    best_solutions_data = []

    for i in range(num_experiments):
        if i % 10 == 0:
            print('.')
        start_time = time.time()
        result, collisions, number_of_iterations = stochastic_hill_climbing()
        end_time = time.time()

        execuion_time = end_time - start_time

        executions_times.append(execuion_time)
        iterations.append(number_of_iterations)
        if collisions == 0 and result not in best_solutions:
            best_solutions.append(result)

        mean_iterations = np.mean(iterations)
        std_iterations = np.std(iterations)
        mean_time = np.mean(executions_times)
        std_time = np.std(executions_times)

        # Saves the data
        data = {
            'Experiment': i + 1,
            'Final State': result,
            'Collisions': collisions,
            'Iterations': number_of_iterations,
            'Execution Time': execuion_time
        }

        results_data.append(data)

        if collisions == 0 and result not in best_solutions_data:
            best_solutions_data.append(data)

    directory = 'hill_climbing_results'

    # Cria o diretório, se ele não existir
    os.makedirs(directory, exist_ok=True)

    df = pd.DataFrame(results_data)
    df.to_csv('hill_climbing_results/stochastic_hill_climbing_results.csv', index=False)

    df_solutions = pd.DataFrame(best_solutions_data)
    df_solutions.to_csv('hill_climbing_results/stochastic_hill_climbing_unique_solutions.csv', index=False)

    return mean_iterations, std_iterations, mean_time, std_time, best_solutions

# Run experiments and display the results
mean_iters, std_iters, mean_time, std_time, best_solutions = run_experiments()
print(f"Average Iterations: {mean_iters}, Standard Deviation: {std_iters:.4f}")
print(f"Average Execution Time: {mean_time:.4f} seconds, Standard Deviation: {std_time:.4f} seconds")
print(f"Top Distinct Solutions Found: {best_solutions[:5]}")
