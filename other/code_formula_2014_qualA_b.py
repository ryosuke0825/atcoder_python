a, b = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
ans1 = ['x', ' ', 'x', ' ', 'x', ' ', 'x']
ans2 = [' ', 'x', ' ', 'x', ' ', 'x']
ans3 = [' ', ' ', 'x', ' ', 'x']
ans4 = [' ', ' ', ' ', 'x']

for tmp in p:
    if tmp == 1:
        ans4[3] = '.'
    elif tmp == 2:
        ans3[2] = '.'
    elif tmp == 3:
        ans3[4] = '.'
    elif tmp == 4:
        ans2[1] = '.'
    elif tmp == 5:
        ans2[3] = '.'
    elif tmp == 6:
        ans2[5] = '.'
    elif tmp == 7:
        ans1[0] = '.'
    elif tmp == 8:
        ans1[2] = '.'
    elif tmp == 9:
        ans1[4] = '.'
    elif tmp == 0:
        ans1[6] = '.'

for tmp in q:
    if tmp == 1:
        ans4[3] = 'o'
    elif tmp == 2:
        ans3[2] = 'o'
    elif tmp == 3:
        ans3[4] = 'o'
    elif tmp == 4:
        ans2[1] = 'o'
    elif tmp == 5:
        ans2[3] = 'o'
    elif tmp == 6:
        ans2[5] = 'o'
    elif tmp == 7:
        ans1[0] = 'o'
    elif tmp == 8:
        ans1[2] = 'o'
    elif tmp == 9:
        ans1[4] = 'o'
    elif tmp == 0:
        ans1[6] = 'o'

print(''.join(ans1))
print(''.join(ans2))
print(''.join(ans3))
print(''.join(ans4))
