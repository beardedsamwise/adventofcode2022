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
        operation = each.replace('  Operation: ', '')
    elif each.startswith('  Test: '):
        test = each.replace('  Test: ', '')
    elif each.startswith('    If true: '):
        true_condition = each.replace('    If true: ', '')
    elif each.startswith('    If false: '):
        false_condition = each.replace('    If false: ', '')
    elif each == '':
        monkeys[monkey_num] = {'start_items': starting_items, 'operation': operation, 'test': test, 'true_condition': true_condition, 'false_condition': false_condition}

print(monkeys)