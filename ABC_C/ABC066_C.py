from collections import deque

N = int(input())
A = list(map(int, input().split()))
ans = deque([])

for i in range(1, N+1):
    if i % 2 == N % 2:
        ans.appendleft(A[i-1])
    else:
        ans.append(A[i-1])
print(*ans)
