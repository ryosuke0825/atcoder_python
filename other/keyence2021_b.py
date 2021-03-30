from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

dic = defaultdict(lambda: 0)
a_max = 0
for a in A:
    dic[a] += 1
    a_max = max(a_max, a)

disp = []
cnt = dic[0]
for i in range(1, a_max+2):
    if cnt > dic[i]:
        for _ in range(cnt-dic[i]):
            disp.append(i)
        cnt = dic[i]

if len(disp) <= K:
    print(sum(disp))
else:
    ans = 0
    cnt = 0
    for i in reversed(range(len(disp))):
        ans += disp[i]
        cnt += 1
        if cnt >= K:
            break
    print(ans)
