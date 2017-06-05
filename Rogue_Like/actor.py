# Actor

# IMPORTS
	# Third Party
import pygame
try:
	import tcod as libtcod
except:
	import libtcodpy as libtcod

	# My Modules

'''
Actor is going to be the generic class of the game.
Every single thing that has position (x, y), has a sprite and player can "interACT" is going to be an actor
'''
class Actor(object):

	def __init__(self, name_object, x, y, animation):

		# What I think that is required to this class
		self.name_object = name_object
		self.animation = animation

		self.x = x
		self.y = y

		# What I want to move away somewhere else:
		self.sprite_image = 0
		self.flicker_timer = 0.0