s = input()
n = int(input())

list = []
for i in range(5):
    for j in range(5):
        list.append(s[i]+s[j])
list = sorted(list)

print(list[n-1])
