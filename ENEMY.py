import sys
import os
from PERSON import Person
import BOARD,PLAYER
import os
import subprocess
Enemies=[]
kill=0

class Bug(Person):
	def __init__(self):
		Person.__init__(self,43,PLAYER.board_initial+110)
		self.var=3

	def create_enemy(self):
		for i in range(0,2):
			BOARD.board[self.x][self.y+i]='0'
		BOARD.board[self.x+1][self.y]='}'
		BOARD.board[self.x+1][self.y+1]='{'

	def __remove_enemy(self):
		for i in range(0,2):
			for j in range(0,2):
				BOARD.board[self.x+i][self.y+j]=' '

	def move(self):
		self.__remove_enemy()
		if(BOARD.board[self.x][self.y-1]=='#' or BOARD.board[self.x][self.y+1]=='#'):
			self.var=self.var*(-1)
		self.y-=self.var
		self.create_enemy()

	def mario_kill(self):
		if BOARD.board[self.x][self.y-2]=='0' and BOARD.board[self.x][self.y-3]=='0' and BOARD.board[self.x+1][self.y-2]=='[' and BOARD.board[self.x+1][self.y-3]==']' :
			self.__remove_enemy()
			Enemies.remove(self)
			PLAYER.life-=1
			os.system('spd-say "MARIO DIED\n"')
			PLAYER.mario.remove_prev_mario()
			PLAYER.mario.y-=80
			if(BOARD.board[PLAYER.mario.x][PLAYER.mario.y-1]=="#"):
				PLAYER.mario.y-=8

		elif  BOARD.board[self.x][self.y+2]=='0' and BOARD.board[self.x][self.y+3]=='0' and BOARD.board[self.x+1][self.y+2]==']'and BOARD.board[self.x+1][self.y+3]=='[':
			self.__remove_enemy()
			Enemies.remove(self)
			PLAYER.life-=1
			os.system('spd-say "MARIO DIED\n"')
			PLAYER.mario.remove_prev_mario()
			PLAYER.mario.y-=80
			if(BOARD.board[PLAYER.mario.x][PLAYER.mario.y-1]=="#"):
				PLAYER.mario.y-=8

	def kill(self):
		global kill
		if(BOARD.board[self.x-1][self.y]==']' or BOARD.board[self.x-1][self.y]=='[' or BOARD.board[self.x-1][self.y+1]==']' or BOARD.board[self.x-1][self.y+1]=='[' ):
			self.__remove_enemy()
			Enemies.remove(self)
			PLAYER.score+=5
			kill+=1
