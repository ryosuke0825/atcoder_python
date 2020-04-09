S = input()
N = len(S)
A = [0]*(N+1)
B = [0]*(N+1)

for i in range(N):
    if S[i] == '<':
        A[i+1] = A[i]+1
    else:
        A[i+1] = 0

for i in range(N):
    if S[N-i-1] == '>':
        B[N-i-1] = B[N-i]+1
    else:
        B[N-i-1] = 0

ans = 0
for i in range(N+1):
    ans += max(A[i], B[i])
print(ans)
