with open("input.txt") as f:
    input_values =  [v.strip() for v in f.readlines()]

word_length = len(input_values[0])


def get_counts(values):
    one_counts = [0] * word_length
    zero_counts = [0] * word_length

    for value in values:
        for idx, char in enumerate(value):
            if char == '1':
                one_counts[idx] += 1
            if char == '0':
                zero_counts[idx] += 1
    return (one_counts, zero_counts)

one_counts, zero_counts = get_counts(input_values)

epsilon_binary = ''
gamma_binary = ''

for idx in range(word_length):
    if one_counts[idx] > zero_counts[idx]:
        gamma_binary += '1'
        epsilon_binary += '0'
    elif one_counts[idx] < zero_counts[idx]: 
        gamma_binary += '0'
        epsilon_binary += '1'
    else:
        print("Equal count detected, no idea what to do now")

gamma = int(gamma_binary, 2)
epsilon = int(epsilon_binary, 2)

print(f'gamma_binary = {gamma_binary}, epsilon = {epsilon_binary}')

power_consumption = gamma * epsilon

print(f'gamma = {gamma}, epsilon = {epsilon}, power_consumption = {power_consumption}')

def most_common(bit_index, values):
    one_counts, zero_counts = get_counts(values)
    if one_counts[bit_index] >= zero_counts[bit_index]:
        return '1'
    else:
        return '0'

def least_common(bit_index, values):
    one_counts, zero_counts = get_counts(values)
    if zero_counts[bit_index] > one_counts[bit_index]:
        return '1'
    else:
        return '0'

# find oxygen generator rating
filtered_values = input_values
bit_position = 0
while len(filtered_values) > 1:
    filtered_values = [x for x in filtered_values if most_common(bit_position, filtered_values) == x[bit_position]]
    bit_position += 1

oxygen_generator_rating = int(filtered_values[0], 2)

filtered_values = input_values
bit_position = 0
while len(filtered_values) > 1:
    filtered_values = [x for x in filtered_values if least_common(bit_position, filtered_values) == x[bit_position]]
    bit_position += 1

co2_scrubber_rating = int(filtered_values[0], 2)

life_support_rating = oxygen_generator_rating * co2_scrubber_rating

print(f"oxygen_generator_rating = {oxygen_generator_rating}, co2_scrubber_rating = {co2_scrubber_rating} life_support_rating = {life_support_rating}")
