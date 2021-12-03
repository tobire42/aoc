with open("input.txt") as f:
    input_values =  [v.strip() for v in f.readlines()]

word_length = len(input_values[0])

one_counts = [0] * word_length
zero_counts = [0] * word_length

for value in input_values:
    for idx, char in enumerate(value):
        if char == '1':
            one_counts[idx] += 1
        if char == '0':
            zero_counts[idx] += 1

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


