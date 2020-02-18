n = int(input())
al = list(map(int, input().split()))

ans = 0
for a in al:
    while True:
        if a % 2 == 0 or a % 3 == 2:
            ans += 1
            a -= 1
        else:
            break

print(ans)
