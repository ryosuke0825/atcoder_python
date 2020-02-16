n = int(input())
sl = {}

for i in range(n):
    s = input()
    if not(s in sl):
        sl[s] = 0
    else:
        sl[s] += 1

ans = []
s_max = max(sl.values())
for key in sl:
    if sl[key] == s_max:
        ans.append(key)

ans.sort()
for a in ans:
    print(a)
