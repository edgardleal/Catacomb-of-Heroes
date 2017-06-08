# Creature

# IMPORTS
	# Third Party
import pygame
try:
	import tcod as libtcod
except:
	import libtcodpy as libtcod

	# My Modules
import actor
import container
'''
Everything that can walk, fight, and die is a creature.
So, monsters and the player are both creatures.
'''
class Creature(actor.Actor):

	def __init__(self, name_object, x, y, animation):

		super(Creature, self).__init__(name_object, x, y, animation)
		self.is_alive = True
		self.Container = container.Container(9)

	def init_attributes(self, VIT, STR, DEX, MAG):

		self.VIT = VIT
		self.STR = STR
		self.DEX = DEX
		self.MAG = MAG 

		self.max_HP = int(((1+self.VIT) * 2) + 10 + (self.VIT/2))
		self.cur_HP = self.max_HP

	def get_hit(self):
		pass

	def get_eva(self):
		pass

	def get_def(self):
		return 1
		pass

	def get_dmg(self):
		'''
		DAMAGE CALC

		dex_scaling = ((Attacker.hit - Defender.eva)+1)*2

		weapon_dmg = (Attacker.weapon.atk*10)

		dmg_armor = (weapon_dmg + dex_scaling)/Defender.Armor.def

		str_dmg = Attacker.str * 2

		dmg_person = str_dmg/Defender.vit

		total_dmg = ((dmg_person * dmg_armor)/50)+2

		total_dmg is going to float between 80% and 100%
		'''

		# This function is going to return two values; weapon_dmg and str_dmg
		# Controller is going to handle it.

		str_dmg = self.STR*2

		total_dmg = str_dmg

		return total_dmg

	def take_damage(self, damage):

		self.cur_HP -= damage

		print self.name_object + " " + str(self.cur_HP) + "/" + str(self.max_HP)
		if self.cur_HP <= 0:
			self.is_alive = False
