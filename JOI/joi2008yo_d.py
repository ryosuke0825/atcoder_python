m = int(input())
M = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    M.append(tmp)

n = int(input())
N = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    N.append(tmp)

# 探したい星座の最も左下(0,0)に近い星（ベース）を探す
base = [1000000, 1000000]
for i in range(m):
    if M[i][0] < base[0]:
        base[0] = M[i][0]
        base[1] = M[i][1]
    elif M[i][0] == base[0] and M[i][1] < base[1]:
        base[0] = M[i][0]
        base[1] = M[i][1]

# 探したい星座の各星のベースに対する差を求める
base_dic = {}
for i in range(m):
    key = str(base[0]-M[i][0]) + '_' + str(base[1]-M[i][1])
    base_dic[key] = True

# 写真に写っている星を順番にベースとしていく
# ベースに対する各星の差を求めて、探したい星座の差すべてと一致したら、
# その時のベースにしている星と探したい星座のベースとの差を求める
for i in range(n):
    tmp_base = N[i]
    match = 0
    for j in range(n):
        key = str(tmp_base[0]-N[j][0]) + '_' + str(tmp_base[1]-N[j][1])
        if key in base_dic:
            match += 1
    # 一致した数が星座の星の数と同じなら
    if match == m:
        print(tmp_base[0]-base[0], tmp_base[1]-base[1])
        exit(0)
