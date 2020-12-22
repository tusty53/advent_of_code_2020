if __name__ == '__main__':
    f = open("input.txt", "r")
    lines = f.readlines()
    group_yeses = set()
    sum_of_counts = 0

    for line in lines:
        if line == '\n':
            #Don't count /n as a character
            sum_of_counts += len(group_yeses) - 1
            group_yeses = set()
        else:
            for c in line:
                group_yeses.add(c)
    if line != '\n':
        sum_of_counts += len(group_yeses) - 1
    print(f"Sum of counts: {sum_of_counts}")
