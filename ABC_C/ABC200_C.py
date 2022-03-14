N = int(input())
A = list(map(int, input().split()))

arr = [0]*200

for a in A:
    arr[a % 200] += 1

ans = 0
for a in arr:
    ans += (a*(a-1)//2)

print(ans)
