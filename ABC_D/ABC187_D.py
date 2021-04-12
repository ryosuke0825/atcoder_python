N = int(input())

AB = []
aoki_sum = 0
for i in range(N):
    A, B = map(int, input().split())
    AB.append([A+A+B, A, B])
    aoki_sum += A
AB.sort(reverse=True)

takahashi_sum = 0
for i in range(N):
    takahashi_sum += (AB[i][1]+AB[i][2])
    aoki_sum -= AB[i][1]
    if takahashi_sum > aoki_sum:
        print(i+1)
        break
