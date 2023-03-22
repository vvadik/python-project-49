#!/usr/bin/env python3
from brain_games.games.brain_even import brain_even
from brain_games.games.engine import process


def main():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    process(rule, brain_even)


if __name__ == "__main__":
    main()
