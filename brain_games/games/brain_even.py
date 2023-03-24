import random

LOWER_BOUND = 0
HIGHER_BOUND = 1000

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even():
    question = random.randint(LOWER_BOUND, HIGHER_BOUND)
    correct = "yes" if question % 2 == 0 else "no"
    return question, correct
