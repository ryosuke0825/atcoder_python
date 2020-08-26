N = int(input())
A = list(map(int, input().split()))

mx = A[0]
ans = 0
for i in range(1, N):
    if A[i] < mx:
        ans += mx-A[i]
    elif A[i] > mx:
        mx = A[i]
print(ans)
