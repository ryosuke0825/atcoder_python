n = int(input())
ans = [0]*6
for _ in range(n):
    maxt, mint = map(float, input().split())
    if maxt >= 35:
        ans[0] += 1
    elif maxt >= 30:
        ans[1] += 1
    elif maxt >= 25:
        ans[2] += 1

    if mint >= 25:
        ans[3] += 1

    if mint < 0 <= maxt:
        ans[4] += 1
    elif maxt < 0:
        ans[5] += 1

ans_str = [str(a) for a in ans]
print(' '.join(ans_str))
