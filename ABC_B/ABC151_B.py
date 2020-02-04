n, k, m = map(int, input().split())
a_list = list(map(int, input().split()))

sum_score = sum(a_list)
goal_score = m*n

if sum_score >= goal_score:
    print(0)
else:
    need_score = goal_score-sum_score
    if k >= need_score:
        print(need_score)
    else:
        print(-1)
