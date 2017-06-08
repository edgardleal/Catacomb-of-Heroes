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

	def logic(self, T_key, Player, Menu, dead_list, item_list, creature_list, msg_list, game_map):



		if not T_key == None:
			key_0, key_1 = T_key

			if isinstance(key_0, str):
				if key_0 == "NG":
					Menu.open = not Menu.open


			if Menu.open:
				self.control_menu(T_key, Menu, Player.Container.inventory)


			if Menu.open == False and Player.turn < 10 and Player.is_alive:
				Menu.select = 0
				if isinstance(key_0, int):
					self.act_creature(Player, creature_list, msg_list, T_key, game_map)
				if isinstance(key_0, str):
					if key_0 == "OK":
						item = self.check_item(item_list, Player.x, Player.y)
						if not item == None:
							self.grab_item(item, Player, item_list, msg_list)
						else:
							self.act_creature(Player, creature_list, msg_list, (0,0), game_map)
				

		elif Player.turn >= 10:
			for creature in creature_list:
				if not isinstance(creature, player.Player):
					self.enemy_act(creature, creature_list, msg_list, dead_list, game_map)
			Player.turn -= 10


	def control_menu(self, T_key, Menu, mylist):

		dir_x, dir_y = T_key

		if isinstance(dir_x, str):
			if dir_x == "OK" and len(mylist) > 0:
				# TODO use item
				print "TODO use " + str(mylist[Menu.select].name_object)
				pass
		else:
			if dir_y > 0:
				Menu.select += 1
			elif dir_y < 0:
				Menu.select -= 1

			if Menu.select < 0:
				Menu.select = len(mylist) - 1

			if Menu.select > len(mylist)-1:
				Menu.select = 0

	def act_creature(self, creature, creature_list, msg_list, T_dir, game_map):

		dir_x, dir_y = T_dir

		is_wall = (game_map[creature.x+dir_x][creature.y+dir_y].wall == True)

		target = self.check_creature(creature_list, creature.x+dir_x, creature.y+dir_y, creature)

		act = False

		if target:
			self.melee_combat(creature, target, msg_list)
			act = True
		elif not is_wall:
			creature.x += dir_x
			creature.y += dir_y
			act = True
		
		# This prevents player from loosing a turn trying to walk into a wall
		if isinstance(creature, player.Player) and act:
				creature.turn += creature.turn_pass

	def melee_combat(self, attacker, defender, msg_list):
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

		message = str((attacker.name_object + " attacks " + defender.name_object + " for " + str(total_dmg)))

		msg_list.append((message, (255,255,255))) 

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

	def enemy_act(self, creature, creature_list, msg_list, dead_list, game_map):
		x = libtcod.random_get_int(0, -1, 1)
		y = libtcod.random_get_int(0, -1, 1)

		T_dir = (x,y)

		if creature.is_alive:
			self.act_creature(creature, creature_list, msg_list, T_dir, game_map)
		else:
			creature_list.remove(creature)
			dead_list.insert(0, creature)

	def check_item(self, item_list, x, y):

		item = None

		for item in item_list:
			if item.x == x and item.y == y:
				return item

	def grab_item(self,  item, creature, item_list, msg_list):

		if creature.Container.used_slots + 1 <= creature.Container.max_slots:
			creature.Container.inventory.append(item)
			creature.Container.used_slots += 1
			item_list.remove(item)
			message = (str(" " + creature.name_object + " got " + item.name_object + "!"))
			color = (0, 160, 0)

		else:
			message = (" Inventory is full. ")
			color = (0, 160, 0) 

		msg_list.append((message, color))

	def drop_item(self, creature, item, item_list):

		item.x = creature.x
		item.y = creature.y

		item_list.insert(0, self)
		creature.Container.inventory.remove(self)
		creature.Container.used_slots -= 1

		message = str(" " + actor.name_object + " drop " + self.name_object + ".")
		color = (0, 0, 0)

		msg_list.append((message, color))