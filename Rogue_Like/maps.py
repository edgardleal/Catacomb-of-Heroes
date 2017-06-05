# Maps

# IMPORTS
	# Third Party
try:
	import tcod as libtcod
except:
	import libtcodpy as libtcod

	# My Modules
import tile

'''
'''
class Maps:

	def __init__(self):
		self.fov_light_walls = True 
		self.fov_algo = libtcod.FOV_SHADOW

	def create(self, map_height, map_width):

		new_map = [[tile.Tile(False) for x in range (0, map_height)] for y in range (0, map_width)]

		new_map[12][7].wall = True
		new_map[12][12].wall = True


		for x in range(map_width):
			new_map[x][0].wall = True
			new_map[x][map_height-1].wall = True

		for y in range(map_height):
			new_map[0][y].wall = True
			new_map[map_width-1][y].wall = True
			

		# Making the field of view
		
		fov_map = self.make_fov(map_width, map_height, new_map)
		

		return new_map, fov_map

	def make_fov(self, map_width, map_height, new_map):
		fov_map = libtcod.map_new(map_width, map_height)
		for x in range(map_width):
			for y in range(map_height):
				libtcod.map_set_properties(fov_map, x, y, not new_map[x][y].wall, not new_map[x][y].wall)
		return fov_map

	def update_fov(self, fov_map, player):

		libtcod.map_compute_fov(fov_map, player.x, player.y, player.torch, self.fov_light_walls, self.fov_algo)