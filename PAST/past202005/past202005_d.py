N = int(input())
S = []
for _ in range(5):
    tmp = list(input())
    S.append(tmp)

ans = []
for i in range(1, N*4, 4):
    s1 = S[0][i:i+3]
    s2 = S[1][i:i+3]
    s3 = S[2][i:i+3]
    s4 = S[3][i:i+3]
    s5 = S[4][i:i+3]

    # .の数をカウントする
    cnt = s1.count('.') + s2.count('.') + s3.count('.') + \
        s4.count('.') + s5.count('.')

    # 確定するもの
    if cnt == 7:
        ans.append('1')
    elif cnt == 6:
        ans.append('4')
    elif cnt == 8:
        ans.append('7')
    elif cnt == 2:
        ans.append('8')
    elif cnt == 4:
        if s4[2] == '.':
            ans.append('2')
        elif s2[2] == '.':
            ans.append('5')
        else:
            ans.append('3')
    elif cnt == 3:
        if s3[1] == '.':
            ans.append('0')
        elif s2.count('.') == 1:
            ans.append('9')
        else:
            ans.append('6')
print(''.join(ans))
