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
		self.width = width
		self.height = height
		self.surface = pygame.Surface((self.width, self.height))
		self.color = (255, 255, 255)
		self.surface.fill((self.color))

class Inventory(Menu):
	"""docstring for Inventory"""
	def __init__(self, width, height):
		super(Inventory, self).__init__(width, height)
		self.item_list = []

	def i_list(self, creature):

		color = (0, 0, 0)
		if not creature.Container.used_slots == 0:
			for item in creature.Container.inventory:
				self.item_list.append((item.name_object, color))

		
