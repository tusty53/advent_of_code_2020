import re

if __name__ == '__main__':

    f = open("input.txt", "r")
    lines = f.readlines()
    correct_passwords_number = 0

    regex = '(?P<min>\d*)-(?P<max>\d*) (?P<letter>[a-z]): (?P<password>[a-z]*)'
    prog = re.compile(regex)

    for line in lines:
        result = prog.match(line)
        a = (result.group('password')[int(result.group('min')) - 1] == result.group('letter'))
        b = (result.group('password')[int(result.group('max')) - 1] == result.group('letter'))
        if (a and not b) or (b and not a):
            correct_passwords_number += 1
    print(f'Answer: {correct_passwords_number}')
