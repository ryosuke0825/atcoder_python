from math import ceil


N = int(input())
T = input()

# N=1の場合
if N == 1:
    if T == '0':
        print(10000000000)
    else:
        print(20000000000)
    exit(0)

# Sは'110'を結合した文字列。3文字ずつの繰り返し。
# '110'*len(T)/3を作る
x = ceil(len(T)/3)

pin = '110'*x
gu = '110'*(x+1)

if T in pin:
    print(10**10+1-x)
elif T in gu:
    print(10**10-x)
else:
    print(0)
