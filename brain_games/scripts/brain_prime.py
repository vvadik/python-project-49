#!/usr/bin/env python3
from brain_games.games.brain_prime import brain_prime
from brain_games.games.engine import process


def main():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    process(rule, brain_prime)


if __name__ == "__main__":
    main()
