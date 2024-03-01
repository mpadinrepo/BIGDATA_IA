#!/usr/bin/python3

import random


class GameAction:

    actions = {
        'rock': {'beats': 'scissors', 'beaten_by': 'paper'},
        'paper': {'beats': 'rock', 'beaten_by': 'scissors'},
        'scissors': {'beats': 'paper', 'beaten_by': 'rock'}
    }


def assess_game(user_action, computer_action):
    if user_action == computer_action:
        print(f"User and computer picked {user_action}. Draw game!")
    elif user_action in GameAction.actions:
        if computer_action == GameAction.actions[user_action]['beats']:
            print(f"{user_action.capitalize()} beats {computer_action}. You won!")
        else:
            print(f"{computer_action.capitalize()} beats {user_action}. You lost!")
    else:
        print("Invalid choice!")


def get_computer_action():
    computer_action = random.choice(list(GameAction.actions.keys()))
    print(f"Computer picked {computer_action}.")
    return computer_action


def get_user_action():
    user_action = input("\nPick a choice: rock, paper or scissors: ").lower()
    return user_action


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'


def main():
    while True:
        user_action = get_user_action()
        computer_action = get_computer_action()
        assess_game(user_action, computer_action)
        if not play_another_round():
            break


if __name__ == "__main__":
    main()
