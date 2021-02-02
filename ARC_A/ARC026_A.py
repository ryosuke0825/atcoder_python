N, A, B = map(int, input().split())

ans = 0
if N <= 5:
    ans = B*N
else:
    ans = A*(N-5)+B*5
print(ans)
