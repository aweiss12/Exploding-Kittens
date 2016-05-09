from os import system
from random import randint

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
	#finds card name based on number value
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

def findcardnum(test, playerturn):
	#finds card num in players hand based on name
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

def clearscreen():
	#clears screen
	AuD = system("clear")

def move_card(deck1, deck2):
	#move card from one deck to another using built in methods
	deck2.add_card(deck1.remove_card())

def analyzecard(playerturn, card, maindeck):
	#based on card played redirects to appropriate execution function
	if card in attackcards:
		attack(playerturn)
		if playerturn.iscomp == 0:
			print("Please return computer to " + playerturn.name + ".")
			blah = str(input())
	elif card in skipcards:
		skip(playerturn)
		if playerturn.iscomp == 0:
			print("Please return computer to " + playerturn.name + ".")
			blah = str(input())
	elif card in shufflecards:
		playshuffle(maindeck)
		if playerturn.iscomp == 0:
			print("Please return computer to " + playerturn.name + ".")
			blah = str(input())
	else:
		stf(maindeck, playerturn)


def attack(playerturn):
	#acts as attack card
	playerturn.turn = 0
	playerturn.nextturn = 2

def skip(playerturn):
	#acts as skip card
	if playerturn.turn > 0:
		playerturn.turn = playerturn.turn - 1

def playshuffle(maindeck):
	#acts as shuffle card
	maindeck.shuffle_deck()

def printstf(stf, playerturn):
	#UI for stf
	clearscreen()
	print(playerturn.name + "'s Turn: See the Future\n")

	print("These are the top three cards in the deck:")
	stf.print_deck_stf()
	print("\nPress enter when you are done looking at these cards")
	blah = str(input())

def stf(maindeck, playerturn):
	#acts as stf card
	if playerturn.iscomp == 0:
		print("Please pass the computer to " + playerturn.name + ".")
		blah = str(input())
		STF = Deck('STF', 0, 0, 0, 1, '', '', [])
		if len(maindeck.cards) > 2:
			for i in range (0, 3):
				move_card(maindeck, STF)
			printstf(STF, playerturn)
			STF.cards.reverse()
			for i in range (0,3):
				move_card(STF, maindeck)
		else:
			for i in range (0, len(maindeck.cards)):
				move_card(maindeck, STF)
			printstf(STF, playerturn)
			STF.cards.reverse()
			for i in range (0,len(maindeck.cards)):
				move_card(STF, maindeck)

def printfavor(playerturn, playeragainst):
	#ui for favor
	clearscreen()
	print(playerturn.name + "'s Turn: Favor Request\n")

	print(playeragainst.name + ", this is what you have in your hand:")
	playeragainst.print_deck()
	
	print("\nPlease enter which card you would like to give up to " + playerturn.name + ": ")

def favor(playerturn, playeragainst):
	#acts as favor card
	if playeragainst.iscomp == 0:
		print("Please pass the computer to " + playeragainst.name + ".")
		blah = str(input())
		check = True
		while check == True:
			test = None
			while test in [None, '']:
				printfavor(playerturn, playeragainst)
				test = str(input())
			test = test.upper()
			card = findcardnum(test, playeragainst)
			if card != 0:
				check = False
			else:
				print("Please give an appropriate response")
				blah = str(input())
	else:
		Ascore = 0
		Skscore = 0
		Shscore = 0
		Stfscore = 0 
		NScore = 0
		Fscore = 0
		Dscore = 0
		TCscore = 0
		WCscore = 0
		PCscore = 0
		BCscore = 0
		RCscore = 0
		for i in playeragainst.cards:
			if i in TCcards:
				TCscore = (TCscore + 1)%3
			elif i in WCcards:
				WCscore = (WCscore + 1)%3
			elif i in PCcards:
				PCscore = (PCscore + 1)%3
			elif i in BCcards:
				BCscore = (BCscore + 1)%3
			elif i in RCcards:
				RCscore = (RCscore + 1)%3
			elif i in attackcards:
				Ascore = Ascore + 1
			elif i in skipcards:
				Skscore = Skscore + 1
			elif i in shufflecards:
				Shscore = Shscore + 1
			elif i in stfcards:
				Stfscore = Stfscore + 1
			elif i in nopecards:
				NScore = NScore + 1
			elif i in favorcards:
				Fscore = Fscore + 1
			else:
				Dscore = Dscore + 1
		if Dscore == len(playeragainst.cards):
			for i in defusecards:
				if i in playeragainst.cards:
					card = i
					break
		elif TCscore == 1:
			for i in TCcards:
				if i in playeragainst.cards:
					card = i
					break
		elif WCscore == 1:
			for i in WCcards:
				if i in playeragainst.cards:
					card = i
					break
		elif PCscore == 1:
			for i in PCcards:
				if i in playeragainst.cards:
					card = i
					break
		elif BCscore == 1:
			for i in BCcards:
				if i in playeragainst.cards:
					card = i
					break
		elif RCscore == 1:
			for i in RCcards:
				if i in playeragainst.cards:
					card = i
					break
		elif Shscore > 1:
			for i in shufflecards:
				if i in playeragainst.cards:
					card = i
					break
		elif Stfscore > 1:
			for i in stfcards:
				if i in playeragainst.cards:
					card = i
					break
		elif NScore > 1:
			for i in nopecards:
				if i in playeragainst.cards:
					card = i
					break
		elif Shscore == 1:
			for i in shufflecards:
				if i in playeragainst.cards:
					card = i
					break
		elif Stfscore == 1:
			for i in stfcards:
				if i in playeragainst.cards:
					card = i
					break
		elif TCscore == 2:
			for i in TCcards:
				if i in playeragainst.cards:
					card = i
					break
		elif WCscore == 2:
			for i in WCcards:
				if i in playeragainst.cards:
					card = i
					break
		elif PCscore == 2:
			for i in PCcards:
				if i in playeragainst.cards:
					card = i
					break
		elif BCscore == 2:
			for i in BCcards:
				if i in playeragainst.cards:
					card = i
					break
		elif RCscore == 2:
			for i in RCcards:
				if i in playeragainst.cards:
					card = i
					break
		elif Skscore > 0:
			for i in skipcards:
				if i in playeragainst.cards:
					card = i
					break	
		elif Ascore > 0:
			for i in attackcards:
				if i in playeragainst.cards:
					card = i
					break
		elif Fscore > 0:
			for i in favorcards:
				if i in playeragainst.cards:
					card = i
					break
		else:
			playeragainst.shuffle_deck()
			for i in playeragainst.cards:
				if i not in defusecards:
					card = i
					break

	playeragainst.cards.remove(card)
	playerturn.add_card(card)
	with open('gamelog.txt', 'at') as f:
		f.write('[' + playeragainst.name + ', ' + findcardname(card) + ', ' +  playerturn.name + '], ')
		f.close()

def printrandcat(playerturn, playeragainst):
	#ui for 2 cat cards
	clearscreen()
	print(playerturn.name + "'s Turn: 2 Cat Card Menu\n")
	print(playeragainst.name + " has " + str(len(playeragainst.cards)) + " cards in their hand.")
	print("Please enter which card you want between 1 and " + str(len(playeragainst.cards)) + ": ")
def randcat(playerturn, playeragainst):
	#acts as 2 cat cards
	playeragainst.shuffle_deck()
	if playerturn.iscomp == 0:
		print("Please pass the computer to " + playerturn.name + ".")
		blah = str(input())
		check = False
		while check == False:
			test = None
			while test in [None,'']:
				printrandcat(playerturn, playeragainst)
				test = str(input())
			if test in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']:
				check = True
				test = int(test)
	else:
		test = randint(1,len(playeragainst.cards))
	i = playeragainst.cards[test-1]
	playeragainst.cards.remove(i)
	playerturn.add_card(i)
	with open('gamelog.txt', 'at') as f:
		f.write('[' + playeragainst.name + ', ' + findcardname(i) + ', ' +  playerturn.name + '], ')
		f.close()

		
def print3cat(playerturn,playeragainst,cardagainst, success):
	#UI for 3 cat cards
	clearscreen()
	print(playerturn.name + "'s Turn: 3 Cat Card Menu\n")
	if success == 1:
		print(playerturn.name + " has successfully taken a " + cardagainst + " from " + playeragainst.name + ". ")
	else:
		print(playerturn.name + " has failed to take a " + cardagainst + " from " + playeragainst.name + ". ")
def activate3cat(playerturn, playeragainst, cardagainst):
	#acts as 3 cat cards
	check = True
	for i in playeragainst.cards:
		if findcardname(i) == cardagainst:
			playerturn.add_card(i)
			playeragainst.cards.remove(i)
			print3cat(playerturn, playeragainst, cardagainst, 1)
			check = False
			break
	if check == True:
		print3cat(playerturn, playeragainst, cardagainst, 0)

	with open('gamelog.txt', 'at') as f:
		f.write('[' + playeragainst.name + ', ' + cardagainst + ', ' +  playerturn.name + '], ')
		f.close()