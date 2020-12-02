CONSTANT = 2020

if __name__ == '__main__':

    f = open("input.txt", "r")
    lines = f.readlines()
    #lines  = ["1200\n", "300\n", "800\n"]
    s = {}
    t = []

    for s_number in lines:
        number = int(s_number)
        if number < CONSTANT:
            t.append(number)

    for number in t:
        reverse = CONSTANT - number
        if reverse in s.keys():
            print(f"{number} x {s[reverse][0]} x {s[reverse][1]} = {number*s[reverse][0]*s[reverse][1]}")
        else:
            for number_2 in t:
                s[number + number_2] = (number, number_2)

    print("Done")
