from day_15.utils import MENU


def run_coffee_machine():
    coins_in_machine = {
        'quarters': 10,
        'dimes': 10,
        'nickles': 10,
        'pennies': 10,
    }
    profit = (coins_in_machine['quarters'] * 0.25) + (coins_in_machine['dimes'] * 0.1) + \
             (coins_in_machine['nickles'] * 0.05) + (coins_in_machine['pennies'] * 0.01)
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    available_menu = MENU

    user_action = ''

    while user_action != 'off':
        display_menu()
        user_action = ask_user_for_action()

        if user_action == 'print':
            print_report(resources, profit)
        elif user_action in ['espresso', 'latte', 'cappuccino']:
            sufficient_ingredients, missing_ingredient = check_resources_sufficient(available_menu, resources,
                                                                                    user_action)
            if sufficient_ingredients:
                paid_value = process_coins(available_menu, user_action)
                transaction_successful, profit, coins_in_machine, change = \
                    check_transaction_successful(available_menu, user_action, paid_value, coins_in_machine, profit)
                if transaction_successful:
                    print(f"Here is your {user_action} ☕. Enjoy!")
            else:
                print(f"Sorry, there is not enough {missing_ingredient} to prepare selected coffee.")
        elif user_action == 'off':
            pass
        else:
            print("Something went wrong. Try again...")

    print('Coffee machine is switching off. ')


def display_menu():
    print("""
    Coffee machine is operating.
    1. To prepare a coffee select type:
        - espresso
        - latte
        - cappuccino
    2. To print report type in 'print'.
    3. To switch machine off type in 'off'.
    """)


def ask_user_for_action():
    user_choice = input("What would you like to do?")
    while user_choice.lower() not in ['off', 'report', 'espresso', 'latte', 'cappuccino']:
        print("I know it's hard, but read menu options carefully...")
        user_choice = input("What would you like to do?")
    return user_choice


def print_report(current_resources_balance, current_profit):
    print(f"""
    Water: {current_resources_balance['water']}ml
    Milk: {current_resources_balance['milk']}ml
    Coffee: {current_resources_balance['coffee']}g
    Money: ${current_profit}
    """)


def check_resources_sufficient(menu, current_resources_balance, chosen_coffee):
    sufficient_ingredients = True
    missing_ingredient = None
    required_ingredients = menu[chosen_coffee]['ingredients']
    for ingredient in required_ingredients:
        if required_ingredients[ingredient] > current_resources_balance[ingredient]:
            sufficient_ingredients = False
            missing_ingredient = ingredient
            break
    return sufficient_ingredients, missing_ingredient


def validate_num_of_coins(coin_type):
    def is_integer(value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    num_of_coins = input(f"How many {coin_type} would you like to insert?")

    while not is_integer(num_of_coins):
        print(f"Type in only the number of {coin_type} you would like to insert...")
        num_of_coins = input(f"How many {coin_type} would you like to insert?")

    return int(num_of_coins)


def process_coins(menu, chosen_coffee):
    print(f"You have selected {chosen_coffee}. It costs ${menu[chosen_coffee]['cost']}. You can pay with coins: "
          f"quarters, dimes, nickles or pennies.")
    num_of_quarters = validate_num_of_coins('quarters')
    num_of_dimes = validate_num_of_coins('dimes')
    num_of_nickles = validate_num_of_coins('nickles')
    num_of_pennies = validate_num_of_coins('pennies')
    inserted_value = (num_of_quarters * 0.25) + (num_of_dimes * 0.1) + (num_of_nickles * 0.05) + (num_of_pennies * 0.01)
    return inserted_value


def check_transaction_successful(menu, chosen_coffee, paid_amount, coins_in_machine, current_profit):
    coffee_price = menu[chosen_coffee]['cost']
    change = 0
    transaction_successful = False
    if paid_amount == coffee_price:
        current_profit += paid_amount
        transaction_successful = True
    elif paid_amount > coffee_price:
        full_change = paid_amount - coffee_price
        change = full_change
        quarters = int(change // 0.25)
        change -= quarters * 0.25
        dimes = int(change // 0.1)
        change -= dimes * 0.1
        nickles = int(change // 0.05)
        change -= nickles * 0.05
        pennies = int(change // 0.01)

        sufficient_coins_for_change = \
            (quarters <= coins_in_machine['quarters'] and
             dimes <= coins_in_machine['dimes'] and
             nickles <= coins_in_machine['nickles'] and
             pennies <= coins_in_machine['pennies'])

        if sufficient_coins_for_change:
            change_in_coins = {'quarters': quarters, 'dimes': dimes, 'nickles': nickles, 'pennies': pennies}
            for coin_type in coins_in_machine:
                coins_in_machine[coin_type] -= change_in_coins[coin_type]
                transaction_successful = True
            print(f"Here is ${round(full_change, 2)} in change.")
        else:
            print("Sorry, there is not enough coins for change. Please use exact amount.")
    else:
        print(f"Sorry, that's not enough money to order {chosen_coffee}. Money refunded.")

    return transaction_successful, current_profit, coins_in_machine, change

run_coffee_machine()