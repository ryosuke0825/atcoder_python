def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


n = int(input())
li = make_divisors(n)

ans = 10 ** 12
for i in li:
    j = n // i
    tmp_ans = (i-1)+(j-1)
    if tmp_ans < ans:
        ans = tmp_ans
print(ans)