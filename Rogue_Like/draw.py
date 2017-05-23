# ________  ________  ________  ___       __      
# |\   ___ \|\   __  \|\   __  \|\  \     |\  \    
# \ \  \_|\ \ \  \|\  \ \  \|\  \ \  \    \ \  \   
#  \ \  \ \\ \ \   _  _\ \   __  \ \  \  __\ \  \  
#   \ \  \_\\ \ \  \\  \\ \  \ \  \ \  \|\__\_\  \ 
#    \ \_______\ \__\\ _\\ \__\ \__\ \____________\
#     \|_______|\|__|\|__|\|__|\|__|\|____________|

# Imports
import libtcodpy as libtcod
import pygame

from object import *
import constant

class Draw:

	def __init__(self, SURFACE_MAIN, map_to_draw, obj_list, FOV_MAP, CLOCK, messages):

		self.SURFACE_MAIN = SURFACE_MAIN
		self.map_to_draw = map_to_draw
		self.obj_list = obj_list
		self.FOV_MAP = FOV_MAP
		self.CLOCK = CLOCK
		self.messages = messages

	def draw_game(self):

		# Clear the surface
		self.SURFACE_MAIN.fill(constant.COLOR_BG)

		# Draw Map
		self.draw_map()

		# Draw Objects
		for Actor in self.obj_list:
			Actor.obj_draw(self.SURFACE_MAIN, self.FOV_MAP)

		# Draw Text
		self.draw_debug()
		self.draw_messages()
		
		# Update
		pygame.display.flip()

	def draw_map(self):
		for x in range (0, constant.MAP_WIDTH):
			for y in range (0, constant.MAP_HEIGHT):

				is_visible = libtcod.map_is_in_fov(self.FOV_MAP, x, y)

				if is_visible:

					self.map_to_draw[x][y].explored = True

					if self.map_to_draw[x][y].block == True:
						#Draw Wall
						self.SURFACE_MAIN.blit(constant.S_WALL, (x*constant.CELL_WIDTH, y*constant.CELL_HEIGHT))
					else:
						# Draw Floor
						self.SURFACE_MAIN.blit(constant.S_FLOOR, (x*constant.CELL_WIDTH, y*constant.CELL_HEIGHT))

				else:

					if self.map_to_draw[x][y].explored:
						if self.map_to_draw[x][y].block == True:
							#Draw Wall
							self.SURFACE_MAIN.blit(constant.S_WALL_EXPLORED, (x*constant.CELL_WIDTH, y*constant.CELL_HEIGHT))
						else:
							# Draw Floor
							self.SURFACE_MAIN.blit(constant.S_FLOOR_EXPLORED, (x*constant.CELL_WIDTH, y*constant.CELL_HEIGHT))

	def draw_text(self, font, display_surface, text_to_draw, T_coord, color, bg_color = None):

		text_surf, text_rect = self.handle_text(font, text_to_draw, color, bg_color)

		text_rect.topleft = T_coord

		display_surface.blit(text_surf, text_rect)

	def handle_text(self, font, incoming_text, incoming_color, incoming_bg_color):

		if incoming_bg_color:
			text_surface = font.render(incoming_text, False, incoming_color, incoming_bg_color)
		else:
			text_surface = font.render(incoming_text, False, incoming_color)

		return text_surface, text_surface.get_rect()

	def handle_text_height(self, font):

		font_obj = font.render('a', False, constant.COLOR_BLACK)
		font_rect = font_obj.get_rect()

		return font_rect.height

	def draw_debug(self):

		self.draw_text(constant.FONT_DEBUG, self.SURFACE_MAIN, " FPS " + str(int(self.CLOCK.get_fps())) + " ", (0,0), constant.COLOR_WHITE, constant.COLOR_BLACK)

	def draw_messages(self):
		if len(self.messages) <= constant.NUM_MESSAGES:
				to_draw = self.messages
		else:
				to_draw = self.messages[-constant.NUM_MESSAGES:]

		text_height = self.handle_text_height(constant.FONT_MESSAGE)

		start_y = constant.MAP_HEIGHT*constant.CELL_HEIGHT - (constant.NUM_MESSAGES*text_height) - 0

		i = 0

		for message, color in to_draw:
			self.draw_text(constant.FONT_MESSAGE, self.SURFACE_MAIN, (" " + message + " "), (1, start_y+(i*text_height)), color, constant.COLOR_BLACK )
			i += 1