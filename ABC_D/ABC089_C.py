N = int(input())
S = [0]*5
for _ in range(N):
    s = input()
    if s[0] == 'M':
        S[0] += 1
    elif s[0] == 'A':
        S[1] += 1
    elif s[0] == 'R':
        S[2] += 1
    elif s[0] == 'C':
        S[3] += 1
    elif s[0] == 'H':
        S[4] += 1

if sum(S) == 0:
    print(0)
    exit(0)

I = [0, 0, 0, 0, 0, 0, 1, 1, 1, 2]
J = [1, 2, 3, 1, 1, 2, 2, 3, 2, 3]
K = [2, 3, 4, 3, 4, 4, 3, 4, 4, 4]
ans = 0
for i in range(10):
    ans += S[I[i]]*S[J[i]]*S[K[i]]
print(ans)
