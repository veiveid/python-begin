# -*- coding: UTF-8 -*-

import random

def get_computer_choice():
    """computer random choice"""
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player, computer):
    """judge the outcome"""
    if player == computer:
        return "draw"
    elif(player == "rock" and computer == "scissors") or \
            (player == "scissors" and computer == "paper") or \
            (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("welcome to rock-paper-scissors!！")
    print("input 'q' to quit.")

    while True:
        player_choice = input("please input your choice:(rock/paper/scissors).")

        if player_choice == "q":
            print("game over, bye!")
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print("invalid choice, please input 'rock', 'paper', 'scissors'.")
            continue

        computer_choice = get_computer_choice()
        print(f"computer choice:{computer_choice}")

        result = get_winner(player_choice, computer_choice)
        print(f"result:{result}")

if __name__ == "__main__":
    play_game()


