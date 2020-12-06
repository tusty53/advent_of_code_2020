import re


if __name__ == '__main__':
    f = open("input.txt", "r")

    reg = '(?P<key>[a-z]{3}):(?P<val>\S*)'
    NORTH_POLE_DATA = "cid"

    whole = f.read()
    passports = whole.split('\n\n')
    valid = 0

    for passport in passports:
        keys = set()
        for m in re.finditer(reg, passport):
            keys.add(m.group('key'))
        if len(keys) == 8 or (len(keys) == 7 and not (NORTH_POLE_DATA in keys)):
            valid += 1

    print(f"Number of valid passports: P{valid}")

