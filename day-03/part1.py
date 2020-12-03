with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]

y_pos = 0
x_pos = 0
trees_encountered = 0

while y_pos < len(lines):
    line = lines[y_pos]

    modulo = x_pos % len(line)
    encounter = line[modulo]
    print(f"Encountered {encounter}")

    if encounter == "#":
        trees_encountered += 1

    y_pos += 1
    x_pos += 3

print(f"{trees_encountered} Trees encountered")
