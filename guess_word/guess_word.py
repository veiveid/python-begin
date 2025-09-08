# -*- coding: UTF-8 -*-

import random

def choose_word():
    """randomly choose a word"""
    word_list = ["python", "hangman", "computer", "keyboard", "programming"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """display the word status have been guessed"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    return display.rstrip()

def play_game():
    """play the game"""
    print("Welcome to Guess Word!")
    secret_word = choose_word()
    guessed_letters = [] # the words that player have guessed
    attempts_left = 6  #left chance

    while attempts_left > 0:
        print("\nword status: ", display_word(secret_word, guessed_letters))
        print(f"Left attempts: {attempts_left}")
        guess = input("guess a letter: ").lower()

        # check input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("You guessed that letter.")
        else:
            print("Sorry, you didn't guess that.")
            attempts_left -= 1

        # Determine whether the word is guessed
        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations, you guessed that word:{secret_word}")
            break

    else:
        print(f" Sorry game over, you didn't guess that. the word was {secret_word}")

if __name__ == "__main__":
    play_game()
