def create_board():
    return np.zeros ((3,3))

board = create_board() 

def place(board, player, position):
    if board[position] == 0:
       board[position] = player
                                 

board = create_board() 
place(board , 1 , (0,0))
