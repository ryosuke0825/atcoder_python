n, m = map(int, input().split())

al = []
for _ in range(n):
    al.append(list(map(int, input().split())))

ans = 0
for i in range(m):
    for j in range(m):
        tmp_ans = 0
        for k in range(n):
            if i == j:
                continue

            tmp_ans += max(al[k][i], al[k][j])
        ans = max(ans, tmp_ans)
print(ans)
