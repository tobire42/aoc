import re
from pprint import pprint

bag_color_contains = {}
bag_color_can_be_in = {}

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        container_color, contents = line.split(" bags contain ")
        if not container_color in bag_color_contains:
            bag_color_contains[container_color] = []
        for contained_bags in contents.split(","):
            contained_bags = contained_bags.strip().strip(".")
            if contained_bags == "no other bags":
                continue
            print(contained_bags)
            m = re.match("^([0-9]+) ([a-z]+ [a-z]+) bags?$", contained_bags)
            assert m
            count = int(m.group(1))
            color = m.group(2)
            if not color in bag_color_can_be_in:
                bag_color_can_be_in[color] = []
            bag_color_can_be_in[color].append(container_color)
            bag_color_contains[container_color].append((color, count))

pprint(bag_color_can_be_in)
pprint(bag_color_contains)

def contained_bags_count(color):
    count = 0
    for contained_color, contained_count in bag_color_contains[color]:
        count += contained_count * (1 + contained_bags_count(contained_color))
    return count
    
print(contained_bags_count("shiny gold"))
