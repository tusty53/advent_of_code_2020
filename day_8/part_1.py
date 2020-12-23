import re

ACCUMULATOR = 0
POINTER = 0


def skip(n):
    global POINTER
    POINTER += 1


def increase_accumulator(n):
    global POINTER
    global ACCUMULATOR
    ACCUMULATOR += n
    POINTER += 1


def goto(n):
    global POINTER
    POINTER += n
    pass


class Instruction:
    regex = re.compile('(?P<func>.{3}) (?P<value>.*)')
    counter = 0

    def __init__(self, line):
        result = Instruction.regex.match(line)
        self.line_number = Instruction.counter
        Instruction.counter += 1
        self.instruction_name = result.group("func")
        self.value = int(result.group("value"))


RUN = {
    "nop": skip,
    "acc": increase_accumulator,
    "jmp": goto,
}

if __name__ == '__main__':
    f = open("input.txt", "r")
    lines = f.readlines()
    visited = set()

    full_instructions = []

    for line in lines:
        full_instructions.append(Instruction(line))

    while POINTER not in visited:
        visited.add(POINTER)
        current_instruction = full_instructions[POINTER]
        RUN[current_instruction.instruction_name](current_instruction.value)

    print(f"Value of accumulator when entering the second iteration of the loop: {ACCUMULATOR}")
