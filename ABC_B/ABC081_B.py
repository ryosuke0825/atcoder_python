n = int(input())
al = list(map(int, input().split()))

ans = 0
while True:
    for i in range(n):
        if al[i] % 2 == 0:
            al[i] = al[i]//2
        else:
            break
    else:
        ans += 1
        continue
    break

print(ans)
