# -*- coding: UTF-8 -*-

import random

def guess_number_game():
    print('welcome to Guess Number Game')
    print("I am thinking of a number between 1 and 100. Can you guess it?")

    # 1. random a number
    secret_number = random.randint(1, 100)

    # 2. guess count
    attempts = 0

    while True:
        # 3. get user input number
        intput_number = input()

        # 4. check number
        if not intput_number.isdigit():
            print('please enter a number')
            continue

        guess = int(intput_number)
        attempts += 1
        if guess == secret_number:
            print('You got it!')
            print(f"You have guess {attempts} 次。")
            break
        elif guess > secret_number:
            print('Your guess is too high.')
        else:
            print('Your guess is too low.')

        if(attempts == 5) :
            print(f'The limit of {attempts} has been exceeded, the game is over')
            break


#
if __name__ == '__main__':
    guess_number_game()
