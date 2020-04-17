import copy

n, q = map(int, input().split())
Q = []
for _ in range(q):
    s = list(map(int, input().split()))
    Q.append(s)

N = [['N'] * n for i in range(n)]
for i in range(q):
    # 誰かをフォローする
    if Q[i][0] == 1:
        N[Q[i][1]-1][Q[i][2]-1] = 'Y'

    # フォロー返し
    elif Q[i][0] == 2:
        for j in range(n):
            if j == Q[i][1]-1:
                continue
            elif N[j][Q[i][1]-1] == 'Y':
                N[Q[i][1]-1][j] = 'Y'

    # あるユーザがフォローしているユーザがフォローしているユーザをフォローする
    elif Q[i][0] == 3:
        # その時点でフォローしている情報を退避しておく
        tmp = copy.deepcopy(N[Q[i][1]-1])
        for j in range(n):
            # あるユーザがフォローしているかどうか
            if j == Q[i][1]-1:
                continue
            elif tmp[j] == 'Y':
                for k in range(n):
                    if k == Q[i][1]-1:
                        continue
                    elif N[j][k] == 'Y':
                        N[Q[i][1]-1][k] = 'Y'

for i in range(n):
    print(''.join(N[i]))
