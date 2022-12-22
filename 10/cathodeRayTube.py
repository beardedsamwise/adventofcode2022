with open('example.txt') as f:
    input = [line.rstrip('\n') for line in f]

### PART 1 ###

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

### PART 2 ###

# create blank display
display = []
for height in range(6):
    display.append([])
    for width in range(40):
        display[height].append(".")

# draw the pixels! 
for i in range (len(cycle_values)):
    row = int(i / 40)
    sprite_position = i - (row * 40)
    current_pixel = cycle_values[i]
    if sprite_position == current_pixel or sprite_position - 1 == current_pixel or sprite_position + 1 == current_pixel:
        display[row][sprite_position] = "#"
    
for each in display:
    print(each)        