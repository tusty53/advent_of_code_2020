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


def contains_macguffin_on_current_level(bag_name, rules):
    for bag_desc in rules[bag_name]:
        if bag_desc[0] == MACGUFFIN_NAME:
            return True
    return False


def check_the_bag(bag):
    if bag in checked_bags:
        return bag in bags_containing_the_macguffin
    checked_bags.add(bag)
    if contains_macguffin_on_current_level(bag, rules):
        bags_containing_the_macguffin.add(bag)
        return True
    else:
        for inner_bag in rules[bag]:
            if check_the_bag(inner_bag[0]):
                bags_containing_the_macguffin.add(bag)
                return True
    return False


if __name__ == '__main__':
    f = open("input.txt", "r")
    lines = f.readlines()
    bags_containing_the_macguffin = set()
    checked_bags = set()
    rules = {}
    MACGUFFIN_NAME = "shiny gold"

    line_rule = re.compile("(?P<name>.* .*) bags contain (?P<contents>.*)")
    contents_rule = re.compile("(?P<quantity>\d*) (?P<name>\D* \D*) bag")

    for line in lines:
        bag_name, bag_list = read_a_rule(line_rule, contents_rule, line)
        rules[bag_name] = bag_list
    for bag in rules.keys():
        check_the_bag(bag)

    print(f"Number of bags that could eventually containg a shiny golden bag: {len(bags_containing_the_macguffin)}")
