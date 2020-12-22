import re

apply_tuple = lambda f: lambda args: f(*args)


def to_numbers(text):
    row = ""
    column = ""
    for char in text[0:7]:
        if char == 'B':
            row += '1'
        else:
            row += '0'
    for char in text[7:10]:
        if char == 'R':
            column += '1'
        else:
            column += '0'

    return int(row, 2), int(column, 2)


def calc_id(row, column):
    return row * 8 + column


if __name__ == '__main__':
    f = open("input.txt", "r")
    passes = f.readlines()
    highest_id = 0

    for a_pass in passes:
        highest_id = max(apply_tuple(calc_id)(to_numbers(a_pass)), highest_id)

    print(f"Highest id: {highest_id}")
