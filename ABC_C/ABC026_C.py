import sys


def input():
    return sys.stdin.readline()[:-1]


N = int(input())
B = [0]*N
salary = [1]*N
for i in range(1, N):
    B[i] = int(input())

MX = 10**18
for i in reversed(range(N)):
    if i+1 in B:
        # 部下がいる
        b_max = 0
        b_min = MX
        for j in range(N):
            if B[j] == i+1:
                b_max = max(b_max, salary[j])
                b_min = min(b_min, salary[j])

        salary[i] = b_max+b_min+1
print(salary[0])
