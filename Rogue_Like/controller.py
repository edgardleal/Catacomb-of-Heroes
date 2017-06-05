# Controller

# IMPORTS
	# Third Party
import random
import pygame
try:
	import tcod as libtcod
except:
	import libtcodpy as libtcod

	# My Modules
import player

'''
Controller is a class that is going to control the logic of "Actors" in the game.
How they interact, move, etc.
'''
class Controller(object):
	def __init__(self):
		super(Controller, self).__init__()

	def logic(self, T_key, Player, creature_list, dead_list, game_map):

		if not T_key == None:
			key_0, key_1 = T_key

			if Player.turn < 10 and Player.is_alive:
				if isinstance(key_0, int):
					self.act_creature(Player, creature_list, T_key, game_map)
					Player.turn += Player.turn_pass
		elif Player.turn >= 10:
			for creature in creature_list:
				if not isinstance(creature, player.Player):
					self.enemy_act(creature, creature_list, dead_list, game_map)
			Player.turn -= 10



	def act_creature(self, creature, creature_list, T_dir, game_map):

		# if not T_dir == None:
		dir_x, dir_y = T_dir

		is_wall = (game_map[creature.x+dir_x][creature.y+dir_y].wall == True)

		target = self.check_creature(creature_list, creature.x+dir_x, creature.y+dir_y, creature)

		if target:
			self.melee_combat(creature, target)
		elif not is_wall:
			creature.x += dir_x
			creature.y += dir_y

	def melee_combat(self, attacker, defender):
		'''
		DAMAGE CALC

		First thing is to decide if defender manages to evade. If not then:

		dex_scaling = ((Attacker.hit - Defender.eva)+1)*2

		weapon_dmg = (Attacker.weapon.atk*10)

		dmg_armor = (weapon_dmg + dex_scaling)/Defender.Armor.def

		str_dmg = Attacker.str * 2

		dmg_person = str_dmg/Defender.vit

		total_dmg = ((dmg_person * dmg_armor)/50)+2

		total_dmg is going to float between 80% and 100%
		'''

		# TODO HIT x EVA
		# TODO WEAPON
		# TODO ARMOR

		total_dmg = attacker.get_dmg()

		print attacker.name_object + " attacks " + defender.name_object + " for " + str(total_dmg)

		defender.take_damage(total_dmg)

	def check_creature(self, creature_list, x, y, exclude_creature = None, exclude_type = None):

		target = None

		for creature in creature_list:

			if creature.x == x and creature.y == y:

				if exclude_creature: # If its not myself.

					if creature is not exclude_creature:
						target = creature

					if exclude_type: # If its not my kind

						if not isinstance(creature, exclude_type):
							target = creature

				else: # If I'm confused I can target anyone, including myself
					target = creature

		if target:
			return target

	def enemy_act(self, creature, creature_list, dead_list, game_map):
		x = libtcod.random_get_int(0, -1, 1)
		y = libtcod.random_get_int(0, -1, 1)

		T_dir = (x,y)

		if creature.is_alive:
			self.act_creature(creature, creature_list, T_dir, game_map)
		else:
			creature_list.remove(creature)
			dead_list.insert(0, creature)
