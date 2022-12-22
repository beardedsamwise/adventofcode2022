with open('example.txt') as f:
    input = [line.rstrip('\n') for line in f]

X = 1
cycle_values = []

for each in input:
    if each == 'noop':
        cycle_values.append(X)
    else:
        addx = int(each.replace('addx ', ''))
        for i in range(2):
            if i == 1:
                cycle_values.append(X)
                X += addx
            else:
                cycle_values.append(X)

signal_strength = cycle_values[19] * 20 + cycle_values[59] * 60 + cycle_values[99] * 100 + cycle_values[139] * 140 + cycle_values[179] * 180 + cycle_values[219] * 220 
print("Signal strength is: " + str(signal_strength))
