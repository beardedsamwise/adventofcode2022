signal = open('input.txt', 'r').read()

def checkIfDuplicates(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

for i in range(len(signal)):
    current_signal = []
    for each in signal[i:i+4]:
        current_signal.append(each)
    result = checkIfDuplicates(current_signal)
    if not result:
        print('Marker location: ' + str(i + 4))
        break
