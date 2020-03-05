n = int(input())

cnt = 0
i = 1
while True:
    num = list(str(i))
    for x in num:
        if num[0] != x:
            break
    else:
        cnt += 1
        if cnt == n:
            print(i)
            exit(0)
    i += 1
