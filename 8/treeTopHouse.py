input = open("input.txt", "r")
data = input.read()
input.close()
forest = data.split("\n")

x = 3
y = 1

visible_tree = 0

# add outer rim trees
visible_tree += len(forest) * 2
visible_tree += (len(forest[0]) - 2 ) * 2

print(visible_tree)

def innerTrees(input_row, input_column):
    row = forest[input_row - 1] # create string containing all items in the trees row 
    tree = row[input_column - 1] # get the actual tree we are checking
    column = str("") # init empty string for column of trees
    for each in forest: # create new string containing column of trees
        column += str(each[input_column - 1])

    # init row and column sight, assume sight is true to begin with
    row_sight = False 
    column_sight = False

    # check each row and column for a taller tree, skip the tree we're actually checking, if a taller tree is found set sight to false
    # check left
    for i in range(0, (x - 1)):
        if not row[i] >= tree:
            row_sight = True
    # check right
    for i in range((x + 1), len(row) - 1):
        if not row[i] >= tree:
            row_sight = True
    # check above
    for i in range(0, (y - 1)):
        if not column[i] >= tree:
            column_sight = True
    # check below
    for i in range((y + 1), len(column) - 1):
        if not column[i] >= tree:
            column_sight = True
    # print(row)
    # print(column)
    # print(tree)
    # print("Row sight: " + str(row_sight))
    # print("Column sight: " + str(column_sight))
    if row_sight or column_sight:
        return True
    else:   
        return False
            
for x in range(1, (len(forest) - 1)):
        for y in range(1, (len(forest[0]) - 1)):
            #print(str(x) + " " + str(y))
            sight = innerTrees(x , y)
            if sight == True:
                visible_tree += 1

print(visible_tree)