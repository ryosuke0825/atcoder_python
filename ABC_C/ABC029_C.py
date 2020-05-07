import itertools

N = int(input())
abc = ['a', 'b', 'c']
As = list(itertools.product(abc, repeat=N))

for i in range(len(As)):
    print(''.join(As[i]))
