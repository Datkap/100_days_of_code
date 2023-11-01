from day_12.logo import logo
import random

number_to_be_guessed = random.randint(1, 101)

game_level = input('What game level would you like to play? Type in "hard" or "easy"')
while game_level not in ['hard', 'easy']:
    print("I know it's hard but read carefully...")
    game_level = input('What game level would you like to play? Type in "hard" or "easy"')

if game_level == 'hard':
    trials = 5
else:
    trials = 10


