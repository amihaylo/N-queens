import random

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

def row_to_col_representation(board):
    """
    maps a row-based representation of a board to a coumn-based one
    row-based representation:    index=col, value=row
    column-based representation: index=row, value=col

    ex.
      0 1 2 3
    0   Q                 
    1       Q          
    2 Q                 
    3     Q            

    row-based: [2,0,3,1]
    column-based: [1,3,0,2]
    """
    return [tup[0] for tup in sorted([(x,y) for x,y in enumerate(board)], key=lambda x: x[1])]

def print_board(board_row_rep):
    """
    Prints the board in more human readable format
    The function takes in a row-based representatioin of the board [2,0,3,1] (index=col, val=row)
    ex.
      0 1 2 3
    0   Q                 
    1       Q          
    2 Q                 
    3     Q            
    """
    #Get the col-based representation of the board
    board_col_rep = row_to_col_representation(board_row_rep)
    # print(board_row_rep)
    # print(board_col_rep)

    #Create the string that will be the final board
    board_str = ""

    #Create the template string
    str_template = " |"*len(board_col_rep)

    #Create the topmost indices of the board
    board_str += "  " + " ".join(map(str,range(len(board_col_rep))))  + "\n"

    #Create the actual board
    for i in range(len(board_col_rep)):
        queen_i = board_col_rep[i]
        board_str += str(i) +"|" + str_template[:queen_i*2] + "Q" + str_template[queen_i*2+1:] + "\n"

    print(board_str)

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
    rng = random.Random()
    attempts = 1 #The number of attempts it took to find a solution
    potential_sol = list(range(n))

    # while True:
    while True:
        rng.shuffle(potential_sol)
        if is_board_valid(potential_sol):
            return {
                "board":list(potential_sol),
                "attempts":attempts
            }
        attempts+=1        

def run_single_solution(n):
    # Solve the N qeen problem and display the board and # attempts
    print("Running the {} Queen problem...".format(n))
    solution = solve_N_queens(n)
    board = solution["board"]
    num_attempts = solution["attempts"]    
    print_board(board)
    print("Number of attempts made before solving = {}".format(num_attempts))

def run_multiple_solutions(highest_n):
    #Solve the N queen problem for everyting up to and including highest_n
    for curr_n in range(4,highest_n+1):
        solution = solve_N_queens(curr_n)  # Faster
        board = solution["board"]
        num_attempts = solution["attempts"]
        print("{:2}-Queen solved in {:8} attempts".format(curr_n, num_attempts))

if __name__ == "__main__":
    run_single_solution(8)
    run_multiple_solutions(10)
