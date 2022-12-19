input = open("input.txt", "r")
data = input.read()
input.close()
data_into_list = data.split("\n")

x = 3
y = 1

def test(input_row, input_column):
    row = data_into_list[input_row - 1]
    tree = row[input_column - 1]
    column = str("")
    for each in data_into_list:
        column += str(each[input_column - 1])
    row_sight = True
    column_sight = True
    for i in range(len(row)):
        if i == int(input_row) - 1:
            continue
        elif each >= tree:
            row_sight = False
    for i in range(len(column)):
        if i == int(input_column) - 1:
            continue
        elif each >= tree:
            column_sight = False
    print(row)
    print(column)
    print(tree)
    print("Row sight: " + str(row_sight))
    print("Column sight: " + str(column_sight))
            

test(x, y)
