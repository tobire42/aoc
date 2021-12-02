
with open("input.txt", "r") as f:
    program = [l.strip().split(" ") for l in f.readlines()]

horizontal_position = 0
depth = 0
aim = 0

for instruction, parameter in program:
    parameter = int(parameter)

    if instruction == "forward":
        horizontal_position += parameter
        depth += aim * parameter
    if instruction == "down":
        aim += parameter
    if instruction == "up":
        aim -= parameter

print(horizontal_position * depth)