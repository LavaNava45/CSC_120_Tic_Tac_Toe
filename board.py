board = [['_', '_', '_'], 
         print(“ — — — — — — -”)
         ['_', '_', '_'],
         print(“ — — — — — — -”)
         ['_', '_', '_']]

board = create_board() 

def place(board, player, position):
    if board[position] == 0:
       board[position] = player
                                 

board = create_board() 
place(board , 1 , (0,0))

def check_row(row, player):
    for marker in row:
        if marker != player:
            return False
    return True

def row_win(board, player):
    for row in board:
        if check_row(row, player):
            return True
    return False                                                                                        
                                                                                                 
#board is already defined from previous exercises. Call row_win to check if Player 1 has a complete row.

row_win(board, 1)
#------------------------------------------------------------------------------

#Exercise 7
#-----------

#Create a similar function col_win(board, player) that takes the player (integer), 
#and determines if any column consists of only their marker. Have it return True if this condition is met, 
#and False otherwise.
        
def col_win(board, player):
    for row in board.T:
        if check_row(row, player):
            return True
    return False
