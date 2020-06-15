N, K = map(int, input().split())
R = list(map(int, input().split()))

R.sort(reverse=True)
c = 0
for i in reversed(range(K)):
    c = (c+R[i])/2
print(c)
