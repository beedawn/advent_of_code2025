import csv
from turtledemo.penrose import start


class DigitRange():
    def __init__(self, start, end):
        self.start = start
        self.end = end


def process_file():
    # Open the CSV file in read mode ('r')
    with open('data.csv', mode='r') as file:
        # Create a csv.reader object
        csv_reader = csv.reader(file)
        ranges = []
        numbers = []
        current = ranges
        # Iterate over each row in the CSV file
        for row in csv_reader:
            if not row:
                current = numbers
                continue
            for item in row:
                    current.append(item)

    return (ranges, numbers)

def convert_to_digitranges(arr):
    new_arr= []
    for item in arr:
        one, two = item.split('-')
        one = int(one)
        two = int(two)
        new_arr.append(DigitRange(one, two))
    return new_arr

def step_one():
    (ranges, numbers) = process_file()
    print(ranges)
    print(numbers)

    ranges = convert_to_digitranges(ranges)
    valid_nums = []
    for number in numbers:
        number = int(number)
        if any(r.start <= number <= r.end for r in ranges):
            valid_nums.append(number)
    print("Step One:")
    print(len(valid_nums))

def step_two():
    (ranges, _) = process_file()
    ranges = convert_to_digitranges(ranges)
    ranges.sort(key=lambda x: x.start)

    merged = []
    current_start = ranges[0].start
    current_end = ranges[0].end

    for singlerange in ranges[1:]:
        if singlerange.start <= current_end + 1:
            current_end = max(current_end, singlerange.end)
        else:
            merged.append((current_start, current_end))
            current_start = singlerange.start
            current_end = singlerange.end
    merged.append((current_start, current_end))
    total = 0
    for start, end in merged:
        total += (end-start) + 1
    print("step two:")
    print(total)
if __name__ == '__main__':
   step_one()
   step_two()