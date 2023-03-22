import random

LOWER_BOUND = 0
HIGHER_BOUND = 1000


def get_correct(term_one, term_two):
    while term_one != 0 and term_two != 0:
        if term_one > term_two:
            term_one = term_one % term_two
        else:
            term_two = term_two % term_one
    return term_one + term_two


def brain_gcd():
    term_one = random.randint(LOWER_BOUND, HIGHER_BOUND)
    term_two = random.randint(LOWER_BOUND, HIGHER_BOUND)
    correct = get_correct(term_one, term_two)
    question = f"{term_one} {term_two}"
    return question, str(correct)
