class Window:
    def __init__(self):
        self.numbers = []
        self.sums = {}

    def add_a_number(self, new_number):
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


if __name__ == '__main__':
    f = open("input.txt", "r")
    WINDOW_SIZE = 25
    window = Window()

    result = -1

    while result == -1:
        result = window.add_a_number(int(f.readline()))

    print(f"First wrong value is: {result}")
