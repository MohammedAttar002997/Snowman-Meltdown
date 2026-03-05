import random

from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current state of the snowman and the word progress."""
    # Display the snowman stage for the current number of mistakes.
    if mistakes < len(STAGES):
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
    """Main game loop for Snowman Meltdown."""
    print("Welcome to Snowman Meltdown!")

    replay = True
    while replay:
        secret_word = get_random_word()
        mistakes = 0
        guessed_letters = []
        max_mistakes = len(STAGES) - 1
        game_over = False

        # Inner loop for the current round
        while mistakes < max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)

            guess = input("Guess a letter: ").lower().strip()

            # Input validation
            while len(guess) != 1 or not guess.isalpha():
                guess = input("Please enter a single valid letter: ").lower().strip()

            # Check if already guessed
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'! Try a different one.")
                continue

            # Add to guessed letters
            guessed_letters.append(guess)

            # Check if the guess exists in the secret word
            if guess in secret_word:
                print(f"Good job! '{guess}' is in the word.")

                # IMMEDIATE WIN CHECK: Check if all letters have been guessed
                if all(letter in guessed_letters for letter in secret_word):
                    display_game_state(mistakes, secret_word, guessed_letters)
                    print(f"Congratulations! You won! The word was: {secret_word}")
                    game_over = True
                    break
            else:
                mistakes += 1
                print(f"Sorry, '{guess}' is not in the word.")

        # If the loop finished because of mistakes (and not a win)
        if not game_over and mistakes >= max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"Bummer! You ran out of tries. The word was: {secret_word}")

        # Replay logic: Ask the user if they want to play again
        replay_option = input("Do you want to play again? (yes(Y)/no(N)): ").lower().strip()
        if replay_option != 'y' and replay_option != 'yes':
            replay = False
            print("Thanks for playing! Goodbye!")