# Itens

# Third Party

# My Modules
from actor import *
from draw import *


class Item(Actor):

	def init_item(self, obj_list):
		self.obj_list = obj_list

	# TODO def use_item
	def drop(self, actor):
		self.obj_list.insert(0, self)
		self.x = actor.x
		self.y = actor.y
		actor.Container.inventory.remove(self)
		actor.Container.used_slots -= 1
		Draw.set_MSG_TO_DRAW(str(" " + actor.name_object + " drop " + self.name_object + "."), (0, 0, 0))