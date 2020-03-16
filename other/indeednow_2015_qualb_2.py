s = input()
t = input()

ans = 0
if s == t:
    print(ans)
    exit(0)

for i in range(len(s)):
    s = s[-1]+s[:-1]
    ans += 1
    if s == t:
        print(ans)
        break
else:
    print(-1)
