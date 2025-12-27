import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1 - Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
word_length = len(chosen_word)
for position in range(1,word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter!! ").lower()
# print(guess)

# TODO-2 - Create a "Display" that puts the guess letter in the right position and _ in the rest of the string.
display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)