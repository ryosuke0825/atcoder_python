S = list(map(int, input()))

ans = S[0]
for i in range(1, len(S)):
    if i % 2 != 0:
        ans -= S[i]
    else:
        ans += S[i]
print(ans)
