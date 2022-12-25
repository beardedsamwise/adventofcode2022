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

print(monkeys[0])

for monkey, values in monkeys.items():
    print("Current monkey is: "+ str(monkey))
    for item in values['items']:
        print("Current item is: " + str(item))
        old = item
        worry = eval(values['operation'])
        worry = math.floor(worry / 3)
        print("Worry is: " + str(worry))
        if worry % values['test'] == 0:
            print("Throw to Monkey: " + str(values['true_condition']))
            print(monkeys[monkey]['items'])
            print(monkeys[false_condition]['items'])
            monkeys[true_condition]['items'].append(str(worry))
            monkeys[monkey]['items'].pop(0)
            print(monkeys[monkey]['items'])
            print(monkeys[false_condition]['items'])
        else:
            print("Throw to Monkey: " + str(values['false_condition']))
            print(monkeys[monkey]['items'])
            print(monkeys[false_condition]['items'])
            monkeys[false_condition]['items'].append(str(worry))
            monkeys[monkey]['items'].pop(0)
            print(monkeys[monkey]['items'])
            print(monkeys[false_condition]['items'])
            



# create monkey class
# class Monkey:
#     def __init__(self, number, items, operation, test, true_condition, false_condition):
#         self.number = number
#         self.items = items
#         self.operation = operation
#         self.test = test
#         self.true_condition = true_condition
#         self.false_condition = false_condition

