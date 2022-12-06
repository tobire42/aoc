import part1

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_stream = f.read()
        print(part1.find_packet_start(input_stream, 14))