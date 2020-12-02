CONSTANT = 2020

if __name__ == '__main__':

    f = open("input.txt", "r")
    lines = f.readlines()
    #lines  = ["1200\n", "300\n", "800\n"]
    s = set()

    for s_number in lines:
        number = int(s_number)
        if CONSTANT - number in s:
            reverse = CONSTANT - number
            print(f"Result: {number} x {reverse} = {number * reverse}")
        else:
            s.add(number)
    print('Done')
