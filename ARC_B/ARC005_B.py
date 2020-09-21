xyw = input().split()
X = int(xyw[0])-1
Y = int(xyw[1])-1

C = []
for _ in range(9):
    li = list(input())
    C.append(li)

ans = ''
flg = True
if xyw[2] == 'R':
    x_add = 1
    for i in range(4):
        ans += C[Y][X]
        if X == 8:
            x_add = -1
        X += x_add
elif xyw[2] == 'L':
    x_add = -1
    for i in range(4):
        ans += C[Y][X]
        if X == 0:
            x_add = 1
        X += x_add
elif xyw[2] == 'U':
    y_add = -1
    for i in range(4):
        ans += C[Y][X]
        if Y == 0:
            y_add = 1
        Y += y_add
elif xyw[2] == 'D':
    y_add = 1
    for i in range(4):
        ans += C[Y][X]
        if Y == 8:
            y_add = -1
        Y += y_add
elif xyw[2] == 'RU':
    x_add = 1
    y_add = -1
    for i in range(4):
        ans += C[Y][X]
        if X == 8 and Y == 0:
            x_add = -1
            y_add = 1
        elif X == 8 and Y != 0:
            x_add = -1
        elif X != 8 and Y == 0:
            y_add = 1
        X += x_add
        Y += y_add
elif xyw[2] == 'RD':
    x_add = 1
    y_add = 1
    for i in range(4):
        ans += C[Y][X]
        if X == 8 and Y == 8:
            x_add = -1
            y_add = -1
        elif X == 8 and Y != 8:
            x_add = -1
        elif X != 8 and Y == 8:
            y_add = -1
        X += x_add
        Y += y_add
elif xyw[2] == 'LU':
    x_add = -1
    y_add = -1
    for i in range(4):
        ans += C[Y][X]
        if X == 0 and Y == 0:
            x_add = 1
            y_add = 1
        elif X == 0 and Y != 0:
            x_add = 1
        elif X != 0 and Y == 0:
            y_add = 1
        X += x_add
        Y += y_add
elif xyw[2] == 'LD':
    x_add = -1
    y_add = 1
    for i in range(4):
        ans += C[Y][X]
        if X == 0 and Y == 8:
            x_add = 1
            y_add = -1
        elif X == 0 and Y != 8:
            x_add = 1
        elif X != 0 and Y == 8:
            y_add = -1
        X += x_add
        Y += y_add
print(ans)
