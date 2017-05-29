#  _____ ______   ________  ________
# |\   _ \  _   \|\   __  \|\   __  \
# \ \  \\\__\ \  \ \  \|\  \ \  \|\  \
#  \ \  \\|__| \  \ \   __  \ \   ____\
#   \ \  \    \ \  \ \  \ \  \ \  \___|
#    \ \__\    \ \__\ \__\ \__\ \__\
#     \|__|     \|__|\|__|\|__|\|__|

try:
    import tcod as libtcod
except:
    import libtcodpy as libtcod

from tile import Tile
import constant


class Map:

	def map_create(self):
		new_map = [[Tile(False) for y in range (0, constant.MAP_HEIGHT)] for x in range (0, constant.MAP_WIDTH)]

		new_map[12][7].block = True
		new_map[12][12].block = True

		for x in range(constant.MAP_WIDTH):
			new_map[x][0].block = True
			new_map[x][constant.MAP_HEIGHT-1].block = True

		for y in range(constant.MAP_HEIGHT):
			new_map[0][y].block = True
			new_map[constant.MAP_WIDTH-1][y].block = True

		self.map_make_fov(new_map)

		return new_map

	def map_make_fov(self, income_map):

		self.FOV_MAP = libtcod.map_new(constant.MAP_WIDTH, constant.MAP_HEIGHT)

		for y in range(constant.MAP_HEIGHT):
			for x in range(constant.MAP_WIDTH):
				libtcod.map_set_properties(self.FOV_MAP, x, y, not income_map[x][y].block, not income_map[x][y].block)

	def map_calculate_fov(self, PLAYER):

		libtcod.map_compute_fov(self.FOV_MAP, PLAYER.x, PLAYER.y, constant.TORCH_RADIUS, constant.FOV_LIGHT_WALLS, constant.FOV_ALGO)

