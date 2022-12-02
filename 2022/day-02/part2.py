from part1 import get_rounds, add_three_overflow, sub_three_overflow, get_round_winner

if __name__ == "__main__":
    rounds = get_rounds()
    score = 0
    for round in rounds:
        opponent_move, desired_result = round
        if desired_result == 1:
            # i need to lose
            own_move = sub_three_overflow(opponent_move)
        elif desired_result == 2:
            # draw
            own_move = opponent_move
        elif desired_result == 3:
            # i need to win
            own_move = add_three_overflow(opponent_move)

        score += get_round_winner((opponent_move, own_move,))
        score += own_move
    print(score)