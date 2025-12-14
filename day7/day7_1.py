import csv


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


def check_beam(arr):
    for row_i, row in enumerate(arr):
        for col_i, col in enumerate(row):
            if row_i +1 < len(arr) and col_i+1 < len(arr[0]):
                if col == 'S':
                    if arr[row_i + 2][col_i] == '^' and arr[row_i + 1][col_i + 1] == '.':
                        arr[row_i + 1][col_i] = '|'
                        arr[row_i + 2][col_i - 1] = '|'
                        arr[row_i + 2][col_i + 1] = '|'

                if arr[row_i][col_i+1] == '^' and arr[row_i - 1][col_i+1] == '|':
                    arr[row_i][col_i] = '|'
                    arr[row_i][col_i + 2] = '|'
                if arr[row_i][col_i] == '|':
                    print(f"row: {row_i + 1} col: {col_i + 1}")
                    print(f"len arr: {len(arr)} len row arr:{len(arr[row_i])}")
                    if arr[row_i + 1][col_i] == '.':
                        arr[row_i + 1][col_i] = '|'

    total = 0
    for row_i, row in enumerate(arr):
        for col_i, col in enumerate(row):
            if row_i +1 < len(arr) and col_i+1 < len(arr[0]):
                if arr[row_i][col_i] == '|' and arr[row_i+1][col_i] == '^':
                    total += 1
    return total


def step_one():
    result = process_file_2()
    print(check_beam(result))



if __name__ == '__main__':
    step_one()
