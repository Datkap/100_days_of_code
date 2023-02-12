# import random
# # Step 1
# word_list = ["aardvark", "baboon", "camel"]
#
# # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# chosen_word = word_list[random.randint(0, len(word_list)-1)] # better solution chosen_word = random.choice(word_list)
#
# # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Guess a letter:").lower()
#
# # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for letter in chosen_word:
#     print(letter == guess)
#
# #Step 2 & 3
# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
#
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
#
# #TODO-1: - Create an empty List called display.
# #For each letter in the chosen_word, add a "_" to 'display'.
# #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# display = ["_" for letter in chosen_word]
#
# #TODO-2: - Loop through each position in the chosen_word;
# #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# while "_" in display:
#     print(display)
#     guess = input("Guess a letter: ").lower()
#     for position in range(len(chosen_word)):
#         if guess == chosen_word[position]:
#             display[position] = guess
# print("You guessed it!")
# print(display)

#Step 4
import random
from  day_7.hangman_stages import stages

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6
used_letters = []

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print("=================================")
    print(f"{' '.join(display)}")
    print("Used letters:")
    print(used_letters)
    guess = input("Guess a letter: ").lower()
    if guess in used_letters:
        print("This letter was already used!")
    else:
    #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."
        if guess not in chosen_word:
            used_letters.append(guess)
            print("Your guess is not in the word!")
            print(stages[lives])
            lives -= 1
            if lives < 0:
                end_of_game = True
                print("You lose.")

    #Join all the elements in the list and turn it into a String.

    #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")
            print(f"{' '.join(display)}")

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.