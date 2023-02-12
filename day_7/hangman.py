import random
from  day_7.hangman_extras import stages, logo, word_list

# initial variables
end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
used_letters = []

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# create blanks for the word
display = []
for _ in range(word_length):
    display += "_"

# game mechanism
print(logo)
while not end_of_game:
    print("=================================")
    print(f"{' '.join(display)}")
    print("Used letters:")
    print(used_letters)
    guess = input("Guess a letter: ").lower()
    if guess in used_letters or guess in display:  # check whether the letter was already used
        print("This letter was already used!")
    else:
        for position in range(word_length):  # check if and where in the word the guess is
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:  # deduct life if guess was not in the word
            used_letters.append(guess)
            print("Your guess is not in the word!")
            print(stages[lives])
            lives -= 1
            if lives < 0:  # end game if player is out of lives
                end_of_game = True
                print("You lose.")
                print(f"The word was: {chosen_word}")

        if "_" not in display:  # Check if user has guessed all letters.
            end_of_game = True
            print("You win.")
            print(f"{' '.join(display)}")
