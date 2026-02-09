import random
Stages  = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''',]
word_list = ["aardvark", "baboon", "camel"]

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal to 6.

lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""
word_length = len(chosen_word)
for position in range(1,word_length):
    placeholder += "_"
print(placeholder)


game_over = False
correct_letters = []

while not game_over:
    # print(guess)
    guess = input("Guess a letter: ").lower()

    display = ""

 

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # TODO-2: - If letter is not in the chosen_word, then reduce lives by 1
    #  If lives go down to 0 then the game should stop and it should print "You Lose!"
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")

    if "_" not in display:
        game_over = True
        print("You win!! ")

    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' that the user has remaining.

    print(Stages[lives])
