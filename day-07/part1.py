import re
from pprint import pprint

bag_color_can_be_in = {}

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        container_color, contents = line.split(" bags contain ")
        for contained_bags in contents.split(","):
            contained_bags = contained_bags.strip().strip(".")
            if contained_bags == "no other bags":
                continue
            print(contained_bags)
            m = re.match("^([0-9]+) ([a-z]+ [a-z]+) bags?$", contained_bags)
            assert m
            count = m.group(1)
            color = m.group(2)
            if not color in bag_color_can_be_in:
                bag_color_can_be_in[color] = []
            bag_color_can_be_in[color].append(container_color)

pprint(bag_color_can_be_in)

def find_possible_container_colors(color):
    possible_container_colors = set()
    try:
        for container_color in bag_color_can_be_in[color]:
            possible_container_colors.add(container_color)
            possible_container_colors = possible_container_colors | find_possible_container_colors(container_color)
    except KeyError:
        pass
    return possible_container_colors

shiny_gold_can_be_in = find_possible_container_colors("shiny gold")

pprint(shiny_gold_can_be_in)
print(len(shiny_gold_can_be_in))

