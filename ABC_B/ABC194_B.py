N = int(input())
A = [0]*N
B = [0]*N

for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b

i = A.index(min(A))
j = B.index(min(B))
a, b = A[i], B[j]

ans = 0
if i == j:
    del A[i]
    del B[j]
    ans = min(a+b, max(a, min(B)), max(min(A), b))
else:
    ans = max(a, b)
print(ans)
