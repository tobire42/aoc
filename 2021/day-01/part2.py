with open("input.txt") as f:
    input_values = [int(v) for v in f.readlines()]

windows = [sum(input_values[i:i+3]) for i in range(len(input_values)-2)]

previous_value = None
increased_count = 0

for value in windows:
    if previous_value and value > previous_value:
        increased_count += 1
    
    previous_value = value

print(increased_count)
