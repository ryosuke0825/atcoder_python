n = int(input())
S = input()

W = [0]
E = [0]
for i in range(n):
    if S[i] == 'W':
        W.append(W[i]+1)
        E.append(E[i])
    else:
        W.append(W[i])
        E.append(E[i]+1)

ans = 3*10**5
for i in range(1, n+1):
    ans = min(ans, W[i-1]+E[-1]-E[i])
print(ans)
