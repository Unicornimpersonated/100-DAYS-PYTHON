import random

rock_paper_scissor = """

██████╗  ██████╗  ██████╗██╗  ██╗    ██████╗  █████╗ ██████╗ ███████╗██████╗     ███████╗ ██████╗██╗███████╗███████╗ ██████╗ ██████╗ ███████╗
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔════╝██╔════╝██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
██████╔╝██║   ██║██║     █████╔╝     ██████╔╝███████║██████╔╝█████╗  ██████╔╝    ███████╗██║     ██║███████╗███████╗██║   ██║██████╔╝███████╗
██╔══██╗██║   ██║██║     ██╔═██╗     ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗    ╚════██║██║     ██║╚════██║╚════██║██║   ██║██╔══██╗╚════██║
██║  ██║╚██████╔╝╚██████╗██║  ██╗    ██║     ██║  ██║██║     ███████╗██║  ██║    ███████║╚██████╗██║███████║███████║╚██████╔╝██║  ██║███████║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

"""

rock = ''' 
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''    
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# ASCII art choices
choices = [rock, paper, scissors]

print(rock_paper_scissor)
print("Welcome to Rock, Paper, Scissors Game!!")

# User input
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")

if user_choice not in ["0", "1", "2"]:
    print("You typed invalid number.You lose. Please restart the game!")
else:
    user_choice = int(user_choice)
    print(f"You chose:\n{choices[user_choice]}")

    # Computer choice
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{choices[computer_choice]}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1
         ):
        print("You win!")
    else:
        print("You lose!")
