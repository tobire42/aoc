import re
import pprint

def read_stacks(lines):
    stack_count = 9
    stacks = [[] for i in range(stack_count)]

    for line in lines[:-1]:
        stack_idx = 0
        for stack in stacks:
            char = line[1 + 4*stack_idx]
            if char != " ":
                stack.append(char)
            stack_idx += 1
    
    return [list(reversed(stack)) for stack in stacks]

def apply_instructions(stacks, instructions):
    for instruction in instructions:
        print(instruction)
        m = re.match("move (\d+) from (\d+) to (\d+)", instruction)
        crate_count = int(m.group(1))
        from_stack = int(m.group(2))
        to_stack = int(m.group(3))

        for i in range(crate_count):
            item = stacks[from_stack - 1].pop()
            stacks[to_stack - 1].append(item)
            pprint.pprint(stacks)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.rstrip("\n") for l in f.readlines()]
        seperator_line_idx = lines.index("")
        stacks = read_stacks(lines[:seperator_line_idx])

        apply_instructions(stacks, lines[seperator_line_idx + 1:])

        print("".join([stack[-1] for stack in stacks]))

