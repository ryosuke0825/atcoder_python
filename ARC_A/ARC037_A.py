n = int(input())
ml = map(int, input().split())

ans = 0
for m in ml:
    if m < 80:
        ans += 80-m
print(ans)
