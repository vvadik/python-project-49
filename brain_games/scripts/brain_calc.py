#!/usr/bin/env python3
from brain_games.games.brain_calc import brain_calc, RULE
from brain_games.engine import process


def main():
    process(RULE, brain_calc)


if __name__ == "__main__":
    main()
