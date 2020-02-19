m = int(input())
k = m*0.001

if k < 0.1:
    print("00")
elif k <= 5:
    ans = str(int(k*10))
    if len(ans) == 1:
        ans = "0"+ans
    print(ans)
elif 6 <= k <= 30:
    k += 50
    print(int(k))
elif 35 <= k <= 70:
    k = (k-30)/5+80
    print(int(k))
elif k > 70:
    print(89)
