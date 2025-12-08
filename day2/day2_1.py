import csv


class DistanceRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def process_file():
    # Open the CSV file in read mode ('r')
    with open('data.csv', mode='r') as file:
        # Create a csv.reader object
        csv_reader = csv.reader(file)
        arr = []
        # Iterate over each row in the CSV file
        for row in csv_reader:
            for item in row:
                items = item.split("-")
                range = DistanceRange(int(items[0]), int(items[1]))
                arr.append(range)
    return arr


def is_invalid_repeating_blocks(number):
    num_str = str(number)
    n = len(num_str)
    for block_len in range(1, n // 2 + 1):
        if n % block_len != 0:
            continue  # block length must divide number evenly
        block = num_str[:block_len]
        repeats = n // block_len
        if block * repeats == num_str:
            return True  # number is made of repeating blocks

    return False  # valid number


def split_half(number):
    str_num = str(number)
    if len(str_num) % 2 != 0:
        return False

    middle = len(str_num) // 2
    if str_num[0:middle] == str_num[middle:]:
        return True
    return False


def step_one():
    return split_half(number)


if __name__ == "__main__":
    arr = process_file()
    dup_numbers_step_two = []
    dup_numbers_step_one = []
    for item in arr:
        for number in range(item.start, item.end + 1):

            # part one

            if step_one():
                dup_numbers_step_one.append(number)

            # part two
            result = is_invalid_repeating_blocks(number)
            if result:
                dup_numbers_step_two.append(number)

    # sum step one
    total_step_one = 0
    for item in dup_numbers_step_one:
        total_step_one += item

    # sum step two
    total_step_two = 0
    for item in dup_numbers_step_two:
        total_step_two += item

    print("part one solution")
    print(total_step_one)

    print("part two solution")
    print(total_step_two)
