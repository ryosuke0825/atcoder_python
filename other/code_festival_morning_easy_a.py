N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    ans += A[i+1]-A[i]
print(ans/(N-1))
