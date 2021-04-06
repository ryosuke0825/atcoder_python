N, M, Q = map(int, input().split())
answer = [[] * N for i in range(N)]
point = [N]*M

for _ in range(Q):
    q = list(map(int, input().split()))

    # クエリの種類毎に分岐する
    if q[0] == 1:
        # 誰かの現時点の点数を求めるクエリ
        ans = 0
        for m in answer[q[1]-1]:
            ans += point[m-1]
        print(ans)

    else:
        # 誰かが問題を解いた時のクエリ
        answer[q[1]-1].append(q[2])
        point[q[2]-1] -= 1
