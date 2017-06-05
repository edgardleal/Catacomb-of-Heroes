# Main menu

# IMPORTS
	# Third Party

	# My modules

'''
This is just a test class
'''
class Main_Menu:

	# State Methods
	def __init__(self):
		# State Vars
		self.finished = False
		self.key_0 = 0
		self.key_1 = 0

		# Self Vars
		self.option = 0

	def get_input(self,  T_Key):

		if not T_Key == None:
			self.key_0, self.key_1 = T_Key

	def update(self):

		option_dic = { 0: "New Game", 1: "Load Game", 2: "Options", 3: "Quit"}

		if isinstance(self.key_0, int):
			if self.key_1 > 0:
				self.option += 1
			elif self.key_1 < 0:
				self.option -= 1
			
			#looping thru dictionary
			if self.option < 0:
				self.option = len(option_dic)-1
			if self.option > len(option_dic)-1:
				self.option = 0
		else:
			if self.key_0 == "OK":
				print option_dic[self.option]


		self.key_0, self.key_1 = (0,0)

	def draw(self, main_surface):
		pass


	def next_state(self, next_id):
		return next_id