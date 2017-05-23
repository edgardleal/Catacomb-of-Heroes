#  ___       __   ___  ________   ________  ________  ___       __      
# |\  \     |\  \|\  \|\   ___  \|\   ___ \|\   __  \|\  \     |\  \    
# \ \  \    \ \  \ \  \ \  \\ \  \ \  \_|\ \ \  \|\  \ \  \    \ \  \   
#  \ \  \  __\ \  \ \  \ \  \\ \  \ \  \ \\ \ \  \\\  \ \  \  __\ \  \  
#   \ \  \|\__\_\  \ \  \ \  \\ \  \ \  \_\\ \ \  \\\  \ \  \|\__\_\  \ 
#    \ \____________\ \__\ \__\\ \__\ \_______\ \_______\ \____________\
#     \|____________|\|__|\|__| \|__|\|_______|\|_______|\|____________|


# EVERY VARIABLE IS A POINTER IN PYTHON.
import pygame

import constant
from game_logic import *

class Window:

	def __init__(self):
		self.win()
		myGame = Game(self.win_surface, self.clock)

	def win(self):
		pygame.init()
		pygame.display.set_caption(constant.WINDOW_NAME)
		# pygame.display.set_icon(constant.WINDOW_ICON)

		self.win_surface = pygame.display.set_mode((constant.GAME_WIDTH, constant.GAME_HEIGHT))
		self.clock = pygame.time.Clock()

