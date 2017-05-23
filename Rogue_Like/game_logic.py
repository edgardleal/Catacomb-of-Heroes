#  ________  ________  _____ ______   _______      
# |\   ____\|\   __  \|\   _ \  _   \|\  ___ \     
# \ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|    
#  \ \  \  __\ \   __  \ \  \\|__| \  \ \  \_|/__  
#   \ \  \|\  \ \  \ \  \ \  \    \ \  \ \  \_|\ \ 
#    \ \_______\ \__\ \__\ \__\    \ \__\ \_______\
#     \|_______|\|__|\|__|\|__|     \|__|\|_______|
#

# Imports
import tcod as libtcod
import pygame

import constant
from draw import Draw
from map_gen import Map
from object import *
from player import *
from components import *
from spritesheet import *

class Game:

	obj_list = [] # List of objects of the game. Everything is a object.
	msg_list = [] # List of Messages

	A_PLAYER = []

	def __init__(self, SURFACE_MAIN, CLOCK):
		self.SURFACE_MAIN = SURFACE_MAIN # THIS POINTS TO THE SURFACE CREATED ON WINDOW.PY AWESOME
		self.CLOCK = CLOCK
		self.game_init()
		self.game_main_loop()

	# Probably a temp function
	# This function inits Actors.
	def init_Actors(self):
		# Create Player
		hero_com = com_Creature("HERO")
		self.p = Player(self.CLOCK, "Player", 1, 1, self.A_PLAYER, creature = hero_com)
		self.p.hero_class(2)

		# Create Enemy
		rat_com = com_Creature("Rat", def_death = death_monster)
		ai_com = com_AI()
		self.e = Actor(self.CLOCK, "Rat", 15, 15, self.A_ENEMY, creature = rat_com, ai = ai_com)

		# Add Objects into list
		self.obj_list.append(self.e)

		# Player needs to be the last on the list, so the game draws him on top.
		self.obj_list.append(self.p)

	# Set up pygame and pygame window

	def game_init(self):

		# Creating the map
		self.m = Map()
		self.current_map = self.m.map_create()

		# Load SpriteSheet
		self.init_gfx()

		# Since everything is a pointer, I can create this class with every variable it needs, and them, just call methods.
		self.d = Draw(self.SURFACE_MAIN, self.current_map, self.obj_list, self.m.FOV_MAP, self.CLOCK, self.msg_list) # Draw class

		self.init_Actors()

	def init_gfx(self):
		self.s = Spritesheet("GFX/Player_SS.png")
		# self.A_PLAYER = self.s.get_image(1, 3, 16, 16, (32,32)) # Knight
		# self.A_PLAYER = self.s.get_image(2, 5, 16, 16, (32,32)) # Herald
		self.A_PLAYER = self.s.get_animation(0, 0, 2, 16, 16, (32,32)) # Scholar

		self.s_e = Spritesheet("GFX/Enemy_SS.png")
		self.A_ENEMY = self.s_e.get_animation(0, 0, 2, 16, 16, (32,32))

		self.s_wf = Spritesheet("GFX/Wall_Floor_SS.png")
		constant.S_WALL = self.s_wf.get_image(0, 0, 16, 16, (32,32))[0]
		constant.S_WALL_EXPLORED = self.s_wf.get_image(1, 0, 16, 16, (32,32))[0]

		constant.S_FLOOR = self.s_wf.get_image(0, 1, 16, 16, (32,32))[0]
		constant.S_FLOOR_EXPLORED = self.s_wf.get_image(1, 1, 16, 16, (32,32))[0]
		

	def game_main_loop(self):

		while True:

			# Get Input
			event_list = pygame.event.get()

			# Quit Game
			self.quit_input(event_list)

			# Handle inputs in a Turn Basead System
			self.turn_system(event_list, self.obj_list)


			# Draw
			self.d.draw_game()
			self.CLOCK.tick(constant.GAME_FPS)

	# Quit the game
	def quit_input (self, event_list):
		for event in event_list:
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

	# GAME LOGIC of the Turns
	def turn_system(self, event_list, obj_list):

		# If player actions are less than a full turn, he can act again
		if self.p.turn < constant.TURN_VALUE:

				# Handle the input
				self.p.handle_input(self.current_map, event_list, self.obj_list)

				#self.game_messages(self.p.creature.battle_message, constant.COLOR_WHITE)

				#Calculate the FOV
				self.FOV_CALC = self.m.map_calculate_fov(self.p)
				
		else:
			# Is enemy turn.

			# TODO A way of enemy move/attack slowly when player is heavy.
			for enemy in self.obj_list:
				if enemy.ai:
					enemy.ai.take_turn(self.current_map, self.obj_list)
					# if self.p.turn > constant.TURN_VALUE:
					# 	pygame.time.wait(300)
			self.p.turn -= constant.TURN_VALUE


	@staticmethod 
	def game_messages(game_msg, msg_color):

		Game.msg_list.append((game_msg, msg_color))
