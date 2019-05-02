N, M, X, Y = map(int, input().split())
XY = []
for i in range(2):
    tmp = list(map(int, input().split()))
    XY.append(tmp)

max_x = max(XY[0])
max_x = max(X, max_x)
min_y = min(XY[1])
min_y = min(Y, min_y)

print("No War" if max_x < min_y else "War")
