input = open("input.txt", "r")
data = input.read()
input.close()
forest = data.split("\n")

visible_tree = 0

# add outer rim trees
visible_tree += len(forest) * 2 # add vertical trees 
visible_tree += (len(forest[0]) - 2 ) * 2 # add horizontal trees minus corner trees already counted

def innerTrees(input_row, input_column):
    row = forest[input_row] # create string containing all items in the trees row 
    tree = row[input_column] # get the actual tree we are checking 
    column = str("") # init empty string for column of trees
    for each in forest: # create new string containing column of trees
        column += str(each[input_column])

    # create arrays of trees to the left, right, above and below of tree we're checking
    sight = False
    left = []
    right = []
    above = []
    below = []
    for i in range(0, input_column):
        left.append(row[i])
    for i in range((input_column + 1), len(row)):
        right.append(row[i])
    for i in range(0, input_row):
        above.append(column[i])
    for i in range(input_row + 1, len(column)):
        below.append(column[i])
    # get the tallest tree in each direction and check if it's smaller than the tree we're checking
    if max(left) < tree or max(right) < tree or max(above) < tree or max(below) < tree:
        sight = True
    return sight
            
for x in range(1, (len(forest) - 1)):
        for y in range(1, (len(forest[0]) - 1)):
            sight = innerTrees(x , y)
            if sight == True:
                visible_tree += 1

print("There are " + str(visible_tree) + " visible trees from outside the forest.")