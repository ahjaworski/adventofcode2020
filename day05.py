with open('input/input5.txt') as f:
    lines = [i.strip() for i in f.readlines()]
    seats = []
    for line in lines:
        seats.append(int("".join(map(lambda seat: "1" if seat in "BR" else "0", line.rstrip())), 2))

    seats.sort()
    print('part one: ', max(seats))

    ourSeat = next(filter(lambda possibleseat: possibleseat not in seats, range(min(seats), max(seats))))
    print('part two: ', ourSeat)



