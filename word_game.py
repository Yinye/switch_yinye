################### WORD GUESS GAME ###############################

### import random is used when performing a random action
#### WORD_LIST is uppercase to show it is a constant
#### Note: return terminates execution
### def represents a function


import random
WORD_LIST = ["hello", "world", "class", "books", "table", "chairs", "pencil"]

def pick_word(list_word):
	word = random.choice(list_word)
	# print("The word is", word)
	return word
#   return random.choice(list_word)

def get_guess():
	print("Running a get_guess function")
	guess = input("Guess a word: ")   ### The user inputs in a word
	if not guess == "":               ### If the input is empty, it returns guess...user is asked to enter an input
		return guess   
	else:
		print("Words cannot be empty")
		get_guess()                     ###recursion is taking pace here....it repeats itself


### The user's input is compared with the word picked
def evaluate_guess():
	print("Running an evaluate function")
	word = pick_word(WORD_LIST)
	guess = get_guess()
	if guess == word:
		return True
	else:
		# print("Your guess is wrong")
		return False

# evaluate_guess()

def play_game(): 
	if evaluate_guess() == True:
		print("Your guess is correct")
		resp = input("Do you want to continue, Y/N: ")
		if resp == "y":
			play_game()
			# evaluate_guess()
		else:
			print("Goodbye")
	else:
		evaluate_guess()

play_game()


	