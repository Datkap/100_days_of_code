from day_11.art import logo
import random


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
        game_result = 'dealer_won'
    elif dealer_score > 21:
        game_result = 'player_won'
    elif player_score > dealer_score:
        game_result = 'player_won'
    elif player_score < dealer_score:
        game_result = 'dealer_won'
    else:
        game_result = 'draw'
    print("Game result:")
    print(game_result)


def ask_to_continue():
    continue_game = input('Would you like to continue the game? Type in "y" or "n"')
    while continue_game not in ['y', 'n']:
        print("I know it's hard but read carefully...")
        continue_game = input('Would you like to continue the game? Type in "y" or "n"')
    if continue_game == 'y':
        play_blackjack()
    else:
        print('Game Over. See you next time!')


def ask_player_for_decision(player_hand, cards):
    player_decision = ''
    while player_decision != "Stand":
        player_decision = input('What is your decision? Type in: "Hit" or "Stand"')
        while player_decision not in ["Hit", "Stand"]:
            print("I know it's hard but read carefully...")
            player_decision = input('What is your decision? Type in: "Hit" or "Stand"')

        if player_decision == 'Hit':
            deal_card(player_hand, cards)
            print("Player's current hand:")
            print(player_hand)
            print("Player's current score: " + str(hand_score(player_hand)))
            if hand_score(player_hand) >= 21:
                break


def complete_dealer_cards(dealer_hand, cards):
    while hand_score(dealer_hand) < 17:
        deal_card(dealer_hand, cards)
        print("Dealer's current hand:")
        print(dealer_hand)
        print("Dealer's current score: " + str(hand_score(dealer_hand)))


def start_game(dealer_hand, player_hand, cards):
    deal_card(dealer_hand, cards)
    for turn in range(2):
        deal_card(player_hand, cards)
    print("Player's current hand:")
    print(player_hand)
    print("Player's current score: " + str(hand_score(player_hand)))
    print("Dealer's current hand:")
    print(dealer_hand)
    print("Dealer's current score: " + str(hand_score(dealer_hand)))


def play_blackjack():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = []
    dealer_hand = []

    start_game(dealer_hand, player_hand, cards)

    if hand_score(player_hand) == 21:
        complete_dealer_cards(dealer_hand, cards)
        compare_scores(hand_score(player_hand), hand_score(dealer_hand))
        ask_to_continue()
    else:
        ask_player_for_decision(player_hand, cards)
        complete_dealer_cards(dealer_hand, cards)
        compare_scores(hand_score(player_hand), hand_score(dealer_hand))
        ask_to_continue()


play_blackjack()
