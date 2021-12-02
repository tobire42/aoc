import math
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]

def get_encountered_trees(right, down):
    y_pos = 0
    x_pos = 0
    trees_encountered = 0

    while y_pos < len(lines):
        line = lines[y_pos]

        modulo = x_pos % len(line)
        encounter = line[modulo]

        if encounter == "#":
            trees_encountered += 1

        y_pos += down
        x_pos += right

    print(f"Right {right} Down {down}: {trees_encountered} Trees encountered")
    return trees_encountered

rightdown = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]


result_list = [get_encountered_trees(*rd) for rd in rightdown]

product = 1
for x in result_list:
    product *= x


print(product)