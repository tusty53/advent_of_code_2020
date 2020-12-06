import re


def validate(key, value):

    clrs = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if key == 'byr' and (1920 <= int(value) <= 2002):
        return True
    if key == 'iyr' and (2010 <= int(value) <= 2020):
        return True
    if key == 'eyr' and (2020 <= int(value) <= 2030):
        return True
    if key == 'hgt' and ((value[-2:] == 'cm' and (150 <= int(value[:-2]) <= 193)) or (
            value[-2:] == 'in' and (59 <= int(value[:-2]) <= 76))):
        return True
    if key == 'hcl' and re.match('^#[a-z0-9]{6}$', value) is not None:
        return True
    if key == 'ecl' and value in clrs:
        return True
    if key == 'pid' and re.match('^[0-9]{9}$', value) is not None:
        return True
    if key == 'cid':
        return True
    return False


if __name__ == '__main__':
    f = open("input.txt", "r")

    reg = '(?P<key>[a-z]{3}):(?P<val>\S*)'
    NORTH_POLE_DATA = "cid"

    whole = f.read()
    passports = whole.split('\n\n')
    number_of_valid = 0

    for passport in passports:
        keys = set()
        valid = True
        for m in re.finditer(reg, passport):
            keys.add(m.group('key'))
            if not (validate(m.group('key'), m.group('val'))):
                valid = False
        if not (len(keys) == 8 or (len(keys) == 7 and not (NORTH_POLE_DATA in keys))):
            valid = False
        if valid:
            number_of_valid += 1

    print(f"Number of valid passports: {number_of_valid}")
