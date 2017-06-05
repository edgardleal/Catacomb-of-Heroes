# Manager

# IMPORTS
	# Third Party
import pygame	

	# My modules
import window
import io
import assets

import main_menu


import game
'''

'''
class Manager:

	def __init__(self):
		# Resoultions
		self.win_height = 800 
		self.win_width = 600
		self.T_win_res = (self.win_height, self.win_width)
		self.spr_res = 32

		# Clock and Frame per second.
		self.clock = pygame.time.Clock()
		self.fps = 60

		# Basic
		self.Window = window.Window(self.T_win_res)
		self.IO = io.IO()
		self.Assets = assets.Assets()

		# States
		'''
		And then you're going to read the states files and you're going to think: 
		"Hey, why this dude didn't make a abstract state class and then make it parent of theese?"
		I didn't quite understand how abstract classes work in python so i made this way, judge me.
		'''
		self.Main_Menu = main_menu.Main_Menu()


		self.Game = game.Game(self.Assets, self.spr_res, self.clock)
		
		# Game Loop
		self.game_loop()

	def states(self, state):

		# Return:
		# -1 - Loading - if i manage to learn how to do it
		# 0 - Slpash 
		# 1 - Intro
		# 2 - Main Menu
		if state == 2:
			return self.Main_Menu
		# 3 - Options
		# 4 - New Game
		elif state == 4:
			return self.Game
		# 5- Load Game
		pass

	def game_loop(self):

		state_id = 4

		while True:

			current_state = self.states(state_id)

			# Current State gets input
			current_state.get_input(self.IO.handle_input())

			# Do it's logic
			current_state.update()

			# Tells draw what to draw
			# I like the idea of having multiple layers when drawing. 
			# So I'm going to pass the first layer, as an argument
			# That way I can play with it drawing multiple surfaces on it
			current_state.draw(self.Window.surface) 

			# Clocks the FPS
			self.clock.tick(self.fps)

			# whenever current state is finished it needs to tell what it's the next state.
			if current_state.finished:
				state_id = current_state.next_state()