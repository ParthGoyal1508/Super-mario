board_width=1050
board_height=47
board = [[' ' for x in range(board_width)] for y in range(board_height)]
class draw_board():
	def __init__(self,n_rows,n_cols):
		for i in range(0,n_cols):
			board[0][i]='*'
			board[n_rows-1][i]="*"
			board[n_rows-2][i]="*"
		for i in range(0,n_cols):
			for j in range(0,n_rows-3):
					board[j+1][i]=' '

		for k in range(0,1033,60):
			for i in range(5,7):
				for j in range(8,16):
					board[i][k+j]='C'
			for i in range(4,8):
				for j in range(10,14):
					board[i][k+j]='C'

		for k in range(30,1033,60):
			for i in range(8,10):
				for j in range(8,16):
					board[i][k+j]='C'
			for i in range(7,11):
				for j in range(10,14):
					board[i][k+j]='C'

		for i in range(30,1050,50):
			for j in range(0,4):
				board[n_rows-10][i+j]='0'

	def brick_generator(self,n_rows,n_cols):
		for i in range(5,1050,50):
			for j in range(0,4):
				board[n_rows-5][i+j]=':'

		for i in range(30,1050,50):
			for j in range(0,4):
				board[n_rows-9][i+j]=':'

	def bush_generator(self):
		for j in range(0,1033,60):
			for i in range(14,18):
				board[40][i+j]="_"
			board[41][13+j]="/"
			board[42][12+j]="/"
			board[43][11+j]="/"
			board[44][10+j]="/"
			board[41][18+j]="\\"
			board[42][19+j]="\\"
			board[43][20+j]="\\"
			board[44][21+j]="\\"

	def pipe_generator(self):
		for k in range(0,1033,180):
			for i in range(38,45):
				for j in range(38,43):
					board[i][j+k]="#"
			for i in range(38,45):
				for j in range(90,97):
					board[i][j+k]="#"

	
