class Window:
    def __init__(self):
        self.numbers = []
        self.sums = {}
        self.full_list = []

    def add_a_number(self, new_number):
        self.full_list.append(new_number)
        if len(self.numbers) >= WINDOW_SIZE:
            if not (new_number in self.sums and self.sums[new_number] > 0):
                return new_number
            self.remove_first_number()
        for number in self.numbers:
            new_sum = number + new_number
            if new_sum in self.sums.keys():
                self.sums[new_sum] += 1
            else:
                self.sums[new_sum] = 1
        self.numbers.append(new_number)
        return -1

    def remove_first_number(self):
        first = self.numbers[0]
        self.numbers = self.numbers[1:]
        for number in self.numbers:
            self.sums[number+first] -= 1


def find_sliding_window(invalid, window):
    sliding_table = []
    sliding_table_sum = 0
    pointer = 0
    while sliding_table_sum != invalid:
        if sliding_table_sum < invalid:
            sliding_table.append(window.full_list[pointer])
            pointer += 1
        else:
            sliding_table = sliding_table[1:]
        sliding_table_sum = sum(sliding_table)
    return sliding_table


if __name__ == '__main__':
    f = open("input.txt", "r")
    WINDOW_SIZE = 25
    window = Window()

    invalid = -1

    while invalid == -1:
        invalid = window.add_a_number(int(f.readline()))

    #invalid = 1000
    result_window = find_sliding_window(invalid, window)

    print(f"Result is the sum of the smallest({min(result_window)}) and largest({max(result_window)}) numbers in the "
          f"sliding window: {min(result_window) + max(result_window)}")
