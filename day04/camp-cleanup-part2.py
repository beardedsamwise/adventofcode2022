import re
from functools import reduce

with open('input.txt') as f:
    contents = [line.rstrip('\n') for line in f]

tally = 0

def camp_cleanup (line):
    split_string = re.split(r'-|,', line)
    tally = 0 
    # convert str to int in list
    for i in range(len(split_string)):
        split_string[i] = int(split_string[i])
    # build lists to compare, then compare
    first_list = []
    second_list = []
    for i in range(split_string[0],split_string[1] + 1):
        first_list.append(i)      
    for i in range(split_string[2],split_string[3] + 1):
        second_list.append(i)
    for each in first_list:
        if each in second_list:
            tally += 1
            break
        else: 
            tally = 0
    return tally

for each in contents:
    tally += camp_cleanup(each)

print(tally)


