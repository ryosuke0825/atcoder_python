n, t = map(int, input().split())

ans = 0
close_time = 0
for _ in range(n):
    a = int(input())
    new_close_time = a+t

    # 自動ドアは閉まっている。tを加算する。
    if close_time == 0 or close_time <= a:
        ans += t
        close_time = new_close_time
    # 自動ドアは開いている。差分だけ加算する。
    else:
        ans += new_close_time-close_time
        close_time = new_close_time

print(ans)
