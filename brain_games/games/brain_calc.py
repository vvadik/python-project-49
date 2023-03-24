import random

LOWER_BOUND = 0
HIGHER_BOUND = 1000

RULE = 'What is the result of the expression?'


def get_correct(term_one, term_two, method):
    if method == "+":
        return term_one + term_two
    elif method == "-":
        return term_one - term_two
    else:
        return term_one * term_two


def brain_calc():
    term_one = random.randint(LOWER_BOUND, HIGHER_BOUND)
    term_two = random.randint(LOWER_BOUND, HIGHER_BOUND)
    method = random.choice(["+", "-", "*"])
    correct = get_correct(term_one, term_two, method)
    question = f"{term_one} {method} {term_two}"
    return question, str(correct)
