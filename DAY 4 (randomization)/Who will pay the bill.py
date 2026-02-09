import random

friends = ["Aneri", "Kiruthika", "Sonal", "Nazneen", "Rithika"]
# CHOICE 1
print(random.choice(friends))

#CHOICE 2
random_index = random.randint(0,4)
print(friends[random_index])