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
    # create list of negative indices for moving crates in batches
    crates_list = []
    for i in range(current_move[0]):
        crates_list.append(-abs(i+1))
    crates_list.sort(reverse= False)
    # move crates
    for each in crates_list:
        source_crate = (stacks.get(current_move[1])[each]) # get the crate we're moving 
        stacks.get(current_move[1]).pop(each) # remove crate from current stack 
        stacks[current_move[2]].append(source_crate) # move crate to new stack

# return crate on top of each stack
for k,v in stacks.items():
    print(v[-1], end="")