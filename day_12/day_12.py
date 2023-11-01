from day_12.logo import logo
import random


def ask_for_guess():
    guess = int(input('What is your guess?'))
    while guess not in range(1, 101):
        print("Your guess must be a number in range from 1 to 100.")
        guess = int(input('What is your guess?'))
    return guess


def play_guess_the_number():
    number_to_be_guessed = random.randint(1, 101)

    game_level = input('What game level would you like to play? Type in "hard" or "easy"')
    while game_level not in ['hard', 'easy']:
        print("I know it's hard but read carefully...")
        game_level = input('What game level would you like to play? Type in "hard" or "easy"')

    if game_level == 'hard':
        trials = 5
    else:
        trials = 10

    while trials != 0:
        player_guess = ask_for_guess()
        if player_guess == number_to_be_guessed:
            print("Good job! You guessed it!")
            break
        elif player_guess > number_to_be_guessed:
            print("Your guess is too high.")
            trials -= 1
        else:
            print("Your guess is too low.")
            trials -= 1

        print(f"You have {trials} trial(s) left.")

    if player_guess != number_to_be_guessed:
        print(f"You're out of trials. The number was {number_to_be_guessed}.")


play_guess_the_number()
