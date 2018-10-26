import itertools

def share_diag(x0,x1,y0,y1):
    x_delta = abs(x0-y0)
    y_delta = abs(x1-y1)
    return x_delta == y_delta

def is_col_valid(partial_sol, col):
    """
    Checks if the given col has any diag. violations with all previous
    queens 0,1,2..col-1 columns
    Assume: all values in partial_sol are unique

    @param partial_sol[list]: A list representing a partial solution
    @param col[int]: The column in question

    @return True: if the column is valid
    @return False: if there is a violation (diag)

    ex.
      0 1 2 3 4 5 6 7
    0       Q            
    1                 
    2     Q            
    3                 
    4   Q              
    5         Q        
    6 Q               
    7                 
    = [6,4,2,0,5] = partial_sol
    Check col = 4 (the 5 above) => True    
    """     
    suspect_x = col
    suspect_y = partial_sol[col]
    for i in range(col):
        curr_x = i
        curr_y = partial_sol[i]
        if share_diag(curr_x, curr_y, suspect_x, suspect_y):
            return False
    return True

def is_board_valid(board_state):
    #Checks if there are any diagnoal conflicts 
    #Assuming that board_state is all unqiue numbers
    for curr_x in range(1,len(board_state)):
        if not is_col_valid(board_state, curr_x):
            return False
    return True

def solve_N_queens(n):
    """
    Given n solve the N-queens problem
    How to place N queens on an NxN grid 
    without any of them sharing the same
    vertical, horizontal, and diagonal space

    @return: the solution
    @return: the # of attempts it took to achieve that solution
    """
    #Init
    attempts = 1 #The number of attempts it took to find a solution
    solution = list(range(n))
    permutations = itertools.permutations(solution)

    # while True:
    for potential_sol in permutations:
        # print(list(potential_sol))
        if is_board_valid(potential_sol):
            return {
                "solution":potential_sol,
                "attempts":attempts
            }
        attempts+=1

if __name__ == "__main__":
    print(solve_N_queens(8))
