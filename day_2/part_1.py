import re

if __name__ == '__main__':

    f = open("input.txt", "r")
    lines = f.readlines()
    correct_passwords_number = 0

    regex = '(?P<min>\d*)-(?P<max>\d*) (?P<letter>[a-z]): (?P<password>[a-z]*)'
    prog = re.compile(regex)

    for line in lines:
        result = prog.match(line)
        count = 0
        for letter in result.group('password'):
            if letter == result.group('letter'):
                count += 1
        if count >= int(result.group('min')):
            if count <= int(result.group('max')):
                print(line)
                correct_passwords_number += 1
    print(f'Answer: {correct_passwords_number}')
