def get_position(seat_spec):
    row_spec = seat_spec[:7]
    column_spec = seat_spec[7:]

    row_binary = row_spec.replace("F", "0").replace("B", "1")
    row = int(row_binary, 2)

    column_binary = column_spec.replace("L", "0").replace("R", "1")
    column = int(column_binary, 2)

    return (row, column)

def get_seat_id(row, column):
    return row*8 + column


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]


result = max([get_seat_id(*(get_position(line))) for line in lines])
print(result)