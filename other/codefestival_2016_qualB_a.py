s = input()
signboard = 'CODEFESTIVAL2016'

ans = 0
for i in range(len(s)):
    if s[i] != signboard[i]:
        ans += 1
print(ans)
