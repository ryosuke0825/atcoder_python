n, l = map(int, input().split())
apples = [0 for i in range(n)]

for i in range(n):
    apples[i] = i+l

apples.sort(key=lambda x: abs(x))
print(sum(apples[1:]))
