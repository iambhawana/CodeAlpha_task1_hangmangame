import random

# List of words
words = ["apple", "mango", "grape", "tiger", "house"]

# Random word selection
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of attempts
attempts = 6

print("===== HANGMAN GAME =====")

# Game loop
while attempts > 0:

    display = ""

    # Display guessed letters
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check letter
    if guess in word:
        print("Correct Guess!")
        guessed_letters.append(guess)
    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Attempts Left:", attempts)

    # Check winning condition
    won = True

    for letter in word:
        if letter not in guessed_letters:
            won = False

    if won:
        print("\nCongratulations! You Won!")
        print("The word was:", word)
        break

# Losing condition
if attempts == 0:
    print("\nGame Over!")
    print("The word was:", word)
