import random

# List of words for the game
word_list = ["python", "java", "ruby", "javascript", "php", "html", "css"]

# Select a random word from the list
chosen_word = random.choice(word_list)

# Scramble the word
scrambled_word = ''.join(random.sample(chosen_word, len(chosen_word)))

# Print the scrambled word and ask the player to guess
print("Guess the word:", scrambled_word)
guess = input("Enter your guess: ")

# Check if the guess is correct
if guess == chosen_word:
    print("Correct! You win.")
else:
    print("Sorry, that's not the correct word. The word was:", chosen_word)
