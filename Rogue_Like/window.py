# Handle Window

# IMPORTS
	# Third Party
import pygame

	# My modules

'''

'''
class Window:

	# Init of the Window.
	def __init__(self, T_res):
		self.win_init(T_res)
		pygame.init()
		pygame.display.set_caption(self.name)
		# pygame.display.set_icon(WIN_ICON)

	def win_init(self, T_res):
		# Window Vars
		self.name = "Catacombs of Heroes"
		# WIN_ICON = 

		# Window's Main Surface
		self.surface = pygame.display.set_mode(T_res)

		# Window Default color in that surface
		self.bg_color = (0, 0, 0)

	# Exit the game
	@staticmethod
	def win_close():
		pygame.quit()
		exit()