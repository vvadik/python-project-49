import random

LOWER_BOUND = 0
HIGHER_BOUND = 1000


def is_prime(num):
    if num == 1:
        return "yes"
    for i in range(2, num):
        if num % i == 0:
            return "no"
    return "yes"


def brain_prime():
    num = random.randint(LOWER_BOUND, HIGHER_BOUND)
    correct = is_prime(num)
    return num, correct
