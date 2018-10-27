class Board:
    """A Chess board with a bunch of queens on it"""

    def __init__(self, row_rep):
        """
        Creates a new board using a row-based representation method
        Numbers should all be unique for the queen problem
        row-based representation: index=col, value=row
        col-based representation: index=row, value = col
        """
        self.row_rep = row_rep
        self.col_rep = self.row_to_col_representation()
        self.size = len(row_rep)
        
    def row_to_col_representation(self):
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
        return [tup[0] for tup in sorted([(x,y) for x,y in enumerate(self.row_rep)], key=lambda x: x[1])]

    def share_diag(self,x0,x1,y0,y1):
        x_delta = abs(x0-y0)
        y_delta = abs(x1-y1)
        return x_delta == y_delta    
    
    def is_col_valid(self,col):
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
        suspect_y = self.row_rep[col]
        for i in range(col):
            curr_x = i
            curr_y = self.row_rep[i]
            if self.share_diag(curr_x, curr_y, suspect_x, suspect_y):
                return False
        return True

    def is_valid(self):
        #Checks if there are any diagnoal conflicts 
        #Assuming that board_state is all unqiue numbers
        for curr_x in range(1,self.size):
            if not self.is_col_valid(curr_x):
                return False
        return True

    def __str__(self):
        #Create the string that will be the final board
        board_str = ""

        #Create the template string
        str_template = " |"*len(self.col_rep)

        #Create the topmost indices of the board
        board_str += "  " + " ".join(map(str,range(len(self.col_rep))))  + "\n"

        #Create the actual board
        for i in range(self.size):
            queen_i = self.col_rep[i]
            board_str += str(i) +"|" + str_template[:queen_i*2] + "Q" + str_template[queen_i*2+1:]
            #The last line should not have a newline
            if i != self.size-1:
                board_str += "\n"

        return board_str
