import csv
from unicodedata import digit


class DigitPosition:
    def __init__(self,digit, index, row):
        self.row = row
        self.digit = digit
        self.index = index

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

def find_largest(s, row):
    largest = 0
    index = 0
    if len(s) == 0:
        return 0
    else:
        for x in range(len(s)):
            if s[x].isdigit() and int(s[x]) > largest:
                largest = int(s[x])
                index = x
    return DigitPosition(largest,index, row)

def step_one(arr):
    result = []
    sum_strs = []
    for row, item in enumerate(arr):
        for i in range(2):
            digitItem = find_largest(item, row)
            result.append(digitItem)
            #need to change this to, once a digit is chosen, we need to pick whatever is to the right of it?
            # if nothing is to the right of it then we need to get the next largest digit?
            item = item[0:digitItem.index]+item[digitItem.index+1:]
    sum = 0
    for index, item in enumerate(result):
        print(item.digit, item.index, item.row)
        if index+1 < len(result) and item.row == result[index+1].row:
            if item.index > result[index+1].index:
                str_num = str(result[index+1].digit)+str(item.digit)
                print(str_num)
                sum_strs.append(str_num)
            else:
                str_num = str(item.digit)+ str(result[index+1].digit)
                print(str_num)
                sum_strs.append(str_num)
    for num in sum_strs:
        sum += int(num)
    print(sum)

if __name__ == "__main__":
    arr = process_file()

    step_one(arr)
