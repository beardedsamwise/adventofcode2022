import re

with open('input.txt') as f:
    puzzle = [line.rstrip('\n') for line in f]

current_dir_list = []
current_dir_str = ""
size_tree = {}

# create dictionary of dirs + file sizes
for output in puzzle:
    if (output.startswith('$')):
        # change directories
        if "cd" in output:
            if "cd .." in output:
                current_dir_list.pop(-1)
            else:
                dir = output.replace('$ cd ', '')
                if dir != '/':
                    current_dir_list.append(dir + "/")
                else:
                    current_dir_list.append(dir)
            current_dir_str = ''.join(current_dir_list)
        if "ls" in output: # we don't actually do anything with the ls command
            continue
    elif "dir" in output: # skip lines that list directories after ls is executed
        continue
    elif output[:1].isdigit(): # check if output starts with a digit, which should be a file size
        size = int(re.search(r'\d+', output).group())
        if current_dir_str in size_tree.keys():
            size_tree[current_dir_str].append(size)
        else:
            size_tree[current_dir_str] = []
            size_tree[current_dir_str].append(size)

# calculate file sizes
tally = 0
for dir_par,sizes_par in size_tree.items():
    if dir_par == "/": # skip the root dir, even though it's probably too big
        continue
    else:
        print("Processing " + dir_par)
        size = 0
        for dir_child,sizes_child in size_tree.items():
            if dir_par == dir_child: # add the current directory to size
                size += sum(sizes_child)
                print("Adding " + dir_par)
            elif dir_child.startswith(dir_par): # check if other dirs are child directories, if so add to size
                print("Adding " + dir_child + " to tally.")
                size += sum(sizes_child)
        print("Size: " + str(size))
        if size <= 100000: # if size of parent + child dirs is under threshold, add to tally
            print("Directory is under the threshold, adding...")
            tally += size
        else:
            print("Too big... skipping...")
        input("Press Enter to continue...")
    

print(size_tree)
print(tally)




        