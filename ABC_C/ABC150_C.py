import itertools

n = int(input())
P = input().split()
Q = input().split()
p = ''.join(P)
q = ''.join(Q)
P.sort()
numbers = list(itertools.permutations(P))

numbers_str = []
for num in numbers:
    numbers_str.append(''.join(num))

print(abs(numbers_str.index(p)-numbers_str.index(q)))
