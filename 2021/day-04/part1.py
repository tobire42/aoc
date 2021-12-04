import pprint

boards = []
current_board = []

with open("input.txt", "r") as f:
    numbers_called = [int(n) for n in f.readline().strip().split(",")]
    print(numbers_called)

    for line in f.readlines():
        split_line = line.split()
        if len(split_line) == 0 and current_board:
            boards.append(current_board)
            current_board = []
        if len(split_line) > 0:
            current_board.append([int(n) for n in split_line])

    if current_board:
        boards.append(current_board)

pprint.pprint(boards)