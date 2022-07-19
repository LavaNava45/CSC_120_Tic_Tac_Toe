def print_board(board):


	for i in range(3):
		print " ",
		for j in range(3):
			if board[i*3+j] == 1:
				print 'X',
			elif board[i*3+j] == 0:
				print 'O',	
			elif board[i*3+j] != -1:
				print board[i*3+j]-1,
			else:
				print ' ',
			
			if j != 2:
				print " | ",
		print
		
		if i != 2:
			print "-----------------"
		else: 
			print 
			
def display():
	print "GO!"
	display_board([2,3,4,5,6,7,8,9,10])


def input(turn):

	valid = False
	while not valid:
		try:
			user = raw_input("Place Number" + turn + " (1-9)? ")
			user = int(user)
			if user >= 1 and user <= 9:
				return user-1
			else:
				print "Please try again.\n"
				display()
		except Exception as e:
			print user + " Please try again.\n"
		
def check_game(board):
	win_cond = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
	for each in win_cond:
		try:
			if board[each[0]-1] == board[each[1]-1] and board[each[1]-1] == board[each[2]-1]:
				return board[each[0]-1]
		except:
			pass
	return -1

def quit(board,msg):
	display_board(board)
	print msg
	quit()

def main():
	
	
	
	display()

	board = []
	for i in range(9):
		board.append(-1)

	win = False
	move = 0
	while not win:

		
		display_board(board)
		print "Turn number " + str(move+1)
		if move % 2 == 0:
			turn = 'X'
		else:
			turn = 'O'

		
		user = input(turn)
		while board[user] != -1:
			print "Invalid move!"
			user = input(turn)
		board[user] = 1 if turn == 'X' else 0

		
		move += 1
		if move > 4:
			winner = check_game(board)
			if winner != -1:
				out = "The winner is " 
				out += "X" if winner == 1 else "O" 
				out += " :)"
				quit(board,out)
			elif move == 9:
				quit(board,"No winner :(")

if __name__ == "__main__":
	main()
