N = int(input())
A = list(map(int, input().split()))

ans1 = A[0]
for i in range(1, N):
    ans1 = ans1 ^ A[i]

ans2 = []
for i in range(N):
    ans2.append(ans1 ^ A[i])

print(*ans2)
