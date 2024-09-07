def calculate_colisions(state: list) -> int:
    """
    Compute the number of colisions beetween queens in the board

    args:
        list: list of queen positions

    returns:
        int: number of colisions
    """
    colisions = 0
    for queen_target_column in range(len(state) // 2):

        queen = {
            "column": queen_target_column,
            "row": state[queen_target_column]
        } # Queen position

        for column, row in enumerate(state):
            if column == queen_target_column:
                continue
            if (column - row == queen["column"] - queen["row"]) or (row + column == queen["column"] + queen["row"]):
                colisions += 1
        
    return colisions


state = [0, 1, 2, 3, 4, 5, 6, 7]

number_of_colisions = calculate_colisions(state)
print(number_of_colisions)
