from collections import Counter

n = int(input())
A = list(map(int, input().split()))

C = Counter(A)
a_sum = 0
for i in C.values():
    a_sum += i*(i-1)//2

for a in A:
    k = C[a]
    print(a_sum-(k*(k-1)//2)+((k-1)*(k-2)//2))
