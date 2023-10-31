# ================================================================ #
from day_11.art import logo
import random

# ================================================================ #
# cards are referred to as their value instead of actual suit/card combination

# ================================================================ #
# Define functions
def hand_score(hand: list):
    score = 0
    for card in hand:
        score += card
    return score

def deal_card(hand_to_receive_card: list, cards_deck: list):
    card = random.choice(cards_deck)
    if card == 11 and (hand_score(hand_to_receive_card) + card) > 21:
        card = 1
    hand_to_receive_card.append(card)


def compare_scores(player_score: int, dealer_score: int):
    if player_score > 21:
        return 'dealer_won'
    elif dealer_score > 21:
        return 'player_won'
    elif player_score > dealer_score:
        return 'player_won'
    elif player_score < dealer_score:
        return 'dealer_won'
    else:
        return 'draw'


# ================================================================ #
def play_blackjack():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    continue_decision = ['y', 'n']
    playing_decision = ["Hit", "Stand"]
    player_hand = []
    dealer_hand = []

    # ================================================================ #
    # First round - dealing single card to dealer and 2 card to player
    deal_card(dealer_hand, cards)
    for turn in range(2):
        deal_card(player_hand, cards)

    print("Player's current hand:")
    print(player_hand)
    print("Player's current score:" + str(hand_score(player_hand)))
    print("Dealer's current hand:")
    print(dealer_hand)
    print("Dealer's current score:" + str(hand_score(dealer_hand)))
    # ================================================================ #
    if hand_score(player_hand) == 21:
        # player score is max, no decision needed
        while hand_score(dealer_hand) < 17:
            deal_card(dealer_hand, cards)
            print("Dealer's current hand:")
            print(dealer_hand)
            print("Dealer's current score:" + str(hand_score(dealer_hand)))

        game_result = compare_scores(hand_score(player_hand), hand_score(dealer_hand))
        print("Game result:")
        print(game_result)


        # ================================================================ #
        # Game finished - ask if player wants to continue
        continue_game = input('Would you like to continue the game? Type in "y" or "n"')
        while continue_game not in continue_decision:
            print("I know it's hard but read carefully...")
            continue_game = input('Would you like to continue the game? Type in "y" or "n"')
        if continue_game == 'y':
            play_blackjack()
        else:
            print('Game Over. See you next time!')
        # ================================================================ #
    else:
        # Ask player to make a decision
        player_decision = ''
        while player_decision != "Stand":
            player_decision = input('What is your decision? Type in: "Hit" or "Stand"')
            while player_decision not in playing_decision:
                print("I know it's hard but read carefully...")
                player_decision = input('What is your decision? Type in: "Hit" or "Stand"')

            if player_decision == 'Hit':
                deal_card(player_hand, cards)
                print("Player's current hand:")
                print(player_hand)
                print("Player's current score:" + str(hand_score(player_hand)))
                if hand_score(player_hand) > 21:
                    break

        while hand_score(dealer_hand) < 17:
            deal_card(dealer_hand, cards)
            print("Dealer's current hand:")
            print(dealer_hand)
            print("Dealer's current score:" + str(hand_score(dealer_hand)))

        game_result = compare_scores(hand_score(player_hand), hand_score(dealer_hand))
        print("Game result:")
        print(game_result)
        # ================================================================ #
        # Game finished - ask if player wants to continue
        continue_game = input('Would you like to continue the game? Type in "y" or "n"')
        while continue_game not in continue_decision:
            print("I know it's hard but read carefully...")
            continue_game = input('Would you like to continue the game? Type in "y" or "n"')
        if continue_game == 'y':
            play_blackjack()
        else:
            print('Game Over. See you next time!')
        # ================================================================ #

play_blackjack()