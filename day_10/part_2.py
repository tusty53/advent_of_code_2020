def count_leaves(potentials_dict, current_value):
    global possibilities_dict
    if current_value in potentials_dict.keys():
        if current_value not in possibilities_dict.keys():
            possibilities_dict[current_value] = sum([count_leaves(potentials_dict, x) for x in potentials_dict[current_value]])
        return possibilities_dict[current_value]
    return 1


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
    possibilities_dict = {}

    for line in f.readlines():
        adapter_joltage = int(line)
        add_adapted_range(adapter_joltage, potentials_dict)

    # add device's adapter
    max_adapter = max(potentials_dict.keys()) + 1
    device_adapter = max_adapter + 3
    add_adapted_range(device_adapter, potentials_dict)

    print(f"Number of posibilites to connect to the device is {count_leaves(potentials_dict, SOCKET_JOLTAGE)}")