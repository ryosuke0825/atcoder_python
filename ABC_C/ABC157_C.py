n, m = map(int, input().split())
ans = [10]*n

sl = []
cl = []
for _ in range(m):
    s, c = map(int, input().split())
    if s in sl:
        if cl[sl.index(s)] != c:
            print(-1)
            exit(0)
    sl.append(s)
    cl.append(c)

for i in range(m):
    if ans[sl[i]-1] > cl[i]:
        ans[sl[i]-1] = cl[i]

if ans[0] == 0 and len(ans) != 1:
    print(-1)
    exit(0)

for i in range(len(ans)):
    if i == 0 and ans[i] == 10 and n != 1:
        ans[i] = 1
    elif ans[i] == 10:
        ans[i] = 0

ans2 = []
for i in ans:
    ans2.append(str(i))
ans3 = "".join(ans2)
ans3_len = len(str(int(ans3)))
if n == ans3_len:
    print(int(ans3))
else:
    print(-1)
