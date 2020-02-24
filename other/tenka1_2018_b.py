a, b, k = map(int, input().split())
for i in range(1, k+1):
    # 高橋君の番
    if i % 2 == 1:
        if a % 2 == 1:
            a -= 1
        a, b = a//2, b+a//2
    # 青木君の番
    else:
        if b % 2 == 1:
            b -= 1
        a, b = a+b//2, b//2
print(a, b)
