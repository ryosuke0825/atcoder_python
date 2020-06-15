s_list = input().split('+')

ans = 0
for s in s_list:
    if s.count('0') == 0:
        ans += 1
print(ans)
