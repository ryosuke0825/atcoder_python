import re

S = input().split()
N = int(input())
pattern = []
for _ in range(N):
    t = input()
    t = t.replace('*', '[a-z]')
    pattern.append(t)

ans = []
for s in S:
    flag = False
    for i in range(N):
        if re.fullmatch(pattern[i], s):
            flag = True

    if flag:
        ans.append('*'*len(s))
    else:
        ans.append(s)

print(*ans)
