def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


N = int(input())
divisor = make_divisors(N*2)

ans = 0
for i in divisor:
    tmp = 2*N/i
    if (tmp+1-i) % 2 == 0:
        ans += 1
print(ans)
