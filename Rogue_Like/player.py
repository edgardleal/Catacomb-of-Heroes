# Player

# IMPORTS
	# Third Party

	# My Modules
import creature

'''

'''
class Player(creature.Creature):

	def __init__(self, name_object, x, y, animation):
		super(Player, self).__init__(name_object, x, y, animation)
		self.torch = 5
		self.turn = 0
		self.turn_pass = 10
		self.init_attributes(6, 6, 6, 6)


	def equip_mod(self):
		pass		

	def weap_mod(self):
		pass

	