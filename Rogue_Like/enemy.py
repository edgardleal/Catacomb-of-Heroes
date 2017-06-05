# Enemy

# IMPORTS
	# Third Party

	# My Modules
import creature

'''

'''
class Enemy(creature.Creature):
	"""docstring for Enemy"""
	def __init__(self, name_object, x, y, animation):
		super(Enemy, self).__init__(name_object, x, y, animation)
		self.init_attributes(1, 1, 1, 1)
		
