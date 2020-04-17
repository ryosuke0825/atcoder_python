N = int(input())
A = [0]*(N+1)
for _ in range(N):
    a = int(input())
    A[a] += 1

x = 0
y = 0
for i in range(N+1):
    if A[i] == 0:
        x = i
    elif A[i] == 2:
        y = i

if x == y == 0:
    print('Correct')
else:
    print(y, x)
