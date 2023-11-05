from day_15.utils import coffee_emoji, MENU


def run_coffee_machine():
    profit = 0
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

        if user_action == 'report':
            print_report(resources, profit)
        elif user_action in ['espresso', 'latte', 'cappuccino']:
            sufficient_ingredients, missing_ingredient = check_resources_sufficient(available_menu, resources, user_action)
            if sufficient_ingredients:
                paid_value = process_coins(available_menu, user_action)
            else:
                print(f"Sorry, there is not enough {missing_ingredient} to prepare selected coffee.")

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


def check_transaction_successful(menu, chosen_coffee, paid_amount):
    pass


def make_coffee():
    pass
