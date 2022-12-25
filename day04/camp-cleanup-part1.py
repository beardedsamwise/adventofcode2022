import re

with open('input.txt') as f:
    contents = [line.rstrip('\n') for line in f]

tally = 0

def camp_cleanup (line):
    split_string = re.split(r'-|,', line)
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
    if all(x in first_list for x in second_list) or all(x in second_list for x in first_list):
        return 1
    else:
        return 0

for each in contents:
    tally += camp_cleanup(each)

print(tally)


