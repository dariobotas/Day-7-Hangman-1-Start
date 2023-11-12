#Step 1 
import random
word_list = ["aardvark", "baboon", "camel", "trick", "suppose","overflow","raise","harmony","seed","sheep","voracious","serve","spiritual","tooth","stingy","glamorous","inexpensive","recondite","taboo","pencil","nervous","eyes","airport","relax","impossible","trains","deadpan","sad","gifted","homely","impulse","crash","tow","knit","spiffy","neighborly","tumble","dark","activity","yielding","bike","boundless","finicky","fry","tongue","unlock","legs","claim","voiceless","adhesive", "scrape", "bárbaros", "blow"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
  if letter == guess:
    print("Right")
  else:
    print("Wrong") 
