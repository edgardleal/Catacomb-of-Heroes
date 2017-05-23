#  ________  ________  _____ ______   ________  ________  ________   _______   ________   _________  ________      
# |\   ____\|\   __  \|\   _ \  _   \|\   __  \|\   __  \|\   ___  \|\  ___ \ |\   ___  \|\___   ___\\   ____\     
# \ \  \___|\ \  \|\  \ \  \\\__\ \  \ \  \|\  \ \  \|\  \ \  \\ \  \ \   __/|\ \  \\ \  \|___ \  \_\ \  \___|_    
#  \ \  \    \ \  \\\  \ \  \\|__| \  \ \   ____\ \  \\\  \ \  \\ \  \ \  \_|/_\ \  \\ \  \   \ \  \ \ \_____  \   
#   \ \  \____\ \  \\\  \ \  \    \ \  \ \  \___|\ \  \\\  \ \  \\ \  \ \  \_|\ \ \  \\ \  \   \ \  \ \|____|\  \  
#    \ \_______\ \_______\ \__\    \ \__\ \__\    \ \_______\ \__\\ \__\ \_______\ \__\\ \__\   \ \__\  ____\_\  \ 
#     \|_______|\|_______|\|__|     \|__|\|__|     \|_______|\|__| \|__|\|_______|\|__| \|__|    \|__| |\_________\
#                                                                                                      \|_________|

import tcod as libtcod

import constant
import game_logic 
# Things that can move, attack and die are going to be Creature.
class com_Creature:


	def __init__(self, name_instance, def_death = None, hp=10, power = 1, acc = 1, mpow = 1, armor = 1, eva = 1):

		self.name_instance = name_instance
		self.def_death = def_death

		self.max_hp = hp
		self.hp = hp
		
		self.power = power
		self.acc = acc
		self.mpow = mpow

		self.armor = armor
		self.eva = eva

	def check_for_Actor(self, obj_list, x, y, exclude_obj):

		target = None
			# Code here is cheking for a target within melee range that is not self.
		for obj in obj_list:
			if (obj is not exclude_obj and 
				obj.x == x and 
				obj.y == y and 
				obj):

				target = obj

			if target:
				return target

	def check_for_creature(self, obj_list, x, y, exclude_obj = None):

		target = None

		if exclude_obj:
			# Code here is cheking for a target within melee range that is not self.
			for obj in obj_list:
				if (obj is not exclude_obj and 
					obj.x == x and 
					obj.y == y and 
					obj.creature):

					target = obj

				if target:
					return target
		else:
			# Code here is checking for any target including self (for confusing spell or something like this)
			for obj in obj_list:
				if (obj.x == x and 
					obj.y == y and 
					obj.creature):

					target = obj

				if target:
					return target


	def move(self, GAME_MAP, obj_list, (dx, dy)):
		
		tile_is_wall = (GAME_MAP[self.owner.x + dx ][self.owner.y + dy].block == True)

		target = self.check_for_creature(obj_list, self.owner.x + dx, self.owner.y + dy, exclude_obj = self.owner)
		actor = self.check_for_Actor(obj_list, self.owner.x + dx, self.owner.y + dy, self.owner)

		if target:
			self.attack(target)

		if not tile_is_wall and target is None:
			self.owner.x += dx
			self.owner.y += dy
			if actor:
				game_logic.Game.game_messages(actor.name_object, constant.COLOR_WHITE)


	def take_damage(self, damage):

		self.hp -= damage
		game_logic.Game.game_messages(str(self.name_instance + ": " + str(self.hp) + "/" + str(self.max_hp)), constant.COLOR_WHITE)

		if self.hp <= 0:

			if self.def_death:
				self.def_death(self.owner)

	def attack(self, target):
		# TODO evade

		# TODO random damage
		damage = int(self.power)

		game_logic.Game.game_messages(str(self.name_instance + " attacks " + target.creature.name_instance + " for " + str(damage)) + " damage!", constant.COLOR_WHITE)
		target.creature.take_damage(damage)

		

def death_monster(monster):

	game_logic.Game.game_messages(str(monster.creature.name_instance + " is dead!"), constant.COLOR_WHITE)
	monster.name_object = "A dead " + monster.creature.name_instance
	monster.creature = None
	monster.ai = None

	monster.sprite = constant.S_ENEMY_DEAD

class com_AI:

	def take_turn(self, GAME_MAP, obj_list):
		self.owner.creature.move(GAME_MAP, obj_list, (libtcod.random_get_int(0, -1, 1), libtcod.random_get_int(0, -1, 1)))


# Things that can be picked up and used are going to be Item.
# TODO class com_Itens:

# Objects that can hold other objects are going to be Container
# TODO class com_Container:                                                                                                                 