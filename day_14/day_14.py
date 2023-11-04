from day_14.logo import vs, logo
from day_14.game_data import data
import random, copy

"""
To-Do:
    1) Start the game, display logos etc
    2) Display information about A and B
    3) Ask player for answer
    3) If correct, show counter, make B -> A and add new B
    4) Ask player for answer
    5) If correct increase score, else end the game
    7) If everything guessed correctly then end the game
"""

current_game_data = copy.deepcopy(data)


def select_item_for_comparison(list_of_items):
    return list_of_items.pop(random.randint(0, len(list_of_items)-1))


def ask_for_player_choice():
    choice = input("Who has more followers? Type 'A' or 'B': ")
    while choice.upper() not in ['A', 'B']:
        print("I know it's hard, but read carefully...")
        choice = input("Who has more followers? Type 'A' or 'B': ")
    return choice


def make_comparison(element_a, element_b, current_score):
    correct_answer = 'A' if element_a['follower_count'] > element_b['follower_count'] \
        else 'B'

    print(f"Compare A: {element_a['name']}, a {element_a['description']} from {element_a['country']}.")
    print(vs)
    print(f"Compare B: {element_b['name']}, a {element_b['description']} from {element_b['country']}.")
    player_choice = ask_for_player_choice().upper()

    if player_choice == correct_answer:
        current_score += 1
        player_failed = False
        return current_score, player_failed
    else:
        player_failed = True
        return current_score, player_failed


def play_comparison_game(current_game_data):
    print(logo)
    score, player_failed = 0, False
    while not len(current_game_data) == 0 and not player_failed:
        if score == 0:
            element_a, element_b = select_item_for_comparison(current_game_data), \
                                   select_item_for_comparison(current_game_data)
            score, player_failed = make_comparison(element_a, element_b, score)
        else:
            print(f"You're right! Current score: {score}.")
            element_a, element_b = element_b, select_item_for_comparison(current_game_data)
            score, player_failed = make_comparison(element_a, element_b, score)

    if player_failed:
        print(f"Sorry, that's wrong. Final score: {score}.")
    else:
        print("Good job! You guessed everything correctly!")


play_comparison_game(current_game_data)
