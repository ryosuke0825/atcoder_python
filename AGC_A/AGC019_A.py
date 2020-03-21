import math

q, h, s, d = map(int, input().split())
n = int(input())*100

qq = [q, q, 25]
hh = [h/2, h, 50]
ss = [s/4, s, 100]
dd = [d/8, d, 200]
qhsd = [qq, hh, ss, dd]
qhsd.sort()

ans = 0
for i in range(4):
    num = n//qhsd[i][2]
    n -= num*qhsd[i][2]
    ans += num*qhsd[i][1]
print(ans)
