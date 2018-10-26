   
def share_diag(x0,x1,y0,y1):
    x_delta = abs(x0-y0)
    y_delta = abs(x1-y1)
    return x_delta == y_delta

def next_row_clashes(partial_sol, next_row):
    """
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
    
    Now we try and add another Queen to the next next_col = len(partial_sol)
    Try and place the Queen on (x,y) = (next_col,next_row) and see if it shares
    any diagonals with all previously places queens    
    """
    next_x = len(partial_sol)
    next_y = next_row
    for curr_x, curr_y in enumerate(partial_sol):
        if share_diag(curr_x,curr_y, next_x, next_y):
            return True
    return False

def is_board_valid(board_state):
    #Checks if there are any diagnoal conflicts 
    #Assuming that board_state is all unqiue numbers
    for curr_x in range(1,len(board_state)):
        curr_y = board_state[curr_x]
        if next_row_clashes(board_state[:curr_x],curr_y):            
            return False
    return True


if __name__ == "__main__":
    pass
