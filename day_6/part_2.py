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
            if len(group_yeses) == 0:
                for c in line:
                    group_yeses.add(c)
            else:
                new_set = set()
                for c in group_yeses:
                    if c in line:
                        new_set.add(c)
                group_yeses = new_set

    if line != '\n':
        sum_of_counts += len(group_yeses)
    print(f"Sum of counts: {sum_of_counts}")