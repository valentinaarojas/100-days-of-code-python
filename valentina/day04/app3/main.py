# Rock, Paper, Scissors Project

import random

# ASCII art

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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

# Rock wins over scissors
# Scissors wins over paper
# Paper wins over rock

# winning moves list
winning_moves = [(1,0), (0,2), (2,1)]

# ascii art list
game_art = [rock, paper, scissors]

if user_choice == computer_choice:
    # draw
    print("\nYou chose:")
    print(game_art[user_choice])
    print("\nComputer chose:")
    print(game_art[computer_choice])
    print("Draw!\n")
elif (user_choice, computer_choice) in winning_moves:
    # user wins
    print("\nYou chose:")
    print(game_art[user_choice])
    print("\nComputer chose:")
    print(game_art[computer_choice])
    print("You win!\n")
elif (computer_choice, user_choice) in winning_moves:
    # computer wins
    print("\nYou chose:")
    print(game_art[user_choice])
    print("\nComputer chose:")
    print(game_art[computer_choice])
    print("Computer wins!\n")
else:
    # invalid
    print("Invalid choice. You lose!\n")
