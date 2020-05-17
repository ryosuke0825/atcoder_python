K = int(input())
S = input()

if len(S) <= K:
    print(S)
else:
    ans = S[0:K]
    ans += '...'
    print(ans)
