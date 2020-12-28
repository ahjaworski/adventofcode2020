import re

requiredKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passports = []

passportIndex = 0
with open('input/input4.txt') as f:
    lines = [i.strip() for i in f.readlines()]
    for line in lines:
        if line == '\n' or line == '':
            passportIndex = passportIndex + 1
        else:
            passportKeys = re.findall('(\S*):\S', line)
            passportValues = re.findall('\S*:(\S*)', line)
            passportDict = dict(zip(passportKeys, passportValues))
            if (len(passports) == passportIndex):
                passports.append(dict(zip(passportKeys, passportValues)))
            else:
                passports[passportIndex].update(dict(zip(passportKeys, passportValues)))

# part one
validPassports = []
for passport in passports:
    if all(key in passport for key in requiredKeys):
        validPassports.append(passport)

print('Part one', len(validPassports))


# part two
validPassportsPartTwo = []
for passport in validPassports:
    byr = int(passport.get('byr'))
    validByr = byr >= 1920 and byr <= 2002

    iyr = int(passport.get('iyr'))
    validIyr = iyr >= 2010 and iyr <= 2020

    eyr = int(passport.get('eyr'))
    validEyr = eyr >= 2020 and eyr <= 2030

    hgt = passport.get('hgt')
    validHgt = False
    if (re.search('\d*in', hgt) != None):
        intHgt = int(re.search(r'\d+', hgt).group())
        validHgt = intHgt >= 59 and intHgt <= 76
    if (re.match('\d*cm', hgt) != None):
        intHgt = int(re.search(r'\d+', hgt).group())
        validHgt = intHgt >= 150 and intHgt <= 193

    hcl = passport.get('hcl')
    validHcl = len(hcl) == 7 and re.search('#[0-9a-f]{6}', hcl) != None

    ecl = passport.get('ecl')
    validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    validEcl = ecl in validEyeColors

    pid = passport.get('pid')
    validPid = len(pid) == 9 and re.search('[0-9]{9}', pid) != None

    if (validByr and validIyr and validEyr and validHgt and validHcl and validEcl and validPid):
        validPassportsPartTwo.append(passport)

print('Part two', len(validPassportsPartTwo))







