#!/usr/bin/env python3
from brain_games.games.brain_gcd import brain_gcd
from brain_games.games.engine import process


def main():
    rule = 'Find the greatest common divisor of given numbers.'
    process(rule, brain_gcd)


if __name__ == "__main__":
    main()
