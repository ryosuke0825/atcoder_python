r, D, x2000 = map(int, input().split())

for _ in range(0, 10):
    x2000 = r*x2000-D
    print(x2000)
