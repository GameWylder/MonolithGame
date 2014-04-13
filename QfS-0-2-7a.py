######The Quest For Susan Ver 0.1.7a
###COPYRIGHT @2014 Game Wylder/Anthony Dragone - Liscenced MIT
[#info tab
######(Version Number is Determined By: State(alpha,beta,released).CompletedSegments(100 lines of code).ObjectivesCompleted) 
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
	]

###END-PreGame Info
###START-PROGRAM

###Global Variables (Below)
devstate = 0
player = "DEFAULT"
morality = 0
egg = 0
deegg = "SCANNING FOR INVALID DRESSCODE"
var = "DEFAULT"
var2 = "DEFAULT"
gameover = 0
indent = "     "

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


#Debug
def bugstate():
	print()
	print("Would you like to Enable Debug mode? \n ((Debug mode will display variables that may change throughout the game))")
	print()
	while True:
		global egg
		global devstate
		choice = input()
		choice = choice.lower()
		if choice == "yes":
			devstate = 1
			print()
			print("Debug Enabled")
			break
		elif choice == "no":
			devstate = 0
			print()
			print("Debug Disabled")
			break
		elif choice in ('matika', 'mateka'):
			devstate = 0
			egg = 1
			print(deegg)
			break
		else:
			print("Invalid")
#
	
#Introduction to the game.
def intro():
	global indent
	print()
	print(indent+"You walk into a dark room. All of the floors, walls, and ceiling, covered in glass panels. The room is pitch dark, but as your eyes slowly adjust, you begin to faintly make out a dark figure. The air is still, not one sound reverberates through the walls. As you take a slow, deep breath, you feel a shiver run down your spine. The air is cold, so cold that your breath condensates before it even leaves your mouth. You don't realise that your breath instantly became shallow upon walking into the silence of this room. Then, you remind yourself about the shadowy figure sitting in the middle of the room.")
	print()
	print("((This is your first choice Hero. In this world, choices are what will allow you to pass through. You will be asked questions, and the words you may respond with will have an ' followed by a capital. You will not be asked to input more than one word. Good Luck, Hero.))")

#Choice Number1
def introchoice():
	print()
	print("Do you 'Hesitate? or do you 'Walk forward?")
	print()
	def Hesitate():
		print()
		print(indent+"You hesitate, standing still as if staring at a monster of your childhood. ''are you just going to stand there?'' the dark figure turns it's head to the side, looking over his shoulder towards you. ''are you frightened of things you do not know?'' he begins to slowly, and shakily stand up, using a cane for support. He then turns around to look at you. ''Fear is something that will hold you back'' he lifts his can and slams it down. The room illuminates, the glass panel beneath him gives off a slight illumination, and all of the other panels follow, like a domino effect. ''What do they call you?''")
		print()
	#
	def Walk():
		print()
		print(indent+"You step forward. Unshaken by the mysterious figure in the middle of the room. ''I see you are a brave one'' The figure slowly stands shakily. Hunched over with a cane in his hand. He lifts the cane and slams it down on the glass panel. The room illuminates, the glass panel beneath him gives off a slight illumination, and all of the other panels follow. It reminds you of a Domino. ''Welcome, now, what is your name?''")
		print()
	#
	def pick():
		global morality
		while True:
			choice = input()
			choice = choice.lower()
			if choice == "hesitate":
				Hesitate()
				morality = 1
				break
			elif choice == "walk":
				Walk()
				morality = 2
				break
			else:
				if egg == 1:
					print()
					print("INVALID DRESSCODE DETECTED!")
					print()
				else:
					print()
					print("You cannot turn back. You must Decide.")
					print()
	pick()
#

#name input
def yourname():
	global player
	player = input("")
	print()
#

#Branches are branches of the game. different branches caused by moral choices will be represented and continued with a decimal number.
def branch1():
	global morality
	global player
	while True:
		if morality == 1:
			print(indent+"''So, your name is "+player+", huh? So "+player+" are you a coward? So hesitant to walk into a dark room? You realise that to pass through these trials, you cannot be a coward. You must be brave'' the old man sighs and clenches his fist tightly around the bulb of his cane. ''You'll have to do though... I guess we can't be picky about our 'Champions' now can we?''")
			print()
			break
		elif morality == 2:
			print(indent+"''"+player+", I'll remember that. It's hard to forget someone who has guts. You're brave "+player+", you're very brave. Your bravery will most definitely help you pass through the trials which befall before you. I can see now that you are going to be a proper Champion'' he smiles.")
			print()
			break
#

def branch2():
	def var():
		global morality
		global var
		if morality == 1:
			var = "hesitate"
		else:
			var = "walk"
	#
	def var2():
		global morality
		global var2
		if morality == 1:
			var2 = " don't be a coward, prove to me you can be brave.'' The old man casually walks into the secret passage."
		else:
			var2 = " you've shown me you can be brave, prove it.'' he faces forward again and begins to walk forward into the secret entrance."
	def follow():
		global var
		global var2
		global player
		print(indent+"''This world is very sensitive, "+player+", your choices will effect your travels. For example: your chose to "+var+", I responded accordingly. Though it doesn't matter if you hesitated or walked, this will be the only choice that doesn't matter. Anyway, come on, follow me. There's a reason you were chosen to be the Champion, and that reason wasn't to stand here and debate on the weather you chose to "+var+" in here or not'' he turns toward the wall behind him. As he slowly walks towards it the glass panels part and reveal a hidden passage. ''come on now,"+var2)
		print()
	#
	var()
	var2()
	follow()
#

[#def branch 3
#def branch3():
	
	#
#	def action():
	]
#

def debugres():
	global devstate
	global morality
	global player
	if devstate == 1:
		print()
		print("Debug Results:")
		print()
		print("Player Name:")
		print(player)
		print()
		print("Moral Path:")
		print(morality)
		print()
		print("End Debug, Program End")
	else:
		print("End Program")
#

[#def endgame
#This just determines if the player has reached the end of the game.
#def endgame():
#	global gameover
#	gameover = 1
#
	]

def restart():
	print()
	print("Replay?")
	print()
	choice = input()
	choice = choice.lower()
	if choice == "yes":
		gamesequence()
	else:
		print()
		print("Game Over")
#

#Below is the game's story sequence#
def gamesequence():
	bugstate()
	intro()
	introchoice()
	yourname()
	branch1()
	branch2()
	#Debug
	debugres()
#	endgame()
	restart()
#

gamesequence()
