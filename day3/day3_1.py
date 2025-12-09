import csv

def process_file():
    # Open the CSV file in read mode ('r')
    with open('data.csv', mode='r') as file:
        # Create a csv.reader object
        csv_reader = csv.reader(file)
        arr = []
        # Iterate over each row in the CSV file
        for row in csv_reader:
            for item in row:
                arr.append(item)
    return arr


def best_two_digit_number(s):
    best = -1
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            num = int(s[i] + s[j])
            if num > best:
                best = num
    return best


def best_12_digit_number(s):
    result = []
    start = 0
    n = len(s)

    for pos in range(12):
        remaining = 12 - pos - 1
        end = n - remaining
        best_digit = max(s[start:end])
        best_index = s.index(best_digit, start, end)
        result.append(best_digit)
        start = best_index + 1

    return "".join(result)


def step_one(arr):
    result = []
    sum_strs = []
    for row, item in enumerate(arr):
            number = best_two_digit_number(item)
            sum_strs.append(number)
    sum1 = 0
    for item in sum_strs:
        sum1 += int(item)
    print(sum1)


def step_two(arr):
    result = []
    sum_strs = []
    for row, item in enumerate(arr):
            number = best_12_digit_number(item)
            sum_strs.append(number)
    sum1 = 0
    for item in sum_strs:
        sum1 += int(item)
    print(sum1)



if __name__ == "__main__":
    arr = process_file()

    step_one(arr)

    step_two(arr)
