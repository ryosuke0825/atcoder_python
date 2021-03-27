N, X = map(int, input().split())

X *= 100
ans = -1
alc = 0
for i in range(1, N+1):
    V, P = map(int, input().split())

    if ans != -1:
        continue

    alc += V*P

    if alc > X:
        ans = i
print(ans)
