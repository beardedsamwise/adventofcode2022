import math

with open('input.txt') as f:
    input = [line.rstrip('\n') for line in f]

# create monkey dict
monkeys = {}
for each in input:
    if each.startswith('Monkey'):
        monkey_num = each.replace('Monkey ', '')
        monkey_num = int(monkey_num.replace(':', ''))
    elif each.startswith('  Starting items: '):
        starting_items = each.replace('  Starting items: ', '')
        starting_items = starting_items.split(', ')
    elif each.startswith('  Operation: '):
        operation = each.replace('  Operation: new = ', '')
        operation = operation.replace('old', 'int(old)')
    elif each.startswith('  Test: '):
        test = int(each.replace('  Test: divisible by ', ''))
    elif each.startswith('    If true: '):
        true_condition = int(each.replace('    If true: throw to monkey ', ''))
    elif each.startswith('    If false: '):
        false_condition = int(each.replace('    If false: throw to monkey ', ''))
    elif each == '':
        monkeys[monkey_num] = {'items': starting_items, 'operation': operation, 'test': test, 'true_condition': true_condition, 'false_condition': false_condition}

print(monkeys)

def monkey_loop(iterations: int) -> int:
    for i in range(iterations): # iterate over monkeys x number of times 
        for monkey in range(len(monkeys)): # iterate over each monkey 
            print("Current monkey is: "+ str(monkey))
            current_items = tuple(monkeys.get(monkey)['items'])
            print("Loaded current items: " +str(current_items))
            for item in range(len(current_items)): # iterate over each monkeys items 
                print("Item loop: " + str(item))
                print("Current items are: " + str(current_items))
                old = current_items[item]
                worry = eval(monkeys.get(monkey)['operation'])
                worry = math.floor(worry / 3)
                print("Worry is: " + str(worry))
                if worry % monkeys.get(monkey)['test'] == 0:
                    print("Throw to Monkey: " + str(monkeys.get(monkey)['true_condition']))
                    print(monkeys.get(monkey)['items'])
                    monkeys.get(true_condition)['items'].append(str(worry))
                    monkeys.get(monkey)['items'].pop(0)
                else:
                    print("Throw to Monkey: " + str(monkeys.get(monkey)['false_condition']))
                    monkeys.get(false_condition)['items'].append(str(worry))
                    monkeys.get(monkey)['items'].pop(0)
                print("Items are now: " + str(monkeys.get(monkey)['items']))

monkey_loop(1)

print(monkeys)

# create monkey class
# class Monkey:
#     def __init__(self, number, items, operation, test, true_condition, false_condition):
#         self.number = number
#         self.items = items
#         self.operation = operation
#         self.test = test
#         self.true_condition = true_condition
#         self.false_condition = false_condition

