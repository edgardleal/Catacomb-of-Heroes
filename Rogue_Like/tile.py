# Tile

class Tile:

	def __init__(self, wall):
		self.wall = wall		# If wall, then is a wall. I'm a genius!
		self.explored = False   # Every Tile that is not seem by the FOV is not explored.