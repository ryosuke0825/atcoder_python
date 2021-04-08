N = int(input())

C = []
for _ in range(N):
    C.append(list(map(int, input().split())))

# 各値の右隣りの値との差が同じであることの確認
for x in range(N-1):
    diff = C[0][x]-C[0][x+1]
    for y in range(N):
        if C[y][x]-C[y][x+1] != diff:
            print('No')
            exit(0)

# 各値の下の値との差が同じであることの確認
for y in range(N-1):
    diff = C[y][0]-C[y+1][0]
    for x in range(N):
        if C[y][x]-C[y+1][x] != diff:
            print('No')
            exit(0)

# 1列目の最小値を0にしてAの値を作る
# 4,2,3=2,0,1
A = [0]*N
mn = 10**9+1
for i in range(N):
    mn = min(mn, C[i][0])
for i in range(N):
    A[i] = C[i][0]-mn

# 1行目目の最小値を0にしてAの値を作る
B = [0]*N
mn = min(C[0][:])
for i in range(N):
    B[i] = C[0][i]-mn

# 差を求めてBに足す
diff = C[0][0]-A[0]-B[0]
for i in range(N):
    B[i] += diff
print('Yes')
print(' '.join(map(str, A)))
print(' '.join(map(str, B)))
