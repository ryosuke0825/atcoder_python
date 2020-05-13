import collections

N = int(input())
A = collections.deque(list(map(int, input().split())))
A.appendleft(0)
A.append(0)

ac = []
for i in range(N+1):
    ac.append(abs(A[i]-A[i+1]))

travel_sum = sum(ac)
for i in range(N):
    # 訪れるのを取りやめた観光スポットの前後の移動金額を合計から引く
    ans = travel_sum-(ac[i]+ac[i+1])

    # 取りやめたことで発生する移動金額を加算する
    ans += abs(A[i]-A[i+2])
    print(ans)
