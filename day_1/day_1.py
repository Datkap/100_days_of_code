# input + string manipulation
print("You name has: " + str(len(input("What is your name?"))) + " letters.")


# swutch variable value
a = input("a: ")
b = input("b: ")

tmp_a = a
a = b
b = tmp_a

print(a)
print(b)

# project
greeting = "Welcome to the Garage Band Name Creator!"
user_city = input("What is the city you gren up in?")
user_pet = input("What's the name of your pet?")
band_name = user_city+user_pet
print("Your new band name is: " + band_name)