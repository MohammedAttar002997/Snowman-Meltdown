import random

from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    # secret_word = get_random_word()
    # guessed_letters = []
    # mistakes = 0
    # max_mistakes = len(STAGES) - 1
    replay = False
    print("Welcome to Snowman Meltdown!")

    # The while loop allows the game to continue until a win or loss condition is met
    while not replay:
        secret_word = get_random_word()
        mistakes = 0
        guessed_letters = []
        max_mistakes = len(STAGES) - 1
        while mistakes < max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)

            guess = input("Guess a letter: ").lower()
            while len(guess) > 1:
                guess = input("Please enter a valid letter: ").lower()
            # Input validation: check if already guessed
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'! Try a different one.")
                continue

            # Check if the guess exists anywhere in the secret word
            if guess in secret_word:
                print(f"Good job! '{guess}' is in the word.")
                guessed_letters.append(guess)
            else:
                mistakes += 1
                print(f"Sorry, '{guess}' is not in the word.")

            # Win condition: check if every letter in the word has been guessed
            if all(letter in guessed_letters for letter in secret_word):
                display_game_state(mistakes, secret_word, guessed_letters)
                print(f"Congratulations! You won! The word was: {secret_word}")
                return
            else:
                # Loss condition: only reached if the while loop finishes without a 'return'
                display_game_state(mistakes, secret_word, guessed_letters)
                print(f"Bummer! You ran out of tries. The word was: {secret_word}")
        replay_option = input("Do you want to play again?(yes(Y)/no(NO)) ")
        if replay_option.lower() == "n":
            replay = True