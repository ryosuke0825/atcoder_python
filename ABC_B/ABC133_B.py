import math
N, D = map(int, input().split())
X = []

for _ in range(N):
    X.append(list(map(int, input().split())))

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        sum = 0
        for k in range(D):
            sum += (X[i][k] - X[j][k])**2
        if math.sqrt(sum).is_integer():
            cnt += 1
print(cnt)
