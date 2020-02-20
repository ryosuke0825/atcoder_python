s = input()
t = input()
atcoder = ['a', 't', 'c', 'o', 'd', 'e', 'r']
ans = 'You can win'
for i in range(len(s)):
    if s[i] == t[i]:
        continue
    if s[i] == "@" and t[i] in atcoder:
        continue
    if t[i] == "@" and s[i] in atcoder:
        continue
    ans = 'You will lose'
    break
print(ans)
