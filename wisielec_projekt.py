import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def words():
    words = ["python", "wsb", "warsaw", "merito", "hangman", "computer", "informatics", "project"]
    return random.choice(words)
def progress(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])
def hangman():
    word = words()
    guessed_letters = set()
    incorrect_guesses = set()
    attempts_left = 6
    def get_guess():
        while True:
            guess = input("Guess a letter: ").lower()
            clear_screen()
            if len(guess) == 1 and guess.isalpha():
                return guess
            print("Please enter a single alphabetical character\n")
            print(progress(word, guessed_letters))
            print(f"\nAttempts left: {attempts_left}\n")
    print("\nWelcome to Hangman\n")
    print(progress(word, guessed_letters))
    print(f"\nAttempts left: {attempts_left}\n")
    while attempts_left > 0:
        guess = get_guess()
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter\n")
            print(progress(word, guessed_letters))
            print(f"\nAttempts left: {attempts_left}\n")
            continue
        if guess in word:
            guessed_letters.add(guess)
            print("Good guess")
        else:
            incorrect_guesses.add(guess)
            attempts_left -= 1
        clear_screen()
        print(progress(word, guessed_letters))
        print(f"\nAttempts left: {attempts_left}\n")
        if "_" not in progress(word, guessed_letters):
            print("Congratulations, you won")
            break
    else:
        print(f"You lost. The word was {word}")
def play_again():
    while True:
        hangman()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        clear_screen()
        while play_again not in ["yes", "no"]:
            print("Please enter 'yes' or 'no'")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            clear_screen()
        if play_again == "no":
            print("Thanks for playing")
            break
play_again()
