import random
ALPHABETS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("Welcome to Hangman game")
print("You are expected to fill in the gaps. A letter cannot be picked twice.")

def pick_a_letter(letters):
  selected_letter = random.choice(letters)
  print("Your selected letter is", selected_letter)
  return pick_a_letter()

def fill_the_gaps():
  filled_gap = 
  


