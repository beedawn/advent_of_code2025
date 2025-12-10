import csv
from operator import index
import copy


from sqlalchemy.engine import row


def process_file():
    # Open the CSV file in read mode ('r')
    with open('data.csv', mode='r') as file:
        # Create a csv.reader object
        csv_reader = csv.reader(file)
        arr = []
        # Iterate over each row in the CSV file
        for row in csv_reader:
            for item in row:
                item_list = []
                for char in item:
                    item_list.append(char)
            arr.append(item_list)
    return arr

def get_neighbors(arr, row, index):
    upper_left = arr[row-1][index-1] if row-1 >= 0 and index-1 >= 0   else None
    upper = arr[row-1][index] if row-1>=0  else None
    upper_right = arr[row-1][index+1] if row-1 >=0 and index+1 < len(arr[row]) else None
    left = arr[row][index-1] if index-1>=0 else None
    right = arr[row][index+1] if index+1<len(arr[row]) else None
    bottom_left = arr[row+1][index-1] if row+1<len(arr) and index-1>=0 else None
    bottom = arr[row+1][index] if row+1<len(arr) else None
    bottom_right = arr[row+1][index+1] if row+1<len(arr) and index+1<len(arr[row]) else None

    return [upper_left, upper, upper_right, left, right, bottom_left, bottom, bottom_right]


def step1(arr):
    count = 0
    for r, row in enumerate(arr):
        for c, column in enumerate(row):
            local_count = 0
            if arr[r][c] != '@':
                continue
            items = get_neighbors(arr, r, c)
            for item in items:
                if item == '@':
                    local_count += 1
            if local_count < 4:
                count += 1
    return count

def step2(arr):
    count = 0
    copy_arr = copy.deepcopy(arr)
    for r, row in enumerate(arr):
        for c, column in enumerate(row):
            local_count = 0
            if arr[r][c] != '@':
                continue
            items = get_neighbors(arr, r, c)
            for item in items:
                if item == '@':
                    local_count += 1
            if local_count < 4:
                copy_arr[r][c] = '.'
                count += 1
    return copy_arr, count

if __name__ == '__main__':
    arr = process_file()
    print(step1(arr))
    full_count = 0
    item_count = -1
    while(item_count != 0):
        (arr, item_count)=step2(arr)
        full_count += item_count
    print(full_count)