# by Joe Riedley

reality = True
this = True
thereallife = False
justfantasy = True
windblows = ["north", "south", "east", "west", True]


class BohemianRhapsody:
	
	def __init__(self):
		self.poor = True
		self.boy = True
		self.sympathy = 0
		self.matters = False
		self.easy = ""
		print("Bohemian Rhapsody")
		
		
	def play(self):
		
		try:
			if this == thereallife:
				print("Life is real")
				
			if this == justfantasy:
				print("Life is just fantasy")

			landslide = 1 / 0

		except ZeroDivisionError as e:
			while reality:
				with open("youreyes.txt", 'r') as fp:
					if lookup("skies & see", fp.readlines()):
						break

				self.poor = True
				self.boy = True

				self.sympathy = 0

				self.easy = "come"
				self.easy = "go"

				high = 0.0001
				low = 0.0001

				if any(windblows):
					self.matters = False

		finally:
			print("🎵🎵🎵")


def lookup(check, line):
	if check in line:
		return True
	else:
		return False


if __name__ == '__main__':
	song = BohemianRhapsody().play()
   
   
