n = int(input())
al = list(map(int, input().split()))

if sum(al) % n != 0:
    print(-1)
else:
    ave = sum(al) // n
    population = 0
    ans = 0
    for a in al:
        population += (a-ave)
        if population != 0:
            ans += 1

    print(ans)
