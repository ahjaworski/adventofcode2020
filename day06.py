with open('input/input6.txt') as f:
    groups = f.read().split("\n\n")

    uniqueAnswers = 0
    for group in groups:
        answers = group.replace("\n", "")
        uniqueAnswers += len(set(answers))
    print("part one:", str(uniqueAnswers))


    uniqueAnswersEveryone = []
    for group in groups:
        persons = group.split("\n")
        answers = set(persons[0])
        for i in range(1, len(persons)):
            answers &= set(persons[i])
        uniqueAnswersEveryone.append(len(answers))
    print("part two:", str(sum(uniqueAnswersEveryone)))
