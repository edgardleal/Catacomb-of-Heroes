# Draw

# IMPORTS
	# Third Party
import pygame
try:
	import tcod as libtcod
except:
	import libtcodpy as libtcod

	# My Modules

'''
Here I decided to have multiple classes of draw, one for each state, that way I can do "from draw import class".
So everything stays in draw file instead of having multiple files with (almost) same name.
Not the best of practices but I prefer it this way.
'''
class Draw_Game:

	def __init__(self, spr_res):
		self.spr_res = spr_res


	# TODO gfx
	def maps(self, map_to_draw, map_height, map_width, fov_map, surface, wall, wall_explored, floor, floor_explored):
		'''
		This code takes the field of view (fov) of the player and draw stuff based on it.
		So, if a floor or wall is visible by the fov of the player, game should draw it
		If a floor or wall is not visible, but was explored, by the fov of the player, it should draw it, but using a diffrent GFX
		'''

		for x in range (0, map_width):
			for y in range (0, map_height):

				is_visible = libtcod.map_is_in_fov(fov_map, x, y)

				# If something is visible right now then:
				if is_visible:
					
					# You saw this part, let's put this as explored.
					map_to_draw[x][y].explored = True

					# If this position is marked as a wall, draw a wall
					if map_to_draw[x][y].wall:
						surface.blit(wall, (x*self.spr_res, y*self.spr_res))
					# Else is no wall, just draw a floor.
					else:
						surface.blit(floor, (x*self.spr_res, y*self.spr_res))
				# Well, this is not in the field of vision anymore, but you 
				elif map_to_draw[x][y].explored:
					if map_to_draw[x][y].wall:
						surface.blit(wall_explored, (x*self.spr_res, y*self.spr_res))
					else:
						surface.blit(floor_explored, (x*self.spr_res, y*self.spr_res))

	def objects(self, obj_list, spr_res, surface, fov_map, clock):
		for obj in obj_list:
			self.obj_draw(obj, spr_res, surface,  fov_map, clock)
			pass

	def obj_draw(self, obj, spr_res, surface, fov_map, clock):

		is_visible = libtcod.map_is_in_fov(fov_map, obj.x, obj.y)

		if is_visible:
			if len(obj.animation) == 1:

				obj.sprite_image = 0

			else:

				flick_speed = .5/len(obj.animation)

				if clock.get_fps() > 0.0:
					obj.flicker_timer += .5 / clock.get_fps()

					if obj.flicker_timer > flick_speed:
						obj.flicker_timer = 0.0

						if obj.sprite_image >= len(obj.animation)-1:
							obj.sprite_image = 0
						else:
							obj.sprite_image += 1

			surface.blit(obj.animation[obj.sprite_image], (obj.x*spr_res, obj.y*spr_res))

	