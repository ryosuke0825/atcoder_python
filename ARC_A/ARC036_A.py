n, k = map(int, input().split())
ans = -1

byesterday = 0
yesterday = 0
for day in range(1, n+1):
    today = int(input())
    if today+yesterday+byesterday < k and day >= 3:
        ans = day
        break
    byesterday = yesterday
    yesterday = today
print(ans)
