# http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
#  _____ ______   ________  ___  ________      
# |\   _ \  _   \|\   __  \|\  \|\   ___  \    
# \ \  \\\__\ \  \ \  \|\  \ \  \ \  \\ \  \   
#  \ \  \\|__| \  \ \   __  \ \  \ \  \\ \  \  
#   \ \  \    \ \  \ \  \ \  \ \  \ \  \\ \  \ 
#    \ \__\    \ \__\ \__\ \__\ \__\ \__\\ \__\
#     \|__|     \|__|\|__|\|__|\|__|\|__| \|__|
                                             
from window import Window

if __name__ == "__main__":
	MainGame = Window()

# TODO
	# REFACTOR THE CODE...

	# TODO GAME
	'''
	The game is a rogue like.
S
	This rogue like will save every hero that died in the dungeon.
	Game will save what that hero did before dying to spawn him in the next gameplay
		Fallen heroes will stay "forever" in the dungeon and the next hero can see and interact with them
		The dead heroes will became dead corpses waiting to be looted, Shop NPCs, Quest NPCs, and even monsters

	The dungeon has a end. It starts on floor (I don't know yet).
	But everytime the player reaches the end he'll find the Dungeon Soul.
		Player will have two choices, kill his soul or live it there.

	IF Player Kills the Dungeon Soul, that hero become the next Dungeon soul.
		Every hero that fallen before will be erased.
		In the next Playthrought the dungeon will have +5 floors
		Essentially, Game starts over with a new challenge.

	IF player Leaves the Dungeon Soul, he'll have to exit the Dungeon and see the ending. 
		In the next playthrough player will find a chest in the very first room with a letter and some loot.
		This letter says something like "Don't fight if you don't know why you fight for."

	'''