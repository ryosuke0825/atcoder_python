n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)

a = sum(l[::2])
b = sum(l[1::2])
print(a-b)
