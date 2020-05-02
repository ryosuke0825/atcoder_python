X = int(input())

azuke = 100
ans = 0
while True:
    azuke = int(azuke*1.01)

    ans += 1
    if azuke >= X:
        print(ans)
        exit(0)
