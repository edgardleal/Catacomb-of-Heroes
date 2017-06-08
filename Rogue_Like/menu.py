# Menu

# IMPORTS
	# Third Party
import pygame
	# My modules

'''

'''
class Menu(object):
	"""docstring for Menu"""
	def __init__(self, width, height):
		super(Menu, self).__init__()
		self.open = False
		self.select = 0

		self.width = width
		self.height = height
		self.color = (255, 255, 255)
		
		self.surface = pygame.Surface((self.width, self.height))
		self.surface.fill((self.color))

class Inventory(Menu):
	"""docstring for Inventory"""
	def __init__(self, width, height):
		super(Inventory, self).__init__(width, height)
