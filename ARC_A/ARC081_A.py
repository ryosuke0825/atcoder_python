import collections

N = int(input())
A = list(map(int, input().split()))

CA = collections.Counter(A)

max1 = 0
max2 = 0
for item in CA.items():
    if item[1] >= 2 and item[0] > max1:
        if item[1] >= 4:
            max1 = item[0]
            max2 = item[0]
        else:
            max2 = max1
            max1 = item[0]
    elif item[1] >= 2 and item[0] > max2:
        max2 = item[0]
print(max1*max2)
