import pprint

def read_input():
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
    return boards, numbers_called

def check_for_bingo(board, numbers_called):
    # check rows
    for row in board:
        row_match = all([column in numbers_called for column in row])
        if row_match:
            return True
    # check columns
    for i in range(len(board[0])):
        column_match = all([row[i] in numbers_called for row in board])
        if column_match:
            return True
    return False

def check_boards_for_bingo(boards, numbers_called):
    slices = [numbers_called[:x] for x in range(1, len(numbers_called))]

    for slice in slices:
        for board in boards:
            bingo = check_for_bingo(board, slice)
            if bingo:
                print("Bingo!")
                return board, slice

def run():
    boards, numbers_called = read_input()
    board, slice = check_boards_for_bingo(boards, numbers_called)
    pprint.pprint(board)
    print(slice)

    unmarked_numbers = []
    for row in board:
        unmarked_numbers += [col for col in row if col not in slice]
    
    score = sum(unmarked_numbers) * slice[-1]
    print(score)



if __name__ == "__main__":
    run()