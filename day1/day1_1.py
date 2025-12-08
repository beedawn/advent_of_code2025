import csv


class Combo:
    def __init__(self, direction, value):
        self.direction = direction
        self.value = value


def process_file():
    # Open the CSV file in read mode ('r')
    with open('day_1_data.csv', mode='r') as file:
        # Create a csv.reader object
        csv_reader = csv.reader(file)
        arr = []
        # Iterate over each row in the CSV file
        for row in csv_reader:
            direction, value = extract_data(row)
            arr.append(Combo(direction, value))
    return arr


def extract_data(item):
    return (item[0][0], int(item[0][1:]))


def is_positive(direction):
    return direction == 'R'


def move_pointer(pointer, direction, value):
    positive = is_positive(direction)
    if positive:
        return (pointer + value) % 100
    else:
        return (pointer - value) % 100


def zero_passes(pointer, direction, value):
    wraps = 0
    if is_positive(direction):
        step = 1
    else:
        step = -1

    for _ in range(value):
        pointer += step
        if pointer % 100 == 0:
            wraps += 1

    return pointer, wraps


def step_one(arr, pointer):
    counter = 0
    for item in arr:
        pointer = move_pointer(pointer, item.direction, item.value)
        if pointer == 0:
            counter += 1
    return counter


def step_two(arr, pointer):
    zero_clicks = 0
    counter = 0
    for item in arr:
        # print(f"{item.direction} {item.value}")
        pointer, zero_clicks = zero_passes(pointer, item.direction, item.value)
        # pointer = move_pointer(pointer, item.direction, item.value)

        counter += zero_clicks

    return counter


if __name__ == "__main__":
    pointer = 50

    arr = process_file()
    counter_step_one = step_one(arr, pointer)

    print(counter_step_one)
    pointer = 50
    # add clicks to counter step_one
    counter_step_two = step_two(arr, pointer)
    print("step 2")
    print(counter_step_two)
