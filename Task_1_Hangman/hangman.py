
import random

# Step 1: List of words
words = ["python", "student", "computer", "science", "game"]

# Step 2: Select a random word
secret_word = random.choice(words)

# Step 3: Initial values
guessed_letters = []
attempts = 6

# Step 4: Hangman drawings
hangman = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# Step 5: Welcome message
print("Welcome to Hangman Game!")

# Step 6: Game loop
while attempts > 0:

    # Display hangman drawing
    print(hangman[6 - attempts])

    # Hide letters that are not guessed
    hidden_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            hidden_word = hidden_word + letter + " "
        else:
            hidden_word = hidden_word + "_ "

    print("Guess the word:", hidden_word)
    print("Attempts left:", attempts)

    # Check winning condition
    if "_" not in hidden_word:
        print("Congratulations! You won!")
        break

    # Take input from user
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one English letter!")
        continue

    

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check correct or wrong guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        attempts = attempts - 1
        print("Wrong guess!")

# Losing condition
else:
    print(hangman[6])
    print("Game Over!")
    print("The word was:", secret_word)
