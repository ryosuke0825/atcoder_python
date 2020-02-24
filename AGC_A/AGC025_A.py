n = int(input())
if n%10==0:
    print(10)
    exit(0)
ans = pow(10,10)
for a in range(n+1):
    b = n-a
    tmp_ans = 0

    for sa in str(a):
        tmp_ans += int(sa)

    for sb in str(b):
        tmp_ans += int(sb)

    ans = min(ans, tmp_ans)
print(ans)
