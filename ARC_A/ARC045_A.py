S = input().split()

ans = ''
for s in S:
    if s == 'Left':
        ans += '< '
    elif s == 'Right':
        ans += '> '
    else:
        ans += 'A '
print(ans[:-1])
