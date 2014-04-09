######The Quest For Susan Ver 0.1.2a
######(Version Number is Determined By: State(alpha,beta,released).CompletedSegments(100 lines of code).ObjectivesCompleted) 
###COPYRIGHT @2014 Game Wylder/Anthony Dragone - Liscenced MIT
###
###	Description:
##	    	A protagonist will explore through 6 different
##		puzzles to achieve their quest to recover Susan,
##		the Monolith.
###	Puzzles:
##			The first puzzle will be a simple puzzle, like
##		a tutorial level. It will require 2 simple steps to
##		be followed through. We will require global variables
##		to track the steps that the player has taken in order
##		to pass through the next level. After the first level,
##		the player will take another 2 steps in the next level.
##		Each level will add on an additional 2 steps. These
##		steps can be anything, such as character encounters.
##		Different rooms will hold different parts of code,
##		that will essentially allow the player to progress.
#
###Below is a quick user input test
#
## input_variable = input ("Enter your name: ")
## print ("Hello " + input_variable + "! Happy Birthday! \n Exactly 16 #years ago, you were born. \n Every year, a child of age 16 is chosen #for a quest.")
##ENDEND
#
##Below is a global variable example
#
##globvar = 0
##
##def set_globvar_to_one():
##    global globvar    # Needed to modify global copy of globvar
##    globvar = 1
##
##def print_globvar():
##    print globvar     # No need for global declaration to read value of globvar
#
##set_globvar_to_one()
##print_globvar()       # Prints 1
###ENDEND

###END-PreGame Info
###START-PROGRAM

###Global Variables (Below)
##	(All Global Variables will start with GlV_)
#gloName
choicepath = 0

###Game Variables
##	(All game variables will start with GaV_)
GaV_Tries = 5
GaV_ValidChoice = True
#Level Steps
GaV_LvlTut = 2
GaV_Lvl1 = 2
GaV_Lvl2 = 2
GaV_Lvl3 = 4
GaV_Lvl4 = 6
GaV_Lvl5 = 8
GaV_Lvl6 = 10

#MORAL
def addmoral():
	global choicepath
	choicepth = 1
def remmoral():
	global choicepath
	choicepath = 2

def intro():
	print()
	print("     You walk into a dark room. All of the floors, walls, and ceiling, covered in glass panels. The room is pitch dark, but as your eyes slowly adjust, you begin to faintly make out a dark figure. The air is still, not one sound reverberates through the walls. As you take a slow, deep breath, you feel a shiver run down your spine. The air is cold, so cold that your breath condensates before it even leaves your mouth. You don't realise that your breath instantly became shallow upon walking into the silence of this room. Then, you remind yourself about the shadowy figure sitting in the middle of the room.")
	print()
	print("((This is your first choice Hero. In this world, choices are what will allow you to pass through. You will be asked questions, and the words you may respond with will have an ' followed by a capital. You will not be asked to input more than one word. Good Luck, Hero.))")

#Choice Number1
def introchoice():
	print()
	print("Do you 'Hesitate? or do you 'Walk forward?")
	print()
	def Hesitate():
		print()
		print("You hesistate, startled by the sudden illumination of the room. Focusing on the old man who has his back turned to you. He gestures for you to come closer. \n ''Come in, Come in, don't be frightened. I'm but a frail old man'' he says.")
		print()
	#
	def Walk():
		print()
		print("You step forward. Unshaken by the mysterious figure in the middle of the room. \n  ''I see you are a brave one'' The figure slowly stands shakily. Hunched over with a cane in his hand. He lifts the cane and slams it down on the glass panel. The room illuminates, the glass panel beneath him gives off a slight illumination, and all of the other panels follow. It reminds you of a Domino. ''Welcome'' ")
		print()
	#
	def pick():
		while True:
			my_input = input("")
			if my_input == "Hesitate":
				Hesitate()
				remmoral()
				break
			elif my_input == "hesitate":
				Hesitate()
				remmoral()
				break
			elif my_input == "walk":
				Walk()
				addmoral()
				break
			elif my_input == "Walk":
				Walk()
				addmoral()
				break
			else:
				print()
				print("You cannot turn back. You must pick.")
				print()
			#
		#
	pick()
	#
#
##Below is the game's story sequence.
intro()
introchoice()
global choicepath
print(choicepath)
