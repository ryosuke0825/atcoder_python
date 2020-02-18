n = int(input())
al = []
for _ in range(n):
    al.append(int(input()))

uni_al = list(set(al))
uni_al.sort(reverse=True)
print(uni_al[1])
