import math

n = int(input())
al = list(map(int, input().split()))

bug_cnt = 0
for a in al:
    if a != 0:
        bug_cnt += 1

print(math.ceil(sum(al)/bug_cnt))
