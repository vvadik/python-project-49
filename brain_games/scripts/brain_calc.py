#!/usr/bin/env python3
from brain_games.games.brain_calc import brain_calc
from brain_games.games.engine import process


def main():
    rule = 'What is the result of the expression?'
    process(rule, brain_calc)


if __name__ == "__main__":
    main()
