# review
def greet():
    print("Good morning!")
    print("How you doin'?")
    print("Was pleasure to meet you!")

greet()

# pain area calculator
#Write your code below this line 👇
from math import ceil
def paint_calc(height, width, cover):
    num_of_cans = ceil((height*width) / coverage)
    print(f"You'll need {num_of_cans} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# prime numbers
# Write your code below this line 👇
def prime_checker(number):
    divisible = [number % i == 0 for i in range(2, number)]
    if True in divisible:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
