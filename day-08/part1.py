program = []

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        command, param = line.split(" ")
        param = int(param)
        program.append((command, param))

visited_lines = []

position = 0
accumulator = 0
while position not in visited_lines:
    visited_lines.append(position)
    command, param = program[position]
    if command == "acc":
        accumulator += param
        position += 1
    if command == "nop":
        position += 1
    if command == "jmp":
        position += param

print(accumulator)
