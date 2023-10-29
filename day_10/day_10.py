# def format_name(f_name: str, l_name: str):
#     return (f_name + ' ' + l_name).title()
#
# print(format_name('jan', 'kowalski'))

# Calculator challenge
def calculator(operation, n_1, n_2):
    def add(n_1, n_2):
        return n_1 + n_2

    def substract(n_1, n_2):
        return n_1 - n_2

    def multiply(n_1, n_2):
        return n_1 * n_2

    def divide(n_1, n_2):
        return n_1 / n_2

    if operation in ["+", "-", "*", "/"]:
        if operation == "+":
            return add(n_1, n_2)
        elif operation == "-":
            return substract(n_1, n_2)
        elif operation == "*":
            return multiply(n_1, n_2)
        elif operation == "/":
            return divide(n_1, n_2)
    else:
        print("Next time you must chose one the available operations.")

def correct_operator(operation_symbol):
    return operation_symbol in ["+", "-", "*", "/"]


continue_calcs = True
operation = input('What kind of operation would you like to perform? Type in: \n "+"\n "-"\n "*"\n "/"')
if correct_operator(operation):
    first_num = float(input("What is the first number for your calculation?"))
    second_num = float(input("What is the second number for your calculation?"))
    calc_result = calculator(operation, first_num, second_num)
    print(f"Result of your calculation is: {calc_result}.")
    while continue_calcs:
        continue_answer = input("Would you like to continue calculation for this number? Type in 'y' or 'n'.")
        if continue_answer == 'y':
            operation = input('What kind of operation would you like to perform? Type in: \n "+"\n "-"\n "*"\n "/"')
            if correct_operator(operation):
                second_num = float(input("What is the second number for your calculation?"))
                calc_result = calculator(operation, calc_result, second_num)
                print(f"Result of your calculation is: {calc_result}.")
            else:
                print("Next time you must chose one the available operations.")
        else:
            continue_calcs = False
else:
    print("Next time you must chose one the available operations.")