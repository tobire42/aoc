with open("input.txt") as f:
    input_values = [int(v) for v in f.readlines()]

previous_value = None
increased_count = 0

for value in input_values:
    if previous_value and value > previous_value:
        increased_count += 1
    
    previous_value = value

print(increased_count)
