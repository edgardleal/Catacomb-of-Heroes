#  ________  ________  ________   ________  _________  ________  ________   _________   
# |\   ____\|\   __  \|\   ___  \|\   ____\|\___   ___\\   __  \|\   ___  \|\___   ___\ 
# \ \  \___|\ \  \|\  \ \  \\ \  \ \  \___|\|___ \  \_\ \  \|\  \ \  \\ \  \|___ \  \_| 
#  \ \  \    \ \  \\\  \ \  \\ \  \ \_____  \   \ \  \ \ \   __  \ \  \\ \  \   \ \  \  
#   \ \  \____\ \  \\\  \ \  \\ \  \|____|\  \   \ \  \ \ \  \ \  \ \  \\ \  \   \ \  \ 
#    \ \_______\ \_______\ \__\\ \__\____\_\  \   \ \__\ \ \__\ \__\ \__\\ \__\   \ \__\
#     \|_______|\|_______|\|__| \|__|\_________\   \|__|  \|__|\|__|\|__| \|__|    \|__|
#                                   \|_________|                                                                                                                              

# Imports
import tcod as libtcod
import pygame
pygame.init()


# Window Info
WINDOW_NAME = "Catacombs of Heroes"
# WINDOW_ICON = pygame.image.load("")

# Window Size
GAME_WIDTH = 800
GAME_HEIGHT = 640

# Frames per second
GAME_FPS = 60

# System Colors
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)

# Game Colors
COLOR_BG = COLOR_BLACK

# Map Variables
MAP_WIDTH = 25 # Game Width / object size
MAP_HEIGHT = 20 # Game Height / object size

CELL_WIDTH = 32 # Size of the sprite.
CELL_HEIGHT = 32

# FOV Settings
FOV_ALGO = libtcod.FOV_BASIC
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 5

# Font
FONT_DEBUG = pygame.font.Font("DATA/Pixeled.ttf", 5)
FONT_MESSAGE = pygame.font.Font("DATA/DUNGRG.ttf", 20)

# Message
NUM_MESSAGES = 3

# Game
TURN_VALUE = 10

# Sprites
S_ENEMY_DEAD = pygame.image.load("GFX/Enemy_dead.png")
