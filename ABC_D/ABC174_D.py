N = int(input())
C = list(input())

r_cnt = C.count('R')
w_cnt = 0
ans = 200000

if w_cnt <= r_cnt:
    ans = min(ans, r_cnt)
else:
    ans = min(ans, w_cnt)

for i in range(N):
    if C[i] == 'R':
        r_cnt -= 1
    else:
        w_cnt += 1

    if w_cnt <= r_cnt:
        ans = min(ans, r_cnt)
    else:
        ans = min(ans, w_cnt)
print(ans)
