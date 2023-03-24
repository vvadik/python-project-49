#!/usr/bin/env python3
from brain_games.games.brain_even import brain_even, RULE
from brain_games.engine import process


def main():
    process(RULE, brain_even)


if __name__ == "__main__":
    main()
