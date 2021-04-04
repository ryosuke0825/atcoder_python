A, B, W = map(int, input().split())
W *= 1000

mx = 0
mn = 1000*1000
for i in range(1, 1000*1000+1):
    if A*i <= W <= B*i:
        mn = min(mn, i)
        mx = max(mx, i)

if mx == 0:
    print('UNSATISFIABLE')
else:
    print(mn, mx)
