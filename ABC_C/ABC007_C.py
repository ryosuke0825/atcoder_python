import sys
from collections import deque


def input():
    return sys.stdin.readline()[:-1]


R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

RC = []
for _ in range(R):
    c = list(input())
    RC.append(c)

q = deque([[sy, sx, 0]])
checked = [[0] * C for i in range(R)]
checked[sy][sx] = -1
while len(q) != 0:
    y, x, cnt = q.popleft()
    if y == gy and x == gx:
        print(cnt)
        exit(0)

    if RC[y+1][x] == '.' and checked[y+1][x] == 0:
        checked[y+1][x] = -1
        q.append([y+1, x, cnt+1])

    if RC[y-1][x] == '.' and checked[y-1][x] == 0:
        checked[y-1][x] = -1
        q.append([y-1, x, cnt+1])

    if RC[y][x+1] == '.' and checked[y][x+1] == 0:
        checked[y][x+1] = -1
        q.append([y, x+1, cnt+1])

    if RC[y][x-1] == '.' and checked[y][x-1] == 0:
        checked[y][x-1] = -1
        q.append([y, x-1, cnt+1])
