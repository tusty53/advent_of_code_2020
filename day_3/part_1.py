import numpy as np


def array_reader(table, x_y):
    x, y = x_y
    # Last char is the new line char
    x_len = len(table[0]) - 1
    y_len = len(table)

    rel_x = x % x_len
    rel_y = y % y_len

    return table[rel_y][rel_x]


if __name__ == '__main__':
    f = open("input.txt", "r")
    lines = f.readlines()

    VECTORS = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    values = []

    for VECTOR in VECTORS:

        position = (0, 0)
        tree_counter = 0

        while position[1] <= len(lines):
            if array_reader(lines, position) == '#':
                tree_counter += 1
            position = tuple(np.add(position, VECTOR))
        print(f"Number of trees met: {tree_counter}")
        values.append(tree_counter)

    answer = 1

    for value in values:
        answer *= value

    print(f"Final answer is {answer}")
