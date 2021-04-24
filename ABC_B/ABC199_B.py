N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mn = 0
mx = 1001
for i in range(N):
    mn = max(mn, A[i])
    mx = min(mx, B[i])
print(max(0, mx-mn+1))
