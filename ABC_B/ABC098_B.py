N = int(input())
S = list(input())
ans = 0
for i in range(1, N):
    ans_tmp = 0
    S_unique = list(set(S[0:i]))
    for j in S_unique:
        if j in S[i:N]:
            ans_tmp += 1
    ans = max(ans, ans_tmp)
print(ans)
