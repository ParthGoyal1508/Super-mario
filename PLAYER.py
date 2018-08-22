import BOARD,ENEMY
import time
import subprocess
jump=False
life=3
board_initial=0
score=0


class Player():
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def print_board(self,n_rows,n_cols):
		global board_initial
		if(self.y>=board_initial+80):
			board_initial+=1
		if(self.y<=board_initial+25):
			board_initial-=1
		for i in range(0,n_rows):
			for j in range(board_initial,board_initial+105):
				if(BOARD.board[i][j]=='*'):
					print("\033[1;32;40m"+BOARD.board[i][j], end=' ')
				elif(BOARD.board[i][j]==':'):
					print("\033[0;31;41m"+BOARD.board[i][j], end=' ')
				elif(BOARD.board[i][j]=='C'):
					print("\033[0;46;46m"+BOARD.board[i][j], end=' ')
				elif(BOARD.board[i][j]==']' or BOARD.board[i][j]=='['):
					print("\033[1;33;40m"+BOARD.board[i][j], end=' ')
				elif(BOARD.board[i][j]=='{' or BOARD.board[i][j]=='}'):
					print("\033[1;33;35m"+BOARD.board[i][j], end=' ')
				elif(BOARD.board[i][j]=='0'):
					print("\033[1;33;40m"+BOARD.board[i][j], end=' ')
				elif(BOARD.board[i][j]==' '):
					print("\033[1;32;40m"+BOARD.board[i][j], end=' ')
				elif(BOARD.board[i][j]=='#'):
						print("\033[2;32;43m"+BOARD.board[i][j], end=' ')
				else:
					print(BOARD.board[i][j], end=' ')
			print()

	def set_position(self):
		BOARD.board[self.x][self.y]=']'
		BOARD.board[self.x][self.y+1]='0'
		BOARD.board[self.x][self.y+2]='0'
		BOARD.board[self.x][self.y+3]='['
		BOARD.board[self.x+1][self.y+1]=']'
		BOARD.board[self.x+1][self.y+2]='['

	def remove_prev_mario(self):
		for i in range(0,4):
			BOARD.board[self.x][self.y+i]=' '
		for i in range(1,3):
			BOARD.board[self.x+1][self.y+i]=' '

	def update_position(self,type):
		global score
		if(BOARD.board[self.x+1][self.y]=='0' and type==-1):
			BOARD.board[self.x+1][self.y]==' '
			do = subprocess.Popen(['mplayer','/drive1/sem3/SSAD/Assignment1/mario/smb_coin.wav'])
			score+=1

		if(BOARD.board[self.x+1][self.y+3]=='0' and type==1):
			BOARD.board[self.x+1][self.y+3]==' '
			do = subprocess.Popen(['mplayer','/drive1/sem3/SSAD/Assignment1/mario/smb_coin.wav'])
			score+=1

		if(BOARD.board[self.x][self.y+4]=='0' and type==1):
			BOARD.board[self.x][self.y+4]==' '
			do = subprocess.Popen(['mplayer','/drive1/sem3/SSAD/Assignment1/mario/smb_coin.wav'])
			score+=1

		if(BOARD.board[self.x][self.y-1]=='0' and type==-1):
			BOARD.board[self.x][self.y-1]==' '
			do = subprocess.Popen(['mplayer','/drive1/sem3/SSAD/Assignment1/mario/smb_coin.wav'])
			score+=1


		if((self.y<=1 and type==-1) or (self.y>=BOARD.board_width-6 and type==1) or(BOARD.board[self.x][self.y+4]==':' and type==1) or (BOARD.board[self.x+1][self.y+3]==':' and type==1) or (BOARD.board[self.x][self.y-1]==':' and type==-1) or (BOARD.board[self.x+1][self.y]==':' and type==-1) or (BOARD.board[self.x][self.y+4]=='#' and type==1) or (BOARD.board[self.x][self.y-1]=='#' and type==-1) or (BOARD.board[self.x+1][self.y+3]=='#' and type==1) ):
			self.set_position()
		else:
			self.remove_prev_mario()
			self.y+=type
			self.set_position()

	def jumper(self):
		global jump
		self.remove_prev_mario()
		if(BOARD.board[self.x-1][self.y]==':' or BOARD.board[self.x-1][self.y+1]==':' or BOARD.board[self.x-1][self.y+2]==':' or BOARD.board[self.x-1][self.y+3]==':' ):
			jump=False
		if(jump==True):
			self.x-=1
		if(BOARD.board[self.x+2][self.y+1]==':' or BOARD.board[self.x+2][self.y+2]==':' or BOARD.board[self.x+2][self.y+1]=='#' or BOARD.board[self.x+2][self.y]=='#' or BOARD.board[self.x+2][self.y+3]=='#'):
			jump=False
		if(self.x<=BOARD.board_height-18):
			jump=False
		if(jump==False and self.x<BOARD.board_height-4):
			if(BOARD.board[self.x+2][self.y]==':' or BOARD.board[self.x+2][self.y+1]==':' or BOARD.board[self.x+2][self.y+2]==':' or BOARD.board[self.x+2][self.y+3]==':' or BOARD.board[self.x+1][self.y+3]==':' or BOARD.board[self.x+1][self.y]==':'  or BOARD.board[self.x+2][self.y+1]=='#' or BOARD.board[self.x+2][self.y]=='#' or BOARD.board[self.x+2][self.y+3]=='#'):
				self.x=self.x
			else:
				self.x+=1
		self.set_position()

	def score(self):
		global score
		if(BOARD.board[self.x+2][self.y]=='0' and BOARD.board[self.x+2][self.y]==':'):
			do = subprocess.Popen(['mplayer','/drive1/sem3/SSAD/Assignment1/mario/smb_coin.wav'])
			score+=1
			BOARD.board[self.x+2][self.y]=' '
		if(BOARD.board[self.x+1][self.y]=='0' and BOARD.board[self.x+1][self.y]==':'):
			do = subprocess.Popen(['mplayer','/drive1/sem3/SSAD/Assignment1/mario/smb_coin.wav'])
			score+=1
			BOARD.board[self.x+1][self.y]=' '
		if(BOARD.board[self.x+1][self.y+3]=='0' and BOARD.board[self.x+1][self.y+3]==':'):
			do = subprocess.Popen(['mplayer','/drive1/sem3/SSAD/Assignment1/mario/smb_coin.wav'])
			score+=1
			BOARD.board[self.x+1][self.y+3]=' '
		if(BOARD.board[self.x+2][self.y+1]=='0' and BOARD.board[self.x+3][self.y+1]==':'):
			do = subprocess.Popen(['mplayer','/drive1/sem3/SSAD/Assignment1/mario/smb_coin.wav'])
			score+=1
			BOARD.board[self.x+2][self.y+1]=' '
		if(BOARD.board[self.x+2][self.y+2]=='0' and BOARD.board[self.x+3][self.y+2]==':'):
			do = subprocess.Popen(['mplayer','/drive1/sem3/SSAD/Assignment1/mario/smb_coin.wav'])
			score+=1
			BOARD.board[self.x+2][self.y+2]=' '
		if(BOARD.board[self.x+2][self.y+3]=='0' and BOARD.board[self.x+2][self.y+3]==':'):
			do = subprocess.Popen(['mplayer','/drive1/sem3/SSAD/Assignment1/mario/smb_coin.wav'])
			score+=1
			BOARD.board[self.x+2][self.y+3]=' '

mario=Player(BOARD.board_height-4,25)
