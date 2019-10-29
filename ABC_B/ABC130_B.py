N, X = map(int, input().split())
L = list(map(int, input().split()))

sum = 0
cnt = 1
for i in range(0, N):
    sum += L[i]
    if X < sum:
        print(cnt)
        break
    else:
        cnt += 1
else:
    print(cnt)
