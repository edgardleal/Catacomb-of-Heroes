# Game Text

# IMPORTS
	# Third Party
import pygame
# try:
# 	import tcod as libtcod
# except:
# 	import libtcodpy as libtcod

	# My Modules

'''

'''
class Text:
	def __init__(self):
		self.screen = 1


	def handle_text_height(self, font):

		font_obj = font.render('a', False, (0,0,0))
		font_rect = font_obj.get_rect()

		return font_rect.height

	def handle_text_width(self, font):

		font_obj = font.render('a', False, (0,0,0))
		font_rect = font_obj.get_rect()

		return font_rect.width

	def handle_text_res(self, font):

		font_height = self.handle_text_height(font)
		font_width = self.handle_text_width(font)

		return (font_width, font_height)

	def handle_text(self, font, incoming_text, incoming_color, incoming_bg_color):

		if incoming_bg_color:
			text_surface = font.render(incoming_text, False, incoming_color, incoming_bg_color)
		else:
			text_surface = font.render(incoming_text, False, incoming_color)

		# Text surface is just a surface with a string.
		return text_surface, text_surface.get_rect()

	def draw_text(self, font, txt_surf_box, text_to_draw, T_coord, color, bg_color = None):

		text_surf, text_rect = self.handle_text(font, text_to_draw, color, bg_color)

		text_rect.topleft = T_coord

		txt_surf_box.blit(text_surf, text_rect)

	'''
	Well.........
	I must admit that I tried for hours and I could'nt find a way to make this work as I wanted.
	I wanted the fist message to be drawn on the very bottom of the screen, and as new messages are appended to message list
	the old ones are going to be pushed upwards.

	As is now, the first message is drawn where the third message would be.

	'''
	def draw_messages(self, font, msg_list, num_msg_screen, txt_surf_box, bg_color = None):

		if len(msg_list) <= num_msg_screen:
			to_draw = msg_list
		else:
			to_draw = msg_list[-num_msg_screen:]

		text_height = self.handle_text_height(font)

		start_y = txt_surf_box.get_height() - (text_height*num_msg_screen)

		i = 0

		if not bg_color:
			bg_color = (0,0,0)


		for message, color in to_draw:
			self.draw_text(font, txt_surf_box, (" " + message + " "), (0, start_y+(i*text_height)), color, bg_color)
			i += 1