import random

# List of words for the game
word_list = ["python", "java", "ruby", "javascript", "php", "html", "css"]
print("The guesses could be one of the follows : ", word_list)

# Select a random word from the list
chosen_word = random.choice(word_list)
print("It is a ", len(chosen_word), "letter word")

# Create a list to store the player's guesses
guesses = []

# Set the number of chances the player has to guess the word
chances = 6

# Loop until the player has run out of chances or guessed the word
while chances > 0:
    # Print the current state of the word, with underscores for unguessed letters
    display_word = ""
    for letter in chosen_word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "_"
    print(display_word)

    # Ask the player for a guess
    guess = input("Guess a letter: ")

    # Check if the guess is correct
    if guess in chosen_word:
        print("Correct!")
        guesses.append(guess)
    else:
        print("Wrong!")
        chances -= 1

    # Check if the player has guessed the whole word
    if set(chosen_word) == set(guesses):
        print("You win! The word was", chosen_word)
        break

# If the player has run out of chances, print the answer
if chances == 0:
    print("You lose! The word was", chosen_word)
