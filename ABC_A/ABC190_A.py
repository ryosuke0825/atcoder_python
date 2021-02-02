A, B, C = map(int, input().split())

ans = ''
if A > B:
    ans = 'Takahashi '
elif B > A:
    ans = 'Aoki'
else:
    if C:
        ans = 'Takahashi '
    else:
        ans = 'Aoki'
print(ans)
