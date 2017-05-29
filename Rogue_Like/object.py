#  ________  ________        ___  _______   ________ _________
# |\   __  \|\   __  \      |\  \|\  ___ \ |\   ____\\___   ___\
# \ \  \|\  \ \  \|\ /_     \ \  \ \   __/|\ \  \___\|___ \  \_|
#  \ \  \\\  \ \   __  \  __ \ \  \ \  \_|/_\ \  \       \ \  \
#   \ \  \\\  \ \  \|\  \|\  \\_\  \ \  \_|\ \ \  \____   \ \  \
#    \ \_______\ \_______\ \________\ \_______\ \_______\  \ \__\
#     \|_______|\|_______|\|________|\|_______|\|_______|   \|__|

try:
    import tcod as libtcod
except:
    import libtcodpy as libtcod

import pygame

import constant


class Actor:

	def __init__(self, CLOCK, name_object, x, y, animation, animation_speed = .5, creature = None, ai = None):

		self.CLOCK = CLOCK

		self.name_object = name_object
		self.x = x
		self.y = y

		self.animation = animation
		self.animation_speed = animation_speed # in seconds

		self.flick_speed = self.animation_speed / len(self.animation)
		self.flick_timer = 0.0
		self.sprite_image = 0

		self.creature = creature
		if creature:
			creature.owner = self

		self.ai = ai
		if ai:
			ai.owner = self

	def obj_draw(self, SURFACE_MAIN, FOV_MAP):
		self.is_visible = libtcod.map_is_in_fov(FOV_MAP, self.x, self.y)

		if self.is_visible:
			if len(self.animation) == 1:
				SURFACE_MAIN.blit(self.animation[0], (self.x*constant.CELL_WIDTH, self.y*constant.CELL_HEIGHT))

			elif len(self.animation) > 1:

				if self.CLOCK.get_fps() > 0.0:
					self.flick_timer += .5 / self.CLOCK.get_fps()

				if self.flick_timer >= self.flick_speed:
					self.flick_timer = 0.0

					if self.sprite_image >= len(self.animation) - 1:
						self.sprite_image = 0

					else:
						self.sprite_image += 1

			SURFACE_MAIN.blit(self.animation[self.sprite_image], (self.x*constant.CELL_WIDTH, self.y*constant.CELL_HEIGHT))

# vi: ts=4
