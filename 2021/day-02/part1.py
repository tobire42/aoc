
with open("input.txt", "r") as f:
    program = [l.strip().split(" ") for l in f.readlines()]

horizontal_position = 0
depth = 0

for instruction, parameter in program:
    parameter = int(parameter)

    if instruction == "forward":
        horizontal_position += parameter
    if instruction == "down":
        depth += parameter
    if instruction == "up":
        depth -= parameter

print(horizontal_position * depth)