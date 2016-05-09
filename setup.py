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

def move_card(deck1, deck2):
	#move card from one deck to another using built in functions
	deck2.add_card(deck1.remove_card())

def maindecksetup(maindeck):
	#in game setup this adds all cards minus defuse and Ek's to maindeck
	for i in range(len(attackcards)):
		maindeck.add_card(attackcards[i])

	for i in range(len(skipcards)):
		maindeck.add_card(skipcards[i])

	for i in range(len(nopecards)):
		maindeck.add_card(nopecards[i])

	for i in range(len(favorcards)):
		maindeck.add_card(favorcards[i])

	for i in range(len(shufflecards)):
		maindeck.add_card(shufflecards[i])

	for i in range(len(stfcards)):
		maindeck.add_card(stfcards[i])

	for i in range(len(TCcards)):
		maindeck.add_card(TCcards[i])

	for i in range(len(WCcards)):
		maindeck.add_card(WCcards[i])

	for i in range(len(BCcards)):
		maindeck.add_card(BCcards[i])

	for i in range(len(RCcards)):
		maindeck.add_card(RCcards[i])

	for i in range(len(PCcards)):
		maindeck.add_card(PCcards[i])

def adddefuse(numplayers, defuselist, players):
	#adds defuse to each players hand
	if numplayers == 5:
		players['Player 1'].add_card(47)
		players['Player 2'].add_card(48)
		players['Player 3'].add_card(49)
		players['Player 4'].add_card(50)
		players['Player 5'].add_card(51)
		defuselist.remove(47)
		defuselist.remove(48)
		defuselist.remove(49)
		defuselist.remove(50)
		defuselist.remove(51)
	elif numplayers == 4:
		players['Player 1'].add_card(52)
		players['Player 2'].add_card(47)
		players['Player 3'].add_card(48)
		players['Player 4'].add_card(49)
		defuselist.remove(52)
		defuselist.remove(47)
		defuselist.remove(48)
		defuselist.remove(49)
	elif numplayers == 3:
		players['Player 1'].add_card(50)
		players['Player 2'].add_card(51)
		players['Player 3'].add_card(52)
		defuselist.remove(50)
		defuselist.remove(51)
		defuselist.remove(52)
	elif numplayers == 2:
		players['Player 1'].add_card(48)
		players['Player 2'].add_card(49)
		defuselist.remove(48)
		defuselist.remove(49)
	else:
		players['Player 1'].add_card(49)
		defuselist.remove(49)

def ingamedefuse(deck):
	#functionality for dealing with defuse with EK process
	for i in range(len(defusecards)):
		deck.add_card(defusecards[i])

def dealhands(numplayers, players, maindeck):
	#deals out hands and adds extra defuses and right # of EK's to maindeck
	defuselist = [47, 48, 49, 50, 51, 52] #used for dealing purposes only, use defusecards for reference
	adddefuse(numplayers, defuselist, players)
	
	for i in range (len(defuselist)):
		maindeck.add_card(defuselist[i])
	maindeck.shuffle_deck()


	if numplayers == 5:
		for i in range(0,4):
			move_card(maindeck, players['Player 1'])
			move_card(maindeck, players['Player 2'])
			move_card(maindeck, players['Player 3'])
			move_card(maindeck, players['Player 4'])
			move_card(maindeck, players['Player 5'])
	elif numplayers == 4:
		for i in range(0,4):
			move_card(maindeck, players['Player 1'])
			move_card(maindeck, players['Player 2'])
			move_card(maindeck, players['Player 3'])
			move_card(maindeck, players['Player 4'])
	elif numplayers == 3:
		for i in range(0,4):
			move_card(maindeck, players['Player 1'])
			move_card(maindeck, players['Player 2'])
			move_card(maindeck, players['Player 3'])
	elif numplayers == 2:
		for i in range(0,4):
			move_card(maindeck, players['Player 1'])
			move_card(maindeck, players['Player 2'])
	else:
		for i in range(0,4):
			move_card(maindeck, players['Player 1'])


	for i in range(numplayers-1):
		maindeck.add_card(ekcards[i])
	maindeck.shuffle_deck()