import itertools

n = int(input())
P = input().split()
numbers = list(itertools.permutations(P))
P = ''.join(P)
Q = input()
Q = Q.replace(' ', '')

numbers_str = []
for num in numbers:
    numbers_str.append(''.join(num))
numbers_str.sort()
print(abs(numbers_str.index(P)-numbers_str.index(Q)))
