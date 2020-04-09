abc = list(map(int, input().split()))

cnt = 0
while True:
    if abc[0] == abc[1] == abc[2]:
        print(cnt)
        break

    if abc.count(min(abc)) == 2:
        if abc.count(abc[0]) == 2 and abc.count(abc[1]) == 2:
            abc[0] += 1
            abc[1] += 1
        if abc.count(abc[0]) == 2 and abc.count(abc[2]) == 2:
            abc[0] += 1
            abc[2] += 1
        if abc.count(abc[1]) == 2 and abc.count(abc[2]) == 2:
            abc[1] += 1
            abc[2] += 1
    else:
        abc[abc.index(min(abc))] += 2
    cnt += 1
