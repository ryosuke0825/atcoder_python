def solve(arr, abcd, Q):
    ans = 0
    for i in range(Q):
        if arr[abcd[i][1]-1]-arr[abcd[i][0]-1] == abcd[i][2]:
            ans += abcd[i][3]
    return ans


N, M, Q = map(int, input().split())
abcd = []
for _ in range(Q):
    tmp = list(map(int, input().split()))
    abcd.append(tmp)

ans = 0
for i1 in range(1, M+1):
    for i2 in range(1, M+1):
        if i1 > i2:
            continue
        if N == 2:
            tmp = [i1, i2]
            tmp_ans = solve(tmp, abcd, Q)
            ans = max(tmp_ans, ans)

        for i3 in range(1, M+1):
            if i2 > i3:
                continue
            if N == 3:
                tmp = [i1, i2, i3]
                tmp_ans = solve(tmp, abcd, Q)
                ans = max(tmp_ans, ans)

            for i4 in range(1, M+1):
                if i3 > i4:
                    continue
                if N == 4:
                    tmp = [i1, i2, i3, i4]
                    tmp_ans = solve(tmp, abcd, Q)
                    ans = max(tmp_ans, ans)

                for i5 in range(1, M+1):
                    if i4 > i5:
                        continue
                    if N == 5:
                        tmp = [i1, i2, i3, i4, i5]
                        tmp_ans = solve(tmp, abcd, Q)
                        ans = max(tmp_ans, ans)

                    for i6 in range(1, M+1):
                        if i5 > i6:
                            continue
                        if N == 6:
                            tmp = [i1, i2, i3, i4, i5, i6]
                            tmp_ans = solve(tmp, abcd, Q)
                            ans = max(tmp_ans, ans)

                        for i7 in range(1, M+1):
                            if i6 > i7:
                                continue
                            if N == 7:
                                tmp = [i1, i2, i3, i4, i5, i6, i7]
                                tmp_ans = solve(tmp, abcd, Q)
                                ans = max(tmp_ans, ans)

                            for i8 in range(1, M+1):
                                if i7 > i8:
                                    continue
                                if N == 8:
                                    tmp = [i1, i2, i3, i4, i5, i6, i7, i8]
                                    tmp_ans = solve(tmp, abcd, Q)
                                    ans = max(tmp_ans, ans)

                                for i9 in range(1, M+1):
                                    if i8 > i9:
                                        continue
                                    if N == 9:
                                        tmp = [i1, i2, i3, i4,
                                               i5, i6, i7, i8, i9]
                                        tmp_ans = solve(tmp, abcd, Q)
                                        ans = max(tmp_ans, ans)

                                    for i10 in range(1, M+1):
                                        if i9 > i10:
                                            continue
                                        if N == 10:
                                            tmp = [i1, i2, i3, i4,
                                                   i5, i6, i7, i8, i9, i10]
                                            tmp_ans = solve(tmp, abcd, Q)
                                            ans = max(tmp_ans, ans)
print(ans)
