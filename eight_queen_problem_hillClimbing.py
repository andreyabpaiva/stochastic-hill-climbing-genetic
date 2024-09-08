import random


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
    """

    state = [random.randint(0, 7) for _ in range(8)] # Initial Solution
    current_collisions = calculate_collisions(state) # Initial Collisions count
    no_improvement = 0 # No Improvements Count

    while no_improvement < max_no_improve:
        col = random.randint(0, 7)
        min_collisions = current_collisions
        best_state = state[:]

        for row in range(8):
            if state[col] == row: # Verify if the queen is already in this row
                continue
            new_state = state[:]
            new_state[col] = row
            new_collisions = calculate_collisions(new_state)
            if new_collisions < min_collisions:
                min_collisions = new_collisions
                best_state = new_state
        
        if min_collisions < current_collisions: # There is a improvement
            state = best_state
            current_collisions = min_collisions
            no_improvement = 0
        else: 
            no_improvement += 1
        

    return state, current_collisions

