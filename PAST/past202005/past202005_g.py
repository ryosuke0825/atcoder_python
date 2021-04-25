from collections import deque

N, X, Y = map(int, input().split())
p = deque()
p.append([0, 0, 1])

checked = {}
for _ in range(N):
    x, y = map(int, input().split())
    key = str(x)+'_'+str(y)
    checked[key] = True

move = [[1, 1], [0, 1], [-1, 1], [1, 0], [-1, 0], [0, -1]]
while len(p) != 0:
    xy = deque.popleft(p)
    for m in move:
        x = xy[0]+m[0]
        y = xy[1]+m[1]

        key = str(x)+'_'+str(y)
        if key in checked:
            continue

        if x == X and y == Y:
            print(xy[2])
            exit(0)
        elif -202 <= x <= 202 and -202 <= y <= 202:
            p.append([x, y, xy[2]+1])
            checked[key] = True
print(-1)
