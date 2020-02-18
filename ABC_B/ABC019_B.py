s = input()

cnt = 1
ans = ""
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        cnt += 1
    else:
        ans += s[i-1]+str(cnt)
        cnt = 1
ans += s[-1]+str(cnt)
print(ans)
