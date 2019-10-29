import math
N, D = map(int, input().split())
X = []

for _ in range(N):
    X.append(list(map(int, input().split())))

cnt = 0
for i in range(0, len(X)):
    sum = 0
    for j in range(i+1, len(X)):
        for k in range(0, len(X[i])):
            sum += (X[i][k] - X[j][k])**2

        print(sum)
        if math.sqrt(sum).is_integer():
            cnt += 1
print(cnt)
