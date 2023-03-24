#!/usr/bin/env python3
from brain_games.games.brain_prime import brain_prime, RULE
from brain_games.engine import process


def main():
    process(RULE, brain_prime)


if __name__ == "__main__":
    main()
