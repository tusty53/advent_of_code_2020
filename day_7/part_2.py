import re


def read_a_rule(line_rule, contents_rule, line):
    bag_list = []
    result = line_rule.match(line)
    bag_name = result.group('name')
    contents = result.group('contents')
    if contents != "no other bags.":
        for match in contents_rule.finditer(contents):
            bag_list.append((match.group('name'), int(match.group('quantity'))))
    return bag_name, bag_list


def check_the_bag(bag):
    inside_bags_count = 0
    if bag in checked_bags.keys():
        inside_bags_count = checked_bags[bag]
    else:
        for inner_bag in rules[bag]:
            inside_bags_count += inner_bag[1] * (1 + check_the_bag(inner_bag[0]))
        checked_bags[bag] = inside_bags_count
    return inside_bags_count


if __name__ == '__main__':
    f = open("input.txt", "r")
    lines = f.readlines()
    bags_containing_the_macguffin = set()
    checked_bags = {}
    rules = {}
    MACGUFFIN_NAME = "shiny gold"

    line_rule = re.compile("(?P<name>.* .*) bags contain (?P<contents>.*)")
    contents_rule = re.compile("(?P<quantity>\d*) (?P<name>\D* \D*) bag")

    for line in lines:
        bag_name, bag_list = read_a_rule(line_rule, contents_rule, line)
        rules[bag_name] = bag_list

    print(f"Number of bags inside a {MACGUFFIN_NAME}: {check_the_bag(MACGUFFIN_NAME)}")
