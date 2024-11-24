import random

def hangman():
    words = ["python", "hangman", "developer", "programming", "challenge"]
    word = random.choice(words)  # Randomly select a word
    guessed_word = ["_"] * len(word)  # Display underscores for the word
    attempts = 6  # Number of incorrect attempts allowed
    guessed_letters = set()  # Track guessed letters

    print("Welcome to Hangman!")
    print(" ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            guessed_letters.add(guess)
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Wrong guess! '{guess}' is not in the word.")
            attempts -= 1
            guessed_letters.add(guess)
            print(f"Attempts remaining: {attempts}")

        print(" ".join(guessed_word))

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

# Run the game
hangman()
