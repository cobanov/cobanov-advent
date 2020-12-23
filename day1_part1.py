# Mert Cobanov - Advent of Code 2020
# Day 1 Part 1 - 23.12.2020 08:34
# github: cobanov
# puzzle answer: 928896

from utils.utils import read_input


def main():
    content = read_input("inputs/day1_input.txt")
    content_int = list(map(lambda x: int(x), content))

    for number in content_int:
        if (2020 - number) in content_int:
            print(f"For {number}, found {2020 - number}")
            print(f"Result: {number * (2020 - number)}")
            break


if __name__ == "__main__":
    main()

# For 1312, found 708
# Result: 928896