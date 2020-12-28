with open('input/input2.txt') as f:
    lines = [i.strip() for i in f.readlines()]

#part one
validPasswordsPartOne = 0
validPasswordsPartTwo = 0

for line in lines:
    if (str(line) in lines):
        policy = line.split(':', 1)[0]
        minMax = policy.split(' ', 1)[0]
        min = minMax.split('-')[0]
        max = minMax.split('-')[1]
        character = policy.split(' ')[1]
        password = line.split(':', 1)[1].strip()
        # print('Found policy: ', min, max, character)
        # print('Found password: ', password)
        countPartOne = 0
        for i in password:
            if i == character:
                countPartOne = countPartOne + 1

        if (countPartOne >= int(min) and countPartOne <= int(max)):
            validPasswordsPartOne = validPasswordsPartOne + 1

        if ((password[int(min)-1] == character) != (password[int(max)-1] == character)):
            validPasswordsPartTwo = validPasswordsPartTwo + 1


print('Found validPasswords part one: ', validPasswordsPartOne)
print('Found validPasswords part two: ', validPasswordsPartTwo)
