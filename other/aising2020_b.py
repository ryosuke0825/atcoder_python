N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(0, N, 2):
    if A[i] % 2 != 0:
        ans += 1
print(ans)
