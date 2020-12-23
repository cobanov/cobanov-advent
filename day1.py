# Mert Cobanov - Advent of Code 2020
# Day 1 - 23.12.2020 08:34
# github: cobanov


def read_input(path):
    with open(path, "r") as file:
        content = file.readlines()

    return content


content = read_input("inputs/day1_input.txt")
content_int = list(map(lambda x: int(x), content))

for number in content_int:
    if (2020 - number) in content_int:
        print(f"For {number}, found {2020 - number}")
        print(f"Result: {number * (2020 - number)}")
        break
