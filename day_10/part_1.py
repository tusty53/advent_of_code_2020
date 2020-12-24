def dict_increment(dictionary, key):
    if key in dictionary.keys():
        dictionary[key] += 1
    else:
        dictionary[key] = 1

def add_adapted_range(adapter_joltage, potentials_dict):
    for i in range(JOLTAGE_RANGE):
        adapted_joltage = adapter_joltage - i - 1
        if adapted_joltage in potentials_dict.keys():
            potentials_dict[adapted_joltage].append(adapter_joltage)
        else:
            potentials_dict[adapted_joltage] = [adapter_joltage]


if __name__ == '__main__':
    f = open("input.txt", "r")

    SOCKET_JOLTAGE = 0
    JOLTAGE_RANGE = 3

    potentials_dict = {SOCKET_JOLTAGE: []}
    #Device's adapter
    joltage_jumps = {3:1}

    for line in f.readlines():
        adapter_joltage = int(line)
        add_adapted_range(adapter_joltage, potentials_dict)

    current_joltage = SOCKET_JOLTAGE
    while current_joltage in potentials_dict.keys():
        new_joltage = min(potentials_dict[current_joltage])
        dict_increment(joltage_jumps, new_joltage - current_joltage)
        current_joltage = new_joltage

    print(f"Number of 1 Jolt jumps: {joltage_jumps[1]}")
    print(f"Number of 3 Jolt jumps: {joltage_jumps[3]}")
    print(f"Result: {joltage_jumps[1] * joltage_jumps[3]}")
