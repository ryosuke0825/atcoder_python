N = int(input())
L = list(map(int, input().split()))

max_len = max(L)
sum = 0
for i in L:
    sum += i
sum -= max_len

print("Yes" if sum > max_len else "No")
