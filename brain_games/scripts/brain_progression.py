#!/usr/bin/env python3
from brain_games.games.brain_progression import brain_progression
from brain_games.games.engine import process


def main():
    rule = 'What number is missing in the progression?'
    process(rule, brain_progression)


if __name__ == "__main__":
    main()
