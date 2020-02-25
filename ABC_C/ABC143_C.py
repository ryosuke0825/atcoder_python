_ = input()
S = input()

before_s = S[0]
ans = ''
for i in range(1, len(S)):
    if S[i] != before_s:
        ans += S[i]
        before_s = S[i]

print(len(ans)+1)
