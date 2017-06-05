# Assets

# IMPORTS
	# Third Party
import pygame

	# My Modules
from spritesheet import *

'''

'''
class Assets:

	def __init__(self):

		self.load_fonts()

		self.load_sprites()

		self.load_animations()

		print "Loading done!"

	def load_fonts(self):
		self.font_debug = pygame.font.Font("Assets/FONTS/Pixeled.ttf", 8)
		self.font_msg = pygame.font.Font("Assets/FONTS/Pixeled.ttf", 8)

	def load_sprites(self):

		self.struct_ss = Spritesheet("Assets/GFX/Wall_Floor_SS.png")
		
		self.wall_GFX = self.struct_ss.get_image(0, 0, 16, 16, (32,32))[0]
		self.e_wall_GFX = self.struct_ss.get_image(1, 0, 16, 16, (32,32))[0]

		self.floor_GFX = self.struct_ss.get_image(0, 1, 16, 16, (32,32))[0]
		self.e_floor_GFX = self.struct_ss.get_image(1, 1, 16, 16, (32,32))[0]

		self.item_ss = Spritesheet("Assets/GFX/Flesh.png")
		self.S_ITEM = self.item_ss.get_animation(0, 1, 1, 16, 16, (32,32))

	def load_animations(self):

		self.player_ss = Spritesheet("Assets/GFX/Player_SS.png")
		self.a_player = self.player_ss.get_animation(0, 2, 2, 16, 16, (32,32))

		self.enemy_ss = Spritesheet("Assets/GFX/Enemy_SS.png")
		self.a_enemy = self.enemy_ss.get_animation(0, 0, 2, 16, 16, (32,32))