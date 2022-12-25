with open('contents.txt') as f:
    contents = [line.rstrip('\n') for line in f]

tally = 0

num_lines = len(contents)

def find_error (rucksack):
    tally = 0
    item_error = set(rucksack[0]).intersection(rucksack[1], rucksack[2])
    for item in item_error:
        if item.isupper():
            tally += ord(item) - 38
        else:
            tally += ord(item) - 96
    return tally

for i in range(0, num_lines, 3):
    tally += find_error(contents[i:i+3])

print(tally)