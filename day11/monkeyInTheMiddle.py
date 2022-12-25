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
    elif each.startswith('  Test: '):
        test = int(each.replace('  Test: divisible by ', ''))
    elif each.startswith('    If true: '):
        true_condition = int(each.replace('    If true: throw to monkey ', ''))
    elif each.startswith('    If false: '):
        false_condition = int(each.replace('    If false: throw to monkey ', ''))
    elif each == '':
        monkeys[monkey_num] = {'start_items': starting_items, 'operation': operation, 'test': test, 'true_condition': true_condition, 'false_condition': false_condition}

# create monkey class
class Monkey:
    def __init__(self, number, items, operation, test, true_condition, false_condition):
        self.number = number
        self.items = items
        self.operation = operation
        self.test = test
        self.true_condition = true_condition
        self.false_condition = false_condition