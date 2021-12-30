import random
def shuffle(cardstack): #shuffle deck
	cardstack_shuffle = random.shuffle(cardstack)

def check_racko(rack): #check to see if either hand is in ascending order
	for i in range(len(rack)):
		if rack[i] == rack[-1]:
			if rack[-1] > rack[-2]:
				return True
			else:
				return False
		if rack[i] > rack[i+1]:
			return False

def get_top_card(card_stack): #remove top card from deck, eventually starts discard pile
	top_card = card_stack.pop() #pops last element which is top card
	return top_card

def deal_initial_hands(deck): #deals both hands witching off between cpu and user
	user = []
	computer = []
	for i in range(20):
		if i % 2 != 0:
			user.append(deck.pop())
			
		else:
			computer.append(deck.pop())
		
	return (user, computer)

def print_top_to_bottom(rack): #prints either hand from top to bottom
	for i in rack:
		print(i)


def find_and_replace(new_card, card_to_be_replaced, hand, discard,deck): #finds the card that the player wants to replace, and puts nely selecte card in that index
	if card_to_be_replaced in hand: 
		location_of_card = hand.index(card_to_be_replaced)
		hand[location_of_card] = new_card
		if new_card in discard:
			discard.remove(new_card)
			discard.insert(-1,card_to_be_replaced)

		else:
			deck.remove(new_card)
			discard.insert(-1,card_to_be_replaced)
		
	else:
		print("Please select a valid card. \n ")
		card_to_be_replaced = int(input("What card do you want to kick out? "))
		find_and_replace(new_card, card_to_be_replaced, hand, discard, deck)


def computer_play(hand, deck, discard): #computer strategy
	check_tower = [False] * 10 
	for i in range(10): #checks if hand has cards in certain range
		if hand[i] >= (i*6 + 1) and hand[i] <= (i + 1)*6:
			check_tower[i] = True

	for i in range(10):	#if the discard or mystery card can fulfill range of index[i] of the hand, replace
		if check_tower[i] == False:
			if discard[-1] >= (i*6 + 1) and discard[-1] <= (i + 1)*6:
				card_to_be_replaced = hand[i]
				find_and_replace(discard[-1], card_to_be_replaced, hand, discard, deck)
				return 
			if deck[-1] >= (i*6 + 1) and deck[-1] <= (i + 1)*6:
				card_to_be_replaced = hand[i]
				find_and_replace(deck[-1], card_to_be_replaced, hand, discard, deck)
				return
	
	discard.append(deck.pop())

def main():
	deck = list(x for x in range (1,61) )
	discard=[]
	shuffle(deck)
	hand = deal_initial_hands(deck)
	user = hand[0]
	computer = hand[1]


	print_top_to_bottom(user)

	discard.append(get_top_card(deck))
	
	while check_racko(user) == False and check_racko(computer) == False:
	
		
		print("The next discard card is: " + str(discard[-1]))

		discard_reply= input("Do you want this card? (y/n) ")
		print_top_to_bottom(user)

		if discard_reply == 'y':
			card_to_be_replaced = int(input("What card do you want to kick out?" ))
			find_and_replace(discard[-1], card_to_be_replaced, user, discard, deck)
			print_top_to_bottom(user)

		elif discard_reply =='n':
			print("Deck Top Card: " + str(deck[-1]))
			secondChoice = input("Keep it? (y/n) ")			
			if secondChoice == 'y':
				card_to_be_replaced = int(input("What card do you want to kick out?" ))
				find_and_replace(deck[-1], card_to_be_replaced, user, discard, deck)

				print_top_to_bottom(user)

			else:
				discard.append(deck[-1])
				deck.pop(-1)
				print_top_to_bottom(user)
			
			
		computer_play(computer, deck, discard)
		# check_num_cards(user,computer,discard,deck) #used to check for total number of cards and avoid repeats

		if len(deck) == 0:
			shuffle(discard)
			deck.extend(discard)
			discard = []
		


	print("\nSomeone won!")
	print("User:")
	print_top_to_bottom(user)	
	print("")
	print("Computer: ")
	print_top_to_bottom(computer)

# def check_num_cards(lst1, lst2, lst3, lst4):
# 	print("Total cards: " + str(len(lst1)+ len(lst2) + len(lst3)+ len(lst4)))
	
if __name__ == '__main__':
	main()