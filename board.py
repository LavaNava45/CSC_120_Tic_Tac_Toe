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
