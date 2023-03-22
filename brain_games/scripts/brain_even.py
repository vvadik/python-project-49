#!/usr/bin/env python3
import prompt

from brain_games.cli import welcome_user
import random

LOWER_BOUND = 0
HIGHER_BOUND = 1000


def main():
    print("Welcome to the Brain Games!")
    username = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        number = random.randint(LOWER_BOUND, HIGHER_BOUND)
        correct = "yes" if number % 2 == 0 else "no"
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ').lower()
        if answer != correct:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct}.")
            print(f"Let's try again, {username}!")
            exit(0)
        print("Correct!")
    print(f"Congratulations, {username}!")


if __name__ == "__main__":
    main()
