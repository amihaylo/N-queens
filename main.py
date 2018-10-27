from board import Board
import random

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
        curr_board = Board(potential_sol)
        if curr_board.is_valid():
            return {
                "board":curr_board,
                "attempts":attempts
            }
        attempts+=1        

def run_single_solution(n):
    # Solve the N qeen problem and display the board and # attempts
    print("Running the {} Queen problem...".format(n))
    solution = solve_N_queens(n)
    board = solution["board"]
    attempts = solution["attempts"]
    print(board)
    print("Number of attempts made before solving = {}".format(attempts))

def run_multiple_solutions(highest_n):
    #Solve the N queen problem for everyting up to and including highest_n
    for curr_n in range(4,highest_n+1):
        solution = solve_N_queens(curr_n)
        board = solution["board"]
        attempts = solution["attempts"]
        print("{:2}-Queen solved in {:8} attempts".format(curr_n, attempts))        

def test():
    pass

if __name__ == "__main__":
    run_single_solution(8)
    print("------------------")
    run_multiple_solutions(10)
