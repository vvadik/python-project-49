import random

LOWER_BOUND = 1
HIGHER_BOUND = 1000

RULE = 'What number is missing in the progression?'


def brain_progression():
    progression_length = random.randint(5, 20)
    step = random.randint(LOWER_BOUND, HIGHER_BOUND)
    start_progression = random.randint(LOWER_BOUND, HIGHER_BOUND)
    progression = [str(start_progression + step * i)
                   for i in range(progression_length)]

    hide_index = random.randint(0, progression_length - 1)
    answer = progression[hide_index]
    progression[hide_index] = ".."

    return " ".join(progression), answer
