n = int(input())

al = []
for _ in range(n):
    al.append(int(input()))

uni_al = list(set(al))
print(len(al)-len(uni_al))
