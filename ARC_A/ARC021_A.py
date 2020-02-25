al = []
for _ in range(4):
    a = list(map(int, input().split()))
    al.append(a)

ans = 'GAMEOVER'
for i in range(4):
    for j in range(4):
        # 上下で動かせるか
        if i == 0:
            if al[i][j] == al[i+1][j]:
                ans = 'CONTINUE'
        elif i == 3:
            if al[i][j] == al[i-1][j]:
                ans = 'CONTINUE'
        else:
            if al[i][j] == al[i+1][j] or al[i][j] == al[i-1][j]:
                ans = 'CONTINUE'

        # 左右で動かせるか
        if j == 0:
            if al[i][j] == al[i][j+1]:
                ans = 'CONTINUE'
        elif j == 3:
            if al[i][j] == al[i][j-1]:
                ans = 'CONTINUE'
        else:
            if al[i][j] == al[i][j+1] or al[i][j] == al[i][j-1]:
                ans = 'CONTINUE'

print(ans)
