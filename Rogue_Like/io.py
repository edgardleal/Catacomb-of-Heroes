# Handle inputs

# IMPORTS
	# Third Party
import pygame

	# My Modules
from window import *

'''

'''
class IO:

	def __init__(self):

		# This are going to be the default key variables.
		# I believe that is the only way to have a proper "set keys" option is to have them this way.
		self.K_UP = pygame.K_UP
		self.K_DOWN = pygame.K_DOWN
		self.K_LEFT = pygame.K_LEFT
		self.K_RIGHT = pygame.K_RIGHT

		self.K_OK = pygame.K_RETURN
		self.K_NG = pygame.K_ESCAPE

		pygame.key.set_repeat(200, 70)

	def handle_input(self):


		
		for event in self.get_events():
			if event.type == pygame.QUIT:
				Window.win_close()
			if event.type == pygame.KEYDOWN:
				return self.game_input(event)

	def get_events(self):
		event_list = pygame.event.get()
		return event_list

	def game_input(self, event):

		# Pygame surfaces start at top-left as (0, 0) and ends in the bottom right.
		# That's why UP and LEFT are negative.

		T_key = None


		# UP/DOWN
		if event.key == self.K_UP:			
			T_key = (0, -1)
		if event.key == self.K_DOWN:
			T_key = (0, 1)

		#LEFT/RIGHT
		if event.key == self.K_LEFT:
			T_key = (-1, 0)
		if event.key == self.K_RIGHT:
			T_key = (1, 0)

		# Confirm
		if event.key == self.K_OK:
			T_key = ("OK", 0)
		# Deny
		if event.key == self.K_NG:
			T_key = ("NG", 0)

		return T_key
	
