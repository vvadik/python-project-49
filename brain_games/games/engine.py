import prompt

from brain_games.cli import welcome_user

ROUNDS = 3


def process(rule, current_game):
    print("Welcome to the Brain Games!")
    username = welcome_user()
    print(rule)
    for _ in range(ROUNDS):
        question, answer = current_game()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if answer != user_answer:
            print(f"{user_answer} is wrong answer ;(. "
                  f"Correct answer was {answer}.")
            print(f"Let's try again, {username}!")
            return
        print("Correct!")
    print(f"Congratulations, {username}!")
