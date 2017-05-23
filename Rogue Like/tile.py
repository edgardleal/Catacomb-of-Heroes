#  _________  ___  ___       _______      
# |\___   ___\\  \|\  \     |\  ___ \     
# \|___ \  \_\ \  \ \  \    \ \   __/|    
#      \ \  \ \ \  \ \  \    \ \  \_|/__  
#       \ \  \ \ \  \ \  \____\ \  \_|\ \ 
#        \ \__\ \ \__\ \_______\ \_______\
#         \|__|  \|__|\|_______|\|_______|
                                        
                                                               
class Tile:

	def __init__(self, block):
		self.block = block		# If block a tile is a wall
		self.explored = False   # Every Tile that is not touched by the FOV is not explored.