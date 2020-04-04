import collections

N = int(input())
A = map(int, input().split())
CA = collections.Counter(A)

ans = CA[0]+CA[1]+CA[2]
tmp = 0
for i in range(2, 10**5):
    tmp = CA[i-1]+CA[i]+CA[i+1]
    ans = max(tmp, ans)
print(ans)
