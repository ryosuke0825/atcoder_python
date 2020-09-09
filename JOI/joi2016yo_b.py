N, M = map(int, input().split())
A = [0]*N
for i in range(N):
    A[i] = int(input())

for k in range(1, M+1):
    for i in range(N-1):
        if A[i] % k > A[i+1] % k:
            A[i], A[i+1] = A[i+1], A[i]

for i in range(N):
    print(A[i])
