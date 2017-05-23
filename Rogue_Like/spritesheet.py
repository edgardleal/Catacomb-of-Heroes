#   ________  ________  ________  ___  _________  _______   ________  ___  ___  _______   _______  _________   
#  |\   ____\|\   __  \|\   __  \|\  \|\___   ___\\  ___ \ |\   ____\|\  \|\  \|\  ___ \ |\  ___ \|\___   ___\ 
#  \ \  \___|\ \  \|\  \ \  \|\  \ \  \|___ \  \_\ \   __/|\ \  \___|\ \  \\\  \ \   __/|\ \   __/\|___ \  \_| 
#   \ \_____  \ \   ____\ \   _  _\ \  \   \ \  \ \ \  \_|/_\ \_____  \ \   __  \ \  \_|/_\ \  \_|/__  \ \  \  
#    \|____|\  \ \  \___|\ \  \\  \\ \  \   \ \  \ \ \  \_|\ \|____|\  \ \  \ \  \ \  \_|\ \ \  \_|\ \  \ \  \ 
#      ____\_\  \ \__\    \ \__\\ _\\ \__\   \ \__\ \ \_______\____\_\  \ \__\ \__\ \_______\ \_______\  \ \__\
#     |\_________\|__|     \|__|\|__|\|__|    \|__|  \|_______|\_________\|__|\|__|\|_______|\|_______|   \|__|
#     \|_________|                                            \|_________|                                     

import pygame

import constant

class Spritesheet:

	def __init__(self, file_name):
		# Load Spritesheet
		self.sprite_sheet = pygame.image.load(file_name).convert()

	def get_image(self, col, row, width = constant.CELL_WIDTH, height = constant.CELL_HEIGHT, scale = None):

		image_list = []

		image = pygame.Surface([width, height]).convert()

		image.blit(self.sprite_sheet, (0,0), (col*width, row*height, width, height))

		image.set_colorkey(constant.COLOR_WHITE)

		if scale:
			(new_w, new_h) = scale

			image = pygame.transform.scale(image, (new_w, new_h))

		image_list.append(image)

		return image_list

	def get_animation(self, col, row, num_sprites, width = constant.CELL_WIDTH, height = constant.CELL_HEIGHT, scale = None):

		image_list = []

		for i in range(num_sprites):
			image = pygame.Surface([width, height]).convert()

			image.blit(self.sprite_sheet, (0,0), (col*width+(width*i), row*height, width, height))

			image.set_colorkey(constant.COLOR_WHITE)

			if scale:
				(new_w, new_h) = scale

				image = pygame.transform.scale(image, (new_w, new_h))

			image_list.append(image)

		return image_list