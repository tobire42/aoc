

def get_calorie_sums():
    sums = []
    with open("input.txt", "r") as f:
        current_sum = 0
        for line in f:
            if line.strip():
                current_sum += int(line.strip())
            else:
                sums.append(current_sum)
                current_sum = 0
    return sums


if __name__ == "__main__":
    print(max(get_calorie_sums()))
