def countTrees(right, down):
    with open('input/input3.txt') as lines:
        trees = 0
        for count, value in enumerate(lines):
            if count % down == 0 and value[int(count/down * right) % (len(value.strip()))] == '#':
                trees = trees + 1
        return trees

print('Part one: ', countTrees(3, 1))

print('Part two: ', countTrees(1, 1) * countTrees(3, 1) * countTrees(5, 1) * countTrees(7, 1) * countTrees(1, 2))

