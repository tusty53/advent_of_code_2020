import copy

SEAT_LEGEND = {
    '#': 'occupied',
    '.': 'floor',
    'L': 'empty'
}


def read_seat_grid(f):
    grid = []
    for line in f.readlines():
        grid.append(list(line[:-1]))
    return grid


def count_occupied_seats(seat_grid):
    count = 0
    for row in seat_grid:
        for place in row:
            if place == '#':
                count += 1
    return count


def simulate_one_movement_round(grid):
    changed = False
    new_grid = copy.deepcopy(grid)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            taken = calculate_number_of_occupied_surrounding_sits(x, y, grid)
            place = grid[x][y]
            if place == 'L' and taken == 0:
                new_grid[x][y] = "#"
                changed = True
            if place == '#' and taken > 3:
                new_grid[x][y] = "L"
                changed = True
    global seat_grid
    seat_grid = new_grid
    return changed


def calculate_number_of_occupied_surrounding_sits(row, column, seat_grid):
    count = 0
    neighbourhood = [
        (row - 1, column),
        (row + 1, column),
        (row - 1, column - 1),
        (row, column - 1),
        (row + 1, column - 1),
        (row - 1, column + 1),
        (row, column + 1),
        (row + 1, column + 1),
    ]

    for (x,y) in neighbourhood:
        if 0 <= x < len(seat_grid) and 0 <= y < len(seat_grid[0]):
            if seat_grid[x][y] == '#':
                count += 1
    return count


if __name__ == '__main__':
    f = open("input.txt", "r")
    seat_grid = read_seat_grid(f)

    while simulate_one_movement_round(seat_grid):
        pass

    print(f"After the stabilization, {count_occupied_seats(seat_grid)} were taken")
