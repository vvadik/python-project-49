#!/usr/bin/env python3
from brain_games.games.brain_progression import brain_progression, RULE
from brain_games.engine import process


def main():
    process(RULE, brain_progression)


if __name__ == "__main__":
    main()
