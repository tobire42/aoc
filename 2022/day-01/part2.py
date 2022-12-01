import part1

if __name__ == "__main__":
    sums = sorted(part1.get_calorie_sums(), reverse=True)
    print(sum(sums[:3]))
