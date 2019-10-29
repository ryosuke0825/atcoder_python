n = int(input())
d = list(map(int, input().split()))
d.sort()

min = d[n//2-1]
max = d[n//2]

print((max-(min+1))+1)
