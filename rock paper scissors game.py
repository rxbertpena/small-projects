import random

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

# add art into list
game_art = [rock, paper, scissors]

#output welcome msg and get user input
print("Welcome to Rock, Paper, Scissors! You will be playing vs a Computer.")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

#display user choice and computer choice with art
if user_choice >= 0 and user_choice <= 2:
    print(game_art[user_choice])


computer_choice = random.randint(0, 2)
print("Computer chose: ")
print(game_art[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
