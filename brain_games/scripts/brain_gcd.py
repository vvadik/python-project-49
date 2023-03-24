#!/usr/bin/env python3
from brain_games.games.brain_gcd import brain_gcd, RULE
from brain_games.engine import process


def main():
    process(RULE, brain_gcd)


if __name__ == "__main__":
    main()
