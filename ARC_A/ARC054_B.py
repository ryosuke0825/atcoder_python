# x年後の計算が終わる時間（最初のxは計算を始めるまでの時間）
def f(x):
    return x+P/2**(x/1.5)


P = float(input())

# サンプル3より最大入力値でも90年くらいと分かるためhighを100とする
high = 100
low = 0
while high-low > 0.000000001:
    mid_left = high/3+low*2/3
    mid_right = high*2/3+low/3
    if f(mid_left) >= f(mid_right):
        low = mid_left
    else:
        high = mid_right
print(f(high))
