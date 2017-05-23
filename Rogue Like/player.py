#  ________  ___       ________      ___    ___ _______   ________     
# |\   __  \|\  \     |\   __  \    |\  \  /  /|\  ___ \ |\   __  \    
# \ \  \|\  \ \  \    \ \  \|\  \   \ \  \/  / | \   __/|\ \  \|\  \   
#  \ \   ____\ \  \    \ \   __  \   \ \    / / \ \  \_|/_\ \   _  _\  
#   \ \  \___|\ \  \____\ \  \ \  \   \/  /  /   \ \  \_|\ \ \  \\  \| 
#    \ \__\    \ \_______\ \__\ \__\__/  / /      \ \_______\ \__\\ _\ 
#     \|__|     \|_______|\|__|\|__|\___/ /        \|_______|\|__|\|__|
#                                  \|___|/                             

import pygame

import constant
from object import *

class Player(Actor):

	turn = 0
	w_mod = 0 # Weapon Modifier
	e_mod = 0 # Equipment Modifier

	def handle_input(self, GAME_MAP, event_list, obj_list):

		for event in event_list:
			if event.type == pygame.KEYDOWN:
				if event.type == pygame.KEYDOWN:

					# Pass Turn
					if event.key == pygame.K_RETURN:
						self.turn += 10

					# Move UP
					if event.key == pygame.K_UP:
						self.creature.move(GAME_MAP, obj_list, (0, -1))
						self.turn += 10*self.e_mod
						

					# Move Down
					if event.key == pygame.K_DOWN:
						self.creature.move(GAME_MAP, obj_list, (0, 1))
						self.turn += 10*self.e_mod
					
					# Move Left
					if event.key == pygame.K_LEFT:
						self.creature.move(GAME_MAP, obj_list, (-1, 0))
						self.turn += 10*self.e_mod


					# Move Right
					if event.key == pygame.K_RIGHT:
						self.creature.move(GAME_MAP, obj_list, (1, 0))
						self.turn += 10*self.e_mod				

	def hero_class(self, id):

		self.vigor = 10
		self.strenght = 10
		self.dexterity = 10
		self.magic = 10

		# The sum of points of atributes are 30 in all classes.

		# Knight
		if id == 0:
			self.creature.hp = int(self.vigor*1.2)
			self.creature.max_hp = int(self.vigor*1.2)
			self.creature.power = self.strenght*1
			self.creature.acc = self.dexterity*.6
			self.creature.mpow = self.magic*.2 

			self.e_mod = 2
			self.w_mod = 2

		# Herald
		elif id == 1:
			self.creature.hp = int(self.vigor*.8)
			self.creature.max_hp = int(self.vigor*.8)
			self.creature.power = self.strenght*.7
			self.creature.acc = self.dexterity*.7
			self.creature.mpow = self.magic*.8

			self.e_mod = 1
			self.w_mod = 1

		# Scholar
		elif id == 2:
			self.creature.hp = int(self.vigor*.6)
			self.creature.max_hp = int(self.vigor*.6)
			self.creature.power = self.strenght*.5
			self.creature.acc = self.dexterity*.6
			self.creature.mpow = self.magic*1.3

			self.e_mod = .5
			self.w_mod = .5


	# TODO Player Class
		# Knight
			# Gear: 
				# Sword (5)
				# Armor (5)
				# High HP

		# Herald
			# Gear: 
				# Mace (3)
				# Armor (3)
				# Heal Spell (3)

		# Scholar
			# Knife (1)
			# Robes (1)
			# Damage Spell (5)

	# TODO Atributes
		# Vigor - Raises HP
		# Strength - More Damge
		# Dexterity - Raises HIT and EVADE
		# Magic - Boost Magic

	# TODO Equipment

		# Weapon Slot
			# There are 3 types of weapons
				# Heavy - When Attack you loose 2 turns. (w_mod = 2)
				# Normal - One Attack costs one Turn (w_mod = 1)
				# Light - You can attack 2 times per turn (w_mod =.5)

		# Armor Slot
			# There are 3 types of Armors
				# Heavy - One step is two turns (e_mod = 2)
				# Normal - One step is one turn (e_mod = 1)
				# Light - Two steps is one turn (e_mod = .5)

		# Explain
			# You cannot Stack the modifiers, witch means:
			# Light Weapon + Light Armor will not give you the hability of walking 2 steps and attack 2 times
			# But you'll be able to attack once and walk once in that turn, so you can hit an run.

		# Spell Slot
			# You can one have one spell on the slot.
			# Every Spell costs a turn to cast.
			# Spells costs cooldown to use it again.
			# Spells have a base base factor and a magic ratio.
				# So, a Heal Spell, for example, will heal (base+(player.Magic*magic ratio))
				# Heal.Base = 5, Heal.Ratio = 1, Herald.Magic = 8
				# That Heals 13, rounded down.