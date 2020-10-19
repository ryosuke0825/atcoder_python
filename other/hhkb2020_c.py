N = int(input())
P = list(map(int, input().split()))

used = set()
ans = 0
for i in range(N):
    used .add(P[i])

    if P[i] != ans:
        print(ans)
    else:
        while ans in used:
            ans += 1
        print(ans)
