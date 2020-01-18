s = list(input())
t = list(input())

ret = 0
if s[0] == t[0]:
    ret += 1
if s[1] == t[1]:
    ret += 1
if s[2] == t[2]:
    ret += 1

print(ret)
