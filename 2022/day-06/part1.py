def find_packet_start(input, char_count=4):
    for i in range(len(input) - char_count):
        if len(set(input[i:i+char_count])) == char_count:
            return i + char_count

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_stream = f.read()
        print(find_packet_start(input_stream))