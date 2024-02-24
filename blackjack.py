import random
import time
import json

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DECK

card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] 
deck = [(card, category) for category in card_categories for card in cards_list] 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#WIN/LOSS

def readwin():
	with open("winlossblackjack.json", "r") as f:
		jayson = json.load(f)
		win = jayson.get("win", None)
		return win
def readloss():
	with open("winlossblackjack.json", "r") as f:
		jayson =  json.load(f)
		loss = jayson.get("loss", None)
		return loss
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#FUNCTIONS
	
def card_value(card): 
	if card[0] in ['Jack', 'Queen', 'King']: 
		return 10
	elif card[0] == 'Ace': 
		return 11
	else: 
		return int(card[0]) 

def hand_to_string(hand):
	x_ystuff = ""
	for x, y in hand:
		x_ystuff = x_ystuff + x + " of " + y + ". "
	return x_ystuff

def hitstay(hitstaychoice):
	if hitstaychoice == "hit":
		another_card = deck.pop()
		player.append(another_card)
	elif hitstaychoice == "stay":
		return hitstaychoice
	
def deal_hands(deck):
	player = [deck.pop(), deck.pop()]
	dealer = [deck.pop(), deck.pop()]
	return player, dealer

def handscore(hand):
	score = 0
	acecheck = 0
	for card in hand:
		score += card_value(card)
		if card[0] == "Ace":
			acecheck +=1
		if score > 21 and acecheck >= 1:
			score -= (acecheck * 10)
			acecheck = 0
	return score

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#GAME START

win = readwin()
loss = readloss()
print(f"Player has {win} wins.")
print(f"Dealer has {loss} wins.")
random.shuffle(deck)
print(f"*Dealing Cards*")
time.sleep(3)
player, dealer = deal_hands(deck)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#GAME LOOP

while True:
#PLAYER TURN
	player_score = handscore(player)
	dealer_score = handscore(dealer)
	dealers_hand = hand_to_string(dealer)
	players_hand = hand_to_string(player)
	print(f"You have: {players_hand}Your score is {player_score}.")
#PLAYER HIT OR STAY
	hitstaychoice = input(f"Do you want to hit or stay? ")
	hitstayresults = hitstay(hitstaychoice)
	players_hand = hand_to_string(player)
	if hitstaychoice == "hit":
		players_hand = hand_to_string(player)
		player_score = handscore(player)
		print(f"*Dealing another card*")
		time.sleep(3)
		if player_score > 21:
			print(f"You bust. You have: {players_hand}Your score is {player_score}.")
			loss += 1
			break
		if player_score < 21:
			continue
	if hitstaychoice == "stay":
		print(f"You have {players_hand}Your score is {player_score}.")
		print(f"Dealer has {dealers_hand}Their score is {dealer_score}.")
		break
#COMPUTER TURN
while hitstayresults == "stay":
	if dealer_score < 21 and player_score > dealer_score:
		another_card = deck.pop()
		dealer.append(another_card)
		dealer_score = handscore(dealer)
		dealers_hand = hand_to_string(dealer)
		print(f"*Dealing another card*")
		time.sleep(3)
		print(f"Dealer has: {dealers_hand}Their score is {dealer_score}")
	if dealer_score > 21: 
		win += 1
		print(f"Dealer Busts! Their hand is: {dealers_hand}Dealer has {dealer_score}.")
		break
	if dealer_score > player_score: 
		loss += 1
		print(f"Dealer wins. Player has {player_score}. Dealer has {dealer_score}.") 
		break
	if player_score == dealer_score:
		print(f"House wins on Ties. Player has {player_score}. Dealer has {dealer_score}.") 
		break

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#UPDATE WIN LOSS
with open("winlossblackjack.json", "r+") as f:
	jason =  json.load(f)
	jason["win"] = win
	jason["loss"] = loss
	f.seek(0)
	json.dump(jason, f)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#TODO save original file for future reference. Adjust the twitchbot file to add blackjack
	
		






	


	
	
	
	
	
	


	
	
