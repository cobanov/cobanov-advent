# Mert Cobanov - Advent of Code 2020
# Day 3 Part 1 - 23.12.2020 13:37
# github: cobanov
# puzzle answer: 1666768320

from utils.utils import read_input
from functools import reduce


def main():
    
    step_sizes = ((1,1), (3, 1), (5, 1), (7, 1), (1, 2))

    content = read_input("inputs/day3_input.txt")
    length = len(content[0]) - 1

    counter_results = list()

    for step_size_x, step_size_y in step_sizes:
        counter = 0
        loc_x = 0
        for line in content[::step_size_y]:
            if loc_x >= length:
                loc_x -= length

            if line[loc_x] == "#":
                counter += 1

            loc_x += step_size_x

        counter_results.append(counter)
    
    print(counter_results)
    print(reduce(lambda x, y: x*y, counter_results))


if __name__ == "__main__":
    main()

# Result: 1666768320
