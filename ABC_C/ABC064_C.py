N = int(input())
A = list(map(int, input().split()))

cnt = [0]*8
ziyu = 0
for a in A:
    if 1 <= a <= 399 and cnt[0] == 0:
        cnt[0] = 1
    elif 400 <= a <= 799 and cnt[1] == 0:
        cnt[1] = 1
    elif 800 <= a < 1199 and cnt[2] == 0:
        cnt[2] = 1
    elif 1200 <= a <= 1599 and cnt[3] == 0:
        cnt[3] = 1
    elif 1600 <= a <= 1999 and cnt[4] == 0:
        cnt[4] = 1
    elif 2000 <= a <= 2399 and cnt[5] == 0:
        cnt[5] = 1
    elif 2400 <= a <= 2799 and cnt[6] == 0:
        cnt[6] = 1
    elif 2800 <= a <= 3199 and cnt[7] == 0:
        cnt[7] = 1
    elif a >= 3200:
        ziyu += 1

min_cnt = 0
if ziyu > 0:
    min_cnt = 1

print(max(min_cnt, sum(cnt)), sum(cnt)+ziyu)
