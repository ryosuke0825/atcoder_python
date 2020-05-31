H1, M1, H2, M2, K = map(int, input().split())

ans = (H2-H1)*60
if M1 <= M2:
    ans += M2-M1
else:
    ans -= M1-M2
ans -= K
print(ans)
