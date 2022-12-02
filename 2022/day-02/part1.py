char_to_no = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

def get_rounds():
    with open("input.txt", "r") as f:
        rounds = []
        for line in f:
            opponent_move, own_move = line.strip().split(" ")
            opponent_move = char_to_no[opponent_move]
            own_move = char_to_no[own_move]
            rounds.append((opponent_move, own_move,))
    return rounds

def add_three_overflow(num):
    result = num + 1
    if result == 4:
        result = 1
    return result

def sub_three_overflow(num):
    result = num - 1
    if result == 0:
        result = 3
    return result

def get_round_winner(round):
    """returns 0 for loss, 3 for draw, 6 for win"""
    opponent_move, own_move = round
    if opponent_move == own_move:
        return 3
    
    if add_three_overflow(own_move) == opponent_move:
        return 0
    else:
        return 6
    
if __name__ == "__main__":
    rounds = get_rounds()
    score = 0
    for round in rounds:
        opponent_move, own_move = round
        score += get_round_winner(round)
        score += own_move
    print(score)