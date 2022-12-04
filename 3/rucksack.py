with open('contents.txt') as f:
    contents = [line.rstrip('\n') for line in f]

tally = 0

def find_error (rucksack):
    tally = 0
    half = int((len(rucksack))/2)
    first_half = list(rucksack[0:half])
    second_half = list(rucksack[half:])
    item_error = list(set(first_half).intersection(second_half))
    for item in item_error:
        if item.isupper():
            tally += ord(item) - 38
        else:
            tally += ord(item) - 96
    return tally

for rucksack in contents:
   tally += find_error(rucksack)

print(tally)