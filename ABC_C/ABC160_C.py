k, n = map(int, input().split())
A = list(map(int, input().split()))

kyori = 0
if A[0] == 0:
    kyori = k-A[-1]
else:
    kyori = k-(A[-1]-A[0])

for i in range(n-1):
    kyori = max(kyori, A[i+1]-A[i])
print(k-kyori)
