import sys
import collections


def input():
    return sys.stdin.readline()[:-1]


N = int(input())
A = []
for i in range(N):
    tmp = list(input())
    c = collections.Counter(tmp)
    A.append(c)

ans = ''
for i in range(N//2):
    for k in A[i].keys():
        if k in A[(i+1)*-1]:
            ans = ans+k
            break
    else:
        print(-1)
        exit(0)

if N % 2 == 1:
    tmp = ''
    for k in A[N//2].keys():
        tmp = k
        break

    ans = ans+tmp+ans[::-1]
else:
    ans = ans+ans[::-1]
print(ans)
