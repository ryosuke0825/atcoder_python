s = input()

ret = 0
for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
        ret += 1
print(ret)
