#!/usr/bin/env python

import sys
import signal
import os
import time
import BOARD,ENEMY,PLAYER
import NonBlockingInput as keyb
import subprocess

#Initialisation

screen=BOARD.draw_board(BOARD.board_height,BOARD.board_width)
mario=PLAYER.mario
mario.set_position()
mario.print_board(BOARD.board_height,BOARD.board_width)
key=keyb.KBHit()
enemy=ENEMY.Bug()
bug=enemy.create_enemy()
ENEMY.Enemies.append(enemy)
initial_time = round(time.time())
enemy_time = round(time.time())
val=4
bgmusic = subprocess.Popen(['xdg-open','./mario_08.wav'])

 # THE GAME

while (PLAYER.life > 0):
	screen.bush_generator()
	screen.pipe_generator()
	screen.brick_generator(BOARD.board_height,BOARD.board_width)
	mario.score()
	if key.kbhit():
		input=key.getch()
	else:
		input='{'
	if(input=='a' or input=='A'):
		mario.update_position(-1)
	elif(input=='d' or input=='D'):
		mario.update_position(1)
	elif(input=='w' or input=='W'):
		do = subprocess.Popen(['mplayer','./smb_jumpsmall.wav'])
		PLAYER.jump=True
	elif(input=='q' or input=='Q'):
		os.killpg(os.getpgid(bgmusic.pid), signal.SIGTERM)
		sys.exit(0)
		os.system('clear')

	mario.jumper()
	if round(time.time()) - initial_time == val:
		initial_time=round(time.time())
		enemy=ENEMY.Bug()
		bug=enemy.create_enemy()
		ENEMY.Enemies.append(enemy)
		val+=1
		if(val==8):
			val=4
	os.system('clear')
	if round(time.time()) - enemy_time==1:
		enemy_time=round(time.time())
		for i in ENEMY.Enemies:
			i.move()
	for i in ENEMY.Enemies:
		i.mario_kill()
		i.kill()
		if(i.y<PLAYER.board_initial-5):
			ENEMY.Enemies.remove(i)
	print("SCORE:: "+str(PLAYER.score))
	print("LIFE:: "+str(PLAYER.life))
	print("KILL:: "+str(ENEMY.kill))
	mario.print_board(BOARD.board_height,BOARD.board_width)
	if(PLAYER.life==0):
		do = subprocess.Popen(['mplayer','./smw_game_over.wav'])
		os.killpg(os.getpgid(bgmusic.pid), signal.SIGTERM)
		os.system('clear')
		print("Game Over")
	if(mario.y==1045):
		os.system('clear')
		os.system('spd-say "YOU WIN\n"')
		print("YOU WIN")
	time.sleep(0.02)
