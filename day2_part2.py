# Mert Cobanov - Advent of Code 2020
# Day 2 Part 1 - 23.12.2020 12:39
# github: cobanov
# puzzle answer: 489

from utils import read_input
from day2_part1 import split_text


def main():

    content = read_input("inputs/day2_input.txt")
    valid_passwords = list()

    for input in content:
        valid_position, not_valid_position, letter, content = split_text(input)

        if content[valid_position -
                   1] == letter and content[not_valid_position - 1] != letter:
            valid_passwords.append(input)

        # opposite conditions
        if content[valid_position -
                   1] != letter and content[not_valid_position - 1] == letter:
            valid_passwords.append(input)

    print("Valid passwords count: ", len(valid_passwords))
    # Valid passwords count: 489


if __name__ == "__main__":
    main()
