input = open("input.txt", "r")
data = input.read()
input.close()
forest = data.split("\n")

def treeScore(adjacent_trees, tree):
    # check how many trees can be seen in a given direction using the provided list of trees ordered in a direction moving away from the tree we're scoring
    score = 0
    for each in adjacent_trees:
        if each < tree:
            score += 1
        elif each >= tree:
            score += 1
            break
    return(score)


def processTree(input_row, input_column):
    row = forest[input_row] # create string containing all items in the trees row 
    tree = row[input_column] # get the actual tree we are checking 
    column = str("") # init empty string for column of trees
    for each in forest: # create new string containing column of trees
        column += str(each[input_column])

    # create arrays of trees to the left, right, above and below of tree we're checking
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
    # flip left and above - we need to check the trees moving away from the inner tree
    left.reverse()
    above.reverse()
    # calculate tree score
    score = treeScore(left, tree)  * treeScore(right, tree)  * treeScore(above, tree) * treeScore(below, tree) 
    return score

high_score = 0
tree_location = ""

for x in range(1, (len(forest) - 1)):
        for y in range(1, (len(forest[0]) - 1)):
            current_score = processTree(x , y)
            if current_score > high_score:
                high_score = current_score
                tree_location = str(x) + ", " + str(y)

print("High score: " + str(high_score))
print("Tree location: " + tree_location)
