import re

# this could/should be imported from crates.txt
stacks = {
    1 : ["Q","S","W","C","Z","V","F","T"],
    2 : ["Q","R","B"],
    3 : ["B","Z","T","Q","P","M","S"],
    4 : ["D","V","F","R","Q","H"],
    5 : ["J","G","L","D","B","S","T","P"],
    6 : ["W","R","T","Z"],
    7 : ["H","Q","M","N","S","F","R","J"],
    8 : ["R","N","F","H","W"],
    9 : ["J","Z","T","Q","P","R","B"]
}

# import moves
with open('moves.txt') as f:
    contents = [line.rstrip('\n') for line in f]

for move in contents:
    current_move = re.split(r'[a-zA-Z]|,| ', move) # remove comma + alpha chars
    current_move = list(filter(None, current_move)) # remove empty strings
    for i in range(len(current_move)): # convert to int
        current_move[i] = int(current_move[i])
    # move crates
    for i in range(current_move[0]):
        source_crate = (stacks.get(current_move[1])[-1])
        stacks.get(current_move[1]).pop(-1)
        stacks[current_move[2]].append(source_crate)

# return crate on top of each stack
for k,v in stacks.items():
    print(v[-1])