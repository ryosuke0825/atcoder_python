import sys

ans = 0


def input():
    return sys.stdin.readline()[:-1]


def dfs(ice, i, j, cnt):
    ice[i][j] = 0
    if ice[i+1][j] == 1:
        dfs(ice, i+1, j, cnt+1)
    if ice[i-1][j] == 1:
        dfs(ice, i-1, j, cnt+1)
    if ice[i][j+1] == 1:
        dfs(ice, i, j+1, cnt+1)
    if ice[i][j-1] == 1:
        dfs(ice, i, j-1, cnt+1)
    ice[i][j] = 1

    if (ice[i-1][j] and ice[i+1][j] and ice[i][j-1] and ice[i][j+1]) == 0:
        global ans
        ans = max(ans, cnt+1)


M = int(input())
N = int(input())
ice = [[0]*(M+2)]
for i in range(N):
    tmp = list(map(int, input().split()))
    ice.append([0]+tmp+[0])
ice.append([0]*(M+2))


for i in range(1, N+1):
    for j in range(1, M+1):
        if ice[i][j] == 1:
            dfs(ice, i, j, 0)
print(ans)
