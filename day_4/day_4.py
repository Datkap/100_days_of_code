import random

# # heads or tails
# print("Hello! Let's toss your coin.")
# user_bet = input("What's your bet? Heads or Tails?")
#
# if user_bet == "Heads" or user_bet == "Tails":
#     throw = random.randint(1, 2)
#     if throw == 1:
#         throw = "Heads"
#     else:
#         throw = "Tails"
#     if throw == user_bet:
#         print(f"It's {throw}! You guessed it right!")
#     else:
#         print(f"It's {throw}! Sadly you didn't guess it...")
# else:
#     print("You were suppose to bet on 'Heads' or 'Tails'.")


# rock, paper, scissors
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = {0: "Rock", 1: "Paper", 2: "Scissors"}
choices_visual = {"Scissors": scissors, "Paper": paper, "Rock": rock}
player_choice = input("What do you choose? Rock, Paper or Scissors?")
ai_choice = choices[random.randint(0, 2)]
if player_choice in choices.values():
    player_won = (player_choice == choices[0] and ai_choice == choices[2]) or\
                 (player_choice == choices[1] and ai_choice == choices[0]) or\
                 (player_choice == choices[2] and ai_choice == choices[1])
    if player_choice == ai_choice:
        print("You chose:")
        print(choices_visual[player_choice])
        print("Computer chose:")
        print(choices_visual[ai_choice])
        print("It's a draw!")
    elif player_won:
        print("You chose:")
        print(choices_visual[player_choice])
        print("Computer chose:")
        print(choices_visual[ai_choice])
        print("You won!")
    else:
        print("You chose:")
        print(choices_visual[player_choice])
        print("Computer chose:")
        print(choices_visual[ai_choice])
        print("You lose!")
else:
    print("Please choose Rock, Paper or Scissors.")