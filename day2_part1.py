# Mert Cobanov - Advent of Code 2020
# Day 2 Part 1 - 23.12.2020 12:32
# github: cobanov
# puzzle answer: 538

from utils.utils import read_input


def split_text(input):

    first_step = input.split("-")
    second_step = first_step[1].split(":")
    third_step = second_step[0].split(" ")

    min_times = int(input.split("-")[0])
    max_times = int(third_step[0])
    letter = third_step[1]
    content = second_step[1].strip()

    return min_times, max_times, letter, content


def main():

    content = read_input("inputs/day2_input.txt")
    valid_passwords = list()

    for input in content:
        min_times, max_times, letter, content = split_text(input)
        times = content.count(letter)
        if times >= min_times and times <= max_times:
            valid_passwords.append(input)

    print("Valid passwords count: ", len(valid_passwords))
    # Valid passwords count: 538


if __name__ == "__main__":
    main()