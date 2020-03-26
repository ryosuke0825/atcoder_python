n = int(input())
A = list(map(int, input().split()))

abs_sum = 0
minus = 0
abs_list = []
for i in range(n):
    if A[i] < 0:
        minus += 1
    abs_list.append(abs(A[i]))
    abs_sum += abs_list[i]

if minus % 2 != 0:
    abs_sum -= min(abs_list)*2
print(abs_sum)
