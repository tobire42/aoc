import part1

if __name__ == "__main__":
    total_count = 0
    with open("input.txt", "r") as f:
        for line in f:
            first_set, second_set = part1.get_section_assignments(line)
            if first_set & second_set:
                total_count += 1
    print(total_count)
            