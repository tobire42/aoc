program = []

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        command, param = line.split(" ")
        param = int(param)
        program.append((command, param))


def run_program(program):
    position = 0
    accumulator = 0
    visited_lines = []
    while position not in visited_lines:
        visited_lines.append(position)
        try:
            command, param = program[position]
        except IndexError:
            return accumulator 
        if command == "acc":
            accumulator += param
            position += 1
        if command == "nop":
            position += 1
        if command == "jmp":
            position += param
    return None

mod_position = 0
while True:
    print(mod_position)
    modified_program = list(program)
    command, param = modified_program[mod_position]
    if command == "acc":
        mod_position += 1
        continue
    if command == "jmp":
        print("jmp -> nop")
        modified_program[mod_position] = ("nop", param)
        if run_program(modified_program):
            print(run_program(modified_program))
            break
        mod_position += 1
    if command == "nop":
        print("nop -> jmp")
        modified_program[mod_position] = ("jmp", param)
        if run_program(modified_program):
            print(run_program(modified_program))
            break
        mod_position += 1

