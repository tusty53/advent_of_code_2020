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


def list_surrounding_ids(an_id, r, c):
    surroundings = []
    if c > 0:
        surroundings.append((an_id - 1, r, c - 1))
    if c < NUMBER_OF_COLUMNS - 1:
        surroundings.append((an_id + 1, r, c + 1))
    if r > 0:
        surroundings.append((an_id - 8, r - 1, c))
    if r < NUMBER_OF_ROWS - 1:
        surroundings.append((an_id + 8, r + 1, c))
    return surroundings


if __name__ == '__main__':
    f = open("input.txt", "r")
    passes = f.readlines()
    my_id = 0
    missing_ids = set()
    listed_ids = set()

    NUMBER_OF_ROWS = 128
    NUMBER_OF_COLUMNS = 8

    for a_pass in passes:
        listed_ids.add(apply_tuple(calc_id)(to_numbers(a_pass)))

    for r in range(NUMBER_OF_ROWS):
        for c in range(NUMBER_OF_COLUMNS):
            this_id = calc_id(r, c)
            if this_id not in listed_ids and r not in (0, NUMBER_OF_ROWS - 1):
                missing_ids.add((this_id, r, c))

    for an_id, r, c in missing_ids:
        surroundings = list_surrounding_ids(an_id, r, c)
        ok = True
        for surr_id in surroundings:
            if surr_id in missing_ids:
                ok = False
        if ok:
            my_id = an_id

    print(f"My id: {my_id}")
