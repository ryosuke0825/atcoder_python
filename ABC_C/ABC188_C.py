N = int(input())
A = list(map(int, input().split()))

member_num = 2**N
rate = min(max(A[:member_num//2]), max(A[member_num//2:]))
print(A.index(rate)+1)
