n = int(input())
al = list(map(int, input().split()))
al.sort()
print(al[-1]-al[0])
