n, m = map(int, input().split())
wa = [0 for _ in range(n)]
ac = [0 for _ in range(n)]

for _ in range(m):
    p, s = input().split()
    if s == 'WA' and ac[int(p)-1] == 0:
        wa[int(p)-1] += 1
    else:
        if ac[int(p)-1] == 0:
            ac[int(p)-1] = 1

wa_ans = 0
ac_ans = sum(ac)
for i in range(n):
    if ac[i] == 1:
        wa_ans += wa[i]

print(ac_ans, wa_ans)
