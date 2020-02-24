n = int(input())
al = list(map(int, input().split()))
al.sort(reverse=True)
print(sum(al[::2]))
