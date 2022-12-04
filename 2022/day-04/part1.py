def get_section_assignments(line):
    first_range, second_range = line.strip().split(",")
    first_start, first_end = [int(e) for e in first_range.split("-")]
    second_start, second_end = [int(e) for e in second_range.split("-")]
    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))
    return first_set, second_set

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        total_count = 0
        for line in f:
            first_set, second_set = get_section_assignments(line)
            if first_set.issubset(second_set) or second_set.issubset(first_set):
                total_count += 1
    print(total_count)
