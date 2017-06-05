# Spritesheets

# IMPORTS
	# Third Party
import pygame
	# My Modules


'''

'''
class Spritesheet:

	def __init__(self, file_name):

		self.sprite_sheet = pygame.image.load(file_name).convert()

		self.COLOR_KEY = (255, 255, 255)


	def get_image(self, col, row, width = None, height = None, scale = None):

		image_list = []

		image = pygame.Surface([width, height]).convert()

		image.blit(self.sprite_sheet, (0,0), (col*width, row*height, width, height))

		image.set_colorkey(self.COLOR_KEY)

		if scale:
			(new_w, new_h) = scale

			image = pygame.transform.scale(image, (new_w, new_h))

		image_list.append(image)

		return image_list

	def get_animation(self, col, row, num_sprites, width = None, height = None, scale = None):

		image_list = []

		for i in range(num_sprites):
			image = pygame.Surface([width, height]).convert()

			image.blit(self.sprite_sheet, (0,0), (col*width+(width*i), row*height, width, height))

			image.set_colorkey(self.COLOR_KEY)

			if scale:
				(new_w, new_h) = scale

				image = pygame.transform.scale(image, (new_w, new_h))

			image_list.append(image)


		return image_list