n = int(input())
d = [0 for _ in range(n)]

for i in range(n):
    d[i] = int(input())

print(len(list(set(d))))
