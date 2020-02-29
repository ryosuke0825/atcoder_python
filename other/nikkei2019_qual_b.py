n = int(input())
a = input()
b = input()
c = input()

cnt = 0
for i in range(n):
    s = [a[i], b[i], c[i]]
    cnt += (len(set(s))-1)
print(cnt)
