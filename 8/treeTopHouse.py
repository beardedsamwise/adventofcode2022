input = open("input.txt", "r")
data = input.read()
input.close()
forest = data.split("\n")

visible_tree = 0

# add outer rim trees
visible_tree += len(forest) * 2 # add vertical trees 
visible_tree += (len(forest[0]) - 2 ) * 2 # add horizontal trees minus corner trees already counted

def innerTrees(input_row, input_column):
    row = forest[input_row - 1] # create string containing all items in the trees row 
    tree = row[input_column - 1] # get the actual tree we are checking
    column = str("") # init empty string for column of trees
    for each in forest: # create new string containing column of trees
        column += str(each[input_column - 1])

    # init row and column sight, assume sight is true to begin with
    sight = False

    # check left
    for i in range(0, (x - 1)):
        if not row[i] >= tree:
            sight = True
    # check right
    for i in range((x + 1), len(row) - 1):
        if not row[i] >= tree:
            sight = True
    # check above
    for i in range(0, (y - 1)):
        if not column[i] >= tree:
            sight = True
    # check below
    for i in range((y + 1), len(column) - 1):
        if not column[i] >= tree:
            sight = True
    return sight
            
for x in range(1, (len(forest) - 1)):
        for y in range(1, (len(forest[0]) - 1)):
            sight = innerTrees(x , y)
            if sight == True:
                visible_tree += 1

print(visible_tree)