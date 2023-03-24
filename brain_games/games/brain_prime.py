import random

LOWER_BOUND = 0
HIGHER_BOUND = 1000

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num == 1:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def brain_prime():
    num = random.randint(LOWER_BOUND, HIGHER_BOUND)
    correct = "yes" if is_prime(num) else "no"
    return num, correct
