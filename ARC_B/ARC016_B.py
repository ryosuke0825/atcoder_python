N = int(input())
X = []
for _ in range(N):
    tmp = list(input())
    X.append(tmp)

ans = 0
for i in range(len(X[0])):
    for j in range(N):
        if X[j][i] == 'x':
            ans += 1
        elif X[j][i] == 'o' and (j == 0 or (j != 0 and X[j-1][i] != 'o')):
            ans += 1
print(ans)
