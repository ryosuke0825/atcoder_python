E = list(map(int, input().split()))
B = int(input())
L = list(map(int, input().split()))

match = 0
for i in range(len(E)):
    if E[i] in L:
        match += 1

if match < 3:
    print(0)
elif match == 3:
    print(5)
elif match == 4:
    print(4)
elif match == 5:
    ans = 3
    for i in range(len(E)):
        if L[i] not in E:
            if L[i] == B:
                ans = 2
    print(ans)

elif match == 6:
    print(1)
