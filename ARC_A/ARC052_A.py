s = input()
ans = ''
for i in s:
    if i.isdecimal():
        ans += i
print(ans)
