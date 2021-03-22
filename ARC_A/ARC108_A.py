import math


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


S, P = map(int, input().split())
divisors = make_divisors(P)

ans = 'No'
for i in range(math.ceil(len(divisors)/2)):
    if divisors[i] + divisors[-1*(i+1)] == S:
        ans = 'Yes'
print(ans)
