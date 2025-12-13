import csv


class NumSet:
    def __init__(self, operand, digits):
        self.operand = operand
        self.digits = digits


def process_file():
    # Open the CSV file in read mode ('r')
    with open('data.csv', mode='r') as file:
        # Create a csv.reader object
        csv_reader = csv.reader(file)
        result = []
        # Iterate over each row in the CSV file
        for row_i, row in enumerate(csv_reader):
            result.append([])
            for col_i, col in enumerate(row):
                for item in col.split(" "):
                    if item == "":
                        continue
                    else:
                        result[row_i].append(item)
    return result


def step_one():
    result = process_file()
    process_nums = []
    num_rows = len(result) - 1
    num_cols = len(result[0])
    for col_i in range(num_cols):
        operand = result[len(result) - 1][col_i]
        string = ""
        num_list = []
        for r_i in range(num_rows):
            digit = result[r_i][col_i]
            num_list.append(int(digit))
        process_nums.append(NumSet(operand, num_list))
        # process_nums.append(string)
    total = 0
    for item in process_nums:

        if item.operand == '+':
            subtotal = 0
            for digit in item.digits:
                subtotal += digit

        elif item.operand == '*':
            subtotal = 1
            for digit in item.digits:
                subtotal *= digit
        total += subtotal
    return total


def process_file_2():
    with open('data.csv', mode='r') as file:
        # Create a csv.reader object
        csv_reader = csv.reader(file)
        result = []
        for row_i, row in enumerate(csv_reader):
            result.append([])
            for col_i, col in enumerate(row):
                for item in col:
                    result[row_i].append(item)

    return result


def convert_chars_to_cephapod_ints(arr):
    process_nums = []
    *digits_rows, operand_row = arr
    for col in zip(*digits_rows, operand_row):
        *digits, operand = col
        process_nums.append(NumSet(operand, list(digits)))
    last_item = []
    for row in range(len(arr) - 1):
        last_item.append(arr[row][len(arr[row]) - 1])

    process_nums.append(NumSet("", last_item))
    return process_nums


def convert_process_nums_to_ints(arr):
    for item in arr:
        item.digits = ''.join(item.digits)
        item.digits = item.digits.strip()
        if item.digits != '':
            item.digits = int(item.digits)

        else:
            item.digits = None
    return arr


def process_arr(arr):
    operand = arr[0].operand
    total = 0
    if operand == '+':
        subtotal = 0
    else:
        subtotal = 1
    for i, item in enumerate(arr):
        if item.digits is None:
            operand = arr[i + 1].operand
            total += subtotal
            if operand == '+':
                subtotal = 0
            else:
                subtotal = 1
        else:
            if operand == '*':
                subtotal *= item.digits
            else:
                subtotal += item.digits
    total += subtotal
    return total


def step_two_redo():
    result = process_file_2()
    process_nums = convert_chars_to_cephapod_ints(result)
    return_arr = convert_process_nums_to_ints(process_nums)
    return process_arr(return_arr)


if __name__ == '__main__':
    print(step_one())
    print(step_two_redo())
