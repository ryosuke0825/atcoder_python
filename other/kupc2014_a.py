from itertools import permutations

a1, a2, a3, b1, b2, b3 = map(int, input().split())
A = [a1, a2, a3]
B = [b1, b2, b3]

ans = 600
for li in list(permutations(range(3))):
    ans = min(ans, abs(A[0]-B[li[0]])+abs(A[1]-B[li[1]])+abs(A[2]-B[li[2]]))
print(ans)
