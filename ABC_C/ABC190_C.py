import sys


def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split())
AB = [[0] * 2 for i in range(M)]
for i in range(M):
    a, b = map(int, input().split())
    AB[i][0] = a-1
    AB[i][1] = b-1
K = int(input())
CD = [[0] * 2 for i in range(K)]
for i in range(K):
    c, d = map(int, input().split())
    CD[i][0] = c-1
    CD[i][1] = d-1

ans = 0
for i in range(2**K):
    dish = [0]*N
    for j in range(K):
        # Cに置く
        if ((i >> j) & 1):
            dish[CD[j][0]] = 1
            # Dに置く
        else:
            dish[CD[j][1]] = 1

        # 満たした条件を集計する
        tmp_ans = 0
        for m in range(M):
            if dish[AB[m][0]] == 1 and dish[AB[m][1]] == 1:
                tmp_ans += 1

        # 条件を満たす最大を更新する
        ans = max(ans, tmp_ans)
print(ans)
