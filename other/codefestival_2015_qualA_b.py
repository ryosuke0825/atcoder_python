N = int(input())
A = list(map(int, input().split()))

ans = A[0]
for i in range(1, N):
    ans = ans*2+A[i]
print(ans)
