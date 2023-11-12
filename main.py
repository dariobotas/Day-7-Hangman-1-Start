#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
all_guess_words = False

while not all_guess_words:
  guess = input("Guess a letter: ").lower()

  #Check guessed letter
  for position in range(word_length):
      letter = chosen_word[position]
      print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
      if letter == guess:
          display[position] = letter
  
  print(display)

  # list = ['larry','curly','moe']
  # if 'curly' in list:
  #  print 'yay'  - this will print yay
  if "_" not in display:
    all_guess_words = True
    print("You win!")
#  count_missed_letters = 0
#  for letter in display: 
#   if letter == '_':
#      count_missed_letters =+ 1
#  
#  if count_missed_letters == 0:
#    all_guess_words = True  