w = []
for _ in range(10):
    w.append(int(input()))

k = []
for _ in range(10):
    k.append(int(input()))

w.sort(reverse=True)
k.sort(reverse=True)

print(sum(w[0:3]), sum(k[0:3]))
