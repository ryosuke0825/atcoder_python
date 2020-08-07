N = int(input())
A = list(map(int, input().split()))

ans = 0
cnt = 0
before = A[0]
for i in range(N):
    if A[i] > before:
        cnt += 1
    else:
        cnt = 1

    ans += cnt
    if i > 0:
        before = A[i]

print(ans)
