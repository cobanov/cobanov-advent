# Mert Cobanov - Advent of Code 2020
# Day 3 Part 1 - 23.12.2020 13:37
# github: cobanov
# puzzle answer: 1666768320

from utils.utils import read_input


def main():

    loc_x = 0
    counter = 0

    content = read_input("inputs/day3_input.txt")
    length = len(content[0]) - 1

    for line in content:
        if loc_x >= length:
            loc_x -= length

        if line[loc_x] == "#":
            counter += 1

        loc_x += 3

    print(counter)


if __name__ == "__main__":
    main()

# Result: 1666768320
