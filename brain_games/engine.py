import prompt

ROUNDS = 3


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


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
