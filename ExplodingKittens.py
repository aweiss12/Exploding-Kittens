import random
import setup
import time
import executefunctions
import webbrowser
import _thread
import threading
from os import system

#list of card values
attackcards = [1, 2, 3, 4]
skipcards = [5, 6, 7, 8]
nopecards = [9, 10, 11, 12, 13]
favorcards = [14, 15, 16, 17]
shufflecards = [18, 19, 20, 21]
stfcards = [22, 23, 24, 25, 26]
TCcards = [27, 28, 29, 30]
WCcards = [31, 32, 33, 34]
PCcards = [35, 36, 37, 38]
BCcards = [39, 40, 41, 42]
RCcards = [43, 44, 45, 46]
defusecards = [47, 48, 49, 50, 51, 52]
ekcards = [53, 54, 55, 56]

class Deck(object):
	#object which is used to create all decks and hands
	def __init__(self, name, cards, turn, nextturn, iscomp, nextplayer, prevplayer, eks):
		self.cards = [None]*cards
		self.turn = turn
		self.nextturn = nextturn
		self.iscomp = iscomp
		self.name = name
		self.nextplayer = nextplayer
		self.prevplayer = prevplayer
		self.eks = eks 
	def add_card(self, card):
		self.cards.insert(0, card)
	def remove_card(self):
		return self.cards.pop(0)
	def shuffle_deck(self):
		random.shuffle(self.cards)
	def print_deck(self):
	 	#print (self.cards)
	 	namelist = []
	 	self.cards.sort()
	 	for i in self.cards:
	 		cardname = findcardname(i)
	 		namelist.append(cardname)
 		print(namelist)
	def print_deck_stf(self):
	 	namelist = []
	 	for i in self.cards:
	 		cardname = findcardname(i)
	 		namelist.append(cardname)
 		print(namelist)

def findcardname(i):
	#correlates card value to name
	if i in attackcards:
 		return 'Attack'
	elif i in skipcards:
		return 'Skip'
	elif i in nopecards:
		return 'Nope'
	elif i in favorcards:
		return 'Favor'
	elif i in stfcards:
		return 'See the Future'
	elif i in defusecards:
		return 'Defuse'
	elif i in shufflecards:
		return 'Shuffle'
	elif i in TCcards:
		return 'TacoCat'
	elif i in RCcards:
		return 'Rainbow Cat'
	elif i in BCcards:
		return 'Beard Cat'
	elif i in PCcards:
		return 'Hairy Potato Cat'
	elif i in WCcards:
		return 'Watermelon Cat'
	else:
		return 'Exploding Kitten'

def prob(num):
	#creates random number between 1 and 100 and using that decides yes or no options
	x = random.randint(0,100)
	if x > num:
		return 0
	else:
		return 1

def findcardnum(test, playerturn):
	#find's the number of a card in a deck based on corresponding card name
	cardnum = 0
	if test[0] == 'A':
		for i in playerturn.cards:
			if i in attackcards:
				cardnum = i
				break
	elif test[0] == 'S':
		skcount = 0
		shcount = 0
		stcount = 0
		for i in playerturn.cards:
			if i in skipcards:
				skcount += 1
			elif i in shufflecards:
				shcount += 1
			elif i in stfcards:
				stcount += 1
		if skcount == 0 and shcount == 0 and stcount != 0:
			for i in playerturn.cards:
				if i in stfcards:
					cardnum = i
					break
		elif skcount == 0 and stcount == 0 and shcount != 0:
			for i in playerturn.cards:
				if i in shufflecards:
					cardnum = i
					break
		elif shcount == 0 and stcount == 0 and skcount != 0:
			for i in playerturn.cards:
				if i in skipcards:
					cardnum = i
					break
		else:
			if len(test) > 1:
				if test[1] not in ['K', 'T', 'E', 'H']:
					reportsinvalid(playerturn)
					cardnum = 0
				else:
					if test[1] == 'K':
						for i in playerturn.cards:
							if i in skipcards:
								cardnum = i
								break
					elif test[1] == 'H':
						for i in playerturn.cards:
							if i in shufflecards:
								cardnum = i
								break
					else:
						for i in playerturn.cards:
							if i in stfcards:
								cardnum = i
								break
			else:
				reportsinvalid(playerturn)
				cardnum = 0

	elif test[0] == 'N':
		for i in playerturn.cards:
			if i in nopecards:
				cardnum = i
				break
	elif test[0] == 'F':
		for i in playerturn.cards:
			if i in favorcards:
				cardnum = i
				break
	elif test[0] == 'T':
		for i in playerturn.cards:
			if i in TCcards:
				cardnum = i
				break
	elif test[0] == 'R':
		for i in playerturn.cards:
			if i in RCcards:
				cardnum = i
				break
	elif test[0] == 'B':
		for i in playerturn.cards:
			if i in BCcards:
				cardnum = i
				break
	elif test[0] == 'H':
		for i in playerturn.cards:
			if i in PCcards:
				cardnum = i
				break
	elif test[0] == 'W':
		for i in playerturn.cards:
			if i in WCcards:
				cardnum = i
				break
	elif test[0] == 'D':
		for i in playerturn.cards:
			if i in defusecards:
				cardnum = i
				break
	return cardnum

def move_card(deck1, deck2):
	#moves card from one deck to another using built in functions
	deck2.add_card(deck1.remove_card())

def gamesetupfunction(numh, numc):
	#creates decks, based on number of wanted human and computer players
	for i in range(1, numh):
		players["Player " + str(i+1)] = Deck(("Player " + str(i+1)), 0, 1, 1, 0, ("Player " + str(((i+1)%5)+1)), ("Player " + str(((i-1)%5)+1)), [])
	for i in range(numh, (numh+numc)-1):
		players["Player " + str(i+1)] = Deck(("Player " + str(i+1)), 0, 1, 1, 1, ("Player " + str(((i+1)%5)+1)), ("Player " + str(((i-1)%5)+1)), [])
	if numh > 0 and numc > 0:
		players["Player 1"] = Deck(("Player 1"), 0, 1, 1, 0, ("Player 2"), ("Player " + str(numh+numc)), [])
		players["Player " + str(numh+numc)] = Deck(("Player " + str(numh+numc)), 0, 1, 1, 1, ("Player 1"), ("Player " + str(numh+numc-1)), [])
	elif numh > 0 and numc == 0:
		players["Player 1"] = Deck(("Player 1"), 0, 1, 1, 0, ("Player 2"), ("Player " + str(numh+numc)), [])
		players["Player " + str(numh+numc)] = Deck(("Player " + str(numh+numc)), 0, 1, 1, 0, ("Player 1"), ("Player " + str(numh+numc-1)), [])
	else:
		players["Player 1"] = Deck(("Player 1"), 0, 1, 1, 1, ("Player 2"), ("Player " + str(numh+numc)), [])
		players["Player " + str(numh+numc)] = Deck(("Player " + str(numh+numc)), 0, 1, 1, 1, ("Player 1"), ("Player " + str(numh+numc-1)), [])
	global maindeck
	global discarddeck
	maindeck = Deck('Main Deck', 0,0,0,1, '', '', [])
	discarddeck = Deck('Discard Pile', 0,0,0,1, '', '', [])
	setup.maindecksetup(maindeck)
	setup.dealhands(len(players), players, maindeck)

def clearscreen():
	#clears the UI
	AuD = system("clear")

def exitprogram():
	#ends program
	global runprogram 
	runprogram = False

def printmainmenu():
	#main menu UI
	clearscreen()
	print("Exploding Kittens\n")
	print("(P)lay Game")
	print("(H)ow to Play")
	print("(E)xit\n")

def mainmenu():
	#main menu, allows user to see how to play, exit, or play game
	check = True
	while check == True: 
		test = None
		while test in [None, '']:
			printmainmenu()
			test = str(input())
		test = test.upper()
		if test[0] in ['E', 'H', 'P']:
			check = False
		else:
			print("Please enter a proper response")
			blah = input()
	
	if test[0] == 'E':
		exitprogram()
	elif test[0] == 'H':
		howtoplay()
	else:
		gamesetup()

def printHtP():
	#opens rules url
	clearscreen()
	webbrowser.open('http://explodingkittens.com/how')
	print("\n (R)eturn to Menu")

def howtoplay():
	#opens rules url
	printHtP()
	test = str(input())

def printgamesetupH():
	#prints screen for user to pick num humans
	numplayers = None
	while numplayers not in ['0','1', '2', '3', '4', '5']:
		clearscreen()
		print("Game Setup\n")
		numplayers = str(input("Please enter the number of human players (0-5): "))
	numplayers = int(numplayers)
	return numplayers

def printgamesetupC(Humans):
	#prints screen for user to pick num computers
	Humans = 5 - Humans
	numplayers = None
	while numplayers not in ['0','1', '2', '3', '4', '5']:
		clearscreen()
		print("Game Setup\n")
		numplayers = str(input("Please enter the number of computer players (0-" + str(Humans) + "): "))
	numplayers = int(numplayers)
	return numplayers

def printproceedtogame(Humans, Computers):
	#print screen to proceed to game
	clearscreen()
	print("Game Setup\n")

	print("You have created " + str(Humans) + " human player(s) and " + str(Computers) + " computer player(s).\n")
	print("(P)lay Game")
	print("(C)hange the Number of Players")
	print("(R)eturn to Main Menu\n")

def gamesetup():
	#functionality to setup game
	gamesetuploop = True
	while gamesetuploop == True:
		numHplayers = printgamesetupH()
		check = True
		while check == True:
			numCplayers = printgamesetupC(numHplayers)
			if numCplayers >= 0 and numCplayers <= (5 - numHplayers):
				check = False
			else: 
				print("Please enter an appropriate number of players")
				blah = input()
		
		check = True 
		while check == True:
			test = None
			while test in [None, '']:
				printproceedtogame(numHplayers, numCplayers)
				test = str(input())
			test = test.upper()
			if test[0] in ['C', 'R', 'P']:
				check = False
			else:
				print("Please give an appropriate response")
				blah = input()
		
		if test[0] == 'C':
			players.clear()

		elif test[0] == 'P' and numHplayers+numCplayers >= 2:
			global gameover
			gameover = False
			global currentturn 
			currentturn = 'Player 1'
			gamesetuploop = False
			gamesetupfunction(numHplayers, numCplayers) #this is mechanics behind text
			with open('gamelog.txt', 'w') as f:
				for i in players:
					players[i].cards.sort()
					f.write(i + ": [")
					for j in players[i].cards:
						if j in defusecards:
							break
						else:
							f.write(findcardname(j) + ", ")
					f.write("Defuse]\n")

		elif test[0] == 'P' and numHplayers+numCplayers < 2:
			print("You must have at least two players to start the game.")
			blah = input()

		else:
			gamesetuploop = False

def printgamemainmenu(playerturn):
	#UI for game main menu
	clearscreen()
	print("Main Menu\n")
	print("There are " + str(len(maindeck.cards)) + " card(s) in the Deck")
	print("There are " + str(len(players)) + " players remaining\n")
	print("It is " + playerturn.name + "'s turn:\n")
	print("Pass the computer to " + playerturn.name + " (have player press Enter upon receiving computer)")
	print("(R)eturn to Main Menu\n")

def gamemainmenu(playerturn):
	#game main menu: public info before handing off to next player
	check = True
	while check == True:
		printgamemainmenu(playerturn)
		test = str(input())
		if test == '':
			check = False
		elif test.upper()[0] == 'R':
			check = False
		else:
			print("Please give an appropriate response")
			blah = input()

	if test == '' and playerturn.iscomp == 0:
		global turnover 
		turnover = False
		with open('gamelog.txt', 'at') as f:
			f.write(playerturn.name + "'s Turn: ")
	elif test == '' and playerturn.iscomp == 1:
		global compturn
		compturn = False
		with open('gamelog.txt', 'at') as f:
			f.write(playerturn.name + "'s Turn: ")
	else:
		global gameover 
		gameover = True
		players.clear()
		savegamelog()

def savegamelog():
	#save game log to new filename
	check = True
	while check == True:
		test = None
		while test in [None, '']:
			clearscreen()
			print("Would you like to save the game log to a new filename? (Y/N)")
			test = str(input())
		test = test.upper()
		if test[0] in ['Y', 'N']:
			check = False
	if test[0] == 'Y':
		check = True
		while check == True:
			clearscreen()
			print("Please enter the filename you wish to save the game log to: ")
			newtest = None
			while newtest in [None, '']:
				newtest = str(input())
			if len(newtest) > 4:
				if newtest[-4:] == '.txt':
					eh = False
					for i in newtest[:-4]:
						if i == '.':
							eh = True
							break
					if eh == False:
						check = False
						with open('gamelog.txt', 'rt') as f:
							with open(newtest, 'wt') as f1:
								for line in f:
									f1.write(line)
				else:
					eh = False
					for i in newtest:
						if i == '.':
							eh = True
							break
					if eh == False:
						check = False
						with open('gamelog.txt', 'rt') as f:
							with open(newtest + '.txt', 'wt') as f1:
								for line in f:
									f1.write(line)
			else:
				eh = False
				for i in newtest:
					if i == '.':
						eh = True
						break
				if eh == False:
					check = False
					with open('gamelog.txt', 'rt') as f:
						with open(newtest + '.txt', 'wt') as f1:
							for line in f:
								f1.write(line)


def printplayermainmenu(playerturn):
	#prints UI for player main menu
	clearscreen()
	print(playerturn.name + "'s Turn: Main Menu\n")
	print("There are " + str(len(maindeck.cards)) + " card(s) in the Deck\n")
	print("There are " + str(len(players)) + " players remaining\n")
	
	for i in players:
		if i == playerturn.name:
			pass
		else:
			print (i + (": ") + str(len(players[i].cards)) + " card(s)")

	print("\nThis is what you have in your hand:")
	playerturn.print_deck()
	
	print("\n(P)lay a card")
	print("(F)inish turn")
	print("(H)elp\n")

def playermainmenu(playerturn):
	#shows player's info - goes to finish turn, help, or play card
	check = True
	while check == True:
		test = None
		while test in [None, '']:
			printplayermainmenu(playerturn)
			test = str(input())
		test = test.upper()
		if test[0] in ['P','F','H']:
			check = False
		else:
			print("Please give an appropriate response")
			blah = input()

	if test[0] == 'P':
		playacard(playerturn)
	elif test[0] == 'F':
		finishturn(playerturn)
	else:
		playerhelp(playerturn)

def playerdead(playerturn):
	#if a player loses comes here to remove player and/or end game
	clearscreen()
	print(str(playerturn.name) + " has drawn an exploding kitten and does not have a defuse card.\n This player has lost the game.")
	
	if len(players) == 2:
		winner = playerturn.nextplayer
		print(winner + " has won the game! Congratulations!")
		blah = str(input())
		global gameover
		gameover = True
		global stfresult
		global discarded
		global eklocals
		eklocals = []
		stfresult = []
		discarded = []
		players.clear()

	else:
		for i in playerturn.cards:
			move_card(playerturn, discarddeck)
		global currentturn
		currentturn = playerturn.nextplayer
		pastplayer = playerturn.prevplayer
		players[pastplayer].nextplayer = playerturn.nextplayer
		players[currentturn].turn = 1
		players[currentturn].prevplayer = playerturn.prevplayer
		currentturn =  playerturn.prevplayer
		del players[playerturn.name]

	with open('gamelog.txt', 'at') as f:
		f.write('Dead, ')
	blah = input()
	if gameover == True:
		savegamelog()

def printreplaceek(playerturn):
	#prints UI for when player needs to place EK back into deck (after defusing)
	clearscreen()
	print(playerturn.name + " has drawn an exploding kitten and has used a defuse card to survive it.")
	print("\n" + playerturn.name + ", please enter where in the deck you'd like to place the exploding kitten, with 1 being the top card on the deck and " + str(len(maindeck.cards)+1) + " being the bottom card of the deck:")

def printCreplaceek(playerturn):
	#prints UI for when player has defuse to survive EK
	clearscreen()
	print(playerturn.name + " has drawn an exploding kitten and has used a defuse card to survive it.")
	
def placeek(playerturn):
	#functionality to place EK into deck after defusing
	check = True
	while check == True:	
		test = None
		while test in [None, '']:
			printreplaceek(playerturn)
			test = str(input())
		test = test.upper()
		if test[0] in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
			test = None
		else:
			test = int(test)
			if test < 1 or test > len(maindeck.cards)+1:
				print("Please give an appropriate response")
				blah = input()
			else:
				check = False
	return test

def compplaceek(playerturn):
	#computer call to place EK after defusing 
	hasd = 0
	printCreplaceek(playerturn)
	for i in playerturn.cards:
		if i in defusecards:
			hasd = 1
			break

	if len(maindeck.cards) == 0:
		v = 1
	elif len(discarded) >= len(players) and hasd == 1:
		v = random.randint(1, len(players)-1)
	elif len(discarded) < len(players) and hasd == 0:
		v = random.randint(int(len(maindeck.cards)*(4/5))+(len(maindeck.cards)%5 > 0), len(maindeck.cards))
	elif len(discarded) >= len(players) and hasd == 0:
		v = random.randrange(1, len(maindeck.cards)+1, int(len(players)/2)+(len(players)%2 > 0))
	else:
		v = random.randrange(1, len(maindeck.cards)+1, random.randint(1, len(players)-1))
	
	return v #do computer strategy

def printresolveek(test):
	#pring UI to show where EK has been placed
	print("The Exploding Kitten is now in the deck.\n(S)tart Next Turn")

def ek(playerturn, drawcard):
	#function to account for action if drawn card is EK
	foundcard = False
	for i in playerturn.cards:
		if i > 46:
			foundcard = True
			burncard = i
			playerturn.cards.remove(i)
			discarddeck.add_card(burncard)
			global discarded
			discarded.append(playerturn)
			with open('gamelog.txt', 'at') as f:
				f.write('[' + playerturn.name + ', ' + findcardname(i) + '], ')
			break
	
	if foundcard == False:
		playerdead(playerturn)

	else:
		global compturn
		if compturn == False:
			test = compplaceek(playerturn)
		else:
			test = placeek(playerturn)
		maindeck.cards.insert((test-1), drawcard)
		playerturn.eks.append(len(maindeck.cards)-(test-1))
		global eklocals
		eklocals.append(len(maindeck.cards)-(test-1))
		with open('gamelog.txt', 'at') as f:
			f.write('[' + playerturn.name + ', ' + findcardname(drawcard) + ', ' + str(test) + '], ')
		printresolveek(test)
		newtest = str(input())

def finishturn(playerturn):
	#function to finish turn and draw a card if necessary (and call EK function)
	if playerturn.iscomp == 0:
		print("Please return the computer so all players can view it:")
		blah = input()
	drawcard = None
	if playerturn.turn != 0:
		drawcard = maindeck.remove_card()
		playerturn.turn = playerturn.turn - 1
		with open('gamelog.txt', 'at') as f:
			f.write(findcardname(drawcard) + ', ')
		if drawcard < 53:
			playerturn.add_card(drawcard)
		else:
			ek(playerturn, drawcard)

	global turnover 
	global compturn
	turnover = True
	compturn = True

	if gameover == False:
		global currentturn
		playerturn = players[currentturn]
		if playerturn.turn == 0:
			currentturn = playerturn.nextplayer
			resetattack = playerturn.prevplayer
			players[resetattack].nextturn = 1
			players[currentturn].turn = playerturn.nextturn
		with open('gamelog.txt', 'at') as f:
			f.write('Turn finished.\n')
		global stfresult
		stfresult = []
		if len(players) == 1:
			players.clear()

def printcarddescription(i):
	#prints description of each card for player help menu
	if i in attackcards:
		print ('Attack card - Play this to not draw a card at the end of your turn, and force the next player to take two turns!\n')
	elif i in skipcards:
		print ('Skip card - Play this to not draw a card at the end of your turn!\n')
	elif i in nopecards:
		print ("Nope card - Play this to reject another player's move. You can't play this until someone else plays a card first!\n")
	elif i in favorcards:
		print ('Favor card - Play this to force another player to give you a card of their choice!\n')
	elif i in stfcards:
		print ('See the Future card - Play this to see the top three cards in the deck!\n')
	elif i in defusecards:
		print ('Defuse card - Play this only if you draw an Exploding Kitten!\n')
	elif i in shufflecards:
		print ('Shuffle card - Play this to shuffle the deck!\n')
	else:
		if i in TCcards:
			test = 'TacoCat'
		elif i in RCcards:
			test = 'Rainbow Cat'
		elif i in BCcards:
			test =  'Beard Cat'
		elif i in PCcards:
			test = 'Hairy Potato Cat'
		elif i in WCcards:
			test = 'Watermelon Cat'
		print (test + " card - Play this with 1 other " + test + " to draw a card from a player's hand at random!\nPlay this with 2 other " + test + "s to ask for a specific card from a player's hand! Be careful! If you ask for a card the player doesn't have you will get nothing!\n")

def printplayerhelp(playerturn):
	#UI for player help
	clearscreen()
	print(playerturn.name + "'s Turn: Help Menu\n")
	print ("You can do one of the following:")
	print ("1. Play a card or cards (you play cards one at a time)\n")
	print ("Your cards can do the following:\n")
	for i in playerturn.cards:
		printcarddescription(i)
	print ('\n2. Finish your turn, drawing a card from the deck unless otherwise specified in the cards played\n')
	print ('(R)eturn to Player Menu')

def playerhelp(playerturn):
	#shows what each card in player's hand does
	printplayerhelp(playerturn)
	test = str(input())

def printplaycardmenu(playerturn):
	#UI for playing a card
	clearscreen()
	print(playerturn.name + "'s Turn: Play Card Menu\n")
	print("There are " + str(len(maindeck.cards)) + " card(s) in the Deck\n")
	print("There are " + str(len(players)) + " players remaining\n")
	
	for i in players:
		if i == playerturn.name:
			pass
		else:
			print (i + (": ") + str(len(players[i].cards)) + " card(s)")

	print("\nThis is what you have in your hand:")
	playerturn.print_deck()
	
	print("\n(G)o Back to Player Menu")
	print("Enter which card you wish to play:\n")

def reportinvalid(playerturn):
	#UI for when player inputs invalid card or invalid response
	clearscreen()
	print(playerturn.name + "'s Turn: Main Menu\n")
	print("The card you've selected cannot be played now. If you need help go to Help in your player menu.")
	print("(R)eturn to Player Menu")
	test = str(input())

def reportsinvalid(playerturn):
	#UI for when player inputs an s but has mutliple cards starting with that letter
	clearscreen()
	print(playerturn.name + "'s Turn: Main Menu\n")
	print("You have entered a value starting with s, but you have multiple cards that start with that letter (or you do not have a card starting with S).\nPlease be specific in your entry.")
	print("(R)eturn to Player Menu")
	test = str(input())

def printcatcard(cardnum, playerturn, numcards):
	#UI for when card selected is a cat card
	clearscreen()
	name = findcardname(cardnum)
	print(playerturn.name + "'s Turn: Cat Card Menu\n")
	print("You have selected a " + name + ". This card can only be played with one or two more " + name + "(s).\n")
	print("Including the card you've played, you have " + str(numcards) + " " + name + "(s) in your hand.\n")
	print("Playing 2 " + name + "s will allow you to draw a card from a player's hand at random!\nPlaying 3 " + name + "s allow you to ask for a specific card from a player's hand! Be careful! If you ask for a card the player doesn't have you will get nothing!\n")
	print("(D)on't Play Cat Cards")
	print("Enter the number of " + name + " Cards you wish to play, INCLUDING the one you've already selected:")

def printplayagainst(cardname, playerturn):
	#UI for when user needs to play against another player
	clearscreen()
	print(playerturn.name + "'s Turn: Play Against Menu\n")
	if cardname[0] == 'F':
		print("You have selected a " + cardname + " card, which is played against another player.")
	else:
		print("You have selected " + cardname + " cards, which are played againts another player.")
	print("There are " + str(len(players)) + " players remaining\n")
	
	for i in players:
		if i == playerturn.name:
			pass
		else:
			print (i + (": ") + str(len(players[i].cards)) + " card(s)")
	print("\n(C)hange card choice")
	print("Enter the number of the player you wish to play against:")

def playagainst(cardname, playerturn):
	#has user pick a player to play a card or cards against
	fullwhile = False
	while fullwhile == False:
		check = False
		test = None
		while check == False:
			while test in [None, '']:
				printplayagainst(cardname, playerturn)
				test = str(input())
			test = test.upper()
			if test[0] in ['1','2','3','4','5','C']:
				check = True
			else:
				test = None
		playagainst = None
		if test == 'C':
			fullwhile = True
		else:
			test = int(test)
			for i in players:
				if int(players[i].name[-1]) == test and players[i].name != playerturn.name and len(players[i].cards) > 0:
					playagainst = players[i]
					fullwhile = True
					break
	return playagainst

def printcat3(cardname, playeragainst, playerturn):
	#UI for if user plays 3 cats and needs to request card
	clearscreen()
	print(playerturn.name + "'s Turn: 3 Cat Card Menu\n")
	print("You have selected 3 " + cardname + " cards to play against " + playeragainst.name + ".")
	print("Please enter which card type you want to ask from " + playeragainst.name + ". If " + playeragainst.name + " doesn't have the card you ask for you will get nothing:")

def cat3(cardname, playeragainst, playerturn):
	#has user pick card to request from another player having played 3 cat cards
	check = False
	test = None
	while check == False:
		while test in [None, '']:
			printcat3(cardname, playeragainst, playerturn)
			test = str(input())
		test = test.upper()
		if test[0] in ['A', 'B', 'D', 'F', 'H', 'N', 'R', 'S', 'T', 'W']:
			testdeck = Deck('Test Deck', 0,0,0,1, '', '', [])
			setup.maindecksetup(testdeck)
			setup.ingamedefuse(testdeck)
			cardnum = findcardnum(test, testdeck)
			check = True
		else:
			test = None
	cardname = findcardname(cardnum)
	return cardname

def catcard(cardnum, playerturn):
	#functionality for if card selected is cat card
	test = None
	numcards = 0
	if cardnum in TCcards:
		for i in playerturn.cards:
			if i in TCcards:
				numcards = numcards + 1
				ourlist = TCcards
	elif cardnum in WCcards:
		for i in playerturn.cards:
			if i in WCcards:
				numcards = numcards + 1
				ourlist = WCcards
	elif cardnum in PCcards:
		for i in playerturn.cards:
			if i in PCcards:
				numcards = numcards + 1
				ourlist = PCcards
	elif cardnum in RCcards:
		for i in playerturn.cards:
			if i in RCcards:
				numcards = numcards + 1
				ourlist = RCcards
	else:
		for i in playerturn.cards:
			if i in BCcards:
				numcards = numcards + 1
				ourlist = BCcards
	check = False
	while check == False:
		while test in [None, '']:
			printcatcard(cardnum, playerturn, numcards)
			test = str(input())
		test = test.upper()
		if test[0] in ['D', '2', '3']:
			check = True
		else:
			test = None
	if test[0] != 'D':
		numCats = int(test)
		cards = []
		for i in playerturn.cards:
			if i in ourlist:
				cards.append(i)
				numCats = numCats - 1
			if numCats == 0:
				break
		if numCats != 0:
			reportinvalid(playerturn)
			return None
		else:
			playeragainst = playagainst(findcardname(cardnum), playerturn)
			move = [playerturn, cards, playeragainst]
			if playeragainst == None:
				return 0
			elif len(cards) == 3 and playeragainst != None:
				cardrequest = cat3(findcardname(cardnum), playeragainst, playerturn)
				move = [playerturn, cards, playeragainst, cardrequest]
				return move
			else:
				return move
	else:
		return 0


def processcard(cardnum, playerturn):
	#takes card played and decides what it is and what functions need to be called
	catcards = TCcards + WCcards + PCcards + BCcards + RCcards
	if cardnum in catcards:
		move = catcard(cardnum, playerturn)
	elif cardnum in favorcards:
		playeragainst = playagainst(findcardname(cardnum), playerturn)
		move = [playerturn, cardnum, playeragainst]
		if playeragainst == None:
			move = 0
	else:
		move = [playerturn, cardnum]
	
	if move == None:
		reportinvalid(playerturn)
	
	elif move == 0:
		pass
	
	else:
		confirmcard(move)

def playacard(playerturn):
	#menu which takes in user input of a card name
	check = False
	cardnum = 0
	while check == False:
		test = None
		while test in [None, '']:
			printplaycardmenu(playerturn)
			test = str(input())
		test = test.upper()
		if test[0] in ['A', 'B', 'D', 'F', 'H', 'N', 'R', 'S', 'T', 'W']:
			cardnum = findcardnum(test, playerturn)
			check = True
		elif test[0] == 'G':
			check = True
	nolist = nopecards + defusecards
	if cardnum != 0 and cardnum not in nolist:
		processcard(cardnum, playerturn)
	elif check == True and cardnum == 0:
		pass
	else:
		reportinvalid(playerturn)

def printconfirmcard(move):
	#UI for confirm card
	playerturn = move[0]
	clearscreen()
	print(playerturn.name + "'s Turn: Confirm Card Menu\n")
	if isinstance(move[1], int):
		card = move[1]
		print("You have selected the following card: " + findcardname(card))
	else:
		cards = move[1]
		print("You have selected " + str(len(cards)) + " of the following cards: " + findcardname(cards[0]))
	if len(move) > 2:
		playeragainst = move[2]
		print("You have chosen to play your card(s) against " + playeragainst.name)
		if len(move) == 4:
			cardrequest = move[3]
			print("You have chosen to ask for the following card: " + cardrequest)

	print("\nDo you want to confirm playing this move? (Y/N)")

def confirmcard(move):
	#menu to confirm player card choice with Y or N. after this the move cannot be taken back
	check = False
	while check == False:
		test = None
		while test in [None, '']:
			printconfirmcard(move)
			test = str(input())
		test = test.upper()
		if test[0] in ['Y', 'N']:
			check = True
	if test[0] == 'Y':
		print("Please return the computer so all players can view it:")
		blah = input()
		
		if isinstance(move[1], int) and move[1] in nopecards: 
			return 1
		else:
			nopemenu(move)

	elif test[0] == 'N' and isinstance(move[1], int) and move[1] in nopecards:
		return 0


def printnopemenu(move, numnopes):
	#UI for when all players have opportunity to Nope a move
	clearscreen()
	print(move[0].name + "'s Turn: Nope Menu\n")
	if type(move[1]) == int:
		if len(move) == 2:
			print(move[0].name + " has played 1 " + findcardname(move[1]) + " card.\n")
		else:
			print(move[0].name + " has played 1 " + findcardname(move[1]) + " card against " + move[2].name + ".\n")
	else:
		if len(move) == 3:
			print(move[0].name + " has played " + str(len(move[1])) + " " + findcardname(move[1][0]) + " cards against " + move[2].name + ".\n")
		else:
			print(move[0].name + " has played " + str(len(move[1])) + " " + findcardname(move[1][0]) + " cards against " + move[2].name + ", and is requesting 1 " + move[3] + " card. \n")
	
	if numnopes == 1:
		print(str(numnopes) + " Nope card has been played, negating " + move[0].name + "'s move.\n")
	elif numnopes%2 == 1 and numnopes != 1:
		print(str(numnopes) + " Nope cards have been played, negating " + move[0].name + "'s move.\n")	
	else:
		print(str(numnopes) + " Nope cards have been played. " + move[0].name + "'s move is still active.\n")

	print("Would any player like to play a Nope? (Y/N). You have 10 seconds to respond")

def discardmove(move):
	#functionality to remove played cards from a user's hand and move them into discard deck (and writes move to file)
	if type(move[1]) == int:
		for i in move[0].cards:
			if i == move[1]:
				val = i
				discarddeck.add_card(val)
				move[0].cards.remove(i)
				break
		if len(move) == 2:
			with open('gamelog.txt', 'at') as f:
				f.write('[' + move[0].name + ', ' + findcardname(move[1]) + '], ')
		else:
			with open('gamelog.txt', 'at') as f:
				f.write('[' + move[0].name + ', ' + findcardname(move[1]) + ', ' + move[2].name + '], ')
	else:
		cardss = findcardname(move[1][0])
		for i in move[1]:
			discarddeck.add_card(i)
			move[0].cards.remove(i)
		namestring = ((cardss + ', ')*(len(move[1])-1)) + cardss
		if len(move) == 3:
			with open('gamelog.txt', 'at') as f:
				f.write('[' + move[0].name + ', [' + namestring + '], ' + move[2].name + '], ')
		else:
			with open('gamelog.txt', 'at') as f:
				f.write('[' + move[0].name + ', [' + namestring + '], ' + move[2].name + ', ' + move[3] + '], ')

def validatenope():
	#function to check if player has nope and confirms if nope will be played
	numnopes = 0
	print("Please pass the computer to the player who wishes to play a Nope card.")
	blah = str(input())
	check = False
	while check == False:
		playernum = None
		while playernum in [None, '']:
			clearscreen()
			print("(D)on't Play Nope")
			playernum = str(input("Please enter your player number: "))
		if playernum in ['1', '2', '3', '4', '5']:
			playernum = 'Player ' + playernum
			if playernum in players:
				playerturn = players[playernum]
				confirm = None
				test = None
				for i in playerturn.cards:
					if i in nopecards:
						move = [playerturn, i]
						confirm = confirmcard(move)
						test = True
						break
				if confirm == 1:
					discardmove(move)
					numnopes = 1
					check = True
				if playerturn.iscomp == 1:
					test = False
				
				elif test != True:
					print("You do not have a Nope card.")
					check = True
					numnopes = 0
					print("Please return the computer so all players can view it: ")
					blah = str(input())


		elif playernum[0].upper() == 'D':
			check = True
			numnopes = 0
			print("Please return the computer so all players can view it: ")
			blah = str(input())
	return numnopes


def nopemenu(move):
	#function which loops over for as long as players want to nope move
	nopeloop = False
	numnopes = 0
	while nopeloop == False:
		eh = False
		prenope = numnopes
		numnopes = numnopes + compnope(move, numnopes)
		check = True
		for i in players:
			if players[i].iscomp == 0:
				check = False
				eh = True
				break
		if eh == False and prenope == numnopes:
			nopeloop = True
		if eh == True:
			timer = threading.Timer(10.0, _thread.interrupt_main)
			try:
				timer.start()
				while check == False:
					test = None
					while test in [None, '']:
						printnopemenu(move, numnopes)
						test = str(input())
					test = test.upper()
					if test[0] in ['Y', 'N']:
						check = True
			except:
				print("Oh no! No one provided an answer within 10 seconds! Press enter to continue: ")
				blah = str(input())
				test = 'N'
				break
			timer.cancel()
			if test[0] == 'N':
				nopeloop = True
			else:
				numnopes = numnopes + validatenope()
	
	if numnopes%2 == 1:
		discardmove(move)
	else:
		discardmove(move)
		executemove(move)

def executemove(move):
	#function which takes move after nopes and executes it (if not nulled by Nopes)
	playerturn = move[0]
	if type(move[1]) == int:
		card = move[1]
		if len(move) == 3:
			playeragainst = move[2]
			if len(playeragainst.cards) != 0:
				executefunctions.favor(playerturn, playeragainst)
			if playerturn.iscomp == 0:
				print("Please return computer to " + playerturn.name + ".")
				blah = str(input())
		else:
			executefunctions.analyzecard(playerturn, card, maindeck)
			if card in shufflecards:
				global stfresult
				global eklocals
				stfresult = []
				eklocals = []
				for i in players:
					players[i].eks = []
			if card in stfcards and playerturn.iscomp == 1:
				if len(maindeck.cards) < 3:
					for i in range(0, len(maindeck.cards)):
						x = maindeck.cards[i]
						stfresult.append(x)
						if x in ekcards:
							playerturn.eks.append(len(maindeck.cards)-(len(stfresult)-1))
				else:
					for i in range (0, 3):
						x = maindeck.cards[i]
						stfresult.append(x)
						if x in ekcards:
							playerturn.eks.append(len(maindeck.cards)-(len(stfresult)-1))

	elif len(move[1]) == 2:
		cards = move[1]
		playeragainst = move[2]
		if len(playeragainst.cards) != 0:
			executefunctions.randcat(playerturn, playeragainst)
		if playerturn.iscomp == 0:
			print("Please return computer to " + playerturn.name + ".")
			blah = str(input())
	else:
		cards = move[1]
		playeragainst = move[2]
		cardagainst = move[3]
		if len(playeragainst.cards) != 0:
			executefunctions.activate3cat(playerturn, playeragainst, cardagainst)
		if playerturn.iscomp == 0:
			print("Please return computer to " + playerturn.name + ".")
		blah = str(input())


def complaynope(playerturn):
	#once AI has committed to noping this actually plays nope (from compnope)
	numnopes = 0
	for i in playerturn.cards:
		if i in nopecards:
			move = [playerturn, i]
			discardmove(move)
			numnopes = 1
			break
	return numnopes

def compnope(move, numnopes):
	#function to check computer players to see if they wish to nope move
	newnumnopes = 0
	for i in players:
		x = calcprob(move[0])
		if players[i].iscomp == 1:
			if i == move[0].name:
				if numnopes%2==1 and x==1:
					newnumnopes = complaynope(players[i])
					break
			elif len(move)>2 and move[2].name == i:
				if numnopes % 2 == 0 and (len(move) == 4 or x==1):
					newnumnopes = complaynope(players[i])
					break
			else:
				q = 0
				for jj in range(0,18):
					z = calcprob(move[0])
					q = q + z
				if q > 5:
					newnumnopes = complaynope(players[i])
					break
	return newnumnopes





def calcprob(playerturn):
	#creates odds to see how likely computer is to draw EK, and then likelihood of acting on that, while avoiding absolutes
	global eklocals
	for i in playerturn.eks:
		if i > len(maindeck.cards):
			playerturn.eks.remove(i)
	for j in eklocals:
		if j > len(maindeck.cards) + 2:
			eklocals.remove(j)
	eklocals = list(set(eklocals))

	y = float(((len(players)-1) - len(playerturn.eks))/len(maindeck.cards))
	if (len(maindeck.cards) + 2 in eklocals or len(maindeck.cards) + 1 in eklocals or len(maindeck.cards) in eklocals or len(maindeck.cards) - 1 in eklocals or len(maindeck.cards) - 2 in eklocals) and y < .4 and playerturn.turn != 0:
		checkplay = prob(70)
	elif playerturn.turn == 0 or y == 0:
		checkplay = 0
	elif y < .1:
		checkplay = prob(5)
	elif y < .15:
		checkplay = prob(15)
	elif y < .2:
		checkplay = prob(25)
	elif y < .25:
		checkplay = prob(35)
	elif y < .3:
		checkplay = prob(45)
	elif y < .35:
		checkplay = prob(55)
	elif y < .4:
		checkplay = prob(65)
	elif y < .45:
		checkplay = prob(75)
	elif y < .5:
		checkplay = prob(85)
	elif y < .55:
		checkplay = prob(95)
	else:
		checkplay = 1
	return checkplay

def createplay(playerturn):
	#designs a move
	playeragainst = playerturn
	cardrequest = findcardname(55)
	for i in players:
		if players[i] not in discarded:
			playeragainst = players[i]
			cardrequest = findcardname(47)
			break
	while playeragainst == playerturn:
		v = random.randint(0,5)
		if len(players) == 2:
			for z in players:
				if z[-1] != playerturn.name[-1]:
					playeragainst = players[z]
					break
		for z in players:
			if int(z[-1]) == v and z[-1] != playerturn.name[-1] and len(players[z].cards) > 0:
				playeragainst = players[z]
	move = []
	goodcards = attackcards + skipcards + shufflecards + stfcards
	badcards = nopecards+defusecards
	while move == []:
		playerturn.shuffle_deck()
		x = playerturn.cards[0]
		if x in badcards:
			continue
		elif x in stfcards and stfresult != []:
			continue
		elif x in goodcards:
			move = [playerturn, x]
		elif x in favorcards:
			move = [playerturn, x, playeragainst]
		elif x in TCcards:
			for j in playerturn.cards:
				if j in TCcards and j != x:
					cards = [x, j]
					if cardrequest[0] == 'E':
						move = [playerturn, cards, playeragainst]
						break
					else:
						for k in playerturn.cards:
							if k in TCcards and k != j and k != x:
								cards = [x, j, k]
								move = [playerturn, cards, playeragainst, cardrequest]
								break
					if move == []:
						move = [playerturn, cards, playeragainst]
						break
		elif x in WCcards:
			for j in playerturn.cards:
				if j in WCcards and j != x:
					cards = [x, j]
					if cardrequest[0] == 'E':
						move = [playerturn, cards, playeragainst]
						break
					else:
						for k in playerturn.cards:
							if k in WCcards and k != j and k != x:
								cards = [x, j, k]
								move = [playerturn, cards, playeragainst, cardrequest]
								break
					if move == []:
						move = [playerturn, cards, playeragainst]
						break
		elif x in PCcards:
			for j in playerturn.cards:
				if j in PCcards and j != x:
					cards = [x, j]
					if cardrequest[0] == 'E':
						move = [playerturn, cards, playeragainst]
						break
					else:
						for k in playerturn.cards:
							if k in PCcards and k != j and k != x:
								cards = [x, j, k]
								move = [playerturn, cards, playeragainst, cardrequest]
								break
					if move == []:
						move = [playerturn, cards, playeragainst]
						break
		elif x in BCcards:
			for j in playerturn.cards:
				if j in BCcards and j != x:
					cards = [x, j]
					if cardrequest[0] == 'E':
						move = [playerturn, cards, playeragainst]
						break
					else:
						for k in playerturn.cards:
							if k in BCcards and k != j and k != x:
								cards = [x, j, k]
								move = [playerturn, cards, playeragainst, cardrequest]
								break
					if move == []:
						move = [playerturn, cards, playeragainst]
						break
		elif x in RCcards:
			for j in playerturn.cards:
				if j in RCcards and j != x:
					cards = [x, j]
					if cardrequest[0] == 'E':
						move = [playerturn, cards, playeragainst]
						break
					else:
						for k in playerturn.cards:
							if k in RCcards and k != j and k != x:
								cards = [x, j, k]
								move = [playerturn, cards, playeragainst, cardrequest]
								break
					if move == []:
						move = [playerturn, cards, playeragainst]
						break
	return move

def canplay(playerturn):
	#calculates if the computer can physically make a move
	x = 0
	checkone = attackcards + shufflecards + skipcards
	for i in playerturn.cards:
		if i in checkone:
			x = 1
			break
		elif i in favorcards:
			z = 0
			for j in players:
				if len(players[j].cards)>0 and j != playerturn:
					z = 1
					break
			if z == 1:
				x = 10
				break
		elif i in stfcards and stfresult == []:
			x = 2
			break
		elif i in TCcards:
			for j in playerturn.cards:
				if j in TCcards and j != i:
					z = 0
					for r in players:
						if len(players[r].cards)>0 and r != playerturn:
							z = 1
							break
					if z == 1:
						x = 3
						break
		elif i in WCcards:
			for j in playerturn.cards:
				if j in WCcards and j != i:
					z = 0
					for r in players:
						if len(players[r].cards)>0 and r != playerturn:
							z = 1
							break
					if z == 1:
						x = 3
						break
		elif i in PCcards:
			for j in playerturn.cards:
				if j in PCcards and j != i:
					z = 0
					for r in players:
						if len(players[r].cards)>0 and r != playerturn:
							z = 1
							break
					if z == 1:
						x = 3
						break
		elif i in BCcards:
			for j in playerturn.cards:
				if j in BCcards and j != i:
					z = 0
					for r in players:
						if len(players[r].cards)>0 and r != playerturn:
							z = 1
							break
					if z == 1:
						x = 3
						break
		elif i in RCcards:
			for j in playerturn.cards:
				if j in RCcards and j != i:
					z = 0
					for r in players:
						if len(players[r].cards)>0 and r != playerturn:
							z = 1
							break
					if z == 1:
						x = 3
						break
	return x

def willplay(playerturn):
	#decides if computer will play a card
	x = canplay(playerturn)
	if x == 0:
		return 0
	else:
		checkplay = calcprob(playerturn)
		if len(maindeck.cards) in playerturn.eks and playerturn.turn != 0:
			checkplay = 1

		if checkplay == 1:
			x = createplay(playerturn)
			return x
		else:
			return 0
	

def playcompturn(playerturn):
	#function to execute computer player turn
	clearscreen()
	move = willplay(playerturn)
	if type(move) == int:
		finishturn(playerturn)
	else:
		nopemenu(move)

runprogram = True
gameover = True
turnover = True
compturn = True
players = {}
currentturn = ''
stfresult = []
discarded = []
eklocals = []
while runprogram == True:
	mainmenu()
	while gameover == False:
		gamemainmenu(players[currentturn])
		while turnover == False:
			playermainmenu(players[currentturn])
		while compturn == False:
			playcompturn(players[currentturn])