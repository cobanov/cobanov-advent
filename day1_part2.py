# Mert Cobanov - Advent of Code 2020
# Day 1 Part 2 - 23.12.2020 08:43
# github: cobanov
# puzzle answer: 295668576


from utils import read_input

def main():
    content = read_input("inputs/day1_input.txt")
    content_int = list(map(lambda x: int(x), content))
    content_sorted = sorted(content_int)

    for index, first_number in enumerate(content_sorted):
        for second_number in content_sorted[index:]:
            calculated_number = first_number + second_number
            if (2020 - calculated_number) in content_int:
                print(f"For {first_number, second_number}, found {2020 - calculated_number}")
                print(f"Result: {(2020 - calculated_number) * first_number * second_number}")
                break

 if __name__ == "__main__":
    main()

# For (558, 664), found 798
# Result: 295668576
