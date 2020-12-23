import re


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


def swap(full_instructions, swap_counter):
    if full_instructions[swap_counter].instruction_name == "jmp":
        full_instructions[swap_counter].instruction_name = "nop"
    else:
        full_instructions[swap_counter].instruction_name = "jmp"


if __name__ == '__main__':
    f = open("input.txt", "r")
    lines = f.readlines()
    flag = True
    swap_counter = 0

    full_instructions = []

    for line in lines:
        full_instructions.append(Instruction(line))

    while flag and swap_counter < len(full_instructions):
        if full_instructions[swap_counter].instruction_name != "acc":
            swap(full_instructions, swap_counter)
            visited = set()
            ACCUMULATOR = 0
            POINTER = 0
            while POINTER not in visited and POINTER < len(full_instructions):
                visited.add(POINTER)
                current_instruction = full_instructions[POINTER]
                RUN[current_instruction.instruction_name](current_instruction.value)

            if POINTER == len(full_instructions):
                flag = False
            swap(full_instructions, swap_counter)
        swap_counter += 1
    print(f"Value of accumulator when swapped out of the loop: {ACCUMULATOR}")
