import part1

if __name__ == "__main__":
    total_sum = 0
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

        for i in range(0, int(len(lines)/3)):
            group = lines[i*3:i*3+3]
            common_items = set(group[0]) & set(group[1]) & set(group[2])
            total_sum += sum([part1.get_item_priority(item) for item in common_items])
    print(total_sum)

