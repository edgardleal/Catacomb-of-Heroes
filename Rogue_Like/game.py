# State

# IMPORTS
	# Third Party
import pygame
	# My modules
import maps
import draw

import controller
import creature
import player
import enemy
import item

import menu
'''

'''
class Game:

	# State Methods
	def __init__(self, Assets, spr_res, clock):
		# State Vars
		self.finished = False
		self.T_key = (0, 0)

		# Self Vars
		self.clock = clock

		self.level = 0

		self.spr_res = spr_res
		self.T_map_res = ([x/spr_res for x in (800,600)]) # For now i'm going to use 800x600
		self.map_width, self.map_height = self.T_map_res
		self.maps = [] # This list of maps is going to keep track of all maps that was made before, if player decides do backtrack

		self.msg_list = []

		# Self Classes
		self.Assets = Assets
		self.Map = maps.Maps()
		self.Draw = draw.Draw_Game(self.spr_res)
		self.Controller = controller.Controller()

		# Init functions
		self.create_map()
		self.game_lists()

		# Menu
		self.I_Menu = menu.Inventory(200, 200)

		# Test
		self.Player = player.Player("Hero", 1, 1, self.Assets.a_player)
		self.append_list(self.Player)

		self.Enemy = enemy.Enemy("Rat", 2, 2, self.Assets.a_enemy)
		self.append_list(self.Enemy)

		self.Item = item.Item("Item 1", 3, 3, self.Assets.s_item)
		self.append_list(self.Item)


		self.Item2 = item.Item("Item 2", 3, 3, self.Assets.s_item)
		self.append_list(self.Item2)


		self.Item3 = item.Item("Item 3", 3, 3, self.Assets.s_item)
		self.append_list(self.Item3)

	def get_input(self, T_key):
		
		self.T_key = T_key

	def update(self):

		self.Controller.logic(self.T_key, self.Player, self.I_Menu,  self.dead_list, self.item_list, self.creature_list, self.msg_list, self.maps[self.level])

		# Last thing to update is the FOV:
		self.Map.update_fov(self.fov_map, self.Player)

	def draw(self, main_surface):

		# This is this state's surface. So I can have multiple surfaces.
		# If I want to have multiple surfaces, in case I want to draw a Menu, or a text box or anything.
		# I can make multiple of theese and play around.
		game_surface = pygame.Surface([800, 600]).convert()
		txt_surf_box = pygame.Surface([800, int(self.Draw.Text.handle_text_height(self.Assets.font_msg) * 3)], pygame.SRCALPHA, 32).convert_alpha()

		# Draw Map:
		self.Draw.maps(self.maps[self.level], self.map_height, self.map_width, self.fov_map, game_surface,
			self.Assets.wall_GFX, self.Assets.e_wall_GFX, self.Assets.floor_GFX, self.Assets.e_floor_GFX)

		# Draw Dead:
		self.Draw.objects(self.dead_list, self.spr_res, game_surface, self.fov_map, self.clock)

		# Draw Itens:
		self.Draw.objects(self.item_list, self.spr_res, game_surface, self.fov_map, self.clock)

		# Draw Creatures:
		self.Draw.objects(self.creature_list, self.spr_res, game_surface, self.fov_map, self.clock)

		# Draw Menu/TextBox:
		self.Draw.text(self.Assets.font_msg, self.msg_list, txt_surf_box)
		self.Draw.menu(game_surface, self.I_Menu, self.Player, self.Assets.font_msg)

		# Draw/Update this surface on screen:

			# Draw Text Surface onto Game Surface:
		game_surface.blit(txt_surf_box, (0,game_surface.get_height()-txt_surf_box.get_height()))

			# Draw Game Surface onto Main Surface:
		main_surface.blit(game_surface, (0,0))

			# Then Display/Update.
		pygame.display.flip()
		pygame.display.update()

	def next_state(self, next_id):
		return next_id

	def end_state(self):
		self.finished = True

	# Self Methods
	def create_map(self):
		map_height, map_width= self.T_map_res
		# self.current_map, self.fov_map = self.Map.create(self.map_height, self.map_width)
		self.current_map, self.fov_map = self.Map.create(self.map_height, self.map_width)
		self.maps.append(self.current_map)


	def game_lists(self):
		self.dead_list = []
		self.item_list = []
		self.creature_list = []

	def append_list(self, obj):
		
		# If the obj i want to append is a creature:
		if isinstance(obj, creature.Creature):

			# If this creature is the Player:
			if isinstance(obj, player.Player):
				self.creature_list.append(obj)

			# If it's not the player and it's alive, it's just a Enemy
			# Since things are drawn from the start of the list to the end
			# And I want the player to be on top of everything,
			# Every new enemy will be added at the first spot on the list, so Player always will be at the end of the list.
			elif obj.is_alive:
				self.creature_list.insert(0, obj)

			else:
				self.dead_list.append(obj)
		elif isinstance(obj, item.Item):
			self.item_list.append(obj)