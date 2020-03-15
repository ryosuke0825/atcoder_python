n = int(input())

child = [0]*(n+1)
child[0] = 1
ad = 0

for i in range(1, n+1):
    if i >= 2:
        ad += child[i-2]
        child[i-2] = 0
    child[i] = ad

print(ad+sum(child))
