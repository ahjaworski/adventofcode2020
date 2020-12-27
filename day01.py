with open('input/input1.txt') as f:
    lines = [i.strip() for i in f.readlines()]

#part one
for line in lines:
    valueToFind = 2020-int(line)
    if (str(valueToFind) in lines):
        print('Found value: ', valueToFind)
        print('Solution: ', valueToFind*int(line))

#part two
for line in lines:
    for anotherLine in lines:
        valueToFind = 2020 - int(line) - int(anotherLine)
        if (str(valueToFind) in lines):
            print('Found value: ', valueToFind)
            print('Solution: ', valueToFind * int(anotherLine) * int(line))

