def parse_contents(line):
    first_compartment = line[:int(len(line)/2)]
    second_compartment = line[int(len(line)/2):]
    return (first_compartment, second_compartment,)

def get_item_priority(item):
    if ord(item) > 96:
        return ord(item) - 96
    else:
        return ord(item) - 64 + 26

if __name__ == "__main__":
    total_sum = 0

    with open("input.txt", "r") as f:
        for line in f:
            first_comp, second_comp = parse_contents(line.strip())
            items_both_compartments = set(first_comp) & set(second_comp)
            total_sum += sum([get_item_priority(item) for item in items_both_compartments])
    print(total_sum)
            
