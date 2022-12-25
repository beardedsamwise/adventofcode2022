# import text file to list
with open('elf-calories.txt') as f:
    f_list = [line.rstrip('\n') for line in f]

# set empty lists for use later
elf_list = []
temp_list = []
elf_totals = []

# loop through every item of the list
for line in f_list:
    if line != '':
        # if current item is not empty append to temp list
        to_int = int(line)
        temp_list.append(to_int)
    else:
        # once empty value is found append temp list to main list
        elf_list.append(temp_list)
        # reset temp list 
        temp_list = []

# append final temporary list to main list
elf_list.append(temp_list)

# sum totals for each elf
for elf in elf_list:
    current_elf = sum(elf)
    elf_totals.append(current_elf)

# Sort list in reverse (so that we can grab the top three values later)
elf_totals.sort(reverse=True)

# Return highest value elf
highest_value = max(elf_totals)
print("Top elf: " + str(highest_value))

# Return top three elfs
top_three = elf_totals[0] + elf_totals[1] + elf_totals[2]
print("Top three elves: " + str(top_three))

