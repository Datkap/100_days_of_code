from day_16.menu import Menu, MenuItem
from day_16.coffee_maker import CoffeeMaker
from day_16.money_machine import MoneyMachine
from day_15.utils import logo


def display_main_menu():
    print(f"""
    Coffee machine is operating.
    1. To prepare a coffee select type:
    {menu.get_items()}
    2. To print report type in 'report'.
    3. To switch machine off type in 'off'.
    """)


def ask_user_for_action():
    user_choice = input("What would you like to do?")
    while user_choice.lower() not in ['off', 'report', 'espresso', 'latte', 'cappuccino']:
        print("I know it's hard, but read menu options carefully...")
        user_choice = input("What would you like to do?")
    return user_choice


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
#
# while user_action != 'off':
#     print(logo)
#     money_machine = MoneyMachine()
#     coffee_machine = CoffeeMaker()
#     menu = Menu()
#     display_main_menu()
#     user_action = ask_user_for_action()
#
#     if user_action == 'report':
#         money_machine.report()
#         coffee_machine.report()
#     elif user_action in ['espresso', 'latte', 'cappuccino']:
#         if coffee_machine.is_resource_sufficient(menu.find_drink(user_action)):
#             paid_value = process_coins(available_menu, user_action)
#             transaction_successful, profit, coins_in_machine, change = \
#                 check_transaction_successful(available_menu, user_action, paid_value, coins_in_machine, profit)
#             if transaction_successful:
#                 print(f"Here is your {user_action} ☕. Enjoy!")
#         else:
#             print(f"Sorry, there is not enough {missing_ingredient} to prepare selected coffee.")
#     elif user_action == 'off':
#         break
#     else:
#         print("Something went wrong. Try again...")
#
# print('Coffee machine is switching off. ')