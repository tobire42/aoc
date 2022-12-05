import re
import part1

def apply_instructions(stacks, instructions):
    for instruction in instructions:
        print(instruction)
        m = re.match("move (\d+) from (\d+) to (\d+)", instruction)
        crate_count = int(m.group(1))
        from_stack = int(m.group(2))
        to_stack = int(m.group(3))

        container_buffer = []

        for i in range(crate_count):
            item = stacks[from_stack - 1].pop()
            container_buffer.append(item)
        
        for item in reversed(container_buffer):
            stacks[to_stack-1].append(item)



if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.rstrip("\n") for l in f.readlines()]
        seperator_line_idx = lines.index("")
        stacks = part1.read_stacks(lines[:seperator_line_idx])

        apply_instructions(stacks, lines[seperator_line_idx + 1:])

        print("".join([stack[-1] for stack in stacks]))