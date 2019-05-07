X = int(input())

ans = 0
if X == 1:
    print(1)
else:
    for i in range(2, X+1):
        tmp = i
        tmp_ans = 0
        j = 2
        while tmp_ans <= X:
            tmp_ans = tmp ** j
            if tmp_ans <= X:
                ans = max(ans, tmp_ans)
            j += 1
    print(ans)
